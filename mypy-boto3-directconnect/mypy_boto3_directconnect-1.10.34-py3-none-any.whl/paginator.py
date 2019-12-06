"Main interface for directconnect service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_directconnect.type_defs import (
    DescribeDirectConnectGatewayAssociationsPaginatePaginationConfigTypeDef,
    DescribeDirectConnectGatewayAssociationsPaginateResponseTypeDef,
    DescribeDirectConnectGatewayAttachmentsPaginatePaginationConfigTypeDef,
    DescribeDirectConnectGatewayAttachmentsPaginateResponseTypeDef,
    DescribeDirectConnectGatewaysPaginatePaginationConfigTypeDef,
    DescribeDirectConnectGatewaysPaginateResponseTypeDef,
)


__all__ = (
    "DescribeDirectConnectGatewayAssociationsPaginator",
    "DescribeDirectConnectGatewayAttachmentsPaginator",
    "DescribeDirectConnectGatewaysPaginator",
)


class DescribeDirectConnectGatewayAssociationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_direct_connect_gateway_associations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        associationId: str = None,
        associatedGatewayId: str = None,
        directConnectGatewayId: str = None,
        virtualGatewayId: str = None,
        PaginationConfig: DescribeDirectConnectGatewayAssociationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDirectConnectGatewayAssociationsPaginateResponseTypeDef:
        """
        [DescribeDirectConnectGatewayAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAssociations.paginate)
        """


class DescribeDirectConnectGatewayAttachmentsPaginator(Boto3Paginator):
    """
    Paginator for `describe_direct_connect_gateway_attachments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        directConnectGatewayId: str = None,
        virtualInterfaceId: str = None,
        PaginationConfig: DescribeDirectConnectGatewayAttachmentsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDirectConnectGatewayAttachmentsPaginateResponseTypeDef:
        """
        [DescribeDirectConnectGatewayAttachments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAttachments.paginate)
        """


class DescribeDirectConnectGatewaysPaginator(Boto3Paginator):
    """
    Paginator for `describe_direct_connect_gateways`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        directConnectGatewayId: str = None,
        PaginationConfig: DescribeDirectConnectGatewaysPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDirectConnectGatewaysPaginateResponseTypeDef:
        """
        [DescribeDirectConnectGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGateways.paginate)
        """
