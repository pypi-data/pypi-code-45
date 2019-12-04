from django.core.signals import request_finished
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from version_control.collections import ModelObjectChangeType
from version_control.models import AbstractVersionControl
from version_control.service import VersionControlManager
from version_control.tasks import process_version_control_storage


@receiver(pre_delete)
def handle_version_control_on_obj_delete(sender, instance, **kwargs):
    """
    Function for processing a signal to delete an object (instead of the model delete () method for tracking
    cascading delete)
    """

    if issubclass(sender, AbstractVersionControl):
        instance.handle_version(version_change_type=ModelObjectChangeType.OBJECT_DELETED)


@receiver(request_finished)
def handle_version_control_on_request_finished(sender, **kwargs):
    """
    Function that process 'request_finished' signal to start recording versions from temporary storage
    'VersionControlTemporaryStorage'.
    Processing through celery is possible.
    """

    manager = VersionControlManager()
    if manager.request_key:
        process_version_control_storage(manager.request_key)
