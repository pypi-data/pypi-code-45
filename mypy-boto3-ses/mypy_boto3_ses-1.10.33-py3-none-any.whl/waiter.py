"Main interface for ses service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_ses.type_defs import IdentityExistsWaitWaiterConfigTypeDef


__all__ = ("IdentityExistsWaiter",)


class IdentityExistsWaiter(Boto3Waiter):
    """
    Waiter for `identity_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, Identities: List[str], WaiterConfig: IdentityExistsWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [identity_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ses.html#SES.Waiter.identity_exists.wait)
        """
