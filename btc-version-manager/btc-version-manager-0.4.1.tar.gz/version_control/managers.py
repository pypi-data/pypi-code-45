from django.db import models


class ModelObjectVersionGroupQuerySet(models.QuerySet):
    """
    A queryset-manager for "ModelObjectVersionGroup" model
    """

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs).prefetch_related('model_object_versions')


class ModelObjectVersionQuerySet(models.QuerySet):
    """
    A queryset-manager for "ModelObjectVersion" model
    """

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs).select_related('group')
