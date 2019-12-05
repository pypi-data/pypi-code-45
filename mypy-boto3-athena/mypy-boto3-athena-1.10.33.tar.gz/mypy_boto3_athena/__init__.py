"Main interface for athena service"

from mypy_boto3_athena.client import Client
from mypy_boto3_athena.paginator import (
    GetQueryResultsPaginator,
    ListNamedQueriesPaginator,
    ListQueryExecutionsPaginator,
)


__all__ = (
    "Client",
    "GetQueryResultsPaginator",
    "ListNamedQueriesPaginator",
    "ListQueryExecutionsPaginator",
)
