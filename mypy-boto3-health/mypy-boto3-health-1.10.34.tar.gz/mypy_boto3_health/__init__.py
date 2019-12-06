"Main interface for health service"

from mypy_boto3_health.client import Client
from mypy_boto3_health.paginator import (
    DescribeAffectedEntitiesPaginator,
    DescribeEventAggregatesPaginator,
    DescribeEventTypesPaginator,
    DescribeEventsPaginator,
)


__all__ = (
    "Client",
    "DescribeAffectedEntitiesPaginator",
    "DescribeEventAggregatesPaginator",
    "DescribeEventTypesPaginator",
    "DescribeEventsPaginator",
)
