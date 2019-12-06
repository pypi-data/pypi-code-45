"Main interface for dynamodb service"

from mypy_boto3_dynamodb.client import Client
from mypy_boto3_dynamodb.paginator import (
    ListBackupsPaginator,
    ListTablesPaginator,
    ListTagsOfResourcePaginator,
    QueryPaginator,
    ScanPaginator,
)
from mypy_boto3_dynamodb.service_resource import ServiceResource
from mypy_boto3_dynamodb.waiter import TableExistsWaiter, TableNotExistsWaiter


__all__ = (
    "Client",
    "ServiceResource",
    "TableExistsWaiter",
    "TableNotExistsWaiter",
    "ListBackupsPaginator",
    "ListTablesPaginator",
    "ListTagsOfResourcePaginator",
    "QueryPaginator",
    "ScanPaginator",
)
