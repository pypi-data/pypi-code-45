"Main interface for kinesis service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_kinesis.type_defs import (
    StreamExistsWaitWaiterConfigTypeDef,
    StreamNotExistsWaitWaiterConfigTypeDef,
)


__all__ = ("StreamExistsWaiter", "StreamNotExistsWaiter")


class StreamExistsWaiter(Boto3Waiter):
    """
    Waiter for `stream_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StreamName: str,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        WaiterConfig: StreamExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [stream_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/kinesis.html#Kinesis.Waiter.stream_exists.wait)
        """


class StreamNotExistsWaiter(Boto3Waiter):
    """
    Waiter for `stream_not_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StreamName: str,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        WaiterConfig: StreamNotExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [stream_not_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/kinesis.html#Kinesis.Waiter.stream_not_exists.wait)
        """
