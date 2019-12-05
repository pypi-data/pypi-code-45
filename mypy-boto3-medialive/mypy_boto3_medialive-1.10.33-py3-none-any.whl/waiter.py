"Main interface for medialive service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_medialive.type_defs import (
    ChannelCreatedWaitWaiterConfigTypeDef,
    ChannelDeletedWaitWaiterConfigTypeDef,
    ChannelRunningWaitWaiterConfigTypeDef,
    ChannelStoppedWaitWaiterConfigTypeDef,
    MultiplexCreatedWaitWaiterConfigTypeDef,
    MultiplexDeletedWaitWaiterConfigTypeDef,
    MultiplexRunningWaitWaiterConfigTypeDef,
    MultiplexStoppedWaitWaiterConfigTypeDef,
)


__all__ = (
    "ChannelCreatedWaiter",
    "ChannelDeletedWaiter",
    "ChannelRunningWaiter",
    "ChannelStoppedWaiter",
    "MultiplexCreatedWaiter",
    "MultiplexDeletedWaiter",
    "MultiplexRunningWaiter",
    "MultiplexStoppedWaiter",
)


class ChannelCreatedWaiter(Boto3Waiter):
    """
    Waiter for `channel_created` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, ChannelId: str, WaiterConfig: ChannelCreatedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [channel_created.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Waiter.channel_created.wait)
        """


class ChannelDeletedWaiter(Boto3Waiter):
    """
    Waiter for `channel_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, ChannelId: str, WaiterConfig: ChannelDeletedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [channel_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Waiter.channel_deleted.wait)
        """


class ChannelRunningWaiter(Boto3Waiter):
    """
    Waiter for `channel_running` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, ChannelId: str, WaiterConfig: ChannelRunningWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [channel_running.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Waiter.channel_running.wait)
        """


class ChannelStoppedWaiter(Boto3Waiter):
    """
    Waiter for `channel_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, ChannelId: str, WaiterConfig: ChannelStoppedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [channel_stopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Waiter.channel_stopped.wait)
        """


class MultiplexCreatedWaiter(Boto3Waiter):
    """
    Waiter for `multiplex_created` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, MultiplexId: str, WaiterConfig: MultiplexCreatedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [multiplex_created.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Waiter.multiplex_created.wait)
        """


class MultiplexDeletedWaiter(Boto3Waiter):
    """
    Waiter for `multiplex_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, MultiplexId: str, WaiterConfig: MultiplexDeletedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [multiplex_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Waiter.multiplex_deleted.wait)
        """


class MultiplexRunningWaiter(Boto3Waiter):
    """
    Waiter for `multiplex_running` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, MultiplexId: str, WaiterConfig: MultiplexRunningWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [multiplex_running.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Waiter.multiplex_running.wait)
        """


class MultiplexStoppedWaiter(Boto3Waiter):
    """
    Waiter for `multiplex_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, MultiplexId: str, WaiterConfig: MultiplexStoppedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [multiplex_stopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Waiter.multiplex_stopped.wait)
        """
