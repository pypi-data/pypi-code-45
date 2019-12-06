"Main interface for datapipeline service"

from mypy_boto3_datapipeline.client import Client
from mypy_boto3_datapipeline.paginator import (
    DescribeObjectsPaginator,
    ListPipelinesPaginator,
    QueryObjectsPaginator,
)


__all__ = ("Client", "DescribeObjectsPaginator", "ListPipelinesPaginator", "QueryObjectsPaginator")
