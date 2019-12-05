"Main interface for codebuild service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codebuild.type_defs import (
    ListBuildsForProjectPaginatePaginationConfigTypeDef,
    ListBuildsForProjectPaginateResponseTypeDef,
    ListBuildsPaginatePaginationConfigTypeDef,
    ListBuildsPaginateResponseTypeDef,
    ListProjectsPaginatePaginationConfigTypeDef,
    ListProjectsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ListBuildsPaginator", "ListBuildsForProjectPaginator", "ListProjectsPaginator")


class ListBuildsPaginator(Boto3Paginator):
    """
    Paginator for `list_builds`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: ListBuildsPaginatePaginationConfigTypeDef = None,
    ) -> ListBuildsPaginateResponseTypeDef:
        """
        [ListBuilds.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codebuild.html#CodeBuild.Paginator.ListBuilds.paginate)
        """


class ListBuildsForProjectPaginator(Boto3Paginator):
    """
    Paginator for `list_builds_for_project`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        projectName: str,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: ListBuildsForProjectPaginatePaginationConfigTypeDef = None,
    ) -> ListBuildsForProjectPaginateResponseTypeDef:
        """
        [ListBuildsForProject.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildsForProject.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    Paginator for `list_projects`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        sortBy: Literal["NAME", "CREATED_TIME", "LAST_MODIFIED_TIME"] = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: ListProjectsPaginatePaginationConfigTypeDef = None,
    ) -> ListProjectsPaginateResponseTypeDef:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codebuild.html#CodeBuild.Paginator.ListProjects.paginate)
        """
