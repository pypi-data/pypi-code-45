"Main interface for ec2 service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_ec2.type_defs import (
    BundleTaskCompleteWaitFiltersTypeDef,
    BundleTaskCompleteWaitWaiterConfigTypeDef,
    ConversionTaskCancelledWaitWaiterConfigTypeDef,
    ConversionTaskCompletedWaitWaiterConfigTypeDef,
    ConversionTaskDeletedWaitWaiterConfigTypeDef,
    CustomerGatewayAvailableWaitFiltersTypeDef,
    CustomerGatewayAvailableWaitWaiterConfigTypeDef,
    ExportTaskCancelledWaitWaiterConfigTypeDef,
    ExportTaskCompletedWaitWaiterConfigTypeDef,
    ImageAvailableWaitFiltersTypeDef,
    ImageAvailableWaitWaiterConfigTypeDef,
    ImageExistsWaitFiltersTypeDef,
    ImageExistsWaitWaiterConfigTypeDef,
    InstanceExistsWaitFiltersTypeDef,
    InstanceExistsWaitWaiterConfigTypeDef,
    InstanceRunningWaitFiltersTypeDef,
    InstanceRunningWaitWaiterConfigTypeDef,
    InstanceStatusOkWaitFiltersTypeDef,
    InstanceStatusOkWaitWaiterConfigTypeDef,
    InstanceStoppedWaitFiltersTypeDef,
    InstanceStoppedWaitWaiterConfigTypeDef,
    InstanceTerminatedWaitFiltersTypeDef,
    InstanceTerminatedWaitWaiterConfigTypeDef,
    KeyPairExistsWaitFiltersTypeDef,
    KeyPairExistsWaitWaiterConfigTypeDef,
    NatGatewayAvailableWaitFiltersTypeDef,
    NatGatewayAvailableWaitWaiterConfigTypeDef,
    NetworkInterfaceAvailableWaitFiltersTypeDef,
    NetworkInterfaceAvailableWaitWaiterConfigTypeDef,
    PasswordDataAvailableWaitWaiterConfigTypeDef,
    SecurityGroupExistsWaitFiltersTypeDef,
    SecurityGroupExistsWaitWaiterConfigTypeDef,
    SnapshotCompletedWaitFiltersTypeDef,
    SnapshotCompletedWaitWaiterConfigTypeDef,
    SpotInstanceRequestFulfilledWaitFiltersTypeDef,
    SpotInstanceRequestFulfilledWaitWaiterConfigTypeDef,
    SubnetAvailableWaitFiltersTypeDef,
    SubnetAvailableWaitWaiterConfigTypeDef,
    SystemStatusOkWaitFiltersTypeDef,
    SystemStatusOkWaitWaiterConfigTypeDef,
    VolumeAvailableWaitFiltersTypeDef,
    VolumeAvailableWaitWaiterConfigTypeDef,
    VolumeDeletedWaitFiltersTypeDef,
    VolumeDeletedWaitWaiterConfigTypeDef,
    VolumeInUseWaitFiltersTypeDef,
    VolumeInUseWaitWaiterConfigTypeDef,
    VpcAvailableWaitFiltersTypeDef,
    VpcAvailableWaitWaiterConfigTypeDef,
    VpcExistsWaitFiltersTypeDef,
    VpcExistsWaitWaiterConfigTypeDef,
    VpcPeeringConnectionDeletedWaitFiltersTypeDef,
    VpcPeeringConnectionDeletedWaitWaiterConfigTypeDef,
    VpcPeeringConnectionExistsWaitFiltersTypeDef,
    VpcPeeringConnectionExistsWaitWaiterConfigTypeDef,
    VpnConnectionAvailableWaitFiltersTypeDef,
    VpnConnectionAvailableWaitWaiterConfigTypeDef,
    VpnConnectionDeletedWaitFiltersTypeDef,
    VpnConnectionDeletedWaitWaiterConfigTypeDef,
)


__all__ = (
    "BundleTaskCompleteWaiter",
    "ConversionTaskCancelledWaiter",
    "ConversionTaskCompletedWaiter",
    "ConversionTaskDeletedWaiter",
    "CustomerGatewayAvailableWaiter",
    "ExportTaskCancelledWaiter",
    "ExportTaskCompletedWaiter",
    "ImageAvailableWaiter",
    "ImageExistsWaiter",
    "InstanceExistsWaiter",
    "InstanceRunningWaiter",
    "InstanceStatusOkWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
    "KeyPairExistsWaiter",
    "NatGatewayAvailableWaiter",
    "NetworkInterfaceAvailableWaiter",
    "PasswordDataAvailableWaiter",
    "SecurityGroupExistsWaiter",
    "SnapshotCompletedWaiter",
    "SpotInstanceRequestFulfilledWaiter",
    "SubnetAvailableWaiter",
    "SystemStatusOkWaiter",
    "VolumeAvailableWaiter",
    "VolumeDeletedWaiter",
    "VolumeInUseWaiter",
    "VpcAvailableWaiter",
    "VpcExistsWaiter",
    "VpcPeeringConnectionDeletedWaiter",
    "VpcPeeringConnectionExistsWaiter",
    "VpnConnectionAvailableWaiter",
    "VpnConnectionDeletedWaiter",
)


class BundleTaskCompleteWaiter(Boto3Waiter):
    """
    Waiter for `bundle_task_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        BundleIds: List[str] = None,
        Filters: List[BundleTaskCompleteWaitFiltersTypeDef] = None,
        DryRun: bool = None,
        WaiterConfig: BundleTaskCompleteWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [bundle_task_complete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.bundle_task_complete.wait)
        """


class ConversionTaskCancelledWaiter(Boto3Waiter):
    """
    Waiter for `conversion_task_cancelled` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ConversionTaskIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: ConversionTaskCancelledWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [conversion_task_cancelled.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.conversion_task_cancelled.wait)
        """


class ConversionTaskCompletedWaiter(Boto3Waiter):
    """
    Waiter for `conversion_task_completed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ConversionTaskIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: ConversionTaskCompletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [conversion_task_completed.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.conversion_task_completed.wait)
        """


class ConversionTaskDeletedWaiter(Boto3Waiter):
    """
    Waiter for `conversion_task_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ConversionTaskIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: ConversionTaskDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [conversion_task_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.conversion_task_deleted.wait)
        """


class CustomerGatewayAvailableWaiter(Boto3Waiter):
    """
    Waiter for `customer_gateway_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        CustomerGatewayIds: List[str] = None,
        Filters: List[CustomerGatewayAvailableWaitFiltersTypeDef] = None,
        DryRun: bool = None,
        WaiterConfig: CustomerGatewayAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [customer_gateway_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.customer_gateway_available.wait)
        """


class ExportTaskCancelledWaiter(Boto3Waiter):
    """
    Waiter for `export_task_cancelled` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ExportTaskIds: List[str] = None,
        WaiterConfig: ExportTaskCancelledWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [export_task_cancelled.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.export_task_cancelled.wait)
        """


class ExportTaskCompletedWaiter(Boto3Waiter):
    """
    Waiter for `export_task_completed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ExportTaskIds: List[str] = None,
        WaiterConfig: ExportTaskCompletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [export_task_completed.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.export_task_completed.wait)
        """


class ImageAvailableWaiter(Boto3Waiter):
    """
    Waiter for `image_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ExecutableUsers: List[str] = None,
        Filters: List[ImageAvailableWaitFiltersTypeDef] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: ImageAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [image_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.image_available.wait)
        """


class ImageExistsWaiter(Boto3Waiter):
    """
    Waiter for `image_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ExecutableUsers: List[str] = None,
        Filters: List[ImageExistsWaitFiltersTypeDef] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: ImageExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [image_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.image_exists.wait)
        """


class InstanceExistsWaiter(Boto3Waiter):
    """
    Waiter for `instance_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[InstanceExistsWaitFiltersTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: InstanceExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [instance_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.instance_exists.wait)
        """


class InstanceRunningWaiter(Boto3Waiter):
    """
    Waiter for `instance_running` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[InstanceRunningWaitFiltersTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: InstanceRunningWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [instance_running.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.instance_running.wait)
        """


class InstanceStatusOkWaiter(Boto3Waiter):
    """
    Waiter for `instance_status_ok` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[InstanceStatusOkWaitFiltersTypeDef] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        WaiterConfig: InstanceStatusOkWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [instance_status_ok.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.instance_status_ok.wait)
        """


class InstanceStoppedWaiter(Boto3Waiter):
    """
    Waiter for `instance_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[InstanceStoppedWaitFiltersTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: InstanceStoppedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [instance_stopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.instance_stopped.wait)
        """


class InstanceTerminatedWaiter(Boto3Waiter):
    """
    Waiter for `instance_terminated` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[InstanceTerminatedWaitFiltersTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: InstanceTerminatedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [instance_terminated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.instance_terminated.wait)
        """


class KeyPairExistsWaiter(Boto3Waiter):
    """
    Waiter for `key_pair_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[KeyPairExistsWaitFiltersTypeDef] = None,
        KeyNames: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: KeyPairExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [key_pair_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.key_pair_exists.wait)
        """


class NatGatewayAvailableWaiter(Boto3Waiter):
    """
    Waiter for `nat_gateway_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[NatGatewayAvailableWaitFiltersTypeDef] = None,
        MaxResults: int = None,
        NatGatewayIds: List[str] = None,
        NextToken: str = None,
        WaiterConfig: NatGatewayAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [nat_gateway_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.nat_gateway_available.wait)
        """


class NetworkInterfaceAvailableWaiter(Boto3Waiter):
    """
    Waiter for `network_interface_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[NetworkInterfaceAvailableWaitFiltersTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: NetworkInterfaceAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [network_interface_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.network_interface_available.wait)
        """


class PasswordDataAvailableWaiter(Boto3Waiter):
    """
    Waiter for `password_data_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        InstanceId: str,
        DryRun: bool = None,
        WaiterConfig: PasswordDataAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [password_data_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.password_data_available.wait)
        """


class SecurityGroupExistsWaiter(Boto3Waiter):
    """
    Waiter for `security_group_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[SecurityGroupExistsWaitFiltersTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: SecurityGroupExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [security_group_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.security_group_exists.wait)
        """


class SnapshotCompletedWaiter(Boto3Waiter):
    """
    Waiter for `snapshot_completed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[SnapshotCompletedWaitFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: SnapshotCompletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [snapshot_completed.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.snapshot_completed.wait)
        """


class SpotInstanceRequestFulfilledWaiter(Boto3Waiter):
    """
    Waiter for `spot_instance_request_fulfilled` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[SpotInstanceRequestFulfilledWaitFiltersTypeDef] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: SpotInstanceRequestFulfilledWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [spot_instance_request_fulfilled.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.spot_instance_request_fulfilled.wait)
        """


class SubnetAvailableWaiter(Boto3Waiter):
    """
    Waiter for `subnet_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[SubnetAvailableWaitFiltersTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: SubnetAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [subnet_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.subnet_available.wait)
        """


class SystemStatusOkWaiter(Boto3Waiter):
    """
    Waiter for `system_status_ok` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[SystemStatusOkWaitFiltersTypeDef] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        WaiterConfig: SystemStatusOkWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [system_status_ok.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.system_status_ok.wait)
        """


class VolumeAvailableWaiter(Boto3Waiter):
    """
    Waiter for `volume_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[VolumeAvailableWaitFiltersTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: VolumeAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [volume_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.volume_available.wait)
        """


class VolumeDeletedWaiter(Boto3Waiter):
    """
    Waiter for `volume_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[VolumeDeletedWaitFiltersTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: VolumeDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [volume_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.volume_deleted.wait)
        """


class VolumeInUseWaiter(Boto3Waiter):
    """
    Waiter for `volume_in_use` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[VolumeInUseWaitFiltersTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: VolumeInUseWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [volume_in_use.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.volume_in_use.wait)
        """


class VpcAvailableWaiter(Boto3Waiter):
    """
    Waiter for `vpc_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[VpcAvailableWaitFiltersTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: VpcAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [vpc_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.vpc_available.wait)
        """


class VpcExistsWaiter(Boto3Waiter):
    """
    Waiter for `vpc_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[VpcExistsWaitFiltersTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: VpcExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [vpc_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.vpc_exists.wait)
        """


class VpcPeeringConnectionDeletedWaiter(Boto3Waiter):
    """
    Waiter for `vpc_peering_connection_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[VpcPeeringConnectionDeletedWaitFiltersTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: VpcPeeringConnectionDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [vpc_peering_connection_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.vpc_peering_connection_deleted.wait)
        """


class VpcPeeringConnectionExistsWaiter(Boto3Waiter):
    """
    Waiter for `vpc_peering_connection_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[VpcPeeringConnectionExistsWaitFiltersTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: VpcPeeringConnectionExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [vpc_peering_connection_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.vpc_peering_connection_exists.wait)
        """


class VpnConnectionAvailableWaiter(Boto3Waiter):
    """
    Waiter for `vpn_connection_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[VpnConnectionAvailableWaitFiltersTypeDef] = None,
        VpnConnectionIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: VpnConnectionAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [vpn_connection_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.vpn_connection_available.wait)
        """


class VpnConnectionDeletedWaiter(Boto3Waiter):
    """
    Waiter for `vpn_connection_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[VpnConnectionDeletedWaitFiltersTypeDef] = None,
        VpnConnectionIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: VpnConnectionDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [vpn_connection_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ec2.html#EC2.Waiter.vpn_connection_deleted.wait)
        """
