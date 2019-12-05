"Main interface for s3 service Waiters"
from __future__ import annotations

from datetime import datetime
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_s3.type_defs import (
    BucketExistsWaitWaiterConfigTypeDef,
    BucketNotExistsWaitWaiterConfigTypeDef,
    ObjectExistsWaitWaiterConfigTypeDef,
    ObjectNotExistsWaitWaiterConfigTypeDef,
)


__all__ = (
    "BucketExistsWaiter",
    "BucketNotExistsWaiter",
    "ObjectExistsWaiter",
    "ObjectNotExistsWaiter",
)


class BucketExistsWaiter(Boto3Waiter):
    """
    Waiter for `bucket_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, Bucket: str, WaiterConfig: BucketExistsWaitWaiterConfigTypeDef = None) -> None:
        """
        [bucket_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/s3.html#S3.Waiter.bucket_exists.wait)
        """


class BucketNotExistsWaiter(Boto3Waiter):
    """
    Waiter for `bucket_not_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, Bucket: str, WaiterConfig: BucketNotExistsWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [bucket_not_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/s3.html#S3.Waiter.bucket_not_exists.wait)
        """


class ObjectExistsWaiter(Boto3Waiter):
    """
    Waiter for `object_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Bucket: str,
        Key: str,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: str = None,
        PartNumber: int = None,
        WaiterConfig: ObjectExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [object_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/s3.html#S3.Waiter.object_exists.wait)
        """


class ObjectNotExistsWaiter(Boto3Waiter):
    """
    Waiter for `object_not_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Bucket: str,
        Key: str,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: str = None,
        PartNumber: int = None,
        WaiterConfig: ObjectNotExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [object_not_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/s3.html#S3.Waiter.object_not_exists.wait)
        """
