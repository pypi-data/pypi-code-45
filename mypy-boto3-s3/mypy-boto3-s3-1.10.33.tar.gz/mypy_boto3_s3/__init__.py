"Main interface for s3 service"

from mypy_boto3_s3.client import Client
from mypy_boto3_s3.paginator import (
    ListMultipartUploadsPaginator,
    ListObjectVersionsPaginator,
    ListObjectsPaginator,
    ListObjectsV2Paginator,
    ListPartsPaginator,
)
from mypy_boto3_s3.service_resource import ServiceResource
from mypy_boto3_s3.waiter import (
    BucketExistsWaiter,
    BucketNotExistsWaiter,
    ObjectExistsWaiter,
    ObjectNotExistsWaiter,
)


__all__ = (
    "Client",
    "ServiceResource",
    "BucketExistsWaiter",
    "BucketNotExistsWaiter",
    "ObjectExistsWaiter",
    "ObjectNotExistsWaiter",
    "ListMultipartUploadsPaginator",
    "ListObjectVersionsPaginator",
    "ListObjectsPaginator",
    "ListObjectsV2Paginator",
    "ListPartsPaginator",
)
