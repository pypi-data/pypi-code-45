"Main interface for storagegateway service"

from mypy_boto3_storagegateway.client import Client
from mypy_boto3_storagegateway.paginator import (
    DescribeTapeArchivesPaginator,
    DescribeTapeRecoveryPointsPaginator,
    DescribeTapesPaginator,
    DescribeVTLDevicesPaginator,
    ListFileSharesPaginator,
    ListGatewaysPaginator,
    ListTagsForResourcePaginator,
    ListTapesPaginator,
    ListVolumesPaginator,
)


__all__ = (
    "Client",
    "DescribeTapeArchivesPaginator",
    "DescribeTapeRecoveryPointsPaginator",
    "DescribeTapesPaginator",
    "DescribeVTLDevicesPaginator",
    "ListFileSharesPaginator",
    "ListGatewaysPaginator",
    "ListTagsForResourcePaginator",
    "ListTapesPaginator",
    "ListVolumesPaginator",
)
