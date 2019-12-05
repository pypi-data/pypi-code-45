"Main interface for route53domains service Paginators"
from __future__ import annotations

from datetime import datetime
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_route53domains.type_defs import (
    ListDomainsPaginatePaginationConfigTypeDef,
    ListDomainsPaginateResponseTypeDef,
    ListOperationsPaginatePaginationConfigTypeDef,
    ListOperationsPaginateResponseTypeDef,
    ViewBillingPaginatePaginationConfigTypeDef,
    ViewBillingPaginateResponseTypeDef,
)


__all__ = ("ListDomainsPaginator", "ListOperationsPaginator", "ViewBillingPaginator")


class ListDomainsPaginator(Boto3Paginator):
    """
    Paginator for `list_domains`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDomainsPaginatePaginationConfigTypeDef = None
    ) -> ListDomainsPaginateResponseTypeDef:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53domains.html#Route53Domains.Paginator.ListDomains.paginate)
        """


class ListOperationsPaginator(Boto3Paginator):
    """
    Paginator for `list_operations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SubmittedSince: datetime = None,
        PaginationConfig: ListOperationsPaginatePaginationConfigTypeDef = None,
    ) -> ListOperationsPaginateResponseTypeDef:
        """
        [ListOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53domains.html#Route53Domains.Paginator.ListOperations.paginate)
        """


class ViewBillingPaginator(Boto3Paginator):
    """
    Paginator for `view_billing`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Start: datetime = None,
        End: datetime = None,
        PaginationConfig: ViewBillingPaginatePaginationConfigTypeDef = None,
    ) -> ViewBillingPaginateResponseTypeDef:
        """
        [ViewBilling.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53domains.html#Route53Domains.Paginator.ViewBilling.paginate)
        """
