"Main interface for cloudfront service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_cloudfront.type_defs import (
    DistributionDeployedWaitWaiterConfigTypeDef,
    InvalidationCompletedWaitWaiterConfigTypeDef,
    StreamingDistributionDeployedWaitWaiterConfigTypeDef,
)


__all__ = (
    "DistributionDeployedWaiter",
    "InvalidationCompletedWaiter",
    "StreamingDistributionDeployedWaiter",
)


class DistributionDeployedWaiter(Boto3Waiter):
    """
    Waiter for `distribution_deployed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, Id: str, WaiterConfig: DistributionDeployedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [distribution_deployed.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudfront.html#CloudFront.Waiter.distribution_deployed.wait)
        """


class InvalidationCompletedWaiter(Boto3Waiter):
    """
    Waiter for `invalidation_completed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DistributionId: str,
        Id: str,
        WaiterConfig: InvalidationCompletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [invalidation_completed.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudfront.html#CloudFront.Waiter.invalidation_completed.wait)
        """


class StreamingDistributionDeployedWaiter(Boto3Waiter):
    """
    Waiter for `streaming_distribution_deployed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, Id: str, WaiterConfig: StreamingDistributionDeployedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [streaming_distribution_deployed.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudfront.html#CloudFront.Waiter.streaming_distribution_deployed.wait)
        """
