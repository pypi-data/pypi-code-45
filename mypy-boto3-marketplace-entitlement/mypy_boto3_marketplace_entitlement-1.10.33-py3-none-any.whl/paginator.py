"Main interface for marketplace-entitlement service Paginators"
from __future__ import annotations

from typing import Dict, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_marketplace_entitlement.type_defs import (
    GetEntitlementsPaginatePaginationConfigTypeDef,
    GetEntitlementsPaginateResponseTypeDef,
)


__all__ = ("GetEntitlementsPaginator",)


class GetEntitlementsPaginator(Boto3Paginator):
    """
    Paginator for `get_entitlements`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProductCode: str,
        Filter: Dict[str, List[str]] = None,
        PaginationConfig: GetEntitlementsPaginatePaginationConfigTypeDef = None,
    ) -> GetEntitlementsPaginateResponseTypeDef:
        """
        [GetEntitlements.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Paginator.GetEntitlements.paginate)
        """
