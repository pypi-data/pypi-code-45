"Main interface for appmesh service"

from mypy_boto3_appmesh.client import Client
from mypy_boto3_appmesh.paginator import (
    ListMeshesPaginator,
    ListRoutesPaginator,
    ListTagsForResourcePaginator,
    ListVirtualNodesPaginator,
    ListVirtualRoutersPaginator,
    ListVirtualServicesPaginator,
)


__all__ = (
    "Client",
    "ListMeshesPaginator",
    "ListRoutesPaginator",
    "ListTagsForResourcePaginator",
    "ListVirtualNodesPaginator",
    "ListVirtualRoutersPaginator",
    "ListVirtualServicesPaginator",
)
