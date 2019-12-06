"Main interface for amplify service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_amplify.type_defs import (
    ListAppsPaginatePaginationConfigTypeDef,
    ListAppsPaginateResponseTypeDef,
    ListBranchesPaginatePaginationConfigTypeDef,
    ListBranchesPaginateResponseTypeDef,
    ListDomainAssociationsPaginatePaginationConfigTypeDef,
    ListDomainAssociationsPaginateResponseTypeDef,
    ListJobsPaginatePaginationConfigTypeDef,
    ListJobsPaginateResponseTypeDef,
)


__all__ = (
    "ListAppsPaginator",
    "ListBranchesPaginator",
    "ListDomainAssociationsPaginator",
    "ListJobsPaginator",
)


class ListAppsPaginator(Boto3Paginator):
    """
    Paginator for `list_apps`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListAppsPaginatePaginationConfigTypeDef = None
    ) -> ListAppsPaginateResponseTypeDef:
        """
        [ListApps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/amplify.html#Amplify.Paginator.ListApps.paginate)
        """


class ListBranchesPaginator(Boto3Paginator):
    """
    Paginator for `list_branches`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, appId: str, PaginationConfig: ListBranchesPaginatePaginationConfigTypeDef = None
    ) -> ListBranchesPaginateResponseTypeDef:
        """
        [ListBranches.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/amplify.html#Amplify.Paginator.ListBranches.paginate)
        """


class ListDomainAssociationsPaginator(Boto3Paginator):
    """
    Paginator for `list_domain_associations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        appId: str,
        PaginationConfig: ListDomainAssociationsPaginatePaginationConfigTypeDef = None,
    ) -> ListDomainAssociationsPaginateResponseTypeDef:
        """
        [ListDomainAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/amplify.html#Amplify.Paginator.ListDomainAssociations.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        appId: str,
        branchName: str,
        PaginationConfig: ListJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListJobsPaginateResponseTypeDef:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/amplify.html#Amplify.Paginator.ListJobs.paginate)
        """
