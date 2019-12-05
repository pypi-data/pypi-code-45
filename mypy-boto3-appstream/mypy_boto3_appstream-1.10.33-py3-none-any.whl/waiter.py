"Main interface for appstream service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_appstream.type_defs import (
    FleetStartedWaitWaiterConfigTypeDef,
    FleetStoppedWaitWaiterConfigTypeDef,
)


__all__ = ("FleetStartedWaiter", "FleetStoppedWaiter")


class FleetStartedWaiter(Boto3Waiter):
    """
    Waiter for `fleet_started` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Names: List[str] = None,
        NextToken: str = None,
        WaiterConfig: FleetStartedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [fleet_started.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Waiter.fleet_started.wait)
        """


class FleetStoppedWaiter(Boto3Waiter):
    """
    Waiter for `fleet_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Names: List[str] = None,
        NextToken: str = None,
        WaiterConfig: FleetStoppedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [fleet_stopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Waiter.fleet_stopped.wait)
        """
