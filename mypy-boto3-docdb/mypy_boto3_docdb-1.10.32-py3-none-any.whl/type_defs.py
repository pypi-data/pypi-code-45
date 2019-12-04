"Main interface for docdb service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseTypeDef",
    "ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCopyDbClusterParameterGroupResponseTypeDef",
    "ClientCopyDbClusterParameterGroupTagsTypeDef",
    "ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCopyDbClusterSnapshotResponseTypeDef",
    "ClientCopyDbClusterSnapshotTagsTypeDef",
    "ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCreateDbClusterParameterGroupResponseTypeDef",
    "ClientCreateDbClusterParameterGroupTagsTypeDef",
    "ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientCreateDbClusterResponseDBClusterTypeDef",
    "ClientCreateDbClusterResponseTypeDef",
    "ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCreateDbClusterSnapshotResponseTypeDef",
    "ClientCreateDbClusterSnapshotTagsTypeDef",
    "ClientCreateDbClusterTagsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceTypeDef",
    "ClientCreateDbInstanceResponseTypeDef",
    "ClientCreateDbInstanceTagsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientCreateDbSubnetGroupResponseTypeDef",
    "ClientCreateDbSubnetGroupTagsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterTypeDef",
    "ClientDeleteDbClusterResponseTypeDef",
    "ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientDeleteDbClusterSnapshotResponseTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceTypeDef",
    "ClientDeleteDbInstanceResponseTypeDef",
    "ClientDescribeCertificatesFiltersTypeDef",
    "ClientDescribeCertificatesResponseCertificatesTypeDef",
    "ClientDescribeCertificatesResponseTypeDef",
    "ClientDescribeDbClusterParameterGroupsFiltersTypeDef",
    "ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef",
    "ClientDescribeDbClusterParameterGroupsResponseTypeDef",
    "ClientDescribeDbClusterParametersFiltersTypeDef",
    "ClientDescribeDbClusterParametersResponseParametersTypeDef",
    "ClientDescribeDbClusterParametersResponseTypeDef",
    "ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    "ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef",
    "ClientDescribeDbClusterSnapshotAttributesResponseTypeDef",
    "ClientDescribeDbClusterSnapshotsFiltersTypeDef",
    "ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef",
    "ClientDescribeDbClusterSnapshotsResponseTypeDef",
    "ClientDescribeDbClustersFiltersTypeDef",
    "ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef",
    "ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef",
    "ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef",
    "ClientDescribeDbClustersResponseDBClustersTypeDef",
    "ClientDescribeDbClustersResponseTypeDef",
    "ClientDescribeDbEngineVersionsFiltersTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef",
    "ClientDescribeDbEngineVersionsResponseTypeDef",
    "ClientDescribeDbInstancesFiltersTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesTypeDef",
    "ClientDescribeDbInstancesResponseTypeDef",
    "ClientDescribeDbSubnetGroupsFiltersTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef",
    "ClientDescribeDbSubnetGroupsResponseTypeDef",
    "ClientDescribeEngineDefaultClusterParametersFiltersTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseTypeDef",
    "ClientDescribeEventCategoriesFiltersTypeDef",
    "ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    "ClientDescribeEventCategoriesResponseTypeDef",
    "ClientDescribeEventsFiltersTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseTypeDef",
    "ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponseTypeDef",
    "ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientFailoverDbClusterResponseDBClusterTypeDef",
    "ClientFailoverDbClusterResponseTypeDef",
    "ClientListTagsForResourceFiltersTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef",
    "ClientModifyDbClusterParameterGroupParametersTypeDef",
    "ClientModifyDbClusterParameterGroupResponseTypeDef",
    "ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientModifyDbClusterResponseDBClusterTypeDef",
    "ClientModifyDbClusterResponseTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceTypeDef",
    "ClientModifyDbInstanceResponseTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientModifyDbSubnetGroupResponseTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceTypeDef",
    "ClientRebootDbInstanceResponseTypeDef",
    "ClientResetDbClusterParameterGroupParametersTypeDef",
    "ClientResetDbClusterParameterGroupResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotTagsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseTypeDef",
    "ClientRestoreDbClusterToPointInTimeTagsTypeDef",
    "ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientStartDbClusterResponseDBClusterTypeDef",
    "ClientStartDbClusterResponseTypeDef",
    "ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientStopDbClusterResponseDBClusterTypeDef",
    "ClientStopDbClusterResponseTypeDef",
    "DbInstanceAvailableWaitFiltersTypeDef",
    "DbInstanceAvailableWaitWaiterConfigTypeDef",
    "DbInstanceDeletedWaitFiltersTypeDef",
    "DbInstanceDeletedWaitWaiterConfigTypeDef",
    "DescribeDBClustersPaginateFiltersTypeDef",
    "DescribeDBClustersPaginatePaginationConfigTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersTypeDef",
    "DescribeDBClustersPaginateResponseTypeDef",
    "DescribeDBEngineVersionsPaginateFiltersTypeDef",
    "DescribeDBEngineVersionsPaginatePaginationConfigTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef",
    "DescribeDBEngineVersionsPaginateResponseTypeDef",
    "DescribeDBInstancesPaginateFiltersTypeDef",
    "DescribeDBInstancesPaginatePaginationConfigTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesTypeDef",
    "DescribeDBInstancesPaginateResponseTypeDef",
    "DescribeDBSubnetGroupsPaginateFiltersTypeDef",
    "DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseTypeDef",
    "DescribeEventsPaginateFiltersTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef",
)


_ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsToResourceTagsTypeDef(_ClientAddTagsToResourceTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
      - **Key** *(string) --*

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
        Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef(
    _ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
):
    pass


_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef(
    _ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef
):
    """
    - **ResourcePendingMaintenanceActions** *(dict) --*

      Represents the output of  ApplyPendingMaintenanceAction .
      - **ResourceIdentifier** *(string) --*

        The Amazon Resource Name (ARN) of the resource that has pending maintenance actions.
    """


_ClientApplyPendingMaintenanceActionResponseTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseTypeDef",
    {
        "ResourcePendingMaintenanceActions": ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseTypeDef(
    _ClientApplyPendingMaintenanceActionResponseTypeDef
):
    """
    - *(dict) --*

      - **ResourcePendingMaintenanceActions** *(dict) --*

        Represents the output of  ApplyPendingMaintenanceAction .
        - **ResourceIdentifier** *(string) --*

          The Amazon Resource Name (ARN) of the resource that has pending maintenance actions.
    """


_ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef = TypedDict(
    "_ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)


class ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef(
    _ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
):
    """
    - **DBClusterParameterGroup** *(dict) --*

      Detailed information about a DB cluster parameter group.
      - **DBClusterParameterGroupName** *(string) --*

        Provides the name of the DB cluster parameter group.
    """


_ClientCopyDbClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientCopyDbClusterParameterGroupResponseTypeDef",
    {
        "DBClusterParameterGroup": ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
    },
    total=False,
)


class ClientCopyDbClusterParameterGroupResponseTypeDef(
    _ClientCopyDbClusterParameterGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **DBClusterParameterGroup** *(dict) --*

        Detailed information about a DB cluster parameter group.
        - **DBClusterParameterGroupName** *(string) --*

          Provides the name of the DB cluster parameter group.
    """


_ClientCopyDbClusterParameterGroupTagsTypeDef = TypedDict(
    "_ClientCopyDbClusterParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCopyDbClusterParameterGroupTagsTypeDef(_ClientCopyDbClusterParameterGroupTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
      - **Key** *(string) --*

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
        Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "_ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)


class ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef(
    _ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef
):
    """
    - **DBClusterSnapshot** *(dict) --*

      Detailed information about a DB cluster snapshot.
      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster snapshot
        can be restored in.
        - *(string) --*
    """


_ClientCopyDbClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientCopyDbClusterSnapshotResponseTypeDef",
    {"DBClusterSnapshot": ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef},
    total=False,
)


class ClientCopyDbClusterSnapshotResponseTypeDef(_ClientCopyDbClusterSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **DBClusterSnapshot** *(dict) --*

        Detailed information about a DB cluster snapshot.
        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster
          snapshot can be restored in.
          - *(string) --*
    """


_ClientCopyDbClusterSnapshotTagsTypeDef = TypedDict(
    "_ClientCopyDbClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCopyDbClusterSnapshotTagsTypeDef(_ClientCopyDbClusterSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
      - **Key** *(string) --*

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
        Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef = TypedDict(
    "_ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)


class ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef(
    _ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
):
    """
    - **DBClusterParameterGroup** *(dict) --*

      Detailed information about a DB cluster parameter group.
      - **DBClusterParameterGroupName** *(string) --*

        Provides the name of the DB cluster parameter group.
    """


_ClientCreateDbClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientCreateDbClusterParameterGroupResponseTypeDef",
    {
        "DBClusterParameterGroup": ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
    },
    total=False,
)


class ClientCreateDbClusterParameterGroupResponseTypeDef(
    _ClientCreateDbClusterParameterGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **DBClusterParameterGroup** *(dict) --*

        Detailed information about a DB cluster parameter group.
        - **DBClusterParameterGroupName** *(string) --*

          Provides the name of the DB cluster parameter group.
    """


_ClientCreateDbClusterParameterGroupTagsTypeDef = TypedDict(
    "_ClientCreateDbClusterParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbClusterParameterGroupTagsTypeDef(
    _ClientCreateDbClusterParameterGroupTagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
      - **Key** *(string) --*

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
        Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    pass


_ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    pass


_ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientCreateDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientCreateDbClusterResponseDBClusterTypeDef(_ClientCreateDbClusterResponseDBClusterTypeDef):
    """
    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.
      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.
        - *(string) --*
    """


_ClientCreateDbClusterResponseTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseTypeDef",
    {"DBCluster": ClientCreateDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientCreateDbClusterResponseTypeDef(_ClientCreateDbClusterResponseTypeDef):
    """
    - *(dict) --*

      - **DBCluster** *(dict) --*

        Detailed information about a DB cluster.
        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
          created in.
          - *(string) --*
    """


_ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "_ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)


class ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef(
    _ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef
):
    """
    - **DBClusterSnapshot** *(dict) --*

      Detailed information about a DB cluster snapshot.
      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster snapshot
        can be restored in.
        - *(string) --*
    """


_ClientCreateDbClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateDbClusterSnapshotResponseTypeDef",
    {"DBClusterSnapshot": ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef},
    total=False,
)


class ClientCreateDbClusterSnapshotResponseTypeDef(_ClientCreateDbClusterSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **DBClusterSnapshot** *(dict) --*

        Detailed information about a DB cluster snapshot.
        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster
          snapshot can be restored in.
          - *(string) --*
    """


_ClientCreateDbClusterSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateDbClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbClusterSnapshotTagsTypeDef(_ClientCreateDbClusterSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
      - **Key** *(string) --*

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
        Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbClusterTagsTypeDef = TypedDict(
    "_ClientCreateDbClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbClusterTagsTypeDef(_ClientCreateDbClusterTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
      - **Key** *(string) --*

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
        Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    pass


_ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef
):
    pass


_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    pass


_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    pass


_ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientCreateDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Detailed information about a DB instance.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-provided database identifier. This identifier is the unique key that
        identifies a DB instance.
    """


_ClientCreateDbInstanceResponseTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseTypeDef",
    {"DBInstance": ClientCreateDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientCreateDbInstanceResponseTypeDef(_ClientCreateDbInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **DBInstance** *(dict) --*

        Detailed information about a DB instance.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-provided database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientCreateDbInstanceTagsTypeDef = TypedDict(
    "_ClientCreateDbInstanceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbInstanceTagsTypeDef(_ClientCreateDbInstanceTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
      - **Key** *(string) --*

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
        Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef(
    _ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef(
    _ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef
):
    """
    - **DBSubnetGroup** *(dict) --*

      Detailed information about a DB subnet group.
      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.
    """


_ClientCreateDbSubnetGroupResponseTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupResponseTypeDef",
    {"DBSubnetGroup": ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef},
    total=False,
)


class ClientCreateDbSubnetGroupResponseTypeDef(_ClientCreateDbSubnetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **DBSubnetGroup** *(dict) --*

        Detailed information about a DB subnet group.
        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.
    """


_ClientCreateDbSubnetGroupTagsTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbSubnetGroupTagsTypeDef(_ClientCreateDbSubnetGroupTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
      - **Key** *(string) --*

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
        Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    pass


_ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    pass


_ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientDeleteDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterTypeDef(_ClientDeleteDbClusterResponseDBClusterTypeDef):
    """
    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.
      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.
        - *(string) --*
    """


_ClientDeleteDbClusterResponseTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseTypeDef",
    {"DBCluster": ClientDeleteDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientDeleteDbClusterResponseTypeDef(_ClientDeleteDbClusterResponseTypeDef):
    """
    - *(dict) --*

      - **DBCluster** *(dict) --*

        Detailed information about a DB cluster.
        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
          created in.
          - *(string) --*
    """


_ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "_ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)


class ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef(
    _ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef
):
    """
    - **DBClusterSnapshot** *(dict) --*

      Detailed information about a DB cluster snapshot.
      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster snapshot
        can be restored in.
        - *(string) --*
    """


_ClientDeleteDbClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientDeleteDbClusterSnapshotResponseTypeDef",
    {"DBClusterSnapshot": ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef},
    total=False,
)


class ClientDeleteDbClusterSnapshotResponseTypeDef(_ClientDeleteDbClusterSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **DBClusterSnapshot** *(dict) --*

        Detailed information about a DB cluster snapshot.
        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster
          snapshot can be restored in.
          - *(string) --*
    """


_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    pass


_ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef
):
    pass


_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    pass


_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    pass


_ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientDeleteDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Detailed information about a DB instance.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-provided database identifier. This identifier is the unique key that
        identifies a DB instance.
    """


_ClientDeleteDbInstanceResponseTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseTypeDef",
    {"DBInstance": ClientDeleteDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientDeleteDbInstanceResponseTypeDef(_ClientDeleteDbInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **DBInstance** *(dict) --*

        Detailed information about a DB instance.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-provided database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_RequiredClientDescribeCertificatesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeCertificatesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeCertificatesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeCertificatesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeCertificatesFiltersTypeDef(
    _RequiredClientDescribeCertificatesFiltersTypeDef,
    _OptionalClientDescribeCertificatesFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientDescribeCertificatesResponseCertificatesTypeDef = TypedDict(
    "_ClientDescribeCertificatesResponseCertificatesTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateType": str,
        "Thumbprint": str,
        "ValidFrom": datetime,
        "ValidTill": datetime,
        "CertificateArn": str,
    },
    total=False,
)


class ClientDescribeCertificatesResponseCertificatesTypeDef(
    _ClientDescribeCertificatesResponseCertificatesTypeDef
):
    """
    - *(dict) --*

      A certificate authority (CA) certificate for an AWS account.
      - **CertificateIdentifier** *(string) --*

        The unique key that identifies a certificate.
        Example: ``rds-ca-2019``
    """


_ClientDescribeCertificatesResponseTypeDef = TypedDict(
    "_ClientDescribeCertificatesResponseTypeDef",
    {"Certificates": List[ClientDescribeCertificatesResponseCertificatesTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeCertificatesResponseTypeDef(_ClientDescribeCertificatesResponseTypeDef):
    """
    - *(dict) --*

      - **Certificates** *(list) --*

        A list of certificates for this AWS account.
        - *(dict) --*

          A certificate authority (CA) certificate for an AWS account.
          - **CertificateIdentifier** *(string) --*

            The unique key that identifies a certificate.
            Example: ``rds-ca-2019``
    """


_RequiredClientDescribeDbClusterParameterGroupsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbClusterParameterGroupsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbClusterParameterGroupsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbClusterParameterGroupsFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeDbClusterParameterGroupsFiltersTypeDef(
    _RequiredClientDescribeDbClusterParameterGroupsFiltersTypeDef,
    _OptionalClientDescribeDbClusterParameterGroupsFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef = TypedDict(
    "_ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)


class ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef(
    _ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef
):
    pass


_ClientDescribeDbClusterParameterGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterParameterGroupsResponseTypeDef",
    {
        "Marker": str,
        "DBClusterParameterGroups": List[
            ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbClusterParameterGroupsResponseTypeDef(
    _ClientDescribeDbClusterParameterGroupsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of  DBClusterParameterGroups .
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_RequiredClientDescribeDbClusterParametersFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbClusterParametersFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbClusterParametersFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbClusterParametersFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbClusterParametersFiltersTypeDef(
    _RequiredClientDescribeDbClusterParametersFiltersTypeDef,
    _OptionalClientDescribeDbClusterParametersFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientDescribeDbClusterParametersResponseParametersTypeDef = TypedDict(
    "_ClientDescribeDbClusterParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": Literal["immediate", "pending-reboot"],
    },
    total=False,
)


class ClientDescribeDbClusterParametersResponseParametersTypeDef(
    _ClientDescribeDbClusterParametersResponseParametersTypeDef
):
    """
    - *(dict) --*

      Detailed information about an individual parameter.
      - **ParameterName** *(string) --*

        Specifies the name of the parameter.
    """


_ClientDescribeDbClusterParametersResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterParametersResponseTypeDef",
    {"Parameters": List[ClientDescribeDbClusterParametersResponseParametersTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeDbClusterParametersResponseTypeDef(
    _ClientDescribeDbClusterParametersResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of  DBClusterParameterGroup .
      - **Parameters** *(list) --*

        Provides a list of parameters for the DB cluster parameter group.
        - *(dict) --*

          Detailed information about an individual parameter.
          - **ParameterName** *(string) --*

            Specifies the name of the parameter.
    """


_ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    {"AttributeName": str, "AttributeValues": List[str]},
    total=False,
)


class ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef(
    _ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
):
    pass


_ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterSnapshotAttributes": List[
            ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef(
    _ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef
):
    """
    - **DBClusterSnapshotAttributesResult** *(dict) --*

      Detailed information about the attributes that are associated with a DB cluster snapshot.
      - **DBClusterSnapshotIdentifier** *(string) --*

        The identifier of the DB cluster snapshot that the attributes apply to.
    """


_ClientDescribeDbClusterSnapshotAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotAttributesResponseTypeDef",
    {
        "DBClusterSnapshotAttributesResult": ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef
    },
    total=False,
)


class ClientDescribeDbClusterSnapshotAttributesResponseTypeDef(
    _ClientDescribeDbClusterSnapshotAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **DBClusterSnapshotAttributesResult** *(dict) --*

        Detailed information about the attributes that are associated with a DB cluster snapshot.
        - **DBClusterSnapshotIdentifier** *(string) --*

          The identifier of the DB cluster snapshot that the attributes apply to.
    """


_RequiredClientDescribeDbClusterSnapshotsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbClusterSnapshotsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbClusterSnapshotsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbClusterSnapshotsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbClusterSnapshotsFiltersTypeDef(
    _RequiredClientDescribeDbClusterSnapshotsFiltersTypeDef,
    _OptionalClientDescribeDbClusterSnapshotsFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)


class ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef(
    _ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef
):
    pass


_ClientDescribeDbClusterSnapshotsResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotsResponseTypeDef",
    {
        "Marker": str,
        "DBClusterSnapshots": List[
            ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbClusterSnapshotsResponseTypeDef(
    _ClientDescribeDbClusterSnapshotsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of  DescribeDBClusterSnapshots .
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_RequiredClientDescribeDbClustersFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbClustersFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbClustersFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbClustersFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbClustersFiltersTypeDef(
    _RequiredClientDescribeDbClustersFiltersTypeDef, _OptionalClientDescribeDbClustersFiltersTypeDef
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef(
    _ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef
):
    pass


_ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef(
    _ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef
):
    pass


_ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef(
    _ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef
):
    pass


_ClientDescribeDbClustersResponseDBClustersTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[
            ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersTypeDef(
    _ClientDescribeDbClustersResponseDBClustersTypeDef
):
    pass


_ClientDescribeDbClustersResponseTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseTypeDef",
    {"Marker": str, "DBClusters": List[ClientDescribeDbClustersResponseDBClustersTypeDef]},
    total=False,
)


class ClientDescribeDbClustersResponseTypeDef(_ClientDescribeDbClustersResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of  DescribeDBClusters .
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_RequiredClientDescribeDbEngineVersionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbEngineVersionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbEngineVersionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbEngineVersionsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbEngineVersionsFiltersTypeDef(
    _RequiredClientDescribeDbEngineVersionsFiltersTypeDef,
    _OptionalClientDescribeDbEngineVersionsFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "Description": str,
        "AutoUpgrade": bool,
        "IsMajorVersionUpgrade": bool,
    },
    total=False,
)


class ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef(
    _ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef
):
    pass


_ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "ValidUpgradeTarget": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef
        ],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
    },
    total=False,
)


class ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef(
    _ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef
):
    pass


_ClientDescribeDbEngineVersionsResponseTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseTypeDef",
    {
        "Marker": str,
        "DBEngineVersions": List[ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef],
    },
    total=False,
)


class ClientDescribeDbEngineVersionsResponseTypeDef(_ClientDescribeDbEngineVersionsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of  DescribeDBEngineVersions .
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_RequiredClientDescribeDbInstancesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbInstancesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbInstancesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbInstancesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbInstancesFiltersTypeDef(
    _RequiredClientDescribeDbInstancesFiltersTypeDef,
    _OptionalClientDescribeDbInstancesFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef
):
    pass


_ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef
):
    pass


_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    pass


_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef
):
    pass


_ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef
):
    pass


_ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef
):
    pass


_ClientDescribeDbInstancesResponseDBInstancesTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[
            ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesTypeDef
):
    pass


_ClientDescribeDbInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseTypeDef",
    {"Marker": str, "DBInstances": List[ClientDescribeDbInstancesResponseDBInstancesTypeDef]},
    total=False,
)


class ClientDescribeDbInstancesResponseTypeDef(_ClientDescribeDbInstancesResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of  DescribeDBInstances .
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_RequiredClientDescribeDbSubnetGroupsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbSubnetGroupsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbSubnetGroupsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbSubnetGroupsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbSubnetGroupsFiltersTypeDef(
    _RequiredClientDescribeDbSubnetGroupsFiltersTypeDef,
    _OptionalClientDescribeDbSubnetGroupsFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef(
    _ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef
):
    pass


_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef(
    _ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef
):
    pass


_ClientDescribeDbSubnetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "DBSubnetGroups": List[ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef],
    },
    total=False,
)


class ClientDescribeDbSubnetGroupsResponseTypeDef(_ClientDescribeDbSubnetGroupsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of  DescribeDBSubnetGroups .
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_RequiredClientDescribeEngineDefaultClusterParametersFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEngineDefaultClusterParametersFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEngineDefaultClusterParametersFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEngineDefaultClusterParametersFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeEngineDefaultClusterParametersFiltersTypeDef(
    _RequiredClientDescribeEngineDefaultClusterParametersFiltersTypeDef,
    _OptionalClientDescribeEngineDefaultClusterParametersFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": Literal["immediate", "pending-reboot"],
    },
    total=False,
)


class ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef(
    _ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef
):
    pass


_ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef(
    _ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef
):
    """
    - **EngineDefaults** *(dict) --*

      Contains the result of a successful invocation of the
      ``DescribeEngineDefaultClusterParameters`` operation.
      - **DBParameterGroupFamily** *(string) --*

        The name of the DB cluster parameter group family to return the engine parameter information
        for.
    """


_ClientDescribeEngineDefaultClusterParametersResponseTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultClusterParametersResponseTypeDef",
    {"EngineDefaults": ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef},
    total=False,
)


class ClientDescribeEngineDefaultClusterParametersResponseTypeDef(
    _ClientDescribeEngineDefaultClusterParametersResponseTypeDef
):
    """
    - *(dict) --*

      - **EngineDefaults** *(dict) --*

        Contains the result of a successful invocation of the
        ``DescribeEngineDefaultClusterParameters`` operation.
        - **DBParameterGroupFamily** *(string) --*

          The name of the DB cluster parameter group family to return the engine parameter
          information for.
    """


_RequiredClientDescribeEventCategoriesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventCategoriesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEventCategoriesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventCategoriesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEventCategoriesFiltersTypeDef(
    _RequiredClientDescribeEventCategoriesFiltersTypeDef,
    _OptionalClientDescribeEventCategoriesFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    {"SourceType": str, "EventCategories": List[str]},
    total=False,
)


class ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef(
    _ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef
):
    """
    - *(dict) --*

      An event source type, accompanied by one or more event category names.
      - **SourceType** *(string) --*

        The source type that the returned categories belong to.
    """


_ClientDescribeEventCategoriesResponseTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesResponseTypeDef",
    {
        "EventCategoriesMapList": List[
            ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeEventCategoriesResponseTypeDef(_ClientDescribeEventCategoriesResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of  DescribeEventCategories .
      - **EventCategoriesMapList** *(list) --*

        A list of event category maps.
        - *(dict) --*

          An event source type, accompanied by one or more event category names.
          - **SourceType** *(string) --*

            The source type that the returned categories belong to.
    """


_RequiredClientDescribeEventsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEventsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEventsFiltersTypeDef(
    _RequiredClientDescribeEventsFiltersTypeDef, _OptionalClientDescribeEventsFiltersTypeDef
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ],
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
        "SourceArn": str,
    },
    total=False,
)


class ClientDescribeEventsResponseEventsTypeDef(_ClientDescribeEventsResponseEventsTypeDef):
    pass


_ClientDescribeEventsResponseTypeDef = TypedDict(
    "_ClientDescribeEventsResponseTypeDef",
    {"Marker": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)


class ClientDescribeEventsResponseTypeDef(_ClientDescribeEventsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of  DescribeEvents .
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_RequiredClientDescribeOrderableDbInstanceOptionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeOrderableDbInstanceOptionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeOrderableDbInstanceOptionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeOrderableDbInstanceOptionsFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef(
    _RequiredClientDescribeOrderableDbInstanceOptionsFiltersTypeDef,
    _OptionalClientDescribeOrderableDbInstanceOptionsFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef = TypedDict(
    "_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef
):
    pass


_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef = TypedDict(
    "_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZones": List[
            ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef
        ],
        "Vpc": bool,
    },
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef
):
    """
    - *(dict) --*

      The options that are available for a DB instance.
      - **Engine** *(string) --*

        The engine type of a DB instance.
    """


_ClientDescribeOrderableDbInstanceOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeOrderableDbInstanceOptionsResponseTypeDef",
    {
        "OrderableDBInstanceOptions": List[
            ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsResponseTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of  DescribeOrderableDBInstanceOptions .
      - **OrderableDBInstanceOptions** *(list) --*

        The options that are available for a particular orderable DB instance.
        - *(dict) --*

          The options that are available for a DB instance.
          - **Engine** *(string) --*

            The engine type of a DB instance.
    """


_RequiredClientDescribePendingMaintenanceActionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribePendingMaintenanceActionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribePendingMaintenanceActionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribePendingMaintenanceActionsFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribePendingMaintenanceActionsFiltersTypeDef(
    _RequiredClientDescribePendingMaintenanceActionsFiltersTypeDef,
    _OptionalClientDescribePendingMaintenanceActionsFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef(
    _ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
):
    pass


_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef(
    _ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef
):
    """
    - *(dict) --*

      Represents the output of  ApplyPendingMaintenanceAction .
      - **ResourceIdentifier** *(string) --*

        The Amazon Resource Name (ARN) of the resource that has pending maintenance actions.
    """


_ClientDescribePendingMaintenanceActionsResponseTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponseTypeDef",
    {
        "PendingMaintenanceActions": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponseTypeDef(
    _ClientDescribePendingMaintenanceActionsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of  DescribePendingMaintenanceActions .
      - **PendingMaintenanceActions** *(list) --*

        The maintenance actions to be applied.
        - *(dict) --*

          Represents the output of  ApplyPendingMaintenanceAction .
          - **ResourceIdentifier** *(string) --*

            The Amazon Resource Name (ARN) of the resource that has pending maintenance actions.
    """


_ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    pass


_ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    pass


_ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientFailoverDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterTypeDef(
    _ClientFailoverDbClusterResponseDBClusterTypeDef
):
    """
    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.
      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.
        - *(string) --*
    """


_ClientFailoverDbClusterResponseTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseTypeDef",
    {"DBCluster": ClientFailoverDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientFailoverDbClusterResponseTypeDef(_ClientFailoverDbClusterResponseTypeDef):
    """
    - *(dict) --*

      - **DBCluster** *(dict) --*

        Detailed information about a DB cluster.
        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
          created in.
          - *(string) --*
    """


_RequiredClientListTagsForResourceFiltersTypeDef = TypedDict(
    "_RequiredClientListTagsForResourceFiltersTypeDef", {"Name": str}
)
_OptionalClientListTagsForResourceFiltersTypeDef = TypedDict(
    "_OptionalClientListTagsForResourceFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientListTagsForResourceFiltersTypeDef(
    _RequiredClientListTagsForResourceFiltersTypeDef,
    _OptionalClientListTagsForResourceFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagListTypeDef(
    _ClientListTagsForResourceResponseTagListTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
      - **Key** *(string) --*

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
        Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of  ListTagsForResource .
      - **TagList** *(list) --*

        A list of one or more tags.
        - *(dict) --*

          Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
          - **Key** *(string) --*

            The required name of the tag. The string value can be from 1 to 128 Unicode characters
            in length and can't be prefixed with "aws:" or "rds:". The string can contain only the
            set of Unicode letters, digits, white space, '_', '.', '/', '=
                ', '+', '-' (Java regex:
            "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "_ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef",
    {"EnableLogTypes": List[str], "DisableLogTypes": List[str]},
    total=False,
)


class ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef(
    _ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef
):
    """
    The configuration setting for the log types to be enabled for export to Amazon CloudWatch Logs
    for a specific DB instance or DB cluster. The ``EnableLogTypes`` and ``DisableLogTypes`` arrays
    determine which logs are exported (or not exported) to CloudWatch Logs.
    - **EnableLogTypes** *(list) --*

      The list of log types to enable.
      - *(string) --*
    """


_ClientModifyDbClusterParameterGroupParametersTypeDef = TypedDict(
    "_ClientModifyDbClusterParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": Literal["immediate", "pending-reboot"],
    },
    total=False,
)


class ClientModifyDbClusterParameterGroupParametersTypeDef(
    _ClientModifyDbClusterParameterGroupParametersTypeDef
):
    """
    - *(dict) --*

      Detailed information about an individual parameter.
      - **ParameterName** *(string) --*

        Specifies the name of the parameter.
    """


_ClientModifyDbClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientModifyDbClusterParameterGroupResponseTypeDef",
    {"DBClusterParameterGroupName": str},
    total=False,
)


class ClientModifyDbClusterParameterGroupResponseTypeDef(
    _ClientModifyDbClusterParameterGroupResponseTypeDef
):
    """
    - *(dict) --*

      Contains the name of a DB cluster parameter group.
      - **DBClusterParameterGroupName** *(string) --*

        The name of a DB cluster parameter group.
        Constraints:
        * Must be from 1 to 255 letters or numbers.
        * The first character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
        .. note::

          This value is stored as a lowercase string.
    """


_ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    pass


_ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    pass


_ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientModifyDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientModifyDbClusterResponseDBClusterTypeDef(_ClientModifyDbClusterResponseDBClusterTypeDef):
    """
    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.
      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.
        - *(string) --*
    """


_ClientModifyDbClusterResponseTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseTypeDef",
    {"DBCluster": ClientModifyDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientModifyDbClusterResponseTypeDef(_ClientModifyDbClusterResponseTypeDef):
    """
    - *(dict) --*

      - **DBCluster** *(dict) --*

        Detailed information about a DB cluster.
        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
          created in.
          - *(string) --*
    """


_ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef = TypedDict(
    "_ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    {"AttributeName": str, "AttributeValues": List[str]},
    total=False,
)


class ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef(
    _ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
):
    pass


_ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "_ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterSnapshotAttributes": List[
            ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
        ],
    },
    total=False,
)


class ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef(
    _ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef
):
    """
    - **DBClusterSnapshotAttributesResult** *(dict) --*

      Detailed information about the attributes that are associated with a DB cluster snapshot.
      - **DBClusterSnapshotIdentifier** *(string) --*

        The identifier of the DB cluster snapshot that the attributes apply to.
    """


_ClientModifyDbClusterSnapshotAttributeResponseTypeDef = TypedDict(
    "_ClientModifyDbClusterSnapshotAttributeResponseTypeDef",
    {
        "DBClusterSnapshotAttributesResult": ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef
    },
    total=False,
)


class ClientModifyDbClusterSnapshotAttributeResponseTypeDef(
    _ClientModifyDbClusterSnapshotAttributeResponseTypeDef
):
    """
    - *(dict) --*

      - **DBClusterSnapshotAttributesResult** *(dict) --*

        Detailed information about the attributes that are associated with a DB cluster snapshot.
        - **DBClusterSnapshotIdentifier** *(string) --*

          The identifier of the DB cluster snapshot that the attributes apply to.
    """


_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    pass


_ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef
):
    pass


_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    pass


_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    pass


_ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientModifyDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Detailed information about a DB instance.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-provided database identifier. This identifier is the unique key that
        identifies a DB instance.
    """


_ClientModifyDbInstanceResponseTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseTypeDef",
    {"DBInstance": ClientModifyDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientModifyDbInstanceResponseTypeDef(_ClientModifyDbInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **DBInstance** *(dict) --*

        Detailed information about a DB instance.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-provided database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef(
    _ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef = TypedDict(
    "_ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef(
    _ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef
):
    """
    - **DBSubnetGroup** *(dict) --*

      Detailed information about a DB subnet group.
      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.
    """


_ClientModifyDbSubnetGroupResponseTypeDef = TypedDict(
    "_ClientModifyDbSubnetGroupResponseTypeDef",
    {"DBSubnetGroup": ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef},
    total=False,
)


class ClientModifyDbSubnetGroupResponseTypeDef(_ClientModifyDbSubnetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **DBSubnetGroup** *(dict) --*

        Detailed information about a DB subnet group.
        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.
    """


_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    pass


_ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef
):
    pass


_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    pass


_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    pass


_ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientRebootDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Detailed information about a DB instance.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-provided database identifier. This identifier is the unique key that
        identifies a DB instance.
    """


_ClientRebootDbInstanceResponseTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseTypeDef",
    {"DBInstance": ClientRebootDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientRebootDbInstanceResponseTypeDef(_ClientRebootDbInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **DBInstance** *(dict) --*

        Detailed information about a DB instance.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-provided database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientResetDbClusterParameterGroupParametersTypeDef = TypedDict(
    "_ClientResetDbClusterParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": Literal["immediate", "pending-reboot"],
    },
    total=False,
)


class ClientResetDbClusterParameterGroupParametersTypeDef(
    _ClientResetDbClusterParameterGroupParametersTypeDef
):
    """
    - *(dict) --*

      Detailed information about an individual parameter.
      - **ParameterName** *(string) --*

        Specifies the name of the parameter.
    """


_ClientResetDbClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientResetDbClusterParameterGroupResponseTypeDef",
    {"DBClusterParameterGroupName": str},
    total=False,
)


class ClientResetDbClusterParameterGroupResponseTypeDef(
    _ClientResetDbClusterParameterGroupResponseTypeDef
):
    """
    - *(dict) --*

      Contains the name of a DB cluster parameter group.
      - **DBClusterParameterGroupName** *(string) --*

        The name of a DB cluster parameter group.
        Constraints:
        * Must be from 1 to 255 letters or numbers.
        * The first character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
        .. note::

          This value is stored as a lowercase string.
    """


_ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef
):
    pass


_ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef
):
    pass


_ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef
):
    """
    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.
      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.
        - *(string) --*
    """


_ClientRestoreDbClusterFromSnapshotResponseTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseTypeDef",
    {"DBCluster": ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef},
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseTypeDef
):
    """
    - *(dict) --*

      - **DBCluster** *(dict) --*

        Detailed information about a DB cluster.
        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
          created in.
          - *(string) --*
    """


_ClientRestoreDbClusterFromSnapshotTagsTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRestoreDbClusterFromSnapshotTagsTypeDef(_ClientRestoreDbClusterFromSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
      - **Key** *(string) --*

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
        Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef
):
    pass


_ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef
):
    pass


_ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef
):
    """
    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.
      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.
        - *(string) --*
    """


_ClientRestoreDbClusterToPointInTimeResponseTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseTypeDef",
    {"DBCluster": ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef},
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseTypeDef
):
    """
    - *(dict) --*

      - **DBCluster** *(dict) --*

        Detailed information about a DB cluster.
        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
          created in.
          - *(string) --*
    """


_ClientRestoreDbClusterToPointInTimeTagsTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRestoreDbClusterToPointInTimeTagsTypeDef(
    _ClientRestoreDbClusterToPointInTimeTagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
      - **Key** *(string) --*

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
        Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    pass


_ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    pass


_ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientStartDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientStartDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientStartDbClusterResponseDBClusterTypeDef(_ClientStartDbClusterResponseDBClusterTypeDef):
    """
    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.
      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.
        - *(string) --*
    """


_ClientStartDbClusterResponseTypeDef = TypedDict(
    "_ClientStartDbClusterResponseTypeDef",
    {"DBCluster": ClientStartDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientStartDbClusterResponseTypeDef(_ClientStartDbClusterResponseTypeDef):
    """
    - *(dict) --*

      - **DBCluster** *(dict) --*

        Detailed information about a DB cluster.
        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
          created in.
          - *(string) --*
    """


_ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    pass


_ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    pass


_ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientStopDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientStopDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientStopDbClusterResponseDBClusterTypeDef(_ClientStopDbClusterResponseDBClusterTypeDef):
    """
    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.
      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.
        - *(string) --*
    """


_ClientStopDbClusterResponseTypeDef = TypedDict(
    "_ClientStopDbClusterResponseTypeDef",
    {"DBCluster": ClientStopDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientStopDbClusterResponseTypeDef(_ClientStopDbClusterResponseTypeDef):
    """
    - *(dict) --*

      - **DBCluster** *(dict) --*

        Detailed information about a DB cluster.
        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
          created in.
          - *(string) --*
    """


_RequiredDbInstanceAvailableWaitFiltersTypeDef = TypedDict(
    "_RequiredDbInstanceAvailableWaitFiltersTypeDef", {"Name": str}
)
_OptionalDbInstanceAvailableWaitFiltersTypeDef = TypedDict(
    "_OptionalDbInstanceAvailableWaitFiltersTypeDef", {"Values": List[str]}, total=False
)


class DbInstanceAvailableWaitFiltersTypeDef(
    _RequiredDbInstanceAvailableWaitFiltersTypeDef, _OptionalDbInstanceAvailableWaitFiltersTypeDef
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_DbInstanceAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_DbInstanceAvailableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class DbInstanceAvailableWaitWaiterConfigTypeDef(_DbInstanceAvailableWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_RequiredDbInstanceDeletedWaitFiltersTypeDef = TypedDict(
    "_RequiredDbInstanceDeletedWaitFiltersTypeDef", {"Name": str}
)
_OptionalDbInstanceDeletedWaitFiltersTypeDef = TypedDict(
    "_OptionalDbInstanceDeletedWaitFiltersTypeDef", {"Values": List[str]}, total=False
)


class DbInstanceDeletedWaitFiltersTypeDef(
    _RequiredDbInstanceDeletedWaitFiltersTypeDef, _OptionalDbInstanceDeletedWaitFiltersTypeDef
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_DbInstanceDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_DbInstanceDeletedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class DbInstanceDeletedWaitWaiterConfigTypeDef(_DbInstanceDeletedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_RequiredDescribeDBClustersPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeDBClustersPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeDBClustersPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeDBClustersPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeDBClustersPaginateFiltersTypeDef(
    _RequiredDescribeDBClustersPaginateFiltersTypeDef,
    _OptionalDescribeDBClustersPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_DescribeDBClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBClustersPaginatePaginationConfigTypeDef(
    _DescribeDBClustersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef
):
    pass


_DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef
):
    pass


_DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef
):
    pass


_DescribeDBClustersPaginateResponseDBClustersTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersTypeDef
):
    """
    - *(dict) --*

      Detailed information about a DB cluster.
      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.
        - *(string) --*
    """


_DescribeDBClustersPaginateResponseTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseTypeDef",
    {"DBClusters": List[DescribeDBClustersPaginateResponseDBClustersTypeDef], "NextToken": str},
    total=False,
)


class DescribeDBClustersPaginateResponseTypeDef(_DescribeDBClustersPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of  DescribeDBClusters .
      - **DBClusters** *(list) --*

        A list of DB clusters.
        - *(dict) --*

          Detailed information about a DB cluster.
          - **AvailabilityZones** *(list) --*

            Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can
            be created in.
            - *(string) --*
    """


_RequiredDescribeDBEngineVersionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeDBEngineVersionsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeDBEngineVersionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeDBEngineVersionsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeDBEngineVersionsPaginateFiltersTypeDef(
    _RequiredDescribeDBEngineVersionsPaginateFiltersTypeDef,
    _OptionalDescribeDBEngineVersionsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_DescribeDBEngineVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBEngineVersionsPaginatePaginationConfigTypeDef(
    _DescribeDBEngineVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "Description": str,
        "AutoUpgrade": bool,
        "IsMajorVersionUpgrade": bool,
    },
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef
):
    pass


_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "ValidUpgradeTarget": List[
            DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef
        ],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
    },
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef
):
    """
    - *(dict) --*

      Detailed information about a DB engine version.
      - **Engine** *(string) --*

        The name of the database engine.
    """


_DescribeDBEngineVersionsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseTypeDef",
    {
        "DBEngineVersions": List[DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseTypeDef(
    _DescribeDBEngineVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of  DescribeDBEngineVersions .
      - **DBEngineVersions** *(list) --*

        Detailed information about one or more DB engine versions.
        - *(dict) --*

          Detailed information about a DB engine version.
          - **Engine** *(string) --*

            The name of the database engine.
    """


_RequiredDescribeDBInstancesPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeDBInstancesPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeDBInstancesPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeDBInstancesPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeDBInstancesPaginateFiltersTypeDef(
    _RequiredDescribeDBInstancesPaginateFiltersTypeDef,
    _OptionalDescribeDBInstancesPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_DescribeDBInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBInstancesPaginatePaginationConfigTypeDef(
    _DescribeDBInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef
):
    pass


_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef
):
    pass


_DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef
):
    pass


_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    pass


_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef
):
    pass


_DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef
):
    pass


_DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef
):
    pass


_DescribeDBInstancesPaginateResponseDBInstancesTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[
            DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesTypeDef
):
    """
    - *(dict) --*

      Detailed information about a DB instance.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-provided database identifier. This identifier is the unique key that
        identifies a DB instance.
    """


_DescribeDBInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseTypeDef",
    {"DBInstances": List[DescribeDBInstancesPaginateResponseDBInstancesTypeDef], "NextToken": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseTypeDef(_DescribeDBInstancesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of  DescribeDBInstances .
      - **DBInstances** *(list) --*

        Detailed information about one or more DB instances.
        - *(dict) --*

          Detailed information about a DB instance.
          - **DBInstanceIdentifier** *(string) --*

            Contains a user-provided database identifier. This identifier is the unique key that
            identifies a DB instance.
    """


_RequiredDescribeDBSubnetGroupsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeDBSubnetGroupsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeDBSubnetGroupsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeDBSubnetGroupsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeDBSubnetGroupsPaginateFiltersTypeDef(
    _RequiredDescribeDBSubnetGroupsPaginateFiltersTypeDef,
    _OptionalDescribeDBSubnetGroupsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef(
    _DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef(
    _DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef
):
    pass


_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef(
    _DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef
):
    """
    - *(dict) --*

      Detailed information about a DB subnet group.
      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.
    """


_DescribeDBSubnetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateResponseTypeDef",
    {
        "DBSubnetGroups": List[DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBSubnetGroupsPaginateResponseTypeDef(_DescribeDBSubnetGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of  DescribeDBSubnetGroups .
      - **DBSubnetGroups** *(list) --*

        Detailed information about one or more DB subnet groups.
        - *(dict) --*

          Detailed information about a DB subnet group.
          - **DBSubnetGroupName** *(string) --*

            The name of the DB subnet group.
    """


_RequiredDescribeEventsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeEventsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeEventsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeEventsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeEventsPaginateFiltersTypeDef(
    _RequiredDescribeEventsPaginateFiltersTypeDef, _OptionalDescribeEventsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventsPaginatePaginationConfigTypeDef(_DescribeEventsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEventsPaginateResponseEventsTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ],
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
        "SourceArn": str,
    },
    total=False,
)


class DescribeEventsPaginateResponseEventsTypeDef(_DescribeEventsPaginateResponseEventsTypeDef):
    """
    - *(dict) --*

      Detailed information about an event.
      - **SourceIdentifier** *(string) --*

        Provides the identifier for the source of the event.
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"Events": List[DescribeEventsPaginateResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of  DescribeEvents .
      - **Events** *(list) --*

        Detailed information about one or more events.
        - *(dict) --*

          Detailed information about an event.
          - **SourceIdentifier** *(string) --*

            Provides the identifier for the source of the event.
    """


_RequiredDescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef(
    _RequiredDescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef,
    _OptionalDescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      A named set of filter values, used to return a more specific list of results. You can use a
      filter to match a set of resources by specific criteria, such as IDs.
      Wildcards are not supported in filters.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case sensitive.
    """


_DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef
):
    pass


_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZones": List[
            DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef
        ],
        "Vpc": bool,
    },
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef
):
    """
    - *(dict) --*

      The options that are available for a DB instance.
      - **Engine** *(string) --*

        The engine type of a DB instance.
    """


_DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef",
    {
        "OrderableDBInstanceOptions": List[
            DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of  DescribeOrderableDBInstanceOptions .
      - **OrderableDBInstanceOptions** *(list) --*

        The options that are available for a particular orderable DB instance.
        - *(dict) --*

          The options that are available for a DB instance.
          - **Engine** *(string) --*

            The engine type of a DB instance.
    """
