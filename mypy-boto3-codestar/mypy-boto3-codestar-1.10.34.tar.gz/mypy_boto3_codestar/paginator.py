"Main interface for codestar service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codestar.type_defs import (
    ListProjectsPaginatePaginationConfigTypeDef,
    ListProjectsPaginateResponseTypeDef,
    ListResourcesPaginatePaginationConfigTypeDef,
    ListResourcesPaginateResponseTypeDef,
    ListTeamMembersPaginatePaginationConfigTypeDef,
    ListTeamMembersPaginateResponseTypeDef,
    ListUserProfilesPaginatePaginationConfigTypeDef,
    ListUserProfilesPaginateResponseTypeDef,
)


__all__ = (
    "ListProjectsPaginator",
    "ListResourcesPaginator",
    "ListTeamMembersPaginator",
    "ListUserProfilesPaginator",
)


class ListProjectsPaginator(Boto3Paginator):
    """
    Paginator for `list_projects`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListProjectsPaginatePaginationConfigTypeDef = None
    ) -> ListProjectsPaginateResponseTypeDef:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codestar.html#CodeStar.Paginator.ListProjects.paginate)
        """


class ListResourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, projectId: str, PaginationConfig: ListResourcesPaginatePaginationConfigTypeDef = None
    ) -> ListResourcesPaginateResponseTypeDef:
        """
        [ListResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codestar.html#CodeStar.Paginator.ListResources.paginate)
        """


class ListTeamMembersPaginator(Boto3Paginator):
    """
    Paginator for `list_team_members`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        projectId: str,
        PaginationConfig: ListTeamMembersPaginatePaginationConfigTypeDef = None,
    ) -> ListTeamMembersPaginateResponseTypeDef:
        """
        [ListTeamMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codestar.html#CodeStar.Paginator.ListTeamMembers.paginate)
        """


class ListUserProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_user_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListUserProfilesPaginatePaginationConfigTypeDef = None
    ) -> ListUserProfilesPaginateResponseTypeDef:
        """
        [ListUserProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codestar.html#CodeStar.Paginator.ListUserProfiles.paginate)
        """
