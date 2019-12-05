"Main interface for rds service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_rds.type_defs import (
    DbClusterSnapshotAvailableWaitFiltersTypeDef,
    DbClusterSnapshotAvailableWaitWaiterConfigTypeDef,
    DbClusterSnapshotDeletedWaitFiltersTypeDef,
    DbClusterSnapshotDeletedWaitWaiterConfigTypeDef,
    DbInstanceAvailableWaitFiltersTypeDef,
    DbInstanceAvailableWaitWaiterConfigTypeDef,
    DbInstanceDeletedWaitFiltersTypeDef,
    DbInstanceDeletedWaitWaiterConfigTypeDef,
    DbSnapshotAvailableWaitFiltersTypeDef,
    DbSnapshotAvailableWaitWaiterConfigTypeDef,
    DbSnapshotCompletedWaitFiltersTypeDef,
    DbSnapshotCompletedWaitWaiterConfigTypeDef,
    DbSnapshotDeletedWaitFiltersTypeDef,
    DbSnapshotDeletedWaitWaiterConfigTypeDef,
)


__all__ = (
    "DBClusterSnapshotAvailableWaiter",
    "DBClusterSnapshotDeletedWaiter",
    "DBInstanceAvailableWaiter",
    "DBInstanceDeletedWaiter",
    "DBSnapshotAvailableWaiter",
    "DBSnapshotCompletedWaiter",
    "DBSnapshotDeletedWaiter",
)


class DBClusterSnapshotAvailableWaiter(Boto3Waiter):
    """
    Waiter for `db_cluster_snapshot_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[DbClusterSnapshotAvailableWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        WaiterConfig: DbClusterSnapshotAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [db_cluster_snapshot_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Waiter.db_cluster_snapshot_available.wait)
        """


class DBClusterSnapshotDeletedWaiter(Boto3Waiter):
    """
    Waiter for `db_cluster_snapshot_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[DbClusterSnapshotDeletedWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        WaiterConfig: DbClusterSnapshotDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [db_cluster_snapshot_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Waiter.db_cluster_snapshot_deleted.wait)
        """


class DBInstanceAvailableWaiter(Boto3Waiter):
    """
    Waiter for `db_instance_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[DbInstanceAvailableWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: DbInstanceAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [db_instance_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Waiter.db_instance_available.wait)
        """


class DBInstanceDeletedWaiter(Boto3Waiter):
    """
    Waiter for `db_instance_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[DbInstanceDeletedWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: DbInstanceDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [db_instance_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Waiter.db_instance_deleted.wait)
        """


class DBSnapshotAvailableWaiter(Boto3Waiter):
    """
    Waiter for `db_snapshot_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[DbSnapshotAvailableWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: DbSnapshotAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [db_snapshot_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Waiter.db_snapshot_available.wait)
        """


class DBSnapshotCompletedWaiter(Boto3Waiter):
    """
    Waiter for `db_snapshot_completed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[DbSnapshotCompletedWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: DbSnapshotCompletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [db_snapshot_completed.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Waiter.db_snapshot_completed.wait)
        """


class DBSnapshotDeletedWaiter(Boto3Waiter):
    """
    Waiter for `db_snapshot_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[DbSnapshotDeletedWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: DbSnapshotDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [db_snapshot_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Waiter.db_snapshot_deleted.wait)
        """
