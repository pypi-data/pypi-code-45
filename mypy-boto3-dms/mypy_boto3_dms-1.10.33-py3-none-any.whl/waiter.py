"Main interface for dms service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_dms.type_defs import (
    EndpointDeletedWaitFiltersTypeDef,
    EndpointDeletedWaitWaiterConfigTypeDef,
    ReplicationInstanceAvailableWaitFiltersTypeDef,
    ReplicationInstanceAvailableWaitWaiterConfigTypeDef,
    ReplicationInstanceDeletedWaitFiltersTypeDef,
    ReplicationInstanceDeletedWaitWaiterConfigTypeDef,
    ReplicationTaskDeletedWaitFiltersTypeDef,
    ReplicationTaskDeletedWaitWaiterConfigTypeDef,
    ReplicationTaskReadyWaitFiltersTypeDef,
    ReplicationTaskReadyWaitWaiterConfigTypeDef,
    ReplicationTaskRunningWaitFiltersTypeDef,
    ReplicationTaskRunningWaitWaiterConfigTypeDef,
    ReplicationTaskStoppedWaitFiltersTypeDef,
    ReplicationTaskStoppedWaitWaiterConfigTypeDef,
    TestConnectionSucceedsWaitFiltersTypeDef,
    TestConnectionSucceedsWaitWaiterConfigTypeDef,
)


__all__ = (
    "EndpointDeletedWaiter",
    "ReplicationInstanceAvailableWaiter",
    "ReplicationInstanceDeletedWaiter",
    "ReplicationTaskDeletedWaiter",
    "ReplicationTaskReadyWaiter",
    "ReplicationTaskRunningWaiter",
    "ReplicationTaskStoppedWaiter",
    "TestConnectionSucceedsWaiter",
)


class EndpointDeletedWaiter(Boto3Waiter):
    """
    Waiter for `endpoint_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[EndpointDeletedWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: EndpointDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [endpoint_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dms.html#DatabaseMigrationService.Waiter.endpoint_deleted.wait)
        """


class ReplicationInstanceAvailableWaiter(Boto3Waiter):
    """
    Waiter for `replication_instance_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[ReplicationInstanceAvailableWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: ReplicationInstanceAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [replication_instance_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dms.html#DatabaseMigrationService.Waiter.replication_instance_available.wait)
        """


class ReplicationInstanceDeletedWaiter(Boto3Waiter):
    """
    Waiter for `replication_instance_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[ReplicationInstanceDeletedWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: ReplicationInstanceDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [replication_instance_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dms.html#DatabaseMigrationService.Waiter.replication_instance_deleted.wait)
        """


class ReplicationTaskDeletedWaiter(Boto3Waiter):
    """
    Waiter for `replication_task_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[ReplicationTaskDeletedWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: ReplicationTaskDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [replication_task_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dms.html#DatabaseMigrationService.Waiter.replication_task_deleted.wait)
        """


class ReplicationTaskReadyWaiter(Boto3Waiter):
    """
    Waiter for `replication_task_ready` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[ReplicationTaskReadyWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: ReplicationTaskReadyWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [replication_task_ready.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dms.html#DatabaseMigrationService.Waiter.replication_task_ready.wait)
        """


class ReplicationTaskRunningWaiter(Boto3Waiter):
    """
    Waiter for `replication_task_running` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[ReplicationTaskRunningWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: ReplicationTaskRunningWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [replication_task_running.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dms.html#DatabaseMigrationService.Waiter.replication_task_running.wait)
        """


class ReplicationTaskStoppedWaiter(Boto3Waiter):
    """
    Waiter for `replication_task_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[ReplicationTaskStoppedWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: ReplicationTaskStoppedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [replication_task_stopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dms.html#DatabaseMigrationService.Waiter.replication_task_stopped.wait)
        """


class TestConnectionSucceedsWaiter(Boto3Waiter):
    """
    Waiter for `test_connection_succeeds` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[TestConnectionSucceedsWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: TestConnectionSucceedsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [test_connection_succeeds.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dms.html#DatabaseMigrationService.Waiter.test_connection_succeeds.wait)
        """
