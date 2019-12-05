"Main interface for sso service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sso.type_defs import (
    ListAccountRolesPaginatePaginationConfigTypeDef,
    ListAccountRolesPaginateResponseTypeDef,
    ListAccountsPaginatePaginationConfigTypeDef,
    ListAccountsPaginateResponseTypeDef,
)


__all__ = ("ListAccountRolesPaginator", "ListAccountsPaginator")


class ListAccountRolesPaginator(Boto3Paginator):
    """
    Paginator for `list_account_roles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        accessToken: str,
        accountId: str,
        PaginationConfig: ListAccountRolesPaginatePaginationConfigTypeDef = None,
    ) -> ListAccountRolesPaginateResponseTypeDef:
        """
        [ListAccountRoles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sso.html#SSO.Paginator.ListAccountRoles.paginate)
        """


class ListAccountsPaginator(Boto3Paginator):
    """
    Paginator for `list_accounts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, accessToken: str, PaginationConfig: ListAccountsPaginatePaginationConfigTypeDef = None
    ) -> ListAccountsPaginateResponseTypeDef:
        """
        [ListAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sso.html#SSO.Paginator.ListAccounts.paginate)
        """
