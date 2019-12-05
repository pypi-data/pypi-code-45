"Main interface for serverlessrepo service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_serverlessrepo.type_defs import (
    ListApplicationDependenciesPaginatePaginationConfigTypeDef,
    ListApplicationDependenciesPaginateResponseTypeDef,
    ListApplicationVersionsPaginatePaginationConfigTypeDef,
    ListApplicationVersionsPaginateResponseTypeDef,
    ListApplicationsPaginatePaginationConfigTypeDef,
    ListApplicationsPaginateResponseTypeDef,
)


__all__ = (
    "ListApplicationDependenciesPaginator",
    "ListApplicationVersionsPaginator",
    "ListApplicationsPaginator",
)


class ListApplicationDependenciesPaginator(Boto3Paginator):
    """
    Paginator for `list_application_dependencies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApplicationId: str,
        SemanticVersion: str = None,
        PaginationConfig: ListApplicationDependenciesPaginatePaginationConfigTypeDef = None,
    ) -> ListApplicationDependenciesPaginateResponseTypeDef:
        """
        [ListApplicationDependencies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationDependencies.paginate)
        """


class ListApplicationVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_application_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApplicationId: str,
        PaginationConfig: ListApplicationVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListApplicationVersionsPaginateResponseTypeDef:
        """
        [ListApplicationVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationVersions.paginate)
        """


class ListApplicationsPaginator(Boto3Paginator):
    """
    Paginator for `list_applications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListApplicationsPaginatePaginationConfigTypeDef = None
    ) -> ListApplicationsPaginateResponseTypeDef:
        """
        [ListApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplications.paginate)
        """
