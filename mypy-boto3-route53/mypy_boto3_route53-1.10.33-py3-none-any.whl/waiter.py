"Main interface for route53 service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_route53.type_defs import ResourceRecordSetsChangedWaitWaiterConfigTypeDef


__all__ = ("ResourceRecordSetsChangedWaiter",)


class ResourceRecordSetsChangedWaiter(Boto3Waiter):
    """
    Waiter for `resource_record_sets_changed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, Id: str, WaiterConfig: ResourceRecordSetsChangedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [resource_record_sets_changed.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53.html#Route53.Waiter.resource_record_sets_changed.wait)
        """
