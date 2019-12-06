from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from django_logic.exceptions import TransitionNotAllowed


class ViewSetActionMixin(object):
    def perform_action(self):
        action_name = kwargs.get('action_name')

        if self.proxy_model is None:
            raise FSMException('Please, provide proxy_model')

        if not action_name:
            return Response(status=HTTP_400_BAD_REQUEST, data={
                "errors": ["Action not specified".format()]
            })

        instance = self.proxy_model.objects.get(pk=self.get_object().pk)

        if action_name not in get_available_user_transitions(instance, self.action_field, request.user):
            return Response(status=HTTP_400_BAD_REQUEST, data={
                "errors": ["Action '{}' is not allowed".format(action_name.capitalize())]
            })

        with transaction.atomic():
            instance = self.proxy_model.objects.select_for_update().get(pk=instance.pk)
            try:  # with provided parameters
                method_to_call = getattr(instance, action_name)
                method_to_call(**request.data)
            except TypeError as er:
                raise ValidationError(er)


            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

    def save_and_perform_action(self, request, action_name, pk=None):
        """
        This method allows to save the serialized data and perform a transition within one transaction

        :param request: HttpRequest
        :param action_name: str
        :param pk: int or None
        :return: Model Instance
        """
        # TODO: add hints
        try:
            with transaction.atomic():
                if pk is None:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    self.perform_create(serializer)
                    instance = serializer.instance
                else:
                    instance = self.get_object()
                    serializer = self.get_serializer(instance, data=request.data)
                    serializer.is_valid(raise_exception=True)
                    self.perform_update(serializer)

                instance = self.proxy_model.objects.select_for_update().get(pk=instance.pk)

                method_to_call = getattr(instance, action_name)
                method_to_call()
                instance.save()
        except TransitionNotAllowed:
            return Response(status=HTTP_400_BAD_REQUEST, data={
                "errors": ["Action '{}' is not allowed".format(action_name.capitalize())]
            })
        else:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
