"Main interface for rds service type defs"
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
    "ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef",
    "ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef",
    "ClientAuthorizeDbSecurityGroupIngressResponseTypeDef",
    "ClientBacktrackDbClusterResponseTypeDef",
    "ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCopyDbClusterParameterGroupResponseTypeDef",
    "ClientCopyDbClusterParameterGroupTagsTypeDef",
    "ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCopyDbClusterSnapshotResponseTypeDef",
    "ClientCopyDbClusterSnapshotTagsTypeDef",
    "ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef",
    "ClientCopyDbParameterGroupResponseTypeDef",
    "ClientCopyDbParameterGroupTagsTypeDef",
    "ClientCopyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    "ClientCopyDbSnapshotResponseDBSnapshotTypeDef",
    "ClientCopyDbSnapshotResponseTypeDef",
    "ClientCopyDbSnapshotTagsTypeDef",
    "ClientCopyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef",
    "ClientCopyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef",
    "ClientCopyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef",
    "ClientCopyOptionGroupResponseOptionGroupOptionsTypeDef",
    "ClientCopyOptionGroupResponseOptionGroupTypeDef",
    "ClientCopyOptionGroupResponseTypeDef",
    "ClientCopyOptionGroupTagsTypeDef",
    "ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef",
    "ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef",
    "ClientCreateCustomAvailabilityZoneResponseTypeDef",
    "ClientCreateDbClusterEndpointResponseTypeDef",
    "ClientCreateDbClusterEndpointTagsTypeDef",
    "ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCreateDbClusterParameterGroupResponseTypeDef",
    "ClientCreateDbClusterParameterGroupTagsTypeDef",
    "ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientCreateDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientCreateDbClusterResponseDBClusterTypeDef",
    "ClientCreateDbClusterResponseTypeDef",
    "ClientCreateDbClusterScalingConfigurationTypeDef",
    "ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCreateDbClusterSnapshotResponseTypeDef",
    "ClientCreateDbClusterSnapshotTagsTypeDef",
    "ClientCreateDbClusterTagsTypeDef",
    "ClientCreateDbInstanceProcessorFeaturesTypeDef",
    "ClientCreateDbInstanceReadReplicaProcessorFeaturesTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceAssociatedRolesTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDomainMembershipsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceEndpointTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceListenerEndpointTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceStatusInfosTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseTypeDef",
    "ClientCreateDbInstanceReadReplicaTagsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceTypeDef",
    "ClientCreateDbInstanceResponseTypeDef",
    "ClientCreateDbInstanceTagsTypeDef",
    "ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef",
    "ClientCreateDbParameterGroupResponseTypeDef",
    "ClientCreateDbParameterGroupTagsTypeDef",
    "ClientCreateDbProxyAuthTypeDef",
    "ClientCreateDbProxyResponseDBProxyAuthTypeDef",
    "ClientCreateDbProxyResponseDBProxyTypeDef",
    "ClientCreateDbProxyResponseTypeDef",
    "ClientCreateDbProxyTagsTypeDef",
    "ClientCreateDbSecurityGroupResponseDBSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientCreateDbSecurityGroupResponseDBSecurityGroupIPRangesTypeDef",
    "ClientCreateDbSecurityGroupResponseDBSecurityGroupTypeDef",
    "ClientCreateDbSecurityGroupResponseTypeDef",
    "ClientCreateDbSecurityGroupTagsTypeDef",
    "ClientCreateDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    "ClientCreateDbSnapshotResponseDBSnapshotTypeDef",
    "ClientCreateDbSnapshotResponseTypeDef",
    "ClientCreateDbSnapshotTagsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientCreateDbSubnetGroupResponseTypeDef",
    "ClientCreateDbSubnetGroupTagsTypeDef",
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientCreateEventSubscriptionResponseTypeDef",
    "ClientCreateEventSubscriptionTagsTypeDef",
    "ClientCreateGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    "ClientCreateGlobalClusterResponseGlobalClusterTypeDef",
    "ClientCreateGlobalClusterResponseTypeDef",
    "ClientCreateOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef",
    "ClientCreateOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef",
    "ClientCreateOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef",
    "ClientCreateOptionGroupResponseOptionGroupOptionsTypeDef",
    "ClientCreateOptionGroupResponseOptionGroupTypeDef",
    "ClientCreateOptionGroupResponseTypeDef",
    "ClientCreateOptionGroupTagsTypeDef",
    "ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef",
    "ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef",
    "ClientDeleteCustomAvailabilityZoneResponseTypeDef",
    "ClientDeleteDbClusterEndpointResponseTypeDef",
    "ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterTypeDef",
    "ClientDeleteDbClusterResponseTypeDef",
    "ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientDeleteDbClusterSnapshotResponseTypeDef",
    "ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupRestoreWindowTypeDef",
    "ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupTypeDef",
    "ClientDeleteDbInstanceAutomatedBackupResponseTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceTypeDef",
    "ClientDeleteDbInstanceResponseTypeDef",
    "ClientDeleteDbProxyResponseDBProxyAuthTypeDef",
    "ClientDeleteDbProxyResponseDBProxyTypeDef",
    "ClientDeleteDbProxyResponseTypeDef",
    "ClientDeleteDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    "ClientDeleteDbSnapshotResponseDBSnapshotTypeDef",
    "ClientDeleteDbSnapshotResponseTypeDef",
    "ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientDeleteEventSubscriptionResponseTypeDef",
    "ClientDeleteGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    "ClientDeleteGlobalClusterResponseGlobalClusterTypeDef",
    "ClientDeleteGlobalClusterResponseTypeDef",
    "ClientDeleteInstallationMediaResponseFailureCauseTypeDef",
    "ClientDeleteInstallationMediaResponseTypeDef",
    "ClientDescribeAccountAttributesResponseAccountQuotasTypeDef",
    "ClientDescribeAccountAttributesResponseTypeDef",
    "ClientDescribeCertificatesFiltersTypeDef",
    "ClientDescribeCertificatesResponseCertificatesTypeDef",
    "ClientDescribeCertificatesResponseTypeDef",
    "ClientDescribeCustomAvailabilityZonesFiltersTypeDef",
    "ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesVpnDetailsTypeDef",
    "ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesTypeDef",
    "ClientDescribeCustomAvailabilityZonesResponseTypeDef",
    "ClientDescribeDbClusterBacktracksFiltersTypeDef",
    "ClientDescribeDbClusterBacktracksResponseDBClusterBacktracksTypeDef",
    "ClientDescribeDbClusterBacktracksResponseTypeDef",
    "ClientDescribeDbClusterEndpointsFiltersTypeDef",
    "ClientDescribeDbClusterEndpointsResponseDBClusterEndpointsTypeDef",
    "ClientDescribeDbClusterEndpointsResponseTypeDef",
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
    "ClientDescribeDbClustersResponseDBClustersScalingConfigurationInfoTypeDef",
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
    "ClientDescribeDbInstanceAutomatedBackupsFiltersTypeDef",
    "ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef",
    "ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsTypeDef",
    "ClientDescribeDbInstanceAutomatedBackupsResponseTypeDef",
    "ClientDescribeDbInstancesFiltersTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesAssociatedRolesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesListenerEndpointTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesProcessorFeaturesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesTypeDef",
    "ClientDescribeDbInstancesResponseTypeDef",
    "ClientDescribeDbLogFilesFiltersTypeDef",
    "ClientDescribeDbLogFilesResponseDescribeDBLogFilesTypeDef",
    "ClientDescribeDbLogFilesResponseTypeDef",
    "ClientDescribeDbParameterGroupsFiltersTypeDef",
    "ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef",
    "ClientDescribeDbParameterGroupsResponseTypeDef",
    "ClientDescribeDbParametersFiltersTypeDef",
    "ClientDescribeDbParametersResponseParametersTypeDef",
    "ClientDescribeDbParametersResponseTypeDef",
    "ClientDescribeDbProxiesFiltersTypeDef",
    "ClientDescribeDbProxiesResponseDBProxiesAuthTypeDef",
    "ClientDescribeDbProxiesResponseDBProxiesTypeDef",
    "ClientDescribeDbProxiesResponseTypeDef",
    "ClientDescribeDbProxyTargetGroupsFiltersTypeDef",
    "ClientDescribeDbProxyTargetGroupsResponseTargetGroupsConnectionPoolConfigTypeDef",
    "ClientDescribeDbProxyTargetGroupsResponseTargetGroupsTypeDef",
    "ClientDescribeDbProxyTargetGroupsResponseTypeDef",
    "ClientDescribeDbProxyTargetsFiltersTypeDef",
    "ClientDescribeDbProxyTargetsResponseTargetsTypeDef",
    "ClientDescribeDbProxyTargetsResponseTypeDef",
    "ClientDescribeDbSecurityGroupsFiltersTypeDef",
    "ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsEC2SecurityGroupsTypeDef",
    "ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsIPRangesTypeDef",
    "ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsTypeDef",
    "ClientDescribeDbSecurityGroupsResponseTypeDef",
    "ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef",
    "ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultTypeDef",
    "ClientDescribeDbSnapshotAttributesResponseTypeDef",
    "ClientDescribeDbSnapshotsFiltersTypeDef",
    "ClientDescribeDbSnapshotsResponseDBSnapshotsProcessorFeaturesTypeDef",
    "ClientDescribeDbSnapshotsResponseDBSnapshotsTypeDef",
    "ClientDescribeDbSnapshotsResponseTypeDef",
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
    "ClientDescribeGlobalClustersFiltersTypeDef",
    "ClientDescribeGlobalClustersResponseGlobalClustersGlobalClusterMembersTypeDef",
    "ClientDescribeGlobalClustersResponseGlobalClustersTypeDef",
    "ClientDescribeGlobalClustersResponseTypeDef",
    "ClientDescribeInstallationMediaFiltersTypeDef",
    "ClientDescribeInstallationMediaResponseInstallationMediaFailureCauseTypeDef",
    "ClientDescribeInstallationMediaResponseInstallationMediaTypeDef",
    "ClientDescribeInstallationMediaResponseTypeDef",
    "ClientDescribeOptionGroupOptionsFiltersTypeDef",
    "ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef",
    "ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef",
    "ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef",
    "ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsTypeDef",
    "ClientDescribeOptionGroupOptionsResponseTypeDef",
    "ClientDescribeOptionGroupsFiltersTypeDef",
    "ClientDescribeOptionGroupsResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef",
    "ClientDescribeOptionGroupsResponseOptionGroupsListOptionsOptionSettingsTypeDef",
    "ClientDescribeOptionGroupsResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef",
    "ClientDescribeOptionGroupsResponseOptionGroupsListOptionsTypeDef",
    "ClientDescribeOptionGroupsResponseOptionGroupsListTypeDef",
    "ClientDescribeOptionGroupsResponseTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseTypeDef",
    "ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponseTypeDef",
    "ClientDescribeReservedDbInstancesFiltersTypeDef",
    "ClientDescribeReservedDbInstancesOfferingsFiltersTypeDef",
    "ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsRecurringChargesTypeDef",
    "ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsTypeDef",
    "ClientDescribeReservedDbInstancesOfferingsResponseTypeDef",
    "ClientDescribeReservedDbInstancesResponseReservedDBInstancesRecurringChargesTypeDef",
    "ClientDescribeReservedDbInstancesResponseReservedDBInstancesTypeDef",
    "ClientDescribeReservedDbInstancesResponseTypeDef",
    "ClientDescribeSourceRegionsFiltersTypeDef",
    "ClientDescribeSourceRegionsResponseSourceRegionsTypeDef",
    "ClientDescribeSourceRegionsResponseTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageValidProcessorFeaturesTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseTypeDef",
    "ClientDownloadDbLogFilePortionResponseTypeDef",
    "ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientFailoverDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientFailoverDbClusterResponseDBClusterTypeDef",
    "ClientFailoverDbClusterResponseTypeDef",
    "ClientImportInstallationMediaResponseFailureCauseTypeDef",
    "ClientImportInstallationMediaResponseTypeDef",
    "ClientListTagsForResourceFiltersTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyCurrentDbClusterCapacityResponseTypeDef",
    "ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef",
    "ClientModifyDbClusterEndpointResponseTypeDef",
    "ClientModifyDbClusterParameterGroupParametersTypeDef",
    "ClientModifyDbClusterParameterGroupResponseTypeDef",
    "ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientModifyDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientModifyDbClusterResponseDBClusterTypeDef",
    "ClientModifyDbClusterResponseTypeDef",
    "ClientModifyDbClusterScalingConfigurationTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseTypeDef",
    "ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef",
    "ClientModifyDbInstanceProcessorFeaturesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceTypeDef",
    "ClientModifyDbInstanceResponseTypeDef",
    "ClientModifyDbParameterGroupParametersTypeDef",
    "ClientModifyDbParameterGroupResponseTypeDef",
    "ClientModifyDbProxyAuthTypeDef",
    "ClientModifyDbProxyResponseDBProxyAuthTypeDef",
    "ClientModifyDbProxyResponseDBProxyTypeDef",
    "ClientModifyDbProxyResponseTypeDef",
    "ClientModifyDbProxyTargetGroupConnectionPoolConfigTypeDef",
    "ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupConnectionPoolConfigTypeDef",
    "ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupTypeDef",
    "ClientModifyDbProxyTargetGroupResponseTypeDef",
    "ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef",
    "ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultTypeDef",
    "ClientModifyDbSnapshotAttributeResponseTypeDef",
    "ClientModifyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    "ClientModifyDbSnapshotResponseDBSnapshotTypeDef",
    "ClientModifyDbSnapshotResponseTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientModifyDbSubnetGroupResponseTypeDef",
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientModifyEventSubscriptionResponseTypeDef",
    "ClientModifyGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    "ClientModifyGlobalClusterResponseGlobalClusterTypeDef",
    "ClientModifyGlobalClusterResponseTypeDef",
    "ClientModifyOptionGroupOptionsToIncludeOptionSettingsTypeDef",
    "ClientModifyOptionGroupOptionsToIncludeTypeDef",
    "ClientModifyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef",
    "ClientModifyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef",
    "ClientModifyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef",
    "ClientModifyOptionGroupResponseOptionGroupOptionsTypeDef",
    "ClientModifyOptionGroupResponseOptionGroupTypeDef",
    "ClientModifyOptionGroupResponseTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceAssociatedRolesTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceDomainMembershipsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceEndpointTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceListenerEndpointTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceStatusInfosTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceTypeDef",
    "ClientPromoteReadReplicaResponseTypeDef",
    "ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceRecurringChargesTypeDef",
    "ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceTypeDef",
    "ClientPurchaseReservedDbInstancesOfferingResponseTypeDef",
    "ClientPurchaseReservedDbInstancesOfferingTagsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceTypeDef",
    "ClientRebootDbInstanceResponseTypeDef",
    "ClientRegisterDbProxyTargetsResponseDBProxyTargetsTypeDef",
    "ClientRegisterDbProxyTargetsResponseTypeDef",
    "ClientRemoveFromGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    "ClientRemoveFromGlobalClusterResponseGlobalClusterTypeDef",
    "ClientRemoveFromGlobalClusterResponseTypeDef",
    "ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef",
    "ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef",
    "ClientResetDbClusterParameterGroupParametersTypeDef",
    "ClientResetDbClusterParameterGroupResponseTypeDef",
    "ClientResetDbParameterGroupParametersTypeDef",
    "ClientResetDbParameterGroupResponseTypeDef",
    "ClientRestoreDbClusterFromS3ResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientRestoreDbClusterFromS3ResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientRestoreDbClusterFromS3ResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterFromS3ResponseDBClusterTypeDef",
    "ClientRestoreDbClusterFromS3ResponseTypeDef",
    "ClientRestoreDbClusterFromS3TagsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotScalingConfigurationTypeDef",
    "ClientRestoreDbClusterFromSnapshotTagsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseTypeDef",
    "ClientRestoreDbClusterToPointInTimeTagsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceAssociatedRolesTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDomainMembershipsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceEndpointTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceListenerEndpointTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceStatusInfosTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotTagsTypeDef",
    "ClientRestoreDbInstanceFromS3ProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceAssociatedRolesTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDomainMembershipsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceEndpointTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceListenerEndpointTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceStatusInfosTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseTypeDef",
    "ClientRestoreDbInstanceFromS3TagsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceAssociatedRolesTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDomainMembershipsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceEndpointTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceListenerEndpointTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceStatusInfosTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseTypeDef",
    "ClientRestoreDbInstanceToPointInTimeTagsTypeDef",
    "ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef",
    "ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef",
    "ClientRevokeDbSecurityGroupIngressResponseTypeDef",
    "ClientStartActivityStreamResponseTypeDef",
    "ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientStartDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientStartDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientStartDbClusterResponseDBClusterTypeDef",
    "ClientStartDbClusterResponseTypeDef",
    "ClientStartDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    "ClientStartDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientStartDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientStartDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientStartDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientStartDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientStartDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    "ClientStartDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientStartDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientStartDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientStartDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientStartDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientStartDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientStartDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientStartDbInstanceResponseDBInstanceTypeDef",
    "ClientStartDbInstanceResponseTypeDef",
    "ClientStopActivityStreamResponseTypeDef",
    "ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientStopDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientStopDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientStopDbClusterResponseDBClusterTypeDef",
    "ClientStopDbClusterResponseTypeDef",
    "ClientStopDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    "ClientStopDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientStopDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientStopDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientStopDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientStopDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientStopDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    "ClientStopDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientStopDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientStopDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientStopDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientStopDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientStopDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientStopDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientStopDbInstanceResponseDBInstanceTypeDef",
    "ClientStopDbInstanceResponseTypeDef",
    "DbClusterSnapshotAvailableWaitFiltersTypeDef",
    "DbClusterSnapshotAvailableWaitWaiterConfigTypeDef",
    "DbClusterSnapshotDeletedWaitFiltersTypeDef",
    "DbClusterSnapshotDeletedWaitWaiterConfigTypeDef",
    "DbInstanceAvailableWaitFiltersTypeDef",
    "DbInstanceAvailableWaitWaiterConfigTypeDef",
    "DbInstanceDeletedWaitFiltersTypeDef",
    "DbInstanceDeletedWaitWaiterConfigTypeDef",
    "DbSnapshotAvailableWaitFiltersTypeDef",
    "DbSnapshotAvailableWaitWaiterConfigTypeDef",
    "DbSnapshotCompletedWaitFiltersTypeDef",
    "DbSnapshotCompletedWaitWaiterConfigTypeDef",
    "DbSnapshotDeletedWaitFiltersTypeDef",
    "DbSnapshotDeletedWaitWaiterConfigTypeDef",
    "DescribeCertificatesPaginateFiltersTypeDef",
    "DescribeCertificatesPaginatePaginationConfigTypeDef",
    "DescribeCertificatesPaginateResponseCertificatesTypeDef",
    "DescribeCertificatesPaginateResponseTypeDef",
    "DescribeCustomAvailabilityZonesPaginateFiltersTypeDef",
    "DescribeCustomAvailabilityZonesPaginatePaginationConfigTypeDef",
    "DescribeCustomAvailabilityZonesPaginateResponseCustomAvailabilityZonesVpnDetailsTypeDef",
    "DescribeCustomAvailabilityZonesPaginateResponseCustomAvailabilityZonesTypeDef",
    "DescribeCustomAvailabilityZonesPaginateResponseTypeDef",
    "DescribeDBClusterBacktracksPaginateFiltersTypeDef",
    "DescribeDBClusterBacktracksPaginatePaginationConfigTypeDef",
    "DescribeDBClusterBacktracksPaginateResponseDBClusterBacktracksTypeDef",
    "DescribeDBClusterBacktracksPaginateResponseTypeDef",
    "DescribeDBClusterEndpointsPaginateFiltersTypeDef",
    "DescribeDBClusterEndpointsPaginatePaginationConfigTypeDef",
    "DescribeDBClusterEndpointsPaginateResponseDBClusterEndpointsTypeDef",
    "DescribeDBClusterEndpointsPaginateResponseTypeDef",
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
    "DescribeDBClustersPaginateResponseDBClustersScalingConfigurationInfoTypeDef",
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
    "DescribeDBInstanceAutomatedBackupsPaginateFiltersTypeDef",
    "DescribeDBInstanceAutomatedBackupsPaginatePaginationConfigTypeDef",
    "DescribeDBInstanceAutomatedBackupsPaginateResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef",
    "DescribeDBInstanceAutomatedBackupsPaginateResponseDBInstanceAutomatedBackupsTypeDef",
    "DescribeDBInstanceAutomatedBackupsPaginateResponseTypeDef",
    "DescribeDBInstancesPaginateFiltersTypeDef",
    "DescribeDBInstancesPaginatePaginationConfigTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesAssociatedRolesTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBParameterGroupsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSecurityGroupsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDomainMembershipsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesListenerEndpointTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesOptionGroupMembershipsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesProcessorFeaturesTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesTypeDef",
    "DescribeDBInstancesPaginateResponseTypeDef",
    "DescribeDBLogFilesPaginateFiltersTypeDef",
    "DescribeDBLogFilesPaginatePaginationConfigTypeDef",
    "DescribeDBLogFilesPaginateResponseDescribeDBLogFilesTypeDef",
    "DescribeDBLogFilesPaginateResponseTypeDef",
    "DescribeDBParameterGroupsPaginateFiltersTypeDef",
    "DescribeDBParameterGroupsPaginatePaginationConfigTypeDef",
    "DescribeDBParameterGroupsPaginateResponseDBParameterGroupsTypeDef",
    "DescribeDBParameterGroupsPaginateResponseTypeDef",
    "DescribeDBParametersPaginateFiltersTypeDef",
    "DescribeDBParametersPaginatePaginationConfigTypeDef",
    "DescribeDBParametersPaginateResponseParametersTypeDef",
    "DescribeDBParametersPaginateResponseTypeDef",
    "DescribeDBProxiesPaginateFiltersTypeDef",
    "DescribeDBProxiesPaginatePaginationConfigTypeDef",
    "DescribeDBProxiesPaginateResponseDBProxiesAuthTypeDef",
    "DescribeDBProxiesPaginateResponseDBProxiesTypeDef",
    "DescribeDBProxiesPaginateResponseTypeDef",
    "DescribeDBProxyTargetGroupsPaginateFiltersTypeDef",
    "DescribeDBProxyTargetGroupsPaginatePaginationConfigTypeDef",
    "DescribeDBProxyTargetGroupsPaginateResponseTargetGroupsConnectionPoolConfigTypeDef",
    "DescribeDBProxyTargetGroupsPaginateResponseTargetGroupsTypeDef",
    "DescribeDBProxyTargetGroupsPaginateResponseTypeDef",
    "DescribeDBProxyTargetsPaginateFiltersTypeDef",
    "DescribeDBProxyTargetsPaginatePaginationConfigTypeDef",
    "DescribeDBProxyTargetsPaginateResponseTargetsTypeDef",
    "DescribeDBProxyTargetsPaginateResponseTypeDef",
    "DescribeDBSecurityGroupsPaginateFiltersTypeDef",
    "DescribeDBSecurityGroupsPaginatePaginationConfigTypeDef",
    "DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsEC2SecurityGroupsTypeDef",
    "DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsIPRangesTypeDef",
    "DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsTypeDef",
    "DescribeDBSecurityGroupsPaginateResponseTypeDef",
    "DescribeDBSnapshotsPaginateFiltersTypeDef",
    "DescribeDBSnapshotsPaginatePaginationConfigTypeDef",
    "DescribeDBSnapshotsPaginateResponseDBSnapshotsProcessorFeaturesTypeDef",
    "DescribeDBSnapshotsPaginateResponseDBSnapshotsTypeDef",
    "DescribeDBSnapshotsPaginateResponseTypeDef",
    "DescribeDBSubnetGroupsPaginateFiltersTypeDef",
    "DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseTypeDef",
    "DescribeEngineDefaultClusterParametersPaginateFiltersTypeDef",
    "DescribeEngineDefaultClusterParametersPaginatePaginationConfigTypeDef",
    "DescribeEngineDefaultClusterParametersPaginateResponseEngineDefaultsParametersTypeDef",
    "DescribeEngineDefaultClusterParametersPaginateResponseEngineDefaultsTypeDef",
    "DescribeEngineDefaultClusterParametersPaginateResponseTypeDef",
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
    "DescribeGlobalClustersPaginateFiltersTypeDef",
    "DescribeGlobalClustersPaginatePaginationConfigTypeDef",
    "DescribeGlobalClustersPaginateResponseGlobalClustersGlobalClusterMembersTypeDef",
    "DescribeGlobalClustersPaginateResponseGlobalClustersTypeDef",
    "DescribeGlobalClustersPaginateResponseTypeDef",
    "DescribeInstallationMediaPaginateFiltersTypeDef",
    "DescribeInstallationMediaPaginatePaginationConfigTypeDef",
    "DescribeInstallationMediaPaginateResponseInstallationMediaFailureCauseTypeDef",
    "DescribeInstallationMediaPaginateResponseInstallationMediaTypeDef",
    "DescribeInstallationMediaPaginateResponseTypeDef",
    "DescribeOptionGroupOptionsPaginateFiltersTypeDef",
    "DescribeOptionGroupOptionsPaginatePaginationConfigTypeDef",
    "DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef",
    "DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef",
    "DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef",
    "DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsTypeDef",
    "DescribeOptionGroupOptionsPaginateResponseTypeDef",
    "DescribeOptionGroupsPaginateFiltersTypeDef",
    "DescribeOptionGroupsPaginatePaginationConfigTypeDef",
    "DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef",
    "DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsOptionSettingsTypeDef",
    "DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef",
    "DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsTypeDef",
    "DescribeOptionGroupsPaginateResponseOptionGroupsListTypeDef",
    "DescribeOptionGroupsPaginateResponseTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef",
    "DescribePendingMaintenanceActionsPaginateFiltersTypeDef",
    "DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef",
    "DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsTypeDef",
    "DescribePendingMaintenanceActionsPaginateResponseTypeDef",
    "DescribeReservedDBInstancesOfferingsPaginateFiltersTypeDef",
    "DescribeReservedDBInstancesOfferingsPaginatePaginationConfigTypeDef",
    "DescribeReservedDBInstancesOfferingsPaginateResponseReservedDBInstancesOfferingsRecurringChargesTypeDef",
    "DescribeReservedDBInstancesOfferingsPaginateResponseReservedDBInstancesOfferingsTypeDef",
    "DescribeReservedDBInstancesOfferingsPaginateResponseTypeDef",
    "DescribeReservedDBInstancesPaginateFiltersTypeDef",
    "DescribeReservedDBInstancesPaginatePaginationConfigTypeDef",
    "DescribeReservedDBInstancesPaginateResponseReservedDBInstancesRecurringChargesTypeDef",
    "DescribeReservedDBInstancesPaginateResponseReservedDBInstancesTypeDef",
    "DescribeReservedDBInstancesPaginateResponseTypeDef",
    "DescribeSourceRegionsPaginateFiltersTypeDef",
    "DescribeSourceRegionsPaginatePaginationConfigTypeDef",
    "DescribeSourceRegionsPaginateResponseSourceRegionsTypeDef",
    "DescribeSourceRegionsPaginateResponseTypeDef",
    "DownloadDBLogFilePortionPaginatePaginationConfigTypeDef",
    "DownloadDBLogFilePortionPaginateResponseTypeDef",
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

      Contains the results of a successful invocation of the ``DescribeEventSubscriptions`` action.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the RDS event notification subscription.
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

        Contains the results of a successful invocation of the ``DescribeEventSubscriptions``
        action.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the RDS event notification subscription.
    """


_ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsToResourceTagsTypeDef(_ClientAddTagsToResourceTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
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


_ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)


class ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef(
    _ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef
):
    pass


_ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef = TypedDict(
    "_ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef",
    {"Status": str, "CIDRIP": str},
    total=False,
)


class ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef(
    _ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef
):
    pass


_ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef = TypedDict(
    "_ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "VpcId": str,
        "EC2SecurityGroups": List[
            ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[
            ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef
        ],
        "DBSecurityGroupArn": str,
    },
    total=False,
)


class ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef(
    _ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef
):
    """
    - **DBSecurityGroup** *(dict) --*

      Contains the details for an Amazon RDS DB security group.
      This data type is used as a response element in the ``DescribeDBSecurityGroups`` action.
      - **OwnerId** *(string) --*

        Provides the AWS ID of the owner of a specific DB security group.
    """


_ClientAuthorizeDbSecurityGroupIngressResponseTypeDef = TypedDict(
    "_ClientAuthorizeDbSecurityGroupIngressResponseTypeDef",
    {"DBSecurityGroup": ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef},
    total=False,
)


class ClientAuthorizeDbSecurityGroupIngressResponseTypeDef(
    _ClientAuthorizeDbSecurityGroupIngressResponseTypeDef
):
    """
    - *(dict) --*

      - **DBSecurityGroup** *(dict) --*

        Contains the details for an Amazon RDS DB security group.
        This data type is used as a response element in the ``DescribeDBSecurityGroups`` action.
        - **OwnerId** *(string) --*

          Provides the AWS ID of the owner of a specific DB security group.
    """


_ClientBacktrackDbClusterResponseTypeDef = TypedDict(
    "_ClientBacktrackDbClusterResponseTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": str,
        "BacktrackTo": datetime,
        "BacktrackedFrom": datetime,
        "BacktrackRequestCreationTime": datetime,
        "Status": str,
    },
    total=False,
)


class ClientBacktrackDbClusterResponseTypeDef(_ClientBacktrackDbClusterResponseTypeDef):
    """
    - *(dict) --*

      This data type is used as a response element in the ``DescribeDBClusterBacktracks`` action.
      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.
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

      Contains the details of an Amazon RDS DB cluster parameter group.
      This data type is used as a response element in the ``DescribeDBClusterParameterGroups``
      action.
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

        Contains the details of an Amazon RDS DB cluster parameter group.
        This data type is used as a response element in the ``DescribeDBClusterParameterGroups``
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

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
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

      Contains the details for an Amazon RDS DB cluster snapshot
      This data type is used as a response element in the ``DescribeDBClusterSnapshots`` action.
      - **AvailabilityZones** *(list) --*

        Provides the list of Availability Zones (AZs) where instances in the DB cluster snapshot can
        be restored.
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

        Contains the details for an Amazon RDS DB cluster snapshot
        This data type is used as a response element in the ``DescribeDBClusterSnapshots`` action.
        - **AvailabilityZones** *(list) --*

          Provides the list of Availability Zones (AZs) where instances in the DB cluster snapshot
          can be restored.
          - *(string) --*
    """


_ClientCopyDbClusterSnapshotTagsTypeDef = TypedDict(
    "_ClientCopyDbClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCopyDbClusterSnapshotTagsTypeDef(_ClientCopyDbClusterSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
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

      Contains the details of an Amazon RDS DB parameter group.
      This data type is used as a response element in the ``DescribeDBParameterGroups`` action.
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

        Contains the details of an Amazon RDS DB parameter group.
        This data type is used as a response element in the ``DescribeDBParameterGroups`` action.
        - **DBParameterGroupName** *(string) --*

          Provides the name of the DB parameter group.
    """


_ClientCopyDbParameterGroupTagsTypeDef = TypedDict(
    "_ClientCopyDbParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCopyDbParameterGroupTagsTypeDef(_ClientCopyDbParameterGroupTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCopyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef = TypedDict(
    "_ClientCopyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCopyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef(
    _ClientCopyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef
):
    pass


_ClientCopyDbSnapshotResponseDBSnapshotTypeDef = TypedDict(
    "_ClientCopyDbSnapshotResponseDBSnapshotTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List[ClientCopyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef],
        "DbiResourceId": str,
    },
    total=False,
)


class ClientCopyDbSnapshotResponseDBSnapshotTypeDef(_ClientCopyDbSnapshotResponseDBSnapshotTypeDef):
    """
    - **DBSnapshot** *(dict) --*

      Contains the details of an Amazon RDS DB snapshot.
      This data type is used as a response element in the ``DescribeDBSnapshots`` action.
      - **DBSnapshotIdentifier** *(string) --*

        Specifies the identifier for the DB snapshot.
    """


_ClientCopyDbSnapshotResponseTypeDef = TypedDict(
    "_ClientCopyDbSnapshotResponseTypeDef",
    {"DBSnapshot": ClientCopyDbSnapshotResponseDBSnapshotTypeDef},
    total=False,
)


class ClientCopyDbSnapshotResponseTypeDef(_ClientCopyDbSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **DBSnapshot** *(dict) --*

        Contains the details of an Amazon RDS DB snapshot.
        This data type is used as a response element in the ``DescribeDBSnapshots`` action.
        - **DBSnapshotIdentifier** *(string) --*

          Specifies the identifier for the DB snapshot.
    """


_ClientCopyDbSnapshotTagsTypeDef = TypedDict(
    "_ClientCopyDbSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCopyDbSnapshotTagsTypeDef(_ClientCopyDbSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCopyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef = TypedDict(
    "_ClientCopyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientCopyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef(
    _ClientCopyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef
):
    pass


_ClientCopyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef = TypedDict(
    "_ClientCopyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)


class ClientCopyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef(
    _ClientCopyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef
):
    pass


_ClientCopyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef = TypedDict(
    "_ClientCopyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCopyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef(
    _ClientCopyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef
):
    pass


_ClientCopyOptionGroupResponseOptionGroupOptionsTypeDef = TypedDict(
    "_ClientCopyOptionGroupResponseOptionGroupOptionsTypeDef",
    {
        "OptionName": str,
        "OptionDescription": str,
        "Persistent": bool,
        "Permanent": bool,
        "Port": int,
        "OptionVersion": str,
        "OptionSettings": List[
            ClientCopyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef
        ],
        "DBSecurityGroupMemberships": List[
            ClientCopyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef
        ],
        "VpcSecurityGroupMemberships": List[
            ClientCopyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef
        ],
    },
    total=False,
)


class ClientCopyOptionGroupResponseOptionGroupOptionsTypeDef(
    _ClientCopyOptionGroupResponseOptionGroupOptionsTypeDef
):
    pass


_ClientCopyOptionGroupResponseOptionGroupTypeDef = TypedDict(
    "_ClientCopyOptionGroupResponseOptionGroupTypeDef",
    {
        "OptionGroupName": str,
        "OptionGroupDescription": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "Options": List[ClientCopyOptionGroupResponseOptionGroupOptionsTypeDef],
        "AllowsVpcAndNonVpcInstanceMemberships": bool,
        "VpcId": str,
        "OptionGroupArn": str,
    },
    total=False,
)


class ClientCopyOptionGroupResponseOptionGroupTypeDef(
    _ClientCopyOptionGroupResponseOptionGroupTypeDef
):
    """
    - **OptionGroup** *(dict) --*

      - **OptionGroupName** *(string) --*

        Specifies the name of the option group.
    """


_ClientCopyOptionGroupResponseTypeDef = TypedDict(
    "_ClientCopyOptionGroupResponseTypeDef",
    {"OptionGroup": ClientCopyOptionGroupResponseOptionGroupTypeDef},
    total=False,
)


class ClientCopyOptionGroupResponseTypeDef(_ClientCopyOptionGroupResponseTypeDef):
    """
    - *(dict) --*

      - **OptionGroup** *(dict) --*

        - **OptionGroupName** *(string) --*

          Specifies the name of the option group.
    """


_ClientCopyOptionGroupTagsTypeDef = TypedDict(
    "_ClientCopyOptionGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCopyOptionGroupTagsTypeDef(_ClientCopyOptionGroupTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef = TypedDict(
    "_ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef",
    {
        "VpnId": str,
        "VpnTunnelOriginatorIP": str,
        "VpnGatewayIp": str,
        "VpnPSK": str,
        "VpnName": str,
        "VpnState": str,
    },
    total=False,
)


class ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef(
    _ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef
):
    pass


_ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef",
    {
        "CustomAvailabilityZoneId": str,
        "CustomAvailabilityZoneName": str,
        "CustomAvailabilityZoneStatus": str,
        "VpnDetails": ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef,
    },
    total=False,
)


class ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef(
    _ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef
):
    """
    - **CustomAvailabilityZone** *(dict) --*

      A custom Availability Zone (AZ) is an on-premises AZ that is integrated with a VMware vSphere
      cluster.
      For more information about RDS on VMware, see the ` *RDS on VMware User Guide.*
      https://docs.aws.amazon.com/AmazonRDS/latest/RDSonVMwareUserGuide/rds-on-vmware.html`__
      - **CustomAvailabilityZoneId** *(string) --*

        The identifier of the custom AZ.
        Amazon RDS generates a unique identifier when a custom AZ is created.
    """


_ClientCreateCustomAvailabilityZoneResponseTypeDef = TypedDict(
    "_ClientCreateCustomAvailabilityZoneResponseTypeDef",
    {
        "CustomAvailabilityZone": ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef
    },
    total=False,
)


class ClientCreateCustomAvailabilityZoneResponseTypeDef(
    _ClientCreateCustomAvailabilityZoneResponseTypeDef
):
    """
    - *(dict) --*

      - **CustomAvailabilityZone** *(dict) --*

        A custom Availability Zone (AZ) is an on-premises AZ that is integrated with a VMware
        vSphere cluster.
        For more information about RDS on VMware, see the ` *RDS on VMware User Guide.*
        https://docs.aws.amazon.com/AmazonRDS/latest/RDSonVMwareUserGuide/rds-on-vmware.html`__
        - **CustomAvailabilityZoneId** *(string) --*

          The identifier of the custom AZ.
          Amazon RDS generates a unique identifier when a custom AZ is created.
    """


_ClientCreateDbClusterEndpointResponseTypeDef = TypedDict(
    "_ClientCreateDbClusterEndpointResponseTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
    },
    total=False,
)


class ClientCreateDbClusterEndpointResponseTypeDef(_ClientCreateDbClusterEndpointResponseTypeDef):
    """
    - *(dict) --*

      This data type represents the information you need to connect to an Amazon Aurora DB cluster.
      This data type is used as a response element in the following actions:
      * ``CreateDBClusterEndpoint``
      * ``DescribeDBClusterEndpoints``
      * ``ModifyDBClusterEndpoint``
      * ``DeleteDBClusterEndpoint``
      For the data structure that represents Amazon RDS DB instance endpoints, see ``Endpoint`` .
      - **DBClusterEndpointIdentifier** *(string) --*

        The identifier associated with the endpoint. This parameter is stored as a lowercase string.
    """


_ClientCreateDbClusterEndpointTagsTypeDef = TypedDict(
    "_ClientCreateDbClusterEndpointTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbClusterEndpointTagsTypeDef(_ClientCreateDbClusterEndpointTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
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

      Contains the details of an Amazon RDS DB cluster parameter group.
      This data type is used as a response element in the ``DescribeDBClusterParameterGroups``
      action.
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

        Contains the details of an Amazon RDS DB cluster parameter group.
        This data type is used as a response element in the ``DescribeDBClusterParameterGroups``
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

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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


_ClientCreateDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientCreateDbClusterResponseDBClusterScalingConfigurationInfoTypeDef(
    _ClientCreateDbClusterResponseDBClusterScalingConfigurationInfoTypeDef
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientCreateDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)


class ClientCreateDbClusterResponseDBClusterTypeDef(_ClientCreateDbClusterResponseDBClusterTypeDef):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Aurora DB cluster.
      This data type is used as a response element in the ``DescribeDBClusters`` , ``StopDBCluster``
      , and ``StartDBCluster`` actions.
      - **AllocatedStorage** *(integer) --*

        For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the allocated
        storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns 1, because
        Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Aurora DB cluster.
        This data type is used as a response element in the ``DescribeDBClusters`` ,
        ``StopDBCluster`` , and ``StartDBCluster`` actions.
        - **AllocatedStorage** *(integer) --*

          For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the
          allocated storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns
          1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts
          as needed.
    """


_ClientCreateDbClusterScalingConfigurationTypeDef = TypedDict(
    "_ClientCreateDbClusterScalingConfigurationTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientCreateDbClusterScalingConfigurationTypeDef(
    _ClientCreateDbClusterScalingConfigurationTypeDef
):
    """
    For DB clusters in ``serverless`` DB engine mode, the scaling properties of the DB cluster.
    - **MinCapacity** *(integer) --*

      The minimum capacity for an Aurora DB cluster in ``serverless`` DB engine mode.
      For Aurora MySQL, valid capacity values are ``1`` , ``2`` , ``4`` , ``8`` , ``16`` , ``32`` ,
      ``64`` , ``128`` , and ``256`` .
      For Aurora PostgreSQL, valid capacity values are ``2`` , ``4`` , ``8`` , ``16`` , ``32`` ,
      ``64`` , ``192`` , and ``384`` .
      The minimum capacity must be less than or equal to the maximum capacity.
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

      Contains the details for an Amazon RDS DB cluster snapshot
      This data type is used as a response element in the ``DescribeDBClusterSnapshots`` action.
      - **AvailabilityZones** *(list) --*

        Provides the list of Availability Zones (AZs) where instances in the DB cluster snapshot can
        be restored.
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

        Contains the details for an Amazon RDS DB cluster snapshot
        This data type is used as a response element in the ``DescribeDBClusterSnapshots`` action.
        - **AvailabilityZones** *(list) --*

          Provides the list of Availability Zones (AZs) where instances in the DB cluster snapshot
          can be restored.
          - *(string) --*
    """


_ClientCreateDbClusterSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateDbClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbClusterSnapshotTagsTypeDef(_ClientCreateDbClusterSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
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

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbInstanceProcessorFeaturesTypeDef = TypedDict(
    "_ClientCreateDbInstanceProcessorFeaturesTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientCreateDbInstanceProcessorFeaturesTypeDef(
    _ClientCreateDbInstanceProcessorFeaturesTypeDef
):
    """
    - *(dict) --*

      Contains the processor features of a DB instance class.
      To specify the number of CPU cores, use the ``coreCount`` feature name for the ``Name``
      parameter. To specify the number of threads per core, use the ``threadsPerCore`` feature name
      for the ``Name`` parameter.
      You can set the processor features of the DB instance class for a DB instance when you call
      one of the following actions:
      * ``CreateDBInstance``
      * ``ModifyDBInstance``
      * ``RestoreDBInstanceFromDBSnapshot``
      * ``RestoreDBInstanceFromS3``
      * ``RestoreDBInstanceToPointInTime``
      You can view the valid processor values for a particular instance class by calling the
      ``DescribeOrderableDBInstanceOptions`` action and specifying the instance class for the
      ``DBInstanceClass`` parameter.
      In addition, you can use the following actions for DB instance class processor information:
      * ``DescribeDBInstances``
      * ``DescribeDBSnapshots``
      * ``DescribeValidDBInstanceModifications``
      For more information, see `Configuring the Processor of the DB Instance Class
      <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor>`__
      in the *Amazon RDS User Guide.*
      - **Name** *(string) --*

        The name of the processor feature. Valid names are ``coreCount`` and ``threadsPerCore`` .
    """


_ClientCreateDbInstanceReadReplicaProcessorFeaturesTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateDbInstanceReadReplicaProcessorFeaturesTypeDef(
    _ClientCreateDbInstanceReadReplicaProcessorFeaturesTypeDef
):
    """
    - *(dict) --*

      Contains the processor features of a DB instance class.
      To specify the number of CPU cores, use the ``coreCount`` feature name for the ``Name``
      parameter. To specify the number of threads per core, use the ``threadsPerCore`` feature name
      for the ``Name`` parameter.
      You can set the processor features of the DB instance class for a DB instance when you call
      one of the following actions:
      * ``CreateDBInstance``
      * ``ModifyDBInstance``
      * ``RestoreDBInstanceFromDBSnapshot``
      * ``RestoreDBInstanceFromS3``
      * ``RestoreDBInstanceToPointInTime``
      You can view the valid processor values for a particular instance class by calling the
      ``DescribeOrderableDBInstanceOptions`` action and specifying the instance class for the
      ``DBInstanceClass`` parameter.
      In addition, you can use the following actions for DB instance class processor information:
      * ``DescribeDBInstances``
      * ``DescribeDBSnapshots``
      * ``DescribeValidDBInstanceModifications``
      For more information, see `Configuring the Processor of the DB Instance Class
      <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor>`__
      in the *Amazon RDS User Guide.*
      - **Name** *(string) --*

        The name of the processor feature. Valid names are ``coreCount`` and ``threadsPerCore`` .
    """


_ClientCreateDbInstanceReadReplicaResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceAssociatedRolesTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceAssociatedRolesTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceDBParameterGroupsTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceDomainMembershipsTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceDomainMembershipsTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceEndpointTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceEndpointTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceListenerEndpointTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceListenerEndpointTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceProcessorFeaturesTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceProcessorFeaturesTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceStatusInfosTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceStatusInfosTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientCreateDbInstanceReadReplicaResponseDBInstanceTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientCreateDbInstanceReadReplicaResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientCreateDbInstanceReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientCreateDbInstanceReadReplicaResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceDomainMembershipsTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceProcessorFeaturesTypeDef
        ],
        "DeletionProtection": bool,
        "AssociatedRoles": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceAssociatedRolesTypeDef
        ],
        "ListenerEndpoint": ClientCreateDbInstanceReadReplicaResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseDBInstanceTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon RDS DB instance.
      This data type is used as a response element in the ``DescribeDBInstances`` action.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
        identifies a DB instance.
    """


_ClientCreateDbInstanceReadReplicaResponseTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaResponseTypeDef",
    {"DBInstance": ClientCreateDbInstanceReadReplicaResponseDBInstanceTypeDef},
    total=False,
)


class ClientCreateDbInstanceReadReplicaResponseTypeDef(
    _ClientCreateDbInstanceReadReplicaResponseTypeDef
):
    """
    - *(dict) --*

      - **DBInstance** *(dict) --*

        Contains the details of an Amazon RDS DB instance.
        This data type is used as a response element in the ``DescribeDBInstances`` action.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientCreateDbInstanceReadReplicaTagsTypeDef = TypedDict(
    "_ClientCreateDbInstanceReadReplicaTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbInstanceReadReplicaTagsTypeDef(_ClientCreateDbInstanceReadReplicaTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbInstanceResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceAssociatedRolesTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceAssociatedRolesTypeDef
):
    pass


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


_ClientCreateDbInstanceResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceListenerEndpointTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceListenerEndpointTypeDef
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


_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef(
    _ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
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
        "ProcessorFeatures": List[
            ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientCreateDbInstanceResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceProcessorFeaturesTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceProcessorFeaturesTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[ClientCreateDbInstanceResponseDBInstanceProcessorFeaturesTypeDef],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientCreateDbInstanceResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientCreateDbInstanceResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon RDS DB instance.
      This data type is used as a response element in the ``DescribeDBInstances`` action.
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

        Contains the details of an Amazon RDS DB instance.
        This data type is used as a response element in the ``DescribeDBInstances`` action.
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

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
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

      Contains the details of an Amazon RDS DB parameter group.
      This data type is used as a response element in the ``DescribeDBParameterGroups`` action.
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

        Contains the details of an Amazon RDS DB parameter group.
        This data type is used as a response element in the ``DescribeDBParameterGroups`` action.
        - **DBParameterGroupName** *(string) --*

          Provides the name of the DB parameter group.
    """


_ClientCreateDbParameterGroupTagsTypeDef = TypedDict(
    "_ClientCreateDbParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbParameterGroupTagsTypeDef(_ClientCreateDbParameterGroupTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbProxyAuthTypeDef = TypedDict(
    "_ClientCreateDbProxyAuthTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": str,
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)


class ClientCreateDbProxyAuthTypeDef(_ClientCreateDbProxyAuthTypeDef):
    """
    - *(dict) --*

      .. note::

        This is prerelease documentation for the RDS Database Proxy feature in preview release. It
        is subject to change.
    """


_ClientCreateDbProxyResponseDBProxyAuthTypeDef = TypedDict(
    "_ClientCreateDbProxyResponseDBProxyAuthTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": str,
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)


class ClientCreateDbProxyResponseDBProxyAuthTypeDef(_ClientCreateDbProxyResponseDBProxyAuthTypeDef):
    pass


_ClientCreateDbProxyResponseDBProxyTypeDef = TypedDict(
    "_ClientCreateDbProxyResponseDBProxyTypeDef",
    {
        "DBProxyName": str,
        "DBProxyArn": str,
        "Status": Literal[
            "available",
            "modifying",
            "incompatible-network",
            "insufficient-resource-limits",
            "creating",
            "deleting",
        ],
        "EngineFamily": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Auth": List[ClientCreateDbProxyResponseDBProxyAuthTypeDef],
        "RoleArn": str,
        "Endpoint": str,
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)


class ClientCreateDbProxyResponseDBProxyTypeDef(_ClientCreateDbProxyResponseDBProxyTypeDef):
    """
    - **DBProxy** *(dict) --*

      The ``DBProxy`` structure corresponding to the new proxy.
      - **DBProxyName** *(string) --*

        The identifier for the proxy. This name must be unique for all proxies owned by your AWS
        account in the specified AWS Region.
    """


_ClientCreateDbProxyResponseTypeDef = TypedDict(
    "_ClientCreateDbProxyResponseTypeDef",
    {"DBProxy": ClientCreateDbProxyResponseDBProxyTypeDef},
    total=False,
)


class ClientCreateDbProxyResponseTypeDef(_ClientCreateDbProxyResponseTypeDef):
    """
    - *(dict) --*

      - **DBProxy** *(dict) --*

        The ``DBProxy`` structure corresponding to the new proxy.
        - **DBProxyName** *(string) --*

          The identifier for the proxy. This name must be unique for all proxies owned by your AWS
          account in the specified AWS Region.
    """


_ClientCreateDbProxyTagsTypeDef = TypedDict(
    "_ClientCreateDbProxyTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbProxyTagsTypeDef(_ClientCreateDbProxyTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbSecurityGroupResponseDBSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientCreateDbSecurityGroupResponseDBSecurityGroupEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)


class ClientCreateDbSecurityGroupResponseDBSecurityGroupEC2SecurityGroupsTypeDef(
    _ClientCreateDbSecurityGroupResponseDBSecurityGroupEC2SecurityGroupsTypeDef
):
    pass


_ClientCreateDbSecurityGroupResponseDBSecurityGroupIPRangesTypeDef = TypedDict(
    "_ClientCreateDbSecurityGroupResponseDBSecurityGroupIPRangesTypeDef",
    {"Status": str, "CIDRIP": str},
    total=False,
)


class ClientCreateDbSecurityGroupResponseDBSecurityGroupIPRangesTypeDef(
    _ClientCreateDbSecurityGroupResponseDBSecurityGroupIPRangesTypeDef
):
    pass


_ClientCreateDbSecurityGroupResponseDBSecurityGroupTypeDef = TypedDict(
    "_ClientCreateDbSecurityGroupResponseDBSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "VpcId": str,
        "EC2SecurityGroups": List[
            ClientCreateDbSecurityGroupResponseDBSecurityGroupEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[ClientCreateDbSecurityGroupResponseDBSecurityGroupIPRangesTypeDef],
        "DBSecurityGroupArn": str,
    },
    total=False,
)


class ClientCreateDbSecurityGroupResponseDBSecurityGroupTypeDef(
    _ClientCreateDbSecurityGroupResponseDBSecurityGroupTypeDef
):
    """
    - **DBSecurityGroup** *(dict) --*

      Contains the details for an Amazon RDS DB security group.
      This data type is used as a response element in the ``DescribeDBSecurityGroups`` action.
      - **OwnerId** *(string) --*

        Provides the AWS ID of the owner of a specific DB security group.
    """


_ClientCreateDbSecurityGroupResponseTypeDef = TypedDict(
    "_ClientCreateDbSecurityGroupResponseTypeDef",
    {"DBSecurityGroup": ClientCreateDbSecurityGroupResponseDBSecurityGroupTypeDef},
    total=False,
)


class ClientCreateDbSecurityGroupResponseTypeDef(_ClientCreateDbSecurityGroupResponseTypeDef):
    """
    - *(dict) --*

      - **DBSecurityGroup** *(dict) --*

        Contains the details for an Amazon RDS DB security group.
        This data type is used as a response element in the ``DescribeDBSecurityGroups`` action.
        - **OwnerId** *(string) --*

          Provides the AWS ID of the owner of a specific DB security group.
    """


_ClientCreateDbSecurityGroupTagsTypeDef = TypedDict(
    "_ClientCreateDbSecurityGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbSecurityGroupTagsTypeDef(_ClientCreateDbSecurityGroupTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef = TypedDict(
    "_ClientCreateDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef(
    _ClientCreateDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef
):
    pass


_ClientCreateDbSnapshotResponseDBSnapshotTypeDef = TypedDict(
    "_ClientCreateDbSnapshotResponseDBSnapshotTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List[ClientCreateDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef],
        "DbiResourceId": str,
    },
    total=False,
)


class ClientCreateDbSnapshotResponseDBSnapshotTypeDef(
    _ClientCreateDbSnapshotResponseDBSnapshotTypeDef
):
    """
    - **DBSnapshot** *(dict) --*

      Contains the details of an Amazon RDS DB snapshot.
      This data type is used as a response element in the ``DescribeDBSnapshots`` action.
      - **DBSnapshotIdentifier** *(string) --*

        Specifies the identifier for the DB snapshot.
    """


_ClientCreateDbSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateDbSnapshotResponseTypeDef",
    {"DBSnapshot": ClientCreateDbSnapshotResponseDBSnapshotTypeDef},
    total=False,
)


class ClientCreateDbSnapshotResponseTypeDef(_ClientCreateDbSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **DBSnapshot** *(dict) --*

        Contains the details of an Amazon RDS DB snapshot.
        This data type is used as a response element in the ``DescribeDBSnapshots`` action.
        - **DBSnapshotIdentifier** *(string) --*

          Specifies the identifier for the DB snapshot.
    """


_ClientCreateDbSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateDbSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbSnapshotTagsTypeDef(_ClientCreateDbSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
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

      Contains the details of an Amazon RDS DB subnet group.
      This data type is used as a response element in the ``DescribeDBSubnetGroups`` action.
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

        Contains the details of an Amazon RDS DB subnet group.
        This data type is used as a response element in the ``DescribeDBSubnetGroups`` action.
        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.
    """


_ClientCreateDbSubnetGroupTagsTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbSubnetGroupTagsTypeDef(_ClientCreateDbSubnetGroupTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
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

      Contains the results of a successful invocation of the ``DescribeEventSubscriptions`` action.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the RDS event notification subscription.
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

        Contains the results of a successful invocation of the ``DescribeEventSubscriptions``
        action.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the RDS event notification subscription.
    """


_ClientCreateEventSubscriptionTagsTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateEventSubscriptionTagsTypeDef(_ClientCreateEventSubscriptionTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef = TypedDict(
    "_ClientCreateGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    {"DBClusterArn": str, "Readers": List[str], "IsWriter": bool},
    total=False,
)


class ClientCreateGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef(
    _ClientCreateGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef
):
    pass


_ClientCreateGlobalClusterResponseGlobalClusterTypeDef = TypedDict(
    "_ClientCreateGlobalClusterResponseGlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List[
            ClientCreateGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef
        ],
    },
    total=False,
)


class ClientCreateGlobalClusterResponseGlobalClusterTypeDef(
    _ClientCreateGlobalClusterResponseGlobalClusterTypeDef
):
    """
    - **GlobalCluster** *(dict) --*

      A data type representing an Aurora global database.
      - **GlobalClusterIdentifier** *(string) --*

        Contains a user-supplied global database cluster identifier. This identifier is the unique
        key that identifies a global database cluster.
    """


_ClientCreateGlobalClusterResponseTypeDef = TypedDict(
    "_ClientCreateGlobalClusterResponseTypeDef",
    {"GlobalCluster": ClientCreateGlobalClusterResponseGlobalClusterTypeDef},
    total=False,
)


class ClientCreateGlobalClusterResponseTypeDef(_ClientCreateGlobalClusterResponseTypeDef):
    """
    - *(dict) --*

      - **GlobalCluster** *(dict) --*

        A data type representing an Aurora global database.
        - **GlobalClusterIdentifier** *(string) --*

          Contains a user-supplied global database cluster identifier. This identifier is the unique
          key that identifies a global database cluster.
    """


_ClientCreateOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef = TypedDict(
    "_ClientCreateOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientCreateOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef(
    _ClientCreateOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef
):
    pass


_ClientCreateOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef = TypedDict(
    "_ClientCreateOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)


class ClientCreateOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef(
    _ClientCreateOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef
):
    pass


_ClientCreateOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef = TypedDict(
    "_ClientCreateOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCreateOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef(
    _ClientCreateOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef
):
    pass


_ClientCreateOptionGroupResponseOptionGroupOptionsTypeDef = TypedDict(
    "_ClientCreateOptionGroupResponseOptionGroupOptionsTypeDef",
    {
        "OptionName": str,
        "OptionDescription": str,
        "Persistent": bool,
        "Permanent": bool,
        "Port": int,
        "OptionVersion": str,
        "OptionSettings": List[
            ClientCreateOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef
        ],
        "DBSecurityGroupMemberships": List[
            ClientCreateOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef
        ],
        "VpcSecurityGroupMemberships": List[
            ClientCreateOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef
        ],
    },
    total=False,
)


class ClientCreateOptionGroupResponseOptionGroupOptionsTypeDef(
    _ClientCreateOptionGroupResponseOptionGroupOptionsTypeDef
):
    pass


_ClientCreateOptionGroupResponseOptionGroupTypeDef = TypedDict(
    "_ClientCreateOptionGroupResponseOptionGroupTypeDef",
    {
        "OptionGroupName": str,
        "OptionGroupDescription": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "Options": List[ClientCreateOptionGroupResponseOptionGroupOptionsTypeDef],
        "AllowsVpcAndNonVpcInstanceMemberships": bool,
        "VpcId": str,
        "OptionGroupArn": str,
    },
    total=False,
)


class ClientCreateOptionGroupResponseOptionGroupTypeDef(
    _ClientCreateOptionGroupResponseOptionGroupTypeDef
):
    """
    - **OptionGroup** *(dict) --*

      - **OptionGroupName** *(string) --*

        Specifies the name of the option group.
    """


_ClientCreateOptionGroupResponseTypeDef = TypedDict(
    "_ClientCreateOptionGroupResponseTypeDef",
    {"OptionGroup": ClientCreateOptionGroupResponseOptionGroupTypeDef},
    total=False,
)


class ClientCreateOptionGroupResponseTypeDef(_ClientCreateOptionGroupResponseTypeDef):
    """
    - *(dict) --*

      - **OptionGroup** *(dict) --*

        - **OptionGroupName** *(string) --*

          Specifies the name of the option group.
    """


_ClientCreateOptionGroupTagsTypeDef = TypedDict(
    "_ClientCreateOptionGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateOptionGroupTagsTypeDef(_ClientCreateOptionGroupTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef = TypedDict(
    "_ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef",
    {
        "VpnId": str,
        "VpnTunnelOriginatorIP": str,
        "VpnGatewayIp": str,
        "VpnPSK": str,
        "VpnName": str,
        "VpnState": str,
    },
    total=False,
)


class ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef(
    _ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef
):
    pass


_ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef = TypedDict(
    "_ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef",
    {
        "CustomAvailabilityZoneId": str,
        "CustomAvailabilityZoneName": str,
        "CustomAvailabilityZoneStatus": str,
        "VpnDetails": ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef,
    },
    total=False,
)


class ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef(
    _ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef
):
    """
    - **CustomAvailabilityZone** *(dict) --*

      A custom Availability Zone (AZ) is an on-premises AZ that is integrated with a VMware vSphere
      cluster.
      For more information about RDS on VMware, see the ` *RDS on VMware User Guide.*
      https://docs.aws.amazon.com/AmazonRDS/latest/RDSonVMwareUserGuide/rds-on-vmware.html`__
      - **CustomAvailabilityZoneId** *(string) --*

        The identifier of the custom AZ.
        Amazon RDS generates a unique identifier when a custom AZ is created.
    """


_ClientDeleteCustomAvailabilityZoneResponseTypeDef = TypedDict(
    "_ClientDeleteCustomAvailabilityZoneResponseTypeDef",
    {
        "CustomAvailabilityZone": ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef
    },
    total=False,
)


class ClientDeleteCustomAvailabilityZoneResponseTypeDef(
    _ClientDeleteCustomAvailabilityZoneResponseTypeDef
):
    """
    - *(dict) --*

      - **CustomAvailabilityZone** *(dict) --*

        A custom Availability Zone (AZ) is an on-premises AZ that is integrated with a VMware
        vSphere cluster.
        For more information about RDS on VMware, see the ` *RDS on VMware User Guide.*
        https://docs.aws.amazon.com/AmazonRDS/latest/RDSonVMwareUserGuide/rds-on-vmware.html`__
        - **CustomAvailabilityZoneId** *(string) --*

          The identifier of the custom AZ.
          Amazon RDS generates a unique identifier when a custom AZ is created.
    """


_ClientDeleteDbClusterEndpointResponseTypeDef = TypedDict(
    "_ClientDeleteDbClusterEndpointResponseTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
    },
    total=False,
)


class ClientDeleteDbClusterEndpointResponseTypeDef(_ClientDeleteDbClusterEndpointResponseTypeDef):
    """
    - *(dict) --*

      This data type represents the information you need to connect to an Amazon Aurora DB cluster.
      This data type is used as a response element in the following actions:
      * ``CreateDBClusterEndpoint``
      * ``DescribeDBClusterEndpoints``
      * ``ModifyDBClusterEndpoint``
      * ``DeleteDBClusterEndpoint``
      For the data structure that represents Amazon RDS DB instance endpoints, see ``Endpoint`` .
      - **DBClusterEndpointIdentifier** *(string) --*

        The identifier associated with the endpoint. This parameter is stored as a lowercase string.
    """


_ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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


_ClientDeleteDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterScalingConfigurationInfoTypeDef(
    _ClientDeleteDbClusterResponseDBClusterScalingConfigurationInfoTypeDef
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientDeleteDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterTypeDef(_ClientDeleteDbClusterResponseDBClusterTypeDef):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Aurora DB cluster.
      This data type is used as a response element in the ``DescribeDBClusters`` , ``StopDBCluster``
      , and ``StartDBCluster`` actions.
      - **AllocatedStorage** *(integer) --*

        For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the allocated
        storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns 1, because
        Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Aurora DB cluster.
        This data type is used as a response element in the ``DescribeDBClusters`` ,
        ``StopDBCluster`` , and ``StartDBCluster`` actions.
        - **AllocatedStorage** *(integer) --*

          For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the
          allocated storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns
          1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts
          as needed.
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

      Contains the details for an Amazon RDS DB cluster snapshot
      This data type is used as a response element in the ``DescribeDBClusterSnapshots`` action.
      - **AvailabilityZones** *(list) --*

        Provides the list of Availability Zones (AZs) where instances in the DB cluster snapshot can
        be restored.
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

        Contains the details for an Amazon RDS DB cluster snapshot
        This data type is used as a response element in the ``DescribeDBClusterSnapshots`` action.
        - **AvailabilityZones** *(list) --*

          Provides the list of Availability Zones (AZs) where instances in the DB cluster snapshot
          can be restored.
          - *(string) --*
    """


_ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupRestoreWindowTypeDef = TypedDict(
    "_ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupRestoreWindowTypeDef",
    {"EarliestTime": datetime, "LatestTime": datetime},
    total=False,
)


class ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupRestoreWindowTypeDef(
    _ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupRestoreWindowTypeDef
):
    pass


_ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupTypeDef = TypedDict(
    "_ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupTypeDef",
    {
        "DBInstanceArn": str,
        "DbiResourceId": str,
        "Region": str,
        "DBInstanceIdentifier": str,
        "RestoreWindow": ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupRestoreWindowTypeDef,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "Engine": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "StorageType": str,
        "KmsKeyId": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)


class ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupTypeDef(
    _ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupTypeDef
):
    """
    - **DBInstanceAutomatedBackup** *(dict) --*

      An automated backup of a DB instance. It it consists of system backups, transaction logs, and
      the database instance properties that existed at the time you deleted the source instance.
      - **DBInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) for the automated backup.
    """


_ClientDeleteDbInstanceAutomatedBackupResponseTypeDef = TypedDict(
    "_ClientDeleteDbInstanceAutomatedBackupResponseTypeDef",
    {
        "DBInstanceAutomatedBackup": ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupTypeDef
    },
    total=False,
)


class ClientDeleteDbInstanceAutomatedBackupResponseTypeDef(
    _ClientDeleteDbInstanceAutomatedBackupResponseTypeDef
):
    """
    - *(dict) --*

      - **DBInstanceAutomatedBackup** *(dict) --*

        An automated backup of a DB instance. It it consists of system backups, transaction logs,
        and the database instance properties that existed at the time you deleted the source
        instance.
        - **DBInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) for the automated backup.
    """


_ClientDeleteDbInstanceResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceAssociatedRolesTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceAssociatedRolesTypeDef
):
    pass


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


_ClientDeleteDbInstanceResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceListenerEndpointTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceListenerEndpointTypeDef
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


_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef(
    _ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
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
        "ProcessorFeatures": List[
            ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientDeleteDbInstanceResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceProcessorFeaturesTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceProcessorFeaturesTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[ClientDeleteDbInstanceResponseDBInstanceProcessorFeaturesTypeDef],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientDeleteDbInstanceResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientDeleteDbInstanceResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon RDS DB instance.
      This data type is used as a response element in the ``DescribeDBInstances`` action.
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

        Contains the details of an Amazon RDS DB instance.
        This data type is used as a response element in the ``DescribeDBInstances`` action.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientDeleteDbProxyResponseDBProxyAuthTypeDef = TypedDict(
    "_ClientDeleteDbProxyResponseDBProxyAuthTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": str,
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)


class ClientDeleteDbProxyResponseDBProxyAuthTypeDef(_ClientDeleteDbProxyResponseDBProxyAuthTypeDef):
    pass


_ClientDeleteDbProxyResponseDBProxyTypeDef = TypedDict(
    "_ClientDeleteDbProxyResponseDBProxyTypeDef",
    {
        "DBProxyName": str,
        "DBProxyArn": str,
        "Status": Literal[
            "available",
            "modifying",
            "incompatible-network",
            "insufficient-resource-limits",
            "creating",
            "deleting",
        ],
        "EngineFamily": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Auth": List[ClientDeleteDbProxyResponseDBProxyAuthTypeDef],
        "RoleArn": str,
        "Endpoint": str,
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)


class ClientDeleteDbProxyResponseDBProxyTypeDef(_ClientDeleteDbProxyResponseDBProxyTypeDef):
    """
    - **DBProxy** *(dict) --*

      The data structure representing the details of the DB proxy that you delete.
      - **DBProxyName** *(string) --*

        The identifier for the proxy. This name must be unique for all proxies owned by your AWS
        account in the specified AWS Region.
    """


_ClientDeleteDbProxyResponseTypeDef = TypedDict(
    "_ClientDeleteDbProxyResponseTypeDef",
    {"DBProxy": ClientDeleteDbProxyResponseDBProxyTypeDef},
    total=False,
)


class ClientDeleteDbProxyResponseTypeDef(_ClientDeleteDbProxyResponseTypeDef):
    """
    - *(dict) --*

      - **DBProxy** *(dict) --*

        The data structure representing the details of the DB proxy that you delete.
        - **DBProxyName** *(string) --*

          The identifier for the proxy. This name must be unique for all proxies owned by your AWS
          account in the specified AWS Region.
    """


_ClientDeleteDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef = TypedDict(
    "_ClientDeleteDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDeleteDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef(
    _ClientDeleteDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef
):
    pass


_ClientDeleteDbSnapshotResponseDBSnapshotTypeDef = TypedDict(
    "_ClientDeleteDbSnapshotResponseDBSnapshotTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List[ClientDeleteDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef],
        "DbiResourceId": str,
    },
    total=False,
)


class ClientDeleteDbSnapshotResponseDBSnapshotTypeDef(
    _ClientDeleteDbSnapshotResponseDBSnapshotTypeDef
):
    """
    - **DBSnapshot** *(dict) --*

      Contains the details of an Amazon RDS DB snapshot.
      This data type is used as a response element in the ``DescribeDBSnapshots`` action.
      - **DBSnapshotIdentifier** *(string) --*

        Specifies the identifier for the DB snapshot.
    """


_ClientDeleteDbSnapshotResponseTypeDef = TypedDict(
    "_ClientDeleteDbSnapshotResponseTypeDef",
    {"DBSnapshot": ClientDeleteDbSnapshotResponseDBSnapshotTypeDef},
    total=False,
)


class ClientDeleteDbSnapshotResponseTypeDef(_ClientDeleteDbSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **DBSnapshot** *(dict) --*

        Contains the details of an Amazon RDS DB snapshot.
        This data type is used as a response element in the ``DescribeDBSnapshots`` action.
        - **DBSnapshotIdentifier** *(string) --*

          Specifies the identifier for the DB snapshot.
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

      Contains the results of a successful invocation of the ``DescribeEventSubscriptions`` action.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the RDS event notification subscription.
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

        Contains the results of a successful invocation of the ``DescribeEventSubscriptions``
        action.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the RDS event notification subscription.
    """


_ClientDeleteGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef = TypedDict(
    "_ClientDeleteGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    {"DBClusterArn": str, "Readers": List[str], "IsWriter": bool},
    total=False,
)


class ClientDeleteGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef(
    _ClientDeleteGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef
):
    pass


_ClientDeleteGlobalClusterResponseGlobalClusterTypeDef = TypedDict(
    "_ClientDeleteGlobalClusterResponseGlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List[
            ClientDeleteGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef
        ],
    },
    total=False,
)


class ClientDeleteGlobalClusterResponseGlobalClusterTypeDef(
    _ClientDeleteGlobalClusterResponseGlobalClusterTypeDef
):
    """
    - **GlobalCluster** *(dict) --*

      A data type representing an Aurora global database.
      - **GlobalClusterIdentifier** *(string) --*

        Contains a user-supplied global database cluster identifier. This identifier is the unique
        key that identifies a global database cluster.
    """


_ClientDeleteGlobalClusterResponseTypeDef = TypedDict(
    "_ClientDeleteGlobalClusterResponseTypeDef",
    {"GlobalCluster": ClientDeleteGlobalClusterResponseGlobalClusterTypeDef},
    total=False,
)


class ClientDeleteGlobalClusterResponseTypeDef(_ClientDeleteGlobalClusterResponseTypeDef):
    """
    - *(dict) --*

      - **GlobalCluster** *(dict) --*

        A data type representing an Aurora global database.
        - **GlobalClusterIdentifier** *(string) --*

          Contains a user-supplied global database cluster identifier. This identifier is the unique
          key that identifies a global database cluster.
    """


_ClientDeleteInstallationMediaResponseFailureCauseTypeDef = TypedDict(
    "_ClientDeleteInstallationMediaResponseFailureCauseTypeDef", {"Message": str}, total=False
)


class ClientDeleteInstallationMediaResponseFailureCauseTypeDef(
    _ClientDeleteInstallationMediaResponseFailureCauseTypeDef
):
    pass


_ClientDeleteInstallationMediaResponseTypeDef = TypedDict(
    "_ClientDeleteInstallationMediaResponseTypeDef",
    {
        "InstallationMediaId": str,
        "CustomAvailabilityZoneId": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineInstallationMediaPath": str,
        "OSInstallationMediaPath": str,
        "Status": str,
        "FailureCause": ClientDeleteInstallationMediaResponseFailureCauseTypeDef,
    },
    total=False,
)


class ClientDeleteInstallationMediaResponseTypeDef(_ClientDeleteInstallationMediaResponseTypeDef):
    """
    - *(dict) --*

      Contains the installation media for a DB engine that requires an on-premises customer provided
      license, such as Microsoft SQL Server.
      - **InstallationMediaId** *(string) --*

        The installation medium ID.
    """


_ClientDescribeAccountAttributesResponseAccountQuotasTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseAccountQuotasTypeDef",
    {"AccountQuotaName": str, "Used": int, "Max": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseAccountQuotasTypeDef(
    _ClientDescribeAccountAttributesResponseAccountQuotasTypeDef
):
    """
    - *(dict) --*

      Describes a quota for an AWS account.
      The following are account quotas:
      * ``AllocatedStorage`` - The total allocated storage per account, in GiB. The used value is
      the total allocated storage in the account, in GiB.
      * ``AuthorizationsPerDBSecurityGroup`` - The number of ingress rules per DB security group.
      The used value is the highest number of ingress rules in a DB security group in the account.
      Other DB security groups in the account might have a lower number of ingress rules.
      * ``CustomEndpointsPerDBCluster`` - The number of custom endpoints per DB cluster. The used
      value is the highest number of custom endpoints in a DB clusters in the account. Other DB
      clusters in the account might have a lower number of custom endpoints.
      * ``DBClusterParameterGroups`` - The number of DB cluster parameter groups per account,
      excluding default parameter groups. The used value is the count of nondefault DB cluster
      parameter groups in the account.
      * ``DBClusterRoles`` - The number of associated AWS Identity and Access Management (IAM) roles
      per DB cluster. The used value is the highest number of associated IAM roles for a DB cluster
      in the account. Other DB clusters in the account might have a lower number of associated IAM
      roles.
      * ``DBClusters`` - The number of DB clusters per account. The used value is the count of DB
      clusters in the account.
      * ``DBInstanceRoles`` - The number of associated IAM roles per DB instance. The used value is
      the highest number of associated IAM roles for a DB instance in the account. Other DB
      instances in the account might have a lower number of associated IAM roles.
      * ``DBInstances`` - The number of DB instances per account. The used value is the count of the
      DB instances in the account.
      * ``DBParameterGroups`` - The number of DB parameter groups per account, excluding default
      parameter groups. The used value is the count of nondefault DB parameter groups in the
      account.
      * ``DBSecurityGroups`` - The number of DB security groups (not VPC security groups) per
      account, excluding the default security group. The used value is the count of nondefault DB
      security groups in the account.
      * ``DBSubnetGroups`` - The number of DB subnet groups per account. The used value is the count
      of the DB subnet groups in the account.
      * ``EventSubscriptions`` - The number of event subscriptions per account. The used value is
      the count of the event subscriptions in the account.
      * ``ManualSnapshots`` - The number of manual DB snapshots per account. The used value is the
      count of the manual DB snapshots in the account.
      * ``OptionGroups`` - The number of DB option groups per account, excluding default option
      groups. The used value is the count of nondefault DB option groups in the account.
      * ``ReadReplicasPerMaster`` - The number of Read Replicas per DB instance. The used value is
      the highest number of Read Replicas for a DB instance in the account. Other DB instances in
      the account might have a lower number of Read Replicas.
      * ``ReservedDBInstances`` - The number of reserved DB instances per account. The used value is
      the count of the active reserved DB instances in the account.
      * ``SubnetsPerDBSubnetGroup`` - The number of subnets per DB subnet group. The used value is
      highest number of subnets for a DB subnet group in the account. Other DB subnet groups in the
      account might have a lower number of subnets.
      For more information, see `Limits
      <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html>`__ in the *Amazon
      RDS User Guide* and `Limits
      <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.html>`__ in the
      *Amazon Aurora User Guide* .
      - **AccountQuotaName** *(string) --*

        The name of the Amazon RDS quota for this AWS account.
    """


_ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseTypeDef",
    {"AccountQuotas": List[ClientDescribeAccountAttributesResponseAccountQuotasTypeDef]},
    total=False,
)


class ClientDescribeAccountAttributesResponseTypeDef(
    _ClientDescribeAccountAttributesResponseTypeDef
):
    """
    - *(dict) --*

      Data returned by the **DescribeAccountAttributes** action.
      - **AccountQuotas** *(list) --*

        A list of ``AccountQuota`` objects. Within this list, each quota has a name, a count of
        usage toward the quota maximum, and a maximum value for the quota.
        - *(dict) --*

          Describes a quota for an AWS account.
          The following are account quotas:
          * ``AllocatedStorage`` - The total allocated storage per account, in GiB. The used value
          is the total allocated storage in the account, in GiB.
          * ``AuthorizationsPerDBSecurityGroup`` - The number of ingress rules per DB security
          group. The used value is the highest number of ingress rules in a DB security group in the
          account. Other DB security groups in the account might have a lower number of ingress
          rules.
          * ``CustomEndpointsPerDBCluster`` - The number of custom endpoints per DB cluster. The
          used value is the highest number of custom endpoints in a DB clusters in the account.
          Other DB clusters in the account might have a lower number of custom endpoints.
          * ``DBClusterParameterGroups`` - The number of DB cluster parameter groups per account,
          excluding default parameter groups. The used value is the count of nondefault DB cluster
          parameter groups in the account.
          * ``DBClusterRoles`` - The number of associated AWS Identity and Access Management (IAM)
          roles per DB cluster. The used value is the highest number of associated IAM roles for a
          DB cluster in the account. Other DB clusters in the account might have a lower number of
          associated IAM roles.
          * ``DBClusters`` - The number of DB clusters per account. The used value is the count of
          DB clusters in the account.
          * ``DBInstanceRoles`` - The number of associated IAM roles per DB instance. The used value
          is the highest number of associated IAM roles for a DB instance in the account. Other DB
          instances in the account might have a lower number of associated IAM roles.
          * ``DBInstances`` - The number of DB instances per account. The used value is the count of
          the DB instances in the account.
          * ``DBParameterGroups`` - The number of DB parameter groups per account, excluding default
          parameter groups. The used value is the count of nondefault DB parameter groups in the
          account.
          * ``DBSecurityGroups`` - The number of DB security groups (not VPC security groups) per
          account, excluding the default security group. The used value is the count of nondefault
          DB security groups in the account.
          * ``DBSubnetGroups`` - The number of DB subnet groups per account. The used value is the
          count of the DB subnet groups in the account.
          * ``EventSubscriptions`` - The number of event subscriptions per account. The used value
          is the count of the event subscriptions in the account.
          * ``ManualSnapshots`` - The number of manual DB snapshots per account. The used value is
          the count of the manual DB snapshots in the account.
          * ``OptionGroups`` - The number of DB option groups per account, excluding default option
          groups. The used value is the count of nondefault DB option groups in the account.
          * ``ReadReplicasPerMaster`` - The number of Read Replicas per DB instance. The used value
          is the highest number of Read Replicas for a DB instance in the account. Other DB
          instances in the account might have a lower number of Read Replicas.
          * ``ReservedDBInstances`` - The number of reserved DB instances per account. The used
          value is the count of the active reserved DB instances in the account.
          * ``SubnetsPerDBSubnetGroup`` - The number of subnets per DB subnet group. The used value
          is highest number of subnets for a DB subnet group in the account. Other DB subnet groups
          in the account might have a lower number of subnets.
          For more information, see `Limits
          <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html>`__ in the
          *Amazon RDS User Guide* and `Limits
          <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.html>`__ in the
          *Amazon Aurora User Guide* .
          - **AccountQuotaName** *(string) --*

            The name of the Amazon RDS quota for this AWS account.
    """


_ClientDescribeCertificatesFiltersTypeDef = TypedDict(
    "_ClientDescribeCertificatesFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeCertificatesFiltersTypeDef(_ClientDescribeCertificatesFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      A CA certificate for an AWS account.
      - **CertificateIdentifier** *(string) --*

        The unique key that identifies a certificate.
    """


_ClientDescribeCertificatesResponseTypeDef = TypedDict(
    "_ClientDescribeCertificatesResponseTypeDef",
    {"Certificates": List[ClientDescribeCertificatesResponseCertificatesTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeCertificatesResponseTypeDef(_ClientDescribeCertificatesResponseTypeDef):
    """
    - *(dict) --*

      Data returned by the **DescribeCertificates** action.
      - **Certificates** *(list) --*

        The list of ``Certificate`` objects for the AWS account.
        - *(dict) --*

          A CA certificate for an AWS account.
          - **CertificateIdentifier** *(string) --*

            The unique key that identifies a certificate.
    """


_ClientDescribeCustomAvailabilityZonesFiltersTypeDef = TypedDict(
    "_ClientDescribeCustomAvailabilityZonesFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeCustomAvailabilityZonesFiltersTypeDef(
    _ClientDescribeCustomAvailabilityZonesFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesVpnDetailsTypeDef = TypedDict(
    "_ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesVpnDetailsTypeDef",
    {
        "VpnId": str,
        "VpnTunnelOriginatorIP": str,
        "VpnGatewayIp": str,
        "VpnPSK": str,
        "VpnName": str,
        "VpnState": str,
    },
    total=False,
)


class ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesVpnDetailsTypeDef(
    _ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesVpnDetailsTypeDef
):
    pass


_ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesTypeDef = TypedDict(
    "_ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesTypeDef",
    {
        "CustomAvailabilityZoneId": str,
        "CustomAvailabilityZoneName": str,
        "CustomAvailabilityZoneStatus": str,
        "VpnDetails": ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesVpnDetailsTypeDef,
    },
    total=False,
)


class ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesTypeDef(
    _ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesTypeDef
):
    pass


_ClientDescribeCustomAvailabilityZonesResponseTypeDef = TypedDict(
    "_ClientDescribeCustomAvailabilityZonesResponseTypeDef",
    {
        "Marker": str,
        "CustomAvailabilityZones": List[
            ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCustomAvailabilityZonesResponseTypeDef(
    _ClientDescribeCustomAvailabilityZonesResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous ``DescribeCustomAvailabilityZones``
        request. If this parameter is specified, the response includes only records beyond the
        marker, up to the value specified by ``MaxRecords`` .
    """


_ClientDescribeDbClusterBacktracksFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClusterBacktracksFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeDbClusterBacktracksFiltersTypeDef(
    _ClientDescribeDbClusterBacktracksFiltersTypeDef
):
    pass


_ClientDescribeDbClusterBacktracksResponseDBClusterBacktracksTypeDef = TypedDict(
    "_ClientDescribeDbClusterBacktracksResponseDBClusterBacktracksTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": str,
        "BacktrackTo": datetime,
        "BacktrackedFrom": datetime,
        "BacktrackRequestCreationTime": datetime,
        "Status": str,
    },
    total=False,
)


class ClientDescribeDbClusterBacktracksResponseDBClusterBacktracksTypeDef(
    _ClientDescribeDbClusterBacktracksResponseDBClusterBacktracksTypeDef
):
    pass


_ClientDescribeDbClusterBacktracksResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterBacktracksResponseTypeDef",
    {
        "Marker": str,
        "DBClusterBacktracks": List[
            ClientDescribeDbClusterBacktracksResponseDBClusterBacktracksTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbClusterBacktracksResponseTypeDef(
    _ClientDescribeDbClusterBacktracksResponseTypeDef
):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeDBClusterBacktracks`` action.
      - **Marker** *(string) --*

        A pagination token that can be used in a subsequent ``DescribeDBClusterBacktracks`` request.
    """


_ClientDescribeDbClusterEndpointsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClusterEndpointsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeDbClusterEndpointsFiltersTypeDef(
    _ClientDescribeDbClusterEndpointsFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeDbClusterEndpointsResponseDBClusterEndpointsTypeDef = TypedDict(
    "_ClientDescribeDbClusterEndpointsResponseDBClusterEndpointsTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
    },
    total=False,
)


class ClientDescribeDbClusterEndpointsResponseDBClusterEndpointsTypeDef(
    _ClientDescribeDbClusterEndpointsResponseDBClusterEndpointsTypeDef
):
    pass


_ClientDescribeDbClusterEndpointsResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterEndpointsResponseTypeDef",
    {
        "Marker": str,
        "DBClusterEndpoints": List[
            ClientDescribeDbClusterEndpointsResponseDBClusterEndpointsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbClusterEndpointsResponseTypeDef(
    _ClientDescribeDbClusterEndpointsResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous ``DescribeDBClusterEndpoints`` request.
        If this parameter is specified, the response includes only records beyond the marker, up to
        the value specified by ``MaxRecords`` .
    """


_ClientDescribeDbClusterParameterGroupsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClusterParameterGroupsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeDbClusterParameterGroupsFiltersTypeDef(
    _ClientDescribeDbClusterParameterGroupsFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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


_ClientDescribeDbClusterParametersFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClusterParametersFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeDbClusterParametersFiltersTypeDef(
    _ClientDescribeDbClusterParametersFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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
        "SupportedEngineModes": List[str],
    },
    total=False,
)


class ClientDescribeDbClusterParametersResponseParametersTypeDef(
    _ClientDescribeDbClusterParametersResponseParametersTypeDef
):
    """
    - *(dict) --*

      This data type is used as a request parameter in the ``ModifyDBParameterGroup`` and
      ``ResetDBParameterGroup`` actions.
      This data type is used as a response element in the ``DescribeEngineDefaultParameters`` and
      ``DescribeDBParameters`` actions.
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

      Provides details about a DB cluster parameter group including the parameters in the DB cluster
      parameter group.
      - **Parameters** *(list) --*

        Provides a list of parameters for the DB cluster parameter group.
        - *(dict) --*

          This data type is used as a request parameter in the ``ModifyDBParameterGroup`` and
          ``ResetDBParameterGroup`` actions.
          This data type is used as a response element in the ``DescribeEngineDefaultParameters``
          and ``DescribeDBParameters`` actions.
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

      Contains the results of a successful call to the ``DescribeDBClusterSnapshotAttributes`` API
      action.
      Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or
      restore a manual DB cluster snapshot. For more information, see the
      ``ModifyDBClusterSnapshotAttribute`` API action.
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

        Contains the results of a successful call to the ``DescribeDBClusterSnapshotAttributes`` API
        action.
        Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or
        restore a manual DB cluster snapshot. For more information, see the
        ``ModifyDBClusterSnapshotAttribute`` API action.
        - **DBClusterSnapshotIdentifier** *(string) --*

          The identifier of the manual DB cluster snapshot that the attributes apply to.
    """


_ClientDescribeDbClusterSnapshotsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeDbClusterSnapshotsFiltersTypeDef(
    _ClientDescribeDbClusterSnapshotsFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      Provides a list of DB cluster snapshots for the user as the result of a call to the
      ``DescribeDBClusterSnapshots`` action.
      - **Marker** *(string) --*

        An optional pagination token provided by a previous ``DescribeDBClusterSnapshots`` request.
        If this parameter is specified, the response includes only records beyond the marker, up to
        the value specified by ``MaxRecords`` .
    """


_ClientDescribeDbClustersFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClustersFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeDbClustersFiltersTypeDef(_ClientDescribeDbClustersFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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


_ClientDescribeDbClustersResponseDBClustersScalingConfigurationInfoTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersScalingConfigurationInfoTypeDef(
    _ClientDescribeDbClustersResponseDBClustersScalingConfigurationInfoTypeDef
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientDescribeDbClustersResponseDBClustersScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
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

      Contains the result of a successful invocation of the ``DescribeDBClusters`` action.
      - **Marker** *(string) --*

        A pagination token that can be used in a subsequent DescribeDBClusters request.
    """


_ClientDescribeDbEngineVersionsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeDbEngineVersionsFiltersTypeDef(_ClientDescribeDbEngineVersionsFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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
        "SupportedEngineModes": List[str],
        "SupportedFeatureNames": List[str],
        "Status": str,
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

      Contains the result of a successful invocation of the ``DescribeDBEngineVersions`` action.
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_ClientDescribeDbInstanceAutomatedBackupsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbInstanceAutomatedBackupsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeDbInstanceAutomatedBackupsFiltersTypeDef(
    _ClientDescribeDbInstanceAutomatedBackupsFiltersTypeDef
):
    pass


_ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef = TypedDict(
    "_ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef",
    {"EarliestTime": datetime, "LatestTime": datetime},
    total=False,
)


class ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef(
    _ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef
):
    pass


_ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsTypeDef = TypedDict(
    "_ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsTypeDef",
    {
        "DBInstanceArn": str,
        "DbiResourceId": str,
        "Region": str,
        "DBInstanceIdentifier": str,
        "RestoreWindow": ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "Engine": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "StorageType": str,
        "KmsKeyId": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)


class ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsTypeDef(
    _ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsTypeDef
):
    pass


_ClientDescribeDbInstanceAutomatedBackupsResponseTypeDef = TypedDict(
    "_ClientDescribeDbInstanceAutomatedBackupsResponseTypeDef",
    {
        "Marker": str,
        "DBInstanceAutomatedBackups": List[
            ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbInstanceAutomatedBackupsResponseTypeDef(
    _ClientDescribeDbInstanceAutomatedBackupsResponseTypeDef
):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeDBInstanceAutomatedBackups``
      action.
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_ClientDescribeDbInstancesFiltersTypeDef = TypedDict(
    "_ClientDescribeDbInstancesFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeDbInstancesFiltersTypeDef(_ClientDescribeDbInstancesFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeDbInstancesResponseDBInstancesAssociatedRolesTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesAssociatedRolesTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesAssociatedRolesTypeDef
):
    pass


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


_ClientDescribeDbInstancesResponseDBInstancesListenerEndpointTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesListenerEndpointTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesListenerEndpointTypeDef
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


_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef
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
        "ProcessorFeatures": List[
            ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef
):
    pass


_ClientDescribeDbInstancesResponseDBInstancesProcessorFeaturesTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesProcessorFeaturesTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesProcessorFeaturesTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[
            ClientDescribeDbInstancesResponseDBInstancesProcessorFeaturesTypeDef
        ],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientDescribeDbInstancesResponseDBInstancesAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientDescribeDbInstancesResponseDBInstancesListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
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

      Contains the result of a successful invocation of the ``DescribeDBInstances`` action.
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_ClientDescribeDbLogFilesFiltersTypeDef = TypedDict(
    "_ClientDescribeDbLogFilesFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeDbLogFilesFiltersTypeDef(_ClientDescribeDbLogFilesFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeDbLogFilesResponseDescribeDBLogFilesTypeDef = TypedDict(
    "_ClientDescribeDbLogFilesResponseDescribeDBLogFilesTypeDef",
    {"LogFileName": str, "LastWritten": int, "Size": int},
    total=False,
)


class ClientDescribeDbLogFilesResponseDescribeDBLogFilesTypeDef(
    _ClientDescribeDbLogFilesResponseDescribeDBLogFilesTypeDef
):
    """
    - *(dict) --*

      This data type is used as a response element to ``DescribeDBLogFiles`` .
      - **LogFileName** *(string) --*

        The name of the log file for the specified DB instance.
    """


_ClientDescribeDbLogFilesResponseTypeDef = TypedDict(
    "_ClientDescribeDbLogFilesResponseTypeDef",
    {
        "DescribeDBLogFiles": List[ClientDescribeDbLogFilesResponseDescribeDBLogFilesTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeDbLogFilesResponseTypeDef(_ClientDescribeDbLogFilesResponseTypeDef):
    """
    - *(dict) --*

      The response from a call to ``DescribeDBLogFiles`` .
      - **DescribeDBLogFiles** *(list) --*

        The DB log files returned.
        - *(dict) --*

          This data type is used as a response element to ``DescribeDBLogFiles`` .
          - **LogFileName** *(string) --*

            The name of the log file for the specified DB instance.
    """


_ClientDescribeDbParameterGroupsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbParameterGroupsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeDbParameterGroupsFiltersTypeDef(_ClientDescribeDbParameterGroupsFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      Contains the result of a successful invocation of the ``DescribeDBParameterGroups`` action.
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_ClientDescribeDbParametersFiltersTypeDef = TypedDict(
    "_ClientDescribeDbParametersFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeDbParametersFiltersTypeDef(_ClientDescribeDbParametersFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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
        "SupportedEngineModes": List[str],
    },
    total=False,
)


class ClientDescribeDbParametersResponseParametersTypeDef(
    _ClientDescribeDbParametersResponseParametersTypeDef
):
    """
    - *(dict) --*

      This data type is used as a request parameter in the ``ModifyDBParameterGroup`` and
      ``ResetDBParameterGroup`` actions.
      This data type is used as a response element in the ``DescribeEngineDefaultParameters`` and
      ``DescribeDBParameters`` actions.
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

      Contains the result of a successful invocation of the ``DescribeDBParameters`` action.
      - **Parameters** *(list) --*

        A list of ``Parameter`` values.
        - *(dict) --*

          This data type is used as a request parameter in the ``ModifyDBParameterGroup`` and
          ``ResetDBParameterGroup`` actions.
          This data type is used as a response element in the ``DescribeEngineDefaultParameters``
          and ``DescribeDBParameters`` actions.
          - **ParameterName** *(string) --*

            Specifies the name of the parameter.
    """


_ClientDescribeDbProxiesFiltersTypeDef = TypedDict(
    "_ClientDescribeDbProxiesFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeDbProxiesFiltersTypeDef(_ClientDescribeDbProxiesFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeDbProxiesResponseDBProxiesAuthTypeDef = TypedDict(
    "_ClientDescribeDbProxiesResponseDBProxiesAuthTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": str,
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)


class ClientDescribeDbProxiesResponseDBProxiesAuthTypeDef(
    _ClientDescribeDbProxiesResponseDBProxiesAuthTypeDef
):
    pass


_ClientDescribeDbProxiesResponseDBProxiesTypeDef = TypedDict(
    "_ClientDescribeDbProxiesResponseDBProxiesTypeDef",
    {
        "DBProxyName": str,
        "DBProxyArn": str,
        "Status": Literal[
            "available",
            "modifying",
            "incompatible-network",
            "insufficient-resource-limits",
            "creating",
            "deleting",
        ],
        "EngineFamily": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Auth": List[ClientDescribeDbProxiesResponseDBProxiesAuthTypeDef],
        "RoleArn": str,
        "Endpoint": str,
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)


class ClientDescribeDbProxiesResponseDBProxiesTypeDef(
    _ClientDescribeDbProxiesResponseDBProxiesTypeDef
):
    """
    - *(dict) --*

      .. note::

        This is prerelease documentation for the RDS Database Proxy feature in preview release. It
        is subject to change.
    """


_ClientDescribeDbProxiesResponseTypeDef = TypedDict(
    "_ClientDescribeDbProxiesResponseTypeDef",
    {"DBProxies": List[ClientDescribeDbProxiesResponseDBProxiesTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeDbProxiesResponseTypeDef(_ClientDescribeDbProxiesResponseTypeDef):
    """
    - *(dict) --*

      - **DBProxies** *(list) --*

        A return value representing an arbitrary number of ``DBProxy`` data structures.
        - *(dict) --*

          .. note::

            This is prerelease documentation for the RDS Database Proxy feature in preview release.
            It is subject to change.
    """


_ClientDescribeDbProxyTargetGroupsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbProxyTargetGroupsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeDbProxyTargetGroupsFiltersTypeDef(
    _ClientDescribeDbProxyTargetGroupsFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeDbProxyTargetGroupsResponseTargetGroupsConnectionPoolConfigTypeDef = TypedDict(
    "_ClientDescribeDbProxyTargetGroupsResponseTargetGroupsConnectionPoolConfigTypeDef",
    {
        "MaxConnectionsPercent": int,
        "MaxIdleConnectionsPercent": int,
        "ConnectionBorrowTimeout": int,
        "SessionPinningFilters": List[str],
        "InitQuery": str,
    },
    total=False,
)


class ClientDescribeDbProxyTargetGroupsResponseTargetGroupsConnectionPoolConfigTypeDef(
    _ClientDescribeDbProxyTargetGroupsResponseTargetGroupsConnectionPoolConfigTypeDef
):
    pass


_ClientDescribeDbProxyTargetGroupsResponseTargetGroupsTypeDef = TypedDict(
    "_ClientDescribeDbProxyTargetGroupsResponseTargetGroupsTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": str,
        "TargetGroupArn": str,
        "IsDefault": bool,
        "Status": str,
        "ConnectionPoolConfig": ClientDescribeDbProxyTargetGroupsResponseTargetGroupsConnectionPoolConfigTypeDef,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)


class ClientDescribeDbProxyTargetGroupsResponseTargetGroupsTypeDef(
    _ClientDescribeDbProxyTargetGroupsResponseTargetGroupsTypeDef
):
    """
    - *(dict) --*

      .. note::

        This is prerelease documentation for the RDS Database Proxy feature in preview release. It
        is subject to change.
    """


_ClientDescribeDbProxyTargetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeDbProxyTargetGroupsResponseTypeDef",
    {
        "TargetGroups": List[ClientDescribeDbProxyTargetGroupsResponseTargetGroupsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeDbProxyTargetGroupsResponseTypeDef(
    _ClientDescribeDbProxyTargetGroupsResponseTypeDef
):
    """
    - *(dict) --*

      - **TargetGroups** *(list) --*

        An arbitrary number of ``DBProxyTargetGroup`` objects, containing details of the
        corresponding target groups.
        - *(dict) --*

          .. note::

            This is prerelease documentation for the RDS Database Proxy feature in preview release.
            It is subject to change.
    """


_ClientDescribeDbProxyTargetsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbProxyTargetsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeDbProxyTargetsFiltersTypeDef(_ClientDescribeDbProxyTargetsFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeDbProxyTargetsResponseTargetsTypeDef = TypedDict(
    "_ClientDescribeDbProxyTargetsResponseTargetsTypeDef",
    {
        "TargetArn": str,
        "Endpoint": str,
        "TrackedClusterId": str,
        "RdsResourceId": str,
        "Port": int,
        "Type": Literal["RDS_INSTANCE", "RDS_SERVERLESS_ENDPOINT", "TRACKED_CLUSTER"],
    },
    total=False,
)


class ClientDescribeDbProxyTargetsResponseTargetsTypeDef(
    _ClientDescribeDbProxyTargetsResponseTargetsTypeDef
):
    """
    - *(dict) --*

      .. note::

        This is prerelease documentation for the RDS Database Proxy feature in preview release. It
        is subject to change.
    """


_ClientDescribeDbProxyTargetsResponseTypeDef = TypedDict(
    "_ClientDescribeDbProxyTargetsResponseTypeDef",
    {"Targets": List[ClientDescribeDbProxyTargetsResponseTargetsTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeDbProxyTargetsResponseTypeDef(_ClientDescribeDbProxyTargetsResponseTypeDef):
    """
    - *(dict) --*

      - **Targets** *(list) --*

        An arbitrary number of ``DBProxyTarget`` objects, containing details of the corresponding
        targets.
        - *(dict) --*

          .. note::

            This is prerelease documentation for the RDS Database Proxy feature in preview release.
            It is subject to change.
    """


_ClientDescribeDbSecurityGroupsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbSecurityGroupsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeDbSecurityGroupsFiltersTypeDef(_ClientDescribeDbSecurityGroupsFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)


class ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsEC2SecurityGroupsTypeDef(
    _ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsEC2SecurityGroupsTypeDef
):
    pass


_ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsIPRangesTypeDef = TypedDict(
    "_ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsIPRangesTypeDef",
    {"Status": str, "CIDRIP": str},
    total=False,
)


class ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsIPRangesTypeDef(
    _ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsIPRangesTypeDef
):
    pass


_ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsTypeDef",
    {
        "OwnerId": str,
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "VpcId": str,
        "EC2SecurityGroups": List[
            ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsIPRangesTypeDef],
        "DBSecurityGroupArn": str,
    },
    total=False,
)


class ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsTypeDef(
    _ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsTypeDef
):
    pass


_ClientDescribeDbSecurityGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeDbSecurityGroupsResponseTypeDef",
    {
        "Marker": str,
        "DBSecurityGroups": List[ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsTypeDef],
    },
    total=False,
)


class ClientDescribeDbSecurityGroupsResponseTypeDef(_ClientDescribeDbSecurityGroupsResponseTypeDef):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeDBSecurityGroups`` action.
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef = TypedDict(
    "_ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef",
    {"AttributeName": str, "AttributeValues": List[str]},
    total=False,
)


class ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef(
    _ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef
):
    pass


_ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultTypeDef = TypedDict(
    "_ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBSnapshotAttributes": List[
            ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultTypeDef(
    _ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultTypeDef
):
    """
    - **DBSnapshotAttributesResult** *(dict) --*

      Contains the results of a successful call to the ``DescribeDBSnapshotAttributes`` API action.
      Manual DB snapshot attributes are used to authorize other AWS accounts to copy or restore a
      manual DB snapshot. For more information, see the ``ModifyDBSnapshotAttribute`` API action.
      - **DBSnapshotIdentifier** *(string) --*

        The identifier of the manual DB snapshot that the attributes apply to.
    """


_ClientDescribeDbSnapshotAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeDbSnapshotAttributesResponseTypeDef",
    {
        "DBSnapshotAttributesResult": ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultTypeDef
    },
    total=False,
)


class ClientDescribeDbSnapshotAttributesResponseTypeDef(
    _ClientDescribeDbSnapshotAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **DBSnapshotAttributesResult** *(dict) --*

        Contains the results of a successful call to the ``DescribeDBSnapshotAttributes`` API
        action.
        Manual DB snapshot attributes are used to authorize other AWS accounts to copy or restore a
        manual DB snapshot. For more information, see the ``ModifyDBSnapshotAttribute`` API action.
        - **DBSnapshotIdentifier** *(string) --*

          The identifier of the manual DB snapshot that the attributes apply to.
    """


_ClientDescribeDbSnapshotsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbSnapshotsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeDbSnapshotsFiltersTypeDef(_ClientDescribeDbSnapshotsFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeDbSnapshotsResponseDBSnapshotsProcessorFeaturesTypeDef = TypedDict(
    "_ClientDescribeDbSnapshotsResponseDBSnapshotsProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeDbSnapshotsResponseDBSnapshotsProcessorFeaturesTypeDef(
    _ClientDescribeDbSnapshotsResponseDBSnapshotsProcessorFeaturesTypeDef
):
    pass


_ClientDescribeDbSnapshotsResponseDBSnapshotsTypeDef = TypedDict(
    "_ClientDescribeDbSnapshotsResponseDBSnapshotsTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List[
            ClientDescribeDbSnapshotsResponseDBSnapshotsProcessorFeaturesTypeDef
        ],
        "DbiResourceId": str,
    },
    total=False,
)


class ClientDescribeDbSnapshotsResponseDBSnapshotsTypeDef(
    _ClientDescribeDbSnapshotsResponseDBSnapshotsTypeDef
):
    pass


_ClientDescribeDbSnapshotsResponseTypeDef = TypedDict(
    "_ClientDescribeDbSnapshotsResponseTypeDef",
    {"Marker": str, "DBSnapshots": List[ClientDescribeDbSnapshotsResponseDBSnapshotsTypeDef]},
    total=False,
)


class ClientDescribeDbSnapshotsResponseTypeDef(_ClientDescribeDbSnapshotsResponseTypeDef):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeDBSnapshots`` action.
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_ClientDescribeDbSubnetGroupsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeDbSubnetGroupsFiltersTypeDef(_ClientDescribeDbSubnetGroupsFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      Contains the result of a successful invocation of the ``DescribeDBSubnetGroups`` action.
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_ClientDescribeEngineDefaultClusterParametersFiltersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultClusterParametersFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeEngineDefaultClusterParametersFiltersTypeDef(
    _ClientDescribeEngineDefaultClusterParametersFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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
        "SupportedEngineModes": List[str],
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

      Contains the result of a successful invocation of the ``DescribeEngineDefaultParameters``
      action.
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

        Contains the result of a successful invocation of the ``DescribeEngineDefaultParameters``
        action.
        - **DBParameterGroupFamily** *(string) --*

          Specifies the name of the DB parameter group family that the engine default parameters
          apply to.
    """


_ClientDescribeEngineDefaultParametersFiltersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeEngineDefaultParametersFiltersTypeDef(
    _ClientDescribeEngineDefaultParametersFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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
        "SupportedEngineModes": List[str],
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

      Contains the result of a successful invocation of the ``DescribeEngineDefaultParameters``
      action.
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

        Contains the result of a successful invocation of the ``DescribeEngineDefaultParameters``
        action.
        - **DBParameterGroupFamily** *(string) --*

          Specifies the name of the DB parameter group family that the engine default parameters
          apply to.
    """


_ClientDescribeEventCategoriesFiltersTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeEventCategoriesFiltersTypeDef(_ClientDescribeEventCategoriesFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      Contains the results of a successful invocation of the ``DescribeEventCategories`` action.
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

      Data returned from the **DescribeEventCategories** action.
      - **EventCategoriesMapList** *(list) --*

        A list of EventCategoriesMap data types.
        - *(dict) --*

          Contains the results of a successful invocation of the ``DescribeEventCategories`` action.
          - **SourceType** *(string) --*

            The source type that the returned categories belong to
    """


_ClientDescribeEventSubscriptionsFiltersTypeDef = TypedDict(
    "_ClientDescribeEventSubscriptionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeEventSubscriptionsFiltersTypeDef(
    _ClientDescribeEventSubscriptionsFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      Data returned by the **DescribeEventSubscriptions** action.
      - **Marker** *(string) --*

        An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions
        request. If this parameter is specified, the response includes only records beyond the
        marker, up to the value specified by ``MaxRecords`` .
    """


_ClientDescribeEventsFiltersTypeDef = TypedDict(
    "_ClientDescribeEventsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeEventsFiltersTypeDef(_ClientDescribeEventsFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      Contains the result of a successful invocation of the ``DescribeEvents`` action.
      - **Marker** *(string) --*

        An optional pagination token provided by a previous Events request. If this parameter is
        specified, the response includes only records beyond the marker, up to the value specified
        by ``MaxRecords`` .
    """


_ClientDescribeGlobalClustersFiltersTypeDef = TypedDict(
    "_ClientDescribeGlobalClustersFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeGlobalClustersFiltersTypeDef(_ClientDescribeGlobalClustersFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeGlobalClustersResponseGlobalClustersGlobalClusterMembersTypeDef = TypedDict(
    "_ClientDescribeGlobalClustersResponseGlobalClustersGlobalClusterMembersTypeDef",
    {"DBClusterArn": str, "Readers": List[str], "IsWriter": bool},
    total=False,
)


class ClientDescribeGlobalClustersResponseGlobalClustersGlobalClusterMembersTypeDef(
    _ClientDescribeGlobalClustersResponseGlobalClustersGlobalClusterMembersTypeDef
):
    pass


_ClientDescribeGlobalClustersResponseGlobalClustersTypeDef = TypedDict(
    "_ClientDescribeGlobalClustersResponseGlobalClustersTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List[
            ClientDescribeGlobalClustersResponseGlobalClustersGlobalClusterMembersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeGlobalClustersResponseGlobalClustersTypeDef(
    _ClientDescribeGlobalClustersResponseGlobalClustersTypeDef
):
    pass


_ClientDescribeGlobalClustersResponseTypeDef = TypedDict(
    "_ClientDescribeGlobalClustersResponseTypeDef",
    {
        "Marker": str,
        "GlobalClusters": List[ClientDescribeGlobalClustersResponseGlobalClustersTypeDef],
    },
    total=False,
)


class ClientDescribeGlobalClustersResponseTypeDef(_ClientDescribeGlobalClustersResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous ``DescribeGlobalClusters`` request. If
        this parameter is specified, the response includes only records beyond the marker, up to the
        value specified by ``MaxRecords`` .
    """


_ClientDescribeInstallationMediaFiltersTypeDef = TypedDict(
    "_ClientDescribeInstallationMediaFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeInstallationMediaFiltersTypeDef(_ClientDescribeInstallationMediaFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeInstallationMediaResponseInstallationMediaFailureCauseTypeDef = TypedDict(
    "_ClientDescribeInstallationMediaResponseInstallationMediaFailureCauseTypeDef",
    {"Message": str},
    total=False,
)


class ClientDescribeInstallationMediaResponseInstallationMediaFailureCauseTypeDef(
    _ClientDescribeInstallationMediaResponseInstallationMediaFailureCauseTypeDef
):
    pass


_ClientDescribeInstallationMediaResponseInstallationMediaTypeDef = TypedDict(
    "_ClientDescribeInstallationMediaResponseInstallationMediaTypeDef",
    {
        "InstallationMediaId": str,
        "CustomAvailabilityZoneId": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineInstallationMediaPath": str,
        "OSInstallationMediaPath": str,
        "Status": str,
        "FailureCause": ClientDescribeInstallationMediaResponseInstallationMediaFailureCauseTypeDef,
    },
    total=False,
)


class ClientDescribeInstallationMediaResponseInstallationMediaTypeDef(
    _ClientDescribeInstallationMediaResponseInstallationMediaTypeDef
):
    pass


_ClientDescribeInstallationMediaResponseTypeDef = TypedDict(
    "_ClientDescribeInstallationMediaResponseTypeDef",
    {
        "Marker": str,
        "InstallationMedia": List[ClientDescribeInstallationMediaResponseInstallationMediaTypeDef],
    },
    total=False,
)


class ClientDescribeInstallationMediaResponseTypeDef(
    _ClientDescribeInstallationMediaResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous  DescribeInstallationMedia request. If
        this parameter is specified, the response includes only records beyond the marker, up to the
        value specified by ``MaxRecords`` .
    """


_ClientDescribeOptionGroupOptionsFiltersTypeDef = TypedDict(
    "_ClientDescribeOptionGroupOptionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeOptionGroupOptionsFiltersTypeDef(
    _ClientDescribeOptionGroupOptionsFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef = TypedDict(
    "_ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef",
    {"AllowedValue": str, "MinimumEngineVersion": str},
    total=False,
)


class ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef(
    _ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef
):
    pass


_ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef = TypedDict(
    "_ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef",
    {
        "SettingName": str,
        "SettingDescription": str,
        "DefaultValue": str,
        "ApplyType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsRequired": bool,
        "MinimumEngineVersionPerAllowedValue": List[
            ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef
        ],
    },
    total=False,
)


class ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef(
    _ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef
):
    pass


_ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef = TypedDict(
    "_ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef",
    {"Version": str, "IsDefault": bool},
    total=False,
)


class ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef(
    _ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef
):
    pass


_ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsTypeDef = TypedDict(
    "_ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsTypeDef",
    {
        "Name": str,
        "Description": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "MinimumRequiredMinorEngineVersion": str,
        "PortRequired": bool,
        "DefaultPort": int,
        "OptionsDependedOn": List[str],
        "OptionsConflictsWith": List[str],
        "Persistent": bool,
        "Permanent": bool,
        "RequiresAutoMinorEngineVersionUpgrade": bool,
        "VpcOnly": bool,
        "SupportsOptionVersionDowngrade": bool,
        "OptionGroupOptionSettings": List[
            ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef
        ],
        "OptionGroupOptionVersions": List[
            ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsTypeDef(
    _ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsTypeDef
):
    """
    - *(dict) --*

      Available option.
      - **Name** *(string) --*

        The name of the option.
    """


_ClientDescribeOptionGroupOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeOptionGroupOptionsResponseTypeDef",
    {
        "OptionGroupOptions": List[
            ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeOptionGroupOptionsResponseTypeDef(
    _ClientDescribeOptionGroupOptionsResponseTypeDef
):
    """
    - *(dict) --*

      - **OptionGroupOptions** *(list) --*

        List of available option group options.
        - *(dict) --*

          Available option.
          - **Name** *(string) --*

            The name of the option.
    """


_ClientDescribeOptionGroupsFiltersTypeDef = TypedDict(
    "_ClientDescribeOptionGroupsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeOptionGroupsFiltersTypeDef(_ClientDescribeOptionGroupsFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeOptionGroupsResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef = TypedDict(
    "_ClientDescribeOptionGroupsResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientDescribeOptionGroupsResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef(
    _ClientDescribeOptionGroupsResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef
):
    pass


_ClientDescribeOptionGroupsResponseOptionGroupsListOptionsOptionSettingsTypeDef = TypedDict(
    "_ClientDescribeOptionGroupsResponseOptionGroupsListOptionsOptionSettingsTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)


class ClientDescribeOptionGroupsResponseOptionGroupsListOptionsOptionSettingsTypeDef(
    _ClientDescribeOptionGroupsResponseOptionGroupsListOptionsOptionSettingsTypeDef
):
    pass


_ClientDescribeOptionGroupsResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef = TypedDict(
    "_ClientDescribeOptionGroupsResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDescribeOptionGroupsResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef(
    _ClientDescribeOptionGroupsResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef
):
    pass


_ClientDescribeOptionGroupsResponseOptionGroupsListOptionsTypeDef = TypedDict(
    "_ClientDescribeOptionGroupsResponseOptionGroupsListOptionsTypeDef",
    {
        "OptionName": str,
        "OptionDescription": str,
        "Persistent": bool,
        "Permanent": bool,
        "Port": int,
        "OptionVersion": str,
        "OptionSettings": List[
            ClientDescribeOptionGroupsResponseOptionGroupsListOptionsOptionSettingsTypeDef
        ],
        "DBSecurityGroupMemberships": List[
            ClientDescribeOptionGroupsResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef
        ],
        "VpcSecurityGroupMemberships": List[
            ClientDescribeOptionGroupsResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeOptionGroupsResponseOptionGroupsListOptionsTypeDef(
    _ClientDescribeOptionGroupsResponseOptionGroupsListOptionsTypeDef
):
    pass


_ClientDescribeOptionGroupsResponseOptionGroupsListTypeDef = TypedDict(
    "_ClientDescribeOptionGroupsResponseOptionGroupsListTypeDef",
    {
        "OptionGroupName": str,
        "OptionGroupDescription": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "Options": List[ClientDescribeOptionGroupsResponseOptionGroupsListOptionsTypeDef],
        "AllowsVpcAndNonVpcInstanceMemberships": bool,
        "VpcId": str,
        "OptionGroupArn": str,
    },
    total=False,
)


class ClientDescribeOptionGroupsResponseOptionGroupsListTypeDef(
    _ClientDescribeOptionGroupsResponseOptionGroupsListTypeDef
):
    """
    - *(dict) --*

      - **OptionGroupName** *(string) --*

        Specifies the name of the option group.
    """


_ClientDescribeOptionGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeOptionGroupsResponseTypeDef",
    {
        "OptionGroupsList": List[ClientDescribeOptionGroupsResponseOptionGroupsListTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeOptionGroupsResponseTypeDef(_ClientDescribeOptionGroupsResponseTypeDef):
    """
    - *(dict) --*

      List of option groups.
      - **OptionGroupsList** *(list) --*

        List of option groups.
        - *(dict) --*

          - **OptionGroupName** *(string) --*

            Specifies the name of the option group.
    """


_ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef = TypedDict(
    "_ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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


_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef = TypedDict(
    "_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef",
    {"Name": str, "DefaultValue": str, "AllowedValues": str},
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef
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
        "AvailableProcessorFeatures": List[
            ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef
        ],
        "SupportedEngineModes": List[str],
        "SupportsStorageAutoscaling": bool,
        "SupportsKerberosAuthentication": bool,
    },
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef
):
    """
    - *(dict) --*

      Contains a list of available options for a DB instance.
      This data type is used as a response element in the ``DescribeOrderableDBInstanceOptions``
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

      Contains the result of a successful invocation of the ``DescribeOrderableDBInstanceOptions``
      action.
      - **OrderableDBInstanceOptions** *(list) --*

        An ``OrderableDBInstanceOption`` structure containing information about orderable options
        for the DB instance.
        - *(dict) --*

          Contains a list of available options for a DB instance.
          This data type is used as a response element in the ``DescribeOrderableDBInstanceOptions``
          action.
          - **Engine** *(string) --*

            The engine type of a DB instance.
    """


_ClientDescribePendingMaintenanceActionsFiltersTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribePendingMaintenanceActionsFiltersTypeDef(
    _ClientDescribePendingMaintenanceActionsFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      Data returned from the **DescribePendingMaintenanceActions** action.
      - **PendingMaintenanceActions** *(list) --*

        A list of the pending maintenance actions for the resource.
        - *(dict) --*

          Describes the pending maintenance actions for a resource.
          - **ResourceIdentifier** *(string) --*

            The ARN of the resource that has pending maintenance actions.
    """


_ClientDescribeReservedDbInstancesFiltersTypeDef = TypedDict(
    "_ClientDescribeReservedDbInstancesFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeReservedDbInstancesFiltersTypeDef(
    _ClientDescribeReservedDbInstancesFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeReservedDbInstancesOfferingsFiltersTypeDef = TypedDict(
    "_ClientDescribeReservedDbInstancesOfferingsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeReservedDbInstancesOfferingsFiltersTypeDef(
    _ClientDescribeReservedDbInstancesOfferingsFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsRecurringChargesTypeDef = TypedDict(
    "_ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsRecurringChargesTypeDef(
    _ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsRecurringChargesTypeDef
):
    pass


_ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsTypeDef = TypedDict(
    "_ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsTypeDef",
    {
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "RecurringCharges": List[
            ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsRecurringChargesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsTypeDef(
    _ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsTypeDef
):
    pass


_ClientDescribeReservedDbInstancesOfferingsResponseTypeDef = TypedDict(
    "_ClientDescribeReservedDbInstancesOfferingsResponseTypeDef",
    {
        "Marker": str,
        "ReservedDBInstancesOfferings": List[
            ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedDbInstancesOfferingsResponseTypeDef(
    _ClientDescribeReservedDbInstancesOfferingsResponseTypeDef
):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeReservedDBInstancesOfferings``
      action.
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_ClientDescribeReservedDbInstancesResponseReservedDBInstancesRecurringChargesTypeDef = TypedDict(
    "_ClientDescribeReservedDbInstancesResponseReservedDBInstancesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientDescribeReservedDbInstancesResponseReservedDBInstancesRecurringChargesTypeDef(
    _ClientDescribeReservedDbInstancesResponseReservedDBInstancesRecurringChargesTypeDef
):
    pass


_ClientDescribeReservedDbInstancesResponseReservedDBInstancesTypeDef = TypedDict(
    "_ClientDescribeReservedDbInstancesResponseReservedDBInstancesTypeDef",
    {
        "ReservedDBInstanceId": str,
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "DBInstanceCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "State": str,
        "RecurringCharges": List[
            ClientDescribeReservedDbInstancesResponseReservedDBInstancesRecurringChargesTypeDef
        ],
        "ReservedDBInstanceArn": str,
        "LeaseId": str,
    },
    total=False,
)


class ClientDescribeReservedDbInstancesResponseReservedDBInstancesTypeDef(
    _ClientDescribeReservedDbInstancesResponseReservedDBInstancesTypeDef
):
    pass


_ClientDescribeReservedDbInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeReservedDbInstancesResponseTypeDef",
    {
        "Marker": str,
        "ReservedDBInstances": List[
            ClientDescribeReservedDbInstancesResponseReservedDBInstancesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedDbInstancesResponseTypeDef(
    _ClientDescribeReservedDbInstancesResponseTypeDef
):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeReservedDBInstances`` action.
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_ClientDescribeSourceRegionsFiltersTypeDef = TypedDict(
    "_ClientDescribeSourceRegionsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeSourceRegionsFiltersTypeDef(_ClientDescribeSourceRegionsFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientDescribeSourceRegionsResponseSourceRegionsTypeDef = TypedDict(
    "_ClientDescribeSourceRegionsResponseSourceRegionsTypeDef",
    {"RegionName": str, "Endpoint": str, "Status": str},
    total=False,
)


class ClientDescribeSourceRegionsResponseSourceRegionsTypeDef(
    _ClientDescribeSourceRegionsResponseSourceRegionsTypeDef
):
    pass


_ClientDescribeSourceRegionsResponseTypeDef = TypedDict(
    "_ClientDescribeSourceRegionsResponseTypeDef",
    {"Marker": str, "SourceRegions": List[ClientDescribeSourceRegionsResponseSourceRegionsTypeDef]},
    total=False,
)


class ClientDescribeSourceRegionsResponseTypeDef(_ClientDescribeSourceRegionsResponseTypeDef):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeSourceRegions`` action.
      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
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
        "SupportsStorageAutoscaling": bool,
    },
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef
):
    """
    - *(dict) --*

      Information about valid modifications that you can make to your DB instance. Contains the
      result of a successful call to the ``DescribeValidDBInstanceModifications`` action.
      - **StorageType** *(string) --*

        The valid storage types for your DB instance. For example, gp2, io1.
    """


_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageValidProcessorFeaturesTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageValidProcessorFeaturesTypeDef",
    {"Name": str, "DefaultValue": str, "AllowedValues": str},
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageValidProcessorFeaturesTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageValidProcessorFeaturesTypeDef
):
    pass


_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef",
    {
        "Storage": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef
        ],
        "ValidProcessorFeatures": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageValidProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef
):
    """
    - **ValidDBInstanceModificationsMessage** *(dict) --*

      Information about valid modifications that you can make to your DB instance. Contains the
      result of a successful call to the ``DescribeValidDBInstanceModifications`` action. You can
      use this information when you call ``ModifyDBInstance`` .
      - **Storage** *(list) --*

        Valid storage options for your DB instance.
        - *(dict) --*

          Information about valid modifications that you can make to your DB instance. Contains the
          result of a successful call to the ``DescribeValidDBInstanceModifications`` action.
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
        result of a successful call to the ``DescribeValidDBInstanceModifications`` action. You can
        use this information when you call ``ModifyDBInstance`` .
        - **Storage** *(list) --*

          Valid storage options for your DB instance.
          - *(dict) --*

            Information about valid modifications that you can make to your DB instance. Contains
            the result of a successful call to the ``DescribeValidDBInstanceModifications`` action.
            - **StorageType** *(string) --*

              The valid storage types for your DB instance. For example, gp2, io1.
    """


_ClientDownloadDbLogFilePortionResponseTypeDef = TypedDict(
    "_ClientDownloadDbLogFilePortionResponseTypeDef",
    {"LogFileData": str, "Marker": str, "AdditionalDataPending": bool},
    total=False,
)


class ClientDownloadDbLogFilePortionResponseTypeDef(_ClientDownloadDbLogFilePortionResponseTypeDef):
    """
    - *(dict) --*

      This data type is used as a response element to ``DownloadDBLogFilePortion`` .
      - **LogFileData** *(string) --*

        Entries from the specified log file.
    """


_ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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


_ClientFailoverDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterScalingConfigurationInfoTypeDef(
    _ClientFailoverDbClusterResponseDBClusterScalingConfigurationInfoTypeDef
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientFailoverDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterTypeDef(
    _ClientFailoverDbClusterResponseDBClusterTypeDef
):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Aurora DB cluster.
      This data type is used as a response element in the ``DescribeDBClusters`` , ``StopDBCluster``
      , and ``StartDBCluster`` actions.
      - **AllocatedStorage** *(integer) --*

        For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the allocated
        storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns 1, because
        Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Aurora DB cluster.
        This data type is used as a response element in the ``DescribeDBClusters`` ,
        ``StopDBCluster`` , and ``StartDBCluster`` actions.
        - **AllocatedStorage** *(integer) --*

          For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the
          allocated storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns
          1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts
          as needed.
    """


_ClientImportInstallationMediaResponseFailureCauseTypeDef = TypedDict(
    "_ClientImportInstallationMediaResponseFailureCauseTypeDef", {"Message": str}, total=False
)


class ClientImportInstallationMediaResponseFailureCauseTypeDef(
    _ClientImportInstallationMediaResponseFailureCauseTypeDef
):
    pass


_ClientImportInstallationMediaResponseTypeDef = TypedDict(
    "_ClientImportInstallationMediaResponseTypeDef",
    {
        "InstallationMediaId": str,
        "CustomAvailabilityZoneId": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineInstallationMediaPath": str,
        "OSInstallationMediaPath": str,
        "Status": str,
        "FailureCause": ClientImportInstallationMediaResponseFailureCauseTypeDef,
    },
    total=False,
)


class ClientImportInstallationMediaResponseTypeDef(_ClientImportInstallationMediaResponseTypeDef):
    """
    - *(dict) --*

      Contains the installation media for a DB engine that requires an on-premises customer provided
      license, such as Microsoft SQL Server.
      - **InstallationMediaId** *(string) --*

        The installation medium ID.
    """


_ClientListTagsForResourceFiltersTypeDef = TypedDict(
    "_ClientListTagsForResourceFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientListTagsForResourceFiltersTypeDef(_ClientListTagsForResourceFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagListTypeDef(
    _ClientListTagsForResourceResponseTagListTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
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

          Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
          - **Key** *(string) --*

            A key is the required name of the tag. The string value can be from 1 to 128 Unicode
            characters in length and can't be prefixed with "aws:" or "rds:". The string can only
            contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
                ', '+',
            '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientModifyCurrentDbClusterCapacityResponseTypeDef = TypedDict(
    "_ClientModifyCurrentDbClusterCapacityResponseTypeDef",
    {
        "DBClusterIdentifier": str,
        "PendingCapacity": int,
        "CurrentCapacity": int,
        "SecondsBeforeTimeout": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientModifyCurrentDbClusterCapacityResponseTypeDef(
    _ClientModifyCurrentDbClusterCapacityResponseTypeDef
):
    """
    - *(dict) --*

      - **DBClusterIdentifier** *(string) --*

        A user-supplied DB cluster identifier. This identifier is the unique key that identifies a
        DB cluster.
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


_ClientModifyDbClusterEndpointResponseTypeDef = TypedDict(
    "_ClientModifyDbClusterEndpointResponseTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
    },
    total=False,
)


class ClientModifyDbClusterEndpointResponseTypeDef(_ClientModifyDbClusterEndpointResponseTypeDef):
    """
    - *(dict) --*

      This data type represents the information you need to connect to an Amazon Aurora DB cluster.
      This data type is used as a response element in the following actions:
      * ``CreateDBClusterEndpoint``
      * ``DescribeDBClusterEndpoints``
      * ``ModifyDBClusterEndpoint``
      * ``DeleteDBClusterEndpoint``
      For the data structure that represents Amazon RDS DB instance endpoints, see ``Endpoint`` .
      - **DBClusterEndpointIdentifier** *(string) --*

        The identifier associated with the endpoint. This parameter is stored as a lowercase string.
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
        "SupportedEngineModes": List[str],
    },
    total=False,
)


class ClientModifyDbClusterParameterGroupParametersTypeDef(
    _ClientModifyDbClusterParameterGroupParametersTypeDef
):
    """
    - *(dict) --*

      This data type is used as a request parameter in the ``ModifyDBParameterGroup`` and
      ``ResetDBParameterGroup`` actions.
      This data type is used as a response element in the ``DescribeEngineDefaultParameters`` and
      ``DescribeDBParameters`` actions.
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
        * Can't end with a hyphen or contain two consecutive hyphens
        .. note::

          This value is stored as a lowercase string.
    """


_ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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


_ClientModifyDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientModifyDbClusterResponseDBClusterScalingConfigurationInfoTypeDef(
    _ClientModifyDbClusterResponseDBClusterScalingConfigurationInfoTypeDef
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientModifyDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)


class ClientModifyDbClusterResponseDBClusterTypeDef(_ClientModifyDbClusterResponseDBClusterTypeDef):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Aurora DB cluster.
      This data type is used as a response element in the ``DescribeDBClusters`` , ``StopDBCluster``
      , and ``StartDBCluster`` actions.
      - **AllocatedStorage** *(integer) --*

        For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the allocated
        storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns 1, because
        Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Aurora DB cluster.
        This data type is used as a response element in the ``DescribeDBClusters`` ,
        ``StopDBCluster`` , and ``StartDBCluster`` actions.
        - **AllocatedStorage** *(integer) --*

          For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the
          allocated storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns
          1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts
          as needed.
    """


_ClientModifyDbClusterScalingConfigurationTypeDef = TypedDict(
    "_ClientModifyDbClusterScalingConfigurationTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientModifyDbClusterScalingConfigurationTypeDef(
    _ClientModifyDbClusterScalingConfigurationTypeDef
):
    """
    The scaling properties of the DB cluster. You can only modify scaling properties for DB clusters
    in ``serverless`` DB engine mode.
    - **MinCapacity** *(integer) --*

      The minimum capacity for an Aurora DB cluster in ``serverless`` DB engine mode.
      For Aurora MySQL, valid capacity values are ``1`` , ``2`` , ``4`` , ``8`` , ``16`` , ``32`` ,
      ``64`` , ``128`` , and ``256`` .
      For Aurora PostgreSQL, valid capacity values are ``2`` , ``4`` , ``8`` , ``16`` , ``32`` ,
      ``64`` , ``192`` , and ``384`` .
      The minimum capacity must be less than or equal to the maximum capacity.
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

      Contains the results of a successful call to the ``DescribeDBClusterSnapshotAttributes`` API
      action.
      Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or
      restore a manual DB cluster snapshot. For more information, see the
      ``ModifyDBClusterSnapshotAttribute`` API action.
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

        Contains the results of a successful call to the ``DescribeDBClusterSnapshotAttributes`` API
        action.
        Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or
        restore a manual DB cluster snapshot. For more information, see the
        ``ModifyDBClusterSnapshotAttribute`` API action.
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
    specific DB instance.
    A change to the ``CloudwatchLogsExportConfiguration`` parameter is always applied to the DB
    instance immediately. Therefore, the ``ApplyImmediately`` parameter has no effect.
    - **EnableLogTypes** *(list) --*

      The list of log types to enable.
      - *(string) --*
    """


_ClientModifyDbInstanceProcessorFeaturesTypeDef = TypedDict(
    "_ClientModifyDbInstanceProcessorFeaturesTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientModifyDbInstanceProcessorFeaturesTypeDef(
    _ClientModifyDbInstanceProcessorFeaturesTypeDef
):
    """
    - *(dict) --*

      Contains the processor features of a DB instance class.
      To specify the number of CPU cores, use the ``coreCount`` feature name for the ``Name``
      parameter. To specify the number of threads per core, use the ``threadsPerCore`` feature name
      for the ``Name`` parameter.
      You can set the processor features of the DB instance class for a DB instance when you call
      one of the following actions:
      * ``CreateDBInstance``
      * ``ModifyDBInstance``
      * ``RestoreDBInstanceFromDBSnapshot``
      * ``RestoreDBInstanceFromS3``
      * ``RestoreDBInstanceToPointInTime``
      You can view the valid processor values for a particular instance class by calling the
      ``DescribeOrderableDBInstanceOptions`` action and specifying the instance class for the
      ``DBInstanceClass`` parameter.
      In addition, you can use the following actions for DB instance class processor information:
      * ``DescribeDBInstances``
      * ``DescribeDBSnapshots``
      * ``DescribeValidDBInstanceModifications``
      For more information, see `Configuring the Processor of the DB Instance Class
      <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor>`__
      in the *Amazon RDS User Guide.*
      - **Name** *(string) --*

        The name of the processor feature. Valid names are ``coreCount`` and ``threadsPerCore`` .
    """


_ClientModifyDbInstanceResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceAssociatedRolesTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceAssociatedRolesTypeDef
):
    pass


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


_ClientModifyDbInstanceResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceListenerEndpointTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceListenerEndpointTypeDef
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


_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef(
    _ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
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
        "ProcessorFeatures": List[
            ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientModifyDbInstanceResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceProcessorFeaturesTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceProcessorFeaturesTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[ClientModifyDbInstanceResponseDBInstanceProcessorFeaturesTypeDef],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientModifyDbInstanceResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientModifyDbInstanceResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon RDS DB instance.
      This data type is used as a response element in the ``DescribeDBInstances`` action.
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

        Contains the details of an Amazon RDS DB instance.
        This data type is used as a response element in the ``DescribeDBInstances`` action.
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
        "SupportedEngineModes": List[str],
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

      Contains the result of a successful invocation of the ``ModifyDBParameterGroup`` or
      ``ResetDBParameterGroup`` action.
      - **DBParameterGroupName** *(string) --*

        Provides the name of the DB parameter group.
    """


_ClientModifyDbProxyAuthTypeDef = TypedDict(
    "_ClientModifyDbProxyAuthTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": str,
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)


class ClientModifyDbProxyAuthTypeDef(_ClientModifyDbProxyAuthTypeDef):
    """
    - *(dict) --*

      .. note::

        This is prerelease documentation for the RDS Database Proxy feature in preview release. It
        is subject to change.
    """


_ClientModifyDbProxyResponseDBProxyAuthTypeDef = TypedDict(
    "_ClientModifyDbProxyResponseDBProxyAuthTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": str,
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)


class ClientModifyDbProxyResponseDBProxyAuthTypeDef(_ClientModifyDbProxyResponseDBProxyAuthTypeDef):
    pass


_ClientModifyDbProxyResponseDBProxyTypeDef = TypedDict(
    "_ClientModifyDbProxyResponseDBProxyTypeDef",
    {
        "DBProxyName": str,
        "DBProxyArn": str,
        "Status": Literal[
            "available",
            "modifying",
            "incompatible-network",
            "insufficient-resource-limits",
            "creating",
            "deleting",
        ],
        "EngineFamily": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Auth": List[ClientModifyDbProxyResponseDBProxyAuthTypeDef],
        "RoleArn": str,
        "Endpoint": str,
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)


class ClientModifyDbProxyResponseDBProxyTypeDef(_ClientModifyDbProxyResponseDBProxyTypeDef):
    """
    - **DBProxy** *(dict) --*

      The ``DBProxy`` object representing the new settings for the proxy.
      - **DBProxyName** *(string) --*

        The identifier for the proxy. This name must be unique for all proxies owned by your AWS
        account in the specified AWS Region.
    """


_ClientModifyDbProxyResponseTypeDef = TypedDict(
    "_ClientModifyDbProxyResponseTypeDef",
    {"DBProxy": ClientModifyDbProxyResponseDBProxyTypeDef},
    total=False,
)


class ClientModifyDbProxyResponseTypeDef(_ClientModifyDbProxyResponseTypeDef):
    """
    - *(dict) --*

      - **DBProxy** *(dict) --*

        The ``DBProxy`` object representing the new settings for the proxy.
        - **DBProxyName** *(string) --*

          The identifier for the proxy. This name must be unique for all proxies owned by your AWS
          account in the specified AWS Region.
    """


_ClientModifyDbProxyTargetGroupConnectionPoolConfigTypeDef = TypedDict(
    "_ClientModifyDbProxyTargetGroupConnectionPoolConfigTypeDef",
    {
        "MaxConnectionsPercent": int,
        "MaxIdleConnectionsPercent": int,
        "ConnectionBorrowTimeout": int,
        "SessionPinningFilters": List[str],
        "InitQuery": str,
    },
    total=False,
)


class ClientModifyDbProxyTargetGroupConnectionPoolConfigTypeDef(
    _ClientModifyDbProxyTargetGroupConnectionPoolConfigTypeDef
):
    """
    The settings that determine the size and behavior of the connection pool for the target group.
    - **MaxConnectionsPercent** *(integer) --*

      The maximum size of the connection pool for each target in a target group. For Aurora MySQL,
      it is expressed as a percentage of the ``max_connections`` setting for the RDS DB instance or
      Aurora DB cluster used by the target group.
      Default: 100
      Constraints: between 1 and 100
    """


_ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupConnectionPoolConfigTypeDef = TypedDict(
    "_ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupConnectionPoolConfigTypeDef",
    {
        "MaxConnectionsPercent": int,
        "MaxIdleConnectionsPercent": int,
        "ConnectionBorrowTimeout": int,
        "SessionPinningFilters": List[str],
        "InitQuery": str,
    },
    total=False,
)


class ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupConnectionPoolConfigTypeDef(
    _ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupConnectionPoolConfigTypeDef
):
    pass


_ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupTypeDef = TypedDict(
    "_ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": str,
        "TargetGroupArn": str,
        "IsDefault": bool,
        "Status": str,
        "ConnectionPoolConfig": ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupConnectionPoolConfigTypeDef,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)


class ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupTypeDef(
    _ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupTypeDef
):
    """
    - **DBProxyTargetGroup** *(dict) --*

      The settings of the modified ``DBProxyTarget`` .
      - **DBProxyName** *(string) --*

        The identifier for the RDS proxy associated with this target group.
    """


_ClientModifyDbProxyTargetGroupResponseTypeDef = TypedDict(
    "_ClientModifyDbProxyTargetGroupResponseTypeDef",
    {"DBProxyTargetGroup": ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupTypeDef},
    total=False,
)


class ClientModifyDbProxyTargetGroupResponseTypeDef(_ClientModifyDbProxyTargetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **DBProxyTargetGroup** *(dict) --*

        The settings of the modified ``DBProxyTarget`` .
        - **DBProxyName** *(string) --*

          The identifier for the RDS proxy associated with this target group.
    """


_ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef = TypedDict(
    "_ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef",
    {"AttributeName": str, "AttributeValues": List[str]},
    total=False,
)


class ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef(
    _ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef
):
    pass


_ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultTypeDef = TypedDict(
    "_ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBSnapshotAttributes": List[
            ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef
        ],
    },
    total=False,
)


class ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultTypeDef(
    _ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultTypeDef
):
    """
    - **DBSnapshotAttributesResult** *(dict) --*

      Contains the results of a successful call to the ``DescribeDBSnapshotAttributes`` API action.
      Manual DB snapshot attributes are used to authorize other AWS accounts to copy or restore a
      manual DB snapshot. For more information, see the ``ModifyDBSnapshotAttribute`` API action.
      - **DBSnapshotIdentifier** *(string) --*

        The identifier of the manual DB snapshot that the attributes apply to.
    """


_ClientModifyDbSnapshotAttributeResponseTypeDef = TypedDict(
    "_ClientModifyDbSnapshotAttributeResponseTypeDef",
    {
        "DBSnapshotAttributesResult": ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultTypeDef
    },
    total=False,
)


class ClientModifyDbSnapshotAttributeResponseTypeDef(
    _ClientModifyDbSnapshotAttributeResponseTypeDef
):
    """
    - *(dict) --*

      - **DBSnapshotAttributesResult** *(dict) --*

        Contains the results of a successful call to the ``DescribeDBSnapshotAttributes`` API
        action.
        Manual DB snapshot attributes are used to authorize other AWS accounts to copy or restore a
        manual DB snapshot. For more information, see the ``ModifyDBSnapshotAttribute`` API action.
        - **DBSnapshotIdentifier** *(string) --*

          The identifier of the manual DB snapshot that the attributes apply to.
    """


_ClientModifyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef = TypedDict(
    "_ClientModifyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientModifyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef(
    _ClientModifyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef
):
    pass


_ClientModifyDbSnapshotResponseDBSnapshotTypeDef = TypedDict(
    "_ClientModifyDbSnapshotResponseDBSnapshotTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List[ClientModifyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef],
        "DbiResourceId": str,
    },
    total=False,
)


class ClientModifyDbSnapshotResponseDBSnapshotTypeDef(
    _ClientModifyDbSnapshotResponseDBSnapshotTypeDef
):
    """
    - **DBSnapshot** *(dict) --*

      Contains the details of an Amazon RDS DB snapshot.
      This data type is used as a response element in the ``DescribeDBSnapshots`` action.
      - **DBSnapshotIdentifier** *(string) --*

        Specifies the identifier for the DB snapshot.
    """


_ClientModifyDbSnapshotResponseTypeDef = TypedDict(
    "_ClientModifyDbSnapshotResponseTypeDef",
    {"DBSnapshot": ClientModifyDbSnapshotResponseDBSnapshotTypeDef},
    total=False,
)


class ClientModifyDbSnapshotResponseTypeDef(_ClientModifyDbSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **DBSnapshot** *(dict) --*

        Contains the details of an Amazon RDS DB snapshot.
        This data type is used as a response element in the ``DescribeDBSnapshots`` action.
        - **DBSnapshotIdentifier** *(string) --*

          Specifies the identifier for the DB snapshot.
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

      Contains the details of an Amazon RDS DB subnet group.
      This data type is used as a response element in the ``DescribeDBSubnetGroups`` action.
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

        Contains the details of an Amazon RDS DB subnet group.
        This data type is used as a response element in the ``DescribeDBSubnetGroups`` action.
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

      Contains the results of a successful invocation of the ``DescribeEventSubscriptions`` action.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the RDS event notification subscription.
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

        Contains the results of a successful invocation of the ``DescribeEventSubscriptions``
        action.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the RDS event notification subscription.
    """


_ClientModifyGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef = TypedDict(
    "_ClientModifyGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    {"DBClusterArn": str, "Readers": List[str], "IsWriter": bool},
    total=False,
)


class ClientModifyGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef(
    _ClientModifyGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef
):
    pass


_ClientModifyGlobalClusterResponseGlobalClusterTypeDef = TypedDict(
    "_ClientModifyGlobalClusterResponseGlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List[
            ClientModifyGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef
        ],
    },
    total=False,
)


class ClientModifyGlobalClusterResponseGlobalClusterTypeDef(
    _ClientModifyGlobalClusterResponseGlobalClusterTypeDef
):
    """
    - **GlobalCluster** *(dict) --*

      A data type representing an Aurora global database.
      - **GlobalClusterIdentifier** *(string) --*

        Contains a user-supplied global database cluster identifier. This identifier is the unique
        key that identifies a global database cluster.
    """


_ClientModifyGlobalClusterResponseTypeDef = TypedDict(
    "_ClientModifyGlobalClusterResponseTypeDef",
    {"GlobalCluster": ClientModifyGlobalClusterResponseGlobalClusterTypeDef},
    total=False,
)


class ClientModifyGlobalClusterResponseTypeDef(_ClientModifyGlobalClusterResponseTypeDef):
    """
    - *(dict) --*

      - **GlobalCluster** *(dict) --*

        A data type representing an Aurora global database.
        - **GlobalClusterIdentifier** *(string) --*

          Contains a user-supplied global database cluster identifier. This identifier is the unique
          key that identifies a global database cluster.
    """


_ClientModifyOptionGroupOptionsToIncludeOptionSettingsTypeDef = TypedDict(
    "_ClientModifyOptionGroupOptionsToIncludeOptionSettingsTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)


class ClientModifyOptionGroupOptionsToIncludeOptionSettingsTypeDef(
    _ClientModifyOptionGroupOptionsToIncludeOptionSettingsTypeDef
):
    pass


_RequiredClientModifyOptionGroupOptionsToIncludeTypeDef = TypedDict(
    "_RequiredClientModifyOptionGroupOptionsToIncludeTypeDef", {"OptionName": str}
)
_OptionalClientModifyOptionGroupOptionsToIncludeTypeDef = TypedDict(
    "_OptionalClientModifyOptionGroupOptionsToIncludeTypeDef",
    {
        "Port": int,
        "OptionVersion": str,
        "DBSecurityGroupMemberships": List[str],
        "VpcSecurityGroupMemberships": List[str],
        "OptionSettings": List[ClientModifyOptionGroupOptionsToIncludeOptionSettingsTypeDef],
    },
    total=False,
)


class ClientModifyOptionGroupOptionsToIncludeTypeDef(
    _RequiredClientModifyOptionGroupOptionsToIncludeTypeDef,
    _OptionalClientModifyOptionGroupOptionsToIncludeTypeDef,
):
    """
    - *(dict) --*

      A list of all available options
      - **OptionName** *(string) --***[REQUIRED]**

        The configuration of options to include in a group.
    """


_ClientModifyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef = TypedDict(
    "_ClientModifyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientModifyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef(
    _ClientModifyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef
):
    pass


_ClientModifyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef = TypedDict(
    "_ClientModifyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)


class ClientModifyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef(
    _ClientModifyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef
):
    pass


_ClientModifyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef = TypedDict(
    "_ClientModifyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef(
    _ClientModifyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef
):
    pass


_ClientModifyOptionGroupResponseOptionGroupOptionsTypeDef = TypedDict(
    "_ClientModifyOptionGroupResponseOptionGroupOptionsTypeDef",
    {
        "OptionName": str,
        "OptionDescription": str,
        "Persistent": bool,
        "Permanent": bool,
        "Port": int,
        "OptionVersion": str,
        "OptionSettings": List[
            ClientModifyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef
        ],
        "DBSecurityGroupMemberships": List[
            ClientModifyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef
        ],
        "VpcSecurityGroupMemberships": List[
            ClientModifyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef
        ],
    },
    total=False,
)


class ClientModifyOptionGroupResponseOptionGroupOptionsTypeDef(
    _ClientModifyOptionGroupResponseOptionGroupOptionsTypeDef
):
    pass


_ClientModifyOptionGroupResponseOptionGroupTypeDef = TypedDict(
    "_ClientModifyOptionGroupResponseOptionGroupTypeDef",
    {
        "OptionGroupName": str,
        "OptionGroupDescription": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "Options": List[ClientModifyOptionGroupResponseOptionGroupOptionsTypeDef],
        "AllowsVpcAndNonVpcInstanceMemberships": bool,
        "VpcId": str,
        "OptionGroupArn": str,
    },
    total=False,
)


class ClientModifyOptionGroupResponseOptionGroupTypeDef(
    _ClientModifyOptionGroupResponseOptionGroupTypeDef
):
    """
    - **OptionGroup** *(dict) --*

      - **OptionGroupName** *(string) --*

        Specifies the name of the option group.
    """


_ClientModifyOptionGroupResponseTypeDef = TypedDict(
    "_ClientModifyOptionGroupResponseTypeDef",
    {"OptionGroup": ClientModifyOptionGroupResponseOptionGroupTypeDef},
    total=False,
)


class ClientModifyOptionGroupResponseTypeDef(_ClientModifyOptionGroupResponseTypeDef):
    """
    - *(dict) --*

      - **OptionGroup** *(dict) --*

        - **OptionGroupName** *(string) --*

          Specifies the name of the option group.
    """


_ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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


_ClientPromoteReadReplicaDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseDBClusterScalingConfigurationInfoTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseDBClusterScalingConfigurationInfoTypeDef
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientPromoteReadReplicaDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef
):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Aurora DB cluster.
      This data type is used as a response element in the ``DescribeDBClusters`` , ``StopDBCluster``
      , and ``StartDBCluster`` actions.
      - **AllocatedStorage** *(integer) --*

        For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the allocated
        storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns 1, because
        Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Aurora DB cluster.
        This data type is used as a response element in the ``DescribeDBClusters`` ,
        ``StopDBCluster`` , and ``StartDBCluster`` actions.
        - **AllocatedStorage** *(integer) --*

          For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the
          allocated storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns
          1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts
          as needed.
    """


_ClientPromoteReadReplicaResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceAssociatedRolesTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceAssociatedRolesTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceDBParameterGroupsTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceDomainMembershipsTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceDomainMembershipsTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceEndpointTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceEndpointTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceListenerEndpointTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceListenerEndpointTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef(
    _ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceProcessorFeaturesTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceProcessorFeaturesTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceStatusInfosTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceStatusInfosTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientPromoteReadReplicaResponseDBInstanceTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientPromoteReadReplicaResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientPromoteReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[
            ClientPromoteReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientPromoteReadReplicaResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientPromoteReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientPromoteReadReplicaResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientPromoteReadReplicaResponseDBInstanceDomainMembershipsTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[
            ClientPromoteReadReplicaResponseDBInstanceProcessorFeaturesTypeDef
        ],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientPromoteReadReplicaResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientPromoteReadReplicaResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)


class ClientPromoteReadReplicaResponseDBInstanceTypeDef(
    _ClientPromoteReadReplicaResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon RDS DB instance.
      This data type is used as a response element in the ``DescribeDBInstances`` action.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
        identifies a DB instance.
    """


_ClientPromoteReadReplicaResponseTypeDef = TypedDict(
    "_ClientPromoteReadReplicaResponseTypeDef",
    {"DBInstance": ClientPromoteReadReplicaResponseDBInstanceTypeDef},
    total=False,
)


class ClientPromoteReadReplicaResponseTypeDef(_ClientPromoteReadReplicaResponseTypeDef):
    """
    - *(dict) --*

      - **DBInstance** *(dict) --*

        Contains the details of an Amazon RDS DB instance.
        This data type is used as a response element in the ``DescribeDBInstances`` action.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceRecurringChargesTypeDef = TypedDict(
    "_ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceRecurringChargesTypeDef(
    _ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceRecurringChargesTypeDef
):
    pass


_ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceTypeDef = TypedDict(
    "_ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceTypeDef",
    {
        "ReservedDBInstanceId": str,
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "DBInstanceCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "State": str,
        "RecurringCharges": List[
            ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceRecurringChargesTypeDef
        ],
        "ReservedDBInstanceArn": str,
        "LeaseId": str,
    },
    total=False,
)


class ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceTypeDef(
    _ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceTypeDef
):
    """
    - **ReservedDBInstance** *(dict) --*

      This data type is used as a response element in the ``DescribeReservedDBInstances`` and
      ``PurchaseReservedDBInstancesOffering`` actions.
      - **ReservedDBInstanceId** *(string) --*

        The unique identifier for the reservation.
    """


_ClientPurchaseReservedDbInstancesOfferingResponseTypeDef = TypedDict(
    "_ClientPurchaseReservedDbInstancesOfferingResponseTypeDef",
    {
        "ReservedDBInstance": ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceTypeDef
    },
    total=False,
)


class ClientPurchaseReservedDbInstancesOfferingResponseTypeDef(
    _ClientPurchaseReservedDbInstancesOfferingResponseTypeDef
):
    """
    - *(dict) --*

      - **ReservedDBInstance** *(dict) --*

        This data type is used as a response element in the ``DescribeReservedDBInstances`` and
        ``PurchaseReservedDBInstancesOffering`` actions.
        - **ReservedDBInstanceId** *(string) --*

          The unique identifier for the reservation.
    """


_ClientPurchaseReservedDbInstancesOfferingTagsTypeDef = TypedDict(
    "_ClientPurchaseReservedDbInstancesOfferingTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientPurchaseReservedDbInstancesOfferingTagsTypeDef(
    _ClientPurchaseReservedDbInstancesOfferingTagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientRebootDbInstanceResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceAssociatedRolesTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceAssociatedRolesTypeDef
):
    pass


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


_ClientRebootDbInstanceResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceListenerEndpointTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceListenerEndpointTypeDef
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


_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef(
    _ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
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
        "ProcessorFeatures": List[
            ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientRebootDbInstanceResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceProcessorFeaturesTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceProcessorFeaturesTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[ClientRebootDbInstanceResponseDBInstanceProcessorFeaturesTypeDef],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientRebootDbInstanceResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientRebootDbInstanceResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon RDS DB instance.
      This data type is used as a response element in the ``DescribeDBInstances`` action.
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

        Contains the details of an Amazon RDS DB instance.
        This data type is used as a response element in the ``DescribeDBInstances`` action.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientRegisterDbProxyTargetsResponseDBProxyTargetsTypeDef = TypedDict(
    "_ClientRegisterDbProxyTargetsResponseDBProxyTargetsTypeDef",
    {
        "TargetArn": str,
        "Endpoint": str,
        "TrackedClusterId": str,
        "RdsResourceId": str,
        "Port": int,
        "Type": Literal["RDS_INSTANCE", "RDS_SERVERLESS_ENDPOINT", "TRACKED_CLUSTER"],
    },
    total=False,
)


class ClientRegisterDbProxyTargetsResponseDBProxyTargetsTypeDef(
    _ClientRegisterDbProxyTargetsResponseDBProxyTargetsTypeDef
):
    """
    - *(dict) --*

      .. note::

        This is prerelease documentation for the RDS Database Proxy feature in preview release. It
        is subject to change.
    """


_ClientRegisterDbProxyTargetsResponseTypeDef = TypedDict(
    "_ClientRegisterDbProxyTargetsResponseTypeDef",
    {"DBProxyTargets": List[ClientRegisterDbProxyTargetsResponseDBProxyTargetsTypeDef]},
    total=False,
)


class ClientRegisterDbProxyTargetsResponseTypeDef(_ClientRegisterDbProxyTargetsResponseTypeDef):
    """
    - *(dict) --*

      - **DBProxyTargets** *(list) --*

        One or more ``DBProxyTarget`` objects that are created when you register targets with a
        target group.
        - *(dict) --*

          .. note::

            This is prerelease documentation for the RDS Database Proxy feature in preview release.
            It is subject to change.
    """


_ClientRemoveFromGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef = TypedDict(
    "_ClientRemoveFromGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    {"DBClusterArn": str, "Readers": List[str], "IsWriter": bool},
    total=False,
)


class ClientRemoveFromGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef(
    _ClientRemoveFromGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef
):
    pass


_ClientRemoveFromGlobalClusterResponseGlobalClusterTypeDef = TypedDict(
    "_ClientRemoveFromGlobalClusterResponseGlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List[
            ClientRemoveFromGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef
        ],
    },
    total=False,
)


class ClientRemoveFromGlobalClusterResponseGlobalClusterTypeDef(
    _ClientRemoveFromGlobalClusterResponseGlobalClusterTypeDef
):
    """
    - **GlobalCluster** *(dict) --*

      A data type representing an Aurora global database.
      - **GlobalClusterIdentifier** *(string) --*

        Contains a user-supplied global database cluster identifier. This identifier is the unique
        key that identifies a global database cluster.
    """


_ClientRemoveFromGlobalClusterResponseTypeDef = TypedDict(
    "_ClientRemoveFromGlobalClusterResponseTypeDef",
    {"GlobalCluster": ClientRemoveFromGlobalClusterResponseGlobalClusterTypeDef},
    total=False,
)


class ClientRemoveFromGlobalClusterResponseTypeDef(_ClientRemoveFromGlobalClusterResponseTypeDef):
    """
    - *(dict) --*

      - **GlobalCluster** *(dict) --*

        A data type representing an Aurora global database.
        - **GlobalClusterIdentifier** *(string) --*

          Contains a user-supplied global database cluster identifier. This identifier is the unique
          key that identifies a global database cluster.
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

      Contains the results of a successful invocation of the ``DescribeEventSubscriptions`` action.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the RDS event notification subscription.
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

        Contains the results of a successful invocation of the ``DescribeEventSubscriptions``
        action.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the RDS event notification subscription.
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
        "SupportedEngineModes": List[str],
    },
    total=False,
)


class ClientResetDbClusterParameterGroupParametersTypeDef(
    _ClientResetDbClusterParameterGroupParametersTypeDef
):
    """
    - *(dict) --*

      This data type is used as a request parameter in the ``ModifyDBParameterGroup`` and
      ``ResetDBParameterGroup`` actions.
      This data type is used as a response element in the ``DescribeEngineDefaultParameters`` and
      ``DescribeDBParameters`` actions.
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
        * Can't end with a hyphen or contain two consecutive hyphens
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
        "SupportedEngineModes": List[str],
    },
    total=False,
)


class ClientResetDbParameterGroupParametersTypeDef(_ClientResetDbParameterGroupParametersTypeDef):
    pass


_ClientResetDbParameterGroupResponseTypeDef = TypedDict(
    "_ClientResetDbParameterGroupResponseTypeDef", {"DBParameterGroupName": str}, total=False
)


class ClientResetDbParameterGroupResponseTypeDef(_ClientResetDbParameterGroupResponseTypeDef):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``ModifyDBParameterGroup`` or
      ``ResetDBParameterGroup`` action.
      - **DBParameterGroupName** *(string) --*

        Provides the name of the DB parameter group.
    """


_ClientRestoreDbClusterFromS3ResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromS3ResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
    total=False,
)


class ClientRestoreDbClusterFromS3ResponseDBClusterAssociatedRolesTypeDef(
    _ClientRestoreDbClusterFromS3ResponseDBClusterAssociatedRolesTypeDef
):
    pass


_ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterMembersTypeDef(
    _ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterMembersTypeDef
):
    pass


_ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
):
    pass


_ClientRestoreDbClusterFromS3ResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromS3ResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientRestoreDbClusterFromS3ResponseDBClusterScalingConfigurationInfoTypeDef(
    _ClientRestoreDbClusterFromS3ResponseDBClusterScalingConfigurationInfoTypeDef
):
    pass


_ClientRestoreDbClusterFromS3ResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromS3ResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterFromS3ResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientRestoreDbClusterFromS3ResponseDBClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientRestoreDbClusterFromS3ResponseDBClusterTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromS3ResponseDBClusterTypeDef",
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
        "CustomEndpoints": List[str],
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[
            ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbClusterFromS3ResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientRestoreDbClusterFromS3ResponseDBClusterAssociatedRolesTypeDef
        ],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientRestoreDbClusterFromS3ResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)


class ClientRestoreDbClusterFromS3ResponseDBClusterTypeDef(
    _ClientRestoreDbClusterFromS3ResponseDBClusterTypeDef
):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Aurora DB cluster.
      This data type is used as a response element in the ``DescribeDBClusters`` , ``StopDBCluster``
      , and ``StartDBCluster`` actions.
      - **AllocatedStorage** *(integer) --*

        For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the allocated
        storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns 1, because
        Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.
    """


_ClientRestoreDbClusterFromS3ResponseTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromS3ResponseTypeDef",
    {"DBCluster": ClientRestoreDbClusterFromS3ResponseDBClusterTypeDef},
    total=False,
)


class ClientRestoreDbClusterFromS3ResponseTypeDef(_ClientRestoreDbClusterFromS3ResponseTypeDef):
    """
    - *(dict) --*

      - **DBCluster** *(dict) --*

        Contains the details of an Amazon Aurora DB cluster.
        This data type is used as a response element in the ``DescribeDBClusters`` ,
        ``StopDBCluster`` , and ``StartDBCluster`` actions.
        - **AllocatedStorage** *(integer) --*

          For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the
          allocated storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns
          1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts
          as needed.
    """


_ClientRestoreDbClusterFromS3TagsTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromS3TagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRestoreDbClusterFromS3TagsTypeDef(_ClientRestoreDbClusterFromS3TagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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


_ClientRestoreDbClusterFromSnapshotResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterScalingConfigurationInfoTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterScalingConfigurationInfoTypeDef
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientRestoreDbClusterFromSnapshotResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef
):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Aurora DB cluster.
      This data type is used as a response element in the ``DescribeDBClusters`` , ``StopDBCluster``
      , and ``StartDBCluster`` actions.
      - **AllocatedStorage** *(integer) --*

        For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the allocated
        storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns 1, because
        Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Aurora DB cluster.
        This data type is used as a response element in the ``DescribeDBClusters`` ,
        ``StopDBCluster`` , and ``StartDBCluster`` actions.
        - **AllocatedStorage** *(integer) --*

          For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the
          allocated storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns
          1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts
          as needed.
    """


_ClientRestoreDbClusterFromSnapshotScalingConfigurationTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotScalingConfigurationTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientRestoreDbClusterFromSnapshotScalingConfigurationTypeDef(
    _ClientRestoreDbClusterFromSnapshotScalingConfigurationTypeDef
):
    """
    For DB clusters in ``serverless`` DB engine mode, the scaling properties of the DB cluster.
    - **MinCapacity** *(integer) --*

      The minimum capacity for an Aurora DB cluster in ``serverless`` DB engine mode.
      For Aurora MySQL, valid capacity values are ``1`` , ``2`` , ``4`` , ``8`` , ``16`` , ``32`` ,
      ``64`` , ``128`` , and ``256`` .
      For Aurora PostgreSQL, valid capacity values are ``2`` , ``4`` , ``8`` , ``16`` , ``32`` ,
      ``64`` , ``192`` , and ``384`` .
      The minimum capacity must be less than or equal to the maximum capacity.
    """


_ClientRestoreDbClusterFromSnapshotTagsTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRestoreDbClusterFromSnapshotTagsTypeDef(_ClientRestoreDbClusterFromSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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


_ClientRestoreDbClusterToPointInTimeResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterScalingConfigurationInfoTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterScalingConfigurationInfoTypeDef
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientRestoreDbClusterToPointInTimeResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef
):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Aurora DB cluster.
      This data type is used as a response element in the ``DescribeDBClusters`` , ``StopDBCluster``
      , and ``StartDBCluster`` actions.
      - **AllocatedStorage** *(integer) --*

        For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the allocated
        storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns 1, because
        Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Aurora DB cluster.
        This data type is used as a response element in the ``DescribeDBClusters`` ,
        ``StopDBCluster`` , and ``StartDBCluster`` actions.
        - **AllocatedStorage** *(integer) --*

          For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the
          allocated storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns
          1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts
          as needed.
    """


_ClientRestoreDbClusterToPointInTimeTagsTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRestoreDbClusterToPointInTimeTagsTypeDef(
    _ClientRestoreDbClusterToPointInTimeTagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientRestoreDbInstanceFromDbSnapshotProcessorFeaturesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotProcessorFeaturesTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotProcessorFeaturesTypeDef
):
    """
    - *(dict) --*

      Contains the processor features of a DB instance class.
      To specify the number of CPU cores, use the ``coreCount`` feature name for the ``Name``
      parameter. To specify the number of threads per core, use the ``threadsPerCore`` feature name
      for the ``Name`` parameter.
      You can set the processor features of the DB instance class for a DB instance when you call
      one of the following actions:
      * ``CreateDBInstance``
      * ``ModifyDBInstance``
      * ``RestoreDBInstanceFromDBSnapshot``
      * ``RestoreDBInstanceFromS3``
      * ``RestoreDBInstanceToPointInTime``
      You can view the valid processor values for a particular instance class by calling the
      ``DescribeOrderableDBInstanceOptions`` action and specifying the instance class for the
      ``DBInstanceClass`` parameter.
      In addition, you can use the following actions for DB instance class processor information:
      * ``DescribeDBInstances``
      * ``DescribeDBSnapshots``
      * ``DescribeValidDBInstanceModifications``
      For more information, see `Configuring the Processor of the DB Instance Class
      <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor>`__
      in the *Amazon RDS User Guide.*
      - **Name** *(string) --*

        The name of the processor feature. Valid names are ``coreCount`` and ``threadsPerCore`` .
    """


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceAssociatedRolesTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceAssociatedRolesTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBParameterGroupsTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSecurityGroupsTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDomainMembershipsTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDomainMembershipsTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceEndpointTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceEndpointTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceListenerEndpointTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceListenerEndpointTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceOptionGroupMembershipsTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceProcessorFeaturesTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceProcessorFeaturesTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceStatusInfosTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceStatusInfosTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceStatusInfosTypeDef
        ],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDomainMembershipsTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceProcessorFeaturesTypeDef
        ],
        "DeletionProtection": bool,
        "AssociatedRoles": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceAssociatedRolesTypeDef
        ],
        "ListenerEndpoint": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon RDS DB instance.
      This data type is used as a response element in the ``DescribeDBInstances`` action.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
        identifies a DB instance.
    """


_ClientRestoreDbInstanceFromDbSnapshotResponseTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotResponseTypeDef",
    {"DBInstance": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceTypeDef},
    total=False,
)


class ClientRestoreDbInstanceFromDbSnapshotResponseTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotResponseTypeDef
):
    """
    - *(dict) --*

      - **DBInstance** *(dict) --*

        Contains the details of an Amazon RDS DB instance.
        This data type is used as a response element in the ``DescribeDBInstances`` action.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientRestoreDbInstanceFromDbSnapshotTagsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromDbSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRestoreDbInstanceFromDbSnapshotTagsTypeDef(
    _ClientRestoreDbInstanceFromDbSnapshotTagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientRestoreDbInstanceFromS3ProcessorFeaturesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientRestoreDbInstanceFromS3ProcessorFeaturesTypeDef(
    _ClientRestoreDbInstanceFromS3ProcessorFeaturesTypeDef
):
    """
    - *(dict) --*

      Contains the processor features of a DB instance class.
      To specify the number of CPU cores, use the ``coreCount`` feature name for the ``Name``
      parameter. To specify the number of threads per core, use the ``threadsPerCore`` feature name
      for the ``Name`` parameter.
      You can set the processor features of the DB instance class for a DB instance when you call
      one of the following actions:
      * ``CreateDBInstance``
      * ``ModifyDBInstance``
      * ``RestoreDBInstanceFromDBSnapshot``
      * ``RestoreDBInstanceFromS3``
      * ``RestoreDBInstanceToPointInTime``
      You can view the valid processor values for a particular instance class by calling the
      ``DescribeOrderableDBInstanceOptions`` action and specifying the instance class for the
      ``DBInstanceClass`` parameter.
      In addition, you can use the following actions for DB instance class processor information:
      * ``DescribeDBInstances``
      * ``DescribeDBSnapshots``
      * ``DescribeValidDBInstanceModifications``
      For more information, see `Configuring the Processor of the DB Instance Class
      <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor>`__
      in the *Amazon RDS User Guide.*
      - **Name** *(string) --*

        The name of the processor feature. Valid names are ``coreCount`` and ``threadsPerCore`` .
    """


_ClientRestoreDbInstanceFromS3ResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceAssociatedRolesTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceAssociatedRolesTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceDBParameterGroupsTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSecurityGroupsTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceDomainMembershipsTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceDomainMembershipsTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceEndpointTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceEndpointTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceListenerEndpointTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceListenerEndpointTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceOptionGroupMembershipsTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceProcessorFeaturesTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceProcessorFeaturesTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceStatusInfosTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceStatusInfosTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientRestoreDbInstanceFromS3ResponseDBInstanceTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRestoreDbInstanceFromS3ResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientRestoreDbInstanceFromS3ResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientRestoreDbInstanceFromS3ResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstanceDomainMembershipsTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstanceProcessorFeaturesTypeDef
        ],
        "DeletionProtection": bool,
        "AssociatedRoles": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstanceAssociatedRolesTypeDef
        ],
        "ListenerEndpoint": ClientRestoreDbInstanceFromS3ResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseDBInstanceTypeDef(
    _ClientRestoreDbInstanceFromS3ResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon RDS DB instance.
      This data type is used as a response element in the ``DescribeDBInstances`` action.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
        identifies a DB instance.
    """


_ClientRestoreDbInstanceFromS3ResponseTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3ResponseTypeDef",
    {"DBInstance": ClientRestoreDbInstanceFromS3ResponseDBInstanceTypeDef},
    total=False,
)


class ClientRestoreDbInstanceFromS3ResponseTypeDef(_ClientRestoreDbInstanceFromS3ResponseTypeDef):
    """
    - *(dict) --*

      - **DBInstance** *(dict) --*

        Contains the details of an Amazon RDS DB instance.
        This data type is used as a response element in the ``DescribeDBInstances`` action.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientRestoreDbInstanceFromS3TagsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceFromS3TagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRestoreDbInstanceFromS3TagsTypeDef(_ClientRestoreDbInstanceFromS3TagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientRestoreDbInstanceToPointInTimeProcessorFeaturesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeProcessorFeaturesTypeDef(
    _ClientRestoreDbInstanceToPointInTimeProcessorFeaturesTypeDef
):
    """
    - *(dict) --*

      Contains the processor features of a DB instance class.
      To specify the number of CPU cores, use the ``coreCount`` feature name for the ``Name``
      parameter. To specify the number of threads per core, use the ``threadsPerCore`` feature name
      for the ``Name`` parameter.
      You can set the processor features of the DB instance class for a DB instance when you call
      one of the following actions:
      * ``CreateDBInstance``
      * ``ModifyDBInstance``
      * ``RestoreDBInstanceFromDBSnapshot``
      * ``RestoreDBInstanceFromS3``
      * ``RestoreDBInstanceToPointInTime``
      You can view the valid processor values for a particular instance class by calling the
      ``DescribeOrderableDBInstanceOptions`` action and specifying the instance class for the
      ``DBInstanceClass`` parameter.
      In addition, you can use the following actions for DB instance class processor information:
      * ``DescribeDBInstances``
      * ``DescribeDBSnapshots``
      * ``DescribeValidDBInstanceModifications``
      For more information, see `Configuring the Processor of the DB Instance Class
      <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor>`__
      in the *Amazon RDS User Guide.*
      - **Name** *(string) --*

        The name of the processor feature. Valid names are ``coreCount`` and ``threadsPerCore`` .
    """


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceAssociatedRolesTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceAssociatedRolesTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBParameterGroupsTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSecurityGroupsTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDomainMembershipsTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDomainMembershipsTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceEndpointTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceEndpointTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceListenerEndpointTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceListenerEndpointTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceOptionGroupMembershipsTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceProcessorFeaturesTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceProcessorFeaturesTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceStatusInfosTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceStatusInfosTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRestoreDbInstanceToPointInTimeResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceStatusInfosTypeDef
        ],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDomainMembershipsTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceProcessorFeaturesTypeDef
        ],
        "DeletionProtection": bool,
        "AssociatedRoles": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceAssociatedRolesTypeDef
        ],
        "ListenerEndpoint": ClientRestoreDbInstanceToPointInTimeResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseDBInstanceTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon RDS DB instance.
      This data type is used as a response element in the ``DescribeDBInstances`` action.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
        identifies a DB instance.
    """


_ClientRestoreDbInstanceToPointInTimeResponseTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeResponseTypeDef",
    {"DBInstance": ClientRestoreDbInstanceToPointInTimeResponseDBInstanceTypeDef},
    total=False,
)


class ClientRestoreDbInstanceToPointInTimeResponseTypeDef(
    _ClientRestoreDbInstanceToPointInTimeResponseTypeDef
):
    """
    - *(dict) --*

      - **DBInstance** *(dict) --*

        Contains the details of an Amazon RDS DB instance.
        This data type is used as a response element in the ``DescribeDBInstances`` action.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientRestoreDbInstanceToPointInTimeTagsTypeDef = TypedDict(
    "_ClientRestoreDbInstanceToPointInTimeTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRestoreDbInstanceToPointInTimeTagsTypeDef(
    _ClientRestoreDbInstanceToPointInTimeTagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and can't be prefixed with "aws:" or "rds:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)


class ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef(
    _ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef
):
    pass


_ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef = TypedDict(
    "_ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef",
    {"Status": str, "CIDRIP": str},
    total=False,
)


class ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef(
    _ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef
):
    pass


_ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef = TypedDict(
    "_ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "VpcId": str,
        "EC2SecurityGroups": List[
            ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef],
        "DBSecurityGroupArn": str,
    },
    total=False,
)


class ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef(
    _ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef
):
    """
    - **DBSecurityGroup** *(dict) --*

      Contains the details for an Amazon RDS DB security group.
      This data type is used as a response element in the ``DescribeDBSecurityGroups`` action.
      - **OwnerId** *(string) --*

        Provides the AWS ID of the owner of a specific DB security group.
    """


_ClientRevokeDbSecurityGroupIngressResponseTypeDef = TypedDict(
    "_ClientRevokeDbSecurityGroupIngressResponseTypeDef",
    {"DBSecurityGroup": ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef},
    total=False,
)


class ClientRevokeDbSecurityGroupIngressResponseTypeDef(
    _ClientRevokeDbSecurityGroupIngressResponseTypeDef
):
    """
    - *(dict) --*

      - **DBSecurityGroup** *(dict) --*

        Contains the details for an Amazon RDS DB security group.
        This data type is used as a response element in the ``DescribeDBSecurityGroups`` action.
        - **OwnerId** *(string) --*

          Provides the AWS ID of the owner of a specific DB security group.
    """


_ClientStartActivityStreamResponseTypeDef = TypedDict(
    "_ClientStartActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": Literal["stopped", "starting", "started", "stopping"],
        "Mode": Literal["sync", "async"],
        "ApplyImmediately": bool,
    },
    total=False,
)


class ClientStartActivityStreamResponseTypeDef(_ClientStartActivityStreamResponseTypeDef):
    """
    - *(dict) --*

      - **KmsKeyId** *(string) --*

        The AWS KMS key identifier for encryption of messages in the database activity stream.
    """


_ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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


_ClientStartDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientStartDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientStartDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientStartDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
):
    pass


_ClientStartDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "_ClientStartDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientStartDbClusterResponseDBClusterScalingConfigurationInfoTypeDef(
    _ClientStartDbClusterResponseDBClusterScalingConfigurationInfoTypeDef
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
        "CustomEndpoints": List[str],
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientStartDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientStartDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)


class ClientStartDbClusterResponseDBClusterTypeDef(_ClientStartDbClusterResponseDBClusterTypeDef):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Aurora DB cluster.
      This data type is used as a response element in the ``DescribeDBClusters`` , ``StopDBCluster``
      , and ``StartDBCluster`` actions.
      - **AllocatedStorage** *(integer) --*

        For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the allocated
        storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns 1, because
        Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Aurora DB cluster.
        This data type is used as a response element in the ``DescribeDBClusters`` ,
        ``StopDBCluster`` , and ``StartDBCluster`` actions.
        - **AllocatedStorage** *(integer) --*

          For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the
          allocated storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns
          1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts
          as needed.
    """


_ClientStartDbInstanceResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceAssociatedRolesTypeDef(
    _ClientStartDbInstanceResponseDBInstanceAssociatedRolesTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientStartDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientStartDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientStartDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceDomainMembershipsTypeDef(
    _ClientStartDbInstanceResponseDBInstanceDomainMembershipsTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientStartDbInstanceResponseDBInstanceEndpointTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceListenerEndpointTypeDef(
    _ClientStartDbInstanceResponseDBInstanceListenerEndpointTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientStartDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientStartDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientStartDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientStartDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef(
    _ClientStartDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientStartDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientStartDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientStartDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientStartDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceProcessorFeaturesTypeDef(
    _ClientStartDbInstanceResponseDBInstanceProcessorFeaturesTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientStartDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientStartDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientStartDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientStartDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientStartDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[ClientStartDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "DBParameterGroups": List[ClientStartDbInstanceResponseDBInstanceDBParameterGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientStartDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientStartDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientStartDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientStartDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[ClientStartDbInstanceResponseDBInstanceDomainMembershipsTypeDef],
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[ClientStartDbInstanceResponseDBInstanceProcessorFeaturesTypeDef],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientStartDbInstanceResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientStartDbInstanceResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)


class ClientStartDbInstanceResponseDBInstanceTypeDef(
    _ClientStartDbInstanceResponseDBInstanceTypeDef
):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon RDS DB instance.
      This data type is used as a response element in the ``DescribeDBInstances`` action.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
        identifies a DB instance.
    """


_ClientStartDbInstanceResponseTypeDef = TypedDict(
    "_ClientStartDbInstanceResponseTypeDef",
    {"DBInstance": ClientStartDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientStartDbInstanceResponseTypeDef(_ClientStartDbInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **DBInstance** *(dict) --*

        Contains the details of an Amazon RDS DB instance.
        This data type is used as a response element in the ``DescribeDBInstances`` action.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_ClientStopActivityStreamResponseTypeDef = TypedDict(
    "_ClientStopActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": Literal["stopped", "starting", "started", "stopping"],
    },
    total=False,
)


class ClientStopActivityStreamResponseTypeDef(_ClientStopActivityStreamResponseTypeDef):
    """
    - *(dict) --*

      - **KmsKeyId** *(string) --*

        The AWS KMS key identifier used for encrypting messages in the database activity stream.
    """


_ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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


_ClientStopDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientStopDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientStopDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientStopDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
):
    pass


_ClientStopDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "_ClientStopDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ClientStopDbClusterResponseDBClusterScalingConfigurationInfoTypeDef(
    _ClientStopDbClusterResponseDBClusterScalingConfigurationInfoTypeDef
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
        "CustomEndpoints": List[str],
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientStopDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientStopDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)


class ClientStopDbClusterResponseDBClusterTypeDef(_ClientStopDbClusterResponseDBClusterTypeDef):
    """
    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Aurora DB cluster.
      This data type is used as a response element in the ``DescribeDBClusters`` , ``StopDBCluster``
      , and ``StartDBCluster`` actions.
      - **AllocatedStorage** *(integer) --*

        For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the allocated
        storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns 1, because
        Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.
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

        Contains the details of an Amazon Aurora DB cluster.
        This data type is used as a response element in the ``DescribeDBClusters`` ,
        ``StopDBCluster`` , and ``StartDBCluster`` actions.
        - **AllocatedStorage** *(integer) --*

          For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the
          allocated storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns
          1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts
          as needed.
    """


_ClientStopDbInstanceResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceAssociatedRolesTypeDef(
    _ClientStopDbInstanceResponseDBInstanceAssociatedRolesTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientStopDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientStopDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientStopDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceDomainMembershipsTypeDef(
    _ClientStopDbInstanceResponseDBInstanceDomainMembershipsTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientStopDbInstanceResponseDBInstanceEndpointTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceListenerEndpointTypeDef(
    _ClientStopDbInstanceResponseDBInstanceListenerEndpointTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientStopDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientStopDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientStopDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientStopDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef(
    _ClientStopDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientStopDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientStopDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientStopDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientStopDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceProcessorFeaturesTypeDef(
    _ClientStopDbInstanceResponseDBInstanceProcessorFeaturesTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientStopDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientStopDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientStopDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientStopDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientStopDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[ClientStopDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "DBParameterGroups": List[ClientStopDbInstanceResponseDBInstanceDBParameterGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientStopDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientStopDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientStopDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientStopDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[ClientStopDbInstanceResponseDBInstanceDomainMembershipsTypeDef],
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[ClientStopDbInstanceResponseDBInstanceProcessorFeaturesTypeDef],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientStopDbInstanceResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientStopDbInstanceResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)


class ClientStopDbInstanceResponseDBInstanceTypeDef(_ClientStopDbInstanceResponseDBInstanceTypeDef):
    """
    - **DBInstance** *(dict) --*

      Contains the details of an Amazon RDS DB instance.
      This data type is used as a response element in the ``DescribeDBInstances`` action.
      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
        identifies a DB instance.
    """


_ClientStopDbInstanceResponseTypeDef = TypedDict(
    "_ClientStopDbInstanceResponseTypeDef",
    {"DBInstance": ClientStopDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientStopDbInstanceResponseTypeDef(_ClientStopDbInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **DBInstance** *(dict) --*

        Contains the details of an Amazon RDS DB instance.
        This data type is used as a response element in the ``DescribeDBInstances`` action.
        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.
    """


_DbClusterSnapshotAvailableWaitFiltersTypeDef = TypedDict(
    "_DbClusterSnapshotAvailableWaitFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DbClusterSnapshotAvailableWaitFiltersTypeDef(_DbClusterSnapshotAvailableWaitFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DbClusterSnapshotAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_DbClusterSnapshotAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class DbClusterSnapshotAvailableWaitWaiterConfigTypeDef(
    _DbClusterSnapshotAvailableWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_DbClusterSnapshotDeletedWaitFiltersTypeDef = TypedDict(
    "_DbClusterSnapshotDeletedWaitFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DbClusterSnapshotDeletedWaitFiltersTypeDef(_DbClusterSnapshotDeletedWaitFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DbClusterSnapshotDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_DbClusterSnapshotDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class DbClusterSnapshotDeletedWaitWaiterConfigTypeDef(
    _DbClusterSnapshotDeletedWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_DbInstanceAvailableWaitFiltersTypeDef = TypedDict(
    "_DbInstanceAvailableWaitFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DbInstanceAvailableWaitFiltersTypeDef(_DbInstanceAvailableWaitFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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


_DbInstanceDeletedWaitFiltersTypeDef = TypedDict(
    "_DbInstanceDeletedWaitFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DbInstanceDeletedWaitFiltersTypeDef(_DbInstanceDeletedWaitFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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


_DbSnapshotAvailableWaitFiltersTypeDef = TypedDict(
    "_DbSnapshotAvailableWaitFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DbSnapshotAvailableWaitFiltersTypeDef(_DbSnapshotAvailableWaitFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DbSnapshotAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_DbSnapshotAvailableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class DbSnapshotAvailableWaitWaiterConfigTypeDef(_DbSnapshotAvailableWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_DbSnapshotCompletedWaitFiltersTypeDef = TypedDict(
    "_DbSnapshotCompletedWaitFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DbSnapshotCompletedWaitFiltersTypeDef(_DbSnapshotCompletedWaitFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DbSnapshotCompletedWaitWaiterConfigTypeDef = TypedDict(
    "_DbSnapshotCompletedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class DbSnapshotCompletedWaitWaiterConfigTypeDef(_DbSnapshotCompletedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_DbSnapshotDeletedWaitFiltersTypeDef = TypedDict(
    "_DbSnapshotDeletedWaitFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DbSnapshotDeletedWaitFiltersTypeDef(_DbSnapshotDeletedWaitFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DbSnapshotDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_DbSnapshotDeletedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class DbSnapshotDeletedWaitWaiterConfigTypeDef(_DbSnapshotDeletedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_DescribeCertificatesPaginateFiltersTypeDef = TypedDict(
    "_DescribeCertificatesPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeCertificatesPaginateFiltersTypeDef(_DescribeCertificatesPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCertificatesPaginatePaginationConfigTypeDef(
    _DescribeCertificatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeCertificatesPaginateResponseCertificatesTypeDef = TypedDict(
    "_DescribeCertificatesPaginateResponseCertificatesTypeDef",
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


class DescribeCertificatesPaginateResponseCertificatesTypeDef(
    _DescribeCertificatesPaginateResponseCertificatesTypeDef
):
    """
    - *(dict) --*

      A CA certificate for an AWS account.
      - **CertificateIdentifier** *(string) --*

        The unique key that identifies a certificate.
    """


_DescribeCertificatesPaginateResponseTypeDef = TypedDict(
    "_DescribeCertificatesPaginateResponseTypeDef",
    {
        "Certificates": List[DescribeCertificatesPaginateResponseCertificatesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeCertificatesPaginateResponseTypeDef(_DescribeCertificatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Data returned by the **DescribeCertificates** action.
      - **Certificates** *(list) --*

        The list of ``Certificate`` objects for the AWS account.
        - *(dict) --*

          A CA certificate for an AWS account.
          - **CertificateIdentifier** *(string) --*

            The unique key that identifies a certificate.
    """


_DescribeCustomAvailabilityZonesPaginateFiltersTypeDef = TypedDict(
    "_DescribeCustomAvailabilityZonesPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeCustomAvailabilityZonesPaginateFiltersTypeDef(
    _DescribeCustomAvailabilityZonesPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeCustomAvailabilityZonesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCustomAvailabilityZonesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCustomAvailabilityZonesPaginatePaginationConfigTypeDef(
    _DescribeCustomAvailabilityZonesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeCustomAvailabilityZonesPaginateResponseCustomAvailabilityZonesVpnDetailsTypeDef = TypedDict(
    "_DescribeCustomAvailabilityZonesPaginateResponseCustomAvailabilityZonesVpnDetailsTypeDef",
    {
        "VpnId": str,
        "VpnTunnelOriginatorIP": str,
        "VpnGatewayIp": str,
        "VpnPSK": str,
        "VpnName": str,
        "VpnState": str,
    },
    total=False,
)


class DescribeCustomAvailabilityZonesPaginateResponseCustomAvailabilityZonesVpnDetailsTypeDef(
    _DescribeCustomAvailabilityZonesPaginateResponseCustomAvailabilityZonesVpnDetailsTypeDef
):
    pass


_DescribeCustomAvailabilityZonesPaginateResponseCustomAvailabilityZonesTypeDef = TypedDict(
    "_DescribeCustomAvailabilityZonesPaginateResponseCustomAvailabilityZonesTypeDef",
    {
        "CustomAvailabilityZoneId": str,
        "CustomAvailabilityZoneName": str,
        "CustomAvailabilityZoneStatus": str,
        "VpnDetails": DescribeCustomAvailabilityZonesPaginateResponseCustomAvailabilityZonesVpnDetailsTypeDef,
    },
    total=False,
)


class DescribeCustomAvailabilityZonesPaginateResponseCustomAvailabilityZonesTypeDef(
    _DescribeCustomAvailabilityZonesPaginateResponseCustomAvailabilityZonesTypeDef
):
    """
    - *(dict) --*

      A custom Availability Zone (AZ) is an on-premises AZ that is integrated with a VMware vSphere
      cluster.
      For more information about RDS on VMware, see the ` *RDS on VMware User Guide.*
      https://docs.aws.amazon.com/AmazonRDS/latest/RDSonVMwareUserGuide/rds-on-vmware.html`__
      - **CustomAvailabilityZoneId** *(string) --*

        The identifier of the custom AZ.
        Amazon RDS generates a unique identifier when a custom AZ is created.
    """


_DescribeCustomAvailabilityZonesPaginateResponseTypeDef = TypedDict(
    "_DescribeCustomAvailabilityZonesPaginateResponseTypeDef",
    {
        "CustomAvailabilityZones": List[
            DescribeCustomAvailabilityZonesPaginateResponseCustomAvailabilityZonesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeCustomAvailabilityZonesPaginateResponseTypeDef(
    _DescribeCustomAvailabilityZonesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **CustomAvailabilityZones** *(list) --*

        The list of  CustomAvailabilityZone objects for the AWS account.
        - *(dict) --*

          A custom Availability Zone (AZ) is an on-premises AZ that is integrated with a VMware
          vSphere cluster.
          For more information about RDS on VMware, see the ` *RDS on VMware User Guide.*
          https://docs.aws.amazon.com/AmazonRDS/latest/RDSonVMwareUserGuide/rds-on-vmware.html`__
          - **CustomAvailabilityZoneId** *(string) --*

            The identifier of the custom AZ.
            Amazon RDS generates a unique identifier when a custom AZ is created.
    """


_DescribeDBClusterBacktracksPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBClusterBacktracksPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeDBClusterBacktracksPaginateFiltersTypeDef(
    _DescribeDBClusterBacktracksPaginateFiltersTypeDef
):
    pass


_DescribeDBClusterBacktracksPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBClusterBacktracksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBClusterBacktracksPaginatePaginationConfigTypeDef(
    _DescribeDBClusterBacktracksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBClusterBacktracksPaginateResponseDBClusterBacktracksTypeDef = TypedDict(
    "_DescribeDBClusterBacktracksPaginateResponseDBClusterBacktracksTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": str,
        "BacktrackTo": datetime,
        "BacktrackedFrom": datetime,
        "BacktrackRequestCreationTime": datetime,
        "Status": str,
    },
    total=False,
)


class DescribeDBClusterBacktracksPaginateResponseDBClusterBacktracksTypeDef(
    _DescribeDBClusterBacktracksPaginateResponseDBClusterBacktracksTypeDef
):
    """
    - *(dict) --*

      This data type is used as a response element in the ``DescribeDBClusterBacktracks`` action.
      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.
    """


_DescribeDBClusterBacktracksPaginateResponseTypeDef = TypedDict(
    "_DescribeDBClusterBacktracksPaginateResponseTypeDef",
    {
        "DBClusterBacktracks": List[
            DescribeDBClusterBacktracksPaginateResponseDBClusterBacktracksTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBClusterBacktracksPaginateResponseTypeDef(
    _DescribeDBClusterBacktracksPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeDBClusterBacktracks`` action.
      - **DBClusterBacktracks** *(list) --*

        Contains a list of backtracks for the user.
        - *(dict) --*

          This data type is used as a response element in the ``DescribeDBClusterBacktracks``
          action.
          - **DBClusterIdentifier** *(string) --*

            Contains a user-supplied DB cluster identifier. This identifier is the unique key that
            identifies a DB cluster.
    """


_DescribeDBClusterEndpointsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBClusterEndpointsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeDBClusterEndpointsPaginateFiltersTypeDef(
    _DescribeDBClusterEndpointsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeDBClusterEndpointsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBClusterEndpointsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBClusterEndpointsPaginatePaginationConfigTypeDef(
    _DescribeDBClusterEndpointsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBClusterEndpointsPaginateResponseDBClusterEndpointsTypeDef = TypedDict(
    "_DescribeDBClusterEndpointsPaginateResponseDBClusterEndpointsTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
    },
    total=False,
)


class DescribeDBClusterEndpointsPaginateResponseDBClusterEndpointsTypeDef(
    _DescribeDBClusterEndpointsPaginateResponseDBClusterEndpointsTypeDef
):
    """
    - *(dict) --*

      This data type represents the information you need to connect to an Amazon Aurora DB cluster.
      This data type is used as a response element in the following actions:
      * ``CreateDBClusterEndpoint``
      * ``DescribeDBClusterEndpoints``
      * ``ModifyDBClusterEndpoint``
      * ``DeleteDBClusterEndpoint``
      For the data structure that represents Amazon RDS DB instance endpoints, see ``Endpoint`` .
      - **DBClusterEndpointIdentifier** *(string) --*

        The identifier associated with the endpoint. This parameter is stored as a lowercase string.
    """


_DescribeDBClusterEndpointsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBClusterEndpointsPaginateResponseTypeDef",
    {
        "DBClusterEndpoints": List[
            DescribeDBClusterEndpointsPaginateResponseDBClusterEndpointsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBClusterEndpointsPaginateResponseTypeDef(
    _DescribeDBClusterEndpointsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **DBClusterEndpoints** *(list) --*

        Contains the details of the endpoints associated with the cluster and matching any filter
        conditions.
        - *(dict) --*

          This data type represents the information you need to connect to an Amazon Aurora DB
          cluster. This data type is used as a response element in the following actions:
          * ``CreateDBClusterEndpoint``
          * ``DescribeDBClusterEndpoints``
          * ``ModifyDBClusterEndpoint``
          * ``DeleteDBClusterEndpoint``
          For the data structure that represents Amazon RDS DB instance endpoints, see ``Endpoint``
          .
          - **DBClusterEndpointIdentifier** *(string) --*

            The identifier associated with the endpoint. This parameter is stored as a lowercase
            string.
    """


_DescribeDBClusterParameterGroupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBClusterParameterGroupsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeDBClusterParameterGroupsPaginateFiltersTypeDef(
    _DescribeDBClusterParameterGroupsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      Contains the details of an Amazon RDS DB cluster parameter group.
      This data type is used as a response element in the ``DescribeDBClusterParameterGroups``
      action.
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

          Contains the details of an Amazon RDS DB cluster parameter group.
          This data type is used as a response element in the ``DescribeDBClusterParameterGroups``
          action.
          - **DBClusterParameterGroupName** *(string) --*

            Provides the name of the DB cluster parameter group.
    """


_DescribeDBClusterParametersPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBClusterParametersPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeDBClusterParametersPaginateFiltersTypeDef(
    _DescribeDBClusterParametersPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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
        "SupportedEngineModes": List[str],
    },
    total=False,
)


class DescribeDBClusterParametersPaginateResponseParametersTypeDef(
    _DescribeDBClusterParametersPaginateResponseParametersTypeDef
):
    """
    - *(dict) --*

      This data type is used as a request parameter in the ``ModifyDBParameterGroup`` and
      ``ResetDBParameterGroup`` actions.
      This data type is used as a response element in the ``DescribeEngineDefaultParameters`` and
      ``DescribeDBParameters`` actions.
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

      Provides details about a DB cluster parameter group including the parameters in the DB cluster
      parameter group.
      - **Parameters** *(list) --*

        Provides a list of parameters for the DB cluster parameter group.
        - *(dict) --*

          This data type is used as a request parameter in the ``ModifyDBParameterGroup`` and
          ``ResetDBParameterGroup`` actions.
          This data type is used as a response element in the ``DescribeEngineDefaultParameters``
          and ``DescribeDBParameters`` actions.
          - **ParameterName** *(string) --*

            Specifies the name of the parameter.
    """


_DescribeDBClusterSnapshotsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBClusterSnapshotsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeDBClusterSnapshotsPaginateFiltersTypeDef(
    _DescribeDBClusterSnapshotsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      Contains the details for an Amazon RDS DB cluster snapshot
      This data type is used as a response element in the ``DescribeDBClusterSnapshots`` action.
      - **AvailabilityZones** *(list) --*

        Provides the list of Availability Zones (AZs) where instances in the DB cluster snapshot can
        be restored.
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

      Provides a list of DB cluster snapshots for the user as the result of a call to the
      ``DescribeDBClusterSnapshots`` action.
      - **DBClusterSnapshots** *(list) --*

        Provides a list of DB cluster snapshots for the user.
        - *(dict) --*

          Contains the details for an Amazon RDS DB cluster snapshot
          This data type is used as a response element in the ``DescribeDBClusterSnapshots`` action.
          - **AvailabilityZones** *(list) --*

            Provides the list of Availability Zones (AZs) where instances in the DB cluster snapshot
            can be restored.
            - *(string) --*
    """


_DescribeDBClustersPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBClustersPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeDBClustersPaginateFiltersTypeDef(_DescribeDBClustersPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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
    {"RoleArn": str, "Status": str, "FeatureName": str},
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


_DescribeDBClustersPaginateResponseDBClustersScalingConfigurationInfoTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersScalingConfigurationInfoTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersScalingConfigurationInfoTypeDef
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": DescribeDBClustersPaginateResponseDBClustersScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersTypeDef
):
    """
    - *(dict) --*

      Contains the details of an Amazon Aurora DB cluster.
      This data type is used as a response element in the ``DescribeDBClusters`` , ``StopDBCluster``
      , and ``StartDBCluster`` actions.
      - **AllocatedStorage** *(integer) --*

        For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the allocated
        storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns 1, because
        Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.
    """


_DescribeDBClustersPaginateResponseTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseTypeDef",
    {"DBClusters": List[DescribeDBClustersPaginateResponseDBClustersTypeDef], "NextToken": str},
    total=False,
)


class DescribeDBClustersPaginateResponseTypeDef(_DescribeDBClustersPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeDBClusters`` action.
      - **DBClusters** *(list) --*

        Contains a list of DB clusters for the user.
        - *(dict) --*

          Contains the details of an Amazon Aurora DB cluster.
          This data type is used as a response element in the ``DescribeDBClusters`` ,
          ``StopDBCluster`` , and ``StartDBCluster`` actions.
          - **AllocatedStorage** *(integer) --*

            For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the
            allocated storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always
            returns 1, because Aurora DB cluster storage size isn't fixed, but instead automatically
            adjusts as needed.
    """


_DescribeDBEngineVersionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeDBEngineVersionsPaginateFiltersTypeDef(
    _DescribeDBEngineVersionsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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
        "SupportedEngineModes": List[str],
        "SupportedFeatureNames": List[str],
        "Status": str,
    },
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef
):
    """
    - *(dict) --*

      This data type is used as a response element in the action ``DescribeDBEngineVersions`` .
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

      Contains the result of a successful invocation of the ``DescribeDBEngineVersions`` action.
      - **DBEngineVersions** *(list) --*

        A list of ``DBEngineVersion`` elements.
        - *(dict) --*

          This data type is used as a response element in the action ``DescribeDBEngineVersions`` .
          - **Engine** *(string) --*

            The name of the database engine.
    """


_DescribeDBInstanceAutomatedBackupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBInstanceAutomatedBackupsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeDBInstanceAutomatedBackupsPaginateFiltersTypeDef(
    _DescribeDBInstanceAutomatedBackupsPaginateFiltersTypeDef
):
    pass


_DescribeDBInstanceAutomatedBackupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBInstanceAutomatedBackupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBInstanceAutomatedBackupsPaginatePaginationConfigTypeDef(
    _DescribeDBInstanceAutomatedBackupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBInstanceAutomatedBackupsPaginateResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef = TypedDict(
    "_DescribeDBInstanceAutomatedBackupsPaginateResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef",
    {"EarliestTime": datetime, "LatestTime": datetime},
    total=False,
)


class DescribeDBInstanceAutomatedBackupsPaginateResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef(
    _DescribeDBInstanceAutomatedBackupsPaginateResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef
):
    pass


_DescribeDBInstanceAutomatedBackupsPaginateResponseDBInstanceAutomatedBackupsTypeDef = TypedDict(
    "_DescribeDBInstanceAutomatedBackupsPaginateResponseDBInstanceAutomatedBackupsTypeDef",
    {
        "DBInstanceArn": str,
        "DbiResourceId": str,
        "Region": str,
        "DBInstanceIdentifier": str,
        "RestoreWindow": DescribeDBInstanceAutomatedBackupsPaginateResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "Engine": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "StorageType": str,
        "KmsKeyId": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)


class DescribeDBInstanceAutomatedBackupsPaginateResponseDBInstanceAutomatedBackupsTypeDef(
    _DescribeDBInstanceAutomatedBackupsPaginateResponseDBInstanceAutomatedBackupsTypeDef
):
    """
    - *(dict) --*

      An automated backup of a DB instance. It it consists of system backups, transaction logs, and
      the database instance properties that existed at the time you deleted the source instance.
      - **DBInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) for the automated backup.
    """


_DescribeDBInstanceAutomatedBackupsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBInstanceAutomatedBackupsPaginateResponseTypeDef",
    {
        "DBInstanceAutomatedBackups": List[
            DescribeDBInstanceAutomatedBackupsPaginateResponseDBInstanceAutomatedBackupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBInstanceAutomatedBackupsPaginateResponseTypeDef(
    _DescribeDBInstanceAutomatedBackupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeDBInstanceAutomatedBackups``
      action.
      - **DBInstanceAutomatedBackups** *(list) --*

        A list of ``DBInstanceAutomatedBackup`` instances.
        - *(dict) --*

          An automated backup of a DB instance. It it consists of system backups, transaction logs,
          and the database instance properties that existed at the time you deleted the source
          instance.
          - **DBInstanceArn** *(string) --*

            The Amazon Resource Name (ARN) for the automated backup.
    """


_DescribeDBInstancesPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeDBInstancesPaginateFiltersTypeDef(_DescribeDBInstancesPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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


_DescribeDBInstancesPaginateResponseDBInstancesAssociatedRolesTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesAssociatedRolesTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesAssociatedRolesTypeDef
):
    pass


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


_DescribeDBInstancesPaginateResponseDBInstancesListenerEndpointTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesListenerEndpointTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesListenerEndpointTypeDef
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


_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef
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
        "ProcessorFeatures": List[
            DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef
):
    pass


_DescribeDBInstancesPaginateResponseDBInstancesProcessorFeaturesTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesProcessorFeaturesTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesProcessorFeaturesTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[
            DescribeDBInstancesPaginateResponseDBInstancesProcessorFeaturesTypeDef
        ],
        "DeletionProtection": bool,
        "AssociatedRoles": List[
            DescribeDBInstancesPaginateResponseDBInstancesAssociatedRolesTypeDef
        ],
        "ListenerEndpoint": DescribeDBInstancesPaginateResponseDBInstancesListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesTypeDef
):
    """
    - *(dict) --*

      Contains the details of an Amazon RDS DB instance.
      This data type is used as a response element in the ``DescribeDBInstances`` action.
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

      Contains the result of a successful invocation of the ``DescribeDBInstances`` action.
      - **DBInstances** *(list) --*

        A list of ``DBInstance`` instances.
        - *(dict) --*

          Contains the details of an Amazon RDS DB instance.
          This data type is used as a response element in the ``DescribeDBInstances`` action.
          - **DBInstanceIdentifier** *(string) --*

            Contains a user-supplied database identifier. This identifier is the unique key that
            identifies a DB instance.
    """


_DescribeDBLogFilesPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBLogFilesPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeDBLogFilesPaginateFiltersTypeDef(_DescribeDBLogFilesPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeDBLogFilesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBLogFilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBLogFilesPaginatePaginationConfigTypeDef(
    _DescribeDBLogFilesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBLogFilesPaginateResponseDescribeDBLogFilesTypeDef = TypedDict(
    "_DescribeDBLogFilesPaginateResponseDescribeDBLogFilesTypeDef",
    {"LogFileName": str, "LastWritten": int, "Size": int},
    total=False,
)


class DescribeDBLogFilesPaginateResponseDescribeDBLogFilesTypeDef(
    _DescribeDBLogFilesPaginateResponseDescribeDBLogFilesTypeDef
):
    """
    - *(dict) --*

      This data type is used as a response element to ``DescribeDBLogFiles`` .
      - **LogFileName** *(string) --*

        The name of the log file for the specified DB instance.
    """


_DescribeDBLogFilesPaginateResponseTypeDef = TypedDict(
    "_DescribeDBLogFilesPaginateResponseTypeDef",
    {
        "DescribeDBLogFiles": List[DescribeDBLogFilesPaginateResponseDescribeDBLogFilesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBLogFilesPaginateResponseTypeDef(_DescribeDBLogFilesPaginateResponseTypeDef):
    """
    - *(dict) --*

      The response from a call to ``DescribeDBLogFiles`` .
      - **DescribeDBLogFiles** *(list) --*

        The DB log files returned.
        - *(dict) --*

          This data type is used as a response element to ``DescribeDBLogFiles`` .
          - **LogFileName** *(string) --*

            The name of the log file for the specified DB instance.
    """


_DescribeDBParameterGroupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBParameterGroupsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeDBParameterGroupsPaginateFiltersTypeDef(
    _DescribeDBParameterGroupsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      Contains the details of an Amazon RDS DB parameter group.
      This data type is used as a response element in the ``DescribeDBParameterGroups`` action.
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

      Contains the result of a successful invocation of the ``DescribeDBParameterGroups`` action.
      - **DBParameterGroups** *(list) --*

        A list of ``DBParameterGroup`` instances.
        - *(dict) --*

          Contains the details of an Amazon RDS DB parameter group.
          This data type is used as a response element in the ``DescribeDBParameterGroups`` action.
          - **DBParameterGroupName** *(string) --*

            Provides the name of the DB parameter group.
    """


_DescribeDBParametersPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBParametersPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeDBParametersPaginateFiltersTypeDef(_DescribeDBParametersPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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
        "SupportedEngineModes": List[str],
    },
    total=False,
)


class DescribeDBParametersPaginateResponseParametersTypeDef(
    _DescribeDBParametersPaginateResponseParametersTypeDef
):
    """
    - *(dict) --*

      This data type is used as a request parameter in the ``ModifyDBParameterGroup`` and
      ``ResetDBParameterGroup`` actions.
      This data type is used as a response element in the ``DescribeEngineDefaultParameters`` and
      ``DescribeDBParameters`` actions.
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

      Contains the result of a successful invocation of the ``DescribeDBParameters`` action.
      - **Parameters** *(list) --*

        A list of ``Parameter`` values.
        - *(dict) --*

          This data type is used as a request parameter in the ``ModifyDBParameterGroup`` and
          ``ResetDBParameterGroup`` actions.
          This data type is used as a response element in the ``DescribeEngineDefaultParameters``
          and ``DescribeDBParameters`` actions.
          - **ParameterName** *(string) --*

            Specifies the name of the parameter.
    """


_DescribeDBProxiesPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBProxiesPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeDBProxiesPaginateFiltersTypeDef(_DescribeDBProxiesPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeDBProxiesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBProxiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBProxiesPaginatePaginationConfigTypeDef(
    _DescribeDBProxiesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBProxiesPaginateResponseDBProxiesAuthTypeDef = TypedDict(
    "_DescribeDBProxiesPaginateResponseDBProxiesAuthTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": str,
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)


class DescribeDBProxiesPaginateResponseDBProxiesAuthTypeDef(
    _DescribeDBProxiesPaginateResponseDBProxiesAuthTypeDef
):
    pass


_DescribeDBProxiesPaginateResponseDBProxiesTypeDef = TypedDict(
    "_DescribeDBProxiesPaginateResponseDBProxiesTypeDef",
    {
        "DBProxyName": str,
        "DBProxyArn": str,
        "Status": Literal[
            "available",
            "modifying",
            "incompatible-network",
            "insufficient-resource-limits",
            "creating",
            "deleting",
        ],
        "EngineFamily": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Auth": List[DescribeDBProxiesPaginateResponseDBProxiesAuthTypeDef],
        "RoleArn": str,
        "Endpoint": str,
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)


class DescribeDBProxiesPaginateResponseDBProxiesTypeDef(
    _DescribeDBProxiesPaginateResponseDBProxiesTypeDef
):
    """
    - *(dict) --*

      .. note::

        This is prerelease documentation for the RDS Database Proxy feature in preview release. It
        is subject to change.
    """


_DescribeDBProxiesPaginateResponseTypeDef = TypedDict(
    "_DescribeDBProxiesPaginateResponseTypeDef",
    {"DBProxies": List[DescribeDBProxiesPaginateResponseDBProxiesTypeDef], "NextToken": str},
    total=False,
)


class DescribeDBProxiesPaginateResponseTypeDef(_DescribeDBProxiesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **DBProxies** *(list) --*

        A return value representing an arbitrary number of ``DBProxy`` data structures.
        - *(dict) --*

          .. note::

            This is prerelease documentation for the RDS Database Proxy feature in preview release.
            It is subject to change.
    """


_DescribeDBProxyTargetGroupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBProxyTargetGroupsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeDBProxyTargetGroupsPaginateFiltersTypeDef(
    _DescribeDBProxyTargetGroupsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeDBProxyTargetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBProxyTargetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBProxyTargetGroupsPaginatePaginationConfigTypeDef(
    _DescribeDBProxyTargetGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBProxyTargetGroupsPaginateResponseTargetGroupsConnectionPoolConfigTypeDef = TypedDict(
    "_DescribeDBProxyTargetGroupsPaginateResponseTargetGroupsConnectionPoolConfigTypeDef",
    {
        "MaxConnectionsPercent": int,
        "MaxIdleConnectionsPercent": int,
        "ConnectionBorrowTimeout": int,
        "SessionPinningFilters": List[str],
        "InitQuery": str,
    },
    total=False,
)


class DescribeDBProxyTargetGroupsPaginateResponseTargetGroupsConnectionPoolConfigTypeDef(
    _DescribeDBProxyTargetGroupsPaginateResponseTargetGroupsConnectionPoolConfigTypeDef
):
    pass


_DescribeDBProxyTargetGroupsPaginateResponseTargetGroupsTypeDef = TypedDict(
    "_DescribeDBProxyTargetGroupsPaginateResponseTargetGroupsTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": str,
        "TargetGroupArn": str,
        "IsDefault": bool,
        "Status": str,
        "ConnectionPoolConfig": DescribeDBProxyTargetGroupsPaginateResponseTargetGroupsConnectionPoolConfigTypeDef,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)


class DescribeDBProxyTargetGroupsPaginateResponseTargetGroupsTypeDef(
    _DescribeDBProxyTargetGroupsPaginateResponseTargetGroupsTypeDef
):
    """
    - *(dict) --*

      .. note::

        This is prerelease documentation for the RDS Database Proxy feature in preview release. It
        is subject to change.
    """


_DescribeDBProxyTargetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBProxyTargetGroupsPaginateResponseTypeDef",
    {
        "TargetGroups": List[DescribeDBProxyTargetGroupsPaginateResponseTargetGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBProxyTargetGroupsPaginateResponseTypeDef(
    _DescribeDBProxyTargetGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **TargetGroups** *(list) --*

        An arbitrary number of ``DBProxyTargetGroup`` objects, containing details of the
        corresponding target groups.
        - *(dict) --*

          .. note::

            This is prerelease documentation for the RDS Database Proxy feature in preview release.
            It is subject to change.
    """


_DescribeDBProxyTargetsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBProxyTargetsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeDBProxyTargetsPaginateFiltersTypeDef(_DescribeDBProxyTargetsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeDBProxyTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBProxyTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBProxyTargetsPaginatePaginationConfigTypeDef(
    _DescribeDBProxyTargetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBProxyTargetsPaginateResponseTargetsTypeDef = TypedDict(
    "_DescribeDBProxyTargetsPaginateResponseTargetsTypeDef",
    {
        "TargetArn": str,
        "Endpoint": str,
        "TrackedClusterId": str,
        "RdsResourceId": str,
        "Port": int,
        "Type": Literal["RDS_INSTANCE", "RDS_SERVERLESS_ENDPOINT", "TRACKED_CLUSTER"],
    },
    total=False,
)


class DescribeDBProxyTargetsPaginateResponseTargetsTypeDef(
    _DescribeDBProxyTargetsPaginateResponseTargetsTypeDef
):
    """
    - *(dict) --*

      .. note::

        This is prerelease documentation for the RDS Database Proxy feature in preview release. It
        is subject to change.
    """


_DescribeDBProxyTargetsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBProxyTargetsPaginateResponseTypeDef",
    {"Targets": List[DescribeDBProxyTargetsPaginateResponseTargetsTypeDef], "NextToken": str},
    total=False,
)


class DescribeDBProxyTargetsPaginateResponseTypeDef(_DescribeDBProxyTargetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Targets** *(list) --*

        An arbitrary number of ``DBProxyTarget`` objects, containing details of the corresponding
        targets.
        - *(dict) --*

          .. note::

            This is prerelease documentation for the RDS Database Proxy feature in preview release.
            It is subject to change.
    """


_DescribeDBSecurityGroupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBSecurityGroupsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeDBSecurityGroupsPaginateFiltersTypeDef(
    _DescribeDBSecurityGroupsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeDBSecurityGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBSecurityGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBSecurityGroupsPaginatePaginationConfigTypeDef(
    _DescribeDBSecurityGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsEC2SecurityGroupsTypeDef = TypedDict(
    "_DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)


class DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsEC2SecurityGroupsTypeDef(
    _DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsEC2SecurityGroupsTypeDef
):
    pass


_DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsIPRangesTypeDef = TypedDict(
    "_DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsIPRangesTypeDef",
    {"Status": str, "CIDRIP": str},
    total=False,
)


class DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsIPRangesTypeDef(
    _DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsIPRangesTypeDef
):
    pass


_DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsTypeDef = TypedDict(
    "_DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsTypeDef",
    {
        "OwnerId": str,
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "VpcId": str,
        "EC2SecurityGroups": List[
            DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsIPRangesTypeDef],
        "DBSecurityGroupArn": str,
    },
    total=False,
)


class DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsTypeDef(
    _DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsTypeDef
):
    """
    - *(dict) --*

      Contains the details for an Amazon RDS DB security group.
      This data type is used as a response element in the ``DescribeDBSecurityGroups`` action.
      - **OwnerId** *(string) --*

        Provides the AWS ID of the owner of a specific DB security group.
    """


_DescribeDBSecurityGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBSecurityGroupsPaginateResponseTypeDef",
    {
        "DBSecurityGroups": List[DescribeDBSecurityGroupsPaginateResponseDBSecurityGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBSecurityGroupsPaginateResponseTypeDef(
    _DescribeDBSecurityGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeDBSecurityGroups`` action.
      - **DBSecurityGroups** *(list) --*

        A list of ``DBSecurityGroup`` instances.
        - *(dict) --*

          Contains the details for an Amazon RDS DB security group.
          This data type is used as a response element in the ``DescribeDBSecurityGroups`` action.
          - **OwnerId** *(string) --*

            Provides the AWS ID of the owner of a specific DB security group.
    """


_DescribeDBSnapshotsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBSnapshotsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeDBSnapshotsPaginateFiltersTypeDef(_DescribeDBSnapshotsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeDBSnapshotsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBSnapshotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBSnapshotsPaginatePaginationConfigTypeDef(
    _DescribeDBSnapshotsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDBSnapshotsPaginateResponseDBSnapshotsProcessorFeaturesTypeDef = TypedDict(
    "_DescribeDBSnapshotsPaginateResponseDBSnapshotsProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeDBSnapshotsPaginateResponseDBSnapshotsProcessorFeaturesTypeDef(
    _DescribeDBSnapshotsPaginateResponseDBSnapshotsProcessorFeaturesTypeDef
):
    pass


_DescribeDBSnapshotsPaginateResponseDBSnapshotsTypeDef = TypedDict(
    "_DescribeDBSnapshotsPaginateResponseDBSnapshotsTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List[
            DescribeDBSnapshotsPaginateResponseDBSnapshotsProcessorFeaturesTypeDef
        ],
        "DbiResourceId": str,
    },
    total=False,
)


class DescribeDBSnapshotsPaginateResponseDBSnapshotsTypeDef(
    _DescribeDBSnapshotsPaginateResponseDBSnapshotsTypeDef
):
    """
    - *(dict) --*

      Contains the details of an Amazon RDS DB snapshot.
      This data type is used as a response element in the ``DescribeDBSnapshots`` action.
      - **DBSnapshotIdentifier** *(string) --*

        Specifies the identifier for the DB snapshot.
    """


_DescribeDBSnapshotsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBSnapshotsPaginateResponseTypeDef",
    {"DBSnapshots": List[DescribeDBSnapshotsPaginateResponseDBSnapshotsTypeDef], "NextToken": str},
    total=False,
)


class DescribeDBSnapshotsPaginateResponseTypeDef(_DescribeDBSnapshotsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeDBSnapshots`` action.
      - **DBSnapshots** *(list) --*

        A list of ``DBSnapshot`` instances.
        - *(dict) --*

          Contains the details of an Amazon RDS DB snapshot.
          This data type is used as a response element in the ``DescribeDBSnapshots`` action.
          - **DBSnapshotIdentifier** *(string) --*

            Specifies the identifier for the DB snapshot.
    """


_DescribeDBSubnetGroupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeDBSubnetGroupsPaginateFiltersTypeDef(_DescribeDBSubnetGroupsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      Contains the details of an Amazon RDS DB subnet group.
      This data type is used as a response element in the ``DescribeDBSubnetGroups`` action.
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

      Contains the result of a successful invocation of the ``DescribeDBSubnetGroups`` action.
      - **DBSubnetGroups** *(list) --*

        A list of ``DBSubnetGroup`` instances.
        - *(dict) --*

          Contains the details of an Amazon RDS DB subnet group.
          This data type is used as a response element in the ``DescribeDBSubnetGroups`` action.
          - **DBSubnetGroupName** *(string) --*

            The name of the DB subnet group.
    """


_DescribeEngineDefaultClusterParametersPaginateFiltersTypeDef = TypedDict(
    "_DescribeEngineDefaultClusterParametersPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeEngineDefaultClusterParametersPaginateFiltersTypeDef(
    _DescribeEngineDefaultClusterParametersPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeEngineDefaultClusterParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEngineDefaultClusterParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEngineDefaultClusterParametersPaginatePaginationConfigTypeDef(
    _DescribeEngineDefaultClusterParametersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEngineDefaultClusterParametersPaginateResponseEngineDefaultsParametersTypeDef = TypedDict(
    "_DescribeEngineDefaultClusterParametersPaginateResponseEngineDefaultsParametersTypeDef",
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
        "SupportedEngineModes": List[str],
    },
    total=False,
)


class DescribeEngineDefaultClusterParametersPaginateResponseEngineDefaultsParametersTypeDef(
    _DescribeEngineDefaultClusterParametersPaginateResponseEngineDefaultsParametersTypeDef
):
    pass


_DescribeEngineDefaultClusterParametersPaginateResponseEngineDefaultsTypeDef = TypedDict(
    "_DescribeEngineDefaultClusterParametersPaginateResponseEngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            DescribeEngineDefaultClusterParametersPaginateResponseEngineDefaultsParametersTypeDef
        ],
    },
    total=False,
)


class DescribeEngineDefaultClusterParametersPaginateResponseEngineDefaultsTypeDef(
    _DescribeEngineDefaultClusterParametersPaginateResponseEngineDefaultsTypeDef
):
    """
    - **EngineDefaults** *(dict) --*

      Contains the result of a successful invocation of the ``DescribeEngineDefaultParameters``
      action.
      - **DBParameterGroupFamily** *(string) --*

        Specifies the name of the DB parameter group family that the engine default parameters apply
        to.
    """


_DescribeEngineDefaultClusterParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeEngineDefaultClusterParametersPaginateResponseTypeDef",
    {
        "EngineDefaults": DescribeEngineDefaultClusterParametersPaginateResponseEngineDefaultsTypeDef,
        "NextToken": str,
    },
    total=False,
)


class DescribeEngineDefaultClusterParametersPaginateResponseTypeDef(
    _DescribeEngineDefaultClusterParametersPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **EngineDefaults** *(dict) --*

        Contains the result of a successful invocation of the ``DescribeEngineDefaultParameters``
        action.
        - **DBParameterGroupFamily** *(string) --*

          Specifies the name of the DB parameter group family that the engine default parameters
          apply to.
    """


_DescribeEngineDefaultParametersPaginateFiltersTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeEngineDefaultParametersPaginateFiltersTypeDef(
    _DescribeEngineDefaultParametersPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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
        "SupportedEngineModes": List[str],
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

      Contains the result of a successful invocation of the ``DescribeEngineDefaultParameters``
      action.
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

        Contains the result of a successful invocation of the ``DescribeEngineDefaultParameters``
        action.
        - **DBParameterGroupFamily** *(string) --*

          Specifies the name of the DB parameter group family that the engine default parameters
          apply to.
    """


_DescribeEventSubscriptionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeEventSubscriptionsPaginateFiltersTypeDef(
    _DescribeEventSubscriptionsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      Contains the results of a successful invocation of the ``DescribeEventSubscriptions`` action.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the RDS event notification subscription.
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

      Data returned by the **DescribeEventSubscriptions** action.
      - **EventSubscriptionsList** *(list) --*

        A list of EventSubscriptions data types.
        - *(dict) --*

          Contains the results of a successful invocation of the ``DescribeEventSubscriptions``
          action.
          - **CustomerAwsId** *(string) --*

            The AWS customer account associated with the RDS event notification subscription.
    """


_DescribeEventsPaginateFiltersTypeDef = TypedDict(
    "_DescribeEventsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeEventsPaginateFiltersTypeDef(_DescribeEventsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      This data type is used as a response element in the ``DescribeEvents`` action.
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

      Contains the result of a successful invocation of the ``DescribeEvents`` action.
      - **Events** *(list) --*

        A list of ``Event`` instances.
        - *(dict) --*

          This data type is used as a response element in the ``DescribeEvents`` action.
          - **SourceIdentifier** *(string) --*

            Provides the identifier for the source of the event.
    """


_DescribeGlobalClustersPaginateFiltersTypeDef = TypedDict(
    "_DescribeGlobalClustersPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeGlobalClustersPaginateFiltersTypeDef(_DescribeGlobalClustersPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeGlobalClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeGlobalClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeGlobalClustersPaginatePaginationConfigTypeDef(
    _DescribeGlobalClustersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeGlobalClustersPaginateResponseGlobalClustersGlobalClusterMembersTypeDef = TypedDict(
    "_DescribeGlobalClustersPaginateResponseGlobalClustersGlobalClusterMembersTypeDef",
    {"DBClusterArn": str, "Readers": List[str], "IsWriter": bool},
    total=False,
)


class DescribeGlobalClustersPaginateResponseGlobalClustersGlobalClusterMembersTypeDef(
    _DescribeGlobalClustersPaginateResponseGlobalClustersGlobalClusterMembersTypeDef
):
    pass


_DescribeGlobalClustersPaginateResponseGlobalClustersTypeDef = TypedDict(
    "_DescribeGlobalClustersPaginateResponseGlobalClustersTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List[
            DescribeGlobalClustersPaginateResponseGlobalClustersGlobalClusterMembersTypeDef
        ],
    },
    total=False,
)


class DescribeGlobalClustersPaginateResponseGlobalClustersTypeDef(
    _DescribeGlobalClustersPaginateResponseGlobalClustersTypeDef
):
    """
    - *(dict) --*

      A data type representing an Aurora global database.
      - **GlobalClusterIdentifier** *(string) --*

        Contains a user-supplied global database cluster identifier. This identifier is the unique
        key that identifies a global database cluster.
    """


_DescribeGlobalClustersPaginateResponseTypeDef = TypedDict(
    "_DescribeGlobalClustersPaginateResponseTypeDef",
    {
        "GlobalClusters": List[DescribeGlobalClustersPaginateResponseGlobalClustersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeGlobalClustersPaginateResponseTypeDef(_DescribeGlobalClustersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **GlobalClusters** *(list) --*

        The list of global clusters returned by this request.
        - *(dict) --*

          A data type representing an Aurora global database.
          - **GlobalClusterIdentifier** *(string) --*

            Contains a user-supplied global database cluster identifier. This identifier is the
            unique key that identifies a global database cluster.
    """


_DescribeInstallationMediaPaginateFiltersTypeDef = TypedDict(
    "_DescribeInstallationMediaPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeInstallationMediaPaginateFiltersTypeDef(
    _DescribeInstallationMediaPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeInstallationMediaPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeInstallationMediaPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeInstallationMediaPaginatePaginationConfigTypeDef(
    _DescribeInstallationMediaPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeInstallationMediaPaginateResponseInstallationMediaFailureCauseTypeDef = TypedDict(
    "_DescribeInstallationMediaPaginateResponseInstallationMediaFailureCauseTypeDef",
    {"Message": str},
    total=False,
)


class DescribeInstallationMediaPaginateResponseInstallationMediaFailureCauseTypeDef(
    _DescribeInstallationMediaPaginateResponseInstallationMediaFailureCauseTypeDef
):
    pass


_DescribeInstallationMediaPaginateResponseInstallationMediaTypeDef = TypedDict(
    "_DescribeInstallationMediaPaginateResponseInstallationMediaTypeDef",
    {
        "InstallationMediaId": str,
        "CustomAvailabilityZoneId": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineInstallationMediaPath": str,
        "OSInstallationMediaPath": str,
        "Status": str,
        "FailureCause": DescribeInstallationMediaPaginateResponseInstallationMediaFailureCauseTypeDef,
    },
    total=False,
)


class DescribeInstallationMediaPaginateResponseInstallationMediaTypeDef(
    _DescribeInstallationMediaPaginateResponseInstallationMediaTypeDef
):
    """
    - *(dict) --*

      Contains the installation media for a DB engine that requires an on-premises customer provided
      license, such as Microsoft SQL Server.
      - **InstallationMediaId** *(string) --*

        The installation medium ID.
    """


_DescribeInstallationMediaPaginateResponseTypeDef = TypedDict(
    "_DescribeInstallationMediaPaginateResponseTypeDef",
    {
        "InstallationMedia": List[
            DescribeInstallationMediaPaginateResponseInstallationMediaTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeInstallationMediaPaginateResponseTypeDef(
    _DescribeInstallationMediaPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **InstallationMedia** *(list) --*

        The list of  InstallationMedia objects for the AWS account.
        - *(dict) --*

          Contains the installation media for a DB engine that requires an on-premises customer
          provided license, such as Microsoft SQL Server.
          - **InstallationMediaId** *(string) --*

            The installation medium ID.
    """


_DescribeOptionGroupOptionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeOptionGroupOptionsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeOptionGroupOptionsPaginateFiltersTypeDef(
    _DescribeOptionGroupOptionsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeOptionGroupOptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeOptionGroupOptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeOptionGroupOptionsPaginatePaginationConfigTypeDef(
    _DescribeOptionGroupOptionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef = TypedDict(
    "_DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef",
    {"AllowedValue": str, "MinimumEngineVersion": str},
    total=False,
)


class DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef(
    _DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef
):
    pass


_DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef = TypedDict(
    "_DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef",
    {
        "SettingName": str,
        "SettingDescription": str,
        "DefaultValue": str,
        "ApplyType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsRequired": bool,
        "MinimumEngineVersionPerAllowedValue": List[
            DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef
        ],
    },
    total=False,
)


class DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef(
    _DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef
):
    pass


_DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef = TypedDict(
    "_DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef",
    {"Version": str, "IsDefault": bool},
    total=False,
)


class DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef(
    _DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef
):
    pass


_DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsTypeDef = TypedDict(
    "_DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsTypeDef",
    {
        "Name": str,
        "Description": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "MinimumRequiredMinorEngineVersion": str,
        "PortRequired": bool,
        "DefaultPort": int,
        "OptionsDependedOn": List[str],
        "OptionsConflictsWith": List[str],
        "Persistent": bool,
        "Permanent": bool,
        "RequiresAutoMinorEngineVersionUpgrade": bool,
        "VpcOnly": bool,
        "SupportsOptionVersionDowngrade": bool,
        "OptionGroupOptionSettings": List[
            DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef
        ],
        "OptionGroupOptionVersions": List[
            DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef
        ],
    },
    total=False,
)


class DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsTypeDef(
    _DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsTypeDef
):
    """
    - *(dict) --*

      Available option.
      - **Name** *(string) --*

        The name of the option.
    """


_DescribeOptionGroupOptionsPaginateResponseTypeDef = TypedDict(
    "_DescribeOptionGroupOptionsPaginateResponseTypeDef",
    {
        "OptionGroupOptions": List[
            DescribeOptionGroupOptionsPaginateResponseOptionGroupOptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeOptionGroupOptionsPaginateResponseTypeDef(
    _DescribeOptionGroupOptionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **OptionGroupOptions** *(list) --*

        List of available option group options.
        - *(dict) --*

          Available option.
          - **Name** *(string) --*

            The name of the option.
    """


_DescribeOptionGroupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeOptionGroupsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeOptionGroupsPaginateFiltersTypeDef(_DescribeOptionGroupsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeOptionGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeOptionGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeOptionGroupsPaginatePaginationConfigTypeDef(
    _DescribeOptionGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef = TypedDict(
    "_DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef(
    _DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef
):
    pass


_DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsOptionSettingsTypeDef = TypedDict(
    "_DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsOptionSettingsTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)


class DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsOptionSettingsTypeDef(
    _DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsOptionSettingsTypeDef
):
    pass


_DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef = TypedDict(
    "_DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef(
    _DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef
):
    pass


_DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsTypeDef = TypedDict(
    "_DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsTypeDef",
    {
        "OptionName": str,
        "OptionDescription": str,
        "Persistent": bool,
        "Permanent": bool,
        "Port": int,
        "OptionVersion": str,
        "OptionSettings": List[
            DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsOptionSettingsTypeDef
        ],
        "DBSecurityGroupMemberships": List[
            DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef
        ],
        "VpcSecurityGroupMemberships": List[
            DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef
        ],
    },
    total=False,
)


class DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsTypeDef(
    _DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsTypeDef
):
    pass


_DescribeOptionGroupsPaginateResponseOptionGroupsListTypeDef = TypedDict(
    "_DescribeOptionGroupsPaginateResponseOptionGroupsListTypeDef",
    {
        "OptionGroupName": str,
        "OptionGroupDescription": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "Options": List[DescribeOptionGroupsPaginateResponseOptionGroupsListOptionsTypeDef],
        "AllowsVpcAndNonVpcInstanceMemberships": bool,
        "VpcId": str,
        "OptionGroupArn": str,
    },
    total=False,
)


class DescribeOptionGroupsPaginateResponseOptionGroupsListTypeDef(
    _DescribeOptionGroupsPaginateResponseOptionGroupsListTypeDef
):
    """
    - *(dict) --*

      - **OptionGroupName** *(string) --*

        Specifies the name of the option group.
    """


_DescribeOptionGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeOptionGroupsPaginateResponseTypeDef",
    {
        "OptionGroupsList": List[DescribeOptionGroupsPaginateResponseOptionGroupsListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeOptionGroupsPaginateResponseTypeDef(_DescribeOptionGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      List of option groups.
      - **OptionGroupsList** *(list) --*

        List of option groups.
        - *(dict) --*

          - **OptionGroupName** *(string) --*

            Specifies the name of the option group.
    """


_DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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


_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef",
    {"Name": str, "DefaultValue": str, "AllowedValues": str},
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef
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
        "AvailableProcessorFeatures": List[
            DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef
        ],
        "SupportedEngineModes": List[str],
        "SupportsStorageAutoscaling": bool,
        "SupportsKerberosAuthentication": bool,
    },
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef
):
    """
    - *(dict) --*

      Contains a list of available options for a DB instance.
      This data type is used as a response element in the ``DescribeOrderableDBInstanceOptions``
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

      Contains the result of a successful invocation of the ``DescribeOrderableDBInstanceOptions``
      action.
      - **OrderableDBInstanceOptions** *(list) --*

        An ``OrderableDBInstanceOption`` structure containing information about orderable options
        for the DB instance.
        - *(dict) --*

          Contains a list of available options for a DB instance.
          This data type is used as a response element in the ``DescribeOrderableDBInstanceOptions``
          action.
          - **Engine** *(string) --*

            The engine type of a DB instance.
    """


_DescribePendingMaintenanceActionsPaginateFiltersTypeDef = TypedDict(
    "_DescribePendingMaintenanceActionsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribePendingMaintenanceActionsPaginateFiltersTypeDef(
    _DescribePendingMaintenanceActionsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
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

      Data returned from the **DescribePendingMaintenanceActions** action.
      - **PendingMaintenanceActions** *(list) --*

        A list of the pending maintenance actions for the resource.
        - *(dict) --*

          Describes the pending maintenance actions for a resource.
          - **ResourceIdentifier** *(string) --*

            The ARN of the resource that has pending maintenance actions.
    """


_DescribeReservedDBInstancesOfferingsPaginateFiltersTypeDef = TypedDict(
    "_DescribeReservedDBInstancesOfferingsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeReservedDBInstancesOfferingsPaginateFiltersTypeDef(
    _DescribeReservedDBInstancesOfferingsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeReservedDBInstancesOfferingsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReservedDBInstancesOfferingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReservedDBInstancesOfferingsPaginatePaginationConfigTypeDef(
    _DescribeReservedDBInstancesOfferingsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReservedDBInstancesOfferingsPaginateResponseReservedDBInstancesOfferingsRecurringChargesTypeDef = TypedDict(
    "_DescribeReservedDBInstancesOfferingsPaginateResponseReservedDBInstancesOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class DescribeReservedDBInstancesOfferingsPaginateResponseReservedDBInstancesOfferingsRecurringChargesTypeDef(
    _DescribeReservedDBInstancesOfferingsPaginateResponseReservedDBInstancesOfferingsRecurringChargesTypeDef
):
    pass


_DescribeReservedDBInstancesOfferingsPaginateResponseReservedDBInstancesOfferingsTypeDef = TypedDict(
    "_DescribeReservedDBInstancesOfferingsPaginateResponseReservedDBInstancesOfferingsTypeDef",
    {
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "RecurringCharges": List[
            DescribeReservedDBInstancesOfferingsPaginateResponseReservedDBInstancesOfferingsRecurringChargesTypeDef
        ],
    },
    total=False,
)


class DescribeReservedDBInstancesOfferingsPaginateResponseReservedDBInstancesOfferingsTypeDef(
    _DescribeReservedDBInstancesOfferingsPaginateResponseReservedDBInstancesOfferingsTypeDef
):
    """
    - *(dict) --*

      This data type is used as a response element in the ``DescribeReservedDBInstancesOfferings``
      action.
      - **ReservedDBInstancesOfferingId** *(string) --*

        The offering identifier.
    """


_DescribeReservedDBInstancesOfferingsPaginateResponseTypeDef = TypedDict(
    "_DescribeReservedDBInstancesOfferingsPaginateResponseTypeDef",
    {
        "ReservedDBInstancesOfferings": List[
            DescribeReservedDBInstancesOfferingsPaginateResponseReservedDBInstancesOfferingsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReservedDBInstancesOfferingsPaginateResponseTypeDef(
    _DescribeReservedDBInstancesOfferingsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeReservedDBInstancesOfferings``
      action.
      - **ReservedDBInstancesOfferings** *(list) --*

        A list of reserved DB instance offerings.
        - *(dict) --*

          This data type is used as a response element in the
          ``DescribeReservedDBInstancesOfferings`` action.
          - **ReservedDBInstancesOfferingId** *(string) --*

            The offering identifier.
    """


_DescribeReservedDBInstancesPaginateFiltersTypeDef = TypedDict(
    "_DescribeReservedDBInstancesPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeReservedDBInstancesPaginateFiltersTypeDef(
    _DescribeReservedDBInstancesPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeReservedDBInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReservedDBInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReservedDBInstancesPaginatePaginationConfigTypeDef(
    _DescribeReservedDBInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReservedDBInstancesPaginateResponseReservedDBInstancesRecurringChargesTypeDef = TypedDict(
    "_DescribeReservedDBInstancesPaginateResponseReservedDBInstancesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class DescribeReservedDBInstancesPaginateResponseReservedDBInstancesRecurringChargesTypeDef(
    _DescribeReservedDBInstancesPaginateResponseReservedDBInstancesRecurringChargesTypeDef
):
    pass


_DescribeReservedDBInstancesPaginateResponseReservedDBInstancesTypeDef = TypedDict(
    "_DescribeReservedDBInstancesPaginateResponseReservedDBInstancesTypeDef",
    {
        "ReservedDBInstanceId": str,
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "DBInstanceCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "State": str,
        "RecurringCharges": List[
            DescribeReservedDBInstancesPaginateResponseReservedDBInstancesRecurringChargesTypeDef
        ],
        "ReservedDBInstanceArn": str,
        "LeaseId": str,
    },
    total=False,
)


class DescribeReservedDBInstancesPaginateResponseReservedDBInstancesTypeDef(
    _DescribeReservedDBInstancesPaginateResponseReservedDBInstancesTypeDef
):
    """
    - *(dict) --*

      This data type is used as a response element in the ``DescribeReservedDBInstances`` and
      ``PurchaseReservedDBInstancesOffering`` actions.
      - **ReservedDBInstanceId** *(string) --*

        The unique identifier for the reservation.
    """


_DescribeReservedDBInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeReservedDBInstancesPaginateResponseTypeDef",
    {
        "ReservedDBInstances": List[
            DescribeReservedDBInstancesPaginateResponseReservedDBInstancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReservedDBInstancesPaginateResponseTypeDef(
    _DescribeReservedDBInstancesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeReservedDBInstances`` action.
      - **ReservedDBInstances** *(list) --*

        A list of reserved DB instances.
        - *(dict) --*

          This data type is used as a response element in the ``DescribeReservedDBInstances`` and
          ``PurchaseReservedDBInstancesOffering`` actions.
          - **ReservedDBInstanceId** *(string) --*

            The unique identifier for the reservation.
    """


_DescribeSourceRegionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeSourceRegionsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeSourceRegionsPaginateFiltersTypeDef(_DescribeSourceRegionsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results from a
      describe operation. Filters can be used to match a set of resources by specific criteria, such
      as IDs. The filters supported by a describe operation are documented with the describe
      operation.
      .. note::

        Currently, wildcards are not supported in filters.
    """


_DescribeSourceRegionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSourceRegionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSourceRegionsPaginatePaginationConfigTypeDef(
    _DescribeSourceRegionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeSourceRegionsPaginateResponseSourceRegionsTypeDef = TypedDict(
    "_DescribeSourceRegionsPaginateResponseSourceRegionsTypeDef",
    {"RegionName": str, "Endpoint": str, "Status": str},
    total=False,
)


class DescribeSourceRegionsPaginateResponseSourceRegionsTypeDef(
    _DescribeSourceRegionsPaginateResponseSourceRegionsTypeDef
):
    """
    - *(dict) --*

      Contains an AWS Region name as the result of a successful call to the
      ``DescribeSourceRegions`` action.
      - **RegionName** *(string) --*

        The name of the source AWS Region.
    """


_DescribeSourceRegionsPaginateResponseTypeDef = TypedDict(
    "_DescribeSourceRegionsPaginateResponseTypeDef",
    {
        "SourceRegions": List[DescribeSourceRegionsPaginateResponseSourceRegionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeSourceRegionsPaginateResponseTypeDef(_DescribeSourceRegionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the result of a successful invocation of the ``DescribeSourceRegions`` action.
      - **SourceRegions** *(list) --*

        A list of SourceRegion instances that contains each source AWS Region that the current AWS
        Region can get a Read Replica or a DB snapshot from.
        - *(dict) --*

          Contains an AWS Region name as the result of a successful call to the
          ``DescribeSourceRegions`` action.
          - **RegionName** *(string) --*

            The name of the source AWS Region.
    """


_DownloadDBLogFilePortionPaginatePaginationConfigTypeDef = TypedDict(
    "_DownloadDBLogFilePortionPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DownloadDBLogFilePortionPaginatePaginationConfigTypeDef(
    _DownloadDBLogFilePortionPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DownloadDBLogFilePortionPaginateResponseTypeDef = TypedDict(
    "_DownloadDBLogFilePortionPaginateResponseTypeDef",
    {"LogFileData": str, "AdditionalDataPending": bool, "NextToken": str},
    total=False,
)


class DownloadDBLogFilePortionPaginateResponseTypeDef(
    _DownloadDBLogFilePortionPaginateResponseTypeDef
):
    """
    - *(dict) --*

      This data type is used as a response element to ``DownloadDBLogFilePortion`` .
      - **LogFileData** *(string) --*

        Entries from the specified log file.
    """
