"Main interface for redshift service Waiters"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_redshift.type_defs import (
    ClusterAvailableWaitWaiterConfigTypeDef,
    ClusterDeletedWaitWaiterConfigTypeDef,
    ClusterRestoredWaitWaiterConfigTypeDef,
    SnapshotAvailableWaitSortingEntitiesTypeDef,
    SnapshotAvailableWaitWaiterConfigTypeDef,
)


__all__ = (
    "ClusterAvailableWaiter",
    "ClusterDeletedWaiter",
    "ClusterRestoredWaiter",
    "SnapshotAvailableWaiter",
)


class ClusterAvailableWaiter(Boto3Waiter):
    """
    Waiter for `cluster_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        WaiterConfig: ClusterAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [cluster_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Waiter.cluster_available.wait)
        """


class ClusterDeletedWaiter(Boto3Waiter):
    """
    Waiter for `cluster_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        WaiterConfig: ClusterDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [cluster_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Waiter.cluster_deleted.wait)
        """


class ClusterRestoredWaiter(Boto3Waiter):
    """
    Waiter for `cluster_restored` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        WaiterConfig: ClusterRestoredWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [cluster_restored.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Waiter.cluster_restored.wait)
        """


class SnapshotAvailableWaiter(Boto3Waiter):
    """
    Waiter for `snapshot_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxRecords: int = None,
        Marker: str = None,
        OwnerAccount: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        ClusterExists: bool = None,
        SortingEntities: List[SnapshotAvailableWaitSortingEntitiesTypeDef] = None,
        WaiterConfig: SnapshotAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [snapshot_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Waiter.snapshot_available.wait)
        """
