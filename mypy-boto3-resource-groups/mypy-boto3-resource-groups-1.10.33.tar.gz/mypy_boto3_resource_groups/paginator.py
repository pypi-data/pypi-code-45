"Main interface for resource-groups service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_resource_groups.type_defs import (
    ListGroupResourcesPaginateFiltersTypeDef,
    ListGroupResourcesPaginatePaginationConfigTypeDef,
    ListGroupResourcesPaginateResponseTypeDef,
    ListGroupsPaginateFiltersTypeDef,
    ListGroupsPaginatePaginationConfigTypeDef,
    ListGroupsPaginateResponseTypeDef,
    SearchResourcesPaginatePaginationConfigTypeDef,
    SearchResourcesPaginateResourceQueryTypeDef,
    SearchResourcesPaginateResponseTypeDef,
)


__all__ = ("ListGroupResourcesPaginator", "ListGroupsPaginator", "SearchResourcesPaginator")


class ListGroupResourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_group_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GroupName: str,
        Filters: List[ListGroupResourcesPaginateFiltersTypeDef] = None,
        PaginationConfig: ListGroupResourcesPaginatePaginationConfigTypeDef = None,
    ) -> ListGroupResourcesPaginateResponseTypeDef:
        """
        [ListGroupResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroupResources.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListGroupsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListGroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListGroupsPaginateResponseTypeDef:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroups.paginate)
        """


class SearchResourcesPaginator(Boto3Paginator):
    """
    Paginator for `search_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceQuery: SearchResourcesPaginateResourceQueryTypeDef,
        PaginationConfig: SearchResourcesPaginatePaginationConfigTypeDef = None,
    ) -> SearchResourcesPaginateResponseTypeDef:
        """
        [SearchResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Paginator.SearchResources.paginate)
        """
