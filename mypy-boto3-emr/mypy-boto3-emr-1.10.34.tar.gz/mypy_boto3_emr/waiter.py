"Main interface for emr service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_emr.type_defs import (
    ClusterRunningWaitWaiterConfigTypeDef,
    ClusterTerminatedWaitWaiterConfigTypeDef,
    StepCompleteWaitWaiterConfigTypeDef,
)


__all__ = ("ClusterRunningWaiter", "ClusterTerminatedWaiter", "StepCompleteWaiter")


class ClusterRunningWaiter(Boto3Waiter):
    """
    Waiter for `cluster_running` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, ClusterId: str, WaiterConfig: ClusterRunningWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [cluster_running.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/emr.html#EMR.Waiter.cluster_running.wait)
        """


class ClusterTerminatedWaiter(Boto3Waiter):
    """
    Waiter for `cluster_terminated` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, ClusterId: str, WaiterConfig: ClusterTerminatedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [cluster_terminated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/emr.html#EMR.Waiter.cluster_terminated.wait)
        """


class StepCompleteWaiter(Boto3Waiter):
    """
    Waiter for `step_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, ClusterId: str, StepId: str, WaiterConfig: StepCompleteWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [step_complete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/emr.html#EMR.Waiter.step_complete.wait)
        """
