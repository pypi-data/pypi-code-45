"Main interface for codecommit service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codecommit.type_defs import (
    DescribePullRequestEventsPaginatePaginationConfigTypeDef,
    DescribePullRequestEventsPaginateResponseTypeDef,
    GetCommentsForComparedCommitPaginatePaginationConfigTypeDef,
    GetCommentsForComparedCommitPaginateResponseTypeDef,
    GetCommentsForPullRequestPaginatePaginationConfigTypeDef,
    GetCommentsForPullRequestPaginateResponseTypeDef,
    GetDifferencesPaginatePaginationConfigTypeDef,
    GetDifferencesPaginateResponseTypeDef,
    ListBranchesPaginatePaginationConfigTypeDef,
    ListBranchesPaginateResponseTypeDef,
    ListPullRequestsPaginatePaginationConfigTypeDef,
    ListPullRequestsPaginateResponseTypeDef,
    ListRepositoriesPaginatePaginationConfigTypeDef,
    ListRepositoriesPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribePullRequestEventsPaginator",
    "GetCommentsForComparedCommitPaginator",
    "GetCommentsForPullRequestPaginator",
    "GetDifferencesPaginator",
    "ListBranchesPaginator",
    "ListPullRequestsPaginator",
    "ListRepositoriesPaginator",
)


class DescribePullRequestEventsPaginator(Boto3Paginator):
    """
    Paginator for `describe_pull_request_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pullRequestId: str,
        pullRequestEventType: Literal[
            "PULL_REQUEST_CREATED",
            "PULL_REQUEST_STATUS_CHANGED",
            "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
            "PULL_REQUEST_MERGE_STATE_CHANGED",
            "PULL_REQUEST_APPROVAL_RULE_CREATED",
            "PULL_REQUEST_APPROVAL_RULE_UPDATED",
            "PULL_REQUEST_APPROVAL_RULE_DELETED",
            "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
            "PULL_REQUEST_APPROVAL_STATE_CHANGED",
        ] = None,
        actorArn: str = None,
        PaginationConfig: DescribePullRequestEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribePullRequestEventsPaginateResponseTypeDef:
        """
        [DescribePullRequestEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codecommit.html#CodeCommit.Paginator.DescribePullRequestEvents.paginate)
        """


class GetCommentsForComparedCommitPaginator(Boto3Paginator):
    """
    Paginator for `get_comments_for_compared_commit`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: str = None,
        PaginationConfig: GetCommentsForComparedCommitPaginatePaginationConfigTypeDef = None,
    ) -> GetCommentsForComparedCommitPaginateResponseTypeDef:
        """
        [GetCommentsForComparedCommit.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForComparedCommit.paginate)
        """


class GetCommentsForPullRequestPaginator(Boto3Paginator):
    """
    Paginator for `get_comments_for_pull_request`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pullRequestId: str,
        repositoryName: str = None,
        beforeCommitId: str = None,
        afterCommitId: str = None,
        PaginationConfig: GetCommentsForPullRequestPaginatePaginationConfigTypeDef = None,
    ) -> GetCommentsForPullRequestPaginateResponseTypeDef:
        """
        [GetCommentsForPullRequest.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForPullRequest.paginate)
        """


class GetDifferencesPaginator(Boto3Paginator):
    """
    Paginator for `get_differences`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: str = None,
        beforePath: str = None,
        afterPath: str = None,
        PaginationConfig: GetDifferencesPaginatePaginationConfigTypeDef = None,
    ) -> GetDifferencesPaginateResponseTypeDef:
        """
        [GetDifferences.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codecommit.html#CodeCommit.Paginator.GetDifferences.paginate)
        """


class ListBranchesPaginator(Boto3Paginator):
    """
    Paginator for `list_branches`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        PaginationConfig: ListBranchesPaginatePaginationConfigTypeDef = None,
    ) -> ListBranchesPaginateResponseTypeDef:
        """
        [ListBranches.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codecommit.html#CodeCommit.Paginator.ListBranches.paginate)
        """


class ListPullRequestsPaginator(Boto3Paginator):
    """
    Paginator for `list_pull_requests`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        authorArn: str = None,
        pullRequestStatus: Literal["OPEN", "CLOSED"] = None,
        PaginationConfig: ListPullRequestsPaginatePaginationConfigTypeDef = None,
    ) -> ListPullRequestsPaginateResponseTypeDef:
        """
        [ListPullRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codecommit.html#CodeCommit.Paginator.ListPullRequests.paginate)
        """


class ListRepositoriesPaginator(Boto3Paginator):
    """
    Paginator for `list_repositories`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        sortBy: Literal["repositoryName", "lastModifiedDate"] = None,
        order: Literal["ascending", "descending"] = None,
        PaginationConfig: ListRepositoriesPaginatePaginationConfigTypeDef = None,
    ) -> ListRepositoriesPaginateResponseTypeDef:
        """
        [ListRepositories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codecommit.html#CodeCommit.Paginator.ListRepositories.paginate)
        """
