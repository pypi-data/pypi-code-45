from typing import List

from version_control.models import ModelObjectVersion
from version_control.service import VersionControlManager


def process_version_control_storage(request_key: str) -> List[ModelObjectVersion]:
    """
    Task for processing temporary storage with data for recording versions of changed objects
    :param request_key: str, uuid of the current 'request' for search in temporary storage
    :return: List[ModelObjectVersion]
    """

    manager = VersionControlManager(request_key=request_key)
    return manager.create_version_from_storage()
