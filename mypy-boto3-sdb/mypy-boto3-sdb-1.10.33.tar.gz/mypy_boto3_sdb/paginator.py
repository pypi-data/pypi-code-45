"Main interface for sdb service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sdb.type_defs import (
    ListDomainsPaginatePaginationConfigTypeDef,
    ListDomainsPaginateResponseTypeDef,
    SelectPaginatePaginationConfigTypeDef,
    SelectPaginateResponseTypeDef,
)


__all__ = ("ListDomainsPaginator", "SelectPaginator")


class ListDomainsPaginator(Boto3Paginator):
    """
    Paginator for `list_domains`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDomainsPaginatePaginationConfigTypeDef = None
    ) -> ListDomainsPaginateResponseTypeDef:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sdb.html#SimpleDB.Paginator.ListDomains.paginate)
        """


class SelectPaginator(Boto3Paginator):
    """
    Paginator for `select`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SelectExpression: str,
        ConsistentRead: bool = None,
        PaginationConfig: SelectPaginatePaginationConfigTypeDef = None,
    ) -> SelectPaginateResponseTypeDef:
        """
        [Select.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sdb.html#SimpleDB.Paginator.Select.paginate)
        """
