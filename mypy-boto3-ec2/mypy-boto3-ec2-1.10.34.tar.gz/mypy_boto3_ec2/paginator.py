"Main interface for ec2 service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ec2.type_defs import (
    DescribeByoipCidrsPaginatePaginationConfigTypeDef,
    DescribeByoipCidrsPaginateResponseTypeDef,
    DescribeCapacityReservationsPaginateFiltersTypeDef,
    DescribeCapacityReservationsPaginatePaginationConfigTypeDef,
    DescribeCapacityReservationsPaginateResponseTypeDef,
    DescribeClassicLinkInstancesPaginateFiltersTypeDef,
    DescribeClassicLinkInstancesPaginatePaginationConfigTypeDef,
    DescribeClassicLinkInstancesPaginateResponseTypeDef,
    DescribeClientVpnAuthorizationRulesPaginateFiltersTypeDef,
    DescribeClientVpnAuthorizationRulesPaginatePaginationConfigTypeDef,
    DescribeClientVpnAuthorizationRulesPaginateResponseTypeDef,
    DescribeClientVpnConnectionsPaginateFiltersTypeDef,
    DescribeClientVpnConnectionsPaginatePaginationConfigTypeDef,
    DescribeClientVpnConnectionsPaginateResponseTypeDef,
    DescribeClientVpnEndpointsPaginateFiltersTypeDef,
    DescribeClientVpnEndpointsPaginatePaginationConfigTypeDef,
    DescribeClientVpnEndpointsPaginateResponseTypeDef,
    DescribeClientVpnRoutesPaginateFiltersTypeDef,
    DescribeClientVpnRoutesPaginatePaginationConfigTypeDef,
    DescribeClientVpnRoutesPaginateResponseTypeDef,
    DescribeClientVpnTargetNetworksPaginateFiltersTypeDef,
    DescribeClientVpnTargetNetworksPaginatePaginationConfigTypeDef,
    DescribeClientVpnTargetNetworksPaginateResponseTypeDef,
    DescribeDhcpOptionsPaginateFiltersTypeDef,
    DescribeDhcpOptionsPaginatePaginationConfigTypeDef,
    DescribeDhcpOptionsPaginateResponseTypeDef,
    DescribeEgressOnlyInternetGatewaysPaginatePaginationConfigTypeDef,
    DescribeEgressOnlyInternetGatewaysPaginateResponseTypeDef,
    DescribeExportImageTasksPaginateFiltersTypeDef,
    DescribeExportImageTasksPaginatePaginationConfigTypeDef,
    DescribeExportImageTasksPaginateResponseTypeDef,
    DescribeFastSnapshotRestoresPaginateFiltersTypeDef,
    DescribeFastSnapshotRestoresPaginatePaginationConfigTypeDef,
    DescribeFastSnapshotRestoresPaginateResponseTypeDef,
    DescribeFleetsPaginateFiltersTypeDef,
    DescribeFleetsPaginatePaginationConfigTypeDef,
    DescribeFleetsPaginateResponseTypeDef,
    DescribeFlowLogsPaginateFiltersTypeDef,
    DescribeFlowLogsPaginatePaginationConfigTypeDef,
    DescribeFlowLogsPaginateResponseTypeDef,
    DescribeFpgaImagesPaginateFiltersTypeDef,
    DescribeFpgaImagesPaginatePaginationConfigTypeDef,
    DescribeFpgaImagesPaginateResponseTypeDef,
    DescribeHostReservationOfferingsPaginateFiltersTypeDef,
    DescribeHostReservationOfferingsPaginatePaginationConfigTypeDef,
    DescribeHostReservationOfferingsPaginateResponseTypeDef,
    DescribeHostReservationsPaginateFiltersTypeDef,
    DescribeHostReservationsPaginatePaginationConfigTypeDef,
    DescribeHostReservationsPaginateResponseTypeDef,
    DescribeHostsPaginateFiltersTypeDef,
    DescribeHostsPaginatePaginationConfigTypeDef,
    DescribeHostsPaginateResponseTypeDef,
    DescribeIamInstanceProfileAssociationsPaginateFiltersTypeDef,
    DescribeIamInstanceProfileAssociationsPaginatePaginationConfigTypeDef,
    DescribeIamInstanceProfileAssociationsPaginateResponseTypeDef,
    DescribeImportImageTasksPaginateFiltersTypeDef,
    DescribeImportImageTasksPaginatePaginationConfigTypeDef,
    DescribeImportImageTasksPaginateResponseTypeDef,
    DescribeImportSnapshotTasksPaginateFiltersTypeDef,
    DescribeImportSnapshotTasksPaginatePaginationConfigTypeDef,
    DescribeImportSnapshotTasksPaginateResponseTypeDef,
    DescribeInstanceCreditSpecificationsPaginateFiltersTypeDef,
    DescribeInstanceCreditSpecificationsPaginatePaginationConfigTypeDef,
    DescribeInstanceCreditSpecificationsPaginateResponseTypeDef,
    DescribeInstanceStatusPaginateFiltersTypeDef,
    DescribeInstanceStatusPaginatePaginationConfigTypeDef,
    DescribeInstanceStatusPaginateResponseTypeDef,
    DescribeInstancesPaginateFiltersTypeDef,
    DescribeInstancesPaginatePaginationConfigTypeDef,
    DescribeInstancesPaginateResponseTypeDef,
    DescribeInternetGatewaysPaginateFiltersTypeDef,
    DescribeInternetGatewaysPaginatePaginationConfigTypeDef,
    DescribeInternetGatewaysPaginateResponseTypeDef,
    DescribeLaunchTemplateVersionsPaginateFiltersTypeDef,
    DescribeLaunchTemplateVersionsPaginatePaginationConfigTypeDef,
    DescribeLaunchTemplateVersionsPaginateResponseTypeDef,
    DescribeLaunchTemplatesPaginateFiltersTypeDef,
    DescribeLaunchTemplatesPaginatePaginationConfigTypeDef,
    DescribeLaunchTemplatesPaginateResponseTypeDef,
    DescribeMovingAddressesPaginateFiltersTypeDef,
    DescribeMovingAddressesPaginatePaginationConfigTypeDef,
    DescribeMovingAddressesPaginateResponseTypeDef,
    DescribeNatGatewaysPaginateFiltersTypeDef,
    DescribeNatGatewaysPaginatePaginationConfigTypeDef,
    DescribeNatGatewaysPaginateResponseTypeDef,
    DescribeNetworkAclsPaginateFiltersTypeDef,
    DescribeNetworkAclsPaginatePaginationConfigTypeDef,
    DescribeNetworkAclsPaginateResponseTypeDef,
    DescribeNetworkInterfacePermissionsPaginateFiltersTypeDef,
    DescribeNetworkInterfacePermissionsPaginatePaginationConfigTypeDef,
    DescribeNetworkInterfacePermissionsPaginateResponseTypeDef,
    DescribeNetworkInterfacesPaginateFiltersTypeDef,
    DescribeNetworkInterfacesPaginatePaginationConfigTypeDef,
    DescribeNetworkInterfacesPaginateResponseTypeDef,
    DescribePrefixListsPaginateFiltersTypeDef,
    DescribePrefixListsPaginatePaginationConfigTypeDef,
    DescribePrefixListsPaginateResponseTypeDef,
    DescribePrincipalIdFormatPaginatePaginationConfigTypeDef,
    DescribePrincipalIdFormatPaginateResponseTypeDef,
    DescribePublicIpv4PoolsPaginatePaginationConfigTypeDef,
    DescribePublicIpv4PoolsPaginateResponseTypeDef,
    DescribeReservedInstancesModificationsPaginateFiltersTypeDef,
    DescribeReservedInstancesModificationsPaginatePaginationConfigTypeDef,
    DescribeReservedInstancesModificationsPaginateResponseTypeDef,
    DescribeReservedInstancesOfferingsPaginateFiltersTypeDef,
    DescribeReservedInstancesOfferingsPaginatePaginationConfigTypeDef,
    DescribeReservedInstancesOfferingsPaginateResponseTypeDef,
    DescribeRouteTablesPaginateFiltersTypeDef,
    DescribeRouteTablesPaginatePaginationConfigTypeDef,
    DescribeRouteTablesPaginateResponseTypeDef,
    DescribeScheduledInstanceAvailabilityPaginateFiltersTypeDef,
    DescribeScheduledInstanceAvailabilityPaginateFirstSlotStartTimeRangeTypeDef,
    DescribeScheduledInstanceAvailabilityPaginatePaginationConfigTypeDef,
    DescribeScheduledInstanceAvailabilityPaginateRecurrenceTypeDef,
    DescribeScheduledInstanceAvailabilityPaginateResponseTypeDef,
    DescribeScheduledInstancesPaginateFiltersTypeDef,
    DescribeScheduledInstancesPaginatePaginationConfigTypeDef,
    DescribeScheduledInstancesPaginateResponseTypeDef,
    DescribeScheduledInstancesPaginateSlotStartTimeRangeTypeDef,
    DescribeSecurityGroupsPaginateFiltersTypeDef,
    DescribeSecurityGroupsPaginatePaginationConfigTypeDef,
    DescribeSecurityGroupsPaginateResponseTypeDef,
    DescribeSnapshotsPaginateFiltersTypeDef,
    DescribeSnapshotsPaginatePaginationConfigTypeDef,
    DescribeSnapshotsPaginateResponseTypeDef,
    DescribeSpotFleetInstancesPaginatePaginationConfigTypeDef,
    DescribeSpotFleetInstancesPaginateResponseTypeDef,
    DescribeSpotFleetRequestsPaginatePaginationConfigTypeDef,
    DescribeSpotFleetRequestsPaginateResponseTypeDef,
    DescribeSpotInstanceRequestsPaginateFiltersTypeDef,
    DescribeSpotInstanceRequestsPaginatePaginationConfigTypeDef,
    DescribeSpotInstanceRequestsPaginateResponseTypeDef,
    DescribeSpotPriceHistoryPaginateFiltersTypeDef,
    DescribeSpotPriceHistoryPaginatePaginationConfigTypeDef,
    DescribeSpotPriceHistoryPaginateResponseTypeDef,
    DescribeStaleSecurityGroupsPaginatePaginationConfigTypeDef,
    DescribeStaleSecurityGroupsPaginateResponseTypeDef,
    DescribeSubnetsPaginateFiltersTypeDef,
    DescribeSubnetsPaginatePaginationConfigTypeDef,
    DescribeSubnetsPaginateResponseTypeDef,
    DescribeTagsPaginateFiltersTypeDef,
    DescribeTagsPaginatePaginationConfigTypeDef,
    DescribeTagsPaginateResponseTypeDef,
    DescribeTrafficMirrorFiltersPaginateFiltersTypeDef,
    DescribeTrafficMirrorFiltersPaginatePaginationConfigTypeDef,
    DescribeTrafficMirrorFiltersPaginateResponseTypeDef,
    DescribeTrafficMirrorSessionsPaginateFiltersTypeDef,
    DescribeTrafficMirrorSessionsPaginatePaginationConfigTypeDef,
    DescribeTrafficMirrorSessionsPaginateResponseTypeDef,
    DescribeTrafficMirrorTargetsPaginateFiltersTypeDef,
    DescribeTrafficMirrorTargetsPaginatePaginationConfigTypeDef,
    DescribeTrafficMirrorTargetsPaginateResponseTypeDef,
    DescribeTransitGatewayAttachmentsPaginateFiltersTypeDef,
    DescribeTransitGatewayAttachmentsPaginatePaginationConfigTypeDef,
    DescribeTransitGatewayAttachmentsPaginateResponseTypeDef,
    DescribeTransitGatewayRouteTablesPaginateFiltersTypeDef,
    DescribeTransitGatewayRouteTablesPaginatePaginationConfigTypeDef,
    DescribeTransitGatewayRouteTablesPaginateResponseTypeDef,
    DescribeTransitGatewayVpcAttachmentsPaginateFiltersTypeDef,
    DescribeTransitGatewayVpcAttachmentsPaginatePaginationConfigTypeDef,
    DescribeTransitGatewayVpcAttachmentsPaginateResponseTypeDef,
    DescribeTransitGatewaysPaginateFiltersTypeDef,
    DescribeTransitGatewaysPaginatePaginationConfigTypeDef,
    DescribeTransitGatewaysPaginateResponseTypeDef,
    DescribeVolumeStatusPaginateFiltersTypeDef,
    DescribeVolumeStatusPaginatePaginationConfigTypeDef,
    DescribeVolumeStatusPaginateResponseTypeDef,
    DescribeVolumesModificationsPaginateFiltersTypeDef,
    DescribeVolumesModificationsPaginatePaginationConfigTypeDef,
    DescribeVolumesModificationsPaginateResponseTypeDef,
    DescribeVolumesPaginateFiltersTypeDef,
    DescribeVolumesPaginatePaginationConfigTypeDef,
    DescribeVolumesPaginateResponseTypeDef,
    DescribeVpcClassicLinkDnsSupportPaginatePaginationConfigTypeDef,
    DescribeVpcClassicLinkDnsSupportPaginateResponseTypeDef,
    DescribeVpcEndpointConnectionNotificationsPaginateFiltersTypeDef,
    DescribeVpcEndpointConnectionNotificationsPaginatePaginationConfigTypeDef,
    DescribeVpcEndpointConnectionNotificationsPaginateResponseTypeDef,
    DescribeVpcEndpointConnectionsPaginateFiltersTypeDef,
    DescribeVpcEndpointConnectionsPaginatePaginationConfigTypeDef,
    DescribeVpcEndpointConnectionsPaginateResponseTypeDef,
    DescribeVpcEndpointServiceConfigurationsPaginateFiltersTypeDef,
    DescribeVpcEndpointServiceConfigurationsPaginatePaginationConfigTypeDef,
    DescribeVpcEndpointServiceConfigurationsPaginateResponseTypeDef,
    DescribeVpcEndpointServicePermissionsPaginateFiltersTypeDef,
    DescribeVpcEndpointServicePermissionsPaginatePaginationConfigTypeDef,
    DescribeVpcEndpointServicePermissionsPaginateResponseTypeDef,
    DescribeVpcEndpointServicesPaginateFiltersTypeDef,
    DescribeVpcEndpointServicesPaginatePaginationConfigTypeDef,
    DescribeVpcEndpointServicesPaginateResponseTypeDef,
    DescribeVpcEndpointsPaginateFiltersTypeDef,
    DescribeVpcEndpointsPaginatePaginationConfigTypeDef,
    DescribeVpcEndpointsPaginateResponseTypeDef,
    DescribeVpcPeeringConnectionsPaginateFiltersTypeDef,
    DescribeVpcPeeringConnectionsPaginatePaginationConfigTypeDef,
    DescribeVpcPeeringConnectionsPaginateResponseTypeDef,
    DescribeVpcsPaginateFiltersTypeDef,
    DescribeVpcsPaginatePaginationConfigTypeDef,
    DescribeVpcsPaginateResponseTypeDef,
    GetTransitGatewayAttachmentPropagationsPaginateFiltersTypeDef,
    GetTransitGatewayAttachmentPropagationsPaginatePaginationConfigTypeDef,
    GetTransitGatewayAttachmentPropagationsPaginateResponseTypeDef,
    GetTransitGatewayRouteTableAssociationsPaginateFiltersTypeDef,
    GetTransitGatewayRouteTableAssociationsPaginatePaginationConfigTypeDef,
    GetTransitGatewayRouteTableAssociationsPaginateResponseTypeDef,
    GetTransitGatewayRouteTablePropagationsPaginateFiltersTypeDef,
    GetTransitGatewayRouteTablePropagationsPaginatePaginationConfigTypeDef,
    GetTransitGatewayRouteTablePropagationsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeByoipCidrsPaginator",
    "DescribeCapacityReservationsPaginator",
    "DescribeClassicLinkInstancesPaginator",
    "DescribeClientVpnAuthorizationRulesPaginator",
    "DescribeClientVpnConnectionsPaginator",
    "DescribeClientVpnEndpointsPaginator",
    "DescribeClientVpnRoutesPaginator",
    "DescribeClientVpnTargetNetworksPaginator",
    "DescribeDhcpOptionsPaginator",
    "DescribeEgressOnlyInternetGatewaysPaginator",
    "DescribeExportImageTasksPaginator",
    "DescribeFastSnapshotRestoresPaginator",
    "DescribeFleetsPaginator",
    "DescribeFlowLogsPaginator",
    "DescribeFpgaImagesPaginator",
    "DescribeHostReservationOfferingsPaginator",
    "DescribeHostReservationsPaginator",
    "DescribeHostsPaginator",
    "DescribeIamInstanceProfileAssociationsPaginator",
    "DescribeImportImageTasksPaginator",
    "DescribeImportSnapshotTasksPaginator",
    "DescribeInstanceCreditSpecificationsPaginator",
    "DescribeInstanceStatusPaginator",
    "DescribeInstancesPaginator",
    "DescribeInternetGatewaysPaginator",
    "DescribeLaunchTemplateVersionsPaginator",
    "DescribeLaunchTemplatesPaginator",
    "DescribeMovingAddressesPaginator",
    "DescribeNatGatewaysPaginator",
    "DescribeNetworkAclsPaginator",
    "DescribeNetworkInterfacePermissionsPaginator",
    "DescribeNetworkInterfacesPaginator",
    "DescribePrefixListsPaginator",
    "DescribePrincipalIdFormatPaginator",
    "DescribePublicIpv4PoolsPaginator",
    "DescribeReservedInstancesModificationsPaginator",
    "DescribeReservedInstancesOfferingsPaginator",
    "DescribeRouteTablesPaginator",
    "DescribeScheduledInstanceAvailabilityPaginator",
    "DescribeScheduledInstancesPaginator",
    "DescribeSecurityGroupsPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeSpotFleetInstancesPaginator",
    "DescribeSpotFleetRequestsPaginator",
    "DescribeSpotInstanceRequestsPaginator",
    "DescribeSpotPriceHistoryPaginator",
    "DescribeStaleSecurityGroupsPaginator",
    "DescribeSubnetsPaginator",
    "DescribeTagsPaginator",
    "DescribeTrafficMirrorFiltersPaginator",
    "DescribeTrafficMirrorSessionsPaginator",
    "DescribeTrafficMirrorTargetsPaginator",
    "DescribeTransitGatewayAttachmentsPaginator",
    "DescribeTransitGatewayRouteTablesPaginator",
    "DescribeTransitGatewayVpcAttachmentsPaginator",
    "DescribeTransitGatewaysPaginator",
    "DescribeVolumeStatusPaginator",
    "DescribeVolumesPaginator",
    "DescribeVolumesModificationsPaginator",
    "DescribeVpcClassicLinkDnsSupportPaginator",
    "DescribeVpcEndpointConnectionNotificationsPaginator",
    "DescribeVpcEndpointConnectionsPaginator",
    "DescribeVpcEndpointServiceConfigurationsPaginator",
    "DescribeVpcEndpointServicePermissionsPaginator",
    "DescribeVpcEndpointServicesPaginator",
    "DescribeVpcEndpointsPaginator",
    "DescribeVpcPeeringConnectionsPaginator",
    "DescribeVpcsPaginator",
    "GetTransitGatewayAttachmentPropagationsPaginator",
    "GetTransitGatewayRouteTableAssociationsPaginator",
    "GetTransitGatewayRouteTablePropagationsPaginator",
)


class DescribeByoipCidrsPaginator(Boto3Paginator):
    """
    Paginator for `describe_byoip_cidrs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        PaginationConfig: DescribeByoipCidrsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeByoipCidrsPaginateResponseTypeDef:
        """
        [DescribeByoipCidrs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeByoipCidrs.paginate)
        """


class DescribeCapacityReservationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_capacity_reservations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CapacityReservationIds: List[str] = None,
        Filters: List[DescribeCapacityReservationsPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeCapacityReservationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCapacityReservationsPaginateResponseTypeDef:
        """
        [DescribeCapacityReservations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservations.paginate)
        """


class DescribeClassicLinkInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_classic_link_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeClassicLinkInstancesPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        InstanceIds: List[str] = None,
        PaginationConfig: DescribeClassicLinkInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClassicLinkInstancesPaginateResponseTypeDef:
        """
        [DescribeClassicLinkInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeClassicLinkInstances.paginate)
        """


class DescribeClientVpnAuthorizationRulesPaginator(Boto3Paginator):
    """
    Paginator for `describe_client_vpn_authorization_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClientVpnEndpointId: str,
        DryRun: bool = None,
        Filters: List[DescribeClientVpnAuthorizationRulesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeClientVpnAuthorizationRulesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClientVpnAuthorizationRulesPaginateResponseTypeDef:
        """
        [DescribeClientVpnAuthorizationRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnAuthorizationRules.paginate)
        """


class DescribeClientVpnConnectionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_client_vpn_connections`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClientVpnEndpointId: str,
        Filters: List[DescribeClientVpnConnectionsPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeClientVpnConnectionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClientVpnConnectionsPaginateResponseTypeDef:
        """
        [DescribeClientVpnConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnConnections.paginate)
        """


class DescribeClientVpnEndpointsPaginator(Boto3Paginator):
    """
    Paginator for `describe_client_vpn_endpoints`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClientVpnEndpointIds: List[str] = None,
        Filters: List[DescribeClientVpnEndpointsPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeClientVpnEndpointsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClientVpnEndpointsPaginateResponseTypeDef:
        """
        [DescribeClientVpnEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnEndpoints.paginate)
        """


class DescribeClientVpnRoutesPaginator(Boto3Paginator):
    """
    Paginator for `describe_client_vpn_routes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClientVpnEndpointId: str,
        Filters: List[DescribeClientVpnRoutesPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeClientVpnRoutesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClientVpnRoutesPaginateResponseTypeDef:
        """
        [DescribeClientVpnRoutes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnRoutes.paginate)
        """


class DescribeClientVpnTargetNetworksPaginator(Boto3Paginator):
    """
    Paginator for `describe_client_vpn_target_networks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClientVpnEndpointId: str,
        AssociationIds: List[str] = None,
        Filters: List[DescribeClientVpnTargetNetworksPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeClientVpnTargetNetworksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClientVpnTargetNetworksPaginateResponseTypeDef:
        """
        [DescribeClientVpnTargetNetworks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnTargetNetworks.paginate)
        """


class DescribeDhcpOptionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_dhcp_options`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DhcpOptionsIds: List[str] = None,
        Filters: List[DescribeDhcpOptionsPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeDhcpOptionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDhcpOptionsPaginateResponseTypeDef:
        """
        [DescribeDhcpOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeDhcpOptions.paginate)
        """


class DescribeEgressOnlyInternetGatewaysPaginator(Boto3Paginator):
    """
    Paginator for `describe_egress_only_internet_gateways`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        EgressOnlyInternetGatewayIds: List[str] = None,
        PaginationConfig: DescribeEgressOnlyInternetGatewaysPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEgressOnlyInternetGatewaysPaginateResponseTypeDef:
        """
        [DescribeEgressOnlyInternetGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeEgressOnlyInternetGateways.paginate)
        """


class DescribeExportImageTasksPaginator(Boto3Paginator):
    """
    Paginator for `describe_export_image_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[DescribeExportImageTasksPaginateFiltersTypeDef] = None,
        ExportImageTaskIds: List[str] = None,
        PaginationConfig: DescribeExportImageTasksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeExportImageTasksPaginateResponseTypeDef:
        """
        [DescribeExportImageTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeExportImageTasks.paginate)
        """


class DescribeFastSnapshotRestoresPaginator(Boto3Paginator):
    """
    Paginator for `describe_fast_snapshot_restores`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeFastSnapshotRestoresPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeFastSnapshotRestoresPaginatePaginationConfigTypeDef = None,
    ) -> DescribeFastSnapshotRestoresPaginateResponseTypeDef:
        """
        [DescribeFastSnapshotRestores.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeFastSnapshotRestores.paginate)
        """


class DescribeFleetsPaginator(Boto3Paginator):
    """
    Paginator for `describe_fleets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        FleetIds: List[str] = None,
        Filters: List[DescribeFleetsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeFleetsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeFleetsPaginateResponseTypeDef:
        """
        [DescribeFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeFleets.paginate)
        """


class DescribeFlowLogsPaginator(Boto3Paginator):
    """
    Paginator for `describe_flow_logs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[DescribeFlowLogsPaginateFiltersTypeDef] = None,
        FlowLogIds: List[str] = None,
        PaginationConfig: DescribeFlowLogsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeFlowLogsPaginateResponseTypeDef:
        """
        [DescribeFlowLogs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeFlowLogs.paginate)
        """


class DescribeFpgaImagesPaginator(Boto3Paginator):
    """
    Paginator for `describe_fpga_images`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        FpgaImageIds: List[str] = None,
        Owners: List[str] = None,
        Filters: List[DescribeFpgaImagesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeFpgaImagesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeFpgaImagesPaginateResponseTypeDef:
        """
        [DescribeFpgaImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeFpgaImages.paginate)
        """


class DescribeHostReservationOfferingsPaginator(Boto3Paginator):
    """
    Paginator for `describe_host_reservation_offerings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeHostReservationOfferingsPaginateFiltersTypeDef] = None,
        MaxDuration: int = None,
        MinDuration: int = None,
        OfferingId: str = None,
        PaginationConfig: DescribeHostReservationOfferingsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeHostReservationOfferingsPaginateResponseTypeDef:
        """
        [DescribeHostReservationOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeHostReservationOfferings.paginate)
        """


class DescribeHostReservationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_host_reservations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeHostReservationsPaginateFiltersTypeDef] = None,
        HostReservationIdSet: List[str] = None,
        PaginationConfig: DescribeHostReservationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeHostReservationsPaginateResponseTypeDef:
        """
        [DescribeHostReservations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeHostReservations.paginate)
        """


class DescribeHostsPaginator(Boto3Paginator):
    """
    Paginator for `describe_hosts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeHostsPaginateFiltersTypeDef] = None,
        HostIds: List[str] = None,
        PaginationConfig: DescribeHostsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeHostsPaginateResponseTypeDef:
        """
        [DescribeHosts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeHosts.paginate)
        """


class DescribeIamInstanceProfileAssociationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_iam_instance_profile_associations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AssociationIds: List[str] = None,
        Filters: List[DescribeIamInstanceProfileAssociationsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeIamInstanceProfileAssociationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeIamInstanceProfileAssociationsPaginateResponseTypeDef:
        """
        [DescribeIamInstanceProfileAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeIamInstanceProfileAssociations.paginate)
        """


class DescribeImportImageTasksPaginator(Boto3Paginator):
    """
    Paginator for `describe_import_image_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[DescribeImportImageTasksPaginateFiltersTypeDef] = None,
        ImportTaskIds: List[str] = None,
        PaginationConfig: DescribeImportImageTasksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeImportImageTasksPaginateResponseTypeDef:
        """
        [DescribeImportImageTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeImportImageTasks.paginate)
        """


class DescribeImportSnapshotTasksPaginator(Boto3Paginator):
    """
    Paginator for `describe_import_snapshot_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[DescribeImportSnapshotTasksPaginateFiltersTypeDef] = None,
        ImportTaskIds: List[str] = None,
        PaginationConfig: DescribeImportSnapshotTasksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeImportSnapshotTasksPaginateResponseTypeDef:
        """
        [DescribeImportSnapshotTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeImportSnapshotTasks.paginate)
        """


class DescribeInstanceCreditSpecificationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_instance_credit_specifications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[DescribeInstanceCreditSpecificationsPaginateFiltersTypeDef] = None,
        InstanceIds: List[str] = None,
        PaginationConfig: DescribeInstanceCreditSpecificationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeInstanceCreditSpecificationsPaginateResponseTypeDef:
        """
        [DescribeInstanceCreditSpecifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeInstanceCreditSpecifications.paginate)
        """


class DescribeInstanceStatusPaginator(Boto3Paginator):
    """
    Paginator for `describe_instance_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeInstanceStatusPaginateFiltersTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        PaginationConfig: DescribeInstanceStatusPaginatePaginationConfigTypeDef = None,
    ) -> DescribeInstanceStatusPaginateResponseTypeDef:
        """
        [DescribeInstanceStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeInstanceStatus.paginate)
        """


class DescribeInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeInstancesPaginateFiltersTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeInstancesPaginateResponseTypeDef:
        """
        [DescribeInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeInstances.paginate)
        """


class DescribeInternetGatewaysPaginator(Boto3Paginator):
    """
    Paginator for `describe_internet_gateways`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeInternetGatewaysPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        PaginationConfig: DescribeInternetGatewaysPaginatePaginationConfigTypeDef = None,
    ) -> DescribeInternetGatewaysPaginateResponseTypeDef:
        """
        [DescribeInternetGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeInternetGateways.paginate)
        """


class DescribeLaunchTemplateVersionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_launch_template_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        Versions: List[str] = None,
        MinVersion: str = None,
        MaxVersion: str = None,
        Filters: List[DescribeLaunchTemplateVersionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeLaunchTemplateVersionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeLaunchTemplateVersionsPaginateResponseTypeDef:
        """
        [DescribeLaunchTemplateVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplateVersions.paginate)
        """


class DescribeLaunchTemplatesPaginator(Boto3Paginator):
    """
    Paginator for `describe_launch_templates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        LaunchTemplateIds: List[str] = None,
        LaunchTemplateNames: List[str] = None,
        Filters: List[DescribeLaunchTemplatesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeLaunchTemplatesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeLaunchTemplatesPaginateResponseTypeDef:
        """
        [DescribeLaunchTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplates.paginate)
        """


class DescribeMovingAddressesPaginator(Boto3Paginator):
    """
    Paginator for `describe_moving_addresses`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeMovingAddressesPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PublicIps: List[str] = None,
        PaginationConfig: DescribeMovingAddressesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeMovingAddressesPaginateResponseTypeDef:
        """
        [DescribeMovingAddresses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeMovingAddresses.paginate)
        """


class DescribeNatGatewaysPaginator(Boto3Paginator):
    """
    Paginator for `describe_nat_gateways`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeNatGatewaysPaginateFiltersTypeDef] = None,
        NatGatewayIds: List[str] = None,
        PaginationConfig: DescribeNatGatewaysPaginatePaginationConfigTypeDef = None,
    ) -> DescribeNatGatewaysPaginateResponseTypeDef:
        """
        [DescribeNatGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeNatGateways.paginate)
        """


class DescribeNetworkAclsPaginator(Boto3Paginator):
    """
    Paginator for `describe_network_acls`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeNetworkAclsPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        PaginationConfig: DescribeNetworkAclsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeNetworkAclsPaginateResponseTypeDef:
        """
        [DescribeNetworkAcls.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeNetworkAcls.paginate)
        """


class DescribeNetworkInterfacePermissionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_network_interface_permissions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        NetworkInterfacePermissionIds: List[str] = None,
        Filters: List[DescribeNetworkInterfacePermissionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeNetworkInterfacePermissionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeNetworkInterfacePermissionsPaginateResponseTypeDef:
        """
        [DescribeNetworkInterfacePermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfacePermissions.paginate)
        """


class DescribeNetworkInterfacesPaginator(Boto3Paginator):
    """
    Paginator for `describe_network_interfaces`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeNetworkInterfacesPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        PaginationConfig: DescribeNetworkInterfacesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeNetworkInterfacesPaginateResponseTypeDef:
        """
        [DescribeNetworkInterfaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfaces.paginate)
        """


class DescribePrefixListsPaginator(Boto3Paginator):
    """
    Paginator for `describe_prefix_lists`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[DescribePrefixListsPaginateFiltersTypeDef] = None,
        PrefixListIds: List[str] = None,
        PaginationConfig: DescribePrefixListsPaginatePaginationConfigTypeDef = None,
    ) -> DescribePrefixListsPaginateResponseTypeDef:
        """
        [DescribePrefixLists.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribePrefixLists.paginate)
        """


class DescribePrincipalIdFormatPaginator(Boto3Paginator):
    """
    Paginator for `describe_principal_id_format`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Resources: List[str] = None,
        PaginationConfig: DescribePrincipalIdFormatPaginatePaginationConfigTypeDef = None,
    ) -> DescribePrincipalIdFormatPaginateResponseTypeDef:
        """
        [DescribePrincipalIdFormat.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribePrincipalIdFormat.paginate)
        """


class DescribePublicIpv4PoolsPaginator(Boto3Paginator):
    """
    Paginator for `describe_public_ipv4_pools`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PoolIds: List[str] = None,
        PaginationConfig: DescribePublicIpv4PoolsPaginatePaginationConfigTypeDef = None,
    ) -> DescribePublicIpv4PoolsPaginateResponseTypeDef:
        """
        [DescribePublicIpv4Pools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribePublicIpv4Pools.paginate)
        """


class DescribeReservedInstancesModificationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_reserved_instances_modifications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeReservedInstancesModificationsPaginateFiltersTypeDef] = None,
        ReservedInstancesModificationIds: List[str] = None,
        PaginationConfig: DescribeReservedInstancesModificationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReservedInstancesModificationsPaginateResponseTypeDef:
        """
        [DescribeReservedInstancesModifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesModifications.paginate)
        """


class DescribeReservedInstancesOfferingsPaginator(Boto3Paginator):
    """
    Paginator for `describe_reserved_instances_offerings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AvailabilityZone: str = None,
        Filters: List[DescribeReservedInstancesOfferingsPaginateFiltersTypeDef] = None,
        IncludeMarketplace: bool = None,
        InstanceType: Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
        ] = None,
        MaxDuration: int = None,
        MaxInstanceCount: int = None,
        MinDuration: int = None,
        OfferingClass: Literal["standard", "convertible"] = None,
        ProductDescription: Literal[
            "Linux/UNIX", "Linux/UNIX (Amazon VPC)", "Windows", "Windows (Amazon VPC)"
        ] = None,
        ReservedInstancesOfferingIds: List[str] = None,
        DryRun: bool = None,
        InstanceTenancy: Literal["default", "dedicated", "host"] = None,
        OfferingType: Literal[
            "Heavy Utilization",
            "Medium Utilization",
            "Light Utilization",
            "No Upfront",
            "Partial Upfront",
            "All Upfront",
        ] = None,
        PaginationConfig: DescribeReservedInstancesOfferingsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReservedInstancesOfferingsPaginateResponseTypeDef:
        """
        [DescribeReservedInstancesOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesOfferings.paginate)
        """


class DescribeRouteTablesPaginator(Boto3Paginator):
    """
    Paginator for `describe_route_tables`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeRouteTablesPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        PaginationConfig: DescribeRouteTablesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeRouteTablesPaginateResponseTypeDef:
        """
        [DescribeRouteTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeRouteTables.paginate)
        """


class DescribeScheduledInstanceAvailabilityPaginator(Boto3Paginator):
    """
    Paginator for `describe_scheduled_instance_availability`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FirstSlotStartTimeRange: DescribeScheduledInstanceAvailabilityPaginateFirstSlotStartTimeRangeTypeDef,
        Recurrence: DescribeScheduledInstanceAvailabilityPaginateRecurrenceTypeDef,
        DryRun: bool = None,
        Filters: List[DescribeScheduledInstanceAvailabilityPaginateFiltersTypeDef] = None,
        MaxSlotDurationInHours: int = None,
        MinSlotDurationInHours: int = None,
        PaginationConfig: DescribeScheduledInstanceAvailabilityPaginatePaginationConfigTypeDef = None,
    ) -> DescribeScheduledInstanceAvailabilityPaginateResponseTypeDef:
        """
        [DescribeScheduledInstanceAvailability.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstanceAvailability.paginate)
        """


class DescribeScheduledInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_scheduled_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[DescribeScheduledInstancesPaginateFiltersTypeDef] = None,
        ScheduledInstanceIds: List[str] = None,
        SlotStartTimeRange: DescribeScheduledInstancesPaginateSlotStartTimeRangeTypeDef = None,
        PaginationConfig: DescribeScheduledInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeScheduledInstancesPaginateResponseTypeDef:
        """
        [DescribeScheduledInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstances.paginate)
        """


class DescribeSecurityGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_security_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeSecurityGroupsPaginateFiltersTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeSecurityGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSecurityGroupsPaginateResponseTypeDef:
        """
        [DescribeSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroups.paginate)
        """


class DescribeSnapshotsPaginator(Boto3Paginator):
    """
    Paginator for `describe_snapshots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeSnapshotsPaginateFiltersTypeDef] = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeSnapshotsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSnapshotsPaginateResponseTypeDef:
        """
        [DescribeSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeSnapshots.paginate)
        """


class DescribeSpotFleetInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_spot_fleet_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SpotFleetRequestId: str,
        DryRun: bool = None,
        PaginationConfig: DescribeSpotFleetInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSpotFleetInstancesPaginateResponseTypeDef:
        """
        [DescribeSpotFleetInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetInstances.paginate)
        """


class DescribeSpotFleetRequestsPaginator(Boto3Paginator):
    """
    Paginator for `describe_spot_fleet_requests`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        SpotFleetRequestIds: List[str] = None,
        PaginationConfig: DescribeSpotFleetRequestsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSpotFleetRequestsPaginateResponseTypeDef:
        """
        [DescribeSpotFleetRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetRequests.paginate)
        """


class DescribeSpotInstanceRequestsPaginator(Boto3Paginator):
    """
    Paginator for `describe_spot_instance_requests`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeSpotInstanceRequestsPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[str] = None,
        PaginationConfig: DescribeSpotInstanceRequestsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSpotInstanceRequestsPaginateResponseTypeDef:
        """
        [DescribeSpotInstanceRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeSpotInstanceRequests.paginate)
        """


class DescribeSpotPriceHistoryPaginator(Boto3Paginator):
    """
    Paginator for `describe_spot_price_history`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeSpotPriceHistoryPaginateFiltersTypeDef] = None,
        AvailabilityZone: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        InstanceTypes: List[
            Literal[
                "t1.micro",
                "t2.nano",
                "t2.micro",
                "t2.small",
                "t2.medium",
                "t2.large",
                "t2.xlarge",
                "t2.2xlarge",
                "t3.nano",
                "t3.micro",
                "t3.small",
                "t3.medium",
                "t3.large",
                "t3.xlarge",
                "t3.2xlarge",
                "t3a.nano",
                "t3a.micro",
                "t3a.small",
                "t3a.medium",
                "t3a.large",
                "t3a.xlarge",
                "t3a.2xlarge",
                "m1.small",
                "m1.medium",
                "m1.large",
                "m1.xlarge",
                "m3.medium",
                "m3.large",
                "m3.xlarge",
                "m3.2xlarge",
                "m4.large",
                "m4.xlarge",
                "m4.2xlarge",
                "m4.4xlarge",
                "m4.10xlarge",
                "m4.16xlarge",
                "m2.xlarge",
                "m2.2xlarge",
                "m2.4xlarge",
                "cr1.8xlarge",
                "r3.large",
                "r3.xlarge",
                "r3.2xlarge",
                "r3.4xlarge",
                "r3.8xlarge",
                "r4.large",
                "r4.xlarge",
                "r4.2xlarge",
                "r4.4xlarge",
                "r4.8xlarge",
                "r4.16xlarge",
                "r5.large",
                "r5.xlarge",
                "r5.2xlarge",
                "r5.4xlarge",
                "r5.8xlarge",
                "r5.12xlarge",
                "r5.16xlarge",
                "r5.24xlarge",
                "r5.metal",
                "r5a.large",
                "r5a.xlarge",
                "r5a.2xlarge",
                "r5a.4xlarge",
                "r5a.8xlarge",
                "r5a.12xlarge",
                "r5a.16xlarge",
                "r5a.24xlarge",
                "r5d.large",
                "r5d.xlarge",
                "r5d.2xlarge",
                "r5d.4xlarge",
                "r5d.8xlarge",
                "r5d.12xlarge",
                "r5d.16xlarge",
                "r5d.24xlarge",
                "r5d.metal",
                "r5ad.large",
                "r5ad.xlarge",
                "r5ad.2xlarge",
                "r5ad.4xlarge",
                "r5ad.8xlarge",
                "r5ad.12xlarge",
                "r5ad.16xlarge",
                "r5ad.24xlarge",
                "x1.16xlarge",
                "x1.32xlarge",
                "x1e.xlarge",
                "x1e.2xlarge",
                "x1e.4xlarge",
                "x1e.8xlarge",
                "x1e.16xlarge",
                "x1e.32xlarge",
                "i2.xlarge",
                "i2.2xlarge",
                "i2.4xlarge",
                "i2.8xlarge",
                "i3.large",
                "i3.xlarge",
                "i3.2xlarge",
                "i3.4xlarge",
                "i3.8xlarge",
                "i3.16xlarge",
                "i3.metal",
                "i3en.large",
                "i3en.xlarge",
                "i3en.2xlarge",
                "i3en.3xlarge",
                "i3en.6xlarge",
                "i3en.12xlarge",
                "i3en.24xlarge",
                "i3en.metal",
                "hi1.4xlarge",
                "hs1.8xlarge",
                "c1.medium",
                "c1.xlarge",
                "c3.large",
                "c3.xlarge",
                "c3.2xlarge",
                "c3.4xlarge",
                "c3.8xlarge",
                "c4.large",
                "c4.xlarge",
                "c4.2xlarge",
                "c4.4xlarge",
                "c4.8xlarge",
                "c5.large",
                "c5.xlarge",
                "c5.2xlarge",
                "c5.4xlarge",
                "c5.9xlarge",
                "c5.12xlarge",
                "c5.18xlarge",
                "c5.24xlarge",
                "c5.metal",
                "c5d.large",
                "c5d.xlarge",
                "c5d.2xlarge",
                "c5d.4xlarge",
                "c5d.9xlarge",
                "c5d.12xlarge",
                "c5d.18xlarge",
                "c5d.24xlarge",
                "c5d.metal",
                "c5n.large",
                "c5n.xlarge",
                "c5n.2xlarge",
                "c5n.4xlarge",
                "c5n.9xlarge",
                "c5n.18xlarge",
                "cc1.4xlarge",
                "cc2.8xlarge",
                "g2.2xlarge",
                "g2.8xlarge",
                "g3.4xlarge",
                "g3.8xlarge",
                "g3.16xlarge",
                "g3s.xlarge",
                "g4dn.xlarge",
                "g4dn.2xlarge",
                "g4dn.4xlarge",
                "g4dn.8xlarge",
                "g4dn.12xlarge",
                "g4dn.16xlarge",
                "cg1.4xlarge",
                "p2.xlarge",
                "p2.8xlarge",
                "p2.16xlarge",
                "p3.2xlarge",
                "p3.8xlarge",
                "p3.16xlarge",
                "p3dn.24xlarge",
                "d2.xlarge",
                "d2.2xlarge",
                "d2.4xlarge",
                "d2.8xlarge",
                "f1.2xlarge",
                "f1.4xlarge",
                "f1.16xlarge",
                "m5.large",
                "m5.xlarge",
                "m5.2xlarge",
                "m5.4xlarge",
                "m5.8xlarge",
                "m5.12xlarge",
                "m5.16xlarge",
                "m5.24xlarge",
                "m5.metal",
                "m5a.large",
                "m5a.xlarge",
                "m5a.2xlarge",
                "m5a.4xlarge",
                "m5a.8xlarge",
                "m5a.12xlarge",
                "m5a.16xlarge",
                "m5a.24xlarge",
                "m5d.large",
                "m5d.xlarge",
                "m5d.2xlarge",
                "m5d.4xlarge",
                "m5d.8xlarge",
                "m5d.12xlarge",
                "m5d.16xlarge",
                "m5d.24xlarge",
                "m5d.metal",
                "m5ad.large",
                "m5ad.xlarge",
                "m5ad.2xlarge",
                "m5ad.4xlarge",
                "m5ad.8xlarge",
                "m5ad.12xlarge",
                "m5ad.16xlarge",
                "m5ad.24xlarge",
                "h1.2xlarge",
                "h1.4xlarge",
                "h1.8xlarge",
                "h1.16xlarge",
                "z1d.large",
                "z1d.xlarge",
                "z1d.2xlarge",
                "z1d.3xlarge",
                "z1d.6xlarge",
                "z1d.12xlarge",
                "z1d.metal",
                "u-6tb1.metal",
                "u-9tb1.metal",
                "u-12tb1.metal",
                "u-18tb1.metal",
                "u-24tb1.metal",
                "a1.medium",
                "a1.large",
                "a1.xlarge",
                "a1.2xlarge",
                "a1.4xlarge",
                "a1.metal",
                "m5dn.large",
                "m5dn.xlarge",
                "m5dn.2xlarge",
                "m5dn.4xlarge",
                "m5dn.8xlarge",
                "m5dn.12xlarge",
                "m5dn.16xlarge",
                "m5dn.24xlarge",
                "m5n.large",
                "m5n.xlarge",
                "m5n.2xlarge",
                "m5n.4xlarge",
                "m5n.8xlarge",
                "m5n.12xlarge",
                "m5n.16xlarge",
                "m5n.24xlarge",
                "r5dn.large",
                "r5dn.xlarge",
                "r5dn.2xlarge",
                "r5dn.4xlarge",
                "r5dn.8xlarge",
                "r5dn.12xlarge",
                "r5dn.16xlarge",
                "r5dn.24xlarge",
                "r5n.large",
                "r5n.xlarge",
                "r5n.2xlarge",
                "r5n.4xlarge",
                "r5n.8xlarge",
                "r5n.12xlarge",
                "r5n.16xlarge",
                "r5n.24xlarge",
                "inf1.xlarge",
                "inf1.2xlarge",
                "inf1.6xlarge",
                "inf1.24xlarge",
            ]
        ] = None,
        ProductDescriptions: List[str] = None,
        StartTime: datetime = None,
        PaginationConfig: DescribeSpotPriceHistoryPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSpotPriceHistoryPaginateResponseTypeDef:
        """
        [DescribeSpotPriceHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeSpotPriceHistory.paginate)
        """


class DescribeStaleSecurityGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_stale_security_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        VpcId: str,
        DryRun: bool = None,
        PaginationConfig: DescribeStaleSecurityGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeStaleSecurityGroupsPaginateResponseTypeDef:
        """
        [DescribeStaleSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeStaleSecurityGroups.paginate)
        """


class DescribeSubnetsPaginator(Boto3Paginator):
    """
    Paginator for `describe_subnets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeSubnetsPaginateFiltersTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeSubnetsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSubnetsPaginateResponseTypeDef:
        """
        [DescribeSubnets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeSubnets.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    Paginator for `describe_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[DescribeTagsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeTagsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTagsPaginateResponseTypeDef:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeTags.paginate)
        """


class DescribeTrafficMirrorFiltersPaginator(Boto3Paginator):
    """
    Paginator for `describe_traffic_mirror_filters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TrafficMirrorFilterIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[DescribeTrafficMirrorFiltersPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeTrafficMirrorFiltersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTrafficMirrorFiltersPaginateResponseTypeDef:
        """
        [DescribeTrafficMirrorFilters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorFilters.paginate)
        """


class DescribeTrafficMirrorSessionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_traffic_mirror_sessions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TrafficMirrorSessionIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[DescribeTrafficMirrorSessionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeTrafficMirrorSessionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTrafficMirrorSessionsPaginateResponseTypeDef:
        """
        [DescribeTrafficMirrorSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorSessions.paginate)
        """


class DescribeTrafficMirrorTargetsPaginator(Boto3Paginator):
    """
    Paginator for `describe_traffic_mirror_targets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TrafficMirrorTargetIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[DescribeTrafficMirrorTargetsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeTrafficMirrorTargetsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTrafficMirrorTargetsPaginateResponseTypeDef:
        """
        [DescribeTrafficMirrorTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorTargets.paginate)
        """


class DescribeTransitGatewayAttachmentsPaginator(Boto3Paginator):
    """
    Paginator for `describe_transit_gateway_attachments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[DescribeTransitGatewayAttachmentsPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeTransitGatewayAttachmentsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTransitGatewayAttachmentsPaginateResponseTypeDef:
        """
        [DescribeTransitGatewayAttachments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayAttachments.paginate)
        """


class DescribeTransitGatewayRouteTablesPaginator(Boto3Paginator):
    """
    Paginator for `describe_transit_gateway_route_tables`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayRouteTableIds: List[str] = None,
        Filters: List[DescribeTransitGatewayRouteTablesPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeTransitGatewayRouteTablesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTransitGatewayRouteTablesPaginateResponseTypeDef:
        """
        [DescribeTransitGatewayRouteTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTables.paginate)
        """


class DescribeTransitGatewayVpcAttachmentsPaginator(Boto3Paginator):
    """
    Paginator for `describe_transit_gateway_vpc_attachments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[DescribeTransitGatewayVpcAttachmentsPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeTransitGatewayVpcAttachmentsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTransitGatewayVpcAttachmentsPaginateResponseTypeDef:
        """
        [DescribeTransitGatewayVpcAttachments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments.paginate)
        """


class DescribeTransitGatewaysPaginator(Boto3Paginator):
    """
    Paginator for `describe_transit_gateways`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayIds: List[str] = None,
        Filters: List[DescribeTransitGatewaysPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeTransitGatewaysPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTransitGatewaysPaginateResponseTypeDef:
        """
        [DescribeTransitGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeTransitGateways.paginate)
        """


class DescribeVolumeStatusPaginator(Boto3Paginator):
    """
    Paginator for `describe_volume_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeVolumeStatusPaginateFiltersTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeVolumeStatusPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVolumeStatusPaginateResponseTypeDef:
        """
        [DescribeVolumeStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeVolumeStatus.paginate)
        """


class DescribeVolumesPaginator(Boto3Paginator):
    """
    Paginator for `describe_volumes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeVolumesPaginateFiltersTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeVolumesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVolumesPaginateResponseTypeDef:
        """
        [DescribeVolumes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeVolumes.paginate)
        """


class DescribeVolumesModificationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_volumes_modifications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        VolumeIds: List[str] = None,
        Filters: List[DescribeVolumesModificationsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeVolumesModificationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVolumesModificationsPaginateResponseTypeDef:
        """
        [DescribeVolumesModifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeVolumesModifications.paginate)
        """


class DescribeVpcClassicLinkDnsSupportPaginator(Boto3Paginator):
    """
    Paginator for `describe_vpc_classic_link_dns_support`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        VpcIds: List[str] = None,
        PaginationConfig: DescribeVpcClassicLinkDnsSupportPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVpcClassicLinkDnsSupportPaginateResponseTypeDef:
        """
        [DescribeVpcClassicLinkDnsSupport.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport.paginate)
        """


class DescribeVpcEndpointConnectionNotificationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_vpc_endpoint_connection_notifications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        ConnectionNotificationId: str = None,
        Filters: List[DescribeVpcEndpointConnectionNotificationsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeVpcEndpointConnectionNotificationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVpcEndpointConnectionNotificationsPaginateResponseTypeDef:
        """
        [DescribeVpcEndpointConnectionNotifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications.paginate)
        """


class DescribeVpcEndpointConnectionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_vpc_endpoint_connections`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[DescribeVpcEndpointConnectionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeVpcEndpointConnectionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVpcEndpointConnectionsPaginateResponseTypeDef:
        """
        [DescribeVpcEndpointConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnections.paginate)
        """


class DescribeVpcEndpointServiceConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_vpc_endpoint_service_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        ServiceIds: List[str] = None,
        Filters: List[DescribeVpcEndpointServiceConfigurationsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeVpcEndpointServiceConfigurationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVpcEndpointServiceConfigurationsPaginateResponseTypeDef:
        """
        [DescribeVpcEndpointServiceConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations.paginate)
        """


class DescribeVpcEndpointServicePermissionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_vpc_endpoint_service_permissions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceId: str,
        DryRun: bool = None,
        Filters: List[DescribeVpcEndpointServicePermissionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeVpcEndpointServicePermissionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVpcEndpointServicePermissionsPaginateResponseTypeDef:
        """
        [DescribeVpcEndpointServicePermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServicePermissions.paginate)
        """


class DescribeVpcEndpointServicesPaginator(Boto3Paginator):
    """
    Paginator for `describe_vpc_endpoint_services`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        ServiceNames: List[str] = None,
        Filters: List[DescribeVpcEndpointServicesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeVpcEndpointServicesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVpcEndpointServicesPaginateResponseTypeDef:
        """
        [DescribeVpcEndpointServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServices.paginate)
        """


class DescribeVpcEndpointsPaginator(Boto3Paginator):
    """
    Paginator for `describe_vpc_endpoints`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        VpcEndpointIds: List[str] = None,
        Filters: List[DescribeVpcEndpointsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeVpcEndpointsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVpcEndpointsPaginateResponseTypeDef:
        """
        [DescribeVpcEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpoints.paginate)
        """


class DescribeVpcPeeringConnectionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_vpc_peering_connections`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeVpcPeeringConnectionsPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        PaginationConfig: DescribeVpcPeeringConnectionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVpcPeeringConnectionsPaginateResponseTypeDef:
        """
        [DescribeVpcPeeringConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeVpcPeeringConnections.paginate)
        """


class DescribeVpcsPaginator(Boto3Paginator):
    """
    Paginator for `describe_vpcs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeVpcsPaginateFiltersTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: DescribeVpcsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVpcsPaginateResponseTypeDef:
        """
        [DescribeVpcs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.DescribeVpcs.paginate)
        """


class GetTransitGatewayAttachmentPropagationsPaginator(Boto3Paginator):
    """
    Paginator for `get_transit_gateway_attachment_propagations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayAttachmentId: str,
        Filters: List[GetTransitGatewayAttachmentPropagationsPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: GetTransitGatewayAttachmentPropagationsPaginatePaginationConfigTypeDef = None,
    ) -> GetTransitGatewayAttachmentPropagationsPaginateResponseTypeDef:
        """
        [GetTransitGatewayAttachmentPropagations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations.paginate)
        """


class GetTransitGatewayRouteTableAssociationsPaginator(Boto3Paginator):
    """
    Paginator for `get_transit_gateway_route_table_associations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[GetTransitGatewayRouteTableAssociationsPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: GetTransitGatewayRouteTableAssociationsPaginatePaginationConfigTypeDef = None,
    ) -> GetTransitGatewayRouteTableAssociationsPaginateResponseTypeDef:
        """
        [GetTransitGatewayRouteTableAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations.paginate)
        """


class GetTransitGatewayRouteTablePropagationsPaginator(Boto3Paginator):
    """
    Paginator for `get_transit_gateway_route_table_propagations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[GetTransitGatewayRouteTablePropagationsPaginateFiltersTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: GetTransitGatewayRouteTablePropagationsPaginatePaginationConfigTypeDef = None,
    ) -> GetTransitGatewayRouteTablePropagationsPaginateResponseTypeDef:
        """
        [GetTransitGatewayRouteTablePropagations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations.paginate)
        """
