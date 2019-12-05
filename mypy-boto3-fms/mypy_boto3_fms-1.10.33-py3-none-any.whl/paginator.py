"Main interface for fms service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_fms.type_defs import (
    ListComplianceStatusPaginatePaginationConfigTypeDef,
    ListComplianceStatusPaginateResponseTypeDef,
    ListMemberAccountsPaginatePaginationConfigTypeDef,
    ListMemberAccountsPaginateResponseTypeDef,
    ListPoliciesPaginatePaginationConfigTypeDef,
    ListPoliciesPaginateResponseTypeDef,
)


__all__ = ("ListComplianceStatusPaginator", "ListMemberAccountsPaginator", "ListPoliciesPaginator")


class ListComplianceStatusPaginator(Boto3Paginator):
    """
    Paginator for `list_compliance_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PolicyId: str,
        PaginationConfig: ListComplianceStatusPaginatePaginationConfigTypeDef = None,
    ) -> ListComplianceStatusPaginateResponseTypeDef:
        """
        [ListComplianceStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/fms.html#FMS.Paginator.ListComplianceStatus.paginate)
        """


class ListMemberAccountsPaginator(Boto3Paginator):
    """
    Paginator for `list_member_accounts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListMemberAccountsPaginatePaginationConfigTypeDef = None
    ) -> ListMemberAccountsPaginateResponseTypeDef:
        """
        [ListMemberAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/fms.html#FMS.Paginator.ListMemberAccounts.paginate)
        """


class ListPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListPoliciesPaginatePaginationConfigTypeDef = None
    ) -> ListPoliciesPaginateResponseTypeDef:
        """
        [ListPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/fms.html#FMS.Paginator.ListPolicies.paginate)
        """
