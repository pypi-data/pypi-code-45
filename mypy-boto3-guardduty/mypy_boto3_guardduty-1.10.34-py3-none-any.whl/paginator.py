"Main interface for guardduty service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_guardduty.type_defs import (
    ListDetectorsPaginatePaginationConfigTypeDef,
    ListDetectorsPaginateResponseTypeDef,
    ListFiltersPaginatePaginationConfigTypeDef,
    ListFiltersPaginateResponseTypeDef,
    ListFindingsPaginateFindingCriteriaTypeDef,
    ListFindingsPaginatePaginationConfigTypeDef,
    ListFindingsPaginateResponseTypeDef,
    ListFindingsPaginateSortCriteriaTypeDef,
    ListIPSetsPaginatePaginationConfigTypeDef,
    ListIPSetsPaginateResponseTypeDef,
    ListInvitationsPaginatePaginationConfigTypeDef,
    ListInvitationsPaginateResponseTypeDef,
    ListMembersPaginatePaginationConfigTypeDef,
    ListMembersPaginateResponseTypeDef,
    ListThreatIntelSetsPaginatePaginationConfigTypeDef,
    ListThreatIntelSetsPaginateResponseTypeDef,
)


__all__ = (
    "ListDetectorsPaginator",
    "ListFiltersPaginator",
    "ListFindingsPaginator",
    "ListIPSetsPaginator",
    "ListInvitationsPaginator",
    "ListMembersPaginator",
    "ListThreatIntelSetsPaginator",
)


class ListDetectorsPaginator(Boto3Paginator):
    """
    Paginator for `list_detectors`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDetectorsPaginatePaginationConfigTypeDef = None
    ) -> ListDetectorsPaginateResponseTypeDef:
        """
        [ListDetectors.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/guardduty.html#GuardDuty.Paginator.ListDetectors.paginate)
        """


class ListFiltersPaginator(Boto3Paginator):
    """
    Paginator for `list_filters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DetectorId: str, PaginationConfig: ListFiltersPaginatePaginationConfigTypeDef = None
    ) -> ListFiltersPaginateResponseTypeDef:
        """
        [ListFilters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/guardduty.html#GuardDuty.Paginator.ListFilters.paginate)
        """


class ListFindingsPaginator(Boto3Paginator):
    """
    Paginator for `list_findings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DetectorId: str,
        FindingCriteria: ListFindingsPaginateFindingCriteriaTypeDef = None,
        SortCriteria: ListFindingsPaginateSortCriteriaTypeDef = None,
        PaginationConfig: ListFindingsPaginatePaginationConfigTypeDef = None,
    ) -> ListFindingsPaginateResponseTypeDef:
        """
        [ListFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/guardduty.html#GuardDuty.Paginator.ListFindings.paginate)
        """


class ListIPSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_ip_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DetectorId: str, PaginationConfig: ListIPSetsPaginatePaginationConfigTypeDef = None
    ) -> ListIPSetsPaginateResponseTypeDef:
        """
        [ListIPSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/guardduty.html#GuardDuty.Paginator.ListIPSets.paginate)
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
        [ListInvitations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/guardduty.html#GuardDuty.Paginator.ListInvitations.paginate)
        """


class ListMembersPaginator(Boto3Paginator):
    """
    Paginator for `list_members`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DetectorId: str,
        OnlyAssociated: str = None,
        PaginationConfig: ListMembersPaginatePaginationConfigTypeDef = None,
    ) -> ListMembersPaginateResponseTypeDef:
        """
        [ListMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/guardduty.html#GuardDuty.Paginator.ListMembers.paginate)
        """


class ListThreatIntelSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_threat_intel_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DetectorId: str,
        PaginationConfig: ListThreatIntelSetsPaginatePaginationConfigTypeDef = None,
    ) -> ListThreatIntelSetsPaginateResponseTypeDef:
        """
        [ListThreatIntelSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/guardduty.html#GuardDuty.Paginator.ListThreatIntelSets.paginate)
        """
