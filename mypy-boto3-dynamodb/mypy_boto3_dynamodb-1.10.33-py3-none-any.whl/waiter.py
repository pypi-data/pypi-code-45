"Main interface for dynamodb service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_dynamodb.type_defs import (
    TableExistsWaitWaiterConfigTypeDef,
    TableNotExistsWaitWaiterConfigTypeDef,
)


__all__ = ("TableExistsWaiter", "TableNotExistsWaiter")


class TableExistsWaiter(Boto3Waiter):
    """
    Waiter for `table_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, TableName: str, WaiterConfig: TableExistsWaitWaiterConfigTypeDef = None) -> None:
        """
        [table_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dynamodb.html#DynamoDB.Waiter.table_exists.wait)
        """


class TableNotExistsWaiter(Boto3Waiter):
    """
    Waiter for `table_not_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, TableName: str, WaiterConfig: TableNotExistsWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [table_not_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dynamodb.html#DynamoDB.Waiter.table_not_exists.wait)
        """
