from django.db import models


class ModelObjectVersionGroupQuerySet(models.QuerySet):
    """
    'ModelObjectVersionGroup' querySet-manager
    """

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs).prefetch_related('model_object_versions')


class ModelObjectVersionQuerySet(models.QuerySet):
    """
    'ModelObjectVersion' querySet-manager
    """

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs).select_related('group')
