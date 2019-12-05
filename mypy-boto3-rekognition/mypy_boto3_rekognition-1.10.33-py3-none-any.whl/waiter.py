"Main interface for rekognition service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_rekognition.type_defs import (
    ProjectVersionRunningWaitWaiterConfigTypeDef,
    ProjectVersionTrainingCompletedWaitWaiterConfigTypeDef,
)


__all__ = ("ProjectVersionRunningWaiter", "ProjectVersionTrainingCompletedWaiter")


class ProjectVersionRunningWaiter(Boto3Waiter):
    """
    Waiter for `project_version_running` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: ProjectVersionRunningWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [project_version_running.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rekognition.html#Rekognition.Waiter.project_version_running.wait)
        """


class ProjectVersionTrainingCompletedWaiter(Boto3Waiter):
    """
    Waiter for `project_version_training_completed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: ProjectVersionTrainingCompletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [project_version_training_completed.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rekognition.html#Rekognition.Waiter.project_version_training_completed.wait)
        """
