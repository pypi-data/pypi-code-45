"Main interface for securityhub service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_securityhub.type_defs import (
    GetEnabledStandardsPaginatePaginationConfigTypeDef,
    GetEnabledStandardsPaginateResponseTypeDef,
    GetFindingsPaginateFiltersTypeDef,
    GetFindingsPaginatePaginationConfigTypeDef,
    GetFindingsPaginateResponseTypeDef,
    GetFindingsPaginateSortCriteriaTypeDef,
    GetInsightsPaginatePaginationConfigTypeDef,
    GetInsightsPaginateResponseTypeDef,
    ListEnabledProductsForImportPaginatePaginationConfigTypeDef,
    ListEnabledProductsForImportPaginateResponseTypeDef,
    ListInvitationsPaginatePaginationConfigTypeDef,
    ListInvitationsPaginateResponseTypeDef,
    ListMembersPaginatePaginationConfigTypeDef,
    ListMembersPaginateResponseTypeDef,
)


__all__ = (
    "GetEnabledStandardsPaginator",
    "GetFindingsPaginator",
    "GetInsightsPaginator",
    "ListEnabledProductsForImportPaginator",
    "ListInvitationsPaginator",
    "ListMembersPaginator",
)


class GetEnabledStandardsPaginator(Boto3Paginator):
    """
    Paginator for `get_enabled_standards`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StandardsSubscriptionArns: List[str] = None,
        PaginationConfig: GetEnabledStandardsPaginatePaginationConfigTypeDef = None,
    ) -> GetEnabledStandardsPaginateResponseTypeDef:
        """
        [GetEnabledStandards.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards.paginate)
        """


class GetFindingsPaginator(Boto3Paginator):
    """
    Paginator for `get_findings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: GetFindingsPaginateFiltersTypeDef = None,
        SortCriteria: List[GetFindingsPaginateSortCriteriaTypeDef] = None,
        PaginationConfig: GetFindingsPaginatePaginationConfigTypeDef = None,
    ) -> GetFindingsPaginateResponseTypeDef:
        """
        [GetFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings.paginate)
        """


class GetInsightsPaginator(Boto3Paginator):
    """
    Paginator for `get_insights`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InsightArns: List[str] = None,
        PaginationConfig: GetInsightsPaginatePaginationConfigTypeDef = None,
    ) -> GetInsightsPaginateResponseTypeDef:
        """
        [GetInsights.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights.paginate)
        """


class ListEnabledProductsForImportPaginator(Boto3Paginator):
    """
    Paginator for `list_enabled_products_for_import`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListEnabledProductsForImportPaginatePaginationConfigTypeDef = None
    ) -> ListEnabledProductsForImportPaginateResponseTypeDef:
        """
        [ListEnabledProductsForImport.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport.paginate)
        """


class ListInvitationsPaginator(Boto3Paginator):
    """
    Paginator for `list_invitations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListInvitationsPaginatePaginationConfigTypeDef = None
    ) -> ListInvitationsPaginateResponseTypeDef:
        """
        [ListInvitations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations.paginate)
        """


class ListMembersPaginator(Boto3Paginator):
    """
    Paginator for `list_members`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        OnlyAssociated: bool = None,
        PaginationConfig: ListMembersPaginatePaginationConfigTypeDef = None,
    ) -> ListMembersPaginateResponseTypeDef:
        """
        [ListMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers.paginate)
        """
