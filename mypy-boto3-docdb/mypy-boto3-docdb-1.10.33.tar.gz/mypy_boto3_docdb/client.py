"Main interface for docdb service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_docdb.client as client_scope

# pylint: disable=import-self
import mypy_boto3_docdb.paginator as paginator_scope
from mypy_boto3_docdb.type_defs import (
    ClientAddTagsToResourceTagsTypeDef,
    ClientApplyPendingMaintenanceActionResponseTypeDef,
    ClientCopyDbClusterParameterGroupResponseTypeDef,
    ClientCopyDbClusterParameterGroupTagsTypeDef,
    ClientCopyDbClusterSnapshotResponseTypeDef,
    ClientCopyDbClusterSnapshotTagsTypeDef,
    ClientCreateDbClusterParameterGroupResponseTypeDef,
    ClientCreateDbClusterParameterGroupTagsTypeDef,
    ClientCreateDbClusterResponseTypeDef,
    ClientCreateDbClusterSnapshotResponseTypeDef,
    ClientCreateDbClusterSnapshotTagsTypeDef,
    ClientCreateDbClusterTagsTypeDef,
    ClientCreateDbInstanceResponseTypeDef,
    ClientCreateDbInstanceTagsTypeDef,
    ClientCreateDbSubnetGroupResponseTypeDef,
    ClientCreateDbSubnetGroupTagsTypeDef,
    ClientDeleteDbClusterResponseTypeDef,
    ClientDeleteDbClusterSnapshotResponseTypeDef,
    ClientDeleteDbInstanceResponseTypeDef,
    ClientDescribeCertificatesFiltersTypeDef,
    ClientDescribeCertificatesResponseTypeDef,
    ClientDescribeDbClusterParameterGroupsFiltersTypeDef,
    ClientDescribeDbClusterParameterGroupsResponseTypeDef,
    ClientDescribeDbClusterParametersFiltersTypeDef,
    ClientDescribeDbClusterParametersResponseTypeDef,
    ClientDescribeDbClusterSnapshotAttributesResponseTypeDef,
    ClientDescribeDbClusterSnapshotsFiltersTypeDef,
    ClientDescribeDbClusterSnapshotsResponseTypeDef,
    ClientDescribeDbClustersFiltersTypeDef,
    ClientDescribeDbClustersResponseTypeDef,
    ClientDescribeDbEngineVersionsFiltersTypeDef,
    ClientDescribeDbEngineVersionsResponseTypeDef,
    ClientDescribeDbInstancesFiltersTypeDef,
    ClientDescribeDbInstancesResponseTypeDef,
    ClientDescribeDbSubnetGroupsFiltersTypeDef,
    ClientDescribeDbSubnetGroupsResponseTypeDef,
    ClientDescribeEngineDefaultClusterParametersFiltersTypeDef,
    ClientDescribeEngineDefaultClusterParametersResponseTypeDef,
    ClientDescribeEventCategoriesFiltersTypeDef,
    ClientDescribeEventCategoriesResponseTypeDef,
    ClientDescribeEventsFiltersTypeDef,
    ClientDescribeEventsResponseTypeDef,
    ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef,
    ClientDescribeOrderableDbInstanceOptionsResponseTypeDef,
    ClientDescribePendingMaintenanceActionsFiltersTypeDef,
    ClientDescribePendingMaintenanceActionsResponseTypeDef,
    ClientFailoverDbClusterResponseTypeDef,
    ClientListTagsForResourceFiltersTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef,
    ClientModifyDbClusterParameterGroupParametersTypeDef,
    ClientModifyDbClusterParameterGroupResponseTypeDef,
    ClientModifyDbClusterResponseTypeDef,
    ClientModifyDbClusterSnapshotAttributeResponseTypeDef,
    ClientModifyDbInstanceResponseTypeDef,
    ClientModifyDbSubnetGroupResponseTypeDef,
    ClientRebootDbInstanceResponseTypeDef,
    ClientResetDbClusterParameterGroupParametersTypeDef,
    ClientResetDbClusterParameterGroupResponseTypeDef,
    ClientRestoreDbClusterFromSnapshotResponseTypeDef,
    ClientRestoreDbClusterFromSnapshotTagsTypeDef,
    ClientRestoreDbClusterToPointInTimeResponseTypeDef,
    ClientRestoreDbClusterToPointInTimeTagsTypeDef,
    ClientStartDbClusterResponseTypeDef,
    ClientStopDbClusterResponseTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_docdb.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [DocDB.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_resource(
        self, ResourceName: str, Tags: List[ClientAddTagsToResourceTagsTypeDef]
    ) -> None:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.add_tags_to_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def apply_pending_maintenance_action(
        self, ResourceIdentifier: str, ApplyAction: str, OptInType: str
    ) -> ClientApplyPendingMaintenanceActionResponseTypeDef:
        """
        [Client.apply_pending_maintenance_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.apply_pending_maintenance_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_db_cluster_parameter_group(
        self,
        SourceDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupDescription: str,
        Tags: List[ClientCopyDbClusterParameterGroupTagsTypeDef] = None,
    ) -> ClientCopyDbClusterParameterGroupResponseTypeDef:
        """
        [Client.copy_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.copy_db_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_db_cluster_snapshot(
        self,
        SourceDBClusterSnapshotIdentifier: str,
        TargetDBClusterSnapshotIdentifier: str,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        CopyTags: bool = None,
        Tags: List[ClientCopyDbClusterSnapshotTagsTypeDef] = None,
    ) -> ClientCopyDbClusterSnapshotResponseTypeDef:
        """
        [Client.copy_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.copy_db_cluster_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_cluster(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        MasterUsername: str,
        MasterUserPassword: str,
        AvailabilityZones: List[str] = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        Tags: List[ClientCreateDbClusterTagsTypeDef] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
    ) -> ClientCreateDbClusterResponseTypeDef:
        """
        [Client.create_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.create_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List[ClientCreateDbClusterParameterGroupTagsTypeDef] = None,
    ) -> ClientCreateDbClusterParameterGroupResponseTypeDef:
        """
        [Client.create_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.create_db_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_cluster_snapshot(
        self,
        DBClusterSnapshotIdentifier: str,
        DBClusterIdentifier: str,
        Tags: List[ClientCreateDbClusterSnapshotTagsTypeDef] = None,
    ) -> ClientCreateDbClusterSnapshotResponseTypeDef:
        """
        [Client.create_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.create_db_cluster_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        DBClusterIdentifier: str,
        AvailabilityZone: str = None,
        PreferredMaintenanceWindow: str = None,
        AutoMinorVersionUpgrade: bool = None,
        Tags: List[ClientCreateDbInstanceTagsTypeDef] = None,
        PromotionTier: int = None,
    ) -> ClientCreateDbInstanceResponseTypeDef:
        """
        [Client.create_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.create_db_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_subnet_group(
        self,
        DBSubnetGroupName: str,
        DBSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List[ClientCreateDbSubnetGroupTagsTypeDef] = None,
    ) -> ClientCreateDbSubnetGroupResponseTypeDef:
        """
        [Client.create_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.create_db_subnet_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_cluster(
        self,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
    ) -> ClientDeleteDbClusterResponseTypeDef:
        """
        [Client.delete_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.delete_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_cluster_parameter_group(self, DBClusterParameterGroupName: str) -> None:
        """
        [Client.delete_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.delete_db_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_cluster_snapshot(
        self, DBClusterSnapshotIdentifier: str
    ) -> ClientDeleteDbClusterSnapshotResponseTypeDef:
        """
        [Client.delete_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.delete_db_cluster_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_instance(
        self, DBInstanceIdentifier: str
    ) -> ClientDeleteDbInstanceResponseTypeDef:
        """
        [Client.delete_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.delete_db_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_subnet_group(self, DBSubnetGroupName: str) -> None:
        """
        [Client.delete_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.delete_db_subnet_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_certificates(
        self,
        CertificateIdentifier: str = None,
        Filters: List[ClientDescribeCertificatesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeCertificatesResponseTypeDef:
        """
        [Client.describe_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_certificates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_cluster_parameter_groups(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[ClientDescribeDbClusterParameterGroupsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbClusterParameterGroupsResponseTypeDef:
        """
        [Client.describe_db_cluster_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_db_cluster_parameter_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_cluster_parameters(
        self,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List[ClientDescribeDbClusterParametersFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbClusterParametersResponseTypeDef:
        """
        [Client.describe_db_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_db_cluster_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_cluster_snapshot_attributes(
        self, DBClusterSnapshotIdentifier: str
    ) -> ClientDescribeDbClusterSnapshotAttributesResponseTypeDef:
        """
        [Client.describe_db_cluster_snapshot_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_db_cluster_snapshot_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_cluster_snapshots(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[ClientDescribeDbClusterSnapshotsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
    ) -> ClientDescribeDbClusterSnapshotsResponseTypeDef:
        """
        [Client.describe_db_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_db_cluster_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_clusters(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[ClientDescribeDbClustersFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbClustersResponseTypeDef:
        """
        [Client.describe_db_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_db_clusters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_engine_versions(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[ClientDescribeDbEngineVersionsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
    ) -> ClientDescribeDbEngineVersionsResponseTypeDef:
        """
        [Client.describe_db_engine_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_db_engine_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_instances(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[ClientDescribeDbInstancesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbInstancesResponseTypeDef:
        """
        [Client.describe_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_db_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_subnet_groups(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[ClientDescribeDbSubnetGroupsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbSubnetGroupsResponseTypeDef:
        """
        [Client.describe_db_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_db_subnet_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_engine_default_cluster_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[ClientDescribeEngineDefaultClusterParametersFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEngineDefaultClusterParametersResponseTypeDef:
        """
        [Client.describe_engine_default_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_engine_default_cluster_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_categories(
        self,
        SourceType: str = None,
        Filters: List[ClientDescribeEventCategoriesFiltersTypeDef] = None,
    ) -> ClientDescribeEventCategoriesResponseTypeDef:
        """
        [Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_event_categories)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[ClientDescribeEventsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_orderable_db_instance_options(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List[ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeOrderableDbInstanceOptionsResponseTypeDef:
        """
        [Client.describe_orderable_db_instance_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_orderable_db_instance_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_pending_maintenance_actions(
        self,
        ResourceIdentifier: str = None,
        Filters: List[ClientDescribePendingMaintenanceActionsFiltersTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> ClientDescribePendingMaintenanceActionsResponseTypeDef:
        """
        [Client.describe_pending_maintenance_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.describe_pending_maintenance_actions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def failover_db_cluster(
        self, DBClusterIdentifier: str = None, TargetDBInstanceIdentifier: str = None
    ) -> ClientFailoverDbClusterResponseTypeDef:
        """
        [Client.failover_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.failover_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceName: str, Filters: List[ClientListTagsForResourceFiltersTypeDef] = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_cluster(
        self,
        DBClusterIdentifier: str,
        NewDBClusterIdentifier: str = None,
        ApplyImmediately: bool = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Port: int = None,
        MasterUserPassword: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        CloudwatchLogsExportConfiguration: ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef = None,
        EngineVersion: str = None,
        DeletionProtection: bool = None,
    ) -> ClientModifyDbClusterResponseTypeDef:
        """
        [Client.modify_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.modify_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        Parameters: List[ClientModifyDbClusterParameterGroupParametersTypeDef],
    ) -> ClientModifyDbClusterParameterGroupResponseTypeDef:
        """
        [Client.modify_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.modify_db_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_cluster_snapshot_attribute(
        self,
        DBClusterSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[str] = None,
        ValuesToRemove: List[str] = None,
    ) -> ClientModifyDbClusterSnapshotAttributeResponseTypeDef:
        """
        [Client.modify_db_cluster_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.modify_db_cluster_snapshot_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str = None,
        ApplyImmediately: bool = None,
        PreferredMaintenanceWindow: str = None,
        AutoMinorVersionUpgrade: bool = None,
        NewDBInstanceIdentifier: str = None,
        CACertificateIdentifier: str = None,
        PromotionTier: int = None,
    ) -> ClientModifyDbInstanceResponseTypeDef:
        """
        [Client.modify_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.modify_db_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_subnet_group(
        self, DBSubnetGroupName: str, SubnetIds: List[str], DBSubnetGroupDescription: str = None
    ) -> ClientModifyDbSubnetGroupResponseTypeDef:
        """
        [Client.modify_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.modify_db_subnet_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot_db_instance(
        self, DBInstanceIdentifier: str, ForceFailover: bool = None
    ) -> ClientRebootDbInstanceResponseTypeDef:
        """
        [Client.reboot_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.reboot_db_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List[str]) -> None:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.remove_tags_from_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List[ClientResetDbClusterParameterGroupParametersTypeDef] = None,
    ) -> ClientResetDbClusterParameterGroupResponseTypeDef:
        """
        [Client.reset_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.reset_db_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_db_cluster_from_snapshot(
        self,
        DBClusterIdentifier: str,
        SnapshotIdentifier: str,
        Engine: str,
        AvailabilityZones: List[str] = None,
        EngineVersion: str = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List[ClientRestoreDbClusterFromSnapshotTagsTypeDef] = None,
        KmsKeyId: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
    ) -> ClientRestoreDbClusterFromSnapshotResponseTypeDef:
        """
        [Client.restore_db_cluster_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.restore_db_cluster_from_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_db_cluster_to_point_in_time(
        self,
        DBClusterIdentifier: str,
        SourceDBClusterIdentifier: str,
        RestoreToTime: datetime = None,
        UseLatestRestorableTime: bool = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List[ClientRestoreDbClusterToPointInTimeTagsTypeDef] = None,
        KmsKeyId: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
    ) -> ClientRestoreDbClusterToPointInTimeResponseTypeDef:
        """
        [Client.restore_db_cluster_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.restore_db_cluster_to_point_in_time)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_db_cluster(self, DBClusterIdentifier: str) -> ClientStartDbClusterResponseTypeDef:
        """
        [Client.start_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.start_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_db_cluster(self, DBClusterIdentifier: str) -> ClientStopDbClusterResponseTypeDef:
        """
        [Client.stop_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Client.stop_db_cluster)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_clusters"]
    ) -> paginator_scope.DescribeDBClustersPaginator:
        """
        [Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_engine_versions"]
    ) -> paginator_scope.DescribeDBEngineVersionsPaginator:
        """
        [Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Paginator.DescribeDBEngineVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_instances"]
    ) -> paginator_scope.DescribeDBInstancesPaginator:
        """
        [Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Paginator.DescribeDBInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_subnet_groups"]
    ) -> paginator_scope.DescribeDBSubnetGroupsPaginator:
        """
        [Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Paginator.DescribeDBSubnetGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> paginator_scope.DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Paginator.DescribeEvents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_orderable_db_instance_options"]
    ) -> paginator_scope.DescribeOrderableDBInstanceOptionsPaginator:
        """
        [Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Paginator.DescribeOrderableDBInstanceOptions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["db_instance_available"]
    ) -> waiter_scope.DBInstanceAvailableWaiter:
        """
        [Waiter.DBInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Waiter.DBInstanceAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["db_instance_deleted"]
    ) -> waiter_scope.DBInstanceDeletedWaiter:
        """
        [Waiter.DBInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Waiter.DBInstanceDeleted)
        """


class Exceptions:
    AuthorizationNotFoundFault: Boto3ClientError
    CertificateNotFoundFault: Boto3ClientError
    ClientError: Boto3ClientError
    DBClusterAlreadyExistsFault: Boto3ClientError
    DBClusterNotFoundFault: Boto3ClientError
    DBClusterParameterGroupNotFoundFault: Boto3ClientError
    DBClusterQuotaExceededFault: Boto3ClientError
    DBClusterSnapshotAlreadyExistsFault: Boto3ClientError
    DBClusterSnapshotNotFoundFault: Boto3ClientError
    DBInstanceAlreadyExistsFault: Boto3ClientError
    DBInstanceNotFoundFault: Boto3ClientError
    DBParameterGroupAlreadyExistsFault: Boto3ClientError
    DBParameterGroupNotFoundFault: Boto3ClientError
    DBParameterGroupQuotaExceededFault: Boto3ClientError
    DBSecurityGroupNotFoundFault: Boto3ClientError
    DBSnapshotAlreadyExistsFault: Boto3ClientError
    DBSnapshotNotFoundFault: Boto3ClientError
    DBSubnetGroupAlreadyExistsFault: Boto3ClientError
    DBSubnetGroupDoesNotCoverEnoughAZs: Boto3ClientError
    DBSubnetGroupNotFoundFault: Boto3ClientError
    DBSubnetGroupQuotaExceededFault: Boto3ClientError
    DBSubnetQuotaExceededFault: Boto3ClientError
    DBUpgradeDependencyFailureFault: Boto3ClientError
    InstanceQuotaExceededFault: Boto3ClientError
    InsufficientDBClusterCapacityFault: Boto3ClientError
    InsufficientDBInstanceCapacityFault: Boto3ClientError
    InsufficientStorageClusterCapacityFault: Boto3ClientError
    InvalidDBClusterSnapshotStateFault: Boto3ClientError
    InvalidDBClusterStateFault: Boto3ClientError
    InvalidDBInstanceStateFault: Boto3ClientError
    InvalidDBParameterGroupStateFault: Boto3ClientError
    InvalidDBSecurityGroupStateFault: Boto3ClientError
    InvalidDBSnapshotStateFault: Boto3ClientError
    InvalidDBSubnetGroupStateFault: Boto3ClientError
    InvalidDBSubnetStateFault: Boto3ClientError
    InvalidRestoreFault: Boto3ClientError
    InvalidSubnet: Boto3ClientError
    InvalidVPCNetworkStateFault: Boto3ClientError
    KMSKeyNotAccessibleFault: Boto3ClientError
    ResourceNotFoundFault: Boto3ClientError
    SharedSnapshotQuotaExceededFault: Boto3ClientError
    SnapshotQuotaExceededFault: Boto3ClientError
    StorageQuotaExceededFault: Boto3ClientError
    StorageTypeNotSupportedFault: Boto3ClientError
    SubnetAlreadyInUse: Boto3ClientError
