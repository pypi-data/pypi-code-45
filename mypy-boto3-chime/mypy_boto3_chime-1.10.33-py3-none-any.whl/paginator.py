"Main interface for chime service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_chime.type_defs import (
    ListAccountsPaginatePaginationConfigTypeDef,
    ListAccountsPaginateResponseTypeDef,
    ListUsersPaginatePaginationConfigTypeDef,
    ListUsersPaginateResponseTypeDef,
)


__all__ = ("ListAccountsPaginator", "ListUsersPaginator")


class ListAccountsPaginator(Boto3Paginator):
    """
    Paginator for `list_accounts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Name: str = None,
        UserEmail: str = None,
        PaginationConfig: ListAccountsPaginatePaginationConfigTypeDef = None,
    ) -> ListAccountsPaginateResponseTypeDef:
        """
        [ListAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/chime.html#Chime.Paginator.ListAccounts.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    Paginator for `list_users`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AccountId: str,
        UserEmail: str = None,
        PaginationConfig: ListUsersPaginatePaginationConfigTypeDef = None,
    ) -> ListUsersPaginateResponseTypeDef:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/chime.html#Chime.Paginator.ListUsers.paginate)
        """
