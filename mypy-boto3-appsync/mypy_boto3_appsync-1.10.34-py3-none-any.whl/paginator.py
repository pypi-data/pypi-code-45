"Main interface for appsync service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_appsync.type_defs import (
    ListApiKeysPaginatePaginationConfigTypeDef,
    ListApiKeysPaginateResponseTypeDef,
    ListDataSourcesPaginatePaginationConfigTypeDef,
    ListDataSourcesPaginateResponseTypeDef,
    ListFunctionsPaginatePaginationConfigTypeDef,
    ListFunctionsPaginateResponseTypeDef,
    ListGraphqlApisPaginatePaginationConfigTypeDef,
    ListGraphqlApisPaginateResponseTypeDef,
    ListResolversByFunctionPaginatePaginationConfigTypeDef,
    ListResolversByFunctionPaginateResponseTypeDef,
    ListResolversPaginatePaginationConfigTypeDef,
    ListResolversPaginateResponseTypeDef,
    ListTypesPaginatePaginationConfigTypeDef,
    ListTypesPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListApiKeysPaginator",
    "ListDataSourcesPaginator",
    "ListFunctionsPaginator",
    "ListGraphqlApisPaginator",
    "ListResolversPaginator",
    "ListResolversByFunctionPaginator",
    "ListTypesPaginator",
)


class ListApiKeysPaginator(Boto3Paginator):
    """
    Paginator for `list_api_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, apiId: str, PaginationConfig: ListApiKeysPaginatePaginationConfigTypeDef = None
    ) -> ListApiKeysPaginateResponseTypeDef:
        """
        [ListApiKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appsync.html#AppSync.Paginator.ListApiKeys.paginate)
        """


class ListDataSourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_data_sources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, apiId: str, PaginationConfig: ListDataSourcesPaginatePaginationConfigTypeDef = None
    ) -> ListDataSourcesPaginateResponseTypeDef:
        """
        [ListDataSources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appsync.html#AppSync.Paginator.ListDataSources.paginate)
        """


class ListFunctionsPaginator(Boto3Paginator):
    """
    Paginator for `list_functions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, apiId: str, PaginationConfig: ListFunctionsPaginatePaginationConfigTypeDef = None
    ) -> ListFunctionsPaginateResponseTypeDef:
        """
        [ListFunctions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appsync.html#AppSync.Paginator.ListFunctions.paginate)
        """


class ListGraphqlApisPaginator(Boto3Paginator):
    """
    Paginator for `list_graphql_apis`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListGraphqlApisPaginatePaginationConfigTypeDef = None
    ) -> ListGraphqlApisPaginateResponseTypeDef:
        """
        [ListGraphqlApis.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appsync.html#AppSync.Paginator.ListGraphqlApis.paginate)
        """


class ListResolversPaginator(Boto3Paginator):
    """
    Paginator for `list_resolvers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        apiId: str,
        typeName: str,
        PaginationConfig: ListResolversPaginatePaginationConfigTypeDef = None,
    ) -> ListResolversPaginateResponseTypeDef:
        """
        [ListResolvers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appsync.html#AppSync.Paginator.ListResolvers.paginate)
        """


class ListResolversByFunctionPaginator(Boto3Paginator):
    """
    Paginator for `list_resolvers_by_function`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        apiId: str,
        functionId: str,
        PaginationConfig: ListResolversByFunctionPaginatePaginationConfigTypeDef = None,
    ) -> ListResolversByFunctionPaginateResponseTypeDef:
        """
        [ListResolversByFunction.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appsync.html#AppSync.Paginator.ListResolversByFunction.paginate)
        """


class ListTypesPaginator(Boto3Paginator):
    """
    Paginator for `list_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        apiId: str,
        format: Literal["SDL", "JSON"],
        PaginationConfig: ListTypesPaginatePaginationConfigTypeDef = None,
    ) -> ListTypesPaginateResponseTypeDef:
        """
        [ListTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appsync.html#AppSync.Paginator.ListTypes.paginate)
        """
