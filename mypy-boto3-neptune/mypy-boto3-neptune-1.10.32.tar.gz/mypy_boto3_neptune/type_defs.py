"Main interface for neptune service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef",
    "ClientAddSourceIdentifierToSubscriptionResponseTypeDef",
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
    "ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef",
    "ClientCopyDbParameterGroupResponseTypeDef",
    "ClientCopyDbParameterGroupTagsTypeDef",
    "ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCreateDbClusterParameterGroupResponseTypeDef",
    "ClientCreateDbClusterParameterGroupTagsTypeDef",
    "ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientCreateDbClusterResponseDBClusterTypeDef",
    "ClientCreateDbClusterResponseTypeDef",
    "ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCreateDbClusterSnapshotResponseTypeDef",
    "ClientCreateDbClusterSnapshotTagsTypeDef",
    "ClientCreateDbClusterTagsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceTypeDef",
    "ClientCreateDbInstanceResponseTypeDef",
    "ClientCreateDbInstanceTagsTypeDef",
    "ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef",
    "ClientCreateDbParameterGroupResponseTypeDef",
    "ClientCreateDbParameterGroupTagsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientCreateDbSubnetGroupResponseTypeDef",
    "ClientCreateDbSubnetGroupTagsTypeDef",
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientCreateEventSubscriptionResponseTypeDef",
    "ClientCreateEventSubscriptionTagsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterTypeDef",
    "ClientDeleteDbClusterResponseTypeDef",
    "ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientDeleteDbClusterSnapshotResponseTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceTypeDef",
    "ClientDeleteDbInstanceResponseTypeDef",
    "ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientDeleteEventSubscriptionResponseTypeDef",
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
    "ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef",
    "ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef",
    "ClientDescribeDbClustersResponseDBClustersTypeDef",
    "ClientDescribeDbClustersResponseTypeDef",
    "ClientDescribeDbEngineVersionsFiltersTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef",
    "ClientDescribeDbEngineVersionsResponseTypeDef",
    "ClientDescribeDbInstancesFiltersTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesTypeDef",
    "ClientDescribeDbInstancesResponseTypeDef",
    "ClientDescribeDbParameterGroupsFiltersTypeDef",
    "ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef",
    "ClientDescribeDbParameterGroupsResponseTypeDef",
    "ClientDescribeDbParametersFiltersTypeDef",
    "ClientDescribeDbParametersResponseParametersTypeDef",
    "ClientDescribeDbParametersResponseTypeDef",
    "ClientDescribeDbSubnetGroupsFiltersTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef",
    "ClientDescribeDbSubnetGroupsResponseTypeDef",
    "ClientDescribeEngineDefaultClusterParametersFiltersTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseTypeDef",
    "ClientDescribeEngineDefaultParametersFiltersTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef",
    "ClientDescribeEngineDefaultParametersResponseTypeDef",
    "ClientDescribeEventCategoriesFiltersTypeDef",
    "ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    "ClientDescribeEventCategoriesResponseTypeDef",
    "ClientDescribeEventSubscriptionsFiltersTypeDef",
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    "ClientDescribeEventSubscriptionsResponseTypeDef",
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
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseTypeDef",
    "ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
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
    "ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientModifyDbClusterResponseDBClusterTypeDef",
    "ClientModifyDbClusterResponseTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseTypeDef",
    "ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceTypeDef",
    "ClientModifyDbInstanceResponseTypeDef",
    "ClientModifyDbParameterGroupParametersTypeDef",
    "ClientModifyDbParameterGroupResponseTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientModifyDbSubnetGroupResponseTypeDef",
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientModifyEventSubscriptionResponseTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceTypeDef",
    "ClientRebootDbInstanceResponseTypeDef",
    "ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef",
    "ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef",
    "ClientResetDbClusterParameterGroupParametersTypeDef",
    "ClientResetDbClusterParameterGroupResponseTypeDef",
    "ClientResetDbParameterGroupParametersTypeDef",
    "ClientResetDbParameterGroupResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotTagsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseTypeDef",
    "ClientRestoreDbClusterToPointInTimeTagsTypeDef",
    "DbInstanceAvailableWaitFiltersTypeDef",
    "DbInstanceAvailableWaitWaiterConfigTypeDef",
    "DbInstanceDeletedWaitFiltersTypeDef",
    "DbInstanceDeletedWaitWaiterConfigTypeDef",
    "DescribeDBClusterParameterGroupsPaginateFiltersTypeDef",
    "DescribeDBClusterParameterGroupsPaginatePaginationConfigTypeDef",
    "DescribeDBClusterParameterGroupsPaginateResponseDBClusterParameterGroupsTypeDef",
    "DescribeDBClusterParameterGroupsPaginateResponseTypeDef",
    "DescribeDBClusterParametersPaginateFiltersTypeDef",
    "DescribeDBClusterParametersPaginatePaginationConfigTypeDef",
    "DescribeDBClusterParametersPaginateResponseParametersTypeDef",
    "DescribeDBClusterParametersPaginateResponseTypeDef",
    "DescribeDBClusterSnapshotsPaginateFiltersTypeDef",
    "DescribeDBClusterSnapshotsPaginatePaginationConfigTypeDef",
    "DescribeDBClusterSnapshotsPaginateResponseDBClusterSnapshotsTypeDef",
    "DescribeDBClusterSnapshotsPaginateResponseTypeDef",
    "DescribeDBClustersPaginateFiltersTypeDef",
    "DescribeDBClustersPaginatePaginationConfigTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersDBClusterOptionGroupMembershipsTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersTypeDef",
    "DescribeDBClustersPaginateResponseTypeDef",
    "DescribeDBEngineVersionsPaginateFiltersTypeDef",
    "DescribeDBEngineVersionsPaginatePaginationConfigTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsDefaultCharacterSetTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedCharacterSetsTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedTimezonesTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef",
    "DescribeDBEngineVersionsPaginateResponseTypeDef",
    "DescribeDBInstancesPaginateFiltersTypeDef",
    "DescribeDBInstancesPaginatePaginationConfigTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBParameterGroupsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSecurityGroupsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDomainMembershipsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesOptionGroupMembershipsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesTypeDef",
    "DescribeDBInstancesPaginateResponseTypeDef",
    "DescribeDBParameterGroupsPaginateFiltersTypeDef",
    "DescribeDBParameterGroupsPaginatePaginationConfigTypeDef",
    "DescribeDBParameterGroupsPaginateResponseDBParameterGroupsTypeDef",
    "DescribeDBParameterGroupsPaginateResponseTypeDef",
    "DescribeDBParametersPaginateFiltersTypeDef",
    "DescribeDBParametersPaginatePaginationConfigTypeDef",
    "DescribeDBParametersPaginateResponseParametersTypeDef",
    "DescribeDBParametersPaginateResponseTypeDef",
    "DescribeDBSubnetGroupsPaginateFiltersTypeDef",
    "DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseTypeDef",
    "DescribeEngineDefaultParametersPaginateFiltersTypeDef",
    "DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseTypeDef",
    "DescribeEventSubscriptionsPaginateFiltersTypeDef",
    "DescribeEventSubscriptionsPaginatePaginationConfigTypeDef",
    "DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef",
    "DescribeEventSubscriptionsPaginateResponseTypeDef",
    "DescribeEventsPaginateFiltersTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef",
    "DescribePendingMaintenanceActionsPaginateFiltersTypeDef",
    "DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef",
    "DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsTypeDef",
    "DescribePendingMaintenanceActionsPaginateResponseTypeDef",
)


_ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef(
    _ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef
):
    """
    - **EventSubscription** *(dict) --*

      Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the event notification subscription.
    """


_ClientAddSourceIdentifierToSubscriptionResponseTypeDef = TypedDict(
    "_ClientAddSourceIdentifierToSubscriptionResponseTypeDef",
    {"EventSubscription": ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)


class ClientAddSourceIdentifierToSubscriptionResponseTypeDef(
    _ClientAddSourceIdentifierToSubscriptionResponseTypeDef
):
    """
    - *(dict) --*

      - **EventSubscription** *(dict) --*

        Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the event notification subscription.
    """


_ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsToResourceTagsTypeDef(_ClientAddTagsToResourceTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
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

      Describes the pending maintenance actions for a resource.
      - **ResourceIdentifier** *(string) --*

        The ARN of the resource that has pending maintenance actions.
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

        Describes the pending maintenance actions for a resource.
        - **ResourceIdentifier** *(string) --*

          The ARN of the resource that has pending maintenance actions.
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

      Contains the details of an Amazon Neptune DB cluster parameter group.
      This data type is used as a response element in the  DescribeDBClusterParameterGroups action.
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

        Contains the details of an Amazon Neptune DB cluster parameter group.
        This data type is used as a response element in the  DescribeDBClusterParameterGroups
        action.
        - **DBClusterParameterGroupName** *(string) --*

          Provides the name of the DB cluster parameter group.
    """


_ClientCopyDbClusterParameterGroupTagsTypeDef = TypedDict(
    "_ClientCopyDbClusterParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCopyDbClusterParameterGroupTagsTypeDef(_ClientCopyDbClusterParameterGroupTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "_ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)


class ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef(
    _ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef
):
    """
    - **DBClusterSnapshot** *(dict) --*

      Contains the details for an Amazon Neptune DB cluster snapshot
      This data type is used as a response element in the  DescribeDBClusterSnapshots action.
      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can be
        restored in.
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

        Contains the details for an Amazon Neptune DB cluster snapshot
        This data type is used as a response element in the  DescribeDBClusterSnapshots action.
        - **AvailabilityZones** *(list) --*

          Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can
          be restored in.
          - *(string) --*
    """


_ClientCopyDbClusterSnapshotTagsTypeDef = TypedDict(
    "_ClientCopyDbClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCopyDbClusterSnapshotTagsTypeDef(_ClientCopyDbClusterSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef = TypedDict(
    "_ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)


class ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef(
    _ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef
):
    """
    - **DBParameterGroup** *(dict) --*

      Contains the details of an Amazon Neptune DB parameter group.
      This data type is used as a response element in the  DescribeDBParameterGroups action.
      - **DBParameterGroupName** *(string) --*

        Provides the name of the DB parameter group.
    """


_ClientCopyDbParameterGroupResponseTypeDef = TypedDict(
    "_ClientCopyDbParameterGroupResponseTypeDef",
    {"DBParameterGroup": ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef},
    total=False,
)


class ClientCopyDbParameterGroupResponseTypeDef(_ClientCopyDbParameterGroupResponseTypeDef):
    """
    - *(dict) --*

      - **DBParameterGroup** *(dict) --*

        Contains the details of an Amazon Neptune DB parameter group.
        This data type is used as a response element in the  DescribeDBParameterGroups action.
        - **DBParameterGroupName** *(string) --*

          Provides the name of the DB parameter group.
    """


_ClientCopyDbParameterGroupTagsTypeDef = TypedDict(
    "_ClientCopyDbParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCopyDbParameterGroupTagsTypeDef(_ClientCopyDbParameterGroupTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
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

      Contains the details of an Amazon Neptune DB cluster parameter group.
      This data type is used as a response element in the  DescribeDBClusterParameterGroups action.
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

        Contains the details of an Amazon Neptune DB cluster parameter group.
        This data type is used as a response element in the  DescribeDBClusterParameterGroups
        action.
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

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
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


_ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientCreateDbClusterResponseDBClusterTypeDef(_ClientCreateDbClusterResponseDBClusterTypeDef):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.
      This data type is used as a response element in the  DescribeDBClusters action.
      - **AllocatedStorage** *(integer) --*

        ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not fixed,
        but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Neptune DB cluster.
        This data type is used as a response element in the  DescribeDBClusters action.
        - **AllocatedStorage** *(integer) --*

          ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
          fixed, but instead automatically adjusts as needed.
    """


_ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "_ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)


class ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef(
    _ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef
):
    """
    - **DBClusterSnapshot** *(dict) --*

      Contains the details for an Amazon Neptune DB cluster snapshot
      This data type is used as a response element in the  DescribeDBClusterSnapshots action.
      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can be
        restored in.
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

        Contains the details for an Amazon Neptune DB cluster snapshot
        This data type is used as a response element in the  DescribeDBClusterSnapshots action.
        - **AvailabilityZones** *(list) --*

          Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can
          be restored in.
          - *(string) --*
    """


_ClientCreateDbClusterSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateDbClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbClusterSnapshotTagsTypeDef(_ClientCreateDbClusterSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbClusterTagsTypeDef = TypedDict(
    "_ClientCreateDbClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbClusterTagsTypeDef(_ClientCreateDbClusterTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
):
    pass


_ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
):
    pass


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


_ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef
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


_ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
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
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "DBParameterGroups": List[ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon Neptune DB instance.
      This data type is used as a response element in the  DescribeDBInstances action.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
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

        Contains the details of an Amazon Neptune DB instance.
        This data type is used as a response element in the  DescribeDBInstances action.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientCreateDbInstanceTagsTypeDef = TypedDict(
    "_ClientCreateDbInstanceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbInstanceTagsTypeDef(_ClientCreateDbInstanceTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef = TypedDict(
    "_ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)


class ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef(
    _ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef
):
    """
    - **DBParameterGroup** *(dict) --*

      Contains the details of an Amazon Neptune DB parameter group.
      This data type is used as a response element in the  DescribeDBParameterGroups action.
      - **DBParameterGroupName** *(string) --*

        Provides the name of the DB parameter group.
    """


_ClientCreateDbParameterGroupResponseTypeDef = TypedDict(
    "_ClientCreateDbParameterGroupResponseTypeDef",
    {"DBParameterGroup": ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef},
    total=False,
)


class ClientCreateDbParameterGroupResponseTypeDef(_ClientCreateDbParameterGroupResponseTypeDef):
    """
    - *(dict) --*

      - **DBParameterGroup** *(dict) --*

        Contains the details of an Amazon Neptune DB parameter group.
        This data type is used as a response element in the  DescribeDBParameterGroups action.
        - **DBParameterGroupName** *(string) --*

          Provides the name of the DB parameter group.
    """


_ClientCreateDbParameterGroupTagsTypeDef = TypedDict(
    "_ClientCreateDbParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbParameterGroupTagsTypeDef(_ClientCreateDbParameterGroupTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
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

      Contains the details of an Amazon Neptune DB subnet group.
      This data type is used as a response element in the  DescribeDBSubnetGroups action.
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

        Contains the details of an Amazon Neptune DB subnet group.
        This data type is used as a response element in the  DescribeDBSubnetGroups action.
        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.
    """


_ClientCreateDbSubnetGroupTagsTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbSubnetGroupTagsTypeDef(_ClientCreateDbSubnetGroupTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    - **EventSubscription** *(dict) --*

      Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the event notification subscription.
    """


_ClientCreateEventSubscriptionResponseTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)


class ClientCreateEventSubscriptionResponseTypeDef(_ClientCreateEventSubscriptionResponseTypeDef):
    """
    - *(dict) --*

      - **EventSubscription** *(dict) --*

        Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the event notification subscription.
    """


_ClientCreateEventSubscriptionTagsTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateEventSubscriptionTagsTypeDef(_ClientCreateEventSubscriptionTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
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


_ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterTypeDef(_ClientDeleteDbClusterResponseDBClusterTypeDef):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.
      This data type is used as a response element in the  DescribeDBClusters action.
      - **AllocatedStorage** *(integer) --*

        ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not fixed,
        but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Neptune DB cluster.
        This data type is used as a response element in the  DescribeDBClusters action.
        - **AllocatedStorage** *(integer) --*

          ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
          fixed, but instead automatically adjusts as needed.
    """


_ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "_ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)


class ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef(
    _ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef
):
    """
    - **DBClusterSnapshot** *(dict) --*

      Contains the details for an Amazon Neptune DB cluster snapshot
      This data type is used as a response element in the  DescribeDBClusterSnapshots action.
      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can be
        restored in.
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

        Contains the details for an Amazon Neptune DB cluster snapshot
        This data type is used as a response element in the  DescribeDBClusterSnapshots action.
        - **AvailabilityZones** *(list) --*

          Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can
          be restored in.
          - *(string) --*
    """


_ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
):
    pass


_ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
):
    pass


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


_ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef
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


_ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
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
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "DBParameterGroups": List[ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon Neptune DB instance.
      This data type is used as a response element in the  DescribeDBInstances action.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
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

        Contains the details of an Amazon Neptune DB instance.
        This data type is used as a response element in the  DescribeDBInstances action.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    - **EventSubscription** *(dict) --*

      Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the event notification subscription.
    """


_ClientDeleteEventSubscriptionResponseTypeDef = TypedDict(
    "_ClientDeleteEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)


class ClientDeleteEventSubscriptionResponseTypeDef(_ClientDeleteEventSubscriptionResponseTypeDef):
    """
    - *(dict) --*

      - **EventSubscription** *(dict) --*

        Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the event notification subscription.
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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

      - **Marker** *(string) --*

        An optional pagination token provided by a previous ``DescribeDBClusterParameterGroups``
        request. If this parameter is specified, the response includes only records beyond the
        marker, up to the value specified by ``MaxRecords`` .
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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

      Specifies a parameter.
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

      - **Parameters** *(list) --*

        Provides a list of parameters for the DB cluster parameter group.
        - *(dict) --*

          Specifies a parameter.
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

      Contains the results of a successful call to the  DescribeDBClusterSnapshotAttributes API
      action.
      Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or
      restore a manual DB cluster snapshot. For more information, see the
      ModifyDBClusterSnapshotAttribute API action.
      - **DBClusterSnapshotIdentifier** *(string) --*

        The identifier of the manual DB cluster snapshot that the attributes apply to.
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

        Contains the results of a successful call to the  DescribeDBClusterSnapshotAttributes API
        action.
        Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or
        restore a manual DB cluster snapshot. For more information, see the
        ModifyDBClusterSnapshotAttribute API action.
        - **DBClusterSnapshotIdentifier** *(string) --*

          The identifier of the manual DB cluster snapshot that the attributes apply to.
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
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

      - **Marker** *(string) --*

        An optional pagination token provided by a previous  DescribeDBClusterSnapshots request. If
        this parameter is specified, the response includes only records beyond the marker, up to the
        value specified by ``MaxRecords`` .
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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


_ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef(
    _ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
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
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
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

      - **Marker** *(string) --*

        A pagination token that can be used in a subsequent DescribeDBClusters request.
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef",
    {"CharacterSetName": str, "CharacterSetDescription": str},
    total=False,
)


class ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef(
    _ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef
):
    pass


_ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef",
    {"CharacterSetName": str, "CharacterSetDescription": str},
    total=False,
)


class ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef(
    _ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef
):
    pass


_ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef",
    {"TimezoneName": str},
    total=False,
)


class ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef(
    _ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef
):
    pass


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
        "DefaultCharacterSet": ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef,
        "SupportedCharacterSets": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef
        ],
        "ValidUpgradeTarget": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef
        ],
        "SupportedTimezones": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef
        ],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
        "SupportsReadReplica": bool,
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef
):
    pass


_ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef
):
    pass


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


_ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef
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


_ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef
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
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef
        ],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
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

      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_RequiredClientDescribeDbParameterGroupsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbParameterGroupsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbParameterGroupsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbParameterGroupsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbParameterGroupsFiltersTypeDef(
    _RequiredClientDescribeDbParameterGroupsFiltersTypeDef,
    _OptionalClientDescribeDbParameterGroupsFiltersTypeDef,
):
    """
    - *(dict) --*

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef = TypedDict(
    "_ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)


class ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef(
    _ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef
):
    pass


_ClientDescribeDbParameterGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeDbParameterGroupsResponseTypeDef",
    {
        "Marker": str,
        "DBParameterGroups": List[ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef],
    },
    total=False,
)


class ClientDescribeDbParameterGroupsResponseTypeDef(
    _ClientDescribeDbParameterGroupsResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_RequiredClientDescribeDbParametersFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbParametersFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbParametersFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbParametersFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbParametersFiltersTypeDef(
    _RequiredClientDescribeDbParametersFiltersTypeDef,
    _OptionalClientDescribeDbParametersFiltersTypeDef,
):
    """
    - *(dict) --*

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_ClientDescribeDbParametersResponseParametersTypeDef = TypedDict(
    "_ClientDescribeDbParametersResponseParametersTypeDef",
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


class ClientDescribeDbParametersResponseParametersTypeDef(
    _ClientDescribeDbParametersResponseParametersTypeDef
):
    """
    - *(dict) --*

      Specifies a parameter.
      - **ParameterName** *(string) --*

        Specifies the name of the parameter.
    """


_ClientDescribeDbParametersResponseTypeDef = TypedDict(
    "_ClientDescribeDbParametersResponseTypeDef",
    {"Parameters": List[ClientDescribeDbParametersResponseParametersTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeDbParametersResponseTypeDef(_ClientDescribeDbParametersResponseTypeDef):
    """
    - *(dict) --*

      - **Parameters** *(list) --*

        A list of  Parameter values.
        - *(dict) --*

          Specifies a parameter.
          - **ParameterName** *(string) --*

            Specifies the name of the parameter.
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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

      Contains the result of a successful invocation of the  DescribeEngineDefaultParameters action.
      - **DBParameterGroupFamily** *(string) --*

        Specifies the name of the DB parameter group family that the engine default parameters apply
        to.
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

        Contains the result of a successful invocation of the  DescribeEngineDefaultParameters
        action.
        - **DBParameterGroupFamily** *(string) --*

          Specifies the name of the DB parameter group family that the engine default parameters
          apply to.
    """


_RequiredClientDescribeEngineDefaultParametersFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEngineDefaultParametersFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEngineDefaultParametersFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEngineDefaultParametersFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeEngineDefaultParametersFiltersTypeDef(
    _RequiredClientDescribeEngineDefaultParametersFiltersTypeDef,
    _OptionalClientDescribeEngineDefaultParametersFiltersTypeDef,
):
    """
    - *(dict) --*

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef",
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


class ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef(
    _ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef
):
    pass


_ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef(
    _ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef
):
    """
    - **EngineDefaults** *(dict) --*

      Contains the result of a successful invocation of the  DescribeEngineDefaultParameters action.
      - **DBParameterGroupFamily** *(string) --*

        Specifies the name of the DB parameter group family that the engine default parameters apply
        to.
    """


_ClientDescribeEngineDefaultParametersResponseTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersResponseTypeDef",
    {"EngineDefaults": ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef},
    total=False,
)


class ClientDescribeEngineDefaultParametersResponseTypeDef(
    _ClientDescribeEngineDefaultParametersResponseTypeDef
):
    """
    - *(dict) --*

      - **EngineDefaults** *(dict) --*

        Contains the result of a successful invocation of the  DescribeEngineDefaultParameters
        action.
        - **DBParameterGroupFamily** *(string) --*

          Specifies the name of the DB parameter group family that the engine default parameters
          apply to.
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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

      Contains the results of a successful invocation of the  DescribeEventCategories action.
      - **SourceType** *(string) --*

        The source type that the returned categories belong to
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

      - **EventCategoriesMapList** *(list) --*

        A list of EventCategoriesMap data types.
        - *(dict) --*

          Contains the results of a successful invocation of the  DescribeEventCategories action.
          - **SourceType** *(string) --*

            The source type that the returned categories belong to
    """


_RequiredClientDescribeEventSubscriptionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventSubscriptionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEventSubscriptionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventSubscriptionsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEventSubscriptionsFiltersTypeDef(
    _RequiredClientDescribeEventSubscriptionsFiltersTypeDef,
    _OptionalClientDescribeEventSubscriptionsFiltersTypeDef,
):
    """
    - *(dict) --*

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef = TypedDict(
    "_ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef(
    _ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef
):
    pass


_ClientDescribeEventSubscriptionsResponseTypeDef = TypedDict(
    "_ClientDescribeEventSubscriptionsResponseTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List[
            ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEventSubscriptionsResponseTypeDef(
    _ClientDescribeEventSubscriptionsResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions
        request. If this parameter is specified, the response includes only records beyond the
        marker, up to the value specified by ``MaxRecords`` .
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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

      - **Marker** *(string) --*

        An optional pagination token provided by a previous Events request. If this parameter is
        specified, the response includes only records beyond the marker, up to the value specified
        by ``MaxRecords`` .
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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
        "MultiAZCapable": bool,
        "ReadReplicaCapable": bool,
        "Vpc": bool,
        "SupportsStorageEncryption": bool,
        "StorageType": str,
        "SupportsIops": bool,
        "SupportsEnhancedMonitoring": bool,
        "SupportsIAMDatabaseAuthentication": bool,
        "SupportsPerformanceInsights": bool,
        "MinStorageSize": int,
        "MaxStorageSize": int,
        "MinIopsPerDbInstance": int,
        "MaxIopsPerDbInstance": int,
        "MinIopsPerGib": float,
        "MaxIopsPerGib": float,
    },
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef
):
    """
    - *(dict) --*

      Contains a list of available options for a DB instance.
      This data type is used as a response element in the  DescribeOrderableDBInstanceOptions
      action.
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

      - **OrderableDBInstanceOptions** *(list) --*

        An  OrderableDBInstanceOption structure containing information about orderable options for
        the DB instance.
        - *(dict) --*

          Contains a list of available options for a DB instance.
          This data type is used as a response element in the  DescribeOrderableDBInstanceOptions
          action.
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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

      Describes the pending maintenance actions for a resource.
      - **ResourceIdentifier** *(string) --*

        The ARN of the resource that has pending maintenance actions.
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

      - **PendingMaintenanceActions** *(list) --*

        A list of the pending maintenance actions for the resource.
        - *(dict) --*

          Describes the pending maintenance actions for a resource.
          - **ResourceIdentifier** *(string) --*

            The ARN of the resource that has pending maintenance actions.
    """


_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef",
    {"From": float, "To": float},
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef
):
    pass


_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef",
    {"From": int, "To": int, "Step": int},
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef
):
    pass


_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef",
    {"From": int, "To": int, "Step": int},
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef
):
    pass


_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef",
    {
        "StorageType": str,
        "StorageSize": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef
        ],
        "ProvisionedIops": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef
        ],
        "IopsToStorageRatio": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef
        ],
    },
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef
):
    """
    - *(dict) --*

      Information about valid modifications that you can make to your DB instance.
      Contains the result of a successful call to the  DescribeValidDBInstanceModifications action.
      - **StorageType** *(string) --*

        The valid storage types for your DB instance. For example, gp2, io1.
    """


_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef",
    {
        "Storage": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef
        ]
    },
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef
):
    """
    - **ValidDBInstanceModificationsMessage** *(dict) --*

      Information about valid modifications that you can make to your DB instance. Contains the
      result of a successful call to the  DescribeValidDBInstanceModifications action. You can use
      this information when you call  ModifyDBInstance .
      - **Storage** *(list) --*

        Valid storage options for your DB instance.
        - *(dict) --*

          Information about valid modifications that you can make to your DB instance.
          Contains the result of a successful call to the  DescribeValidDBInstanceModifications
          action.
          - **StorageType** *(string) --*

            The valid storage types for your DB instance. For example, gp2, io1.
    """


_ClientDescribeValidDbInstanceModificationsResponseTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseTypeDef",
    {
        "ValidDBInstanceModificationsMessage": ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef
    },
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseTypeDef
):
    """
    - *(dict) --*

      - **ValidDBInstanceModificationsMessage** *(dict) --*

        Information about valid modifications that you can make to your DB instance. Contains the
        result of a successful call to the  DescribeValidDBInstanceModifications action. You can use
        this information when you call  ModifyDBInstance .
        - **Storage** *(list) --*

          Valid storage options for your DB instance.
          - *(dict) --*

            Information about valid modifications that you can make to your DB instance.
            Contains the result of a successful call to the  DescribeValidDBInstanceModifications
            action.
            - **StorageType** *(string) --*

              The valid storage types for your DB instance. For example, gp2, io1.
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


_ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterTypeDef(
    _ClientFailoverDbClusterResponseDBClusterTypeDef
):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.
      This data type is used as a response element in the  DescribeDBClusters action.
      - **AllocatedStorage** *(integer) --*

        ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not fixed,
        but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Neptune DB cluster.
        This data type is used as a response element in the  DescribeDBClusters action.
        - **AllocatedStorage** *(integer) --*

          ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
          fixed, but instead automatically adjusts as needed.
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagListTypeDef(
    _ClientListTagsForResourceResponseTagListTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **TagList** *(list) --*

        List of tags returned by the ListTagsForResource operation.
        - *(dict) --*

          Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
          - **Key** *(string) --*

            A key is the required name of the tag. The string value can be from 1 to 128 Unicode
            characters in length and can't be prefixed with "aws:" or "rds:". The string can only
            contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
                ', '+',
            '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
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
    The configuration setting for the log types to be enabled for export to CloudWatch Logs for a
    specific DB cluster.
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

      Specifies a parameter.
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

      - **DBClusterParameterGroupName** *(string) --*

        The name of the DB cluster parameter group.
        Constraints:
        * Must be 1 to 255 letters or numbers.
        * First character must be a letter
        * Cannot end with a hyphen or contain two consecutive hyphens
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


_ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientModifyDbClusterResponseDBClusterTypeDef(_ClientModifyDbClusterResponseDBClusterTypeDef):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.
      This data type is used as a response element in the  DescribeDBClusters action.
      - **AllocatedStorage** *(integer) --*

        ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not fixed,
        but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Neptune DB cluster.
        This data type is used as a response element in the  DescribeDBClusters action.
        - **AllocatedStorage** *(integer) --*

          ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
          fixed, but instead automatically adjusts as needed.
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

      Contains the results of a successful call to the  DescribeDBClusterSnapshotAttributes API
      action.
      Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or
      restore a manual DB cluster snapshot. For more information, see the
      ModifyDBClusterSnapshotAttribute API action.
      - **DBClusterSnapshotIdentifier** *(string) --*

        The identifier of the manual DB cluster snapshot that the attributes apply to.
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

        Contains the results of a successful call to the  DescribeDBClusterSnapshotAttributes API
        action.
        Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or
        restore a manual DB cluster snapshot. For more information, see the
        ModifyDBClusterSnapshotAttribute API action.
        - **DBClusterSnapshotIdentifier** *(string) --*

          The identifier of the manual DB cluster snapshot that the attributes apply to.
    """


_ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "_ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef",
    {"EnableLogTypes": List[str], "DisableLogTypes": List[str]},
    total=False,
)


class ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef(
    _ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef
):
    """
    The configuration setting for the log types to be enabled for export to CloudWatch Logs for a
    specific DB instance or DB cluster.
    - **EnableLogTypes** *(list) --*

      The list of log types to enable.
      - *(string) --*
    """


_ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
):
    pass


_ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
):
    pass


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


_ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef
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


_ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
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
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "DBParameterGroups": List[ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon Neptune DB instance.
      This data type is used as a response element in the  DescribeDBInstances action.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
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

        Contains the details of an Amazon Neptune DB instance.
        This data type is used as a response element in the  DescribeDBInstances action.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientModifyDbParameterGroupParametersTypeDef = TypedDict(
    "_ClientModifyDbParameterGroupParametersTypeDef",
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


class ClientModifyDbParameterGroupParametersTypeDef(_ClientModifyDbParameterGroupParametersTypeDef):
    pass


_ClientModifyDbParameterGroupResponseTypeDef = TypedDict(
    "_ClientModifyDbParameterGroupResponseTypeDef", {"DBParameterGroupName": str}, total=False
)


class ClientModifyDbParameterGroupResponseTypeDef(_ClientModifyDbParameterGroupResponseTypeDef):
    """
    - *(dict) --*

      - **DBParameterGroupName** *(string) --*

        Provides the name of the DB parameter group.
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

      Contains the details of an Amazon Neptune DB subnet group.
      This data type is used as a response element in the  DescribeDBSubnetGroups action.
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

        Contains the details of an Amazon Neptune DB subnet group.
        This data type is used as a response element in the  DescribeDBSubnetGroups action.
        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.
    """


_ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    - **EventSubscription** *(dict) --*

      Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the event notification subscription.
    """


_ClientModifyEventSubscriptionResponseTypeDef = TypedDict(
    "_ClientModifyEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)


class ClientModifyEventSubscriptionResponseTypeDef(_ClientModifyEventSubscriptionResponseTypeDef):
    """
    - *(dict) --*

      - **EventSubscription** *(dict) --*

        Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the event notification subscription.
    """


_ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    pass


_ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    pass


_ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
):
    pass


_ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[
            ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef
        ],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef
):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.
      This data type is used as a response element in the  DescribeDBClusters action.
      - **AllocatedStorage** *(integer) --*

        ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not fixed,
        but instead automatically adjusts as needed.
    """


_ClientPromoteReadReplicaDbClusterResponseTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseTypeDef",
    {"DBCluster": ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseTypeDef
):
    """
    - *(dict) --*

      - **DBCluster** *(dict) --*

        Contains the details of an Amazon Neptune DB cluster.
        This data type is used as a response element in the  DescribeDBClusters action.
        - **AllocatedStorage** *(integer) --*

          ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
          fixed, but instead automatically adjusts as needed.
    """


_ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
):
    pass


_ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
):
    pass


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


_ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef
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


_ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
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
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "DBParameterGroups": List[ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon Neptune DB instance.
      This data type is used as a response element in the  DescribeDBInstances action.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
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

        Contains the details of an Amazon Neptune DB instance.
        This data type is used as a response element in the  DescribeDBInstances action.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef(
    _ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef
):
    """
    - **EventSubscription** *(dict) --*

      Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the event notification subscription.
    """


_ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef = TypedDict(
    "_ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef",
    {
        "EventSubscription": ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef
    },
    total=False,
)


class ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef(
    _ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef
):
    """
    - *(dict) --*

      - **EventSubscription** *(dict) --*

        Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the event notification subscription.
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

      Specifies a parameter.
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

      - **DBClusterParameterGroupName** *(string) --*

        The name of the DB cluster parameter group.
        Constraints:
        * Must be 1 to 255 letters or numbers.
        * First character must be a letter
        * Cannot end with a hyphen or contain two consecutive hyphens
        .. note::

          This value is stored as a lowercase string.
    """


_ClientResetDbParameterGroupParametersTypeDef = TypedDict(
    "_ClientResetDbParameterGroupParametersTypeDef",
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


class ClientResetDbParameterGroupParametersTypeDef(_ClientResetDbParameterGroupParametersTypeDef):
    """
    - *(dict) --*

      Specifies a parameter.
      - **ParameterName** *(string) --*

        Specifies the name of the parameter.
    """


_ClientResetDbParameterGroupResponseTypeDef = TypedDict(
    "_ClientResetDbParameterGroupResponseTypeDef", {"DBParameterGroupName": str}, total=False
)


class ClientResetDbParameterGroupResponseTypeDef(_ClientResetDbParameterGroupResponseTypeDef):
    """
    - *(dict) --*

      - **DBParameterGroupName** *(string) --*

        Provides the name of the DB parameter group.
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


_ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
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
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef
):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.
      This data type is used as a response element in the  DescribeDBClusters action.
      - **AllocatedStorage** *(integer) --*

        ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not fixed,
        but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Neptune DB cluster.
        This data type is used as a response element in the  DescribeDBClusters action.
        - **AllocatedStorage** *(integer) --*

          ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
          fixed, but instead automatically adjusts as needed.
    """


_ClientRestoreDbClusterFromSnapshotTagsTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRestoreDbClusterFromSnapshotTagsTypeDef(_ClientRestoreDbClusterFromSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
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


_ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
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
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef
):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.
      This data type is used as a response element in the  DescribeDBClusters action.
      - **AllocatedStorage** *(integer) --*

        ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not fixed,
        but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Neptune DB cluster.
        This data type is used as a response element in the  DescribeDBClusters action.
        - **AllocatedStorage** *(integer) --*

          ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
          fixed, but instead automatically adjusts as needed.
    """


_ClientRestoreDbClusterToPointInTimeTagsTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRestoreDbClusterToPointInTimeTagsTypeDef(
    _ClientRestoreDbClusterToPointInTimeTagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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


_RequiredDescribeDBClusterParameterGroupsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeDBClusterParameterGroupsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeDBClusterParameterGroupsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeDBClusterParameterGroupsPaginateFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeDBClusterParameterGroupsPaginateFiltersTypeDef(
    _RequiredDescribeDBClusterParameterGroupsPaginateFiltersTypeDef,
    _OptionalDescribeDBClusterParameterGroupsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_DescribeDBClusterParameterGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBClusterParameterGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBClusterParameterGroupsPaginatePaginationConfigTypeDef(
    _DescribeDBClusterParameterGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBClusterParameterGroupsPaginateResponseDBClusterParameterGroupsTypeDef = TypedDict(
    "_DescribeDBClusterParameterGroupsPaginateResponseDBClusterParameterGroupsTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)


class DescribeDBClusterParameterGroupsPaginateResponseDBClusterParameterGroupsTypeDef(
    _DescribeDBClusterParameterGroupsPaginateResponseDBClusterParameterGroupsTypeDef
):
    """
    - *(dict) --*

      Contains the details of an Amazon Neptune DB cluster parameter group.
      This data type is used as a response element in the  DescribeDBClusterParameterGroups action.
      - **DBClusterParameterGroupName** *(string) --*

        Provides the name of the DB cluster parameter group.
    """


_DescribeDBClusterParameterGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBClusterParameterGroupsPaginateResponseTypeDef",
    {
        "DBClusterParameterGroups": List[
            DescribeDBClusterParameterGroupsPaginateResponseDBClusterParameterGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBClusterParameterGroupsPaginateResponseTypeDef(
    _DescribeDBClusterParameterGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **DBClusterParameterGroups** *(list) --*

        A list of DB cluster parameter groups.
        - *(dict) --*

          Contains the details of an Amazon Neptune DB cluster parameter group.
          This data type is used as a response element in the  DescribeDBClusterParameterGroups
          action.
          - **DBClusterParameterGroupName** *(string) --*

            Provides the name of the DB cluster parameter group.
    """


_RequiredDescribeDBClusterParametersPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeDBClusterParametersPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeDBClusterParametersPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeDBClusterParametersPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeDBClusterParametersPaginateFiltersTypeDef(
    _RequiredDescribeDBClusterParametersPaginateFiltersTypeDef,
    _OptionalDescribeDBClusterParametersPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_DescribeDBClusterParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBClusterParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBClusterParametersPaginatePaginationConfigTypeDef(
    _DescribeDBClusterParametersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBClusterParametersPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeDBClusterParametersPaginateResponseParametersTypeDef",
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


class DescribeDBClusterParametersPaginateResponseParametersTypeDef(
    _DescribeDBClusterParametersPaginateResponseParametersTypeDef
):
    """
    - *(dict) --*

      Specifies a parameter.
      - **ParameterName** *(string) --*

        Specifies the name of the parameter.
    """


_DescribeDBClusterParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeDBClusterParametersPaginateResponseTypeDef",
    {
        "Parameters": List[DescribeDBClusterParametersPaginateResponseParametersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBClusterParametersPaginateResponseTypeDef(
    _DescribeDBClusterParametersPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Parameters** *(list) --*

        Provides a list of parameters for the DB cluster parameter group.
        - *(dict) --*

          Specifies a parameter.
          - **ParameterName** *(string) --*

            Specifies the name of the parameter.
    """


_RequiredDescribeDBClusterSnapshotsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeDBClusterSnapshotsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeDBClusterSnapshotsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeDBClusterSnapshotsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeDBClusterSnapshotsPaginateFiltersTypeDef(
    _RequiredDescribeDBClusterSnapshotsPaginateFiltersTypeDef,
    _OptionalDescribeDBClusterSnapshotsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_DescribeDBClusterSnapshotsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBClusterSnapshotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBClusterSnapshotsPaginatePaginationConfigTypeDef(
    _DescribeDBClusterSnapshotsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBClusterSnapshotsPaginateResponseDBClusterSnapshotsTypeDef = TypedDict(
    "_DescribeDBClusterSnapshotsPaginateResponseDBClusterSnapshotsTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)


class DescribeDBClusterSnapshotsPaginateResponseDBClusterSnapshotsTypeDef(
    _DescribeDBClusterSnapshotsPaginateResponseDBClusterSnapshotsTypeDef
):
    """
    - *(dict) --*

      Contains the details for an Amazon Neptune DB cluster snapshot
      This data type is used as a response element in the  DescribeDBClusterSnapshots action.
      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can be
        restored in.
        - *(string) --*
    """


_DescribeDBClusterSnapshotsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBClusterSnapshotsPaginateResponseTypeDef",
    {
        "DBClusterSnapshots": List[
            DescribeDBClusterSnapshotsPaginateResponseDBClusterSnapshotsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBClusterSnapshotsPaginateResponseTypeDef(
    _DescribeDBClusterSnapshotsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **DBClusterSnapshots** *(list) --*

        Provides a list of DB cluster snapshots for the user.
        - *(dict) --*

          Contains the details for an Amazon Neptune DB cluster snapshot
          This data type is used as a response element in the  DescribeDBClusterSnapshots action.
          - **AvailabilityZones** *(list) --*

            Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot
            can be restored in.
            - *(string) --*
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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


_DescribeDBClustersPaginateResponseDBClustersDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersDBClusterOptionGroupMembershipsTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersDBClusterOptionGroupMembershipsTypeDef
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            DescribeDBClustersPaginateResponseDBClustersDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
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
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersTypeDef
):
    """
    - *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.
      This data type is used as a response element in the  DescribeDBClusters action.
      - **AllocatedStorage** *(integer) --*

        ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not fixed,
        but instead automatically adjusts as needed.
    """


_DescribeDBClustersPaginateResponseTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseTypeDef",
    {"DBClusters": List[DescribeDBClustersPaginateResponseDBClustersTypeDef], "NextToken": str},
    total=False,
)


class DescribeDBClustersPaginateResponseTypeDef(_DescribeDBClustersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **DBClusters** *(list) --*

        Contains a list of DB clusters for the user.
        - *(dict) --*

          Contains the details of an Amazon Neptune DB cluster.
          This data type is used as a response element in the  DescribeDBClusters action.
          - **AllocatedStorage** *(integer) --*

            ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
            fixed, but instead automatically adjusts as needed.
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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


_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsDefaultCharacterSetTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsDefaultCharacterSetTypeDef",
    {"CharacterSetName": str, "CharacterSetDescription": str},
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsDefaultCharacterSetTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsDefaultCharacterSetTypeDef
):
    pass


_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedCharacterSetsTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedCharacterSetsTypeDef",
    {"CharacterSetName": str, "CharacterSetDescription": str},
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedCharacterSetsTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedCharacterSetsTypeDef
):
    pass


_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedTimezonesTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedTimezonesTypeDef",
    {"TimezoneName": str},
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedTimezonesTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedTimezonesTypeDef
):
    pass


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
        "DefaultCharacterSet": DescribeDBEngineVersionsPaginateResponseDBEngineVersionsDefaultCharacterSetTypeDef,
        "SupportedCharacterSets": List[
            DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedCharacterSetsTypeDef
        ],
        "ValidUpgradeTarget": List[
            DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef
        ],
        "SupportedTimezones": List[
            DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedTimezonesTypeDef
        ],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
        "SupportsReadReplica": bool,
    },
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef
):
    """
    - *(dict) --*

      This data type is used as a response element in the action  DescribeDBEngineVersions .
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

      - **DBEngineVersions** *(list) --*

        A list of ``DBEngineVersion`` elements.
        - *(dict) --*

          This data type is used as a response element in the action  DescribeDBEngineVersions .
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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


_DescribeDBInstancesPaginateResponseDBInstancesDBParameterGroupsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDBParameterGroupsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDBParameterGroupsTypeDef
):
    pass


_DescribeDBInstancesPaginateResponseDBInstancesDBSecurityGroupsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDBSecurityGroupsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDBSecurityGroupsTypeDef
):
    pass


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


_DescribeDBInstancesPaginateResponseDBInstancesDomainMembershipsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDomainMembershipsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDomainMembershipsTypeDef
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


_DescribeDBInstancesPaginateResponseDBInstancesOptionGroupMembershipsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesOptionGroupMembershipsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesOptionGroupMembershipsTypeDef
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
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            DescribeDBInstancesPaginateResponseDBInstancesDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            DescribeDBInstancesPaginateResponseDBInstancesDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            DescribeDBInstancesPaginateResponseDBInstancesOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            DescribeDBInstancesPaginateResponseDBInstancesDomainMembershipsTypeDef
        ],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesTypeDef
):
    """
    - *(dict) --*

      Contains the details of an Amazon Neptune DB instance.
      This data type is used as a response element in the  DescribeDBInstances action.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
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

      - **DBInstances** *(list) --*

        A list of  DBInstance instances.
        - *(dict) --*

          Contains the details of an Amazon Neptune DB instance.
          This data type is used as a response element in the  DescribeDBInstances action.
          - **DBInstanceIdentifier** *(string) --*

            Contains a user-supplied database identifier. This identifier is the unique key that
            identifies a DB instance.
    """


_RequiredDescribeDBParameterGroupsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeDBParameterGroupsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeDBParameterGroupsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeDBParameterGroupsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeDBParameterGroupsPaginateFiltersTypeDef(
    _RequiredDescribeDBParameterGroupsPaginateFiltersTypeDef,
    _OptionalDescribeDBParameterGroupsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_DescribeDBParameterGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBParameterGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBParameterGroupsPaginatePaginationConfigTypeDef(
    _DescribeDBParameterGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBParameterGroupsPaginateResponseDBParameterGroupsTypeDef = TypedDict(
    "_DescribeDBParameterGroupsPaginateResponseDBParameterGroupsTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)


class DescribeDBParameterGroupsPaginateResponseDBParameterGroupsTypeDef(
    _DescribeDBParameterGroupsPaginateResponseDBParameterGroupsTypeDef
):
    """
    - *(dict) --*

      Contains the details of an Amazon Neptune DB parameter group.
      This data type is used as a response element in the  DescribeDBParameterGroups action.
      - **DBParameterGroupName** *(string) --*

        Provides the name of the DB parameter group.
    """


_DescribeDBParameterGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBParameterGroupsPaginateResponseTypeDef",
    {
        "DBParameterGroups": List[
            DescribeDBParameterGroupsPaginateResponseDBParameterGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBParameterGroupsPaginateResponseTypeDef(
    _DescribeDBParameterGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **DBParameterGroups** *(list) --*

        A list of  DBParameterGroup instances.
        - *(dict) --*

          Contains the details of an Amazon Neptune DB parameter group.
          This data type is used as a response element in the  DescribeDBParameterGroups action.
          - **DBParameterGroupName** *(string) --*

            Provides the name of the DB parameter group.
    """


_RequiredDescribeDBParametersPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeDBParametersPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeDBParametersPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeDBParametersPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeDBParametersPaginateFiltersTypeDef(
    _RequiredDescribeDBParametersPaginateFiltersTypeDef,
    _OptionalDescribeDBParametersPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_DescribeDBParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBParametersPaginatePaginationConfigTypeDef(
    _DescribeDBParametersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBParametersPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeDBParametersPaginateResponseParametersTypeDef",
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


class DescribeDBParametersPaginateResponseParametersTypeDef(
    _DescribeDBParametersPaginateResponseParametersTypeDef
):
    """
    - *(dict) --*

      Specifies a parameter.
      - **ParameterName** *(string) --*

        Specifies the name of the parameter.
    """


_DescribeDBParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeDBParametersPaginateResponseTypeDef",
    {"Parameters": List[DescribeDBParametersPaginateResponseParametersTypeDef], "NextToken": str},
    total=False,
)


class DescribeDBParametersPaginateResponseTypeDef(_DescribeDBParametersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Parameters** *(list) --*

        A list of  Parameter values.
        - *(dict) --*

          Specifies a parameter.
          - **ParameterName** *(string) --*

            Specifies the name of the parameter.
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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

      Contains the details of an Amazon Neptune DB subnet group.
      This data type is used as a response element in the  DescribeDBSubnetGroups action.
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

      - **DBSubnetGroups** *(list) --*

        A list of  DBSubnetGroup instances.
        - *(dict) --*

          Contains the details of an Amazon Neptune DB subnet group.
          This data type is used as a response element in the  DescribeDBSubnetGroups action.
          - **DBSubnetGroupName** *(string) --*

            The name of the DB subnet group.
    """


_RequiredDescribeEngineDefaultParametersPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeEngineDefaultParametersPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeEngineDefaultParametersPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeEngineDefaultParametersPaginateFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeEngineDefaultParametersPaginateFiltersTypeDef(
    _RequiredDescribeEngineDefaultParametersPaginateFiltersTypeDef,
    _OptionalDescribeEngineDefaultParametersPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef(
    _DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef",
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


class DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef(
    _DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef
):
    pass


_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef
        ],
    },
    total=False,
)


class DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef(
    _DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef
):
    """
    - **EngineDefaults** *(dict) --*

      Contains the result of a successful invocation of the  DescribeEngineDefaultParameters action.
      - **DBParameterGroupFamily** *(string) --*

        Specifies the name of the DB parameter group family that the engine default parameters apply
        to.
    """


_DescribeEngineDefaultParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateResponseTypeDef",
    {
        "EngineDefaults": DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef,
        "NextToken": str,
    },
    total=False,
)


class DescribeEngineDefaultParametersPaginateResponseTypeDef(
    _DescribeEngineDefaultParametersPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **EngineDefaults** *(dict) --*

        Contains the result of a successful invocation of the  DescribeEngineDefaultParameters
        action.
        - **DBParameterGroupFamily** *(string) --*

          Specifies the name of the DB parameter group family that the engine default parameters
          apply to.
    """


_RequiredDescribeEventSubscriptionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeEventSubscriptionsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeEventSubscriptionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeEventSubscriptionsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeEventSubscriptionsPaginateFiltersTypeDef(
    _RequiredDescribeEventSubscriptionsPaginateFiltersTypeDef,
    _OptionalDescribeEventSubscriptionsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_DescribeEventSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventSubscriptionsPaginatePaginationConfigTypeDef(
    _DescribeEventSubscriptionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef(
    _DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef
):
    """
    - *(dict) --*

      Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the event notification subscription.
    """


_DescribeEventSubscriptionsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginateResponseTypeDef",
    {
        "EventSubscriptionsList": List[
            DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeEventSubscriptionsPaginateResponseTypeDef(
    _DescribeEventSubscriptionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **EventSubscriptionsList** *(list) --*

        A list of EventSubscriptions data types.
        - *(dict) --*

          Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
          - **CustomerAwsId** *(string) --*

            The AWS customer account associated with the event notification subscription.
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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

      This data type is used as a response element in the  DescribeEvents action.
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

      - **Events** *(list) --*

        A list of  Event instances.
        - *(dict) --*

          This data type is used as a response element in the  DescribeEvents action.
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

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
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
        "MultiAZCapable": bool,
        "ReadReplicaCapable": bool,
        "Vpc": bool,
        "SupportsStorageEncryption": bool,
        "StorageType": str,
        "SupportsIops": bool,
        "SupportsEnhancedMonitoring": bool,
        "SupportsIAMDatabaseAuthentication": bool,
        "SupportsPerformanceInsights": bool,
        "MinStorageSize": int,
        "MaxStorageSize": int,
        "MinIopsPerDbInstance": int,
        "MaxIopsPerDbInstance": int,
        "MinIopsPerGib": float,
        "MaxIopsPerGib": float,
    },
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef
):
    """
    - *(dict) --*

      Contains a list of available options for a DB instance.
      This data type is used as a response element in the  DescribeOrderableDBInstanceOptions
      action.
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

      - **OrderableDBInstanceOptions** *(list) --*

        An  OrderableDBInstanceOption structure containing information about orderable options for
        the DB instance.
        - *(dict) --*

          Contains a list of available options for a DB instance.
          This data type is used as a response element in the  DescribeOrderableDBInstanceOptions
          action.
          - **Engine** *(string) --*

            The engine type of a DB instance.
    """


_RequiredDescribePendingMaintenanceActionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribePendingMaintenanceActionsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribePendingMaintenanceActionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribePendingMaintenanceActionsPaginateFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribePendingMaintenanceActionsPaginateFiltersTypeDef(
    _RequiredDescribePendingMaintenanceActionsPaginateFiltersTypeDef,
    _OptionalDescribePendingMaintenanceActionsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      This type is not currently supported.
      - **Name** *(string) --***[REQUIRED]**

        This parameter is not currently supported.
    """


_DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef(
    _DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "_DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
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


class DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef(
    _DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
):
    pass


_DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsTypeDef = TypedDict(
    "_DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)


class DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsTypeDef(
    _DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsTypeDef
):
    """
    - *(dict) --*

      Describes the pending maintenance actions for a resource.
      - **ResourceIdentifier** *(string) --*

        The ARN of the resource that has pending maintenance actions.
    """


_DescribePendingMaintenanceActionsPaginateResponseTypeDef = TypedDict(
    "_DescribePendingMaintenanceActionsPaginateResponseTypeDef",
    {
        "PendingMaintenanceActions": List[
            DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribePendingMaintenanceActionsPaginateResponseTypeDef(
    _DescribePendingMaintenanceActionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **PendingMaintenanceActions** *(list) --*

        A list of the pending maintenance actions for the resource.
        - *(dict) --*

          Describes the pending maintenance actions for a resource.
          - **ResourceIdentifier** *(string) --*

            The ARN of the resource that has pending maintenance actions.
    """
