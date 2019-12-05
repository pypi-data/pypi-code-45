"Main interface for discovery service"

from mypy_boto3_discovery.client import Client
from mypy_boto3_discovery.paginator import (
    DescribeAgentsPaginator,
    DescribeContinuousExportsPaginator,
    DescribeExportConfigurationsPaginator,
    DescribeExportTasksPaginator,
    DescribeTagsPaginator,
    ListConfigurationsPaginator,
)


__all__ = (
    "Client",
    "DescribeAgentsPaginator",
    "DescribeContinuousExportsPaginator",
    "DescribeExportConfigurationsPaginator",
    "DescribeExportTasksPaginator",
    "DescribeTagsPaginator",
    "ListConfigurationsPaginator",
)
