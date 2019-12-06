"Main interface for resource-groups service"

from mypy_boto3_resource_groups.client import Client
from mypy_boto3_resource_groups.paginator import (
    ListGroupResourcesPaginator,
    ListGroupsPaginator,
    SearchResourcesPaginator,
)


__all__ = (
    "Client",
    "ListGroupResourcesPaginator",
    "ListGroupsPaginator",
    "SearchResourcesPaginator",
)
