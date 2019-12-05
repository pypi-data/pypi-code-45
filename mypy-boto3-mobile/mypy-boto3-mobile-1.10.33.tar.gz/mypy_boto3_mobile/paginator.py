"Main interface for mobile service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mobile.type_defs import (
    ListBundlesPaginatePaginationConfigTypeDef,
    ListBundlesPaginateResponseTypeDef,
    ListProjectsPaginatePaginationConfigTypeDef,
    ListProjectsPaginateResponseTypeDef,
)


__all__ = ("ListBundlesPaginator", "ListProjectsPaginator")


class ListBundlesPaginator(Boto3Paginator):
    """
    Paginator for `list_bundles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListBundlesPaginatePaginationConfigTypeDef = None
    ) -> ListBundlesPaginateResponseTypeDef:
        """
        [ListBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Paginator.ListBundles.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    Paginator for `list_projects`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListProjectsPaginatePaginationConfigTypeDef = None
    ) -> ListProjectsPaginateResponseTypeDef:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Paginator.ListProjects.paginate)
        """
