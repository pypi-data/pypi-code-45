"Main interface for ecs service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_ecs.type_defs import (
    ServicesInactiveWaitWaiterConfigTypeDef,
    ServicesStableWaitWaiterConfigTypeDef,
    TasksRunningWaitWaiterConfigTypeDef,
    TasksStoppedWaitWaiterConfigTypeDef,
)


__all__ = (
    "ServicesInactiveWaiter",
    "ServicesStableWaiter",
    "TasksRunningWaiter",
    "TasksStoppedWaiter",
)


class ServicesInactiveWaiter(Boto3Waiter):
    """
    Waiter for `services_inactive` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        services: List[str],
        cluster: str = None,
        include: List[str] = None,
        WaiterConfig: ServicesInactiveWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [services_inactive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ecs.html#ECS.Waiter.services_inactive.wait)
        """


class ServicesStableWaiter(Boto3Waiter):
    """
    Waiter for `services_stable` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        services: List[str],
        cluster: str = None,
        include: List[str] = None,
        WaiterConfig: ServicesStableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [services_stable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ecs.html#ECS.Waiter.services_stable.wait)
        """


class TasksRunningWaiter(Boto3Waiter):
    """
    Waiter for `tasks_running` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        tasks: List[str],
        cluster: str = None,
        include: List[str] = None,
        WaiterConfig: TasksRunningWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [tasks_running.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ecs.html#ECS.Waiter.tasks_running.wait)
        """


class TasksStoppedWaiter(Boto3Waiter):
    """
    Waiter for `tasks_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        tasks: List[str],
        cluster: str = None,
        include: List[str] = None,
        WaiterConfig: TasksStoppedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [tasks_stopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ecs.html#ECS.Waiter.tasks_stopped.wait)
        """
