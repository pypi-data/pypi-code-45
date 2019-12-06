"Main interface for appmesh service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_appmesh.type_defs import (
    ListMeshesPaginatePaginationConfigTypeDef,
    ListMeshesPaginateResponseTypeDef,
    ListRoutesPaginatePaginationConfigTypeDef,
    ListRoutesPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
    ListVirtualNodesPaginatePaginationConfigTypeDef,
    ListVirtualNodesPaginateResponseTypeDef,
    ListVirtualRoutersPaginatePaginationConfigTypeDef,
    ListVirtualRoutersPaginateResponseTypeDef,
    ListVirtualServicesPaginatePaginationConfigTypeDef,
    ListVirtualServicesPaginateResponseTypeDef,
)


__all__ = (
    "ListMeshesPaginator",
    "ListRoutesPaginator",
    "ListTagsForResourcePaginator",
    "ListVirtualNodesPaginator",
    "ListVirtualRoutersPaginator",
    "ListVirtualServicesPaginator",
)


class ListMeshesPaginator(Boto3Paginator):
    """
    Paginator for `list_meshes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListMeshesPaginatePaginationConfigTypeDef = None
    ) -> ListMeshesPaginateResponseTypeDef:
        """
        [ListMeshes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListMeshes.paginate)
        """


class ListRoutesPaginator(Boto3Paginator):
    """
    Paginator for `list_routes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        meshName: str,
        virtualRouterName: str,
        PaginationConfig: ListRoutesPaginatePaginationConfigTypeDef = None,
    ) -> ListRoutesPaginateResponseTypeDef:
        """
        [ListRoutes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListRoutes.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_tags_for_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceArn: str,
        PaginationConfig: ListTagsForResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListTagsForResourcePaginateResponseTypeDef:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListTagsForResource.paginate)
        """


class ListVirtualNodesPaginator(Boto3Paginator):
    """
    Paginator for `list_virtual_nodes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        meshName: str,
        PaginationConfig: ListVirtualNodesPaginatePaginationConfigTypeDef = None,
    ) -> ListVirtualNodesPaginateResponseTypeDef:
        """
        [ListVirtualNodes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualNodes.paginate)
        """


class ListVirtualRoutersPaginator(Boto3Paginator):
    """
    Paginator for `list_virtual_routers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        meshName: str,
        PaginationConfig: ListVirtualRoutersPaginatePaginationConfigTypeDef = None,
    ) -> ListVirtualRoutersPaginateResponseTypeDef:
        """
        [ListVirtualRouters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualRouters.paginate)
        """


class ListVirtualServicesPaginator(Boto3Paginator):
    """
    Paginator for `list_virtual_services`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        meshName: str,
        PaginationConfig: ListVirtualServicesPaginatePaginationConfigTypeDef = None,
    ) -> ListVirtualServicesPaginateResponseTypeDef:
        """
        [ListVirtualServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualServices.paginate)
        """
