"Main interface for athena service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_athena.type_defs import (
    GetQueryResultsPaginatePaginationConfigTypeDef,
    GetQueryResultsPaginateResponseTypeDef,
    ListNamedQueriesPaginatePaginationConfigTypeDef,
    ListNamedQueriesPaginateResponseTypeDef,
    ListQueryExecutionsPaginatePaginationConfigTypeDef,
    ListQueryExecutionsPaginateResponseTypeDef,
)


__all__ = ("GetQueryResultsPaginator", "ListNamedQueriesPaginator", "ListQueryExecutionsPaginator")


class GetQueryResultsPaginator(Boto3Paginator):
    """
    Paginator for `get_query_results`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        QueryExecutionId: str,
        PaginationConfig: GetQueryResultsPaginatePaginationConfigTypeDef = None,
    ) -> GetQueryResultsPaginateResponseTypeDef:
        """
        [GetQueryResults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/athena.html#Athena.Paginator.GetQueryResults.paginate)
        """


class ListNamedQueriesPaginator(Boto3Paginator):
    """
    Paginator for `list_named_queries`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WorkGroup: str = None,
        PaginationConfig: ListNamedQueriesPaginatePaginationConfigTypeDef = None,
    ) -> ListNamedQueriesPaginateResponseTypeDef:
        """
        [ListNamedQueries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/athena.html#Athena.Paginator.ListNamedQueries.paginate)
        """


class ListQueryExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `list_query_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WorkGroup: str = None,
        PaginationConfig: ListQueryExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> ListQueryExecutionsPaginateResponseTypeDef:
        """
        [ListQueryExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/athena.html#Athena.Paginator.ListQueryExecutions.paginate)
        """
