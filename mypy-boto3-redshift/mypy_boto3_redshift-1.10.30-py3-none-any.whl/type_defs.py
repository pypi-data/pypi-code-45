"Main interface for redshift service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeRecurringChargesTypeDef",
    "ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeTypeDef",
    "ClientAcceptReservedNodeExchangeResponseTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseTypeDef",
    "ClientAuthorizeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef",
    "ClientAuthorizeSnapshotAccessResponseSnapshotTagsTypeDef",
    "ClientAuthorizeSnapshotAccessResponseSnapshotTypeDef",
    "ClientAuthorizeSnapshotAccessResponseTypeDef",
    "ClientBatchDeleteClusterSnapshotsIdentifiersTypeDef",
    "ClientBatchDeleteClusterSnapshotsResponseErrorsTypeDef",
    "ClientBatchDeleteClusterSnapshotsResponseTypeDef",
    "ClientBatchModifyClusterSnapshotsResponseErrorsTypeDef",
    "ClientBatchModifyClusterSnapshotsResponseTypeDef",
    "ClientCancelResizeResponseTypeDef",
    "ClientCopyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    "ClientCopyClusterSnapshotResponseSnapshotTagsTypeDef",
    "ClientCopyClusterSnapshotResponseSnapshotTypeDef",
    "ClientCopyClusterSnapshotResponseTypeDef",
    "ClientCreateClusterParameterGroupResponseClusterParameterGroupTagsTypeDef",
    "ClientCreateClusterParameterGroupResponseClusterParameterGroupTypeDef",
    "ClientCreateClusterParameterGroupResponseTypeDef",
    "ClientCreateClusterParameterGroupTagsTypeDef",
    "ClientCreateClusterResponseClusterClusterNodesTypeDef",
    "ClientCreateClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientCreateClusterResponseClusterClusterParameterGroupsTypeDef",
    "ClientCreateClusterResponseClusterClusterSecurityGroupsTypeDef",
    "ClientCreateClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientCreateClusterResponseClusterDataTransferProgressTypeDef",
    "ClientCreateClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientCreateClusterResponseClusterElasticIpStatusTypeDef",
    "ClientCreateClusterResponseClusterEndpointTypeDef",
    "ClientCreateClusterResponseClusterHsmStatusTypeDef",
    "ClientCreateClusterResponseClusterIamRolesTypeDef",
    "ClientCreateClusterResponseClusterPendingModifiedValuesTypeDef",
    "ClientCreateClusterResponseClusterResizeInfoTypeDef",
    "ClientCreateClusterResponseClusterRestoreStatusTypeDef",
    "ClientCreateClusterResponseClusterTagsTypeDef",
    "ClientCreateClusterResponseClusterVpcSecurityGroupsTypeDef",
    "ClientCreateClusterResponseClusterTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef",
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTagsTypeDef",
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTypeDef",
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTagsTypeDef",
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTypeDef",
    "ClientCreateClusterSecurityGroupResponseTypeDef",
    "ClientCreateClusterSecurityGroupTagsTypeDef",
    "ClientCreateClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    "ClientCreateClusterSnapshotResponseSnapshotTagsTypeDef",
    "ClientCreateClusterSnapshotResponseSnapshotTypeDef",
    "ClientCreateClusterSnapshotResponseTypeDef",
    "ClientCreateClusterSnapshotTagsTypeDef",
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef",
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef",
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTypeDef",
    "ClientCreateClusterSubnetGroupResponseTypeDef",
    "ClientCreateClusterSubnetGroupTagsTypeDef",
    "ClientCreateClusterTagsTypeDef",
    "ClientCreateEventSubscriptionResponseEventSubscriptionTagsTypeDef",
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientCreateEventSubscriptionResponseTypeDef",
    "ClientCreateEventSubscriptionTagsTypeDef",
    "ClientCreateHsmClientCertificateResponseHsmClientCertificateTagsTypeDef",
    "ClientCreateHsmClientCertificateResponseHsmClientCertificateTypeDef",
    "ClientCreateHsmClientCertificateResponseTypeDef",
    "ClientCreateHsmClientCertificateTagsTypeDef",
    "ClientCreateHsmConfigurationResponseHsmConfigurationTagsTypeDef",
    "ClientCreateHsmConfigurationResponseHsmConfigurationTypeDef",
    "ClientCreateHsmConfigurationResponseTypeDef",
    "ClientCreateHsmConfigurationTagsTypeDef",
    "ClientCreateScheduledActionResponseTargetActionResizeClusterTypeDef",
    "ClientCreateScheduledActionResponseTargetActionTypeDef",
    "ClientCreateScheduledActionResponseTypeDef",
    "ClientCreateScheduledActionTargetActionResizeClusterTypeDef",
    "ClientCreateScheduledActionTargetActionTypeDef",
    "ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTagsTypeDef",
    "ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTypeDef",
    "ClientCreateSnapshotCopyGrantResponseTypeDef",
    "ClientCreateSnapshotCopyGrantTagsTypeDef",
    "ClientCreateSnapshotScheduleResponseAssociatedClustersTypeDef",
    "ClientCreateSnapshotScheduleResponseTagsTypeDef",
    "ClientCreateSnapshotScheduleResponseTypeDef",
    "ClientCreateSnapshotScheduleTagsTypeDef",
    "ClientCreateTagsTagsTypeDef",
    "ClientDeleteClusterResponseClusterClusterNodesTypeDef",
    "ClientDeleteClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientDeleteClusterResponseClusterClusterParameterGroupsTypeDef",
    "ClientDeleteClusterResponseClusterClusterSecurityGroupsTypeDef",
    "ClientDeleteClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientDeleteClusterResponseClusterDataTransferProgressTypeDef",
    "ClientDeleteClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientDeleteClusterResponseClusterElasticIpStatusTypeDef",
    "ClientDeleteClusterResponseClusterEndpointTypeDef",
    "ClientDeleteClusterResponseClusterHsmStatusTypeDef",
    "ClientDeleteClusterResponseClusterIamRolesTypeDef",
    "ClientDeleteClusterResponseClusterPendingModifiedValuesTypeDef",
    "ClientDeleteClusterResponseClusterResizeInfoTypeDef",
    "ClientDeleteClusterResponseClusterRestoreStatusTypeDef",
    "ClientDeleteClusterResponseClusterTagsTypeDef",
    "ClientDeleteClusterResponseClusterVpcSecurityGroupsTypeDef",
    "ClientDeleteClusterResponseClusterTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDeleteClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    "ClientDeleteClusterSnapshotResponseSnapshotTagsTypeDef",
    "ClientDeleteClusterSnapshotResponseSnapshotTypeDef",
    "ClientDeleteClusterSnapshotResponseTypeDef",
    "ClientDescribeAccountAttributesResponseAccountAttributesAttributeValuesTypeDef",
    "ClientDescribeAccountAttributesResponseAccountAttributesTypeDef",
    "ClientDescribeAccountAttributesResponseTypeDef",
    "ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsRevisionTargetsTypeDef",
    "ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsTypeDef",
    "ClientDescribeClusterDbRevisionsResponseTypeDef",
    "ClientDescribeClusterParameterGroupsResponseParameterGroupsTagsTypeDef",
    "ClientDescribeClusterParameterGroupsResponseParameterGroupsTypeDef",
    "ClientDescribeClusterParameterGroupsResponseTypeDef",
    "ClientDescribeClusterParametersResponseParametersTypeDef",
    "ClientDescribeClusterParametersResponseTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTagsTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTagsTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseTypeDef",
    "ClientDescribeClusterSnapshotsResponseSnapshotsAccountsWithRestoreAccessTypeDef",
    "ClientDescribeClusterSnapshotsResponseSnapshotsTagsTypeDef",
    "ClientDescribeClusterSnapshotsResponseSnapshotsTypeDef",
    "ClientDescribeClusterSnapshotsResponseTypeDef",
    "ClientDescribeClusterSnapshotsSortingEntitiesTypeDef",
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsTypeDef",
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTagsTypeDef",
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTypeDef",
    "ClientDescribeClusterSubnetGroupsResponseTypeDef",
    "ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef",
    "ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsTypeDef",
    "ClientDescribeClusterTracksResponseMaintenanceTracksTypeDef",
    "ClientDescribeClusterTracksResponseTypeDef",
    "ClientDescribeClusterVersionsResponseClusterVersionsTypeDef",
    "ClientDescribeClusterVersionsResponseTypeDef",
    "ClientDescribeClustersResponseClustersClusterNodesTypeDef",
    "ClientDescribeClustersResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientDescribeClustersResponseClustersClusterParameterGroupsTypeDef",
    "ClientDescribeClustersResponseClustersClusterSecurityGroupsTypeDef",
    "ClientDescribeClustersResponseClustersClusterSnapshotCopyStatusTypeDef",
    "ClientDescribeClustersResponseClustersDataTransferProgressTypeDef",
    "ClientDescribeClustersResponseClustersDeferredMaintenanceWindowsTypeDef",
    "ClientDescribeClustersResponseClustersElasticIpStatusTypeDef",
    "ClientDescribeClustersResponseClustersEndpointTypeDef",
    "ClientDescribeClustersResponseClustersHsmStatusTypeDef",
    "ClientDescribeClustersResponseClustersIamRolesTypeDef",
    "ClientDescribeClustersResponseClustersPendingModifiedValuesTypeDef",
    "ClientDescribeClustersResponseClustersResizeInfoTypeDef",
    "ClientDescribeClustersResponseClustersRestoreStatusTypeDef",
    "ClientDescribeClustersResponseClustersTagsTypeDef",
    "ClientDescribeClustersResponseClustersVpcSecurityGroupsTypeDef",
    "ClientDescribeClustersResponseClustersTypeDef",
    "ClientDescribeClustersResponseTypeDef",
    "ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersParametersTypeDef",
    "ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersTypeDef",
    "ClientDescribeDefaultClusterParametersResponseTypeDef",
    "ClientDescribeEventCategoriesResponseEventCategoriesMapListEventsTypeDef",
    "ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    "ClientDescribeEventCategoriesResponseTypeDef",
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTagsTypeDef",
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    "ClientDescribeEventSubscriptionsResponseTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTagsTypeDef",
    "ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTypeDef",
    "ClientDescribeHsmClientCertificatesResponseTypeDef",
    "ClientDescribeHsmConfigurationsResponseHsmConfigurationsTagsTypeDef",
    "ClientDescribeHsmConfigurationsResponseHsmConfigurationsTypeDef",
    "ClientDescribeHsmConfigurationsResponseTypeDef",
    "ClientDescribeLoggingStatusResponseTypeDef",
    "ClientDescribeNodeConfigurationOptionsFiltersTypeDef",
    "ClientDescribeNodeConfigurationOptionsResponseNodeConfigurationOptionListTypeDef",
    "ClientDescribeNodeConfigurationOptionsResponseTypeDef",
    "ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef",
    "ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesTypeDef",
    "ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsTypeDef",
    "ClientDescribeOrderableClusterOptionsResponseTypeDef",
    "ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef",
    "ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsTypeDef",
    "ClientDescribeReservedNodeOfferingsResponseTypeDef",
    "ClientDescribeReservedNodesResponseReservedNodesRecurringChargesTypeDef",
    "ClientDescribeReservedNodesResponseReservedNodesTypeDef",
    "ClientDescribeReservedNodesResponseTypeDef",
    "ClientDescribeResizeResponseTypeDef",
    "ClientDescribeScheduledActionsFiltersTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledActionsTargetActionResizeClusterTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledActionsTargetActionTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledActionsTypeDef",
    "ClientDescribeScheduledActionsResponseTypeDef",
    "ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTagsTypeDef",
    "ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTypeDef",
    "ClientDescribeSnapshotCopyGrantsResponseTypeDef",
    "ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesAssociatedClustersTypeDef",
    "ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTagsTypeDef",
    "ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTypeDef",
    "ClientDescribeSnapshotSchedulesResponseTypeDef",
    "ClientDescribeStorageResponseTypeDef",
    "ClientDescribeTableRestoreStatusResponseTableRestoreStatusDetailsTypeDef",
    "ClientDescribeTableRestoreStatusResponseTypeDef",
    "ClientDescribeTagsResponseTaggedResourcesTagTypeDef",
    "ClientDescribeTagsResponseTaggedResourcesTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDisableLoggingResponseTypeDef",
    "ClientDisableSnapshotCopyResponseClusterClusterNodesTypeDef",
    "ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef",
    "ClientDisableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef",
    "ClientDisableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientDisableSnapshotCopyResponseClusterDataTransferProgressTypeDef",
    "ClientDisableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientDisableSnapshotCopyResponseClusterElasticIpStatusTypeDef",
    "ClientDisableSnapshotCopyResponseClusterEndpointTypeDef",
    "ClientDisableSnapshotCopyResponseClusterHsmStatusTypeDef",
    "ClientDisableSnapshotCopyResponseClusterIamRolesTypeDef",
    "ClientDisableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef",
    "ClientDisableSnapshotCopyResponseClusterResizeInfoTypeDef",
    "ClientDisableSnapshotCopyResponseClusterRestoreStatusTypeDef",
    "ClientDisableSnapshotCopyResponseClusterTagsTypeDef",
    "ClientDisableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef",
    "ClientDisableSnapshotCopyResponseClusterTypeDef",
    "ClientDisableSnapshotCopyResponseTypeDef",
    "ClientEnableLoggingResponseTypeDef",
    "ClientEnableSnapshotCopyResponseClusterClusterNodesTypeDef",
    "ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef",
    "ClientEnableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef",
    "ClientEnableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientEnableSnapshotCopyResponseClusterDataTransferProgressTypeDef",
    "ClientEnableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientEnableSnapshotCopyResponseClusterElasticIpStatusTypeDef",
    "ClientEnableSnapshotCopyResponseClusterEndpointTypeDef",
    "ClientEnableSnapshotCopyResponseClusterHsmStatusTypeDef",
    "ClientEnableSnapshotCopyResponseClusterIamRolesTypeDef",
    "ClientEnableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef",
    "ClientEnableSnapshotCopyResponseClusterResizeInfoTypeDef",
    "ClientEnableSnapshotCopyResponseClusterRestoreStatusTypeDef",
    "ClientEnableSnapshotCopyResponseClusterTagsTypeDef",
    "ClientEnableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef",
    "ClientEnableSnapshotCopyResponseClusterTypeDef",
    "ClientEnableSnapshotCopyResponseTypeDef",
    "ClientGetClusterCredentialsResponseTypeDef",
    "ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef",
    "ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsTypeDef",
    "ClientGetReservedNodeExchangeOfferingsResponseTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterClusterNodesTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterClusterSecurityGroupsTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterDataTransferProgressTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterElasticIpStatusTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterEndpointTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterHsmStatusTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterIamRolesTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterPendingModifiedValuesTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterResizeInfoTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterRestoreStatusTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterTagsTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterVpcSecurityGroupsTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterTypeDef",
    "ClientModifyClusterDbRevisionResponseTypeDef",
    "ClientModifyClusterIamRolesResponseClusterClusterNodesTypeDef",
    "ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsTypeDef",
    "ClientModifyClusterIamRolesResponseClusterClusterSecurityGroupsTypeDef",
    "ClientModifyClusterIamRolesResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientModifyClusterIamRolesResponseClusterDataTransferProgressTypeDef",
    "ClientModifyClusterIamRolesResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientModifyClusterIamRolesResponseClusterElasticIpStatusTypeDef",
    "ClientModifyClusterIamRolesResponseClusterEndpointTypeDef",
    "ClientModifyClusterIamRolesResponseClusterHsmStatusTypeDef",
    "ClientModifyClusterIamRolesResponseClusterIamRolesTypeDef",
    "ClientModifyClusterIamRolesResponseClusterPendingModifiedValuesTypeDef",
    "ClientModifyClusterIamRolesResponseClusterResizeInfoTypeDef",
    "ClientModifyClusterIamRolesResponseClusterRestoreStatusTypeDef",
    "ClientModifyClusterIamRolesResponseClusterTagsTypeDef",
    "ClientModifyClusterIamRolesResponseClusterVpcSecurityGroupsTypeDef",
    "ClientModifyClusterIamRolesResponseClusterTypeDef",
    "ClientModifyClusterIamRolesResponseTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterClusterNodesTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterClusterSecurityGroupsTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterDataTransferProgressTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterElasticIpStatusTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterEndpointTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterHsmStatusTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterIamRolesTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterPendingModifiedValuesTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterResizeInfoTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterRestoreStatusTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterTagsTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterVpcSecurityGroupsTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterTypeDef",
    "ClientModifyClusterMaintenanceResponseTypeDef",
    "ClientModifyClusterParameterGroupParametersTypeDef",
    "ClientModifyClusterParameterGroupResponseTypeDef",
    "ClientModifyClusterResponseClusterClusterNodesTypeDef",
    "ClientModifyClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientModifyClusterResponseClusterClusterParameterGroupsTypeDef",
    "ClientModifyClusterResponseClusterClusterSecurityGroupsTypeDef",
    "ClientModifyClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientModifyClusterResponseClusterDataTransferProgressTypeDef",
    "ClientModifyClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientModifyClusterResponseClusterElasticIpStatusTypeDef",
    "ClientModifyClusterResponseClusterEndpointTypeDef",
    "ClientModifyClusterResponseClusterHsmStatusTypeDef",
    "ClientModifyClusterResponseClusterIamRolesTypeDef",
    "ClientModifyClusterResponseClusterPendingModifiedValuesTypeDef",
    "ClientModifyClusterResponseClusterResizeInfoTypeDef",
    "ClientModifyClusterResponseClusterRestoreStatusTypeDef",
    "ClientModifyClusterResponseClusterTagsTypeDef",
    "ClientModifyClusterResponseClusterVpcSecurityGroupsTypeDef",
    "ClientModifyClusterResponseClusterTypeDef",
    "ClientModifyClusterResponseTypeDef",
    "ClientModifyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    "ClientModifyClusterSnapshotResponseSnapshotTagsTypeDef",
    "ClientModifyClusterSnapshotResponseSnapshotTypeDef",
    "ClientModifyClusterSnapshotResponseTypeDef",
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef",
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef",
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTypeDef",
    "ClientModifyClusterSubnetGroupResponseTypeDef",
    "ClientModifyEventSubscriptionResponseEventSubscriptionTagsTypeDef",
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientModifyEventSubscriptionResponseTypeDef",
    "ClientModifyScheduledActionResponseTargetActionResizeClusterTypeDef",
    "ClientModifyScheduledActionResponseTargetActionTypeDef",
    "ClientModifyScheduledActionResponseTypeDef",
    "ClientModifyScheduledActionTargetActionResizeClusterTypeDef",
    "ClientModifyScheduledActionTargetActionTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterNodesTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSecurityGroupsTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterDataTransferProgressTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterElasticIpStatusTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterEndpointTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterHsmStatusTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterIamRolesTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterPendingModifiedValuesTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterResizeInfoTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterRestoreStatusTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterTagsTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterVpcSecurityGroupsTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseTypeDef",
    "ClientModifySnapshotScheduleResponseAssociatedClustersTypeDef",
    "ClientModifySnapshotScheduleResponseTagsTypeDef",
    "ClientModifySnapshotScheduleResponseTypeDef",
    "ClientPurchaseReservedNodeOfferingResponseReservedNodeRecurringChargesTypeDef",
    "ClientPurchaseReservedNodeOfferingResponseReservedNodeTypeDef",
    "ClientPurchaseReservedNodeOfferingResponseTypeDef",
    "ClientRebootClusterResponseClusterClusterNodesTypeDef",
    "ClientRebootClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientRebootClusterResponseClusterClusterParameterGroupsTypeDef",
    "ClientRebootClusterResponseClusterClusterSecurityGroupsTypeDef",
    "ClientRebootClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientRebootClusterResponseClusterDataTransferProgressTypeDef",
    "ClientRebootClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientRebootClusterResponseClusterElasticIpStatusTypeDef",
    "ClientRebootClusterResponseClusterEndpointTypeDef",
    "ClientRebootClusterResponseClusterHsmStatusTypeDef",
    "ClientRebootClusterResponseClusterIamRolesTypeDef",
    "ClientRebootClusterResponseClusterPendingModifiedValuesTypeDef",
    "ClientRebootClusterResponseClusterResizeInfoTypeDef",
    "ClientRebootClusterResponseClusterRestoreStatusTypeDef",
    "ClientRebootClusterResponseClusterTagsTypeDef",
    "ClientRebootClusterResponseClusterVpcSecurityGroupsTypeDef",
    "ClientRebootClusterResponseClusterTypeDef",
    "ClientRebootClusterResponseTypeDef",
    "ClientResetClusterParameterGroupParametersTypeDef",
    "ClientResetClusterParameterGroupResponseTypeDef",
    "ClientResizeClusterResponseClusterClusterNodesTypeDef",
    "ClientResizeClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientResizeClusterResponseClusterClusterParameterGroupsTypeDef",
    "ClientResizeClusterResponseClusterClusterSecurityGroupsTypeDef",
    "ClientResizeClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientResizeClusterResponseClusterDataTransferProgressTypeDef",
    "ClientResizeClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientResizeClusterResponseClusterElasticIpStatusTypeDef",
    "ClientResizeClusterResponseClusterEndpointTypeDef",
    "ClientResizeClusterResponseClusterHsmStatusTypeDef",
    "ClientResizeClusterResponseClusterIamRolesTypeDef",
    "ClientResizeClusterResponseClusterPendingModifiedValuesTypeDef",
    "ClientResizeClusterResponseClusterResizeInfoTypeDef",
    "ClientResizeClusterResponseClusterRestoreStatusTypeDef",
    "ClientResizeClusterResponseClusterTagsTypeDef",
    "ClientResizeClusterResponseClusterVpcSecurityGroupsTypeDef",
    "ClientResizeClusterResponseClusterTypeDef",
    "ClientResizeClusterResponseTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterClusterNodesTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterClusterSecurityGroupsTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterDataTransferProgressTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterElasticIpStatusTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterEndpointTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterHsmStatusTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterIamRolesTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterPendingModifiedValuesTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterResizeInfoTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterRestoreStatusTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterTagsTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterTypeDef",
    "ClientRestoreFromClusterSnapshotResponseTypeDef",
    "ClientRestoreTableFromClusterSnapshotResponseTableRestoreStatusTypeDef",
    "ClientRestoreTableFromClusterSnapshotResponseTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseTypeDef",
    "ClientRevokeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef",
    "ClientRevokeSnapshotAccessResponseSnapshotTagsTypeDef",
    "ClientRevokeSnapshotAccessResponseSnapshotTypeDef",
    "ClientRevokeSnapshotAccessResponseTypeDef",
    "ClientRotateEncryptionKeyResponseClusterClusterNodesTypeDef",
    "ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsTypeDef",
    "ClientRotateEncryptionKeyResponseClusterClusterSecurityGroupsTypeDef",
    "ClientRotateEncryptionKeyResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientRotateEncryptionKeyResponseClusterDataTransferProgressTypeDef",
    "ClientRotateEncryptionKeyResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientRotateEncryptionKeyResponseClusterElasticIpStatusTypeDef",
    "ClientRotateEncryptionKeyResponseClusterEndpointTypeDef",
    "ClientRotateEncryptionKeyResponseClusterHsmStatusTypeDef",
    "ClientRotateEncryptionKeyResponseClusterIamRolesTypeDef",
    "ClientRotateEncryptionKeyResponseClusterPendingModifiedValuesTypeDef",
    "ClientRotateEncryptionKeyResponseClusterResizeInfoTypeDef",
    "ClientRotateEncryptionKeyResponseClusterRestoreStatusTypeDef",
    "ClientRotateEncryptionKeyResponseClusterTagsTypeDef",
    "ClientRotateEncryptionKeyResponseClusterVpcSecurityGroupsTypeDef",
    "ClientRotateEncryptionKeyResponseClusterTypeDef",
    "ClientRotateEncryptionKeyResponseTypeDef",
    "ClusterAvailableWaitWaiterConfigTypeDef",
    "ClusterDeletedWaitWaiterConfigTypeDef",
    "ClusterRestoredWaitWaiterConfigTypeDef",
    "DescribeClusterDbRevisionsPaginatePaginationConfigTypeDef",
    "DescribeClusterDbRevisionsPaginateResponseClusterDbRevisionsRevisionTargetsTypeDef",
    "DescribeClusterDbRevisionsPaginateResponseClusterDbRevisionsTypeDef",
    "DescribeClusterDbRevisionsPaginateResponseTypeDef",
    "DescribeClusterParameterGroupsPaginatePaginationConfigTypeDef",
    "DescribeClusterParameterGroupsPaginateResponseParameterGroupsTagsTypeDef",
    "DescribeClusterParameterGroupsPaginateResponseParameterGroupsTypeDef",
    "DescribeClusterParameterGroupsPaginateResponseTypeDef",
    "DescribeClusterParametersPaginatePaginationConfigTypeDef",
    "DescribeClusterParametersPaginateResponseParametersTypeDef",
    "DescribeClusterParametersPaginateResponseTypeDef",
    "DescribeClusterSecurityGroupsPaginatePaginationConfigTypeDef",
    "DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef",
    "DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef",
    "DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsIPRangesTagsTypeDef",
    "DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsIPRangesTypeDef",
    "DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsTagsTypeDef",
    "DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsTypeDef",
    "DescribeClusterSecurityGroupsPaginateResponseTypeDef",
    "DescribeClusterSnapshotsPaginatePaginationConfigTypeDef",
    "DescribeClusterSnapshotsPaginateResponseSnapshotsAccountsWithRestoreAccessTypeDef",
    "DescribeClusterSnapshotsPaginateResponseSnapshotsTagsTypeDef",
    "DescribeClusterSnapshotsPaginateResponseSnapshotsTypeDef",
    "DescribeClusterSnapshotsPaginateResponseTypeDef",
    "DescribeClusterSnapshotsPaginateSortingEntitiesTypeDef",
    "DescribeClusterSubnetGroupsPaginatePaginationConfigTypeDef",
    "DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    "DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsTypeDef",
    "DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsTagsTypeDef",
    "DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsTypeDef",
    "DescribeClusterSubnetGroupsPaginateResponseTypeDef",
    "DescribeClusterTracksPaginatePaginationConfigTypeDef",
    "DescribeClusterTracksPaginateResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef",
    "DescribeClusterTracksPaginateResponseMaintenanceTracksUpdateTargetsTypeDef",
    "DescribeClusterTracksPaginateResponseMaintenanceTracksTypeDef",
    "DescribeClusterTracksPaginateResponseTypeDef",
    "DescribeClusterVersionsPaginatePaginationConfigTypeDef",
    "DescribeClusterVersionsPaginateResponseClusterVersionsTypeDef",
    "DescribeClusterVersionsPaginateResponseTypeDef",
    "DescribeClustersPaginatePaginationConfigTypeDef",
    "DescribeClustersPaginateResponseClustersClusterNodesTypeDef",
    "DescribeClustersPaginateResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef",
    "DescribeClustersPaginateResponseClustersClusterParameterGroupsTypeDef",
    "DescribeClustersPaginateResponseClustersClusterSecurityGroupsTypeDef",
    "DescribeClustersPaginateResponseClustersClusterSnapshotCopyStatusTypeDef",
    "DescribeClustersPaginateResponseClustersDataTransferProgressTypeDef",
    "DescribeClustersPaginateResponseClustersDeferredMaintenanceWindowsTypeDef",
    "DescribeClustersPaginateResponseClustersElasticIpStatusTypeDef",
    "DescribeClustersPaginateResponseClustersEndpointTypeDef",
    "DescribeClustersPaginateResponseClustersHsmStatusTypeDef",
    "DescribeClustersPaginateResponseClustersIamRolesTypeDef",
    "DescribeClustersPaginateResponseClustersPendingModifiedValuesTypeDef",
    "DescribeClustersPaginateResponseClustersResizeInfoTypeDef",
    "DescribeClustersPaginateResponseClustersRestoreStatusTypeDef",
    "DescribeClustersPaginateResponseClustersTagsTypeDef",
    "DescribeClustersPaginateResponseClustersVpcSecurityGroupsTypeDef",
    "DescribeClustersPaginateResponseClustersTypeDef",
    "DescribeClustersPaginateResponseTypeDef",
    "DescribeDefaultClusterParametersPaginatePaginationConfigTypeDef",
    "DescribeDefaultClusterParametersPaginateResponseDefaultClusterParametersParametersTypeDef",
    "DescribeDefaultClusterParametersPaginateResponseDefaultClusterParametersTypeDef",
    "DescribeDefaultClusterParametersPaginateResponseTypeDef",
    "DescribeEventSubscriptionsPaginatePaginationConfigTypeDef",
    "DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTagsTypeDef",
    "DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef",
    "DescribeEventSubscriptionsPaginateResponseTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "DescribeHsmClientCertificatesPaginatePaginationConfigTypeDef",
    "DescribeHsmClientCertificatesPaginateResponseHsmClientCertificatesTagsTypeDef",
    "DescribeHsmClientCertificatesPaginateResponseHsmClientCertificatesTypeDef",
    "DescribeHsmClientCertificatesPaginateResponseTypeDef",
    "DescribeHsmConfigurationsPaginatePaginationConfigTypeDef",
    "DescribeHsmConfigurationsPaginateResponseHsmConfigurationsTagsTypeDef",
    "DescribeHsmConfigurationsPaginateResponseHsmConfigurationsTypeDef",
    "DescribeHsmConfigurationsPaginateResponseTypeDef",
    "DescribeNodeConfigurationOptionsPaginateFiltersTypeDef",
    "DescribeNodeConfigurationOptionsPaginatePaginationConfigTypeDef",
    "DescribeNodeConfigurationOptionsPaginateResponseNodeConfigurationOptionListTypeDef",
    "DescribeNodeConfigurationOptionsPaginateResponseTypeDef",
    "DescribeOrderableClusterOptionsPaginatePaginationConfigTypeDef",
    "DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef",
    "DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsAvailabilityZonesTypeDef",
    "DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsTypeDef",
    "DescribeOrderableClusterOptionsPaginateResponseTypeDef",
    "DescribeReservedNodeOfferingsPaginatePaginationConfigTypeDef",
    "DescribeReservedNodeOfferingsPaginateResponseReservedNodeOfferingsRecurringChargesTypeDef",
    "DescribeReservedNodeOfferingsPaginateResponseReservedNodeOfferingsTypeDef",
    "DescribeReservedNodeOfferingsPaginateResponseTypeDef",
    "DescribeReservedNodesPaginatePaginationConfigTypeDef",
    "DescribeReservedNodesPaginateResponseReservedNodesRecurringChargesTypeDef",
    "DescribeReservedNodesPaginateResponseReservedNodesTypeDef",
    "DescribeReservedNodesPaginateResponseTypeDef",
    "DescribeScheduledActionsPaginateFiltersTypeDef",
    "DescribeScheduledActionsPaginatePaginationConfigTypeDef",
    "DescribeScheduledActionsPaginateResponseScheduledActionsTargetActionResizeClusterTypeDef",
    "DescribeScheduledActionsPaginateResponseScheduledActionsTargetActionTypeDef",
    "DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef",
    "DescribeScheduledActionsPaginateResponseTypeDef",
    "DescribeSnapshotCopyGrantsPaginatePaginationConfigTypeDef",
    "DescribeSnapshotCopyGrantsPaginateResponseSnapshotCopyGrantsTagsTypeDef",
    "DescribeSnapshotCopyGrantsPaginateResponseSnapshotCopyGrantsTypeDef",
    "DescribeSnapshotCopyGrantsPaginateResponseTypeDef",
    "DescribeSnapshotSchedulesPaginatePaginationConfigTypeDef",
    "DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesAssociatedClustersTypeDef",
    "DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesTagsTypeDef",
    "DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesTypeDef",
    "DescribeSnapshotSchedulesPaginateResponseTypeDef",
    "DescribeTableRestoreStatusPaginatePaginationConfigTypeDef",
    "DescribeTableRestoreStatusPaginateResponseTableRestoreStatusDetailsTypeDef",
    "DescribeTableRestoreStatusPaginateResponseTypeDef",
    "DescribeTagsPaginatePaginationConfigTypeDef",
    "DescribeTagsPaginateResponseTaggedResourcesTagTypeDef",
    "DescribeTagsPaginateResponseTaggedResourcesTypeDef",
    "DescribeTagsPaginateResponseTypeDef",
    "GetReservedNodeExchangeOfferingsPaginatePaginationConfigTypeDef",
    "GetReservedNodeExchangeOfferingsPaginateResponseReservedNodeOfferingsRecurringChargesTypeDef",
    "GetReservedNodeExchangeOfferingsPaginateResponseReservedNodeOfferingsTypeDef",
    "GetReservedNodeExchangeOfferingsPaginateResponseTypeDef",
    "SnapshotAvailableWaitSortingEntitiesTypeDef",
    "SnapshotAvailableWaitWaiterConfigTypeDef",
)


_ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeRecurringChargesTypeDef = TypedDict(
    "_ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeRecurringChargesTypeDef(
    _ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeRecurringChargesTypeDef
):
    pass


_ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeTypeDef = TypedDict(
    "_ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeTypeDef",
    {
        "ReservedNodeId": str,
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "NodeCount": int,
        "State": str,
        "OfferingType": str,
        "RecurringCharges": List[
            ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeRecurringChargesTypeDef
        ],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)


class ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeTypeDef(
    _ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeTypeDef
):
    """
    - **ExchangedReservedNode** *(dict) --*

      - **ReservedNodeId** *(string) --*

        The unique identifier for the reservation.
    """


_ClientAcceptReservedNodeExchangeResponseTypeDef = TypedDict(
    "_ClientAcceptReservedNodeExchangeResponseTypeDef",
    {"ExchangedReservedNode": ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeTypeDef},
    total=False,
)


class ClientAcceptReservedNodeExchangeResponseTypeDef(
    _ClientAcceptReservedNodeExchangeResponseTypeDef
):
    """
    - *(dict) --*

      - **ExchangedReservedNode** *(dict) --*

        - **ReservedNodeId** *(string) --*

          The unique identifier for the reservation.
    """


_ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef = TypedDict(
    "_ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef(
    _ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef
):
    pass


_ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
        "Tags": List[
            ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef
        ],
    },
    total=False,
)


class ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef(
    _ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef
):
    pass


_ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef = TypedDict(
    "_ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef(
    _ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef
):
    pass


_ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef = TypedDict(
    "_ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
        "Tags": List[
            ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef
        ],
    },
    total=False,
)


class ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef(
    _ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef
):
    pass


_ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef = TypedDict(
    "_ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef(
    _ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef
):
    pass


_ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef = TypedDict(
    "_ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[
            ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef
        ],
        "Tags": List[
            ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef
        ],
    },
    total=False,
)


class ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef(
    _ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef
):
    """
    - **ClusterSecurityGroup** *(dict) --*

      Describes a security group.
      - **ClusterSecurityGroupName** *(string) --*

        The name of the cluster security group to which the operation was applied.
    """


_ClientAuthorizeClusterSecurityGroupIngressResponseTypeDef = TypedDict(
    "_ClientAuthorizeClusterSecurityGroupIngressResponseTypeDef",
    {
        "ClusterSecurityGroup": ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef
    },
    total=False,
)


class ClientAuthorizeClusterSecurityGroupIngressResponseTypeDef(
    _ClientAuthorizeClusterSecurityGroupIngressResponseTypeDef
):
    """
    - *(dict) --*

      - **ClusterSecurityGroup** *(dict) --*

        Describes a security group.
        - **ClusterSecurityGroupName** *(string) --*

          The name of the cluster security group to which the operation was applied.
    """


_ClientAuthorizeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef = TypedDict(
    "_ClientAuthorizeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)


class ClientAuthorizeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef(
    _ClientAuthorizeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef
):
    pass


_ClientAuthorizeSnapshotAccessResponseSnapshotTagsTypeDef = TypedDict(
    "_ClientAuthorizeSnapshotAccessResponseSnapshotTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientAuthorizeSnapshotAccessResponseSnapshotTagsTypeDef(
    _ClientAuthorizeSnapshotAccessResponseSnapshotTagsTypeDef
):
    pass


_ClientAuthorizeSnapshotAccessResponseSnapshotTypeDef = TypedDict(
    "_ClientAuthorizeSnapshotAccessResponseSnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientAuthorizeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientAuthorizeSnapshotAccessResponseSnapshotTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)


class ClientAuthorizeSnapshotAccessResponseSnapshotTypeDef(
    _ClientAuthorizeSnapshotAccessResponseSnapshotTypeDef
):
    """
    - **Snapshot** *(dict) --*

      Describes a snapshot.
      - **SnapshotIdentifier** *(string) --*

        The snapshot identifier that is provided in the request.
    """


_ClientAuthorizeSnapshotAccessResponseTypeDef = TypedDict(
    "_ClientAuthorizeSnapshotAccessResponseTypeDef",
    {"Snapshot": ClientAuthorizeSnapshotAccessResponseSnapshotTypeDef},
    total=False,
)


class ClientAuthorizeSnapshotAccessResponseTypeDef(_ClientAuthorizeSnapshotAccessResponseTypeDef):
    """
    - *(dict) --*

      - **Snapshot** *(dict) --*

        Describes a snapshot.
        - **SnapshotIdentifier** *(string) --*

          The snapshot identifier that is provided in the request.
    """


_RequiredClientBatchDeleteClusterSnapshotsIdentifiersTypeDef = TypedDict(
    "_RequiredClientBatchDeleteClusterSnapshotsIdentifiersTypeDef", {"SnapshotIdentifier": str}
)
_OptionalClientBatchDeleteClusterSnapshotsIdentifiersTypeDef = TypedDict(
    "_OptionalClientBatchDeleteClusterSnapshotsIdentifiersTypeDef",
    {"SnapshotClusterIdentifier": str},
    total=False,
)


class ClientBatchDeleteClusterSnapshotsIdentifiersTypeDef(
    _RequiredClientBatchDeleteClusterSnapshotsIdentifiersTypeDef,
    _OptionalClientBatchDeleteClusterSnapshotsIdentifiersTypeDef,
):
    """
    - *(dict) --*

      - **SnapshotIdentifier** *(string) --***[REQUIRED]**

        The unique identifier of the manual snapshot to be deleted.
        Constraints: Must be the name of an existing snapshot that is in the ``available`` ,
        ``failed`` , or ``cancelled`` state.
    """


_ClientBatchDeleteClusterSnapshotsResponseErrorsTypeDef = TypedDict(
    "_ClientBatchDeleteClusterSnapshotsResponseErrorsTypeDef",
    {
        "SnapshotIdentifier": str,
        "SnapshotClusterIdentifier": str,
        "FailureCode": str,
        "FailureReason": str,
    },
    total=False,
)


class ClientBatchDeleteClusterSnapshotsResponseErrorsTypeDef(
    _ClientBatchDeleteClusterSnapshotsResponseErrorsTypeDef
):
    pass


_ClientBatchDeleteClusterSnapshotsResponseTypeDef = TypedDict(
    "_ClientBatchDeleteClusterSnapshotsResponseTypeDef",
    {
        "Resources": List[str],
        "Errors": List[ClientBatchDeleteClusterSnapshotsResponseErrorsTypeDef],
    },
    total=False,
)


class ClientBatchDeleteClusterSnapshotsResponseTypeDef(
    _ClientBatchDeleteClusterSnapshotsResponseTypeDef
):
    """
    - *(dict) --*

      - **Resources** *(list) --*

        A list of the snapshot identifiers that were deleted.
        - *(string) --*
    """


_ClientBatchModifyClusterSnapshotsResponseErrorsTypeDef = TypedDict(
    "_ClientBatchModifyClusterSnapshotsResponseErrorsTypeDef",
    {
        "SnapshotIdentifier": str,
        "SnapshotClusterIdentifier": str,
        "FailureCode": str,
        "FailureReason": str,
    },
    total=False,
)


class ClientBatchModifyClusterSnapshotsResponseErrorsTypeDef(
    _ClientBatchModifyClusterSnapshotsResponseErrorsTypeDef
):
    pass


_ClientBatchModifyClusterSnapshotsResponseTypeDef = TypedDict(
    "_ClientBatchModifyClusterSnapshotsResponseTypeDef",
    {
        "Resources": List[str],
        "Errors": List[ClientBatchModifyClusterSnapshotsResponseErrorsTypeDef],
    },
    total=False,
)


class ClientBatchModifyClusterSnapshotsResponseTypeDef(
    _ClientBatchModifyClusterSnapshotsResponseTypeDef
):
    """
    - *(dict) --*

      - **Resources** *(list) --*

        A list of the snapshots that were modified.
        - *(string) --*
    """


_ClientCancelResizeResponseTypeDef = TypedDict(
    "_ClientCancelResizeResponseTypeDef",
    {
        "TargetNodeType": str,
        "TargetNumberOfNodes": int,
        "TargetClusterType": str,
        "Status": str,
        "ImportTablesCompleted": List[str],
        "ImportTablesInProgress": List[str],
        "ImportTablesNotStarted": List[str],
        "AvgResizeRateInMegaBytesPerSecond": float,
        "TotalResizeDataInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ResizeType": str,
        "Message": str,
        "TargetEncryptionType": str,
        "DataTransferProgressPercent": float,
    },
    total=False,
)


class ClientCancelResizeResponseTypeDef(_ClientCancelResizeResponseTypeDef):
    """
    - *(dict) --*

      Describes the result of a cluster resize operation.
      - **TargetNodeType** *(string) --*

        The node type that the cluster will have after the resize operation is complete.
    """


_ClientCopyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef = TypedDict(
    "_ClientCopyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)


class ClientCopyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef(
    _ClientCopyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef
):
    pass


_ClientCopyClusterSnapshotResponseSnapshotTagsTypeDef = TypedDict(
    "_ClientCopyClusterSnapshotResponseSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCopyClusterSnapshotResponseSnapshotTagsTypeDef(
    _ClientCopyClusterSnapshotResponseSnapshotTagsTypeDef
):
    pass


_ClientCopyClusterSnapshotResponseSnapshotTypeDef = TypedDict(
    "_ClientCopyClusterSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientCopyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientCopyClusterSnapshotResponseSnapshotTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)


class ClientCopyClusterSnapshotResponseSnapshotTypeDef(
    _ClientCopyClusterSnapshotResponseSnapshotTypeDef
):
    """
    - **Snapshot** *(dict) --*

      Describes a snapshot.
      - **SnapshotIdentifier** *(string) --*

        The snapshot identifier that is provided in the request.
    """


_ClientCopyClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientCopyClusterSnapshotResponseTypeDef",
    {"Snapshot": ClientCopyClusterSnapshotResponseSnapshotTypeDef},
    total=False,
)


class ClientCopyClusterSnapshotResponseTypeDef(_ClientCopyClusterSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **Snapshot** *(dict) --*

        Describes a snapshot.
        - **SnapshotIdentifier** *(string) --*

          The snapshot identifier that is provided in the request.
    """


_ClientCreateClusterParameterGroupResponseClusterParameterGroupTagsTypeDef = TypedDict(
    "_ClientCreateClusterParameterGroupResponseClusterParameterGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateClusterParameterGroupResponseClusterParameterGroupTagsTypeDef(
    _ClientCreateClusterParameterGroupResponseClusterParameterGroupTagsTypeDef
):
    pass


_ClientCreateClusterParameterGroupResponseClusterParameterGroupTypeDef = TypedDict(
    "_ClientCreateClusterParameterGroupResponseClusterParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupFamily": str,
        "Description": str,
        "Tags": List[ClientCreateClusterParameterGroupResponseClusterParameterGroupTagsTypeDef],
    },
    total=False,
)


class ClientCreateClusterParameterGroupResponseClusterParameterGroupTypeDef(
    _ClientCreateClusterParameterGroupResponseClusterParameterGroupTypeDef
):
    """
    - **ClusterParameterGroup** *(dict) --*

      Describes a parameter group.
      - **ParameterGroupName** *(string) --*

        The name of the cluster parameter group.
    """


_ClientCreateClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientCreateClusterParameterGroupResponseTypeDef",
    {
        "ClusterParameterGroup": ClientCreateClusterParameterGroupResponseClusterParameterGroupTypeDef
    },
    total=False,
)


class ClientCreateClusterParameterGroupResponseTypeDef(
    _ClientCreateClusterParameterGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **ClusterParameterGroup** *(dict) --*

        Describes a parameter group.
        - **ParameterGroupName** *(string) --*

          The name of the cluster parameter group.
    """


_ClientCreateClusterParameterGroupTagsTypeDef = TypedDict(
    "_ClientCreateClusterParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateClusterParameterGroupTagsTypeDef(_ClientCreateClusterParameterGroupTagsTypeDef):
    """
    - *(dict) --*

      A tag consisting of a name/value pair for a resource.
      - **Key** *(string) --*

        The key, or name, for the resource tag.
    """


_ClientCreateClusterResponseClusterClusterNodesTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientCreateClusterResponseClusterClusterNodesTypeDef(
    _ClientCreateClusterResponseClusterClusterNodesTypeDef
):
    pass


_ClientCreateClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientCreateClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientCreateClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientCreateClusterResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientCreateClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientCreateClusterResponseClusterClusterParameterGroupsTypeDef(
    _ClientCreateClusterResponseClusterClusterParameterGroupsTypeDef
):
    pass


_ClientCreateClusterResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientCreateClusterResponseClusterClusterSecurityGroupsTypeDef(
    _ClientCreateClusterResponseClusterClusterSecurityGroupsTypeDef
):
    pass


_ClientCreateClusterResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientCreateClusterResponseClusterClusterSnapshotCopyStatusTypeDef(
    _ClientCreateClusterResponseClusterClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientCreateClusterResponseClusterDataTransferProgressTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientCreateClusterResponseClusterDataTransferProgressTypeDef(
    _ClientCreateClusterResponseClusterDataTransferProgressTypeDef
):
    pass


_ClientCreateClusterResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientCreateClusterResponseClusterDeferredMaintenanceWindowsTypeDef(
    _ClientCreateClusterResponseClusterDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientCreateClusterResponseClusterElasticIpStatusTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientCreateClusterResponseClusterElasticIpStatusTypeDef(
    _ClientCreateClusterResponseClusterElasticIpStatusTypeDef
):
    pass


_ClientCreateClusterResponseClusterEndpointTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterEndpointTypeDef", {"Address": str, "Port": int}, total=False
)


class ClientCreateClusterResponseClusterEndpointTypeDef(
    _ClientCreateClusterResponseClusterEndpointTypeDef
):
    pass


_ClientCreateClusterResponseClusterHsmStatusTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientCreateClusterResponseClusterHsmStatusTypeDef(
    _ClientCreateClusterResponseClusterHsmStatusTypeDef
):
    pass


_ClientCreateClusterResponseClusterIamRolesTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientCreateClusterResponseClusterIamRolesTypeDef(
    _ClientCreateClusterResponseClusterIamRolesTypeDef
):
    pass


_ClientCreateClusterResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientCreateClusterResponseClusterPendingModifiedValuesTypeDef(
    _ClientCreateClusterResponseClusterPendingModifiedValuesTypeDef
):
    pass


_ClientCreateClusterResponseClusterResizeInfoTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientCreateClusterResponseClusterResizeInfoTypeDef(
    _ClientCreateClusterResponseClusterResizeInfoTypeDef
):
    pass


_ClientCreateClusterResponseClusterRestoreStatusTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientCreateClusterResponseClusterRestoreStatusTypeDef(
    _ClientCreateClusterResponseClusterRestoreStatusTypeDef
):
    pass


_ClientCreateClusterResponseClusterTagsTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateClusterResponseClusterTagsTypeDef(_ClientCreateClusterResponseClusterTagsTypeDef):
    pass


_ClientCreateClusterResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCreateClusterResponseClusterVpcSecurityGroupsTypeDef(
    _ClientCreateClusterResponseClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientCreateClusterResponseClusterTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientCreateClusterResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientCreateClusterResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientCreateClusterResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientCreateClusterResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateClusterResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientCreateClusterResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientCreateClusterResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientCreateClusterResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientCreateClusterResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientCreateClusterResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientCreateClusterResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientCreateClusterResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientCreateClusterResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientCreateClusterResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientCreateClusterResponseClusterResizeInfoTypeDef,
    },
    total=False,
)


class ClientCreateClusterResponseClusterTypeDef(_ClientCreateClusterResponseClusterTypeDef):
    """
    - **Cluster** *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_ClientCreateClusterResponseTypeDef = TypedDict(
    "_ClientCreateClusterResponseTypeDef",
    {"Cluster": ClientCreateClusterResponseClusterTypeDef},
    total=False,
)


class ClientCreateClusterResponseTypeDef(_ClientCreateClusterResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        Describes a cluster.
        - **ClusterIdentifier** *(string) --*

          The unique identifier of the cluster.
    """


_ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef = TypedDict(
    "_ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef(
    _ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef
):
    pass


_ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
        "Tags": List[
            ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef
        ],
    },
    total=False,
)


class ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTypeDef(
    _ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTypeDef
):
    pass


_ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTagsTypeDef = TypedDict(
    "_ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTagsTypeDef(
    _ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTagsTypeDef
):
    pass


_ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTypeDef = TypedDict(
    "_ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
        "Tags": List[
            ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTagsTypeDef
        ],
    },
    total=False,
)


class ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTypeDef(
    _ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTypeDef
):
    pass


_ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTagsTypeDef = TypedDict(
    "_ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTagsTypeDef(
    _ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTagsTypeDef
):
    pass


_ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTypeDef = TypedDict(
    "_ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[
            ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTypeDef
        ],
        "Tags": List[ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTagsTypeDef],
    },
    total=False,
)


class ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTypeDef(
    _ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTypeDef
):
    """
    - **ClusterSecurityGroup** *(dict) --*

      Describes a security group.
      - **ClusterSecurityGroupName** *(string) --*

        The name of the cluster security group to which the operation was applied.
    """


_ClientCreateClusterSecurityGroupResponseTypeDef = TypedDict(
    "_ClientCreateClusterSecurityGroupResponseTypeDef",
    {"ClusterSecurityGroup": ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTypeDef},
    total=False,
)


class ClientCreateClusterSecurityGroupResponseTypeDef(
    _ClientCreateClusterSecurityGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **ClusterSecurityGroup** *(dict) --*

        Describes a security group.
        - **ClusterSecurityGroupName** *(string) --*

          The name of the cluster security group to which the operation was applied.
    """


_ClientCreateClusterSecurityGroupTagsTypeDef = TypedDict(
    "_ClientCreateClusterSecurityGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateClusterSecurityGroupTagsTypeDef(_ClientCreateClusterSecurityGroupTagsTypeDef):
    """
    - *(dict) --*

      A tag consisting of a name/value pair for a resource.
      - **Key** *(string) --*

        The key, or name, for the resource tag.
    """


_ClientCreateClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef = TypedDict(
    "_ClientCreateClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)


class ClientCreateClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef(
    _ClientCreateClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef
):
    pass


_ClientCreateClusterSnapshotResponseSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateClusterSnapshotResponseSnapshotTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateClusterSnapshotResponseSnapshotTagsTypeDef(
    _ClientCreateClusterSnapshotResponseSnapshotTagsTypeDef
):
    pass


_ClientCreateClusterSnapshotResponseSnapshotTypeDef = TypedDict(
    "_ClientCreateClusterSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientCreateClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientCreateClusterSnapshotResponseSnapshotTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)


class ClientCreateClusterSnapshotResponseSnapshotTypeDef(
    _ClientCreateClusterSnapshotResponseSnapshotTypeDef
):
    """
    - **Snapshot** *(dict) --*

      Describes a snapshot.
      - **SnapshotIdentifier** *(string) --*

        The snapshot identifier that is provided in the request.
    """


_ClientCreateClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateClusterSnapshotResponseTypeDef",
    {"Snapshot": ClientCreateClusterSnapshotResponseSnapshotTypeDef},
    total=False,
)


class ClientCreateClusterSnapshotResponseTypeDef(_ClientCreateClusterSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **Snapshot** *(dict) --*

        Describes a snapshot.
        - **SnapshotIdentifier** *(string) --*

          The snapshot identifier that is provided in the request.
    """


_ClientCreateClusterSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateClusterSnapshotTagsTypeDef(_ClientCreateClusterSnapshotTagsTypeDef):
    """
    - *(dict) --*

      A tag consisting of a name/value pair for a resource.
      - **Key** *(string) --*

        The key, or name, for the resource tag.
    """


_ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef = TypedDict(
    "_ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef(
    _ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef
):
    pass


_ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {
        "Name": str,
        "SupportedPlatforms": List[
            ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef
        ],
    },
    total=False,
)


class ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef(
    _ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef
):
    pass


_ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef = TypedDict(
    "_ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef(
    _ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef
):
    pass


_ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTypeDef = TypedDict(
    "_ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef],
        "Tags": List[ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef],
    },
    total=False,
)


class ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTypeDef(
    _ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTypeDef
):
    """
    - **ClusterSubnetGroup** *(dict) --*

      Describes a subnet group.
      - **ClusterSubnetGroupName** *(string) --*

        The name of the cluster subnet group.
    """


_ClientCreateClusterSubnetGroupResponseTypeDef = TypedDict(
    "_ClientCreateClusterSubnetGroupResponseTypeDef",
    {"ClusterSubnetGroup": ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTypeDef},
    total=False,
)


class ClientCreateClusterSubnetGroupResponseTypeDef(_ClientCreateClusterSubnetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **ClusterSubnetGroup** *(dict) --*

        Describes a subnet group.
        - **ClusterSubnetGroupName** *(string) --*

          The name of the cluster subnet group.
    """


_ClientCreateClusterSubnetGroupTagsTypeDef = TypedDict(
    "_ClientCreateClusterSubnetGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateClusterSubnetGroupTagsTypeDef(_ClientCreateClusterSubnetGroupTagsTypeDef):
    """
    - *(dict) --*

      A tag consisting of a name/value pair for a resource.
      - **Key** *(string) --*

        The key, or name, for the resource tag.
    """


_ClientCreateClusterTagsTypeDef = TypedDict(
    "_ClientCreateClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateClusterTagsTypeDef(_ClientCreateClusterTagsTypeDef):
    """
    - *(dict) --*

      A tag consisting of a name/value pair for a resource.
      - **Key** *(string) --*

        The key, or name, for the resource tag.
    """


_ClientCreateEventSubscriptionResponseEventSubscriptionTagsTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionResponseEventSubscriptionTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateEventSubscriptionResponseEventSubscriptionTagsTypeDef(
    _ClientCreateEventSubscriptionResponseEventSubscriptionTagsTypeDef
):
    pass


_ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": datetime,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Severity": str,
        "Enabled": bool,
        "Tags": List[ClientCreateEventSubscriptionResponseEventSubscriptionTagsTypeDef],
    },
    total=False,
)


class ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    - **EventSubscription** *(dict) --*

      Describes event subscriptions.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the Amazon Redshift event notification
        subscription.
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

        Describes event subscriptions.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the Amazon Redshift event notification
          subscription.
    """


_ClientCreateEventSubscriptionTagsTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateEventSubscriptionTagsTypeDef(_ClientCreateEventSubscriptionTagsTypeDef):
    """
    - *(dict) --*

      A tag consisting of a name/value pair for a resource.
      - **Key** *(string) --*

        The key, or name, for the resource tag.
    """


_ClientCreateHsmClientCertificateResponseHsmClientCertificateTagsTypeDef = TypedDict(
    "_ClientCreateHsmClientCertificateResponseHsmClientCertificateTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateHsmClientCertificateResponseHsmClientCertificateTagsTypeDef(
    _ClientCreateHsmClientCertificateResponseHsmClientCertificateTagsTypeDef
):
    pass


_ClientCreateHsmClientCertificateResponseHsmClientCertificateTypeDef = TypedDict(
    "_ClientCreateHsmClientCertificateResponseHsmClientCertificateTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmClientCertificatePublicKey": str,
        "Tags": List[ClientCreateHsmClientCertificateResponseHsmClientCertificateTagsTypeDef],
    },
    total=False,
)


class ClientCreateHsmClientCertificateResponseHsmClientCertificateTypeDef(
    _ClientCreateHsmClientCertificateResponseHsmClientCertificateTypeDef
):
    """
    - **HsmClientCertificate** *(dict) --*

      Returns information about an HSM client certificate. The certificate is stored in a secure
      Hardware Storage Module (HSM), and used by the Amazon Redshift cluster to encrypt data files.
      - **HsmClientCertificateIdentifier** *(string) --*

        The identifier of the HSM client certificate.
    """


_ClientCreateHsmClientCertificateResponseTypeDef = TypedDict(
    "_ClientCreateHsmClientCertificateResponseTypeDef",
    {"HsmClientCertificate": ClientCreateHsmClientCertificateResponseHsmClientCertificateTypeDef},
    total=False,
)


class ClientCreateHsmClientCertificateResponseTypeDef(
    _ClientCreateHsmClientCertificateResponseTypeDef
):
    """
    - *(dict) --*

      - **HsmClientCertificate** *(dict) --*

        Returns information about an HSM client certificate. The certificate is stored in a secure
        Hardware Storage Module (HSM), and used by the Amazon Redshift cluster to encrypt data
        files.
        - **HsmClientCertificateIdentifier** *(string) --*

          The identifier of the HSM client certificate.
    """


_ClientCreateHsmClientCertificateTagsTypeDef = TypedDict(
    "_ClientCreateHsmClientCertificateTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateHsmClientCertificateTagsTypeDef(_ClientCreateHsmClientCertificateTagsTypeDef):
    """
    - *(dict) --*

      A tag consisting of a name/value pair for a resource.
      - **Key** *(string) --*

        The key, or name, for the resource tag.
    """


_ClientCreateHsmConfigurationResponseHsmConfigurationTagsTypeDef = TypedDict(
    "_ClientCreateHsmConfigurationResponseHsmConfigurationTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateHsmConfigurationResponseHsmConfigurationTagsTypeDef(
    _ClientCreateHsmConfigurationResponseHsmConfigurationTagsTypeDef
):
    pass


_ClientCreateHsmConfigurationResponseHsmConfigurationTypeDef = TypedDict(
    "_ClientCreateHsmConfigurationResponseHsmConfigurationTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "Description": str,
        "HsmIpAddress": str,
        "HsmPartitionName": str,
        "Tags": List[ClientCreateHsmConfigurationResponseHsmConfigurationTagsTypeDef],
    },
    total=False,
)


class ClientCreateHsmConfigurationResponseHsmConfigurationTypeDef(
    _ClientCreateHsmConfigurationResponseHsmConfigurationTypeDef
):
    """
    - **HsmConfiguration** *(dict) --*

      Returns information about an HSM configuration, which is an object that describes to Amazon
      Redshift clusters the information they require to connect to an HSM where they can store
      database encryption keys.
      - **HsmConfigurationIdentifier** *(string) --*

        The name of the Amazon Redshift HSM configuration.
    """


_ClientCreateHsmConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateHsmConfigurationResponseTypeDef",
    {"HsmConfiguration": ClientCreateHsmConfigurationResponseHsmConfigurationTypeDef},
    total=False,
)


class ClientCreateHsmConfigurationResponseTypeDef(_ClientCreateHsmConfigurationResponseTypeDef):
    """
    - *(dict) --*

      - **HsmConfiguration** *(dict) --*

        Returns information about an HSM configuration, which is an object that describes to Amazon
        Redshift clusters the information they require to connect to an HSM where they can store
        database encryption keys.
        - **HsmConfigurationIdentifier** *(string) --*

          The name of the Amazon Redshift HSM configuration.
    """


_ClientCreateHsmConfigurationTagsTypeDef = TypedDict(
    "_ClientCreateHsmConfigurationTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateHsmConfigurationTagsTypeDef(_ClientCreateHsmConfigurationTagsTypeDef):
    """
    - *(dict) --*

      A tag consisting of a name/value pair for a resource.
      - **Key** *(string) --*

        The key, or name, for the resource tag.
    """


_ClientCreateScheduledActionResponseTargetActionResizeClusterTypeDef = TypedDict(
    "_ClientCreateScheduledActionResponseTargetActionResizeClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "ClusterType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "Classic": bool,
    },
    total=False,
)


class ClientCreateScheduledActionResponseTargetActionResizeClusterTypeDef(
    _ClientCreateScheduledActionResponseTargetActionResizeClusterTypeDef
):
    pass


_ClientCreateScheduledActionResponseTargetActionTypeDef = TypedDict(
    "_ClientCreateScheduledActionResponseTargetActionTypeDef",
    {"ResizeCluster": ClientCreateScheduledActionResponseTargetActionResizeClusterTypeDef},
    total=False,
)


class ClientCreateScheduledActionResponseTargetActionTypeDef(
    _ClientCreateScheduledActionResponseTargetActionTypeDef
):
    pass


_ClientCreateScheduledActionResponseTypeDef = TypedDict(
    "_ClientCreateScheduledActionResponseTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": ClientCreateScheduledActionResponseTargetActionTypeDef,
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "State": Literal["ACTIVE", "DISABLED"],
        "NextInvocations": List[datetime],
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)


class ClientCreateScheduledActionResponseTypeDef(_ClientCreateScheduledActionResponseTypeDef):
    """
    - *(dict) --*

      Describes a scheduled action. You can use a scheduled action to trigger some Amazon Redshift
      API operations on a schedule. For information about which API operations can be scheduled, see
      ScheduledActionType .
      - **ScheduledActionName** *(string) --*

        The name of the scheduled action.
    """


_RequiredClientCreateScheduledActionTargetActionResizeClusterTypeDef = TypedDict(
    "_RequiredClientCreateScheduledActionTargetActionResizeClusterTypeDef",
    {"ClusterIdentifier": str},
)
_OptionalClientCreateScheduledActionTargetActionResizeClusterTypeDef = TypedDict(
    "_OptionalClientCreateScheduledActionTargetActionResizeClusterTypeDef",
    {"ClusterType": str, "NodeType": str, "NumberOfNodes": int, "Classic": bool},
    total=False,
)


class ClientCreateScheduledActionTargetActionResizeClusterTypeDef(
    _RequiredClientCreateScheduledActionTargetActionResizeClusterTypeDef,
    _OptionalClientCreateScheduledActionTargetActionResizeClusterTypeDef,
):
    """
    - **ResizeCluster** *(dict) --*

      An action that runs a ``ResizeCluster`` API operation.
      - **ClusterIdentifier** *(string) --***[REQUIRED]**

        The unique identifier for the cluster to resize.
    """


_ClientCreateScheduledActionTargetActionTypeDef = TypedDict(
    "_ClientCreateScheduledActionTargetActionTypeDef",
    {"ResizeCluster": ClientCreateScheduledActionTargetActionResizeClusterTypeDef},
    total=False,
)


class ClientCreateScheduledActionTargetActionTypeDef(
    _ClientCreateScheduledActionTargetActionTypeDef
):
    """
    A JSON format string of the Amazon Redshift API operation with input parameters. For more
    information about this parameter, see  ScheduledAction .
    - **ResizeCluster** *(dict) --*

      An action that runs a ``ResizeCluster`` API operation.
      - **ClusterIdentifier** *(string) --***[REQUIRED]**

        The unique identifier for the cluster to resize.
    """


_ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTagsTypeDef = TypedDict(
    "_ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTagsTypeDef(
    _ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTagsTypeDef
):
    pass


_ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTypeDef = TypedDict(
    "_ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTypeDef",
    {
        "SnapshotCopyGrantName": str,
        "KmsKeyId": str,
        "Tags": List[ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTagsTypeDef],
    },
    total=False,
)


class ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTypeDef(
    _ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTypeDef
):
    """
    - **SnapshotCopyGrant** *(dict) --*

      The snapshot copy grant that grants Amazon Redshift permission to encrypt copied snapshots
      with the specified customer master key (CMK) from AWS KMS in the destination region.
      For more information about managing snapshot copy grants, go to `Amazon Redshift Database
      Encryption
      <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html>`__ in the
      *Amazon Redshift Cluster Management Guide* .
      - **SnapshotCopyGrantName** *(string) --*

        The name of the snapshot copy grant.
    """


_ClientCreateSnapshotCopyGrantResponseTypeDef = TypedDict(
    "_ClientCreateSnapshotCopyGrantResponseTypeDef",
    {"SnapshotCopyGrant": ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTypeDef},
    total=False,
)


class ClientCreateSnapshotCopyGrantResponseTypeDef(_ClientCreateSnapshotCopyGrantResponseTypeDef):
    """
    - *(dict) --*

      - **SnapshotCopyGrant** *(dict) --*

        The snapshot copy grant that grants Amazon Redshift permission to encrypt copied snapshots
        with the specified customer master key (CMK) from AWS KMS in the destination region.
        For more information about managing snapshot copy grants, go to `Amazon Redshift Database
        Encryption
        <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html>`__ in the
        *Amazon Redshift Cluster Management Guide* .
        - **SnapshotCopyGrantName** *(string) --*

          The name of the snapshot copy grant.
    """


_ClientCreateSnapshotCopyGrantTagsTypeDef = TypedDict(
    "_ClientCreateSnapshotCopyGrantTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateSnapshotCopyGrantTagsTypeDef(_ClientCreateSnapshotCopyGrantTagsTypeDef):
    """
    - *(dict) --*

      A tag consisting of a name/value pair for a resource.
      - **Key** *(string) --*

        The key, or name, for the resource tag.
    """


_ClientCreateSnapshotScheduleResponseAssociatedClustersTypeDef = TypedDict(
    "_ClientCreateSnapshotScheduleResponseAssociatedClustersTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleAssociationState": Literal["MODIFYING", "ACTIVE", "FAILED"],
    },
    total=False,
)


class ClientCreateSnapshotScheduleResponseAssociatedClustersTypeDef(
    _ClientCreateSnapshotScheduleResponseAssociatedClustersTypeDef
):
    pass


_ClientCreateSnapshotScheduleResponseTagsTypeDef = TypedDict(
    "_ClientCreateSnapshotScheduleResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateSnapshotScheduleResponseTagsTypeDef(
    _ClientCreateSnapshotScheduleResponseTagsTypeDef
):
    pass


_ClientCreateSnapshotScheduleResponseTypeDef = TypedDict(
    "_ClientCreateSnapshotScheduleResponseTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List[ClientCreateSnapshotScheduleResponseTagsTypeDef],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List[ClientCreateSnapshotScheduleResponseAssociatedClustersTypeDef],
    },
    total=False,
)


class ClientCreateSnapshotScheduleResponseTypeDef(_ClientCreateSnapshotScheduleResponseTypeDef):
    """
    - *(dict) --*

      Describes a snapshot schedule. You can set a regular interval for creating snapshots of a
      cluster. You can also schedule snapshots for specific dates.
      - **ScheduleDefinitions** *(list) --*

        A list of ScheduleDefinitions.
        - *(string) --*
    """


_ClientCreateSnapshotScheduleTagsTypeDef = TypedDict(
    "_ClientCreateSnapshotScheduleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateSnapshotScheduleTagsTypeDef(_ClientCreateSnapshotScheduleTagsTypeDef):
    """
    - *(dict) --*

      A tag consisting of a name/value pair for a resource.
      - **Key** *(string) --*

        The key, or name, for the resource tag.
    """


_ClientCreateTagsTagsTypeDef = TypedDict(
    "_ClientCreateTagsTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateTagsTagsTypeDef(_ClientCreateTagsTagsTypeDef):
    """
    - *(dict) --*

      A tag consisting of a name/value pair for a resource.
      - **Key** *(string) --*

        The key, or name, for the resource tag.
    """


_ClientDeleteClusterResponseClusterClusterNodesTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientDeleteClusterResponseClusterClusterNodesTypeDef(
    _ClientDeleteClusterResponseClusterClusterNodesTypeDef
):
    pass


_ClientDeleteClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientDeleteClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientDeleteClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientDeleteClusterResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientDeleteClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientDeleteClusterResponseClusterClusterParameterGroupsTypeDef(
    _ClientDeleteClusterResponseClusterClusterParameterGroupsTypeDef
):
    pass


_ClientDeleteClusterResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientDeleteClusterResponseClusterClusterSecurityGroupsTypeDef(
    _ClientDeleteClusterResponseClusterClusterSecurityGroupsTypeDef
):
    pass


_ClientDeleteClusterResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterClusterSnapshotCopyStatusTypeDef(
    _ClientDeleteClusterResponseClusterClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientDeleteClusterResponseClusterDataTransferProgressTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterDataTransferProgressTypeDef(
    _ClientDeleteClusterResponseClusterDataTransferProgressTypeDef
):
    pass


_ClientDeleteClusterResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterDeferredMaintenanceWindowsTypeDef(
    _ClientDeleteClusterResponseClusterDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientDeleteClusterResponseClusterElasticIpStatusTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientDeleteClusterResponseClusterElasticIpStatusTypeDef(
    _ClientDeleteClusterResponseClusterElasticIpStatusTypeDef
):
    pass


_ClientDeleteClusterResponseClusterEndpointTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterEndpointTypeDef", {"Address": str, "Port": int}, total=False
)


class ClientDeleteClusterResponseClusterEndpointTypeDef(
    _ClientDeleteClusterResponseClusterEndpointTypeDef
):
    pass


_ClientDeleteClusterResponseClusterHsmStatusTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientDeleteClusterResponseClusterHsmStatusTypeDef(
    _ClientDeleteClusterResponseClusterHsmStatusTypeDef
):
    pass


_ClientDeleteClusterResponseClusterIamRolesTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientDeleteClusterResponseClusterIamRolesTypeDef(
    _ClientDeleteClusterResponseClusterIamRolesTypeDef
):
    pass


_ClientDeleteClusterResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterPendingModifiedValuesTypeDef(
    _ClientDeleteClusterResponseClusterPendingModifiedValuesTypeDef
):
    pass


_ClientDeleteClusterResponseClusterResizeInfoTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientDeleteClusterResponseClusterResizeInfoTypeDef(
    _ClientDeleteClusterResponseClusterResizeInfoTypeDef
):
    pass


_ClientDeleteClusterResponseClusterRestoreStatusTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterRestoreStatusTypeDef(
    _ClientDeleteClusterResponseClusterRestoreStatusTypeDef
):
    pass


_ClientDeleteClusterResponseClusterTagsTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDeleteClusterResponseClusterTagsTypeDef(_ClientDeleteClusterResponseClusterTagsTypeDef):
    pass


_ClientDeleteClusterResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDeleteClusterResponseClusterVpcSecurityGroupsTypeDef(
    _ClientDeleteClusterResponseClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientDeleteClusterResponseClusterTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientDeleteClusterResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientDeleteClusterResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientDeleteClusterResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientDeleteClusterResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteClusterResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientDeleteClusterResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientDeleteClusterResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientDeleteClusterResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientDeleteClusterResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientDeleteClusterResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientDeleteClusterResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientDeleteClusterResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientDeleteClusterResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientDeleteClusterResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientDeleteClusterResponseClusterResizeInfoTypeDef,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterTypeDef(_ClientDeleteClusterResponseClusterTypeDef):
    """
    - **Cluster** *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_ClientDeleteClusterResponseTypeDef = TypedDict(
    "_ClientDeleteClusterResponseTypeDef",
    {"Cluster": ClientDeleteClusterResponseClusterTypeDef},
    total=False,
)


class ClientDeleteClusterResponseTypeDef(_ClientDeleteClusterResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        Describes a cluster.
        - **ClusterIdentifier** *(string) --*

          The unique identifier of the cluster.
    """


_ClientDeleteClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef = TypedDict(
    "_ClientDeleteClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)


class ClientDeleteClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef(
    _ClientDeleteClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef
):
    pass


_ClientDeleteClusterSnapshotResponseSnapshotTagsTypeDef = TypedDict(
    "_ClientDeleteClusterSnapshotResponseSnapshotTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDeleteClusterSnapshotResponseSnapshotTagsTypeDef(
    _ClientDeleteClusterSnapshotResponseSnapshotTagsTypeDef
):
    pass


_ClientDeleteClusterSnapshotResponseSnapshotTypeDef = TypedDict(
    "_ClientDeleteClusterSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientDeleteClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientDeleteClusterSnapshotResponseSnapshotTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)


class ClientDeleteClusterSnapshotResponseSnapshotTypeDef(
    _ClientDeleteClusterSnapshotResponseSnapshotTypeDef
):
    """
    - **Snapshot** *(dict) --*

      Describes a snapshot.
      - **SnapshotIdentifier** *(string) --*

        The snapshot identifier that is provided in the request.
    """


_ClientDeleteClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientDeleteClusterSnapshotResponseTypeDef",
    {"Snapshot": ClientDeleteClusterSnapshotResponseSnapshotTypeDef},
    total=False,
)


class ClientDeleteClusterSnapshotResponseTypeDef(_ClientDeleteClusterSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **Snapshot** *(dict) --*

        Describes a snapshot.
        - **SnapshotIdentifier** *(string) --*

          The snapshot identifier that is provided in the request.
    """


_ClientDescribeAccountAttributesResponseAccountAttributesAttributeValuesTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseAccountAttributesAttributeValuesTypeDef",
    {"AttributeValue": str},
    total=False,
)


class ClientDescribeAccountAttributesResponseAccountAttributesAttributeValuesTypeDef(
    _ClientDescribeAccountAttributesResponseAccountAttributesAttributeValuesTypeDef
):
    pass


_ClientDescribeAccountAttributesResponseAccountAttributesTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseAccountAttributesTypeDef",
    {
        "AttributeName": str,
        "AttributeValues": List[
            ClientDescribeAccountAttributesResponseAccountAttributesAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAccountAttributesResponseAccountAttributesTypeDef(
    _ClientDescribeAccountAttributesResponseAccountAttributesTypeDef
):
    """
    - *(dict) --*

      A name value pair that describes an aspect of an account.
      - **AttributeName** *(string) --*

        The name of the attribute.
    """


_ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseTypeDef",
    {"AccountAttributes": List[ClientDescribeAccountAttributesResponseAccountAttributesTypeDef]},
    total=False,
)


class ClientDescribeAccountAttributesResponseTypeDef(
    _ClientDescribeAccountAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **AccountAttributes** *(list) --*

        A list of attributes assigned to an account.
        - *(dict) --*

          A name value pair that describes an aspect of an account.
          - **AttributeName** *(string) --*

            The name of the attribute.
    """


_ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsRevisionTargetsTypeDef = TypedDict(
    "_ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsRevisionTargetsTypeDef",
    {"DatabaseRevision": str, "Description": str, "DatabaseRevisionReleaseDate": datetime},
    total=False,
)


class ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsRevisionTargetsTypeDef(
    _ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsRevisionTargetsTypeDef
):
    pass


_ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsTypeDef = TypedDict(
    "_ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsTypeDef",
    {
        "ClusterIdentifier": str,
        "CurrentDatabaseRevision": str,
        "DatabaseRevisionReleaseDate": datetime,
        "RevisionTargets": List[
            ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsRevisionTargetsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsTypeDef(
    _ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsTypeDef
):
    pass


_ClientDescribeClusterDbRevisionsResponseTypeDef = TypedDict(
    "_ClientDescribeClusterDbRevisionsResponseTypeDef",
    {
        "Marker": str,
        "ClusterDbRevisions": List[
            ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClusterDbRevisionsResponseTypeDef(
    _ClientDescribeClusterDbRevisionsResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        A string representing the starting point for the next set of revisions. If a value is
        returned in a response, you can retrieve the next set of revisions by providing the value in
        the ``marker`` parameter and retrying the command. If the ``marker`` field is empty, all
        revisions have already been returned.
    """


_ClientDescribeClusterParameterGroupsResponseParameterGroupsTagsTypeDef = TypedDict(
    "_ClientDescribeClusterParameterGroupsResponseParameterGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeClusterParameterGroupsResponseParameterGroupsTagsTypeDef(
    _ClientDescribeClusterParameterGroupsResponseParameterGroupsTagsTypeDef
):
    pass


_ClientDescribeClusterParameterGroupsResponseParameterGroupsTypeDef = TypedDict(
    "_ClientDescribeClusterParameterGroupsResponseParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupFamily": str,
        "Description": str,
        "Tags": List[ClientDescribeClusterParameterGroupsResponseParameterGroupsTagsTypeDef],
    },
    total=False,
)


class ClientDescribeClusterParameterGroupsResponseParameterGroupsTypeDef(
    _ClientDescribeClusterParameterGroupsResponseParameterGroupsTypeDef
):
    pass


_ClientDescribeClusterParameterGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeClusterParameterGroupsResponseTypeDef",
    {
        "Marker": str,
        "ParameterGroups": List[ClientDescribeClusterParameterGroupsResponseParameterGroupsTypeDef],
    },
    total=False,
)


class ClientDescribeClusterParameterGroupsResponseTypeDef(
    _ClientDescribeClusterParameterGroupsResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output from the  DescribeClusterParameterGroups action.
      - **Marker** *(string) --*

        A value that indicates the starting point for the next set of response records in a
        subsequent request. If a value is returned in a response, you can retrieve the next set of
        records by providing this returned marker value in the ``Marker`` parameter and retrying the
        command. If the ``Marker`` field is empty, all response records have been retrieved for the
        request.
    """


_ClientDescribeClusterParametersResponseParametersTypeDef = TypedDict(
    "_ClientDescribeClusterParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "ApplyType": Literal["static", "dynamic"],
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)


class ClientDescribeClusterParametersResponseParametersTypeDef(
    _ClientDescribeClusterParametersResponseParametersTypeDef
):
    """
    - *(dict) --*

      Describes a parameter in a cluster parameter group.
      - **ParameterName** *(string) --*

        The name of the parameter.
    """


_ClientDescribeClusterParametersResponseTypeDef = TypedDict(
    "_ClientDescribeClusterParametersResponseTypeDef",
    {"Parameters": List[ClientDescribeClusterParametersResponseParametersTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeClusterParametersResponseTypeDef(
    _ClientDescribeClusterParametersResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output from the  DescribeClusterParameters action.
      - **Parameters** *(list) --*

        A list of  Parameter instances. Each instance lists the parameters of one cluster parameter
        group.
        - *(dict) --*

          Describes a parameter in a cluster parameter group.
          - **ParameterName** *(string) --*

            The name of the parameter.
    """


_ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef = TypedDict(
    "_ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef(
    _ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef
):
    pass


_ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
        "Tags": List[
            ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef(
    _ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef
):
    pass


_ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTagsTypeDef = TypedDict(
    "_ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTagsTypeDef(
    _ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTagsTypeDef
):
    pass


_ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTypeDef = TypedDict(
    "_ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
        "Tags": List[
            ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTagsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTypeDef(
    _ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTypeDef
):
    pass


_ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTagsTypeDef = TypedDict(
    "_ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTagsTypeDef(
    _ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTagsTypeDef
):
    pass


_ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[
            ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTypeDef
        ],
        "Tags": List[ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTagsTypeDef],
    },
    total=False,
)


class ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTypeDef(
    _ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTypeDef
):
    pass


_ClientDescribeClusterSecurityGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeClusterSecurityGroupsResponseTypeDef",
    {
        "Marker": str,
        "ClusterSecurityGroups": List[
            ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClusterSecurityGroupsResponseTypeDef(
    _ClientDescribeClusterSecurityGroupsResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        A value that indicates the starting point for the next set of response records in a
        subsequent request. If a value is returned in a response, you can retrieve the next set of
        records by providing this returned marker value in the ``Marker`` parameter and retrying the
        command. If the ``Marker`` field is empty, all response records have been retrieved for the
        request.
    """


_ClientDescribeClusterSnapshotsResponseSnapshotsAccountsWithRestoreAccessTypeDef = TypedDict(
    "_ClientDescribeClusterSnapshotsResponseSnapshotsAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)


class ClientDescribeClusterSnapshotsResponseSnapshotsAccountsWithRestoreAccessTypeDef(
    _ClientDescribeClusterSnapshotsResponseSnapshotsAccountsWithRestoreAccessTypeDef
):
    pass


_ClientDescribeClusterSnapshotsResponseSnapshotsTagsTypeDef = TypedDict(
    "_ClientDescribeClusterSnapshotsResponseSnapshotsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeClusterSnapshotsResponseSnapshotsTagsTypeDef(
    _ClientDescribeClusterSnapshotsResponseSnapshotsTagsTypeDef
):
    pass


_ClientDescribeClusterSnapshotsResponseSnapshotsTypeDef = TypedDict(
    "_ClientDescribeClusterSnapshotsResponseSnapshotsTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientDescribeClusterSnapshotsResponseSnapshotsAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientDescribeClusterSnapshotsResponseSnapshotsTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)


class ClientDescribeClusterSnapshotsResponseSnapshotsTypeDef(
    _ClientDescribeClusterSnapshotsResponseSnapshotsTypeDef
):
    pass


_ClientDescribeClusterSnapshotsResponseTypeDef = TypedDict(
    "_ClientDescribeClusterSnapshotsResponseTypeDef",
    {"Marker": str, "Snapshots": List[ClientDescribeClusterSnapshotsResponseSnapshotsTypeDef]},
    total=False,
)


class ClientDescribeClusterSnapshotsResponseTypeDef(_ClientDescribeClusterSnapshotsResponseTypeDef):
    """
    - *(dict) --*

      Contains the output from the  DescribeClusterSnapshots action.
      - **Marker** *(string) --*

        A value that indicates the starting point for the next set of response records in a
        subsequent request. If a value is returned in a response, you can retrieve the next set of
        records by providing this returned marker value in the ``Marker`` parameter and retrying the
        command. If the ``Marker`` field is empty, all response records have been retrieved for the
        request.
    """


_RequiredClientDescribeClusterSnapshotsSortingEntitiesTypeDef = TypedDict(
    "_RequiredClientDescribeClusterSnapshotsSortingEntitiesTypeDef",
    {"Attribute": Literal["SOURCE_TYPE", "TOTAL_SIZE", "CREATE_TIME"]},
)
_OptionalClientDescribeClusterSnapshotsSortingEntitiesTypeDef = TypedDict(
    "_OptionalClientDescribeClusterSnapshotsSortingEntitiesTypeDef",
    {"SortOrder": Literal["ASC", "DESC"]},
    total=False,
)


class ClientDescribeClusterSnapshotsSortingEntitiesTypeDef(
    _RequiredClientDescribeClusterSnapshotsSortingEntitiesTypeDef,
    _OptionalClientDescribeClusterSnapshotsSortingEntitiesTypeDef,
):
    """
    - *(dict) --*

      Describes a sorting entity
      - **Attribute** *(string) --***[REQUIRED]**

        The category for sorting the snapshots.
    """


_ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef = TypedDict(
    "_ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef(
    _ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef
):
    pass


_ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {
        "Name": str,
        "SupportedPlatforms": List[
            ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsTypeDef = TypedDict(
    "_ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsTypeDef(
    _ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsTypeDef
):
    pass


_ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTagsTypeDef = TypedDict(
    "_ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTagsTypeDef(
    _ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTagsTypeDef
):
    pass


_ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTypeDef = TypedDict(
    "_ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsTypeDef],
        "Tags": List[ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTagsTypeDef],
    },
    total=False,
)


class ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTypeDef(
    _ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTypeDef
):
    pass


_ClientDescribeClusterSubnetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeClusterSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "ClusterSubnetGroups": List[
            ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClusterSubnetGroupsResponseTypeDef(
    _ClientDescribeClusterSubnetGroupsResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output from the  DescribeClusterSubnetGroups action.
      - **Marker** *(string) --*

        A value that indicates the starting point for the next set of response records in a
        subsequent request. If a value is returned in a response, you can retrieve the next set of
        records by providing this returned marker value in the ``Marker`` parameter and retrying the
        command. If the ``Marker`` field is empty, all response records have been retrieved for the
        request.
    """


_ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef = TypedDict(
    "_ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef",
    {"OperationName": str},
    total=False,
)


class ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef(
    _ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef
):
    pass


_ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsTypeDef = TypedDict(
    "_ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "SupportedOperations": List[
            ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsTypeDef(
    _ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsTypeDef
):
    pass


_ClientDescribeClusterTracksResponseMaintenanceTracksTypeDef = TypedDict(
    "_ClientDescribeClusterTracksResponseMaintenanceTracksTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "UpdateTargets": List[
            ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClusterTracksResponseMaintenanceTracksTypeDef(
    _ClientDescribeClusterTracksResponseMaintenanceTracksTypeDef
):
    """
    - *(dict) --*

      Defines a maintenance track that determines which Amazon Redshift version to apply during a
      maintenance window. If the value for ``MaintenanceTrack`` is ``current`` , the cluster is
      updated to the most recently certified maintenance release. If the value is ``trailing`` , the
      cluster is updated to the previously certified maintenance release.
      - **MaintenanceTrackName** *(string) --*

        The name of the maintenance track. Possible values are ``current`` and ``trailing`` .
    """


_ClientDescribeClusterTracksResponseTypeDef = TypedDict(
    "_ClientDescribeClusterTracksResponseTypeDef",
    {
        "MaintenanceTracks": List[ClientDescribeClusterTracksResponseMaintenanceTracksTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeClusterTracksResponseTypeDef(_ClientDescribeClusterTracksResponseTypeDef):
    """
    - *(dict) --*

      - **MaintenanceTracks** *(list) --*

        A list of maintenance tracks output by the ``DescribeClusterTracks`` operation.
        - *(dict) --*

          Defines a maintenance track that determines which Amazon Redshift version to apply during
          a maintenance window. If the value for ``MaintenanceTrack`` is ``current`` , the cluster
          is updated to the most recently certified maintenance release. If the value is
          ``trailing`` , the cluster is updated to the previously certified maintenance release.
          - **MaintenanceTrackName** *(string) --*

            The name of the maintenance track. Possible values are ``current`` and ``trailing`` .
    """


_ClientDescribeClusterVersionsResponseClusterVersionsTypeDef = TypedDict(
    "_ClientDescribeClusterVersionsResponseClusterVersionsTypeDef",
    {"ClusterVersion": str, "ClusterParameterGroupFamily": str, "Description": str},
    total=False,
)


class ClientDescribeClusterVersionsResponseClusterVersionsTypeDef(
    _ClientDescribeClusterVersionsResponseClusterVersionsTypeDef
):
    pass


_ClientDescribeClusterVersionsResponseTypeDef = TypedDict(
    "_ClientDescribeClusterVersionsResponseTypeDef",
    {
        "Marker": str,
        "ClusterVersions": List[ClientDescribeClusterVersionsResponseClusterVersionsTypeDef],
    },
    total=False,
)


class ClientDescribeClusterVersionsResponseTypeDef(_ClientDescribeClusterVersionsResponseTypeDef):
    """
    - *(dict) --*

      Contains the output from the  DescribeClusterVersions action.
      - **Marker** *(string) --*

        A value that indicates the starting point for the next set of response records in a
        subsequent request. If a value is returned in a response, you can retrieve the next set of
        records by providing this returned marker value in the ``Marker`` parameter and retrying the
        command. If the ``Marker`` field is empty, all response records have been retrieved for the
        request.
    """


_ClientDescribeClustersResponseClustersClusterNodesTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientDescribeClustersResponseClustersClusterNodesTypeDef(
    _ClientDescribeClustersResponseClustersClusterNodesTypeDef
):
    pass


_ClientDescribeClustersResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientDescribeClustersResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientDescribeClustersResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientDescribeClustersResponseClustersClusterParameterGroupsTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientDescribeClustersResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClustersResponseClustersClusterParameterGroupsTypeDef(
    _ClientDescribeClustersResponseClustersClusterParameterGroupsTypeDef
):
    pass


_ClientDescribeClustersResponseClustersClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientDescribeClustersResponseClustersClusterSecurityGroupsTypeDef(
    _ClientDescribeClustersResponseClustersClusterSecurityGroupsTypeDef
):
    pass


_ClientDescribeClustersResponseClustersClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersClusterSnapshotCopyStatusTypeDef(
    _ClientDescribeClustersResponseClustersClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientDescribeClustersResponseClustersDataTransferProgressTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersDataTransferProgressTypeDef(
    _ClientDescribeClustersResponseClustersDataTransferProgressTypeDef
):
    pass


_ClientDescribeClustersResponseClustersDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersDeferredMaintenanceWindowsTypeDef(
    _ClientDescribeClustersResponseClustersDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientDescribeClustersResponseClustersElasticIpStatusTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientDescribeClustersResponseClustersElasticIpStatusTypeDef(
    _ClientDescribeClustersResponseClustersElasticIpStatusTypeDef
):
    pass


_ClientDescribeClustersResponseClustersEndpointTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeClustersResponseClustersEndpointTypeDef(
    _ClientDescribeClustersResponseClustersEndpointTypeDef
):
    pass


_ClientDescribeClustersResponseClustersHsmStatusTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientDescribeClustersResponseClustersHsmStatusTypeDef(
    _ClientDescribeClustersResponseClustersHsmStatusTypeDef
):
    pass


_ClientDescribeClustersResponseClustersIamRolesTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientDescribeClustersResponseClustersIamRolesTypeDef(
    _ClientDescribeClustersResponseClustersIamRolesTypeDef
):
    pass


_ClientDescribeClustersResponseClustersPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersPendingModifiedValuesTypeDef(
    _ClientDescribeClustersResponseClustersPendingModifiedValuesTypeDef
):
    pass


_ClientDescribeClustersResponseClustersResizeInfoTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientDescribeClustersResponseClustersResizeInfoTypeDef(
    _ClientDescribeClustersResponseClustersResizeInfoTypeDef
):
    pass


_ClientDescribeClustersResponseClustersRestoreStatusTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersRestoreStatusTypeDef(
    _ClientDescribeClustersResponseClustersRestoreStatusTypeDef
):
    pass


_ClientDescribeClustersResponseClustersTagsTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeClustersResponseClustersTagsTypeDef(
    _ClientDescribeClustersResponseClustersTagsTypeDef
):
    pass


_ClientDescribeClustersResponseClustersVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDescribeClustersResponseClustersVpcSecurityGroupsTypeDef(
    _ClientDescribeClustersResponseClustersVpcSecurityGroupsTypeDef
):
    pass


_ClientDescribeClustersResponseClustersTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientDescribeClustersResponseClustersEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientDescribeClustersResponseClustersClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientDescribeClustersResponseClustersVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientDescribeClustersResponseClustersClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeClustersResponseClustersPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientDescribeClustersResponseClustersRestoreStatusTypeDef,
        "DataTransferProgress": ClientDescribeClustersResponseClustersDataTransferProgressTypeDef,
        "HsmStatus": ClientDescribeClustersResponseClustersHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientDescribeClustersResponseClustersClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientDescribeClustersResponseClustersClusterNodesTypeDef],
        "ElasticIpStatus": ClientDescribeClustersResponseClustersElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientDescribeClustersResponseClustersTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientDescribeClustersResponseClustersIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientDescribeClustersResponseClustersDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientDescribeClustersResponseClustersResizeInfoTypeDef,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersTypeDef(_ClientDescribeClustersResponseClustersTypeDef):
    pass


_ClientDescribeClustersResponseTypeDef = TypedDict(
    "_ClientDescribeClustersResponseTypeDef",
    {"Marker": str, "Clusters": List[ClientDescribeClustersResponseClustersTypeDef]},
    total=False,
)


class ClientDescribeClustersResponseTypeDef(_ClientDescribeClustersResponseTypeDef):
    """
    - *(dict) --*

      Contains the output from the  DescribeClusters action.
      - **Marker** *(string) --*

        A value that indicates the starting point for the next set of response records in a
        subsequent request. If a value is returned in a response, you can retrieve the next set of
        records by providing this returned marker value in the ``Marker`` parameter and retrying the
        command. If the ``Marker`` field is empty, all response records have been retrieved for the
        request.
    """


_ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersParametersTypeDef = TypedDict(
    "_ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "ApplyType": Literal["static", "dynamic"],
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)


class ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersParametersTypeDef(
    _ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersParametersTypeDef
):
    pass


_ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersTypeDef = TypedDict(
    "_ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersTypeDef",
    {
        "ParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersTypeDef(
    _ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersTypeDef
):
    """
    - **DefaultClusterParameters** *(dict) --*

      Describes the default cluster parameters for a parameter group family.
      - **ParameterGroupFamily** *(string) --*

        The name of the cluster parameter group family to which the engine default parameters apply.
    """


_ClientDescribeDefaultClusterParametersResponseTypeDef = TypedDict(
    "_ClientDescribeDefaultClusterParametersResponseTypeDef",
    {
        "DefaultClusterParameters": ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersTypeDef
    },
    total=False,
)


class ClientDescribeDefaultClusterParametersResponseTypeDef(
    _ClientDescribeDefaultClusterParametersResponseTypeDef
):
    """
    - *(dict) --*

      - **DefaultClusterParameters** *(dict) --*

        Describes the default cluster parameters for a parameter group family.
        - **ParameterGroupFamily** *(string) --*

          The name of the cluster parameter group family to which the engine default parameters
          apply.
    """


_ClientDescribeEventCategoriesResponseEventCategoriesMapListEventsTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesResponseEventCategoriesMapListEventsTypeDef",
    {"EventId": str, "EventCategories": List[str], "EventDescription": str, "Severity": str},
    total=False,
)


class ClientDescribeEventCategoriesResponseEventCategoriesMapListEventsTypeDef(
    _ClientDescribeEventCategoriesResponseEventCategoriesMapListEventsTypeDef
):
    pass


_ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    {
        "SourceType": str,
        "Events": List[ClientDescribeEventCategoriesResponseEventCategoriesMapListEventsTypeDef],
    },
    total=False,
)


class ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef(
    _ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef
):
    """
    - *(dict) --*

      Describes event categories.
      - **SourceType** *(string) --*

        The source type, such as cluster or cluster-snapshot, that the returned categories belong
        to.
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

        A list of event categories descriptions.
        - *(dict) --*

          Describes event categories.
          - **SourceType** *(string) --*

            The source type, such as cluster or cluster-snapshot, that the returned categories
            belong to.
    """


_ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTagsTypeDef = TypedDict(
    "_ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTagsTypeDef(
    _ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTagsTypeDef
):
    pass


_ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef = TypedDict(
    "_ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": datetime,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Severity": str,
        "Enabled": bool,
        "Tags": List[ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTagsTypeDef],
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

        A value that indicates the starting point for the next set of response records in a
        subsequent request. If a value is returned in a response, you can retrieve the next set of
        records by providing this returned marker value in the ``Marker`` parameter and retrying the
        command. If the ``Marker`` field is empty, all response records have been retrieved for the
        request.
    """


_ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal[
            "cluster",
            "cluster-parameter-group",
            "cluster-security-group",
            "cluster-snapshot",
            "scheduled-action",
        ],
        "Message": str,
        "EventCategories": List[str],
        "Severity": str,
        "Date": datetime,
        "EventId": str,
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

        A value that indicates the starting point for the next set of response records in a
        subsequent request. If a value is returned in a response, you can retrieve the next set of
        records by providing this returned marker value in the ``Marker`` parameter and retrying the
        command. If the ``Marker`` field is empty, all response records have been retrieved for the
        request.
    """


_ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTagsTypeDef = TypedDict(
    "_ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTagsTypeDef(
    _ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTagsTypeDef
):
    pass


_ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTypeDef = TypedDict(
    "_ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmClientCertificatePublicKey": str,
        "Tags": List[ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTagsTypeDef],
    },
    total=False,
)


class ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTypeDef(
    _ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTypeDef
):
    pass


_ClientDescribeHsmClientCertificatesResponseTypeDef = TypedDict(
    "_ClientDescribeHsmClientCertificatesResponseTypeDef",
    {
        "Marker": str,
        "HsmClientCertificates": List[
            ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeHsmClientCertificatesResponseTypeDef(
    _ClientDescribeHsmClientCertificatesResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        A value that indicates the starting point for the next set of response records in a
        subsequent request. If a value is returned in a response, you can retrieve the next set of
        records by providing this returned marker value in the ``Marker`` parameter and retrying the
        command. If the ``Marker`` field is empty, all response records have been retrieved for the
        request.
    """


_ClientDescribeHsmConfigurationsResponseHsmConfigurationsTagsTypeDef = TypedDict(
    "_ClientDescribeHsmConfigurationsResponseHsmConfigurationsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeHsmConfigurationsResponseHsmConfigurationsTagsTypeDef(
    _ClientDescribeHsmConfigurationsResponseHsmConfigurationsTagsTypeDef
):
    pass


_ClientDescribeHsmConfigurationsResponseHsmConfigurationsTypeDef = TypedDict(
    "_ClientDescribeHsmConfigurationsResponseHsmConfigurationsTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "Description": str,
        "HsmIpAddress": str,
        "HsmPartitionName": str,
        "Tags": List[ClientDescribeHsmConfigurationsResponseHsmConfigurationsTagsTypeDef],
    },
    total=False,
)


class ClientDescribeHsmConfigurationsResponseHsmConfigurationsTypeDef(
    _ClientDescribeHsmConfigurationsResponseHsmConfigurationsTypeDef
):
    pass


_ClientDescribeHsmConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeHsmConfigurationsResponseTypeDef",
    {
        "Marker": str,
        "HsmConfigurations": List[ClientDescribeHsmConfigurationsResponseHsmConfigurationsTypeDef],
    },
    total=False,
)


class ClientDescribeHsmConfigurationsResponseTypeDef(
    _ClientDescribeHsmConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        A value that indicates the starting point for the next set of response records in a
        subsequent request. If a value is returned in a response, you can retrieve the next set of
        records by providing this returned marker value in the ``Marker`` parameter and retrying the
        command. If the ``Marker`` field is empty, all response records have been retrieved for the
        request.
    """


_ClientDescribeLoggingStatusResponseTypeDef = TypedDict(
    "_ClientDescribeLoggingStatusResponseTypeDef",
    {
        "LoggingEnabled": bool,
        "BucketName": str,
        "S3KeyPrefix": str,
        "LastSuccessfulDeliveryTime": datetime,
        "LastFailureTime": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)


class ClientDescribeLoggingStatusResponseTypeDef(_ClientDescribeLoggingStatusResponseTypeDef):
    """
    - *(dict) --*

      Describes the status of logging for a cluster.
      - **LoggingEnabled** *(boolean) --*

        ``true`` if logging is on, ``false`` if logging is off.
    """


_ClientDescribeNodeConfigurationOptionsFiltersTypeDef = TypedDict(
    "_ClientDescribeNodeConfigurationOptionsFiltersTypeDef",
    {
        "Name": Literal["NodeType", "NumberOfNodes", "EstimatedDiskUtilizationPercent", "Mode"],
        "Operator": Literal["eq", "lt", "gt", "le", "ge", "in", "between"],
        "Values": List[str],
    },
    total=False,
)


class ClientDescribeNodeConfigurationOptionsFiltersTypeDef(
    _ClientDescribeNodeConfigurationOptionsFiltersTypeDef
):
    """
    - *(dict) --*

      A set of elements to filter the returned node configurations.
      - **Name** *(string) --*

        The name of the element to filter.
    """


_ClientDescribeNodeConfigurationOptionsResponseNodeConfigurationOptionListTypeDef = TypedDict(
    "_ClientDescribeNodeConfigurationOptionsResponseNodeConfigurationOptionListTypeDef",
    {
        "NodeType": str,
        "NumberOfNodes": int,
        "EstimatedDiskUtilizationPercent": float,
        "Mode": Literal["standard", "high-performance"],
    },
    total=False,
)


class ClientDescribeNodeConfigurationOptionsResponseNodeConfigurationOptionListTypeDef(
    _ClientDescribeNodeConfigurationOptionsResponseNodeConfigurationOptionListTypeDef
):
    """
    - *(dict) --*

      A list of node configurations.
      - **NodeType** *(string) --*

        The node type, such as, "ds2.8xlarge".
    """


_ClientDescribeNodeConfigurationOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeNodeConfigurationOptionsResponseTypeDef",
    {
        "NodeConfigurationOptionList": List[
            ClientDescribeNodeConfigurationOptionsResponseNodeConfigurationOptionListTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeNodeConfigurationOptionsResponseTypeDef(
    _ClientDescribeNodeConfigurationOptionsResponseTypeDef
):
    """
    - *(dict) --*

      - **NodeConfigurationOptionList** *(list) --*

        A list of valid node configurations.
        - *(dict) --*

          A list of node configurations.
          - **NodeType** *(string) --*

            The node type, such as, "ds2.8xlarge".
    """


_ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef = TypedDict(
    "_ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef(
    _ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef
):
    pass


_ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesTypeDef = TypedDict(
    "_ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesTypeDef",
    {
        "Name": str,
        "SupportedPlatforms": List[
            ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesTypeDef(
    _ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesTypeDef
):
    pass


_ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsTypeDef = TypedDict(
    "_ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsTypeDef",
    {
        "ClusterVersion": str,
        "ClusterType": str,
        "NodeType": str,
        "AvailabilityZones": List[
            ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsTypeDef(
    _ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsTypeDef
):
    """
    - *(dict) --*

      Describes an orderable cluster option.
      - **ClusterVersion** *(string) --*

        The version of the orderable cluster.
    """


_ClientDescribeOrderableClusterOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeOrderableClusterOptionsResponseTypeDef",
    {
        "OrderableClusterOptions": List[
            ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeOrderableClusterOptionsResponseTypeDef(
    _ClientDescribeOrderableClusterOptionsResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output from the  DescribeOrderableClusterOptions action.
      - **OrderableClusterOptions** *(list) --*

        An ``OrderableClusterOption`` structure containing information about orderable options for
        the cluster.
        - *(dict) --*

          Describes an orderable cluster option.
          - **ClusterVersion** *(string) --*

            The version of the orderable cluster.
    """


_ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef = TypedDict(
    "_ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef(
    _ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef
):
    pass


_ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsTypeDef = TypedDict(
    "_ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsTypeDef",
    {
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "OfferingType": str,
        "RecurringCharges": List[
            ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef
        ],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)


class ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsTypeDef(
    _ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsTypeDef
):
    pass


_ClientDescribeReservedNodeOfferingsResponseTypeDef = TypedDict(
    "_ClientDescribeReservedNodeOfferingsResponseTypeDef",
    {
        "Marker": str,
        "ReservedNodeOfferings": List[
            ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedNodeOfferingsResponseTypeDef(
    _ClientDescribeReservedNodeOfferingsResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        A value that indicates the starting point for the next set of response records in a
        subsequent request. If a value is returned in a response, you can retrieve the next set of
        records by providing this returned marker value in the ``Marker`` parameter and retrying the
        command. If the ``Marker`` field is empty, all response records have been retrieved for the
        request.
    """


_ClientDescribeReservedNodesResponseReservedNodesRecurringChargesTypeDef = TypedDict(
    "_ClientDescribeReservedNodesResponseReservedNodesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientDescribeReservedNodesResponseReservedNodesRecurringChargesTypeDef(
    _ClientDescribeReservedNodesResponseReservedNodesRecurringChargesTypeDef
):
    pass


_ClientDescribeReservedNodesResponseReservedNodesTypeDef = TypedDict(
    "_ClientDescribeReservedNodesResponseReservedNodesTypeDef",
    {
        "ReservedNodeId": str,
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "NodeCount": int,
        "State": str,
        "OfferingType": str,
        "RecurringCharges": List[
            ClientDescribeReservedNodesResponseReservedNodesRecurringChargesTypeDef
        ],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)


class ClientDescribeReservedNodesResponseReservedNodesTypeDef(
    _ClientDescribeReservedNodesResponseReservedNodesTypeDef
):
    pass


_ClientDescribeReservedNodesResponseTypeDef = TypedDict(
    "_ClientDescribeReservedNodesResponseTypeDef",
    {"Marker": str, "ReservedNodes": List[ClientDescribeReservedNodesResponseReservedNodesTypeDef]},
    total=False,
)


class ClientDescribeReservedNodesResponseTypeDef(_ClientDescribeReservedNodesResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        A value that indicates the starting point for the next set of response records in a
        subsequent request. If a value is returned in a response, you can retrieve the next set of
        records by providing this returned marker value in the ``Marker`` parameter and retrying the
        command. If the ``Marker`` field is empty, all response records have been retrieved for the
        request.
    """


_ClientDescribeResizeResponseTypeDef = TypedDict(
    "_ClientDescribeResizeResponseTypeDef",
    {
        "TargetNodeType": str,
        "TargetNumberOfNodes": int,
        "TargetClusterType": str,
        "Status": str,
        "ImportTablesCompleted": List[str],
        "ImportTablesInProgress": List[str],
        "ImportTablesNotStarted": List[str],
        "AvgResizeRateInMegaBytesPerSecond": float,
        "TotalResizeDataInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ResizeType": str,
        "Message": str,
        "TargetEncryptionType": str,
        "DataTransferProgressPercent": float,
    },
    total=False,
)


class ClientDescribeResizeResponseTypeDef(_ClientDescribeResizeResponseTypeDef):
    """
    - *(dict) --*

      Describes the result of a cluster resize operation.
      - **TargetNodeType** *(string) --*

        The node type that the cluster will have after the resize operation is complete.
    """


_RequiredClientDescribeScheduledActionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeScheduledActionsFiltersTypeDef",
    {"Name": Literal["cluster-identifier", "iam-role"]},
)
_OptionalClientDescribeScheduledActionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeScheduledActionsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeScheduledActionsFiltersTypeDef(
    _RequiredClientDescribeScheduledActionsFiltersTypeDef,
    _OptionalClientDescribeScheduledActionsFiltersTypeDef,
):
    """
    - *(dict) --*

      A set of elements to filter the returned scheduled actions.
      - **Name** *(string) --***[REQUIRED]**

        The type of element to filter.
    """


_ClientDescribeScheduledActionsResponseScheduledActionsTargetActionResizeClusterTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseScheduledActionsTargetActionResizeClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "ClusterType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "Classic": bool,
    },
    total=False,
)


class ClientDescribeScheduledActionsResponseScheduledActionsTargetActionResizeClusterTypeDef(
    _ClientDescribeScheduledActionsResponseScheduledActionsTargetActionResizeClusterTypeDef
):
    pass


_ClientDescribeScheduledActionsResponseScheduledActionsTargetActionTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseScheduledActionsTargetActionTypeDef",
    {
        "ResizeCluster": ClientDescribeScheduledActionsResponseScheduledActionsTargetActionResizeClusterTypeDef
    },
    total=False,
)


class ClientDescribeScheduledActionsResponseScheduledActionsTargetActionTypeDef(
    _ClientDescribeScheduledActionsResponseScheduledActionsTargetActionTypeDef
):
    pass


_ClientDescribeScheduledActionsResponseScheduledActionsTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseScheduledActionsTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": ClientDescribeScheduledActionsResponseScheduledActionsTargetActionTypeDef,
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "State": Literal["ACTIVE", "DISABLED"],
        "NextInvocations": List[datetime],
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)


class ClientDescribeScheduledActionsResponseScheduledActionsTypeDef(
    _ClientDescribeScheduledActionsResponseScheduledActionsTypeDef
):
    pass


_ClientDescribeScheduledActionsResponseTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseTypeDef",
    {
        "Marker": str,
        "ScheduledActions": List[ClientDescribeScheduledActionsResponseScheduledActionsTypeDef],
    },
    total=False,
)


class ClientDescribeScheduledActionsResponseTypeDef(_ClientDescribeScheduledActionsResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional parameter that specifies the starting point to return a set of response records.
        When the results of a  DescribeScheduledActions request exceed the value specified in
        ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can
        retrieve the next set of response records by providing the returned marker value in the
        ``Marker`` parameter and retrying the request.
    """


_ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTagsTypeDef = TypedDict(
    "_ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTagsTypeDef(
    _ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTagsTypeDef
):
    pass


_ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTypeDef = TypedDict(
    "_ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTypeDef",
    {
        "SnapshotCopyGrantName": str,
        "KmsKeyId": str,
        "Tags": List[ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTagsTypeDef],
    },
    total=False,
)


class ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTypeDef(
    _ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTypeDef
):
    pass


_ClientDescribeSnapshotCopyGrantsResponseTypeDef = TypedDict(
    "_ClientDescribeSnapshotCopyGrantsResponseTypeDef",
    {
        "Marker": str,
        "SnapshotCopyGrants": List[
            ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeSnapshotCopyGrantsResponseTypeDef(
    _ClientDescribeSnapshotCopyGrantsResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional parameter that specifies the starting point to return a set of response records.
        When the results of a ``DescribeSnapshotCopyGrant`` request exceed the value specified in
        ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can
        retrieve the next set of response records by providing the returned marker value in the
        ``Marker`` parameter and retrying the request.
        Constraints: You can specify either the **SnapshotCopyGrantName** parameter or the
        **Marker** parameter, but not both.
    """


_ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesAssociatedClustersTypeDef = TypedDict(
    "_ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesAssociatedClustersTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleAssociationState": Literal["MODIFYING", "ACTIVE", "FAILED"],
    },
    total=False,
)


class ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesAssociatedClustersTypeDef(
    _ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesAssociatedClustersTypeDef
):
    pass


_ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTagsTypeDef = TypedDict(
    "_ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTagsTypeDef(
    _ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTagsTypeDef
):
    pass


_ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTypeDef = TypedDict(
    "_ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List[ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTagsTypeDef],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List[
            ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesAssociatedClustersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTypeDef(
    _ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTypeDef
):
    """
    - *(dict) --*

      Describes a snapshot schedule. You can set a regular interval for creating snapshots of a
      cluster. You can also schedule snapshots for specific dates.
      - **ScheduleDefinitions** *(list) --*

        A list of ScheduleDefinitions.
        - *(string) --*
    """


_ClientDescribeSnapshotSchedulesResponseTypeDef = TypedDict(
    "_ClientDescribeSnapshotSchedulesResponseTypeDef",
    {
        "SnapshotSchedules": List[ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeSnapshotSchedulesResponseTypeDef(
    _ClientDescribeSnapshotSchedulesResponseTypeDef
):
    """
    - *(dict) --*

      - **SnapshotSchedules** *(list) --*

        A list of SnapshotSchedules.
        - *(dict) --*

          Describes a snapshot schedule. You can set a regular interval for creating snapshots of a
          cluster. You can also schedule snapshots for specific dates.
          - **ScheduleDefinitions** *(list) --*

            A list of ScheduleDefinitions.
            - *(string) --*
    """


_ClientDescribeStorageResponseTypeDef = TypedDict(
    "_ClientDescribeStorageResponseTypeDef",
    {"TotalBackupSizeInMegaBytes": float, "TotalProvisionedStorageInMegaBytes": float},
    total=False,
)


class ClientDescribeStorageResponseTypeDef(_ClientDescribeStorageResponseTypeDef):
    """
    - *(dict) --*

      - **TotalBackupSizeInMegaBytes** *(float) --*

        The total amount of storage currently used for snapshots.
    """


_ClientDescribeTableRestoreStatusResponseTableRestoreStatusDetailsTypeDef = TypedDict(
    "_ClientDescribeTableRestoreStatusResponseTableRestoreStatusDetailsTypeDef",
    {
        "TableRestoreRequestId": str,
        "Status": Literal["PENDING", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED"],
        "Message": str,
        "RequestTime": datetime,
        "ProgressInMegaBytes": int,
        "TotalDataInMegaBytes": int,
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SourceDatabaseName": str,
        "SourceSchemaName": str,
        "SourceTableName": str,
        "TargetDatabaseName": str,
        "TargetSchemaName": str,
        "NewTableName": str,
    },
    total=False,
)


class ClientDescribeTableRestoreStatusResponseTableRestoreStatusDetailsTypeDef(
    _ClientDescribeTableRestoreStatusResponseTableRestoreStatusDetailsTypeDef
):
    """
    - *(dict) --*

      Describes the status of a  RestoreTableFromClusterSnapshot operation.
      - **TableRestoreRequestId** *(string) --*

        The unique identifier for the table restore request.
    """


_ClientDescribeTableRestoreStatusResponseTypeDef = TypedDict(
    "_ClientDescribeTableRestoreStatusResponseTypeDef",
    {
        "TableRestoreStatusDetails": List[
            ClientDescribeTableRestoreStatusResponseTableRestoreStatusDetailsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeTableRestoreStatusResponseTypeDef(
    _ClientDescribeTableRestoreStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **TableRestoreStatusDetails** *(list) --*

        A list of status details for one or more table restore requests.
        - *(dict) --*

          Describes the status of a  RestoreTableFromClusterSnapshot operation.
          - **TableRestoreRequestId** *(string) --*

            The unique identifier for the table restore request.
    """


_ClientDescribeTagsResponseTaggedResourcesTagTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTaggedResourcesTagTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeTagsResponseTaggedResourcesTagTypeDef(
    _ClientDescribeTagsResponseTaggedResourcesTagTypeDef
):
    """
    - **Tag** *(dict) --*

      The tag for the resource.
      - **Key** *(string) --*

        The key, or name, for the resource tag.
    """


_ClientDescribeTagsResponseTaggedResourcesTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTaggedResourcesTypeDef",
    {
        "Tag": ClientDescribeTagsResponseTaggedResourcesTagTypeDef,
        "ResourceName": str,
        "ResourceType": str,
    },
    total=False,
)


class ClientDescribeTagsResponseTaggedResourcesTypeDef(
    _ClientDescribeTagsResponseTaggedResourcesTypeDef
):
    """
    - *(dict) --*

      A tag and its associated resource.
      - **Tag** *(dict) --*

        The tag for the resource.
        - **Key** *(string) --*

          The key, or name, for the resource tag.
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {"TaggedResources": List[ClientDescribeTagsResponseTaggedResourcesTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    - *(dict) --*

      - **TaggedResources** *(list) --*

        A list of tags with their associated resources.
        - *(dict) --*

          A tag and its associated resource.
          - **Tag** *(dict) --*

            The tag for the resource.
            - **Key** *(string) --*

              The key, or name, for the resource tag.
    """


_ClientDisableLoggingResponseTypeDef = TypedDict(
    "_ClientDisableLoggingResponseTypeDef",
    {
        "LoggingEnabled": bool,
        "BucketName": str,
        "S3KeyPrefix": str,
        "LastSuccessfulDeliveryTime": datetime,
        "LastFailureTime": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)


class ClientDisableLoggingResponseTypeDef(_ClientDisableLoggingResponseTypeDef):
    """
    - *(dict) --*

      Describes the status of logging for a cluster.
      - **LoggingEnabled** *(boolean) --*

        ``true`` if logging is on, ``false`` if logging is off.
    """


_ClientDisableSnapshotCopyResponseClusterClusterNodesTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterClusterNodesTypeDef(
    _ClientDisableSnapshotCopyResponseClusterClusterNodesTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef(
    _ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef(
    _ClientDisableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef(
    _ClientDisableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterDataTransferProgressTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterDataTransferProgressTypeDef(
    _ClientDisableSnapshotCopyResponseClusterDataTransferProgressTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef(
    _ClientDisableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterElasticIpStatusTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterElasticIpStatusTypeDef(
    _ClientDisableSnapshotCopyResponseClusterElasticIpStatusTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterEndpointTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterEndpointTypeDef(
    _ClientDisableSnapshotCopyResponseClusterEndpointTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterHsmStatusTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterHsmStatusTypeDef(
    _ClientDisableSnapshotCopyResponseClusterHsmStatusTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterIamRolesTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterIamRolesTypeDef(
    _ClientDisableSnapshotCopyResponseClusterIamRolesTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef(
    _ClientDisableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterResizeInfoTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterResizeInfoTypeDef(
    _ClientDisableSnapshotCopyResponseClusterResizeInfoTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterRestoreStatusTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterRestoreStatusTypeDef(
    _ClientDisableSnapshotCopyResponseClusterRestoreStatusTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterTagsTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDisableSnapshotCopyResponseClusterTagsTypeDef(
    _ClientDisableSnapshotCopyResponseClusterTagsTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef(
    _ClientDisableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientDisableSnapshotCopyResponseClusterTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientDisableSnapshotCopyResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientDisableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientDisableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDisableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientDisableSnapshotCopyResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientDisableSnapshotCopyResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientDisableSnapshotCopyResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientDisableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientDisableSnapshotCopyResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientDisableSnapshotCopyResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientDisableSnapshotCopyResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientDisableSnapshotCopyResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientDisableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientDisableSnapshotCopyResponseClusterResizeInfoTypeDef,
    },
    total=False,
)


class ClientDisableSnapshotCopyResponseClusterTypeDef(
    _ClientDisableSnapshotCopyResponseClusterTypeDef
):
    """
    - **Cluster** *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_ClientDisableSnapshotCopyResponseTypeDef = TypedDict(
    "_ClientDisableSnapshotCopyResponseTypeDef",
    {"Cluster": ClientDisableSnapshotCopyResponseClusterTypeDef},
    total=False,
)


class ClientDisableSnapshotCopyResponseTypeDef(_ClientDisableSnapshotCopyResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        Describes a cluster.
        - **ClusterIdentifier** *(string) --*

          The unique identifier of the cluster.
    """


_ClientEnableLoggingResponseTypeDef = TypedDict(
    "_ClientEnableLoggingResponseTypeDef",
    {
        "LoggingEnabled": bool,
        "BucketName": str,
        "S3KeyPrefix": str,
        "LastSuccessfulDeliveryTime": datetime,
        "LastFailureTime": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)


class ClientEnableLoggingResponseTypeDef(_ClientEnableLoggingResponseTypeDef):
    """
    - *(dict) --*

      Describes the status of logging for a cluster.
      - **LoggingEnabled** *(boolean) --*

        ``true`` if logging is on, ``false`` if logging is off.
    """


_ClientEnableSnapshotCopyResponseClusterClusterNodesTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterClusterNodesTypeDef(
    _ClientEnableSnapshotCopyResponseClusterClusterNodesTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef(
    _ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef(
    _ClientEnableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef(
    _ClientEnableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterDataTransferProgressTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterDataTransferProgressTypeDef(
    _ClientEnableSnapshotCopyResponseClusterDataTransferProgressTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef(
    _ClientEnableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterElasticIpStatusTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterElasticIpStatusTypeDef(
    _ClientEnableSnapshotCopyResponseClusterElasticIpStatusTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterEndpointTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterEndpointTypeDef(
    _ClientEnableSnapshotCopyResponseClusterEndpointTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterHsmStatusTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterHsmStatusTypeDef(
    _ClientEnableSnapshotCopyResponseClusterHsmStatusTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterIamRolesTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterIamRolesTypeDef(
    _ClientEnableSnapshotCopyResponseClusterIamRolesTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef(
    _ClientEnableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterResizeInfoTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterResizeInfoTypeDef(
    _ClientEnableSnapshotCopyResponseClusterResizeInfoTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterRestoreStatusTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterRestoreStatusTypeDef(
    _ClientEnableSnapshotCopyResponseClusterRestoreStatusTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterTagsTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientEnableSnapshotCopyResponseClusterTagsTypeDef(
    _ClientEnableSnapshotCopyResponseClusterTagsTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef(
    _ClientEnableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientEnableSnapshotCopyResponseClusterTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientEnableSnapshotCopyResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientEnableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientEnableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientEnableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientEnableSnapshotCopyResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientEnableSnapshotCopyResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientEnableSnapshotCopyResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientEnableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientEnableSnapshotCopyResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientEnableSnapshotCopyResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientEnableSnapshotCopyResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientEnableSnapshotCopyResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientEnableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientEnableSnapshotCopyResponseClusterResizeInfoTypeDef,
    },
    total=False,
)


class ClientEnableSnapshotCopyResponseClusterTypeDef(
    _ClientEnableSnapshotCopyResponseClusterTypeDef
):
    """
    - **Cluster** *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_ClientEnableSnapshotCopyResponseTypeDef = TypedDict(
    "_ClientEnableSnapshotCopyResponseTypeDef",
    {"Cluster": ClientEnableSnapshotCopyResponseClusterTypeDef},
    total=False,
)


class ClientEnableSnapshotCopyResponseTypeDef(_ClientEnableSnapshotCopyResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        Describes a cluster.
        - **ClusterIdentifier** *(string) --*

          The unique identifier of the cluster.
    """


_ClientGetClusterCredentialsResponseTypeDef = TypedDict(
    "_ClientGetClusterCredentialsResponseTypeDef",
    {"DbUser": str, "DbPassword": str, "Expiration": datetime},
    total=False,
)


class ClientGetClusterCredentialsResponseTypeDef(_ClientGetClusterCredentialsResponseTypeDef):
    """
    - *(dict) --*

      Temporary credentials with authorization to log on to an Amazon Redshift database.
      - **DbUser** *(string) --*

        A database user name that is authorized to log on to the database ``DbName`` using the
        password ``DbPassword`` . If the specified DbUser exists in the database, the new user name
        has the same database privileges as the the user named in DbUser. By default, the user is
        added to PUBLIC. If the ``DbGroups`` parameter is specifed, ``DbUser`` is added to the
        listed groups for any sessions created using these credentials.
    """


_ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef = TypedDict(
    "_ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef(
    _ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef
):
    pass


_ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsTypeDef = TypedDict(
    "_ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsTypeDef",
    {
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "OfferingType": str,
        "RecurringCharges": List[
            ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef
        ],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)


class ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsTypeDef(
    _ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsTypeDef
):
    pass


_ClientGetReservedNodeExchangeOfferingsResponseTypeDef = TypedDict(
    "_ClientGetReservedNodeExchangeOfferingsResponseTypeDef",
    {
        "Marker": str,
        "ReservedNodeOfferings": List[
            ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsTypeDef
        ],
    },
    total=False,
)


class ClientGetReservedNodeExchangeOfferingsResponseTypeDef(
    _ClientGetReservedNodeExchangeOfferingsResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional parameter that specifies the starting point for returning a set of response
        records. When the results of a ``GetReservedNodeExchangeOfferings`` request exceed the value
        specified in MaxRecords, Amazon Redshift returns a value in the marker field of the
        response. You can retrieve the next set of response records by providing the returned marker
        value in the marker parameter and retrying the request.
    """


_ClientModifyClusterDbRevisionResponseClusterClusterNodesTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterClusterNodesTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterClusterNodesTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterClusterSecurityGroupsTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterClusterSecurityGroupsTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterClusterSnapshotCopyStatusTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterDataTransferProgressTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterDataTransferProgressTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterDataTransferProgressTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterDeferredMaintenanceWindowsTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterElasticIpStatusTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterElasticIpStatusTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterElasticIpStatusTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterEndpointTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterEndpointTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterEndpointTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterHsmStatusTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterHsmStatusTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterHsmStatusTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterIamRolesTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterIamRolesTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterIamRolesTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterPendingModifiedValuesTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterPendingModifiedValuesTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterResizeInfoTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterResizeInfoTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterResizeInfoTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterRestoreStatusTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterRestoreStatusTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterRestoreStatusTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterTagsTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterTagsTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterTagsTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterVpcSecurityGroupsTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientModifyClusterDbRevisionResponseClusterTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientModifyClusterDbRevisionResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientModifyClusterDbRevisionResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientModifyClusterDbRevisionResponseClusterVpcSecurityGroupsTypeDef
        ],
        "ClusterParameterGroups": List[
            ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyClusterDbRevisionResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientModifyClusterDbRevisionResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientModifyClusterDbRevisionResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientModifyClusterDbRevisionResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientModifyClusterDbRevisionResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientModifyClusterDbRevisionResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientModifyClusterDbRevisionResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientModifyClusterDbRevisionResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientModifyClusterDbRevisionResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientModifyClusterDbRevisionResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientModifyClusterDbRevisionResponseClusterResizeInfoTypeDef,
    },
    total=False,
)


class ClientModifyClusterDbRevisionResponseClusterTypeDef(
    _ClientModifyClusterDbRevisionResponseClusterTypeDef
):
    """
    - **Cluster** *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_ClientModifyClusterDbRevisionResponseTypeDef = TypedDict(
    "_ClientModifyClusterDbRevisionResponseTypeDef",
    {"Cluster": ClientModifyClusterDbRevisionResponseClusterTypeDef},
    total=False,
)


class ClientModifyClusterDbRevisionResponseTypeDef(_ClientModifyClusterDbRevisionResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        Describes a cluster.
        - **ClusterIdentifier** *(string) --*

          The unique identifier of the cluster.
    """


_ClientModifyClusterIamRolesResponseClusterClusterNodesTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterClusterNodesTypeDef(
    _ClientModifyClusterIamRolesResponseClusterClusterNodesTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsTypeDef(
    _ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterClusterSecurityGroupsTypeDef(
    _ClientModifyClusterIamRolesResponseClusterClusterSecurityGroupsTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterClusterSnapshotCopyStatusTypeDef(
    _ClientModifyClusterIamRolesResponseClusterClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterDataTransferProgressTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterDataTransferProgressTypeDef(
    _ClientModifyClusterIamRolesResponseClusterDataTransferProgressTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterDeferredMaintenanceWindowsTypeDef(
    _ClientModifyClusterIamRolesResponseClusterDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterElasticIpStatusTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterElasticIpStatusTypeDef(
    _ClientModifyClusterIamRolesResponseClusterElasticIpStatusTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterEndpointTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterEndpointTypeDef(
    _ClientModifyClusterIamRolesResponseClusterEndpointTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterHsmStatusTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterHsmStatusTypeDef(
    _ClientModifyClusterIamRolesResponseClusterHsmStatusTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterIamRolesTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterIamRolesTypeDef(
    _ClientModifyClusterIamRolesResponseClusterIamRolesTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterPendingModifiedValuesTypeDef(
    _ClientModifyClusterIamRolesResponseClusterPendingModifiedValuesTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterResizeInfoTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterResizeInfoTypeDef(
    _ClientModifyClusterIamRolesResponseClusterResizeInfoTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterRestoreStatusTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterRestoreStatusTypeDef(
    _ClientModifyClusterIamRolesResponseClusterRestoreStatusTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterTagsTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterTagsTypeDef(
    _ClientModifyClusterIamRolesResponseClusterTagsTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterVpcSecurityGroupsTypeDef(
    _ClientModifyClusterIamRolesResponseClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientModifyClusterIamRolesResponseClusterTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientModifyClusterIamRolesResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientModifyClusterIamRolesResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientModifyClusterIamRolesResponseClusterVpcSecurityGroupsTypeDef
        ],
        "ClusterParameterGroups": List[
            ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyClusterIamRolesResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientModifyClusterIamRolesResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientModifyClusterIamRolesResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientModifyClusterIamRolesResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientModifyClusterIamRolesResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientModifyClusterIamRolesResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientModifyClusterIamRolesResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientModifyClusterIamRolesResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientModifyClusterIamRolesResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientModifyClusterIamRolesResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientModifyClusterIamRolesResponseClusterResizeInfoTypeDef,
    },
    total=False,
)


class ClientModifyClusterIamRolesResponseClusterTypeDef(
    _ClientModifyClusterIamRolesResponseClusterTypeDef
):
    """
    - **Cluster** *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_ClientModifyClusterIamRolesResponseTypeDef = TypedDict(
    "_ClientModifyClusterIamRolesResponseTypeDef",
    {"Cluster": ClientModifyClusterIamRolesResponseClusterTypeDef},
    total=False,
)


class ClientModifyClusterIamRolesResponseTypeDef(_ClientModifyClusterIamRolesResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        Describes a cluster.
        - **ClusterIdentifier** *(string) --*

          The unique identifier of the cluster.
    """


_ClientModifyClusterMaintenanceResponseClusterClusterNodesTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterClusterNodesTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterClusterNodesTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterClusterSecurityGroupsTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterClusterSecurityGroupsTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterClusterSnapshotCopyStatusTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterDataTransferProgressTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterDataTransferProgressTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterDataTransferProgressTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterDeferredMaintenanceWindowsTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterElasticIpStatusTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterElasticIpStatusTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterElasticIpStatusTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterEndpointTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterEndpointTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterEndpointTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterHsmStatusTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterHsmStatusTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterHsmStatusTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterIamRolesTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterIamRolesTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterIamRolesTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterPendingModifiedValuesTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterPendingModifiedValuesTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterResizeInfoTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterResizeInfoTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterResizeInfoTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterRestoreStatusTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterRestoreStatusTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterRestoreStatusTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterTagsTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterTagsTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterTagsTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterVpcSecurityGroupsTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientModifyClusterMaintenanceResponseClusterTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientModifyClusterMaintenanceResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientModifyClusterMaintenanceResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientModifyClusterMaintenanceResponseClusterVpcSecurityGroupsTypeDef
        ],
        "ClusterParameterGroups": List[
            ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyClusterMaintenanceResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientModifyClusterMaintenanceResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientModifyClusterMaintenanceResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientModifyClusterMaintenanceResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientModifyClusterMaintenanceResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientModifyClusterMaintenanceResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientModifyClusterMaintenanceResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientModifyClusterMaintenanceResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientModifyClusterMaintenanceResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientModifyClusterMaintenanceResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientModifyClusterMaintenanceResponseClusterResizeInfoTypeDef,
    },
    total=False,
)


class ClientModifyClusterMaintenanceResponseClusterTypeDef(
    _ClientModifyClusterMaintenanceResponseClusterTypeDef
):
    """
    - **Cluster** *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_ClientModifyClusterMaintenanceResponseTypeDef = TypedDict(
    "_ClientModifyClusterMaintenanceResponseTypeDef",
    {"Cluster": ClientModifyClusterMaintenanceResponseClusterTypeDef},
    total=False,
)


class ClientModifyClusterMaintenanceResponseTypeDef(_ClientModifyClusterMaintenanceResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        Describes a cluster.
        - **ClusterIdentifier** *(string) --*

          The unique identifier of the cluster.
    """


_ClientModifyClusterParameterGroupParametersTypeDef = TypedDict(
    "_ClientModifyClusterParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "ApplyType": Literal["static", "dynamic"],
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)


class ClientModifyClusterParameterGroupParametersTypeDef(
    _ClientModifyClusterParameterGroupParametersTypeDef
):
    """
    - *(dict) --*

      Describes a parameter in a cluster parameter group.
      - **ParameterName** *(string) --*

        The name of the parameter.
    """


_ClientModifyClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientModifyClusterParameterGroupResponseTypeDef",
    {"ParameterGroupName": str, "ParameterGroupStatus": str},
    total=False,
)


class ClientModifyClusterParameterGroupResponseTypeDef(
    _ClientModifyClusterParameterGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **ParameterGroupName** *(string) --*

        The name of the cluster parameter group.
    """


_ClientModifyClusterResponseClusterClusterNodesTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientModifyClusterResponseClusterClusterNodesTypeDef(
    _ClientModifyClusterResponseClusterClusterNodesTypeDef
):
    pass


_ClientModifyClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientModifyClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientModifyClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientModifyClusterResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientModifyClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientModifyClusterResponseClusterClusterParameterGroupsTypeDef(
    _ClientModifyClusterResponseClusterClusterParameterGroupsTypeDef
):
    pass


_ClientModifyClusterResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientModifyClusterResponseClusterClusterSecurityGroupsTypeDef(
    _ClientModifyClusterResponseClusterClusterSecurityGroupsTypeDef
):
    pass


_ClientModifyClusterResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientModifyClusterResponseClusterClusterSnapshotCopyStatusTypeDef(
    _ClientModifyClusterResponseClusterClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientModifyClusterResponseClusterDataTransferProgressTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientModifyClusterResponseClusterDataTransferProgressTypeDef(
    _ClientModifyClusterResponseClusterDataTransferProgressTypeDef
):
    pass


_ClientModifyClusterResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientModifyClusterResponseClusterDeferredMaintenanceWindowsTypeDef(
    _ClientModifyClusterResponseClusterDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientModifyClusterResponseClusterElasticIpStatusTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientModifyClusterResponseClusterElasticIpStatusTypeDef(
    _ClientModifyClusterResponseClusterElasticIpStatusTypeDef
):
    pass


_ClientModifyClusterResponseClusterEndpointTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterEndpointTypeDef", {"Address": str, "Port": int}, total=False
)


class ClientModifyClusterResponseClusterEndpointTypeDef(
    _ClientModifyClusterResponseClusterEndpointTypeDef
):
    pass


_ClientModifyClusterResponseClusterHsmStatusTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientModifyClusterResponseClusterHsmStatusTypeDef(
    _ClientModifyClusterResponseClusterHsmStatusTypeDef
):
    pass


_ClientModifyClusterResponseClusterIamRolesTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientModifyClusterResponseClusterIamRolesTypeDef(
    _ClientModifyClusterResponseClusterIamRolesTypeDef
):
    pass


_ClientModifyClusterResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientModifyClusterResponseClusterPendingModifiedValuesTypeDef(
    _ClientModifyClusterResponseClusterPendingModifiedValuesTypeDef
):
    pass


_ClientModifyClusterResponseClusterResizeInfoTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientModifyClusterResponseClusterResizeInfoTypeDef(
    _ClientModifyClusterResponseClusterResizeInfoTypeDef
):
    pass


_ClientModifyClusterResponseClusterRestoreStatusTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientModifyClusterResponseClusterRestoreStatusTypeDef(
    _ClientModifyClusterResponseClusterRestoreStatusTypeDef
):
    pass


_ClientModifyClusterResponseClusterTagsTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientModifyClusterResponseClusterTagsTypeDef(_ClientModifyClusterResponseClusterTagsTypeDef):
    pass


_ClientModifyClusterResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyClusterResponseClusterVpcSecurityGroupsTypeDef(
    _ClientModifyClusterResponseClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientModifyClusterResponseClusterTypeDef = TypedDict(
    "_ClientModifyClusterResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientModifyClusterResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientModifyClusterResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientModifyClusterResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientModifyClusterResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyClusterResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientModifyClusterResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientModifyClusterResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientModifyClusterResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientModifyClusterResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientModifyClusterResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientModifyClusterResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientModifyClusterResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientModifyClusterResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientModifyClusterResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientModifyClusterResponseClusterResizeInfoTypeDef,
    },
    total=False,
)


class ClientModifyClusterResponseClusterTypeDef(_ClientModifyClusterResponseClusterTypeDef):
    """
    - **Cluster** *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_ClientModifyClusterResponseTypeDef = TypedDict(
    "_ClientModifyClusterResponseTypeDef",
    {"Cluster": ClientModifyClusterResponseClusterTypeDef},
    total=False,
)


class ClientModifyClusterResponseTypeDef(_ClientModifyClusterResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        Describes a cluster.
        - **ClusterIdentifier** *(string) --*

          The unique identifier of the cluster.
    """


_ClientModifyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef = TypedDict(
    "_ClientModifyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)


class ClientModifyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef(
    _ClientModifyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef
):
    pass


_ClientModifyClusterSnapshotResponseSnapshotTagsTypeDef = TypedDict(
    "_ClientModifyClusterSnapshotResponseSnapshotTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyClusterSnapshotResponseSnapshotTagsTypeDef(
    _ClientModifyClusterSnapshotResponseSnapshotTagsTypeDef
):
    pass


_ClientModifyClusterSnapshotResponseSnapshotTypeDef = TypedDict(
    "_ClientModifyClusterSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientModifyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientModifyClusterSnapshotResponseSnapshotTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)


class ClientModifyClusterSnapshotResponseSnapshotTypeDef(
    _ClientModifyClusterSnapshotResponseSnapshotTypeDef
):
    """
    - **Snapshot** *(dict) --*

      Describes a snapshot.
      - **SnapshotIdentifier** *(string) --*

        The snapshot identifier that is provided in the request.
    """


_ClientModifyClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientModifyClusterSnapshotResponseTypeDef",
    {"Snapshot": ClientModifyClusterSnapshotResponseSnapshotTypeDef},
    total=False,
)


class ClientModifyClusterSnapshotResponseTypeDef(_ClientModifyClusterSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **Snapshot** *(dict) --*

        Describes a snapshot.
        - **SnapshotIdentifier** *(string) --*

          The snapshot identifier that is provided in the request.
    """


_ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef = TypedDict(
    "_ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    {"Name": str},
    total=False,
)


class ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef(
    _ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef
):
    pass


_ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {
        "Name": str,
        "SupportedPlatforms": List[
            ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef
        ],
    },
    total=False,
)


class ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef(
    _ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef
):
    pass


_ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef = TypedDict(
    "_ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef(
    _ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef
):
    pass


_ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTypeDef = TypedDict(
    "_ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef],
        "Tags": List[ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef],
    },
    total=False,
)


class ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTypeDef(
    _ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTypeDef
):
    """
    - **ClusterSubnetGroup** *(dict) --*

      Describes a subnet group.
      - **ClusterSubnetGroupName** *(string) --*

        The name of the cluster subnet group.
    """


_ClientModifyClusterSubnetGroupResponseTypeDef = TypedDict(
    "_ClientModifyClusterSubnetGroupResponseTypeDef",
    {"ClusterSubnetGroup": ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTypeDef},
    total=False,
)


class ClientModifyClusterSubnetGroupResponseTypeDef(_ClientModifyClusterSubnetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **ClusterSubnetGroup** *(dict) --*

        Describes a subnet group.
        - **ClusterSubnetGroupName** *(string) --*

          The name of the cluster subnet group.
    """


_ClientModifyEventSubscriptionResponseEventSubscriptionTagsTypeDef = TypedDict(
    "_ClientModifyEventSubscriptionResponseEventSubscriptionTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyEventSubscriptionResponseEventSubscriptionTagsTypeDef(
    _ClientModifyEventSubscriptionResponseEventSubscriptionTagsTypeDef
):
    pass


_ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": datetime,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Severity": str,
        "Enabled": bool,
        "Tags": List[ClientModifyEventSubscriptionResponseEventSubscriptionTagsTypeDef],
    },
    total=False,
)


class ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    - **EventSubscription** *(dict) --*

      Describes event subscriptions.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the Amazon Redshift event notification
        subscription.
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

        Describes event subscriptions.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the Amazon Redshift event notification
          subscription.
    """


_ClientModifyScheduledActionResponseTargetActionResizeClusterTypeDef = TypedDict(
    "_ClientModifyScheduledActionResponseTargetActionResizeClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "ClusterType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "Classic": bool,
    },
    total=False,
)


class ClientModifyScheduledActionResponseTargetActionResizeClusterTypeDef(
    _ClientModifyScheduledActionResponseTargetActionResizeClusterTypeDef
):
    pass


_ClientModifyScheduledActionResponseTargetActionTypeDef = TypedDict(
    "_ClientModifyScheduledActionResponseTargetActionTypeDef",
    {"ResizeCluster": ClientModifyScheduledActionResponseTargetActionResizeClusterTypeDef},
    total=False,
)


class ClientModifyScheduledActionResponseTargetActionTypeDef(
    _ClientModifyScheduledActionResponseTargetActionTypeDef
):
    pass


_ClientModifyScheduledActionResponseTypeDef = TypedDict(
    "_ClientModifyScheduledActionResponseTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": ClientModifyScheduledActionResponseTargetActionTypeDef,
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "State": Literal["ACTIVE", "DISABLED"],
        "NextInvocations": List[datetime],
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)


class ClientModifyScheduledActionResponseTypeDef(_ClientModifyScheduledActionResponseTypeDef):
    """
    - *(dict) --*

      Describes a scheduled action. You can use a scheduled action to trigger some Amazon Redshift
      API operations on a schedule. For information about which API operations can be scheduled, see
      ScheduledActionType .
      - **ScheduledActionName** *(string) --*

        The name of the scheduled action.
    """


_RequiredClientModifyScheduledActionTargetActionResizeClusterTypeDef = TypedDict(
    "_RequiredClientModifyScheduledActionTargetActionResizeClusterTypeDef",
    {"ClusterIdentifier": str},
)
_OptionalClientModifyScheduledActionTargetActionResizeClusterTypeDef = TypedDict(
    "_OptionalClientModifyScheduledActionTargetActionResizeClusterTypeDef",
    {"ClusterType": str, "NodeType": str, "NumberOfNodes": int, "Classic": bool},
    total=False,
)


class ClientModifyScheduledActionTargetActionResizeClusterTypeDef(
    _RequiredClientModifyScheduledActionTargetActionResizeClusterTypeDef,
    _OptionalClientModifyScheduledActionTargetActionResizeClusterTypeDef,
):
    """
    - **ResizeCluster** *(dict) --*

      An action that runs a ``ResizeCluster`` API operation.
      - **ClusterIdentifier** *(string) --***[REQUIRED]**

        The unique identifier for the cluster to resize.
    """


_ClientModifyScheduledActionTargetActionTypeDef = TypedDict(
    "_ClientModifyScheduledActionTargetActionTypeDef",
    {"ResizeCluster": ClientModifyScheduledActionTargetActionResizeClusterTypeDef},
    total=False,
)


class ClientModifyScheduledActionTargetActionTypeDef(
    _ClientModifyScheduledActionTargetActionTypeDef
):
    """
    A modified JSON format of the scheduled action. For more information about this parameter, see
    ScheduledAction .
    - **ResizeCluster** *(dict) --*

      An action that runs a ``ResizeCluster`` API operation.
      - **ClusterIdentifier** *(string) --***[REQUIRED]**

        The unique identifier for the cluster to resize.
    """


_ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterNodesTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterNodesTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterNodesTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSecurityGroupsTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSecurityGroupsTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSnapshotCopyStatusTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterDataTransferProgressTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterDataTransferProgressTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterDataTransferProgressTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterDeferredMaintenanceWindowsTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterElasticIpStatusTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterElasticIpStatusTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterElasticIpStatusTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterEndpointTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterEndpointTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterEndpointTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterHsmStatusTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterHsmStatusTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterHsmStatusTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterIamRolesTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterIamRolesTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterIamRolesTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterPendingModifiedValuesTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterPendingModifiedValuesTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterResizeInfoTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterResizeInfoTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterResizeInfoTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterRestoreStatusTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterRestoreStatusTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterRestoreStatusTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterTagsTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterTagsTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterTagsTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterVpcSecurityGroupsTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientModifySnapshotCopyRetentionPeriodResponseClusterTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientModifySnapshotCopyRetentionPeriodResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientModifySnapshotCopyRetentionPeriodResponseClusterVpcSecurityGroupsTypeDef
        ],
        "ClusterParameterGroups": List[
            ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifySnapshotCopyRetentionPeriodResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientModifySnapshotCopyRetentionPeriodResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientModifySnapshotCopyRetentionPeriodResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientModifySnapshotCopyRetentionPeriodResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[
            ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterNodesTypeDef
        ],
        "ElasticIpStatus": ClientModifySnapshotCopyRetentionPeriodResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientModifySnapshotCopyRetentionPeriodResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientModifySnapshotCopyRetentionPeriodResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientModifySnapshotCopyRetentionPeriodResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientModifySnapshotCopyRetentionPeriodResponseClusterResizeInfoTypeDef,
    },
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseClusterTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseClusterTypeDef
):
    """
    - **Cluster** *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_ClientModifySnapshotCopyRetentionPeriodResponseTypeDef = TypedDict(
    "_ClientModifySnapshotCopyRetentionPeriodResponseTypeDef",
    {"Cluster": ClientModifySnapshotCopyRetentionPeriodResponseClusterTypeDef},
    total=False,
)


class ClientModifySnapshotCopyRetentionPeriodResponseTypeDef(
    _ClientModifySnapshotCopyRetentionPeriodResponseTypeDef
):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        Describes a cluster.
        - **ClusterIdentifier** *(string) --*

          The unique identifier of the cluster.
    """


_ClientModifySnapshotScheduleResponseAssociatedClustersTypeDef = TypedDict(
    "_ClientModifySnapshotScheduleResponseAssociatedClustersTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleAssociationState": Literal["MODIFYING", "ACTIVE", "FAILED"],
    },
    total=False,
)


class ClientModifySnapshotScheduleResponseAssociatedClustersTypeDef(
    _ClientModifySnapshotScheduleResponseAssociatedClustersTypeDef
):
    pass


_ClientModifySnapshotScheduleResponseTagsTypeDef = TypedDict(
    "_ClientModifySnapshotScheduleResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientModifySnapshotScheduleResponseTagsTypeDef(
    _ClientModifySnapshotScheduleResponseTagsTypeDef
):
    pass


_ClientModifySnapshotScheduleResponseTypeDef = TypedDict(
    "_ClientModifySnapshotScheduleResponseTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List[ClientModifySnapshotScheduleResponseTagsTypeDef],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List[ClientModifySnapshotScheduleResponseAssociatedClustersTypeDef],
    },
    total=False,
)


class ClientModifySnapshotScheduleResponseTypeDef(_ClientModifySnapshotScheduleResponseTypeDef):
    """
    - *(dict) --*

      Describes a snapshot schedule. You can set a regular interval for creating snapshots of a
      cluster. You can also schedule snapshots for specific dates.
      - **ScheduleDefinitions** *(list) --*

        A list of ScheduleDefinitions.
        - *(string) --*
    """


_ClientPurchaseReservedNodeOfferingResponseReservedNodeRecurringChargesTypeDef = TypedDict(
    "_ClientPurchaseReservedNodeOfferingResponseReservedNodeRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientPurchaseReservedNodeOfferingResponseReservedNodeRecurringChargesTypeDef(
    _ClientPurchaseReservedNodeOfferingResponseReservedNodeRecurringChargesTypeDef
):
    pass


_ClientPurchaseReservedNodeOfferingResponseReservedNodeTypeDef = TypedDict(
    "_ClientPurchaseReservedNodeOfferingResponseReservedNodeTypeDef",
    {
        "ReservedNodeId": str,
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "NodeCount": int,
        "State": str,
        "OfferingType": str,
        "RecurringCharges": List[
            ClientPurchaseReservedNodeOfferingResponseReservedNodeRecurringChargesTypeDef
        ],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)


class ClientPurchaseReservedNodeOfferingResponseReservedNodeTypeDef(
    _ClientPurchaseReservedNodeOfferingResponseReservedNodeTypeDef
):
    """
    - **ReservedNode** *(dict) --*

      Describes a reserved node. You can call the  DescribeReservedNodeOfferings API to obtain the
      available reserved node offerings.
      - **ReservedNodeId** *(string) --*

        The unique identifier for the reservation.
    """


_ClientPurchaseReservedNodeOfferingResponseTypeDef = TypedDict(
    "_ClientPurchaseReservedNodeOfferingResponseTypeDef",
    {"ReservedNode": ClientPurchaseReservedNodeOfferingResponseReservedNodeTypeDef},
    total=False,
)


class ClientPurchaseReservedNodeOfferingResponseTypeDef(
    _ClientPurchaseReservedNodeOfferingResponseTypeDef
):
    """
    - *(dict) --*

      - **ReservedNode** *(dict) --*

        Describes a reserved node. You can call the  DescribeReservedNodeOfferings API to obtain the
        available reserved node offerings.
        - **ReservedNodeId** *(string) --*

          The unique identifier for the reservation.
    """


_ClientRebootClusterResponseClusterClusterNodesTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientRebootClusterResponseClusterClusterNodesTypeDef(
    _ClientRebootClusterResponseClusterClusterNodesTypeDef
):
    pass


_ClientRebootClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientRebootClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientRebootClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientRebootClusterResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientRebootClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientRebootClusterResponseClusterClusterParameterGroupsTypeDef(
    _ClientRebootClusterResponseClusterClusterParameterGroupsTypeDef
):
    pass


_ClientRebootClusterResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientRebootClusterResponseClusterClusterSecurityGroupsTypeDef(
    _ClientRebootClusterResponseClusterClusterSecurityGroupsTypeDef
):
    pass


_ClientRebootClusterResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientRebootClusterResponseClusterClusterSnapshotCopyStatusTypeDef(
    _ClientRebootClusterResponseClusterClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientRebootClusterResponseClusterDataTransferProgressTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientRebootClusterResponseClusterDataTransferProgressTypeDef(
    _ClientRebootClusterResponseClusterDataTransferProgressTypeDef
):
    pass


_ClientRebootClusterResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientRebootClusterResponseClusterDeferredMaintenanceWindowsTypeDef(
    _ClientRebootClusterResponseClusterDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientRebootClusterResponseClusterElasticIpStatusTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientRebootClusterResponseClusterElasticIpStatusTypeDef(
    _ClientRebootClusterResponseClusterElasticIpStatusTypeDef
):
    pass


_ClientRebootClusterResponseClusterEndpointTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterEndpointTypeDef", {"Address": str, "Port": int}, total=False
)


class ClientRebootClusterResponseClusterEndpointTypeDef(
    _ClientRebootClusterResponseClusterEndpointTypeDef
):
    pass


_ClientRebootClusterResponseClusterHsmStatusTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientRebootClusterResponseClusterHsmStatusTypeDef(
    _ClientRebootClusterResponseClusterHsmStatusTypeDef
):
    pass


_ClientRebootClusterResponseClusterIamRolesTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientRebootClusterResponseClusterIamRolesTypeDef(
    _ClientRebootClusterResponseClusterIamRolesTypeDef
):
    pass


_ClientRebootClusterResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientRebootClusterResponseClusterPendingModifiedValuesTypeDef(
    _ClientRebootClusterResponseClusterPendingModifiedValuesTypeDef
):
    pass


_ClientRebootClusterResponseClusterResizeInfoTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientRebootClusterResponseClusterResizeInfoTypeDef(
    _ClientRebootClusterResponseClusterResizeInfoTypeDef
):
    pass


_ClientRebootClusterResponseClusterRestoreStatusTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientRebootClusterResponseClusterRestoreStatusTypeDef(
    _ClientRebootClusterResponseClusterRestoreStatusTypeDef
):
    pass


_ClientRebootClusterResponseClusterTagsTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRebootClusterResponseClusterTagsTypeDef(_ClientRebootClusterResponseClusterTagsTypeDef):
    pass


_ClientRebootClusterResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRebootClusterResponseClusterVpcSecurityGroupsTypeDef(
    _ClientRebootClusterResponseClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientRebootClusterResponseClusterTypeDef = TypedDict(
    "_ClientRebootClusterResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRebootClusterResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientRebootClusterResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientRebootClusterResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientRebootClusterResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootClusterResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientRebootClusterResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientRebootClusterResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientRebootClusterResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientRebootClusterResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientRebootClusterResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientRebootClusterResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientRebootClusterResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientRebootClusterResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientRebootClusterResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientRebootClusterResponseClusterResizeInfoTypeDef,
    },
    total=False,
)


class ClientRebootClusterResponseClusterTypeDef(_ClientRebootClusterResponseClusterTypeDef):
    """
    - **Cluster** *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_ClientRebootClusterResponseTypeDef = TypedDict(
    "_ClientRebootClusterResponseTypeDef",
    {"Cluster": ClientRebootClusterResponseClusterTypeDef},
    total=False,
)


class ClientRebootClusterResponseTypeDef(_ClientRebootClusterResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        Describes a cluster.
        - **ClusterIdentifier** *(string) --*

          The unique identifier of the cluster.
    """


_ClientResetClusterParameterGroupParametersTypeDef = TypedDict(
    "_ClientResetClusterParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "ApplyType": Literal["static", "dynamic"],
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)


class ClientResetClusterParameterGroupParametersTypeDef(
    _ClientResetClusterParameterGroupParametersTypeDef
):
    """
    - *(dict) --*

      Describes a parameter in a cluster parameter group.
      - **ParameterName** *(string) --*

        The name of the parameter.
    """


_ClientResetClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientResetClusterParameterGroupResponseTypeDef",
    {"ParameterGroupName": str, "ParameterGroupStatus": str},
    total=False,
)


class ClientResetClusterParameterGroupResponseTypeDef(
    _ClientResetClusterParameterGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **ParameterGroupName** *(string) --*

        The name of the cluster parameter group.
    """


_ClientResizeClusterResponseClusterClusterNodesTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientResizeClusterResponseClusterClusterNodesTypeDef(
    _ClientResizeClusterResponseClusterClusterNodesTypeDef
):
    pass


_ClientResizeClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientResizeClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientResizeClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientResizeClusterResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientResizeClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientResizeClusterResponseClusterClusterParameterGroupsTypeDef(
    _ClientResizeClusterResponseClusterClusterParameterGroupsTypeDef
):
    pass


_ClientResizeClusterResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientResizeClusterResponseClusterClusterSecurityGroupsTypeDef(
    _ClientResizeClusterResponseClusterClusterSecurityGroupsTypeDef
):
    pass


_ClientResizeClusterResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientResizeClusterResponseClusterClusterSnapshotCopyStatusTypeDef(
    _ClientResizeClusterResponseClusterClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientResizeClusterResponseClusterDataTransferProgressTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientResizeClusterResponseClusterDataTransferProgressTypeDef(
    _ClientResizeClusterResponseClusterDataTransferProgressTypeDef
):
    pass


_ClientResizeClusterResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientResizeClusterResponseClusterDeferredMaintenanceWindowsTypeDef(
    _ClientResizeClusterResponseClusterDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientResizeClusterResponseClusterElasticIpStatusTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientResizeClusterResponseClusterElasticIpStatusTypeDef(
    _ClientResizeClusterResponseClusterElasticIpStatusTypeDef
):
    pass


_ClientResizeClusterResponseClusterEndpointTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterEndpointTypeDef", {"Address": str, "Port": int}, total=False
)


class ClientResizeClusterResponseClusterEndpointTypeDef(
    _ClientResizeClusterResponseClusterEndpointTypeDef
):
    pass


_ClientResizeClusterResponseClusterHsmStatusTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientResizeClusterResponseClusterHsmStatusTypeDef(
    _ClientResizeClusterResponseClusterHsmStatusTypeDef
):
    pass


_ClientResizeClusterResponseClusterIamRolesTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientResizeClusterResponseClusterIamRolesTypeDef(
    _ClientResizeClusterResponseClusterIamRolesTypeDef
):
    pass


_ClientResizeClusterResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientResizeClusterResponseClusterPendingModifiedValuesTypeDef(
    _ClientResizeClusterResponseClusterPendingModifiedValuesTypeDef
):
    pass


_ClientResizeClusterResponseClusterResizeInfoTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientResizeClusterResponseClusterResizeInfoTypeDef(
    _ClientResizeClusterResponseClusterResizeInfoTypeDef
):
    pass


_ClientResizeClusterResponseClusterRestoreStatusTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientResizeClusterResponseClusterRestoreStatusTypeDef(
    _ClientResizeClusterResponseClusterRestoreStatusTypeDef
):
    pass


_ClientResizeClusterResponseClusterTagsTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientResizeClusterResponseClusterTagsTypeDef(_ClientResizeClusterResponseClusterTagsTypeDef):
    pass


_ClientResizeClusterResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientResizeClusterResponseClusterVpcSecurityGroupsTypeDef(
    _ClientResizeClusterResponseClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientResizeClusterResponseClusterTypeDef = TypedDict(
    "_ClientResizeClusterResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientResizeClusterResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientResizeClusterResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientResizeClusterResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientResizeClusterResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientResizeClusterResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientResizeClusterResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientResizeClusterResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientResizeClusterResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientResizeClusterResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientResizeClusterResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientResizeClusterResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientResizeClusterResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientResizeClusterResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientResizeClusterResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientResizeClusterResponseClusterResizeInfoTypeDef,
    },
    total=False,
)


class ClientResizeClusterResponseClusterTypeDef(_ClientResizeClusterResponseClusterTypeDef):
    """
    - **Cluster** *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_ClientResizeClusterResponseTypeDef = TypedDict(
    "_ClientResizeClusterResponseTypeDef",
    {"Cluster": ClientResizeClusterResponseClusterTypeDef},
    total=False,
)


class ClientResizeClusterResponseTypeDef(_ClientResizeClusterResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        Describes a cluster.
        - **ClusterIdentifier** *(string) --*

          The unique identifier of the cluster.
    """


_ClientRestoreFromClusterSnapshotResponseClusterClusterNodesTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterClusterNodesTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterClusterNodesTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterClusterSecurityGroupsTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterClusterSecurityGroupsTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterClusterSnapshotCopyStatusTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterDataTransferProgressTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterDataTransferProgressTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterDataTransferProgressTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterDeferredMaintenanceWindowsTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterElasticIpStatusTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterElasticIpStatusTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterElasticIpStatusTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterEndpointTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterEndpointTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterEndpointTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterHsmStatusTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterHsmStatusTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterHsmStatusTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterIamRolesTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterIamRolesTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterIamRolesTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterPendingModifiedValuesTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterPendingModifiedValuesTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterResizeInfoTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterResizeInfoTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterResizeInfoTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterRestoreStatusTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterRestoreStatusTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterRestoreStatusTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterTagsTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterTagsTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterTagsTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterVpcSecurityGroupsTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientRestoreFromClusterSnapshotResponseClusterTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRestoreFromClusterSnapshotResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientRestoreFromClusterSnapshotResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreFromClusterSnapshotResponseClusterVpcSecurityGroupsTypeDef
        ],
        "ClusterParameterGroups": List[
            ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRestoreFromClusterSnapshotResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientRestoreFromClusterSnapshotResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientRestoreFromClusterSnapshotResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientRestoreFromClusterSnapshotResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientRestoreFromClusterSnapshotResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientRestoreFromClusterSnapshotResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientRestoreFromClusterSnapshotResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientRestoreFromClusterSnapshotResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientRestoreFromClusterSnapshotResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientRestoreFromClusterSnapshotResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientRestoreFromClusterSnapshotResponseClusterResizeInfoTypeDef,
    },
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseClusterTypeDef(
    _ClientRestoreFromClusterSnapshotResponseClusterTypeDef
):
    """
    - **Cluster** *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_ClientRestoreFromClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientRestoreFromClusterSnapshotResponseTypeDef",
    {"Cluster": ClientRestoreFromClusterSnapshotResponseClusterTypeDef},
    total=False,
)


class ClientRestoreFromClusterSnapshotResponseTypeDef(
    _ClientRestoreFromClusterSnapshotResponseTypeDef
):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        Describes a cluster.
        - **ClusterIdentifier** *(string) --*

          The unique identifier of the cluster.
    """


_ClientRestoreTableFromClusterSnapshotResponseTableRestoreStatusTypeDef = TypedDict(
    "_ClientRestoreTableFromClusterSnapshotResponseTableRestoreStatusTypeDef",
    {
        "TableRestoreRequestId": str,
        "Status": Literal["PENDING", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED"],
        "Message": str,
        "RequestTime": datetime,
        "ProgressInMegaBytes": int,
        "TotalDataInMegaBytes": int,
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SourceDatabaseName": str,
        "SourceSchemaName": str,
        "SourceTableName": str,
        "TargetDatabaseName": str,
        "TargetSchemaName": str,
        "NewTableName": str,
    },
    total=False,
)


class ClientRestoreTableFromClusterSnapshotResponseTableRestoreStatusTypeDef(
    _ClientRestoreTableFromClusterSnapshotResponseTableRestoreStatusTypeDef
):
    """
    - **TableRestoreStatus** *(dict) --*

      Describes the status of a  RestoreTableFromClusterSnapshot operation.
      - **TableRestoreRequestId** *(string) --*

        The unique identifier for the table restore request.
    """


_ClientRestoreTableFromClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientRestoreTableFromClusterSnapshotResponseTypeDef",
    {"TableRestoreStatus": ClientRestoreTableFromClusterSnapshotResponseTableRestoreStatusTypeDef},
    total=False,
)


class ClientRestoreTableFromClusterSnapshotResponseTypeDef(
    _ClientRestoreTableFromClusterSnapshotResponseTypeDef
):
    """
    - *(dict) --*

      - **TableRestoreStatus** *(dict) --*

        Describes the status of a  RestoreTableFromClusterSnapshot operation.
        - **TableRestoreRequestId** *(string) --*

          The unique identifier for the table restore request.
    """


_ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef = TypedDict(
    "_ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef(
    _ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef
):
    pass


_ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
        "Tags": List[
            ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef
        ],
    },
    total=False,
)


class ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef(
    _ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef
):
    pass


_ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef = TypedDict(
    "_ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef(
    _ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef
):
    pass


_ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef = TypedDict(
    "_ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
        "Tags": List[
            ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef
        ],
    },
    total=False,
)


class ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef(
    _ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef
):
    pass


_ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef = TypedDict(
    "_ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef(
    _ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef
):
    pass


_ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef = TypedDict(
    "_ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[
            ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef
        ],
        "Tags": List[
            ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef
        ],
    },
    total=False,
)


class ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef(
    _ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef
):
    """
    - **ClusterSecurityGroup** *(dict) --*

      Describes a security group.
      - **ClusterSecurityGroupName** *(string) --*

        The name of the cluster security group to which the operation was applied.
    """


_ClientRevokeClusterSecurityGroupIngressResponseTypeDef = TypedDict(
    "_ClientRevokeClusterSecurityGroupIngressResponseTypeDef",
    {
        "ClusterSecurityGroup": ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef
    },
    total=False,
)


class ClientRevokeClusterSecurityGroupIngressResponseTypeDef(
    _ClientRevokeClusterSecurityGroupIngressResponseTypeDef
):
    """
    - *(dict) --*

      - **ClusterSecurityGroup** *(dict) --*

        Describes a security group.
        - **ClusterSecurityGroupName** *(string) --*

          The name of the cluster security group to which the operation was applied.
    """


_ClientRevokeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef = TypedDict(
    "_ClientRevokeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)


class ClientRevokeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef(
    _ClientRevokeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef
):
    pass


_ClientRevokeSnapshotAccessResponseSnapshotTagsTypeDef = TypedDict(
    "_ClientRevokeSnapshotAccessResponseSnapshotTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRevokeSnapshotAccessResponseSnapshotTagsTypeDef(
    _ClientRevokeSnapshotAccessResponseSnapshotTagsTypeDef
):
    pass


_ClientRevokeSnapshotAccessResponseSnapshotTypeDef = TypedDict(
    "_ClientRevokeSnapshotAccessResponseSnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientRevokeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientRevokeSnapshotAccessResponseSnapshotTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)


class ClientRevokeSnapshotAccessResponseSnapshotTypeDef(
    _ClientRevokeSnapshotAccessResponseSnapshotTypeDef
):
    """
    - **Snapshot** *(dict) --*

      Describes a snapshot.
      - **SnapshotIdentifier** *(string) --*

        The snapshot identifier that is provided in the request.
    """


_ClientRevokeSnapshotAccessResponseTypeDef = TypedDict(
    "_ClientRevokeSnapshotAccessResponseTypeDef",
    {"Snapshot": ClientRevokeSnapshotAccessResponseSnapshotTypeDef},
    total=False,
)


class ClientRevokeSnapshotAccessResponseTypeDef(_ClientRevokeSnapshotAccessResponseTypeDef):
    """
    - *(dict) --*

      - **Snapshot** *(dict) --*

        Describes a snapshot.
        - **SnapshotIdentifier** *(string) --*

          The snapshot identifier that is provided in the request.
    """


_ClientRotateEncryptionKeyResponseClusterClusterNodesTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterClusterNodesTypeDef(
    _ClientRotateEncryptionKeyResponseClusterClusterNodesTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef(
    _ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsTypeDef(
    _ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterClusterSecurityGroupsTypeDef(
    _ClientRotateEncryptionKeyResponseClusterClusterSecurityGroupsTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterClusterSnapshotCopyStatusTypeDef(
    _ClientRotateEncryptionKeyResponseClusterClusterSnapshotCopyStatusTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterDataTransferProgressTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterDataTransferProgressTypeDef(
    _ClientRotateEncryptionKeyResponseClusterDataTransferProgressTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterDeferredMaintenanceWindowsTypeDef(
    _ClientRotateEncryptionKeyResponseClusterDeferredMaintenanceWindowsTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterElasticIpStatusTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterElasticIpStatusTypeDef(
    _ClientRotateEncryptionKeyResponseClusterElasticIpStatusTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterEndpointTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterEndpointTypeDef(
    _ClientRotateEncryptionKeyResponseClusterEndpointTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterHsmStatusTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterHsmStatusTypeDef(
    _ClientRotateEncryptionKeyResponseClusterHsmStatusTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterIamRolesTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterIamRolesTypeDef(
    _ClientRotateEncryptionKeyResponseClusterIamRolesTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterPendingModifiedValuesTypeDef(
    _ClientRotateEncryptionKeyResponseClusterPendingModifiedValuesTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterResizeInfoTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterResizeInfoTypeDef(
    _ClientRotateEncryptionKeyResponseClusterResizeInfoTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterRestoreStatusTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterRestoreStatusTypeDef(
    _ClientRotateEncryptionKeyResponseClusterRestoreStatusTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterTagsTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRotateEncryptionKeyResponseClusterTagsTypeDef(
    _ClientRotateEncryptionKeyResponseClusterTagsTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterVpcSecurityGroupsTypeDef(
    _ClientRotateEncryptionKeyResponseClusterVpcSecurityGroupsTypeDef
):
    pass


_ClientRotateEncryptionKeyResponseClusterTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRotateEncryptionKeyResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientRotateEncryptionKeyResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientRotateEncryptionKeyResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRotateEncryptionKeyResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientRotateEncryptionKeyResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientRotateEncryptionKeyResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientRotateEncryptionKeyResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientRotateEncryptionKeyResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientRotateEncryptionKeyResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientRotateEncryptionKeyResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientRotateEncryptionKeyResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientRotateEncryptionKeyResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientRotateEncryptionKeyResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientRotateEncryptionKeyResponseClusterResizeInfoTypeDef,
    },
    total=False,
)


class ClientRotateEncryptionKeyResponseClusterTypeDef(
    _ClientRotateEncryptionKeyResponseClusterTypeDef
):
    """
    - **Cluster** *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_ClientRotateEncryptionKeyResponseTypeDef = TypedDict(
    "_ClientRotateEncryptionKeyResponseTypeDef",
    {"Cluster": ClientRotateEncryptionKeyResponseClusterTypeDef},
    total=False,
)


class ClientRotateEncryptionKeyResponseTypeDef(_ClientRotateEncryptionKeyResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        Describes a cluster.
        - **ClusterIdentifier** *(string) --*

          The unique identifier of the cluster.
    """


_ClusterAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_ClusterAvailableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class ClusterAvailableWaitWaiterConfigTypeDef(_ClusterAvailableWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 60
    """


_ClusterDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_ClusterDeletedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class ClusterDeletedWaitWaiterConfigTypeDef(_ClusterDeletedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 60
    """


_ClusterRestoredWaitWaiterConfigTypeDef = TypedDict(
    "_ClusterRestoredWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class ClusterRestoredWaitWaiterConfigTypeDef(_ClusterRestoredWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 60
    """


_DescribeClusterDbRevisionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeClusterDbRevisionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeClusterDbRevisionsPaginatePaginationConfigTypeDef(
    _DescribeClusterDbRevisionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeClusterDbRevisionsPaginateResponseClusterDbRevisionsRevisionTargetsTypeDef = TypedDict(
    "_DescribeClusterDbRevisionsPaginateResponseClusterDbRevisionsRevisionTargetsTypeDef",
    {"DatabaseRevision": str, "Description": str, "DatabaseRevisionReleaseDate": datetime},
    total=False,
)


class DescribeClusterDbRevisionsPaginateResponseClusterDbRevisionsRevisionTargetsTypeDef(
    _DescribeClusterDbRevisionsPaginateResponseClusterDbRevisionsRevisionTargetsTypeDef
):
    pass


_DescribeClusterDbRevisionsPaginateResponseClusterDbRevisionsTypeDef = TypedDict(
    "_DescribeClusterDbRevisionsPaginateResponseClusterDbRevisionsTypeDef",
    {
        "ClusterIdentifier": str,
        "CurrentDatabaseRevision": str,
        "DatabaseRevisionReleaseDate": datetime,
        "RevisionTargets": List[
            DescribeClusterDbRevisionsPaginateResponseClusterDbRevisionsRevisionTargetsTypeDef
        ],
    },
    total=False,
)


class DescribeClusterDbRevisionsPaginateResponseClusterDbRevisionsTypeDef(
    _DescribeClusterDbRevisionsPaginateResponseClusterDbRevisionsTypeDef
):
    """
    - *(dict) --*

      Describes a ``ClusterDbRevision`` .
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_DescribeClusterDbRevisionsPaginateResponseTypeDef = TypedDict(
    "_DescribeClusterDbRevisionsPaginateResponseTypeDef",
    {
        "ClusterDbRevisions": List[
            DescribeClusterDbRevisionsPaginateResponseClusterDbRevisionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeClusterDbRevisionsPaginateResponseTypeDef(
    _DescribeClusterDbRevisionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ClusterDbRevisions** *(list) --*

        A list of revisions.
        - *(dict) --*

          Describes a ``ClusterDbRevision`` .
          - **ClusterIdentifier** *(string) --*

            The unique identifier of the cluster.
    """


_DescribeClusterParameterGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeClusterParameterGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeClusterParameterGroupsPaginatePaginationConfigTypeDef(
    _DescribeClusterParameterGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeClusterParameterGroupsPaginateResponseParameterGroupsTagsTypeDef = TypedDict(
    "_DescribeClusterParameterGroupsPaginateResponseParameterGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeClusterParameterGroupsPaginateResponseParameterGroupsTagsTypeDef(
    _DescribeClusterParameterGroupsPaginateResponseParameterGroupsTagsTypeDef
):
    pass


_DescribeClusterParameterGroupsPaginateResponseParameterGroupsTypeDef = TypedDict(
    "_DescribeClusterParameterGroupsPaginateResponseParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupFamily": str,
        "Description": str,
        "Tags": List[DescribeClusterParameterGroupsPaginateResponseParameterGroupsTagsTypeDef],
    },
    total=False,
)


class DescribeClusterParameterGroupsPaginateResponseParameterGroupsTypeDef(
    _DescribeClusterParameterGroupsPaginateResponseParameterGroupsTypeDef
):
    """
    - *(dict) --*

      Describes a parameter group.
      - **ParameterGroupName** *(string) --*

        The name of the cluster parameter group.
    """


_DescribeClusterParameterGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeClusterParameterGroupsPaginateResponseTypeDef",
    {
        "ParameterGroups": List[
            DescribeClusterParameterGroupsPaginateResponseParameterGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeClusterParameterGroupsPaginateResponseTypeDef(
    _DescribeClusterParameterGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output from the  DescribeClusterParameterGroups action.
      - **ParameterGroups** *(list) --*

        A list of  ClusterParameterGroup instances. Each instance describes one cluster parameter
        group.
        - *(dict) --*

          Describes a parameter group.
          - **ParameterGroupName** *(string) --*

            The name of the cluster parameter group.
    """


_DescribeClusterParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeClusterParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeClusterParametersPaginatePaginationConfigTypeDef(
    _DescribeClusterParametersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeClusterParametersPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeClusterParametersPaginateResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "ApplyType": Literal["static", "dynamic"],
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)


class DescribeClusterParametersPaginateResponseParametersTypeDef(
    _DescribeClusterParametersPaginateResponseParametersTypeDef
):
    """
    - *(dict) --*

      Describes a parameter in a cluster parameter group.
      - **ParameterName** *(string) --*

        The name of the parameter.
    """


_DescribeClusterParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeClusterParametersPaginateResponseTypeDef",
    {
        "Parameters": List[DescribeClusterParametersPaginateResponseParametersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeClusterParametersPaginateResponseTypeDef(
    _DescribeClusterParametersPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output from the  DescribeClusterParameters action.
      - **Parameters** *(list) --*

        A list of  Parameter instances. Each instance lists the parameters of one cluster parameter
        group.
        - *(dict) --*

          Describes a parameter in a cluster parameter group.
          - **ParameterName** *(string) --*

            The name of the parameter.
    """


_DescribeClusterSecurityGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeClusterSecurityGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeClusterSecurityGroupsPaginatePaginationConfigTypeDef(
    _DescribeClusterSecurityGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef = TypedDict(
    "_DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef(
    _DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef
):
    pass


_DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef = TypedDict(
    "_DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
        "Tags": List[
            DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef
        ],
    },
    total=False,
)


class DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef(
    _DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef
):
    pass


_DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsIPRangesTagsTypeDef = TypedDict(
    "_DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsIPRangesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsIPRangesTagsTypeDef(
    _DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsIPRangesTagsTypeDef
):
    pass


_DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsIPRangesTypeDef = TypedDict(
    "_DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsIPRangesTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
        "Tags": List[
            DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsIPRangesTagsTypeDef
        ],
    },
    total=False,
)


class DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsIPRangesTypeDef(
    _DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsIPRangesTypeDef
):
    pass


_DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsTagsTypeDef = TypedDict(
    "_DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsTagsTypeDef(
    _DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsTagsTypeDef
):
    pass


_DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[
            DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsIPRangesTypeDef
        ],
        "Tags": List[DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsTagsTypeDef],
    },
    total=False,
)


class DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsTypeDef(
    _DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsTypeDef
):
    """
    - *(dict) --*

      Describes a security group.
      - **ClusterSecurityGroupName** *(string) --*

        The name of the cluster security group to which the operation was applied.
    """


_DescribeClusterSecurityGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeClusterSecurityGroupsPaginateResponseTypeDef",
    {
        "ClusterSecurityGroups": List[
            DescribeClusterSecurityGroupsPaginateResponseClusterSecurityGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeClusterSecurityGroupsPaginateResponseTypeDef(
    _DescribeClusterSecurityGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ClusterSecurityGroups** *(list) --*

        A list of  ClusterSecurityGroup instances.
        - *(dict) --*

          Describes a security group.
          - **ClusterSecurityGroupName** *(string) --*

            The name of the cluster security group to which the operation was applied.
    """


_DescribeClusterSnapshotsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeClusterSnapshotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeClusterSnapshotsPaginatePaginationConfigTypeDef(
    _DescribeClusterSnapshotsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeClusterSnapshotsPaginateResponseSnapshotsAccountsWithRestoreAccessTypeDef = TypedDict(
    "_DescribeClusterSnapshotsPaginateResponseSnapshotsAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)


class DescribeClusterSnapshotsPaginateResponseSnapshotsAccountsWithRestoreAccessTypeDef(
    _DescribeClusterSnapshotsPaginateResponseSnapshotsAccountsWithRestoreAccessTypeDef
):
    pass


_DescribeClusterSnapshotsPaginateResponseSnapshotsTagsTypeDef = TypedDict(
    "_DescribeClusterSnapshotsPaginateResponseSnapshotsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeClusterSnapshotsPaginateResponseSnapshotsTagsTypeDef(
    _DescribeClusterSnapshotsPaginateResponseSnapshotsTagsTypeDef
):
    pass


_DescribeClusterSnapshotsPaginateResponseSnapshotsTypeDef = TypedDict(
    "_DescribeClusterSnapshotsPaginateResponseSnapshotsTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            DescribeClusterSnapshotsPaginateResponseSnapshotsAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[DescribeClusterSnapshotsPaginateResponseSnapshotsTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)


class DescribeClusterSnapshotsPaginateResponseSnapshotsTypeDef(
    _DescribeClusterSnapshotsPaginateResponseSnapshotsTypeDef
):
    """
    - *(dict) --*

      Describes a snapshot.
      - **SnapshotIdentifier** *(string) --*

        The snapshot identifier that is provided in the request.
    """


_DescribeClusterSnapshotsPaginateResponseTypeDef = TypedDict(
    "_DescribeClusterSnapshotsPaginateResponseTypeDef",
    {"Snapshots": List[DescribeClusterSnapshotsPaginateResponseSnapshotsTypeDef], "NextToken": str},
    total=False,
)


class DescribeClusterSnapshotsPaginateResponseTypeDef(
    _DescribeClusterSnapshotsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output from the  DescribeClusterSnapshots action.
      - **Snapshots** *(list) --*

        A list of  Snapshot instances.
        - *(dict) --*

          Describes a snapshot.
          - **SnapshotIdentifier** *(string) --*

            The snapshot identifier that is provided in the request.
    """


_RequiredDescribeClusterSnapshotsPaginateSortingEntitiesTypeDef = TypedDict(
    "_RequiredDescribeClusterSnapshotsPaginateSortingEntitiesTypeDef",
    {"Attribute": Literal["SOURCE_TYPE", "TOTAL_SIZE", "CREATE_TIME"]},
)
_OptionalDescribeClusterSnapshotsPaginateSortingEntitiesTypeDef = TypedDict(
    "_OptionalDescribeClusterSnapshotsPaginateSortingEntitiesTypeDef",
    {"SortOrder": Literal["ASC", "DESC"]},
    total=False,
)


class DescribeClusterSnapshotsPaginateSortingEntitiesTypeDef(
    _RequiredDescribeClusterSnapshotsPaginateSortingEntitiesTypeDef,
    _OptionalDescribeClusterSnapshotsPaginateSortingEntitiesTypeDef,
):
    """
    - *(dict) --*

      Describes a sorting entity
      - **Attribute** *(string) --***[REQUIRED]**

        The category for sorting the snapshots.
    """


_DescribeClusterSubnetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeClusterSubnetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeClusterSubnetGroupsPaginatePaginationConfigTypeDef(
    _DescribeClusterSubnetGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef = TypedDict(
    "_DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    {"Name": str},
    total=False,
)


class DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef(
    _DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef
):
    pass


_DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {
        "Name": str,
        "SupportedPlatforms": List[
            DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef
        ],
    },
    total=False,
)


class DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsTypeDef = TypedDict(
    "_DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsTypeDef(
    _DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsTypeDef
):
    pass


_DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsTagsTypeDef = TypedDict(
    "_DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsTagsTypeDef(
    _DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsTagsTypeDef
):
    pass


_DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsTypeDef = TypedDict(
    "_DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsSubnetsTypeDef
        ],
        "Tags": List[DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsTagsTypeDef],
    },
    total=False,
)


class DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsTypeDef(
    _DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsTypeDef
):
    """
    - *(dict) --*

      Describes a subnet group.
      - **ClusterSubnetGroupName** *(string) --*

        The name of the cluster subnet group.
    """


_DescribeClusterSubnetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeClusterSubnetGroupsPaginateResponseTypeDef",
    {
        "ClusterSubnetGroups": List[
            DescribeClusterSubnetGroupsPaginateResponseClusterSubnetGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeClusterSubnetGroupsPaginateResponseTypeDef(
    _DescribeClusterSubnetGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output from the  DescribeClusterSubnetGroups action.
      - **ClusterSubnetGroups** *(list) --*

        A list of  ClusterSubnetGroup instances.
        - *(dict) --*

          Describes a subnet group.
          - **ClusterSubnetGroupName** *(string) --*

            The name of the cluster subnet group.
    """


_DescribeClusterTracksPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeClusterTracksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeClusterTracksPaginatePaginationConfigTypeDef(
    _DescribeClusterTracksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeClusterTracksPaginateResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef = TypedDict(
    "_DescribeClusterTracksPaginateResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef",
    {"OperationName": str},
    total=False,
)


class DescribeClusterTracksPaginateResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef(
    _DescribeClusterTracksPaginateResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef
):
    pass


_DescribeClusterTracksPaginateResponseMaintenanceTracksUpdateTargetsTypeDef = TypedDict(
    "_DescribeClusterTracksPaginateResponseMaintenanceTracksUpdateTargetsTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "SupportedOperations": List[
            DescribeClusterTracksPaginateResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef
        ],
    },
    total=False,
)


class DescribeClusterTracksPaginateResponseMaintenanceTracksUpdateTargetsTypeDef(
    _DescribeClusterTracksPaginateResponseMaintenanceTracksUpdateTargetsTypeDef
):
    pass


_DescribeClusterTracksPaginateResponseMaintenanceTracksTypeDef = TypedDict(
    "_DescribeClusterTracksPaginateResponseMaintenanceTracksTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "UpdateTargets": List[
            DescribeClusterTracksPaginateResponseMaintenanceTracksUpdateTargetsTypeDef
        ],
    },
    total=False,
)


class DescribeClusterTracksPaginateResponseMaintenanceTracksTypeDef(
    _DescribeClusterTracksPaginateResponseMaintenanceTracksTypeDef
):
    """
    - *(dict) --*

      Defines a maintenance track that determines which Amazon Redshift version to apply during a
      maintenance window. If the value for ``MaintenanceTrack`` is ``current`` , the cluster is
      updated to the most recently certified maintenance release. If the value is ``trailing`` , the
      cluster is updated to the previously certified maintenance release.
      - **MaintenanceTrackName** *(string) --*

        The name of the maintenance track. Possible values are ``current`` and ``trailing`` .
    """


_DescribeClusterTracksPaginateResponseTypeDef = TypedDict(
    "_DescribeClusterTracksPaginateResponseTypeDef",
    {
        "MaintenanceTracks": List[DescribeClusterTracksPaginateResponseMaintenanceTracksTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeClusterTracksPaginateResponseTypeDef(_DescribeClusterTracksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **MaintenanceTracks** *(list) --*

        A list of maintenance tracks output by the ``DescribeClusterTracks`` operation.
        - *(dict) --*

          Defines a maintenance track that determines which Amazon Redshift version to apply during
          a maintenance window. If the value for ``MaintenanceTrack`` is ``current`` , the cluster
          is updated to the most recently certified maintenance release. If the value is
          ``trailing`` , the cluster is updated to the previously certified maintenance release.
          - **MaintenanceTrackName** *(string) --*

            The name of the maintenance track. Possible values are ``current`` and ``trailing`` .
    """


_DescribeClusterVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeClusterVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeClusterVersionsPaginatePaginationConfigTypeDef(
    _DescribeClusterVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeClusterVersionsPaginateResponseClusterVersionsTypeDef = TypedDict(
    "_DescribeClusterVersionsPaginateResponseClusterVersionsTypeDef",
    {"ClusterVersion": str, "ClusterParameterGroupFamily": str, "Description": str},
    total=False,
)


class DescribeClusterVersionsPaginateResponseClusterVersionsTypeDef(
    _DescribeClusterVersionsPaginateResponseClusterVersionsTypeDef
):
    """
    - *(dict) --*

      Describes a cluster version, including the parameter group family and description of the
      version.
      - **ClusterVersion** *(string) --*

        The version number used by the cluster.
    """


_DescribeClusterVersionsPaginateResponseTypeDef = TypedDict(
    "_DescribeClusterVersionsPaginateResponseTypeDef",
    {
        "ClusterVersions": List[DescribeClusterVersionsPaginateResponseClusterVersionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeClusterVersionsPaginateResponseTypeDef(
    _DescribeClusterVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output from the  DescribeClusterVersions action.
      - **ClusterVersions** *(list) --*

        A list of ``Version`` elements.
        - *(dict) --*

          Describes a cluster version, including the parameter group family and description of the
          version.
          - **ClusterVersion** *(string) --*

            The version number used by the cluster.
    """


_DescribeClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeClustersPaginatePaginationConfigTypeDef(
    _DescribeClustersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeClustersPaginateResponseClustersClusterNodesTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)


class DescribeClustersPaginateResponseClustersClusterNodesTypeDef(
    _DescribeClustersPaginateResponseClustersClusterNodesTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)


class DescribeClustersPaginateResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef(
    _DescribeClustersPaginateResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersClusterParameterGroupsTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            DescribeClustersPaginateResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersClusterParameterGroupsTypeDef(
    _DescribeClustersPaginateResponseClustersClusterParameterGroupsTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersClusterSecurityGroupsTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)


class DescribeClustersPaginateResponseClustersClusterSecurityGroupsTypeDef(
    _DescribeClustersPaginateResponseClustersClusterSecurityGroupsTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersClusterSnapshotCopyStatusTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersClusterSnapshotCopyStatusTypeDef(
    _DescribeClustersPaginateResponseClustersClusterSnapshotCopyStatusTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersDataTransferProgressTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersDataTransferProgressTypeDef(
    _DescribeClustersPaginateResponseClustersDataTransferProgressTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersDeferredMaintenanceWindowsTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersDeferredMaintenanceWindowsTypeDef(
    _DescribeClustersPaginateResponseClustersDeferredMaintenanceWindowsTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersElasticIpStatusTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)


class DescribeClustersPaginateResponseClustersElasticIpStatusTypeDef(
    _DescribeClustersPaginateResponseClustersElasticIpStatusTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersEndpointTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeClustersPaginateResponseClustersEndpointTypeDef(
    _DescribeClustersPaginateResponseClustersEndpointTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersHsmStatusTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)


class DescribeClustersPaginateResponseClustersHsmStatusTypeDef(
    _DescribeClustersPaginateResponseClustersHsmStatusTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersIamRolesTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)


class DescribeClustersPaginateResponseClustersIamRolesTypeDef(
    _DescribeClustersPaginateResponseClustersIamRolesTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersPendingModifiedValuesTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersPendingModifiedValuesTypeDef(
    _DescribeClustersPaginateResponseClustersPendingModifiedValuesTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersResizeInfoTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)


class DescribeClustersPaginateResponseClustersResizeInfoTypeDef(
    _DescribeClustersPaginateResponseClustersResizeInfoTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersRestoreStatusTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersRestoreStatusTypeDef(
    _DescribeClustersPaginateResponseClustersRestoreStatusTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersTagsTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class DescribeClustersPaginateResponseClustersTagsTypeDef(
    _DescribeClustersPaginateResponseClustersTagsTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersVpcSecurityGroupsTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class DescribeClustersPaginateResponseClustersVpcSecurityGroupsTypeDef(
    _DescribeClustersPaginateResponseClustersVpcSecurityGroupsTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": DescribeClustersPaginateResponseClustersEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            DescribeClustersPaginateResponseClustersClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[DescribeClustersPaginateResponseClustersVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            DescribeClustersPaginateResponseClustersClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": DescribeClustersPaginateResponseClustersPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": DescribeClustersPaginateResponseClustersRestoreStatusTypeDef,
        "DataTransferProgress": DescribeClustersPaginateResponseClustersDataTransferProgressTypeDef,
        "HsmStatus": DescribeClustersPaginateResponseClustersHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": DescribeClustersPaginateResponseClustersClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[DescribeClustersPaginateResponseClustersClusterNodesTypeDef],
        "ElasticIpStatus": DescribeClustersPaginateResponseClustersElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[DescribeClustersPaginateResponseClustersTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[DescribeClustersPaginateResponseClustersIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            DescribeClustersPaginateResponseClustersDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": DescribeClustersPaginateResponseClustersResizeInfoTypeDef,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersTypeDef(
    _DescribeClustersPaginateResponseClustersTypeDef
):
    """
    - *(dict) --*

      Describes a cluster.
      - **ClusterIdentifier** *(string) --*

        The unique identifier of the cluster.
    """


_DescribeClustersPaginateResponseTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseTypeDef",
    {"Clusters": List[DescribeClustersPaginateResponseClustersTypeDef], "NextToken": str},
    total=False,
)


class DescribeClustersPaginateResponseTypeDef(_DescribeClustersPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the output from the  DescribeClusters action.
      - **Clusters** *(list) --*

        A list of ``Cluster`` objects, where each object describes one cluster.
        - *(dict) --*

          Describes a cluster.
          - **ClusterIdentifier** *(string) --*

            The unique identifier of the cluster.
    """


_DescribeDefaultClusterParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDefaultClusterParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDefaultClusterParametersPaginatePaginationConfigTypeDef(
    _DescribeDefaultClusterParametersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDefaultClusterParametersPaginateResponseDefaultClusterParametersParametersTypeDef = TypedDict(
    "_DescribeDefaultClusterParametersPaginateResponseDefaultClusterParametersParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "ApplyType": Literal["static", "dynamic"],
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)


class DescribeDefaultClusterParametersPaginateResponseDefaultClusterParametersParametersTypeDef(
    _DescribeDefaultClusterParametersPaginateResponseDefaultClusterParametersParametersTypeDef
):
    pass


_DescribeDefaultClusterParametersPaginateResponseDefaultClusterParametersTypeDef = TypedDict(
    "_DescribeDefaultClusterParametersPaginateResponseDefaultClusterParametersTypeDef",
    {
        "ParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            DescribeDefaultClusterParametersPaginateResponseDefaultClusterParametersParametersTypeDef
        ],
    },
    total=False,
)


class DescribeDefaultClusterParametersPaginateResponseDefaultClusterParametersTypeDef(
    _DescribeDefaultClusterParametersPaginateResponseDefaultClusterParametersTypeDef
):
    """
    - **DefaultClusterParameters** *(dict) --*

      Describes the default cluster parameters for a parameter group family.
      - **ParameterGroupFamily** *(string) --*

        The name of the cluster parameter group family to which the engine default parameters apply.
    """


_DescribeDefaultClusterParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeDefaultClusterParametersPaginateResponseTypeDef",
    {
        "DefaultClusterParameters": DescribeDefaultClusterParametersPaginateResponseDefaultClusterParametersTypeDef,
        "NextToken": str,
    },
    total=False,
)


class DescribeDefaultClusterParametersPaginateResponseTypeDef(
    _DescribeDefaultClusterParametersPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **DefaultClusterParameters** *(dict) --*

        Describes the default cluster parameters for a parameter group family.
        - **ParameterGroupFamily** *(string) --*

          The name of the cluster parameter group family to which the engine default parameters
          apply.
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


_DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTagsTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTagsTypeDef(
    _DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTagsTypeDef
):
    pass


_DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": datetime,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Severity": str,
        "Enabled": bool,
        "Tags": List[DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTagsTypeDef],
    },
    total=False,
)


class DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef(
    _DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef
):
    """
    - *(dict) --*

      Describes event subscriptions.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the Amazon Redshift event notification
        subscription.
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

        A list of event subscriptions.
        - *(dict) --*

          Describes event subscriptions.
          - **CustomerAwsId** *(string) --*

            The AWS customer account associated with the Amazon Redshift event notification
            subscription.
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
            "cluster",
            "cluster-parameter-group",
            "cluster-security-group",
            "cluster-snapshot",
            "scheduled-action",
        ],
        "Message": str,
        "EventCategories": List[str],
        "Severity": str,
        "Date": datetime,
        "EventId": str,
    },
    total=False,
)


class DescribeEventsPaginateResponseEventsTypeDef(_DescribeEventsPaginateResponseEventsTypeDef):
    """
    - *(dict) --*

      Describes an event.
      - **SourceIdentifier** *(string) --*

        The identifier for the source of the event.
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

        A list of ``Event`` instances.
        - *(dict) --*

          Describes an event.
          - **SourceIdentifier** *(string) --*

            The identifier for the source of the event.
    """


_DescribeHsmClientCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeHsmClientCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeHsmClientCertificatesPaginatePaginationConfigTypeDef(
    _DescribeHsmClientCertificatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeHsmClientCertificatesPaginateResponseHsmClientCertificatesTagsTypeDef = TypedDict(
    "_DescribeHsmClientCertificatesPaginateResponseHsmClientCertificatesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeHsmClientCertificatesPaginateResponseHsmClientCertificatesTagsTypeDef(
    _DescribeHsmClientCertificatesPaginateResponseHsmClientCertificatesTagsTypeDef
):
    pass


_DescribeHsmClientCertificatesPaginateResponseHsmClientCertificatesTypeDef = TypedDict(
    "_DescribeHsmClientCertificatesPaginateResponseHsmClientCertificatesTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmClientCertificatePublicKey": str,
        "Tags": List[DescribeHsmClientCertificatesPaginateResponseHsmClientCertificatesTagsTypeDef],
    },
    total=False,
)


class DescribeHsmClientCertificatesPaginateResponseHsmClientCertificatesTypeDef(
    _DescribeHsmClientCertificatesPaginateResponseHsmClientCertificatesTypeDef
):
    """
    - *(dict) --*

      Returns information about an HSM client certificate. The certificate is stored in a secure
      Hardware Storage Module (HSM), and used by the Amazon Redshift cluster to encrypt data files.
      - **HsmClientCertificateIdentifier** *(string) --*

        The identifier of the HSM client certificate.
    """


_DescribeHsmClientCertificatesPaginateResponseTypeDef = TypedDict(
    "_DescribeHsmClientCertificatesPaginateResponseTypeDef",
    {
        "HsmClientCertificates": List[
            DescribeHsmClientCertificatesPaginateResponseHsmClientCertificatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeHsmClientCertificatesPaginateResponseTypeDef(
    _DescribeHsmClientCertificatesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **HsmClientCertificates** *(list) --*

        A list of the identifiers for one or more HSM client certificates used by Amazon Redshift
        clusters to store and retrieve database encryption keys in an HSM.
        - *(dict) --*

          Returns information about an HSM client certificate. The certificate is stored in a secure
          Hardware Storage Module (HSM), and used by the Amazon Redshift cluster to encrypt data
          files.
          - **HsmClientCertificateIdentifier** *(string) --*

            The identifier of the HSM client certificate.
    """


_DescribeHsmConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeHsmConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeHsmConfigurationsPaginatePaginationConfigTypeDef(
    _DescribeHsmConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeHsmConfigurationsPaginateResponseHsmConfigurationsTagsTypeDef = TypedDict(
    "_DescribeHsmConfigurationsPaginateResponseHsmConfigurationsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeHsmConfigurationsPaginateResponseHsmConfigurationsTagsTypeDef(
    _DescribeHsmConfigurationsPaginateResponseHsmConfigurationsTagsTypeDef
):
    pass


_DescribeHsmConfigurationsPaginateResponseHsmConfigurationsTypeDef = TypedDict(
    "_DescribeHsmConfigurationsPaginateResponseHsmConfigurationsTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "Description": str,
        "HsmIpAddress": str,
        "HsmPartitionName": str,
        "Tags": List[DescribeHsmConfigurationsPaginateResponseHsmConfigurationsTagsTypeDef],
    },
    total=False,
)


class DescribeHsmConfigurationsPaginateResponseHsmConfigurationsTypeDef(
    _DescribeHsmConfigurationsPaginateResponseHsmConfigurationsTypeDef
):
    """
    - *(dict) --*

      Returns information about an HSM configuration, which is an object that describes to Amazon
      Redshift clusters the information they require to connect to an HSM where they can store
      database encryption keys.
      - **HsmConfigurationIdentifier** *(string) --*

        The name of the Amazon Redshift HSM configuration.
    """


_DescribeHsmConfigurationsPaginateResponseTypeDef = TypedDict(
    "_DescribeHsmConfigurationsPaginateResponseTypeDef",
    {
        "HsmConfigurations": List[
            DescribeHsmConfigurationsPaginateResponseHsmConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeHsmConfigurationsPaginateResponseTypeDef(
    _DescribeHsmConfigurationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **HsmConfigurations** *(list) --*

        A list of ``HsmConfiguration`` objects.
        - *(dict) --*

          Returns information about an HSM configuration, which is an object that describes to
          Amazon Redshift clusters the information they require to connect to an HSM where they can
          store database encryption keys.
          - **HsmConfigurationIdentifier** *(string) --*

            The name of the Amazon Redshift HSM configuration.
    """


_DescribeNodeConfigurationOptionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeNodeConfigurationOptionsPaginateFiltersTypeDef",
    {
        "Name": Literal["NodeType", "NumberOfNodes", "EstimatedDiskUtilizationPercent", "Mode"],
        "Operator": Literal["eq", "lt", "gt", "le", "ge", "in", "between"],
        "Values": List[str],
    },
    total=False,
)


class DescribeNodeConfigurationOptionsPaginateFiltersTypeDef(
    _DescribeNodeConfigurationOptionsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A set of elements to filter the returned node configurations.
      - **Name** *(string) --*

        The name of the element to filter.
    """


_DescribeNodeConfigurationOptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeNodeConfigurationOptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeNodeConfigurationOptionsPaginatePaginationConfigTypeDef(
    _DescribeNodeConfigurationOptionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeNodeConfigurationOptionsPaginateResponseNodeConfigurationOptionListTypeDef = TypedDict(
    "_DescribeNodeConfigurationOptionsPaginateResponseNodeConfigurationOptionListTypeDef",
    {
        "NodeType": str,
        "NumberOfNodes": int,
        "EstimatedDiskUtilizationPercent": float,
        "Mode": Literal["standard", "high-performance"],
    },
    total=False,
)


class DescribeNodeConfigurationOptionsPaginateResponseNodeConfigurationOptionListTypeDef(
    _DescribeNodeConfigurationOptionsPaginateResponseNodeConfigurationOptionListTypeDef
):
    """
    - *(dict) --*

      A list of node configurations.
      - **NodeType** *(string) --*

        The node type, such as, "ds2.8xlarge".
    """


_DescribeNodeConfigurationOptionsPaginateResponseTypeDef = TypedDict(
    "_DescribeNodeConfigurationOptionsPaginateResponseTypeDef",
    {
        "NodeConfigurationOptionList": List[
            DescribeNodeConfigurationOptionsPaginateResponseNodeConfigurationOptionListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeNodeConfigurationOptionsPaginateResponseTypeDef(
    _DescribeNodeConfigurationOptionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **NodeConfigurationOptionList** *(list) --*

        A list of valid node configurations.
        - *(dict) --*

          A list of node configurations.
          - **NodeType** *(string) --*

            The node type, such as, "ds2.8xlarge".
    """


_DescribeOrderableClusterOptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeOrderableClusterOptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeOrderableClusterOptionsPaginatePaginationConfigTypeDef(
    _DescribeOrderableClusterOptionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef = TypedDict(
    "_DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef",
    {"Name": str},
    total=False,
)


class DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef(
    _DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef
):
    pass


_DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsAvailabilityZonesTypeDef = TypedDict(
    "_DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsAvailabilityZonesTypeDef",
    {
        "Name": str,
        "SupportedPlatforms": List[
            DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef
        ],
    },
    total=False,
)


class DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsAvailabilityZonesTypeDef(
    _DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsAvailabilityZonesTypeDef
):
    pass


_DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsTypeDef = TypedDict(
    "_DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsTypeDef",
    {
        "ClusterVersion": str,
        "ClusterType": str,
        "NodeType": str,
        "AvailabilityZones": List[
            DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsAvailabilityZonesTypeDef
        ],
    },
    total=False,
)


class DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsTypeDef(
    _DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsTypeDef
):
    """
    - *(dict) --*

      Describes an orderable cluster option.
      - **ClusterVersion** *(string) --*

        The version of the orderable cluster.
    """


_DescribeOrderableClusterOptionsPaginateResponseTypeDef = TypedDict(
    "_DescribeOrderableClusterOptionsPaginateResponseTypeDef",
    {
        "OrderableClusterOptions": List[
            DescribeOrderableClusterOptionsPaginateResponseOrderableClusterOptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeOrderableClusterOptionsPaginateResponseTypeDef(
    _DescribeOrderableClusterOptionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output from the  DescribeOrderableClusterOptions action.
      - **OrderableClusterOptions** *(list) --*

        An ``OrderableClusterOption`` structure containing information about orderable options for
        the cluster.
        - *(dict) --*

          Describes an orderable cluster option.
          - **ClusterVersion** *(string) --*

            The version of the orderable cluster.
    """


_DescribeReservedNodeOfferingsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReservedNodeOfferingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReservedNodeOfferingsPaginatePaginationConfigTypeDef(
    _DescribeReservedNodeOfferingsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReservedNodeOfferingsPaginateResponseReservedNodeOfferingsRecurringChargesTypeDef = TypedDict(
    "_DescribeReservedNodeOfferingsPaginateResponseReservedNodeOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class DescribeReservedNodeOfferingsPaginateResponseReservedNodeOfferingsRecurringChargesTypeDef(
    _DescribeReservedNodeOfferingsPaginateResponseReservedNodeOfferingsRecurringChargesTypeDef
):
    pass


_DescribeReservedNodeOfferingsPaginateResponseReservedNodeOfferingsTypeDef = TypedDict(
    "_DescribeReservedNodeOfferingsPaginateResponseReservedNodeOfferingsTypeDef",
    {
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "OfferingType": str,
        "RecurringCharges": List[
            DescribeReservedNodeOfferingsPaginateResponseReservedNodeOfferingsRecurringChargesTypeDef
        ],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)


class DescribeReservedNodeOfferingsPaginateResponseReservedNodeOfferingsTypeDef(
    _DescribeReservedNodeOfferingsPaginateResponseReservedNodeOfferingsTypeDef
):
    """
    - *(dict) --*

      Describes a reserved node offering.
      - **ReservedNodeOfferingId** *(string) --*

        The offering identifier.
    """


_DescribeReservedNodeOfferingsPaginateResponseTypeDef = TypedDict(
    "_DescribeReservedNodeOfferingsPaginateResponseTypeDef",
    {
        "ReservedNodeOfferings": List[
            DescribeReservedNodeOfferingsPaginateResponseReservedNodeOfferingsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReservedNodeOfferingsPaginateResponseTypeDef(
    _DescribeReservedNodeOfferingsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ReservedNodeOfferings** *(list) --*

        A list of ``ReservedNodeOffering`` objects.
        - *(dict) --*

          Describes a reserved node offering.
          - **ReservedNodeOfferingId** *(string) --*

            The offering identifier.
    """


_DescribeReservedNodesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReservedNodesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReservedNodesPaginatePaginationConfigTypeDef(
    _DescribeReservedNodesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReservedNodesPaginateResponseReservedNodesRecurringChargesTypeDef = TypedDict(
    "_DescribeReservedNodesPaginateResponseReservedNodesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class DescribeReservedNodesPaginateResponseReservedNodesRecurringChargesTypeDef(
    _DescribeReservedNodesPaginateResponseReservedNodesRecurringChargesTypeDef
):
    pass


_DescribeReservedNodesPaginateResponseReservedNodesTypeDef = TypedDict(
    "_DescribeReservedNodesPaginateResponseReservedNodesTypeDef",
    {
        "ReservedNodeId": str,
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "NodeCount": int,
        "State": str,
        "OfferingType": str,
        "RecurringCharges": List[
            DescribeReservedNodesPaginateResponseReservedNodesRecurringChargesTypeDef
        ],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)


class DescribeReservedNodesPaginateResponseReservedNodesTypeDef(
    _DescribeReservedNodesPaginateResponseReservedNodesTypeDef
):
    """
    - *(dict) --*

      Describes a reserved node. You can call the  DescribeReservedNodeOfferings API to obtain the
      available reserved node offerings.
      - **ReservedNodeId** *(string) --*

        The unique identifier for the reservation.
    """


_DescribeReservedNodesPaginateResponseTypeDef = TypedDict(
    "_DescribeReservedNodesPaginateResponseTypeDef",
    {
        "ReservedNodes": List[DescribeReservedNodesPaginateResponseReservedNodesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeReservedNodesPaginateResponseTypeDef(_DescribeReservedNodesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ReservedNodes** *(list) --*

        The list of ``ReservedNode`` objects.
        - *(dict) --*

          Describes a reserved node. You can call the  DescribeReservedNodeOfferings API to obtain
          the available reserved node offerings.
          - **ReservedNodeId** *(string) --*

            The unique identifier for the reservation.
    """


_RequiredDescribeScheduledActionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeScheduledActionsPaginateFiltersTypeDef",
    {"Name": Literal["cluster-identifier", "iam-role"]},
)
_OptionalDescribeScheduledActionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeScheduledActionsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeScheduledActionsPaginateFiltersTypeDef(
    _RequiredDescribeScheduledActionsPaginateFiltersTypeDef,
    _OptionalDescribeScheduledActionsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      A set of elements to filter the returned scheduled actions.
      - **Name** *(string) --***[REQUIRED]**

        The type of element to filter.
    """


_DescribeScheduledActionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScheduledActionsPaginatePaginationConfigTypeDef(
    _DescribeScheduledActionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeScheduledActionsPaginateResponseScheduledActionsTargetActionResizeClusterTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseScheduledActionsTargetActionResizeClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "ClusterType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "Classic": bool,
    },
    total=False,
)


class DescribeScheduledActionsPaginateResponseScheduledActionsTargetActionResizeClusterTypeDef(
    _DescribeScheduledActionsPaginateResponseScheduledActionsTargetActionResizeClusterTypeDef
):
    pass


_DescribeScheduledActionsPaginateResponseScheduledActionsTargetActionTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseScheduledActionsTargetActionTypeDef",
    {
        "ResizeCluster": DescribeScheduledActionsPaginateResponseScheduledActionsTargetActionResizeClusterTypeDef
    },
    total=False,
)


class DescribeScheduledActionsPaginateResponseScheduledActionsTargetActionTypeDef(
    _DescribeScheduledActionsPaginateResponseScheduledActionsTargetActionTypeDef
):
    pass


_DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": DescribeScheduledActionsPaginateResponseScheduledActionsTargetActionTypeDef,
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "State": Literal["ACTIVE", "DISABLED"],
        "NextInvocations": List[datetime],
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)


class DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef(
    _DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef
):
    """
    - *(dict) --*

      Describes a scheduled action. You can use a scheduled action to trigger some Amazon Redshift
      API operations on a schedule. For information about which API operations can be scheduled, see
      ScheduledActionType .
      - **ScheduledActionName** *(string) --*

        The name of the scheduled action.
    """


_DescribeScheduledActionsPaginateResponseTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseTypeDef",
    {
        "ScheduledActions": List[DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeScheduledActionsPaginateResponseTypeDef(
    _DescribeScheduledActionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ScheduledActions** *(list) --*

        List of retrieved scheduled actions.
        - *(dict) --*

          Describes a scheduled action. You can use a scheduled action to trigger some Amazon
          Redshift API operations on a schedule. For information about which API operations can be
          scheduled, see  ScheduledActionType .
          - **ScheduledActionName** *(string) --*

            The name of the scheduled action.
    """


_DescribeSnapshotCopyGrantsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSnapshotCopyGrantsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSnapshotCopyGrantsPaginatePaginationConfigTypeDef(
    _DescribeSnapshotCopyGrantsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeSnapshotCopyGrantsPaginateResponseSnapshotCopyGrantsTagsTypeDef = TypedDict(
    "_DescribeSnapshotCopyGrantsPaginateResponseSnapshotCopyGrantsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeSnapshotCopyGrantsPaginateResponseSnapshotCopyGrantsTagsTypeDef(
    _DescribeSnapshotCopyGrantsPaginateResponseSnapshotCopyGrantsTagsTypeDef
):
    pass


_DescribeSnapshotCopyGrantsPaginateResponseSnapshotCopyGrantsTypeDef = TypedDict(
    "_DescribeSnapshotCopyGrantsPaginateResponseSnapshotCopyGrantsTypeDef",
    {
        "SnapshotCopyGrantName": str,
        "KmsKeyId": str,
        "Tags": List[DescribeSnapshotCopyGrantsPaginateResponseSnapshotCopyGrantsTagsTypeDef],
    },
    total=False,
)


class DescribeSnapshotCopyGrantsPaginateResponseSnapshotCopyGrantsTypeDef(
    _DescribeSnapshotCopyGrantsPaginateResponseSnapshotCopyGrantsTypeDef
):
    """
    - *(dict) --*

      The snapshot copy grant that grants Amazon Redshift permission to encrypt copied snapshots
      with the specified customer master key (CMK) from AWS KMS in the destination region.
      For more information about managing snapshot copy grants, go to `Amazon Redshift Database
      Encryption
      <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html>`__ in the
      *Amazon Redshift Cluster Management Guide* .
      - **SnapshotCopyGrantName** *(string) --*

        The name of the snapshot copy grant.
    """


_DescribeSnapshotCopyGrantsPaginateResponseTypeDef = TypedDict(
    "_DescribeSnapshotCopyGrantsPaginateResponseTypeDef",
    {
        "SnapshotCopyGrants": List[
            DescribeSnapshotCopyGrantsPaginateResponseSnapshotCopyGrantsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeSnapshotCopyGrantsPaginateResponseTypeDef(
    _DescribeSnapshotCopyGrantsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **SnapshotCopyGrants** *(list) --*

        The list of ``SnapshotCopyGrant`` objects.
        - *(dict) --*

          The snapshot copy grant that grants Amazon Redshift permission to encrypt copied snapshots
          with the specified customer master key (CMK) from AWS KMS in the destination region.
          For more information about managing snapshot copy grants, go to `Amazon Redshift Database
          Encryption
          <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html>`__ in
          the *Amazon Redshift Cluster Management Guide* .
          - **SnapshotCopyGrantName** *(string) --*

            The name of the snapshot copy grant.
    """


_DescribeSnapshotSchedulesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSnapshotSchedulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSnapshotSchedulesPaginatePaginationConfigTypeDef(
    _DescribeSnapshotSchedulesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesAssociatedClustersTypeDef = TypedDict(
    "_DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesAssociatedClustersTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleAssociationState": Literal["MODIFYING", "ACTIVE", "FAILED"],
    },
    total=False,
)


class DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesAssociatedClustersTypeDef(
    _DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesAssociatedClustersTypeDef
):
    pass


_DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesTagsTypeDef = TypedDict(
    "_DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesTagsTypeDef(
    _DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesTagsTypeDef
):
    pass


_DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesTypeDef = TypedDict(
    "_DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List[DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesTagsTypeDef],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List[
            DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesAssociatedClustersTypeDef
        ],
    },
    total=False,
)


class DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesTypeDef(
    _DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesTypeDef
):
    """
    - *(dict) --*

      Describes a snapshot schedule. You can set a regular interval for creating snapshots of a
      cluster. You can also schedule snapshots for specific dates.
      - **ScheduleDefinitions** *(list) --*

        A list of ScheduleDefinitions.
        - *(string) --*
    """


_DescribeSnapshotSchedulesPaginateResponseTypeDef = TypedDict(
    "_DescribeSnapshotSchedulesPaginateResponseTypeDef",
    {
        "SnapshotSchedules": List[
            DescribeSnapshotSchedulesPaginateResponseSnapshotSchedulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeSnapshotSchedulesPaginateResponseTypeDef(
    _DescribeSnapshotSchedulesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **SnapshotSchedules** *(list) --*

        A list of SnapshotSchedules.
        - *(dict) --*

          Describes a snapshot schedule. You can set a regular interval for creating snapshots of a
          cluster. You can also schedule snapshots for specific dates.
          - **ScheduleDefinitions** *(list) --*

            A list of ScheduleDefinitions.
            - *(string) --*
    """


_DescribeTableRestoreStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTableRestoreStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTableRestoreStatusPaginatePaginationConfigTypeDef(
    _DescribeTableRestoreStatusPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeTableRestoreStatusPaginateResponseTableRestoreStatusDetailsTypeDef = TypedDict(
    "_DescribeTableRestoreStatusPaginateResponseTableRestoreStatusDetailsTypeDef",
    {
        "TableRestoreRequestId": str,
        "Status": Literal["PENDING", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED"],
        "Message": str,
        "RequestTime": datetime,
        "ProgressInMegaBytes": int,
        "TotalDataInMegaBytes": int,
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SourceDatabaseName": str,
        "SourceSchemaName": str,
        "SourceTableName": str,
        "TargetDatabaseName": str,
        "TargetSchemaName": str,
        "NewTableName": str,
    },
    total=False,
)


class DescribeTableRestoreStatusPaginateResponseTableRestoreStatusDetailsTypeDef(
    _DescribeTableRestoreStatusPaginateResponseTableRestoreStatusDetailsTypeDef
):
    """
    - *(dict) --*

      Describes the status of a  RestoreTableFromClusterSnapshot operation.
      - **TableRestoreRequestId** *(string) --*

        The unique identifier for the table restore request.
    """


_DescribeTableRestoreStatusPaginateResponseTypeDef = TypedDict(
    "_DescribeTableRestoreStatusPaginateResponseTypeDef",
    {
        "TableRestoreStatusDetails": List[
            DescribeTableRestoreStatusPaginateResponseTableRestoreStatusDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeTableRestoreStatusPaginateResponseTypeDef(
    _DescribeTableRestoreStatusPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **TableRestoreStatusDetails** *(list) --*

        A list of status details for one or more table restore requests.
        - *(dict) --*

          Describes the status of a  RestoreTableFromClusterSnapshot operation.
          - **TableRestoreRequestId** *(string) --*

            The unique identifier for the table restore request.
    """


_DescribeTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTagsPaginatePaginationConfigTypeDef(_DescribeTagsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeTagsPaginateResponseTaggedResourcesTagTypeDef = TypedDict(
    "_DescribeTagsPaginateResponseTaggedResourcesTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeTagsPaginateResponseTaggedResourcesTagTypeDef(
    _DescribeTagsPaginateResponseTaggedResourcesTagTypeDef
):
    """
    - **Tag** *(dict) --*

      The tag for the resource.
      - **Key** *(string) --*

        The key, or name, for the resource tag.
    """


_DescribeTagsPaginateResponseTaggedResourcesTypeDef = TypedDict(
    "_DescribeTagsPaginateResponseTaggedResourcesTypeDef",
    {
        "Tag": DescribeTagsPaginateResponseTaggedResourcesTagTypeDef,
        "ResourceName": str,
        "ResourceType": str,
    },
    total=False,
)


class DescribeTagsPaginateResponseTaggedResourcesTypeDef(
    _DescribeTagsPaginateResponseTaggedResourcesTypeDef
):
    """
    - *(dict) --*

      A tag and its associated resource.
      - **Tag** *(dict) --*

        The tag for the resource.
        - **Key** *(string) --*

          The key, or name, for the resource tag.
    """


_DescribeTagsPaginateResponseTypeDef = TypedDict(
    "_DescribeTagsPaginateResponseTypeDef",
    {"TaggedResources": List[DescribeTagsPaginateResponseTaggedResourcesTypeDef], "NextToken": str},
    total=False,
)


class DescribeTagsPaginateResponseTypeDef(_DescribeTagsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TaggedResources** *(list) --*

        A list of tags with their associated resources.
        - *(dict) --*

          A tag and its associated resource.
          - **Tag** *(dict) --*

            The tag for the resource.
            - **Key** *(string) --*

              The key, or name, for the resource tag.
    """


_GetReservedNodeExchangeOfferingsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetReservedNodeExchangeOfferingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetReservedNodeExchangeOfferingsPaginatePaginationConfigTypeDef(
    _GetReservedNodeExchangeOfferingsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetReservedNodeExchangeOfferingsPaginateResponseReservedNodeOfferingsRecurringChargesTypeDef = TypedDict(
    "_GetReservedNodeExchangeOfferingsPaginateResponseReservedNodeOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class GetReservedNodeExchangeOfferingsPaginateResponseReservedNodeOfferingsRecurringChargesTypeDef(
    _GetReservedNodeExchangeOfferingsPaginateResponseReservedNodeOfferingsRecurringChargesTypeDef
):
    pass


_GetReservedNodeExchangeOfferingsPaginateResponseReservedNodeOfferingsTypeDef = TypedDict(
    "_GetReservedNodeExchangeOfferingsPaginateResponseReservedNodeOfferingsTypeDef",
    {
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "OfferingType": str,
        "RecurringCharges": List[
            GetReservedNodeExchangeOfferingsPaginateResponseReservedNodeOfferingsRecurringChargesTypeDef
        ],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)


class GetReservedNodeExchangeOfferingsPaginateResponseReservedNodeOfferingsTypeDef(
    _GetReservedNodeExchangeOfferingsPaginateResponseReservedNodeOfferingsTypeDef
):
    """
    - *(dict) --*

      Describes a reserved node offering.
      - **ReservedNodeOfferingId** *(string) --*

        The offering identifier.
    """


_GetReservedNodeExchangeOfferingsPaginateResponseTypeDef = TypedDict(
    "_GetReservedNodeExchangeOfferingsPaginateResponseTypeDef",
    {
        "ReservedNodeOfferings": List[
            GetReservedNodeExchangeOfferingsPaginateResponseReservedNodeOfferingsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetReservedNodeExchangeOfferingsPaginateResponseTypeDef(
    _GetReservedNodeExchangeOfferingsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ReservedNodeOfferings** *(list) --*

        Returns an array of  ReservedNodeOffering objects.
        - *(dict) --*

          Describes a reserved node offering.
          - **ReservedNodeOfferingId** *(string) --*

            The offering identifier.
    """


_RequiredSnapshotAvailableWaitSortingEntitiesTypeDef = TypedDict(
    "_RequiredSnapshotAvailableWaitSortingEntitiesTypeDef",
    {"Attribute": Literal["SOURCE_TYPE", "TOTAL_SIZE", "CREATE_TIME"]},
)
_OptionalSnapshotAvailableWaitSortingEntitiesTypeDef = TypedDict(
    "_OptionalSnapshotAvailableWaitSortingEntitiesTypeDef",
    {"SortOrder": Literal["ASC", "DESC"]},
    total=False,
)


class SnapshotAvailableWaitSortingEntitiesTypeDef(
    _RequiredSnapshotAvailableWaitSortingEntitiesTypeDef,
    _OptionalSnapshotAvailableWaitSortingEntitiesTypeDef,
):
    """
    - *(dict) --*

      Describes a sorting entity
      - **Attribute** *(string) --***[REQUIRED]**

        The category for sorting the snapshots.
    """


_SnapshotAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_SnapshotAvailableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class SnapshotAvailableWaitWaiterConfigTypeDef(_SnapshotAvailableWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """
