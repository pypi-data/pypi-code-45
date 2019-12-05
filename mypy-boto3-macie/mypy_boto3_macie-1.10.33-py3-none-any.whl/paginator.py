"Main interface for macie service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_macie.type_defs import (
    ListMemberAccountsPaginatePaginationConfigTypeDef,
    ListMemberAccountsPaginateResponseTypeDef,
    ListS3ResourcesPaginatePaginationConfigTypeDef,
    ListS3ResourcesPaginateResponseTypeDef,
)


__all__ = ("ListMemberAccountsPaginator", "ListS3ResourcesPaginator")


class ListMemberAccountsPaginator(Boto3Paginator):
    """
    Paginator for `list_member_accounts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListMemberAccountsPaginatePaginationConfigTypeDef = None
    ) -> ListMemberAccountsPaginateResponseTypeDef:
        """
        [ListMemberAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/macie.html#Macie.Paginator.ListMemberAccounts.paginate)
        """


class ListS3ResourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_s3_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        memberAccountId: str = None,
        PaginationConfig: ListS3ResourcesPaginatePaginationConfigTypeDef = None,
    ) -> ListS3ResourcesPaginateResponseTypeDef:
        """
        [ListS3Resources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/macie.html#Macie.Paginator.ListS3Resources.paginate)
        """
