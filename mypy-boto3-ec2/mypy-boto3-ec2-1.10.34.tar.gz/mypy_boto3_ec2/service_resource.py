"Main interface for ec2 service ServiceResource"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_ec2.service_resource as service_resource_scope
from mypy_boto3_ec2.type_defs import (
    ClassicAddressAssociateResponseTypeDef,
    DhcpOptionsCreateTagsTagsTypeDef,
    DhcpOptionsSetsFilterFiltersTypeDef,
    ImageCreateTagsTagsTypeDef,
    ImageDescribeAttributeResponseTypeDef,
    ImageModifyAttributeDescriptionTypeDef,
    ImageModifyAttributeLaunchPermissionTypeDef,
    ImageWaitUntilExistsFiltersTypeDef,
    ImagesFilterFiltersTypeDef,
    InstanceAttachClassicLinkVpcResponseTypeDef,
    InstanceAttachVolumeResponseTypeDef,
    InstanceConsoleOutputResponseTypeDef,
    InstanceCreateImageBlockDeviceMappingsTypeDef,
    InstanceCreateTagsTagsTypeDef,
    InstanceDeleteTagsTagsTypeDef,
    InstanceDescribeAttributeResponseTypeDef,
    InstanceDetachClassicLinkVpcResponseTypeDef,
    InstanceDetachVolumeResponseTypeDef,
    InstanceModifyAttributeBlockDeviceMappingsTypeDef,
    InstanceModifyAttributeDisableApiTerminationTypeDef,
    InstanceModifyAttributeEbsOptimizedTypeDef,
    InstanceModifyAttributeEnaSupportTypeDef,
    InstanceModifyAttributeInstanceInitiatedShutdownBehaviorTypeDef,
    InstanceModifyAttributeInstanceTypeTypeDef,
    InstanceModifyAttributeKernelTypeDef,
    InstanceModifyAttributeRamdiskTypeDef,
    InstanceModifyAttributeSourceDestCheckTypeDef,
    InstanceModifyAttributeSriovNetSupportTypeDef,
    InstanceModifyAttributeUserDataTypeDef,
    InstanceMonitorResponseTypeDef,
    InstancePasswordDataResponseTypeDef,
    InstanceStartResponseTypeDef,
    InstanceStopResponseTypeDef,
    InstanceTerminateResponseTypeDef,
    InstanceUnmonitorResponseTypeDef,
    InstanceWaitUntilExistsFiltersTypeDef,
    InstanceWaitUntilRunningFiltersTypeDef,
    InstanceWaitUntilStoppedFiltersTypeDef,
    InstanceWaitUntilTerminatedFiltersTypeDef,
    InstancesCreateTagsTagsTypeDef,
    InstancesFilterFiltersTypeDef,
    InstancesMonitorResponseTypeDef,
    InstancesStartResponseTypeDef,
    InstancesStopResponseTypeDef,
    InstancesTerminateResponseTypeDef,
    InstancesUnmonitorResponseTypeDef,
    InternetGatewayCreateTagsTagsTypeDef,
    InternetGatewaysFilterFiltersTypeDef,
    KeyPairsFilterFiltersTypeDef,
    NetworkAclCreateEntryIcmpTypeCodeTypeDef,
    NetworkAclCreateEntryPortRangeTypeDef,
    NetworkAclCreateTagsTagsTypeDef,
    NetworkAclReplaceAssociationResponseTypeDef,
    NetworkAclReplaceEntryIcmpTypeCodeTypeDef,
    NetworkAclReplaceEntryPortRangeTypeDef,
    NetworkAclsFilterFiltersTypeDef,
    NetworkInterfaceAssignPrivateIpAddressesResponseTypeDef,
    NetworkInterfaceAttachResponseTypeDef,
    NetworkInterfaceCreateTagsTagsTypeDef,
    NetworkInterfaceDescribeAttributeResponseTypeDef,
    NetworkInterfaceModifyAttributeAttachmentTypeDef,
    NetworkInterfaceModifyAttributeDescriptionTypeDef,
    NetworkInterfaceModifyAttributeSourceDestCheckTypeDef,
    NetworkInterfacesFilterFiltersTypeDef,
    PlacementGroupsFilterFiltersTypeDef,
    RouteTableCreateTagsTagsTypeDef,
    RouteTablesFilterFiltersTypeDef,
    SecurityGroupAuthorizeEgressIpPermissionsTypeDef,
    SecurityGroupAuthorizeIngressIpPermissionsTypeDef,
    SecurityGroupCreateTagsTagsTypeDef,
    SecurityGroupRevokeEgressIpPermissionsTypeDef,
    SecurityGroupRevokeIngressIpPermissionsTypeDef,
    SecurityGroupsFilterFiltersTypeDef,
    ServiceResourceCreateDhcpOptionsDhcpConfigurationsTypeDef,
    ServiceResourceCreateInstancesBlockDeviceMappingsTypeDef,
    ServiceResourceCreateInstancesCapacityReservationSpecificationTypeDef,
    ServiceResourceCreateInstancesCpuOptionsTypeDef,
    ServiceResourceCreateInstancesCreditSpecificationTypeDef,
    ServiceResourceCreateInstancesElasticGpuSpecificationTypeDef,
    ServiceResourceCreateInstancesElasticInferenceAcceleratorsTypeDef,
    ServiceResourceCreateInstancesHibernationOptionsTypeDef,
    ServiceResourceCreateInstancesIamInstanceProfileTypeDef,
    ServiceResourceCreateInstancesInstanceMarketOptionsTypeDef,
    ServiceResourceCreateInstancesIpv6AddressesTypeDef,
    ServiceResourceCreateInstancesLaunchTemplateTypeDef,
    ServiceResourceCreateInstancesLicenseSpecificationsTypeDef,
    ServiceResourceCreateInstancesMetadataOptionsTypeDef,
    ServiceResourceCreateInstancesMonitoringTypeDef,
    ServiceResourceCreateInstancesNetworkInterfacesTypeDef,
    ServiceResourceCreateInstancesPlacementTypeDef,
    ServiceResourceCreateInstancesTagSpecificationsTypeDef,
    ServiceResourceCreateNetworkInterfaceIpv6AddressesTypeDef,
    ServiceResourceCreateNetworkInterfacePrivateIpAddressesTypeDef,
    ServiceResourceCreateSnapshotTagSpecificationsTypeDef,
    ServiceResourceCreateVolumeTagSpecificationsTypeDef,
    ServiceResourceRegisterImageBlockDeviceMappingsTypeDef,
    SnapshotCopyResponseTypeDef,
    SnapshotCopyTagSpecificationsTypeDef,
    SnapshotCreateTagsTagsTypeDef,
    SnapshotDescribeAttributeResponseTypeDef,
    SnapshotModifyAttributeCreateVolumePermissionTypeDef,
    SnapshotWaitUntilCompletedFiltersTypeDef,
    SnapshotsFilterFiltersTypeDef,
    SubnetCreateInstancesBlockDeviceMappingsTypeDef,
    SubnetCreateInstancesCapacityReservationSpecificationTypeDef,
    SubnetCreateInstancesCpuOptionsTypeDef,
    SubnetCreateInstancesCreditSpecificationTypeDef,
    SubnetCreateInstancesElasticGpuSpecificationTypeDef,
    SubnetCreateInstancesElasticInferenceAcceleratorsTypeDef,
    SubnetCreateInstancesHibernationOptionsTypeDef,
    SubnetCreateInstancesIamInstanceProfileTypeDef,
    SubnetCreateInstancesInstanceMarketOptionsTypeDef,
    SubnetCreateInstancesIpv6AddressesTypeDef,
    SubnetCreateInstancesLaunchTemplateTypeDef,
    SubnetCreateInstancesLicenseSpecificationsTypeDef,
    SubnetCreateInstancesMetadataOptionsTypeDef,
    SubnetCreateInstancesMonitoringTypeDef,
    SubnetCreateInstancesNetworkInterfacesTypeDef,
    SubnetCreateInstancesPlacementTypeDef,
    SubnetCreateInstancesTagSpecificationsTypeDef,
    SubnetCreateNetworkInterfaceIpv6AddressesTypeDef,
    SubnetCreateNetworkInterfacePrivateIpAddressesTypeDef,
    SubnetCreateTagsTagsTypeDef,
    SubnetsFilterFiltersTypeDef,
    TagTypeDef,
    VolumeAttachToInstanceResponseTypeDef,
    VolumeCreateSnapshotTagSpecificationsTypeDef,
    VolumeCreateTagsTagsTypeDef,
    VolumeDescribeAttributeResponseTypeDef,
    VolumeDescribeStatusFiltersTypeDef,
    VolumeDescribeStatusResponseTypeDef,
    VolumeDetachFromInstanceResponseTypeDef,
    VolumeModifyAttributeAutoEnableIOTypeDef,
    VolumesFilterFiltersTypeDef,
    VpcAddressAssociateResponseTypeDef,
    VpcAttachClassicLinkInstanceResponseTypeDef,
    VpcCreateTagsTagsTypeDef,
    VpcDescribeAttributeResponseTypeDef,
    VpcDetachClassicLinkInstanceResponseTypeDef,
    VpcDisableClassicLinkResponseTypeDef,
    VpcEnableClassicLinkResponseTypeDef,
    VpcModifyAttributeEnableDnsHostnamesTypeDef,
    VpcModifyAttributeEnableDnsSupportTypeDef,
    VpcPeeringConnectionAcceptResponseTypeDef,
    VpcPeeringConnectionDeleteResponseTypeDef,
    VpcPeeringConnectionRejectResponseTypeDef,
    VpcPeeringConnectionWaitUntilExistsFiltersTypeDef,
    VpcPeeringConnectionsFilterFiltersTypeDef,
    VpcWaitUntilAvailableFiltersTypeDef,
    VpcWaitUntilExistsFiltersTypeDef,
    VpcsFilterFiltersTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ServiceResource",
    "ClassicAddress",
    "DhcpOptions",
    "Image",
    "Instance",
    "InternetGateway",
    "KeyPair",
    "KeyPairInfo",
    "NetworkAcl",
    "NetworkInterface",
    "NetworkInterfaceAssociation",
    "PlacementGroup",
    "Route",
    "RouteTable",
    "RouteTableAssociation",
    "SecurityGroup",
    "Snapshot",
    "Subnet",
    "Tag",
    "Volume",
    "Vpc",
    "VpcPeeringConnection",
    "VpcAddress",
    "ServiceResourceClassicAddressesCollection",
    "ServiceResourceDhcpOptionsSetsCollection",
    "ServiceResourceImagesCollection",
    "ServiceResourceInstancesCollection",
    "ServiceResourceInternetGatewaysCollection",
    "ServiceResourceKeyPairsCollection",
    "ServiceResourceNetworkAclsCollection",
    "ServiceResourceNetworkInterfacesCollection",
    "ServiceResourcePlacementGroupsCollection",
    "ServiceResourceRouteTablesCollection",
    "ServiceResourceSecurityGroupsCollection",
    "ServiceResourceSnapshotsCollection",
    "ServiceResourceSubnetsCollection",
    "ServiceResourceVolumesCollection",
    "ServiceResourceVpcAddressesCollection",
    "ServiceResourceVpcPeeringConnectionsCollection",
    "ServiceResourceVpcsCollection",
    "InstanceVolumesCollection",
    "InstanceVpcAddressesCollection",
    "PlacementGroupInstancesCollection",
    "SubnetInstancesCollection",
    "SubnetNetworkInterfacesCollection",
    "VolumeSnapshotsCollection",
    "VpcAcceptedVpcPeeringConnectionsCollection",
    "VpcInstancesCollection",
    "VpcInternetGatewaysCollection",
    "VpcNetworkAclsCollection",
    "VpcNetworkInterfacesCollection",
    "VpcRequestedVpcPeeringConnectionsCollection",
    "VpcRouteTablesCollection",
    "VpcSecurityGroupsCollection",
    "VpcSubnetsCollection",
)


class ServiceResource(Boto3ServiceResource):
    """
    [EC2.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource)
    """

    classic_addresses: service_resource_scope.ServiceResourceClassicAddressesCollection
    dhcp_options_sets: service_resource_scope.ServiceResourceDhcpOptionsSetsCollection
    images: service_resource_scope.ServiceResourceImagesCollection
    instances: service_resource_scope.ServiceResourceInstancesCollection
    internet_gateways: service_resource_scope.ServiceResourceInternetGatewaysCollection
    key_pairs: service_resource_scope.ServiceResourceKeyPairsCollection
    network_acls: service_resource_scope.ServiceResourceNetworkAclsCollection
    network_interfaces: service_resource_scope.ServiceResourceNetworkInterfacesCollection
    placement_groups: service_resource_scope.ServiceResourcePlacementGroupsCollection
    route_tables: service_resource_scope.ServiceResourceRouteTablesCollection
    security_groups: service_resource_scope.ServiceResourceSecurityGroupsCollection
    snapshots: service_resource_scope.ServiceResourceSnapshotsCollection
    subnets: service_resource_scope.ServiceResourceSubnetsCollection
    volumes: service_resource_scope.ServiceResourceVolumesCollection
    vpc_addresses: service_resource_scope.ServiceResourceVpcAddressesCollection
    vpc_peering_connections: service_resource_scope.ServiceResourceVpcPeeringConnectionsCollection
    vpcs: service_resource_scope.ServiceResourceVpcsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def ClassicAddress(self, public_ip: str) -> service_resource_scope.ClassicAddress:
        """
        [ServiceResource.ClassicAddress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.ClassicAddress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def DhcpOptions(self, id: str) -> service_resource_scope.DhcpOptions:
        """
        [ServiceResource.DhcpOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.DhcpOptions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Image(self, id: str) -> service_resource_scope.Image:
        """
        [ServiceResource.Image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Instance(self, id: str) -> service_resource_scope.Instance:
        """
        [ServiceResource.Instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def InternetGateway(self, id: str) -> service_resource_scope.InternetGateway:
        """
        [ServiceResource.InternetGateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.InternetGateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def KeyPair(self, name: str) -> service_resource_scope.KeyPairInfo:
        """
        [ServiceResource.KeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.KeyPair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def NetworkAcl(self, id: str) -> service_resource_scope.NetworkAcl:
        """
        [ServiceResource.NetworkAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.NetworkAcl)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def NetworkInterface(self, id: str) -> service_resource_scope.NetworkInterface:
        """
        [ServiceResource.NetworkInterface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.NetworkInterface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def NetworkInterfaceAssociation(
        self, id: str
    ) -> service_resource_scope.NetworkInterfaceAssociation:
        """
        [ServiceResource.NetworkInterfaceAssociation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.NetworkInterfaceAssociation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def PlacementGroup(self, name: str) -> service_resource_scope.PlacementGroup:
        """
        [ServiceResource.PlacementGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.PlacementGroup)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Route(
        self, route_table_id: str, destination_cidr_block: str
    ) -> service_resource_scope.Route:
        """
        [ServiceResource.Route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def RouteTable(self, id: str) -> service_resource_scope.RouteTable:
        """
        [ServiceResource.RouteTable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.RouteTable)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def RouteTableAssociation(self, id: str) -> service_resource_scope.RouteTableAssociation:
        """
        [ServiceResource.RouteTableAssociation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.RouteTableAssociation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def SecurityGroup(self, id: str) -> service_resource_scope.SecurityGroup:
        """
        [ServiceResource.SecurityGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.SecurityGroup)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Snapshot(self, id: str) -> service_resource_scope.Snapshot:
        """
        [ServiceResource.Snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Subnet(self, id: str) -> service_resource_scope.Subnet:
        """
        [ServiceResource.Subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Subnet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Tag(self, resource_id: str, key: str, value: str) -> service_resource_scope.Tag:
        """
        [ServiceResource.Tag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Tag)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Volume(self, id: str) -> service_resource_scope.Volume:
        """
        [ServiceResource.Volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Vpc(self, id: str) -> service_resource_scope.Vpc:
        """
        [ServiceResource.Vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def VpcAddress(self, allocation_id: str) -> service_resource_scope.VpcAddress:
        """
        [ServiceResource.VpcAddress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.VpcAddress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def VpcPeeringConnection(self, id: str) -> service_resource_scope.VpcPeeringConnection:
        """
        [ServiceResource.VpcPeeringConnection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.VpcPeeringConnection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dhcp_options(
        self,
        DhcpConfigurations: List[ServiceResourceCreateDhcpOptionsDhcpConfigurationsTypeDef],
        DryRun: bool = None,
    ) -> service_resource_scope.DhcpOptions:
        """
        [ServiceResource.create_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_dhcp_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_instances(
        self,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: List[ServiceResourceCreateInstancesBlockDeviceMappingsTypeDef] = None,
        ImageId: str = None,
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
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List[ServiceResourceCreateInstancesIpv6AddressesTypeDef] = None,
        KernelId: str = None,
        KeyName: str = None,
        Monitoring: ServiceResourceCreateInstancesMonitoringTypeDef = None,
        Placement: ServiceResourceCreateInstancesPlacementTypeDef = None,
        RamdiskId: str = None,
        SecurityGroupIds: List[str] = None,
        SecurityGroups: List[str] = None,
        SubnetId: str = None,
        UserData: str = None,
        AdditionalInfo: str = None,
        ClientToken: str = None,
        DisableApiTermination: bool = None,
        DryRun: bool = None,
        EbsOptimized: bool = None,
        IamInstanceProfile: ServiceResourceCreateInstancesIamInstanceProfileTypeDef = None,
        InstanceInitiatedShutdownBehavior: Literal["stop", "terminate"] = None,
        NetworkInterfaces: List[ServiceResourceCreateInstancesNetworkInterfacesTypeDef] = None,
        PrivateIpAddress: str = None,
        ElasticGpuSpecification: List[
            ServiceResourceCreateInstancesElasticGpuSpecificationTypeDef
        ] = None,
        ElasticInferenceAccelerators: List[
            ServiceResourceCreateInstancesElasticInferenceAcceleratorsTypeDef
        ] = None,
        TagSpecifications: List[ServiceResourceCreateInstancesTagSpecificationsTypeDef] = None,
        LaunchTemplate: ServiceResourceCreateInstancesLaunchTemplateTypeDef = None,
        InstanceMarketOptions: ServiceResourceCreateInstancesInstanceMarketOptionsTypeDef = None,
        CreditSpecification: ServiceResourceCreateInstancesCreditSpecificationTypeDef = None,
        CpuOptions: ServiceResourceCreateInstancesCpuOptionsTypeDef = None,
        CapacityReservationSpecification: ServiceResourceCreateInstancesCapacityReservationSpecificationTypeDef = None,
        HibernationOptions: ServiceResourceCreateInstancesHibernationOptionsTypeDef = None,
        LicenseSpecifications: List[
            ServiceResourceCreateInstancesLicenseSpecificationsTypeDef
        ] = None,
        MetadataOptions: ServiceResourceCreateInstancesMetadataOptionsTypeDef = None,
    ) -> List[service_resource_scope.Instance]:
        """
        [ServiceResource.create_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_internet_gateway(
        self, DryRun: bool = None
    ) -> service_resource_scope.InternetGateway:
        """
        [ServiceResource.create_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_internet_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_key_pair(self, KeyName: str, DryRun: bool = None) -> service_resource_scope.KeyPair:
        """
        [ServiceResource.create_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_key_pair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_network_acl(
        self, VpcId: str, DryRun: bool = None
    ) -> service_resource_scope.NetworkAcl:
        """
        [ServiceResource.create_network_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_network_acl)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_network_interface(
        self,
        SubnetId: str,
        Description: str = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List[ServiceResourceCreateNetworkInterfaceIpv6AddressesTypeDef] = None,
        PrivateIpAddress: str = None,
        PrivateIpAddresses: List[
            ServiceResourceCreateNetworkInterfacePrivateIpAddressesTypeDef
        ] = None,
        SecondaryPrivateIpAddressCount: int = None,
        InterfaceType: str = None,
    ) -> service_resource_scope.NetworkInterface:
        """
        [ServiceResource.create_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_network_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_placement_group(
        self,
        DryRun: bool = None,
        GroupName: str = None,
        Strategy: Literal["cluster", "spread", "partition"] = None,
        PartitionCount: int = None,
    ) -> service_resource_scope.PlacementGroup:
        """
        [ServiceResource.create_placement_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_placement_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_route_table(
        self, VpcId: str, DryRun: bool = None
    ) -> service_resource_scope.RouteTable:
        """
        [ServiceResource.create_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_route_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_security_group(
        self, Description: str, GroupName: str, VpcId: str = None, DryRun: bool = None
    ) -> service_resource_scope.SecurityGroup:
        """
        [ServiceResource.create_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_security_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_snapshot(
        self,
        VolumeId: str,
        Description: str = None,
        TagSpecifications: List[ServiceResourceCreateSnapshotTagSpecificationsTypeDef] = None,
        DryRun: bool = None,
    ) -> service_resource_scope.Snapshot:
        """
        [ServiceResource.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_subnet(
        self,
        CidrBlock: str,
        VpcId: str,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Ipv6CidrBlock: str = None,
        OutpostArn: str = None,
        DryRun: bool = None,
    ) -> service_resource_scope.Subnet:
        """
        [ServiceResource.create_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_subnet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = False
    ) -> None:
        """
        [ServiceResource.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_volume(
        self,
        AvailabilityZone: str,
        Encrypted: bool = None,
        Iops: int = None,
        KmsKeyId: str = None,
        OutpostArn: str = None,
        Size: int = None,
        SnapshotId: str = None,
        VolumeType: Literal["standard", "io1", "gp2", "sc1", "st1"] = None,
        DryRun: bool = None,
        TagSpecifications: List[ServiceResourceCreateVolumeTagSpecificationsTypeDef] = None,
    ) -> service_resource_scope.Volume:
        """
        [ServiceResource.create_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vpc(
        self,
        CidrBlock: str,
        AmazonProvidedIpv6CidrBlock: bool = None,
        DryRun: bool = None,
        InstanceTenancy: Literal["default", "dedicated", "host"] = None,
        Ipv6CidrBlockNetworkBorderGroup: str = None,
    ) -> service_resource_scope.Vpc:
        """
        [ServiceResource.create_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vpc_peering_connection(
        self,
        DryRun: bool = None,
        PeerOwnerId: str = None,
        PeerVpcId: str = None,
        VpcId: str = None,
        PeerRegion: str = None,
    ) -> service_resource_scope.VpcPeeringConnection:
        """
        [ServiceResource.create_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.create_vpc_peering_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_route_table(self, AssociationId: str, DryRun: bool = None) -> None:
        """
        [ServiceResource.disassociate_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.disassociate_route_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_key_pair(
        self, KeyName: str, PublicKeyMaterial: bytes, DryRun: bool = None
    ) -> service_resource_scope.KeyPairInfo:
        """
        [ServiceResource.import_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.import_key_pair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_image(
        self,
        Name: str,
        ImageLocation: str = None,
        Architecture: Literal["i386", "x86_64", "arm64"] = None,
        BlockDeviceMappings: List[ServiceResourceRegisterImageBlockDeviceMappingsTypeDef] = None,
        Description: str = None,
        DryRun: bool = None,
        EnaSupport: bool = None,
        KernelId: str = None,
        BillingProducts: List[str] = None,
        RamdiskId: str = None,
        RootDeviceName: str = None,
        SriovNetSupport: str = None,
        VirtualizationType: str = None,
    ) -> service_resource_scope.Image:
        """
        [ServiceResource.register_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.register_image)
        """


class ClassicAddress(Boto3ServiceResource):
    """
    [ClassicAddress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.ClassicAddress)
    """

    instance_id: str
    allocation_id: str
    association_id: str
    domain: str
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List[Any]
    public_ipv4_pool: str
    network_border_group: str
    customer_owned_ip: str
    customer_owned_ipv4_pool: str
    public_ip: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate(
        self,
        AllocationId: str = None,
        InstanceId: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None,
    ) -> ClassicAddressAssociateResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate(self, AssociationId: str = None, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def release(
        self, AllocationId: str = None, NetworkBorderGroup: str = None, DryRun: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class DhcpOptions(Boto3ServiceResource):
    """
    [DhcpOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.DhcpOptions)
    """

    dhcp_configurations: List[Any]
    dhcp_options_id: str
    owner_id: str
    tags: List[Any]
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_with_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Tags: List[DhcpOptionsCreateTagsTagsTypeDef], DryRun: bool = None
    ) -> List[service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class Image(Boto3ServiceResource):
    """
    [Image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Image)
    """

    architecture: str
    creation_date: str
    image_id: str
    image_location: str
    image_type: str
    public: bool
    kernel_id: str
    owner_id: str
    platform: str
    product_codes: List[Any]
    ramdisk_id: str
    state: str
    block_device_mappings: List[Any]
    description: str
    ena_support: bool
    hypervisor: str
    image_owner_alias: str
    name: str
    root_device_name: str
    root_device_type: str
    sriov_net_support: str
    state_reason: Dict[str, Any]
    tags: List[Any]
    virtualization_type: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Tags: List[ImageCreateTagsTagsTypeDef], DryRun: bool = None
    ) -> List[service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attribute(
        self,
        Attribute: Literal[
            "description",
            "kernel",
            "ramdisk",
            "launchPermission",
            "productCodes",
            "blockDeviceMapping",
            "sriovNetSupport",
        ],
        DryRun: bool = None,
    ) -> ImageDescribeAttributeResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_attribute(
        self,
        Attribute: str = None,
        Description: ImageModifyAttributeDescriptionTypeDef = None,
        LaunchPermission: ImageModifyAttributeLaunchPermissionTypeDef = None,
        OperationType: Literal["add", "remove"] = None,
        ProductCodes: List[str] = None,
        UserGroups: List[str] = None,
        UserIds: List[str] = None,
        Value: str = None,
        DryRun: bool = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_attribute(self, Attribute: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_exists(
        self,
        ExecutableUsers: List[str] = None,
        Filters: List[ImageWaitUntilExistsFiltersTypeDef] = None,
        Owners: List[str] = None,
        DryRun: bool = None,
    ) -> None:
        pass


class Instance(Boto3ServiceResource):
    """
    [Instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Instance)
    """

    ami_launch_index: int
    image_id: str
    instance_id: str
    instance_type: str
    kernel_id: str
    key_name: str
    launch_time: datetime
    monitoring: Dict[str, Any]
    placement: Dict[str, Any]
    platform: str
    private_dns_name: str
    private_ip_address: str
    product_codes: List[Any]
    public_dns_name: str
    public_ip_address: str
    ramdisk_id: str
    state: Dict[str, Any]
    state_transition_reason: str
    subnet_id: str
    vpc_id: str
    architecture: str
    block_device_mappings: List[Any]
    client_token: str
    ebs_optimized: bool
    ena_support: bool
    hypervisor: str
    iam_instance_profile: Dict[str, Any]
    instance_lifecycle: str
    elastic_gpu_associations: List[Any]
    elastic_inference_accelerator_associations: List[Any]
    network_interfaces_attribute: List[Any]
    outpost_arn: str
    root_device_name: str
    root_device_type: str
    security_groups: List[Any]
    source_dest_check: bool
    spot_instance_request_id: str
    sriov_net_support: str
    state_reason: Dict[str, Any]
    tags: List[Any]
    virtualization_type: str
    cpu_options: Dict[str, Any]
    capacity_reservation_id: str
    capacity_reservation_specification: Dict[str, Any]
    hibernation_options: Dict[str, Any]
    licenses: List[Any]
    metadata_options: Dict[str, Any]
    id: str
    volumes: service_resource_scope.InstanceVolumesCollection
    vpc_addresses: service_resource_scope.InstanceVpcAddressesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_classic_link_vpc(
        self, Groups: List[str], VpcId: str, DryRun: bool = None
    ) -> InstanceAttachClassicLinkVpcResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_volume(
        self, Device: str, VolumeId: str, DryRun: bool = None
    ) -> InstanceAttachVolumeResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def console_output(
        self, DryRun: bool = None, Latest: bool = None
    ) -> InstanceConsoleOutputResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_image(
        self,
        Name: str,
        BlockDeviceMappings: List[InstanceCreateImageBlockDeviceMappingsTypeDef] = None,
        Description: str = None,
        DryRun: bool = None,
        NoReboot: bool = None,
    ) -> service_resource_scope.Image:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Tags: List[InstanceCreateTagsTagsTypeDef], DryRun: bool = None
    ) -> List[service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tags(
        self, DryRun: bool = None, Tags: List[InstanceDeleteTagsTagsTypeDef] = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attribute(
        self,
        Attribute: Literal[
            "instanceType",
            "kernel",
            "ramdisk",
            "userData",
            "disableApiTermination",
            "instanceInitiatedShutdownBehavior",
            "rootDeviceName",
            "blockDeviceMapping",
            "productCodes",
            "sourceDestCheck",
            "groupSet",
            "ebsOptimized",
            "sriovNetSupport",
            "enaSupport",
        ],
        DryRun: bool = None,
    ) -> InstanceDescribeAttributeResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_classic_link_vpc(
        self, VpcId: str, DryRun: bool = None
    ) -> InstanceDetachClassicLinkVpcResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_volume(
        self, VolumeId: str, Device: str = None, Force: bool = None, DryRun: bool = None
    ) -> InstanceDetachVolumeResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_attribute(
        self,
        SourceDestCheck: InstanceModifyAttributeSourceDestCheckTypeDef = None,
        Attribute: Literal[
            "instanceType",
            "kernel",
            "ramdisk",
            "userData",
            "disableApiTermination",
            "instanceInitiatedShutdownBehavior",
            "rootDeviceName",
            "blockDeviceMapping",
            "productCodes",
            "sourceDestCheck",
            "groupSet",
            "ebsOptimized",
            "sriovNetSupport",
            "enaSupport",
        ] = None,
        BlockDeviceMappings: List[InstanceModifyAttributeBlockDeviceMappingsTypeDef] = None,
        DisableApiTermination: InstanceModifyAttributeDisableApiTerminationTypeDef = None,
        DryRun: bool = None,
        EbsOptimized: InstanceModifyAttributeEbsOptimizedTypeDef = None,
        EnaSupport: InstanceModifyAttributeEnaSupportTypeDef = None,
        Groups: List[str] = None,
        InstanceInitiatedShutdownBehavior: InstanceModifyAttributeInstanceInitiatedShutdownBehaviorTypeDef = None,
        InstanceType: InstanceModifyAttributeInstanceTypeTypeDef = None,
        Kernel: InstanceModifyAttributeKernelTypeDef = None,
        Ramdisk: InstanceModifyAttributeRamdiskTypeDef = None,
        SriovNetSupport: InstanceModifyAttributeSriovNetSupportTypeDef = None,
        UserData: InstanceModifyAttributeUserDataTypeDef = None,
        Value: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def monitor(self, DryRun: bool = None) -> InstanceMonitorResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def password_data(self, DryRun: bool = None) -> InstancePasswordDataResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def report_status(
        self,
        ReasonCodes: List[
            Literal[
                "instance-stuck-in-state",
                "unresponsive",
                "not-accepting-credentials",
                "password-not-available",
                "performance-network",
                "performance-instance-store",
                "performance-ebs-volume",
                "performance-other",
                "other",
            ]
        ],
        Status: Literal["ok", "impaired"],
        Description: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        StartTime: datetime = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_attribute(
        self,
        Attribute: Literal[
            "instanceType",
            "kernel",
            "ramdisk",
            "userData",
            "disableApiTermination",
            "instanceInitiatedShutdownBehavior",
            "rootDeviceName",
            "blockDeviceMapping",
            "productCodes",
            "sourceDestCheck",
            "groupSet",
            "ebsOptimized",
            "sriovNetSupport",
            "enaSupport",
        ],
        DryRun: bool = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_kernel(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_ramdisk(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_source_dest_check(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start(
        self, AdditionalInfo: str = None, DryRun: bool = None
    ) -> InstanceStartResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop(
        self, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> InstanceStopResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate(self, DryRun: bool = None) -> InstanceTerminateResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unmonitor(self, DryRun: bool = None) -> InstanceUnmonitorResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_exists(
        self,
        Filters: List[InstanceWaitUntilExistsFiltersTypeDef] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_running(
        self,
        Filters: List[InstanceWaitUntilRunningFiltersTypeDef] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_stopped(
        self,
        Filters: List[InstanceWaitUntilStoppedFiltersTypeDef] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_terminated(
        self,
        Filters: List[InstanceWaitUntilTerminatedFiltersTypeDef] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> None:
        pass


class InternetGateway(Boto3ServiceResource):
    """
    [InternetGateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.InternetGateway)
    """

    attachments: List[Any]
    internet_gateway_id: str
    owner_id: str
    tags: List[Any]
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_to_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Tags: List[InternetGatewayCreateTagsTagsTypeDef], DryRun: bool = None
    ) -> List[service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_from_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class KeyPair(Boto3ServiceResource):
    """
    [KeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.KeyPair)
    """

    key_fingerprint: str
    key_material: str
    key_name: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass


class KeyPairInfo(Boto3ServiceResource):
    """
    [KeyPairInfo documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.KeyPairInfo)
    """

    key_fingerprint: str
    key_name: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class NetworkAcl(Boto3ServiceResource):
    """
    [NetworkAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.NetworkAcl)
    """

    associations: List[Any]
    entries: List[Any]
    is_default: bool
    network_acl_id: str
    tags: List[Any]
    vpc_id: str
    owner_id: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_entry(
        self,
        Egress: bool,
        Protocol: str,
        RuleAction: Literal["allow", "deny"],
        RuleNumber: int,
        CidrBlock: str = None,
        DryRun: bool = None,
        IcmpTypeCode: NetworkAclCreateEntryIcmpTypeCodeTypeDef = None,
        Ipv6CidrBlock: str = None,
        PortRange: NetworkAclCreateEntryPortRangeTypeDef = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Tags: List[NetworkAclCreateTagsTagsTypeDef], DryRun: bool = None
    ) -> List[service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_entry(self, Egress: bool, RuleNumber: int, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace_association(
        self, AssociationId: str, DryRun: bool = None
    ) -> NetworkAclReplaceAssociationResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace_entry(
        self,
        Egress: bool,
        Protocol: str,
        RuleAction: Literal["allow", "deny"],
        RuleNumber: int,
        CidrBlock: str = None,
        DryRun: bool = None,
        IcmpTypeCode: NetworkAclReplaceEntryIcmpTypeCodeTypeDef = None,
        Ipv6CidrBlock: str = None,
        PortRange: NetworkAclReplaceEntryPortRangeTypeDef = None,
    ) -> None:
        pass


class NetworkInterface(Boto3ServiceResource):
    """
    [NetworkInterface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.NetworkInterface)
    """

    association_attribute: Dict[str, Any]
    attachment: Dict[str, Any]
    availability_zone: str
    description: str
    groups: List[Any]
    interface_type: str
    ipv6_addresses: List[Any]
    mac_address: str
    network_interface_id: str
    outpost_arn: str
    owner_id: str
    private_dns_name: str
    private_ip_address: str
    private_ip_addresses: List[Any]
    requester_id: str
    requester_managed: bool
    source_dest_check: bool
    status: str
    subnet_id: str
    tag_set: List[Any]
    vpc_id: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def assign_private_ip_addresses(
        self,
        AllowReassignment: bool = None,
        PrivateIpAddresses: List[str] = None,
        SecondaryPrivateIpAddressCount: int = None,
    ) -> NetworkInterfaceAssignPrivateIpAddressesResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach(
        self, DeviceIndex: int, InstanceId: str, DryRun: bool = None
    ) -> NetworkInterfaceAttachResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Tags: List[NetworkInterfaceCreateTagsTagsTypeDef], DryRun: bool = None
    ) -> List[service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attribute(
        self,
        Attribute: Literal["description", "groupSet", "sourceDestCheck", "attachment"] = None,
        DryRun: bool = None,
    ) -> NetworkInterfaceDescribeAttributeResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach(self, DryRun: bool = None, Force: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_attribute(
        self,
        Attachment: NetworkInterfaceModifyAttributeAttachmentTypeDef = None,
        Description: NetworkInterfaceModifyAttributeDescriptionTypeDef = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        SourceDestCheck: NetworkInterfaceModifyAttributeSourceDestCheckTypeDef = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_attribute(self, DryRun: bool = None, SourceDestCheck: str = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unassign_private_ip_addresses(self, PrivateIpAddresses: List[str]) -> None:
        pass


class NetworkInterfaceAssociation(Boto3ServiceResource):
    """
    [NetworkInterfaceAssociation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.NetworkInterfaceAssociation)
    """

    ip_owner_id: str
    public_dns_name: str
    public_ip: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, PublicIp: str = None, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class PlacementGroup(Boto3ServiceResource):
    """
    [PlacementGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.PlacementGroup)
    """

    group_name: str
    state: str
    strategy: str
    partition_count: int
    name: str
    instances: service_resource_scope.PlacementGroupInstancesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class Route(Boto3ServiceResource):
    """
    [Route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Route)
    """

    destination_ipv6_cidr_block: str
    destination_prefix_list_id: str
    egress_only_internet_gateway_id: str
    gateway_id: str
    instance_id: str
    instance_owner_id: str
    nat_gateway_id: str
    transit_gateway_id: str
    local_gateway_id: str
    network_interface_id: str
    origin: str
    state: str
    vpc_peering_connection_id: str
    route_table_id: str
    destination_cidr_block: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DestinationIpv6CidrBlock: str = None, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace(
        self,
        DestinationIpv6CidrBlock: str = None,
        DryRun: bool = None,
        EgressOnlyInternetGatewayId: str = None,
        GatewayId: str = None,
        InstanceId: str = None,
        LocalTarget: bool = None,
        NatGatewayId: str = None,
        TransitGatewayId: str = None,
        LocalGatewayId: str = None,
        NetworkInterfaceId: str = None,
        VpcPeeringConnectionId: str = None,
    ) -> None:
        pass


class RouteTable(Boto3ServiceResource):
    """
    [RouteTable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.RouteTable)
    """

    associations_attribute: List[Any]
    propagating_vgws: List[Any]
    route_table_id: str
    routes_attribute: List[Any]
    tags: List[Any]
    vpc_id: str
    owner_id: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_with_subnet(
        self, DryRun: bool = None, SubnetId: str = None, GatewayId: str = None
    ) -> service_resource_scope.RouteTableAssociation:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_route(
        self,
        DestinationCidrBlock: str = None,
        DestinationIpv6CidrBlock: str = None,
        DryRun: bool = None,
        EgressOnlyInternetGatewayId: str = None,
        GatewayId: str = None,
        InstanceId: str = None,
        NatGatewayId: str = None,
        TransitGatewayId: str = None,
        LocalGatewayId: str = None,
        NetworkInterfaceId: str = None,
        VpcPeeringConnectionId: str = None,
    ) -> service_resource_scope.Route:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Tags: List[RouteTableCreateTagsTagsTypeDef], DryRun: bool = None
    ) -> List[service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class RouteTableAssociation(Boto3ServiceResource):
    """
    [RouteTableAssociation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.RouteTableAssociation)
    """

    main: bool
    route_table_association_id: str
    route_table_id: str
    subnet_id: str
    gateway_id: str
    association_state: Dict[str, Any]
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace_subnet(
        self, RouteTableId: str, DryRun: bool = None
    ) -> service_resource_scope.RouteTableAssociation:
        pass


class SecurityGroup(Boto3ServiceResource):
    """
    [SecurityGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.SecurityGroup)
    """

    description: str
    group_name: str
    ip_permissions: List[Any]
    owner_id: str
    group_id: str
    ip_permissions_egress: List[Any]
    tags: List[Any]
    vpc_id: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def authorize_egress(
        self,
        DryRun: bool = None,
        IpPermissions: List[SecurityGroupAuthorizeEgressIpPermissionsTypeDef] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def authorize_ingress(
        self,
        CidrIp: str = None,
        FromPort: int = None,
        GroupName: str = None,
        IpPermissions: List[SecurityGroupAuthorizeIngressIpPermissionsTypeDef] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Tags: List[SecurityGroupCreateTagsTagsTypeDef], DryRun: bool = None
    ) -> List[service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, GroupName: str = None, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_egress(
        self,
        DryRun: bool = None,
        IpPermissions: List[SecurityGroupRevokeEgressIpPermissionsTypeDef] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_ingress(
        self,
        CidrIp: str = None,
        FromPort: int = None,
        GroupName: str = None,
        IpPermissions: List[SecurityGroupRevokeIngressIpPermissionsTypeDef] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
    ) -> None:
        pass


class Snapshot(Boto3ServiceResource):
    """
    [Snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Snapshot)
    """

    data_encryption_key_id: str
    description: str
    encrypted: bool
    kms_key_id: str
    owner_id: str
    progress: str
    snapshot_id: str
    start_time: datetime
    state: str
    state_message: str
    volume_id: str
    volume_size: int
    owner_alias: str
    tags: List[Any]
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy(
        self,
        SourceRegion: str,
        Description: str = None,
        DestinationRegion: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        PresignedUrl: str = None,
        TagSpecifications: List[SnapshotCopyTagSpecificationsTypeDef] = None,
        DryRun: bool = None,
    ) -> SnapshotCopyResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Tags: List[SnapshotCreateTagsTagsTypeDef], DryRun: bool = None
    ) -> List[service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attribute(
        self, Attribute: Literal["productCodes", "createVolumePermission"], DryRun: bool = None
    ) -> SnapshotDescribeAttributeResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_attribute(
        self,
        Attribute: Literal["productCodes", "createVolumePermission"] = None,
        CreateVolumePermission: SnapshotModifyAttributeCreateVolumePermissionTypeDef = None,
        GroupNames: List[str] = None,
        OperationType: Literal["add", "remove"] = None,
        UserIds: List[str] = None,
        DryRun: bool = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_attribute(
        self, Attribute: Literal["productCodes", "createVolumePermission"], DryRun: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_completed(
        self,
        Filters: List[SnapshotWaitUntilCompletedFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        DryRun: bool = None,
    ) -> None:
        pass


class Subnet(Boto3ServiceResource):
    """
    [Subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Subnet)
    """

    availability_zone: str
    availability_zone_id: str
    available_ip_address_count: int
    cidr_block: str
    default_for_az: bool
    map_public_ip_on_launch: bool
    state: str
    subnet_id: str
    vpc_id: str
    owner_id: str
    assign_ipv6_address_on_creation: bool
    ipv6_cidr_block_association_set: List[Any]
    tags: List[Any]
    subnet_arn: str
    outpost_arn: str
    id: str
    instances: service_resource_scope.SubnetInstancesCollection
    network_interfaces: service_resource_scope.SubnetNetworkInterfacesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_instances(
        self,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: List[SubnetCreateInstancesBlockDeviceMappingsTypeDef] = None,
        ImageId: str = None,
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
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List[SubnetCreateInstancesIpv6AddressesTypeDef] = None,
        KernelId: str = None,
        KeyName: str = None,
        Monitoring: SubnetCreateInstancesMonitoringTypeDef = None,
        Placement: SubnetCreateInstancesPlacementTypeDef = None,
        RamdiskId: str = None,
        SecurityGroupIds: List[str] = None,
        SecurityGroups: List[str] = None,
        UserData: str = None,
        AdditionalInfo: str = None,
        ClientToken: str = None,
        DisableApiTermination: bool = None,
        DryRun: bool = None,
        EbsOptimized: bool = None,
        IamInstanceProfile: SubnetCreateInstancesIamInstanceProfileTypeDef = None,
        InstanceInitiatedShutdownBehavior: Literal["stop", "terminate"] = None,
        NetworkInterfaces: List[SubnetCreateInstancesNetworkInterfacesTypeDef] = None,
        PrivateIpAddress: str = None,
        ElasticGpuSpecification: List[SubnetCreateInstancesElasticGpuSpecificationTypeDef] = None,
        ElasticInferenceAccelerators: List[
            SubnetCreateInstancesElasticInferenceAcceleratorsTypeDef
        ] = None,
        TagSpecifications: List[SubnetCreateInstancesTagSpecificationsTypeDef] = None,
        LaunchTemplate: SubnetCreateInstancesLaunchTemplateTypeDef = None,
        InstanceMarketOptions: SubnetCreateInstancesInstanceMarketOptionsTypeDef = None,
        CreditSpecification: SubnetCreateInstancesCreditSpecificationTypeDef = None,
        CpuOptions: SubnetCreateInstancesCpuOptionsTypeDef = None,
        CapacityReservationSpecification: SubnetCreateInstancesCapacityReservationSpecificationTypeDef = None,
        HibernationOptions: SubnetCreateInstancesHibernationOptionsTypeDef = None,
        LicenseSpecifications: List[SubnetCreateInstancesLicenseSpecificationsTypeDef] = None,
        MetadataOptions: SubnetCreateInstancesMetadataOptionsTypeDef = None,
    ) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_network_interface(
        self,
        Description: str = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List[SubnetCreateNetworkInterfaceIpv6AddressesTypeDef] = None,
        PrivateIpAddress: str = None,
        PrivateIpAddresses: List[SubnetCreateNetworkInterfacePrivateIpAddressesTypeDef] = None,
        SecondaryPrivateIpAddressCount: int = None,
        InterfaceType: str = None,
    ) -> service_resource_scope.NetworkInterface:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Tags: List[SubnetCreateTagsTagsTypeDef], DryRun: bool = None
    ) -> List[service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class Tag(Boto3ServiceResource):
    """
    [Tag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Tag)
    """

    resource_type: str
    resource_id: str
    key: str
    value: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class Volume(Boto3ServiceResource):
    """
    [Volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Volume)
    """

    attachments: List[Any]
    availability_zone: str
    create_time: datetime
    encrypted: bool
    kms_key_id: str
    outpost_arn: str
    size: int
    snapshot_id: str
    state: str
    volume_id: str
    iops: int
    tags: List[Any]
    volume_type: str
    fast_restored: bool
    id: str
    snapshots: service_resource_scope.VolumeSnapshotsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_to_instance(
        self, Device: str, InstanceId: str, DryRun: bool = None
    ) -> VolumeAttachToInstanceResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_snapshot(
        self,
        Description: str = None,
        TagSpecifications: List[VolumeCreateSnapshotTagSpecificationsTypeDef] = None,
        DryRun: bool = None,
    ) -> service_resource_scope.Snapshot:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Tags: List[VolumeCreateTagsTagsTypeDef], DryRun: bool = None
    ) -> List[service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attribute(
        self, Attribute: Literal["autoEnableIO", "productCodes"], DryRun: bool = None
    ) -> VolumeDescribeAttributeResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_status(
        self,
        Filters: List[VolumeDescribeStatusFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> VolumeDescribeStatusResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_from_instance(
        self, Device: str = None, Force: bool = None, InstanceId: str = None, DryRun: bool = None
    ) -> VolumeDetachFromInstanceResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_io(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_attribute(
        self, AutoEnableIO: VolumeModifyAttributeAutoEnableIOTypeDef = None, DryRun: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class Vpc(Boto3ServiceResource):
    """
    [Vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.Vpc)
    """

    cidr_block: str
    dhcp_options_id: str
    state: str
    vpc_id: str
    owner_id: str
    instance_tenancy: str
    ipv6_cidr_block_association_set: List[Any]
    cidr_block_association_set: List[Any]
    is_default: bool
    tags: List[Any]
    id: str
    accepted_vpc_peering_connections: service_resource_scope.VpcAcceptedVpcPeeringConnectionsCollection
    instances: service_resource_scope.VpcInstancesCollection
    internet_gateways: service_resource_scope.VpcInternetGatewaysCollection
    network_acls: service_resource_scope.VpcNetworkAclsCollection
    network_interfaces: service_resource_scope.VpcNetworkInterfacesCollection
    requested_vpc_peering_connections: service_resource_scope.VpcRequestedVpcPeeringConnectionsCollection
    route_tables: service_resource_scope.VpcRouteTablesCollection
    security_groups: service_resource_scope.VpcSecurityGroupsCollection
    subnets: service_resource_scope.VpcSubnetsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_dhcp_options(self, DhcpOptionsId: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_classic_link_instance(
        self, Groups: List[str], InstanceId: str, DryRun: bool = None
    ) -> VpcAttachClassicLinkInstanceResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_network_acl(self, DryRun: bool = None) -> service_resource_scope.NetworkAcl:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_route_table(self, DryRun: bool = None) -> service_resource_scope.RouteTable:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_security_group(
        self, Description: str, GroupName: str, DryRun: bool = None
    ) -> service_resource_scope.SecurityGroup:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_subnet(
        self,
        CidrBlock: str,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Ipv6CidrBlock: str = None,
        OutpostArn: str = None,
        DryRun: bool = None,
    ) -> service_resource_scope.Subnet:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Tags: List[VpcCreateTagsTagsTypeDef], DryRun: bool = None
    ) -> List[service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attribute(
        self, Attribute: Literal["enableDnsSupport", "enableDnsHostnames"], DryRun: bool = None
    ) -> VpcDescribeAttributeResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_classic_link_instance(
        self, InstanceId: str, DryRun: bool = None
    ) -> VpcDetachClassicLinkInstanceResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_classic_link(self, DryRun: bool = None) -> VpcDisableClassicLinkResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_classic_link(self, DryRun: bool = None) -> VpcEnableClassicLinkResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_attribute(
        self,
        EnableDnsHostnames: VpcModifyAttributeEnableDnsHostnamesTypeDef = None,
        EnableDnsSupport: VpcModifyAttributeEnableDnsSupportTypeDef = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def request_vpc_peering_connection(
        self,
        DryRun: bool = None,
        PeerOwnerId: str = None,
        PeerVpcId: str = None,
        PeerRegion: str = None,
    ) -> service_resource_scope.VpcPeeringConnection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_available(
        self,
        Filters: List[VpcWaitUntilAvailableFiltersTypeDef] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_exists(
        self,
        Filters: List[VpcWaitUntilExistsFiltersTypeDef] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> None:
        pass


class VpcPeeringConnection(Boto3ServiceResource):
    """
    [VpcPeeringConnection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.VpcPeeringConnection)
    """

    accepter_vpc_info: Dict[str, Any]
    expiration_time: datetime
    requester_vpc_info: Dict[str, Any]
    status: Dict[str, Any]
    tags: List[Any]
    vpc_peering_connection_id: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept(self, DryRun: bool = None) -> VpcPeeringConnectionAcceptResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> VpcPeeringConnectionDeleteResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject(self, DryRun: bool = None) -> VpcPeeringConnectionRejectResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_exists(
        self,
        Filters: List[VpcPeeringConnectionWaitUntilExistsFiltersTypeDef] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> None:
        pass


class VpcAddress(Boto3ServiceResource):
    """
    [VpcAddress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.VpcAddress)
    """

    instance_id: str
    public_ip: str
    association_id: str
    domain: str
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List[Any]
    public_ipv4_pool: str
    network_border_group: str
    customer_owned_ip: str
    customer_owned_ipv4_pool: str
    allocation_id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate(
        self,
        InstanceId: str = None,
        PublicIp: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None,
    ) -> VpcAddressAssociateResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def release(
        self, PublicIp: str = None, NetworkBorderGroup: str = None, DryRun: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class ServiceResourceClassicAddressesCollection(ResourceCollection):
    """
    [ServiceResource.classic_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.classic_addresses)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.ClassicAddress]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PublicIps: List[str] = None, AllocationIds: List[str] = None, DryRun: bool = None
    ) -> List[service_resource_scope.ClassicAddress]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.ClassicAddress]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.ClassicAddress]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceDhcpOptionsSetsCollection(ResourceCollection):
    """
    [ServiceResource.dhcp_options_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.dhcp_options_sets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.DhcpOptions]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        DhcpOptionsIds: List[str] = None,
        Filters: List[DhcpOptionsSetsFilterFiltersTypeDef] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.DhcpOptions]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.DhcpOptions]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.DhcpOptions]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceImagesCollection(ResourceCollection):
    """
    [ServiceResource.images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.images)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Image]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        ExecutableUsers: List[str] = None,
        Filters: List[ImagesFilterFiltersTypeDef] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        DryRun: bool = None,
    ) -> List[service_resource_scope.Image]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Image]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Image]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceInstancesCollection(ResourceCollection):
    """
    [ServiceResource.instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.instances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(self, Tags: List[InstancesCreateTagsTagsTypeDef], DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Filters: List[InstancesFilterFiltersTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def monitor(self, DryRun: bool = None) -> InstancesMonitorResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start(
        self, AdditionalInfo: str = None, DryRun: bool = None
    ) -> InstancesStartResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop(
        self, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> InstancesStopResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate(self, DryRun: bool = None) -> InstancesTerminateResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unmonitor(self, DryRun: bool = None) -> InstancesUnmonitorResponseTypeDef:
        pass


class ServiceResourceInternetGatewaysCollection(ResourceCollection):
    """
    [ServiceResource.internet_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.internet_gateways)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.InternetGateway]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Filters: List[InternetGatewaysFilterFiltersTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.InternetGateway]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.InternetGateway]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.InternetGateway]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceKeyPairsCollection(ResourceCollection):
    """
    [ServiceResource.key_pairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.key_pairs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.KeyPairInfo]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Filters: List[KeyPairsFilterFiltersTypeDef] = None,
        KeyNames: List[str] = None,
        DryRun: bool = None,
    ) -> List[service_resource_scope.KeyPairInfo]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.KeyPairInfo]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.KeyPairInfo]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceNetworkAclsCollection(ResourceCollection):
    """
    [ServiceResource.network_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.network_acls)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.NetworkAcl]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Filters: List[NetworkAclsFilterFiltersTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.NetworkAcl]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.NetworkAcl]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.NetworkAcl]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceNetworkInterfacesCollection(ResourceCollection):
    """
    [ServiceResource.network_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.network_interfaces)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.NetworkInterface]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Filters: List[NetworkInterfacesFilterFiltersTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.NetworkInterface]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.NetworkInterface]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.NetworkInterface]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourcePlacementGroupsCollection(ResourceCollection):
    """
    [ServiceResource.placement_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.placement_groups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.PlacementGroup]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Filters: List[PlacementGroupsFilterFiltersTypeDef] = None,
        DryRun: bool = None,
        GroupNames: List[str] = None,
    ) -> List[service_resource_scope.PlacementGroup]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.PlacementGroup]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.PlacementGroup]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceRouteTablesCollection(ResourceCollection):
    """
    [ServiceResource.route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.route_tables)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.RouteTable]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Filters: List[RouteTablesFilterFiltersTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.RouteTable]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.RouteTable]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.RouteTable]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceSecurityGroupsCollection(ResourceCollection):
    """
    [ServiceResource.security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.security_groups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.SecurityGroup]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Filters: List[SecurityGroupsFilterFiltersTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.SecurityGroup]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.SecurityGroup]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.SecurityGroup]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceSnapshotsCollection(ResourceCollection):
    """
    [ServiceResource.snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.snapshots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Snapshot]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Filters: List[SnapshotsFilterFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
    ) -> List[service_resource_scope.Snapshot]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Snapshot]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Snapshot]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceSubnetsCollection(ResourceCollection):
    """
    [ServiceResource.subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.subnets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Subnet]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Filters: List[SubnetsFilterFiltersTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.Subnet]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Subnet]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Subnet]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceVolumesCollection(ResourceCollection):
    """
    [ServiceResource.volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.volumes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Volume]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Filters: List[VolumesFilterFiltersTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> List[service_resource_scope.Volume]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Volume]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Volume]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceVpcAddressesCollection(ResourceCollection):
    """
    [ServiceResource.vpc_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.vpc_addresses)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.VpcAddress]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PublicIps: List[str] = None, AllocationIds: List[str] = None, DryRun: bool = None
    ) -> List[service_resource_scope.VpcAddress]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.VpcAddress]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.VpcAddress]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [ServiceResource.vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.vpc_peering_connections)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.VpcPeeringConnection]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Filters: List[VpcPeeringConnectionsFilterFiltersTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.VpcPeeringConnection]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.VpcPeeringConnection]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.VpcPeeringConnection]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceVpcsCollection(ResourceCollection):
    """
    [ServiceResource.vpcs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.ServiceResource.vpcs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Vpc]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Filters: List[VpcsFilterFiltersTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.Vpc]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Vpc]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Vpc]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class InstanceVolumesCollection(ResourceCollection):
    """
    [Instance.volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Instance.volumes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Volume]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> List[service_resource_scope.Volume]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Volume]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Volume]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class InstanceVpcAddressesCollection(ResourceCollection):
    """
    [Instance.vpc_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Instance.vpc_addresses)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.VpcAddress]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PublicIps: List[str] = None, AllocationIds: List[str] = None, DryRun: bool = None
    ) -> List[service_resource_scope.VpcAddress]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.VpcAddress]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.VpcAddress]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class PlacementGroupInstancesCollection(ResourceCollection):
    """
    [PlacementGroup.instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.PlacementGroup.instances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(self, Tags: List[InstancesCreateTagsTagsTypeDef], DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def monitor(self, DryRun: bool = None) -> InstancesMonitorResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start(
        self, AdditionalInfo: str = None, DryRun: bool = None
    ) -> InstancesStartResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop(
        self, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> InstancesStopResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate(self, DryRun: bool = None) -> InstancesTerminateResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unmonitor(self, DryRun: bool = None) -> InstancesUnmonitorResponseTypeDef:
        pass


class SubnetInstancesCollection(ResourceCollection):
    """
    [Subnet.instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Subnet.instances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(self, Tags: List[InstancesCreateTagsTagsTypeDef], DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def monitor(self, DryRun: bool = None) -> InstancesMonitorResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start(
        self, AdditionalInfo: str = None, DryRun: bool = None
    ) -> InstancesStartResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop(
        self, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> InstancesStopResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate(self, DryRun: bool = None) -> InstancesTerminateResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unmonitor(self, DryRun: bool = None) -> InstancesUnmonitorResponseTypeDef:
        pass


class SubnetNetworkInterfacesCollection(ResourceCollection):
    """
    [Subnet.network_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Subnet.network_interfaces)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.NetworkInterface]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.NetworkInterface]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.NetworkInterface]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.NetworkInterface]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VolumeSnapshotsCollection(ResourceCollection):
    """
    [Volume.snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Volume.snapshots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Snapshot]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
    ) -> List[service_resource_scope.Snapshot]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Snapshot]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Snapshot]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VpcAcceptedVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [Vpc.accepted_vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Vpc.accepted_vpc_peering_connections)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.VpcPeeringConnection]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.VpcPeeringConnection]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.VpcPeeringConnection]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.VpcPeeringConnection]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VpcInstancesCollection(ResourceCollection):
    """
    [Vpc.instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Vpc.instances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(self, Tags: List[InstancesCreateTagsTagsTypeDef], DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def monitor(self, DryRun: bool = None) -> InstancesMonitorResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Instance]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start(
        self, AdditionalInfo: str = None, DryRun: bool = None
    ) -> InstancesStartResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop(
        self, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> InstancesStopResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate(self, DryRun: bool = None) -> InstancesTerminateResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unmonitor(self, DryRun: bool = None) -> InstancesUnmonitorResponseTypeDef:
        pass


class VpcInternetGatewaysCollection(ResourceCollection):
    """
    [Vpc.internet_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Vpc.internet_gateways)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.InternetGateway]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.InternetGateway]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.InternetGateway]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.InternetGateway]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VpcNetworkAclsCollection(ResourceCollection):
    """
    [Vpc.network_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Vpc.network_acls)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.NetworkAcl]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.NetworkAcl]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.NetworkAcl]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.NetworkAcl]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VpcNetworkInterfacesCollection(ResourceCollection):
    """
    [Vpc.network_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Vpc.network_interfaces)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.NetworkInterface]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.NetworkInterface]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.NetworkInterface]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.NetworkInterface]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VpcRequestedVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [Vpc.requested_vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Vpc.requested_vpc_peering_connections)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.VpcPeeringConnection]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.VpcPeeringConnection]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.VpcPeeringConnection]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.VpcPeeringConnection]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VpcRouteTablesCollection(ResourceCollection):
    """
    [Vpc.route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Vpc.route_tables)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.RouteTable]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.RouteTable]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.RouteTable]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.RouteTable]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VpcSecurityGroupsCollection(ResourceCollection):
    """
    [Vpc.security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Vpc.security_groups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.SecurityGroup]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.SecurityGroup]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.SecurityGroup]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.SecurityGroup]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VpcSubnetsCollection(ResourceCollection):
    """
    [Vpc.subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Vpc.subnets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Subnet]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[service_resource_scope.Subnet]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Subnet]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Subnet]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass
