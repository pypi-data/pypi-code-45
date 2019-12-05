"Main interface for iot1click-projects service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iot1click_projects.type_defs import (
    ListPlacementsPaginatePaginationConfigTypeDef,
    ListPlacementsPaginateResponseTypeDef,
    ListProjectsPaginatePaginationConfigTypeDef,
    ListProjectsPaginateResponseTypeDef,
)


__all__ = ("ListPlacementsPaginator", "ListProjectsPaginator")


class ListPlacementsPaginator(Boto3Paginator):
    """
    Paginator for `list_placements`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        projectName: str,
        PaginationConfig: ListPlacementsPaginatePaginationConfigTypeDef = None,
    ) -> ListPlacementsPaginateResponseTypeDef:
        """
        [ListPlacements.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListPlacements.paginate)
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
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListProjects.paginate)
        """
