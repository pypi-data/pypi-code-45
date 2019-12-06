"Main interface for docdb service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_docdb.type_defs import (
    DbInstanceAvailableWaitFiltersTypeDef,
    DbInstanceAvailableWaitWaiterConfigTypeDef,
    DbInstanceDeletedWaitFiltersTypeDef,
    DbInstanceDeletedWaitWaiterConfigTypeDef,
)


__all__ = ("DBInstanceAvailableWaiter", "DBInstanceDeletedWaiter")


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
        [db_instance_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/docdb.html#DocDB.Waiter.db_instance_available.wait)
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
        [db_instance_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/docdb.html#DocDB.Waiter.db_instance_deleted.wait)
        """
