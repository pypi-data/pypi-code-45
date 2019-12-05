"Main interface for cloudwatch service Waiters"
from __future__ import annotations

import sys
from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_cloudwatch.type_defs import AlarmExistsWaitWaiterConfigTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AlarmExistsWaiter",)


class AlarmExistsWaiter(Boto3Waiter):
    """
    Waiter for `alarm_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        StateValue: Literal["OK", "ALARM", "INSUFFICIENT_DATA"] = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: AlarmExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [alarm_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudwatch.html#CloudWatch.Waiter.alarm_exists.wait)
        """
