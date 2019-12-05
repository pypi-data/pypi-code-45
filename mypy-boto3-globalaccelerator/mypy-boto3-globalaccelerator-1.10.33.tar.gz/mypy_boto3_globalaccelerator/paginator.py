"Main interface for globalaccelerator service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_globalaccelerator.type_defs import (
    ListAcceleratorsPaginatePaginationConfigTypeDef,
    ListAcceleratorsPaginateResponseTypeDef,
    ListEndpointGroupsPaginatePaginationConfigTypeDef,
    ListEndpointGroupsPaginateResponseTypeDef,
    ListListenersPaginatePaginationConfigTypeDef,
    ListListenersPaginateResponseTypeDef,
)


__all__ = ("ListAcceleratorsPaginator", "ListEndpointGroupsPaginator", "ListListenersPaginator")


class ListAcceleratorsPaginator(Boto3Paginator):
    """
    Paginator for `list_accelerators`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListAcceleratorsPaginatePaginationConfigTypeDef = None
    ) -> ListAcceleratorsPaginateResponseTypeDef:
        """
        [ListAccelerators.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators.paginate)
        """


class ListEndpointGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_endpoint_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ListenerArn: str,
        PaginationConfig: ListEndpointGroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListEndpointGroupsPaginateResponseTypeDef:
        """
        [ListEndpointGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups.paginate)
        """


class ListListenersPaginator(Boto3Paginator):
    """
    Paginator for `list_listeners`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AcceleratorArn: str,
        PaginationConfig: ListListenersPaginatePaginationConfigTypeDef = None,
    ) -> ListListenersPaginateResponseTypeDef:
        """
        [ListListeners.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners.paginate)
        """
