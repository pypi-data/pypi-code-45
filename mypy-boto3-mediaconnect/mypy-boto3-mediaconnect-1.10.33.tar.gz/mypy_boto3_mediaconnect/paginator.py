"Main interface for mediaconnect service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediaconnect.type_defs import (
    ListEntitlementsPaginatePaginationConfigTypeDef,
    ListEntitlementsPaginateResponseTypeDef,
    ListFlowsPaginatePaginationConfigTypeDef,
    ListFlowsPaginateResponseTypeDef,
)


__all__ = ("ListEntitlementsPaginator", "ListFlowsPaginator")


class ListEntitlementsPaginator(Boto3Paginator):
    """
    Paginator for `list_entitlements`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListEntitlementsPaginatePaginationConfigTypeDef = None
    ) -> ListEntitlementsPaginateResponseTypeDef:
        """
        [ListEntitlements.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediaconnect.html#MediaConnect.Paginator.ListEntitlements.paginate)
        """


class ListFlowsPaginator(Boto3Paginator):
    """
    Paginator for `list_flows`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListFlowsPaginatePaginationConfigTypeDef = None
    ) -> ListFlowsPaginateResponseTypeDef:
        """
        [ListFlows.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediaconnect.html#MediaConnect.Paginator.ListFlows.paginate)
        """
