"Main interface for shield service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_shield.type_defs import (
    ListAttacksPaginateEndTimeTypeDef,
    ListAttacksPaginatePaginationConfigTypeDef,
    ListAttacksPaginateResponseTypeDef,
    ListAttacksPaginateStartTimeTypeDef,
    ListProtectionsPaginatePaginationConfigTypeDef,
    ListProtectionsPaginateResponseTypeDef,
)


__all__ = ("ListAttacksPaginator", "ListProtectionsPaginator")


class ListAttacksPaginator(Boto3Paginator):
    """
    Paginator for `list_attacks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceArns: List[str] = None,
        StartTime: ListAttacksPaginateStartTimeTypeDef = None,
        EndTime: ListAttacksPaginateEndTimeTypeDef = None,
        PaginationConfig: ListAttacksPaginatePaginationConfigTypeDef = None,
    ) -> ListAttacksPaginateResponseTypeDef:
        """
        [ListAttacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/shield.html#Shield.Paginator.ListAttacks.paginate)
        """


class ListProtectionsPaginator(Boto3Paginator):
    """
    Paginator for `list_protections`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListProtectionsPaginatePaginationConfigTypeDef = None
    ) -> ListProtectionsPaginateResponseTypeDef:
        """
        [ListProtections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/shield.html#Shield.Paginator.ListProtections.paginate)
        """
