"Main interface for networkmanager service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_networkmanager.type_defs import (
    DescribeGlobalNetworksPaginatePaginationConfigTypeDef,
    DescribeGlobalNetworksPaginateResponseTypeDef,
    GetCustomerGatewayAssociationsPaginatePaginationConfigTypeDef,
    GetCustomerGatewayAssociationsPaginateResponseTypeDef,
    GetDevicesPaginatePaginationConfigTypeDef,
    GetDevicesPaginateResponseTypeDef,
    GetLinkAssociationsPaginatePaginationConfigTypeDef,
    GetLinkAssociationsPaginateResponseTypeDef,
    GetLinksPaginatePaginationConfigTypeDef,
    GetLinksPaginateResponseTypeDef,
    GetSitesPaginatePaginationConfigTypeDef,
    GetSitesPaginateResponseTypeDef,
    GetTransitGatewayRegistrationsPaginatePaginationConfigTypeDef,
    GetTransitGatewayRegistrationsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeGlobalNetworksPaginator",
    "GetCustomerGatewayAssociationsPaginator",
    "GetDevicesPaginator",
    "GetLinkAssociationsPaginator",
    "GetLinksPaginator",
    "GetSitesPaginator",
    "GetTransitGatewayRegistrationsPaginator",
)


class DescribeGlobalNetworksPaginator(Boto3Paginator):
    """
    Paginator for `describe_global_networks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalNetworkIds: List[str] = None,
        PaginationConfig: DescribeGlobalNetworksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeGlobalNetworksPaginateResponseTypeDef:
        """
        [DescribeGlobalNetworks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks.paginate)
        """


class GetCustomerGatewayAssociationsPaginator(Boto3Paginator):
    """
    Paginator for `get_customer_gateway_associations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalNetworkId: str,
        CustomerGatewayArns: List[str] = None,
        PaginationConfig: GetCustomerGatewayAssociationsPaginatePaginationConfigTypeDef = None,
    ) -> GetCustomerGatewayAssociationsPaginateResponseTypeDef:
        """
        [GetCustomerGatewayAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations.paginate)
        """


class GetDevicesPaginator(Boto3Paginator):
    """
    Paginator for `get_devices`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalNetworkId: str,
        DeviceIds: List[str] = None,
        SiteId: str = None,
        PaginationConfig: GetDevicesPaginatePaginationConfigTypeDef = None,
    ) -> GetDevicesPaginateResponseTypeDef:
        """
        [GetDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices.paginate)
        """


class GetLinkAssociationsPaginator(Boto3Paginator):
    """
    Paginator for `get_link_associations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalNetworkId: str,
        DeviceId: str = None,
        LinkId: str = None,
        PaginationConfig: GetLinkAssociationsPaginatePaginationConfigTypeDef = None,
    ) -> GetLinkAssociationsPaginateResponseTypeDef:
        """
        [GetLinkAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations.paginate)
        """


class GetLinksPaginator(Boto3Paginator):
    """
    Paginator for `get_links`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalNetworkId: str,
        LinkIds: List[str] = None,
        SiteId: str = None,
        Type: str = None,
        Provider: str = None,
        PaginationConfig: GetLinksPaginatePaginationConfigTypeDef = None,
    ) -> GetLinksPaginateResponseTypeDef:
        """
        [GetLinks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks.paginate)
        """


class GetSitesPaginator(Boto3Paginator):
    """
    Paginator for `get_sites`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalNetworkId: str,
        SiteIds: List[str] = None,
        PaginationConfig: GetSitesPaginatePaginationConfigTypeDef = None,
    ) -> GetSitesPaginateResponseTypeDef:
        """
        [GetSites.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites.paginate)
        """


class GetTransitGatewayRegistrationsPaginator(Boto3Paginator):
    """
    Paginator for `get_transit_gateway_registrations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalNetworkId: str,
        TransitGatewayArns: List[str] = None,
        PaginationConfig: GetTransitGatewayRegistrationsPaginatePaginationConfigTypeDef = None,
    ) -> GetTransitGatewayRegistrationsPaginateResponseTypeDef:
        """
        [GetTransitGatewayRegistrations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations.paginate)
        """
