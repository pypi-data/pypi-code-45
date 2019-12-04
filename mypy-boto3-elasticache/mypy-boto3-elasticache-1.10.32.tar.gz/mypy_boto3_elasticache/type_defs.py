"Main interface for elasticache service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "CacheClusterAvailableWaitWaiterConfigTypeDef",
    "CacheClusterDeletedWaitWaiterConfigTypeDef",
    "ClientAddTagsToResourceResponseTagListTypeDef",
    "ClientAddTagsToResourceResponseTypeDef",
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
    "ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef",
    "ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef",
    "ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    "ClientBatchApplyUpdateActionResponseTypeDef",
    "ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef",
    "ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    "ClientBatchStopUpdateActionResponseTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupTypeDef",
    "ClientCompleteMigrationResponseTypeDef",
    "ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    "ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef",
    "ClientCopySnapshotResponseSnapshotTypeDef",
    "ClientCopySnapshotResponseTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterTypeDef",
    "ClientCreateCacheClusterResponseTypeDef",
    "ClientCreateCacheClusterTagsTypeDef",
    "ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef",
    "ClientCreateCacheParameterGroupResponseTypeDef",
    "ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef",
    "ClientCreateCacheSecurityGroupResponseTypeDef",
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    "ClientCreateCacheSubnetGroupResponseTypeDef",
    "ClientCreateReplicationGroupNodeGroupConfigurationTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupTypeDef",
    "ClientCreateReplicationGroupResponseTypeDef",
    "ClientCreateReplicationGroupTagsTypeDef",
    "ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    "ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef",
    "ClientCreateSnapshotResponseSnapshotTypeDef",
    "ClientCreateSnapshotResponseTypeDef",
    "ClientDecreaseReplicaCountReplicaConfigurationTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupTypeDef",
    "ClientDecreaseReplicaCountResponseTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterTypeDef",
    "ClientDeleteCacheClusterResponseTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupTypeDef",
    "ClientDeleteReplicationGroupResponseTypeDef",
    "ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    "ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef",
    "ClientDeleteSnapshotResponseSnapshotTypeDef",
    "ClientDeleteSnapshotResponseTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersTypeDef",
    "ClientDescribeCacheClustersResponseTypeDef",
    "ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef",
    "ClientDescribeCacheEngineVersionsResponseTypeDef",
    "ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef",
    "ClientDescribeCacheParameterGroupsResponseTypeDef",
    "ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    "ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef",
    "ClientDescribeCacheParametersResponseParametersTypeDef",
    "ClientDescribeCacheParametersResponseTypeDef",
    "ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef",
    "ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef",
    "ClientDescribeCacheSecurityGroupsResponseTypeDef",
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef",
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef",
    "ClientDescribeCacheSubnetGroupsResponseTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef",
    "ClientDescribeEngineDefaultParametersResponseTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef",
    "ClientDescribeReplicationGroupsResponseTypeDef",
    "ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef",
    "ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef",
    "ClientDescribeReservedCacheNodesOfferingsResponseTypeDef",
    "ClientDescribeReservedCacheNodesResponseReservedCacheNodesRecurringChargesTypeDef",
    "ClientDescribeReservedCacheNodesResponseReservedCacheNodesTypeDef",
    "ClientDescribeReservedCacheNodesResponseTypeDef",
    "ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef",
    "ClientDescribeServiceUpdatesResponseTypeDef",
    "ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef",
    "ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef",
    "ClientDescribeSnapshotsResponseSnapshotsTypeDef",
    "ClientDescribeSnapshotsResponseTypeDef",
    "ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef",
    "ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef",
    "ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef",
    "ClientDescribeUpdateActionsResponseUpdateActionsTypeDef",
    "ClientDescribeUpdateActionsResponseTypeDef",
    "ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef",
    "ClientIncreaseReplicaCountReplicaConfigurationTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupTypeDef",
    "ClientIncreaseReplicaCountResponseTypeDef",
    "ClientListAllowedNodeTypeModificationsResponseTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterTypeDef",
    "ClientModifyCacheClusterResponseTypeDef",
    "ClientModifyCacheParameterGroupParameterNameValuesTypeDef",
    "ClientModifyCacheParameterGroupResponseTypeDef",
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    "ClientModifyCacheSubnetGroupResponseTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupTypeDef",
    "ClientModifyReplicationGroupResponseTypeDef",
    "ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseTypeDef",
    "ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef",
    "ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef",
    "ClientPurchaseReservedCacheNodesOfferingResponseTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterTypeDef",
    "ClientRebootCacheClusterResponseTypeDef",
    "ClientRemoveTagsFromResourceResponseTagListTypeDef",
    "ClientRemoveTagsFromResourceResponseTypeDef",
    "ClientResetCacheParameterGroupParameterNameValuesTypeDef",
    "ClientResetCacheParameterGroupResponseTypeDef",
    "ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
    "ClientRevokeCacheSecurityGroupIngressResponseTypeDef",
    "ClientStartMigrationCustomerNodeEndpointListTypeDef",
    "ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef",
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientStartMigrationResponseReplicationGroupTypeDef",
    "ClientStartMigrationResponseTypeDef",
    "ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef",
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientTestFailoverResponseReplicationGroupTypeDef",
    "ClientTestFailoverResponseTypeDef",
    "DescribeCacheClustersPaginatePaginationConfigTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersTypeDef",
    "DescribeCacheClustersPaginateResponseTypeDef",
    "DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef",
    "DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef",
    "DescribeCacheEngineVersionsPaginateResponseTypeDef",
    "DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef",
    "DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef",
    "DescribeCacheParameterGroupsPaginateResponseTypeDef",
    "DescribeCacheParametersPaginatePaginationConfigTypeDef",
    "DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    "DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef",
    "DescribeCacheParametersPaginateResponseParametersTypeDef",
    "DescribeCacheParametersPaginateResponseTypeDef",
    "DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef",
    "DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef",
    "DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef",
    "DescribeCacheSecurityGroupsPaginateResponseTypeDef",
    "DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef",
    "DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef",
    "DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef",
    "DescribeCacheSubnetGroupsPaginateResponseTypeDef",
    "DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "DescribeReplicationGroupsPaginatePaginationConfigTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef",
    "DescribeReplicationGroupsPaginateResponseTypeDef",
    "DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef",
    "DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef",
    "DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef",
    "DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef",
    "DescribeReservedCacheNodesPaginatePaginationConfigTypeDef",
    "DescribeReservedCacheNodesPaginateResponseReservedCacheNodesRecurringChargesTypeDef",
    "DescribeReservedCacheNodesPaginateResponseReservedCacheNodesTypeDef",
    "DescribeReservedCacheNodesPaginateResponseTypeDef",
    "DescribeServiceUpdatesPaginatePaginationConfigTypeDef",
    "DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef",
    "DescribeServiceUpdatesPaginateResponseTypeDef",
    "DescribeSnapshotsPaginatePaginationConfigTypeDef",
    "DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef",
    "DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef",
    "DescribeSnapshotsPaginateResponseSnapshotsTypeDef",
    "DescribeSnapshotsPaginateResponseTypeDef",
    "DescribeUpdateActionsPaginatePaginationConfigTypeDef",
    "DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef",
    "DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef",
    "DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef",
    "DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef",
    "DescribeUpdateActionsPaginateResponseTypeDef",
    "DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef",
    "ReplicationGroupAvailableWaitWaiterConfigTypeDef",
    "ReplicationGroupDeletedWaitWaiterConfigTypeDef",
)


_CacheClusterAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_CacheClusterAvailableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class CacheClusterAvailableWaitWaiterConfigTypeDef(_CacheClusterAvailableWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_CacheClusterDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_CacheClusterDeletedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class CacheClusterDeletedWaitWaiterConfigTypeDef(_CacheClusterDeletedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_ClientAddTagsToResourceResponseTagListTypeDef = TypedDict(
    "_ClientAddTagsToResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsToResourceResponseTagListTypeDef(_ClientAddTagsToResourceResponseTagListTypeDef):
    """
    - *(dict) --*

      A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags
      are composed of a Key/Value pair. A tag with a null Value is permitted.
      - **Key** *(string) --*

        The key for the tag. May not be null.
    """


_ClientAddTagsToResourceResponseTypeDef = TypedDict(
    "_ClientAddTagsToResourceResponseTypeDef",
    {"TagList": List[ClientAddTagsToResourceResponseTagListTypeDef]},
    total=False,
)


class ClientAddTagsToResourceResponseTypeDef(_ClientAddTagsToResourceResponseTypeDef):
    """
    - *(dict) --*

      Represents the output from the ``AddTagsToResource`` , ``ListTagsForResource`` , and
      ``RemoveTagsFromResource`` operations.
      - **TagList** *(list) --*

        A list of cost allocation tags as key-value pairs.
        - *(dict) --*

          A cost allocation Tag that can be added to an ElastiCache cluster or replication group.
          Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
          - **Key** *(string) --*

            The key for the tag. May not be null.
    """


_ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsToResourceTagsTypeDef(_ClientAddTagsToResourceTagsTypeDef):
    """
    - *(dict) --*

      A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags
      are composed of a Key/Value pair. A tag with a null Value is permitted.
      - **Key** *(string) --*

        The key for the tag. May not be null.
    """


_ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)


class ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef(
    _ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
):
    pass


_ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef = TypedDict(
    "_ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)


class ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef(
    _ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef
):
    """
    - **CacheSecurityGroup** *(dict) --*

      Represents the output of one of the following operations:
      * ``AuthorizeCacheSecurityGroupIngress``
      * ``CreateCacheSecurityGroup``
      * ``RevokeCacheSecurityGroupIngress``
      - **OwnerId** *(string) --*

        The AWS account ID of the cache security group owner.
    """


_ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef = TypedDict(
    "_ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef",
    {
        "CacheSecurityGroup": ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef
    },
    total=False,
)


class ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef(
    _ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef
):
    """
    - *(dict) --*

      - **CacheSecurityGroup** *(dict) --*

        Represents the output of one of the following operations:
        * ``AuthorizeCacheSecurityGroupIngress``
        * ``CreateCacheSecurityGroup``
        * ``RevokeCacheSecurityGroupIngress``
        - **OwnerId** *(string) --*

          The AWS account ID of the cache security group owner.
    """


_ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef = TypedDict(
    "_ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "UpdateActionStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
    },
    total=False,
)


class ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef(
    _ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef
):
    """
    - *(dict) --*

      Update action that has been processed for the corresponding apply/stop request
      - **ReplicationGroupId** *(string) --*

        The ID of the replication group
    """


_ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef = TypedDict(
    "_ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ErrorType": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef(
    _ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef
):
    pass


_ClientBatchApplyUpdateActionResponseTypeDef = TypedDict(
    "_ClientBatchApplyUpdateActionResponseTypeDef",
    {
        "ProcessedUpdateActions": List[
            ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef
        ],
        "UnprocessedUpdateActions": List[
            ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef
        ],
    },
    total=False,
)


class ClientBatchApplyUpdateActionResponseTypeDef(_ClientBatchApplyUpdateActionResponseTypeDef):
    """
    - *(dict) --*

      - **ProcessedUpdateActions** *(list) --*

        Update actions that have been processed successfully
        - *(dict) --*

          Update action that has been processed for the corresponding apply/stop request
          - **ReplicationGroupId** *(string) --*

            The ID of the replication group
    """


_ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef = TypedDict(
    "_ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "UpdateActionStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
    },
    total=False,
)


class ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef(
    _ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef
):
    """
    - *(dict) --*

      Update action that has been processed for the corresponding apply/stop request
      - **ReplicationGroupId** *(string) --*

        The ID of the replication group
    """


_ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef = TypedDict(
    "_ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ErrorType": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef(
    _ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef
):
    pass


_ClientBatchStopUpdateActionResponseTypeDef = TypedDict(
    "_ClientBatchStopUpdateActionResponseTypeDef",
    {
        "ProcessedUpdateActions": List[
            ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef
        ],
        "UnprocessedUpdateActions": List[
            ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef
        ],
    },
    total=False,
)


class ClientBatchStopUpdateActionResponseTypeDef(_ClientBatchStopUpdateActionResponseTypeDef):
    """
    - *(dict) --*

      - **ProcessedUpdateActions** *(list) --*

        Update actions that have been processed successfully
        - *(dict) --*

          Update action that has been processed for the corresponding apply/stop request
          - **ReplicationGroupId** *(string) --*

            The ID of the replication group
    """


_ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef
):
    pass


_ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    pass


_ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    pass


_ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    pass


_ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    pass


_ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef
):
    pass


_ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    pass


_ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    pass


_ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef
):
    pass


_ClientCompleteMigrationResponseReplicationGroupTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupTypeDef
):
    """
    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.
      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.
    """


_ClientCompleteMigrationResponseTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseTypeDef",
    {"ReplicationGroup": ClientCompleteMigrationResponseReplicationGroupTypeDef},
    total=False,
)


class ClientCompleteMigrationResponseTypeDef(_ClientCompleteMigrationResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationGroup** *(dict) --*

        Contains all of the attributes of a specific Redis replication group.
        - **ReplicationGroupId** *(string) --*

          The identifier for the replication group.
    """


_ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "_ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)


class ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef(
    _ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef
):
    pass


_ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef = TypedDict(
    "_ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)


class ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef(
    _ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef
):
    pass


_ClientCopySnapshotResponseSnapshotTypeDef = TypedDict(
    "_ClientCopySnapshotResponseSnapshotTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "NodeSnapshots": List[ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)


class ClientCopySnapshotResponseSnapshotTypeDef(_ClientCopySnapshotResponseSnapshotTypeDef):
    """
    - **Snapshot** *(dict) --*

      Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.
      - **SnapshotName** *(string) --*

        The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
        manual snapshot, this is the user-provided name.
    """


_ClientCopySnapshotResponseTypeDef = TypedDict(
    "_ClientCopySnapshotResponseTypeDef",
    {"Snapshot": ClientCopySnapshotResponseSnapshotTypeDef},
    total=False,
)


class ClientCopySnapshotResponseTypeDef(_ClientCopySnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **Snapshot** *(dict) --*

        Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.
        - **SnapshotName** *(string) --*

          The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
          manual snapshot, this is the user-provided name.
    """


_ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef
):
    pass


_ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef
):
    pass


_ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef
):
    pass


_ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
):
    pass


_ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef
):
    pass


_ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef
):
    pass


_ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef
):
    pass


_ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef
):
    pass


_ClientCreateCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterTypeDef
):
    """
    - **CacheCluster** *(dict) --*

      Contains all of the attributes of a specific cluster.
      - **CacheClusterId** *(string) --*

        The user-supplied identifier of the cluster. This identifier is a unique key that identifies
        a cluster.
    """


_ClientCreateCacheClusterResponseTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseTypeDef",
    {"CacheCluster": ClientCreateCacheClusterResponseCacheClusterTypeDef},
    total=False,
)


class ClientCreateCacheClusterResponseTypeDef(_ClientCreateCacheClusterResponseTypeDef):
    """
    - *(dict) --*

      - **CacheCluster** *(dict) --*

        Contains all of the attributes of a specific cluster.
        - **CacheClusterId** *(string) --*

          The user-supplied identifier of the cluster. This identifier is a unique key that
          identifies a cluster.
    """


_ClientCreateCacheClusterTagsTypeDef = TypedDict(
    "_ClientCreateCacheClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateCacheClusterTagsTypeDef(_ClientCreateCacheClusterTagsTypeDef):
    """
    - *(dict) --*

      A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags
      are composed of a Key/Value pair. A tag with a null Value is permitted.
      - **Key** *(string) --*

        The key for the tag. May not be null.
    """


_ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef = TypedDict(
    "_ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef",
    {"CacheParameterGroupName": str, "CacheParameterGroupFamily": str, "Description": str},
    total=False,
)


class ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef(
    _ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef
):
    """
    - **CacheParameterGroup** *(dict) --*

      Represents the output of a ``CreateCacheParameterGroup`` operation.
      - **CacheParameterGroupName** *(string) --*

        The name of the cache parameter group.
    """


_ClientCreateCacheParameterGroupResponseTypeDef = TypedDict(
    "_ClientCreateCacheParameterGroupResponseTypeDef",
    {"CacheParameterGroup": ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef},
    total=False,
)


class ClientCreateCacheParameterGroupResponseTypeDef(
    _ClientCreateCacheParameterGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **CacheParameterGroup** *(dict) --*

        Represents the output of a ``CreateCacheParameterGroup`` operation.
        - **CacheParameterGroupName** *(string) --*

          The name of the cache parameter group.
    """


_ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)


class ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef(
    _ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
):
    pass


_ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef = TypedDict(
    "_ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)


class ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef(
    _ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef
):
    """
    - **CacheSecurityGroup** *(dict) --*

      Represents the output of one of the following operations:
      * ``AuthorizeCacheSecurityGroupIngress``
      * ``CreateCacheSecurityGroup``
      * ``RevokeCacheSecurityGroupIngress``
      - **OwnerId** *(string) --*

        The AWS account ID of the cache security group owner.
    """


_ClientCreateCacheSecurityGroupResponseTypeDef = TypedDict(
    "_ClientCreateCacheSecurityGroupResponseTypeDef",
    {"CacheSecurityGroup": ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef},
    total=False,
)


class ClientCreateCacheSecurityGroupResponseTypeDef(_ClientCreateCacheSecurityGroupResponseTypeDef):
    """
    - *(dict) --*

      - **CacheSecurityGroup** *(dict) --*

        Represents the output of one of the following operations:
        * ``AuthorizeCacheSecurityGroupIngress``
        * ``CreateCacheSecurityGroup``
        * ``RevokeCacheSecurityGroupIngress``
        - **OwnerId** *(string) --*

          The AWS account ID of the cache security group owner.
    """


_ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)


class ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef(
    _ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef
):
    pass


_ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef = TypedDict(
    "_ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef],
    },
    total=False,
)


class ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef(
    _ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef
):
    """
    - **CacheSubnetGroup** *(dict) --*

      Represents the output of one of the following operations:
      * ``CreateCacheSubnetGroup``
      * ``ModifyCacheSubnetGroup``
      - **CacheSubnetGroupName** *(string) --*

        The name of the cache subnet group.
    """


_ClientCreateCacheSubnetGroupResponseTypeDef = TypedDict(
    "_ClientCreateCacheSubnetGroupResponseTypeDef",
    {"CacheSubnetGroup": ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef},
    total=False,
)


class ClientCreateCacheSubnetGroupResponseTypeDef(_ClientCreateCacheSubnetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **CacheSubnetGroup** *(dict) --*

        Represents the output of one of the following operations:
        * ``CreateCacheSubnetGroup``
        * ``ModifyCacheSubnetGroup``
        - **CacheSubnetGroupName** *(string) --*

          The name of the cache subnet group.
    """


_ClientCreateReplicationGroupNodeGroupConfigurationTypeDef = TypedDict(
    "_ClientCreateReplicationGroupNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)


class ClientCreateReplicationGroupNodeGroupConfigurationTypeDef(
    _ClientCreateReplicationGroupNodeGroupConfigurationTypeDef
):
    """
    - *(dict) --*

      Node group (shard) configuration options. Each node group (shard) configuration has the
      following: ``Slots`` , ``PrimaryAvailabilityZone`` , ``ReplicaAvailabilityZones`` ,
      ``ReplicaCount`` .
      - **NodeGroupId** *(string) --*

        Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node
        group these configuration values apply to.
    """


_ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef
):
    pass


_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    pass


_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    pass


_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    pass


_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    pass


_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef
):
    pass


_ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    pass


_ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    pass


_ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef
):
    pass


_ClientCreateReplicationGroupResponseReplicationGroupTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupTypeDef
):
    """
    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.
      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.
    """


_ClientCreateReplicationGroupResponseTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseTypeDef",
    {"ReplicationGroup": ClientCreateReplicationGroupResponseReplicationGroupTypeDef},
    total=False,
)


class ClientCreateReplicationGroupResponseTypeDef(_ClientCreateReplicationGroupResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationGroup** *(dict) --*

        Contains all of the attributes of a specific Redis replication group.
        - **ReplicationGroupId** *(string) --*

          The identifier for the replication group.
    """


_ClientCreateReplicationGroupTagsTypeDef = TypedDict(
    "_ClientCreateReplicationGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateReplicationGroupTagsTypeDef(_ClientCreateReplicationGroupTagsTypeDef):
    """
    - *(dict) --*

      A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags
      are composed of a Key/Value pair. A tag with a null Value is permitted.
      - **Key** *(string) --*

        The key for the tag. May not be null.
    """


_ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "_ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)


class ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef(
    _ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef
):
    pass


_ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef = TypedDict(
    "_ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)


class ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef(
    _ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef
):
    pass


_ClientCreateSnapshotResponseSnapshotTypeDef = TypedDict(
    "_ClientCreateSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "NodeSnapshots": List[ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)


class ClientCreateSnapshotResponseSnapshotTypeDef(_ClientCreateSnapshotResponseSnapshotTypeDef):
    """
    - **Snapshot** *(dict) --*

      Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.
      - **SnapshotName** *(string) --*

        The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
        manual snapshot, this is the user-provided name.
    """


_ClientCreateSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateSnapshotResponseTypeDef",
    {"Snapshot": ClientCreateSnapshotResponseSnapshotTypeDef},
    total=False,
)


class ClientCreateSnapshotResponseTypeDef(_ClientCreateSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **Snapshot** *(dict) --*

        Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.
        - **SnapshotName** *(string) --*

          The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
          manual snapshot, this is the user-provided name.
    """


_RequiredClientDecreaseReplicaCountReplicaConfigurationTypeDef = TypedDict(
    "_RequiredClientDecreaseReplicaCountReplicaConfigurationTypeDef", {"NodeGroupId": str}
)
_OptionalClientDecreaseReplicaCountReplicaConfigurationTypeDef = TypedDict(
    "_OptionalClientDecreaseReplicaCountReplicaConfigurationTypeDef",
    {"NewReplicaCount": int, "PreferredAvailabilityZones": List[str]},
    total=False,
)


class ClientDecreaseReplicaCountReplicaConfigurationTypeDef(
    _RequiredClientDecreaseReplicaCountReplicaConfigurationTypeDef,
    _OptionalClientDecreaseReplicaCountReplicaConfigurationTypeDef,
):
    """
    - *(dict) --*

      Node group (shard) configuration options when adding or removing replicas. Each node group
      (shard) configuration has the following members: NodeGroupId, NewReplicaCount, and
      PreferredAvailabilityZones.
      - **NodeGroupId** *(string) --***[REQUIRED]**

        The 4-digit id for the node group you are configuring. For Redis (cluster mode disabled)
        replication groups, the node group id is always 0001. To find a Redis (cluster mode
        enabled)'s node group's (shard's) id, see `Finding a Shard's Id
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/shard-find-id.html>`__ .
    """


_ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef
):
    pass


_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    pass


_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    pass


_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    pass


_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    pass


_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef
):
    pass


_ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    pass


_ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    pass


_ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef
):
    pass


_ClientDecreaseReplicaCountResponseReplicationGroupTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupTypeDef
):
    """
    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.
      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.
    """


_ClientDecreaseReplicaCountResponseTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseTypeDef",
    {"ReplicationGroup": ClientDecreaseReplicaCountResponseReplicationGroupTypeDef},
    total=False,
)


class ClientDecreaseReplicaCountResponseTypeDef(_ClientDecreaseReplicaCountResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationGroup** *(dict) --*

        Contains all of the attributes of a specific Redis replication group.
        - **ReplicationGroupId** *(string) --*

          The identifier for the replication group.
    """


_ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef
):
    pass


_ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef
):
    pass


_ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef
):
    pass


_ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
):
    pass


_ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef
):
    pass


_ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef
):
    pass


_ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef
):
    pass


_ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef
):
    pass


_ClientDeleteCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterTypeDef
):
    """
    - **CacheCluster** *(dict) --*

      Contains all of the attributes of a specific cluster.
      - **CacheClusterId** *(string) --*

        The user-supplied identifier of the cluster. This identifier is a unique key that identifies
        a cluster.
    """


_ClientDeleteCacheClusterResponseTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseTypeDef",
    {"CacheCluster": ClientDeleteCacheClusterResponseCacheClusterTypeDef},
    total=False,
)


class ClientDeleteCacheClusterResponseTypeDef(_ClientDeleteCacheClusterResponseTypeDef):
    """
    - *(dict) --*

      - **CacheCluster** *(dict) --*

        Contains all of the attributes of a specific cluster.
        - **CacheClusterId** *(string) --*

          The user-supplied identifier of the cluster. This identifier is a unique key that
          identifies a cluster.
    """


_ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef
):
    pass


_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    pass


_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    pass


_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    pass


_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    pass


_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef
):
    pass


_ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    pass


_ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    pass


_ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef
):
    pass


_ClientDeleteReplicationGroupResponseReplicationGroupTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupTypeDef
):
    """
    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.
      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.
    """


_ClientDeleteReplicationGroupResponseTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseTypeDef",
    {"ReplicationGroup": ClientDeleteReplicationGroupResponseReplicationGroupTypeDef},
    total=False,
)


class ClientDeleteReplicationGroupResponseTypeDef(_ClientDeleteReplicationGroupResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationGroup** *(dict) --*

        Contains all of the attributes of a specific Redis replication group.
        - **ReplicationGroupId** *(string) --*

          The identifier for the replication group.
    """


_ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "_ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)


class ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef(
    _ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef
):
    pass


_ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef = TypedDict(
    "_ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)


class ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef(
    _ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef
):
    pass


_ClientDeleteSnapshotResponseSnapshotTypeDef = TypedDict(
    "_ClientDeleteSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "NodeSnapshots": List[ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)


class ClientDeleteSnapshotResponseSnapshotTypeDef(_ClientDeleteSnapshotResponseSnapshotTypeDef):
    """
    - **Snapshot** *(dict) --*

      Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.
      - **SnapshotName** *(string) --*

        The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
        manual snapshot, this is the user-provided name.
    """


_ClientDeleteSnapshotResponseTypeDef = TypedDict(
    "_ClientDeleteSnapshotResponseTypeDef",
    {"Snapshot": ClientDeleteSnapshotResponseSnapshotTypeDef},
    total=False,
)


class ClientDeleteSnapshotResponseTypeDef(_ClientDeleteSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **Snapshot** *(dict) --*

        Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.
        - **SnapshotName** *(string) --*

          The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
          manual snapshot, this is the user-provided name.
    """


_ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef
):
    pass


_ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef
):
    pass


_ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef
):
    pass


_ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef
):
    pass


_ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef
):
    pass


_ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef
):
    pass


_ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef
):
    pass


_ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef
):
    pass


_ClientDescribeCacheClustersResponseCacheClustersTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[
            ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef
        ],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersTypeDef
):
    pass


_ClientDescribeCacheClustersResponseTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseTypeDef",
    {"Marker": str, "CacheClusters": List[ClientDescribeCacheClustersResponseCacheClustersTypeDef]},
    total=False,
)


class ClientDescribeCacheClustersResponseTypeDef(_ClientDescribeCacheClustersResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DescribeCacheClusters`` operation.
      - **Marker** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef = TypedDict(
    "_ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupFamily": str,
        "CacheEngineDescription": str,
        "CacheEngineVersionDescription": str,
    },
    total=False,
)


class ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef(
    _ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef
):
    pass


_ClientDescribeCacheEngineVersionsResponseTypeDef = TypedDict(
    "_ClientDescribeCacheEngineVersionsResponseTypeDef",
    {
        "Marker": str,
        "CacheEngineVersions": List[
            ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCacheEngineVersionsResponseTypeDef(
    _ClientDescribeCacheEngineVersionsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a  DescribeCacheEngineVersions operation.
      - **Marker** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef = TypedDict(
    "_ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef",
    {"CacheParameterGroupName": str, "CacheParameterGroupFamily": str, "Description": str},
    total=False,
)


class ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef(
    _ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef
):
    pass


_ClientDescribeCacheParameterGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeCacheParameterGroupsResponseTypeDef",
    {
        "Marker": str,
        "CacheParameterGroups": List[
            ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCacheParameterGroupsResponseTypeDef(
    _ClientDescribeCacheParameterGroupsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeCacheParameterGroups`` operation.
      - **Marker** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "_ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)


class ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef(
    _ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
):
    pass


_ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "_ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef",
    {
        "ParameterName": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "CacheNodeTypeSpecificValues": List[
            ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
        ],
        "ChangeType": Literal["immediate", "requires-reboot"],
    },
    total=False,
)


class ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef(
    _ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef
):
    pass


_ClientDescribeCacheParametersResponseParametersTypeDef = TypedDict(
    "_ClientDescribeCacheParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ChangeType": Literal["immediate", "requires-reboot"],
    },
    total=False,
)


class ClientDescribeCacheParametersResponseParametersTypeDef(
    _ClientDescribeCacheParametersResponseParametersTypeDef
):
    pass


_ClientDescribeCacheParametersResponseTypeDef = TypedDict(
    "_ClientDescribeCacheParametersResponseTypeDef",
    {
        "Marker": str,
        "Parameters": List[ClientDescribeCacheParametersResponseParametersTypeDef],
        "CacheNodeTypeSpecificParameters": List[
            ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCacheParametersResponseTypeDef(_ClientDescribeCacheParametersResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DescribeCacheParameters`` operation.
      - **Marker** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)


class ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef(
    _ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef
):
    pass


_ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef(
    _ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef
):
    pass


_ClientDescribeCacheSecurityGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeCacheSecurityGroupsResponseTypeDef",
    {
        "Marker": str,
        "CacheSecurityGroups": List[
            ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCacheSecurityGroupsResponseTypeDef(
    _ClientDescribeCacheSecurityGroupsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeCacheSecurityGroups`` operation.
      - **Marker** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef = TypedDict(
    "_ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)


class ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef(
    _ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef
):
    pass


_ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef = TypedDict(
    "_ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef],
    },
    total=False,
)


class ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef(
    _ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef
):
    pass


_ClientDescribeCacheSubnetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeCacheSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "CacheSubnetGroups": List[ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef],
    },
    total=False,
)


class ClientDescribeCacheSubnetGroupsResponseTypeDef(
    _ClientDescribeCacheSubnetGroupsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeCacheSubnetGroups`` operation.
      - **Marker** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)


class ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef(
    _ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
):
    pass


_ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef",
    {
        "ParameterName": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "CacheNodeTypeSpecificValues": List[
            ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
        ],
        "ChangeType": Literal["immediate", "requires-reboot"],
    },
    total=False,
)


class ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef(
    _ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef
):
    pass


_ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ChangeType": Literal["immediate", "requires-reboot"],
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
        "CacheParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef
        ],
        "CacheNodeTypeSpecificParameters": List[
            ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef(
    _ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef
):
    """
    - **EngineDefaults** *(dict) --*

      Represents the output of a ``DescribeEngineDefaultParameters`` operation.
      - **CacheParameterGroupFamily** *(string) --*

        Specifies the name of the cache parameter group family to which the engine default
        parameters apply.
        Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
        ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |
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

        Represents the output of a ``DescribeEngineDefaultParameters`` operation.
        - **CacheParameterGroupFamily** *(string) --*

          Specifies the name of the cache parameter group family to which the engine default
          parameters apply.
          Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8``
          |
          ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |
    """


_ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal[
            "cache-cluster",
            "cache-parameter-group",
            "cache-security-group",
            "cache-subnet-group",
            "replication-group",
        ],
        "Message": str,
        "Date": datetime,
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

      Represents the output of a ``DescribeEvents`` operation.
      - **Marker** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef
):
    pass


_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    pass


_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef
):
    pass


_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef
):
    pass


_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef
):
    pass


_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef
):
    pass


_ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    pass


_ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef
):
    pass


_ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef
):
    pass


_ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef
):
    pass


_ClientDescribeReplicationGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationGroups": List[ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef],
    },
    total=False,
)


class ClientDescribeReplicationGroupsResponseTypeDef(
    _ClientDescribeReplicationGroupsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeReplicationGroups`` operation.
      - **Marker** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef = TypedDict(
    "_ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef(
    _ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef
):
    pass


_ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef = TypedDict(
    "_ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "ProductDescription": str,
        "OfferingType": str,
        "RecurringCharges": List[
            ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef(
    _ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef
):
    pass


_ClientDescribeReservedCacheNodesOfferingsResponseTypeDef = TypedDict(
    "_ClientDescribeReservedCacheNodesOfferingsResponseTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodesOfferings": List[
            ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedCacheNodesOfferingsResponseTypeDef(
    _ClientDescribeReservedCacheNodesOfferingsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeReservedCacheNodesOfferings`` operation.
      - **Marker** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeReservedCacheNodesResponseReservedCacheNodesRecurringChargesTypeDef = TypedDict(
    "_ClientDescribeReservedCacheNodesResponseReservedCacheNodesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientDescribeReservedCacheNodesResponseReservedCacheNodesRecurringChargesTypeDef(
    _ClientDescribeReservedCacheNodesResponseReservedCacheNodesRecurringChargesTypeDef
):
    pass


_ClientDescribeReservedCacheNodesResponseReservedCacheNodesTypeDef = TypedDict(
    "_ClientDescribeReservedCacheNodesResponseReservedCacheNodesTypeDef",
    {
        "ReservedCacheNodeId": str,
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CacheNodeCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "State": str,
        "RecurringCharges": List[
            ClientDescribeReservedCacheNodesResponseReservedCacheNodesRecurringChargesTypeDef
        ],
        "ReservationARN": str,
    },
    total=False,
)


class ClientDescribeReservedCacheNodesResponseReservedCacheNodesTypeDef(
    _ClientDescribeReservedCacheNodesResponseReservedCacheNodesTypeDef
):
    pass


_ClientDescribeReservedCacheNodesResponseTypeDef = TypedDict(
    "_ClientDescribeReservedCacheNodesResponseTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodes": List[
            ClientDescribeReservedCacheNodesResponseReservedCacheNodesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedCacheNodesResponseTypeDef(
    _ClientDescribeReservedCacheNodesResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeReservedCacheNodes`` operation.
      - **Marker** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef = TypedDict(
    "_ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef",
    {
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateEndDate": datetime,
        "ServiceUpdateSeverity": Literal["critical", "important", "medium", "low"],
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateStatus": Literal["available", "cancelled", "expired"],
        "ServiceUpdateDescription": str,
        "ServiceUpdateType": str,
        "Engine": str,
        "EngineVersion": str,
        "AutoUpdateAfterRecommendedApplyByDate": bool,
        "EstimatedUpdateTime": str,
    },
    total=False,
)


class ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef(
    _ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef
):
    pass


_ClientDescribeServiceUpdatesResponseTypeDef = TypedDict(
    "_ClientDescribeServiceUpdatesResponseTypeDef",
    {
        "Marker": str,
        "ServiceUpdates": List[ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef],
    },
    total=False,
)


class ClientDescribeServiceUpdatesResponseTypeDef(_ClientDescribeServiceUpdatesResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional marker returned from a prior request. Use this marker for pagination of results
        from this operation. If this parameter is specified, the response includes only records
        beyond the marker, up to the value specified by ``MaxRecords`` .
    """


_ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "_ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)


class ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef(
    _ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef
):
    pass


_ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef = TypedDict(
    "_ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)


class ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef(
    _ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef
):
    pass


_ClientDescribeSnapshotsResponseSnapshotsTypeDef = TypedDict(
    "_ClientDescribeSnapshotsResponseSnapshotsTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "NodeSnapshots": List[ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)


class ClientDescribeSnapshotsResponseSnapshotsTypeDef(
    _ClientDescribeSnapshotsResponseSnapshotsTypeDef
):
    pass


_ClientDescribeSnapshotsResponseTypeDef = TypedDict(
    "_ClientDescribeSnapshotsResponseTypeDef",
    {"Marker": str, "Snapshots": List[ClientDescribeSnapshotsResponseSnapshotsTypeDef]},
    total=False,
)


class ClientDescribeSnapshotsResponseTypeDef(_ClientDescribeSnapshotsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DescribeSnapshots`` operation.
      - **Marker** *(string) --*

        An optional marker returned from a prior request. Use this marker for pagination of results
        from this operation. If this parameter is specified, the response includes only records
        beyond the marker, up to the value specified by ``MaxRecords`` .
    """


_ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef = TypedDict(
    "_ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef",
    {
        "CacheNodeId": str,
        "NodeUpdateStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": Literal["system", "customer"],
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef(
    _ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef
):
    pass


_ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef = TypedDict(
    "_ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "NodeUpdateStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": Literal["system", "customer"],
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef(
    _ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef
):
    pass


_ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef = TypedDict(
    "_ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef",
    {
        "NodeGroupId": str,
        "NodeGroupMemberUpdateStatus": List[
            ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef
        ],
    },
    total=False,
)


class ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef(
    _ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef
):
    pass


_ClientDescribeUpdateActionsResponseUpdateActionsTypeDef = TypedDict(
    "_ClientDescribeUpdateActionsResponseUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateSeverity": Literal["critical", "important", "medium", "low"],
        "ServiceUpdateStatus": Literal["available", "cancelled", "expired"],
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateType": str,
        "UpdateActionAvailableDate": datetime,
        "UpdateActionStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
        "NodesUpdated": str,
        "UpdateActionStatusModifiedDate": datetime,
        "SlaMet": Literal["yes", "no", "n/a"],
        "NodeGroupUpdateStatus": List[
            ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef
        ],
        "CacheNodeUpdateStatus": List[
            ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef
        ],
        "EstimatedUpdateTime": str,
        "Engine": str,
    },
    total=False,
)


class ClientDescribeUpdateActionsResponseUpdateActionsTypeDef(
    _ClientDescribeUpdateActionsResponseUpdateActionsTypeDef
):
    pass


_ClientDescribeUpdateActionsResponseTypeDef = TypedDict(
    "_ClientDescribeUpdateActionsResponseTypeDef",
    {"Marker": str, "UpdateActions": List[ClientDescribeUpdateActionsResponseUpdateActionsTypeDef]},
    total=False,
)


class ClientDescribeUpdateActionsResponseTypeDef(_ClientDescribeUpdateActionsResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional marker returned from a prior request. Use this marker for pagination of results
        from this operation. If this parameter is specified, the response includes only records
        beyond the marker, up to the value specified by ``MaxRecords`` .
    """


_ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef = TypedDict(
    "_ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)


class ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef(
    _ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef
):
    """
    The range of time specified to search for service updates that are in available status
    - **StartTime** *(datetime) --*

      The start time of the time range filter
    """


_RequiredClientIncreaseReplicaCountReplicaConfigurationTypeDef = TypedDict(
    "_RequiredClientIncreaseReplicaCountReplicaConfigurationTypeDef", {"NodeGroupId": str}
)
_OptionalClientIncreaseReplicaCountReplicaConfigurationTypeDef = TypedDict(
    "_OptionalClientIncreaseReplicaCountReplicaConfigurationTypeDef",
    {"NewReplicaCount": int, "PreferredAvailabilityZones": List[str]},
    total=False,
)


class ClientIncreaseReplicaCountReplicaConfigurationTypeDef(
    _RequiredClientIncreaseReplicaCountReplicaConfigurationTypeDef,
    _OptionalClientIncreaseReplicaCountReplicaConfigurationTypeDef,
):
    """
    - *(dict) --*

      Node group (shard) configuration options when adding or removing replicas. Each node group
      (shard) configuration has the following members: NodeGroupId, NewReplicaCount, and
      PreferredAvailabilityZones.
      - **NodeGroupId** *(string) --***[REQUIRED]**

        The 4-digit id for the node group you are configuring. For Redis (cluster mode disabled)
        replication groups, the node group id is always 0001. To find a Redis (cluster mode
        enabled)'s node group's (shard's) id, see `Finding a Shard's Id
        <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/shard-find-id.html>`__ .
    """


_ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef
):
    pass


_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    pass


_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    pass


_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    pass


_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    pass


_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef
):
    pass


_ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    pass


_ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    pass


_ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef
):
    pass


_ClientIncreaseReplicaCountResponseReplicationGroupTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupTypeDef
):
    """
    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.
      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.
    """


_ClientIncreaseReplicaCountResponseTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseTypeDef",
    {"ReplicationGroup": ClientIncreaseReplicaCountResponseReplicationGroupTypeDef},
    total=False,
)


class ClientIncreaseReplicaCountResponseTypeDef(_ClientIncreaseReplicaCountResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationGroup** *(dict) --*

        Contains all of the attributes of a specific Redis replication group.
        - **ReplicationGroupId** *(string) --*

          The identifier for the replication group.
    """


_ClientListAllowedNodeTypeModificationsResponseTypeDef = TypedDict(
    "_ClientListAllowedNodeTypeModificationsResponseTypeDef",
    {"ScaleUpModifications": List[str], "ScaleDownModifications": List[str]},
    total=False,
)


class ClientListAllowedNodeTypeModificationsResponseTypeDef(
    _ClientListAllowedNodeTypeModificationsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the allowed node types you can use to modify your cluster or replication group.
      - **ScaleUpModifications** *(list) --*

        A string list, each element of which specifies a cache node type which you can use to scale
        your cluster or replication group.
        When scaling up a Redis cluster or replication group using ``ModifyCacheCluster`` or
        ``ModifyReplicationGroup`` , use a value from this list for the ``CacheNodeType`` parameter.
        - *(string) --*
    """


_ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagListTypeDef(
    _ClientListTagsForResourceResponseTagListTypeDef
):
    """
    - *(dict) --*

      A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags
      are composed of a Key/Value pair. A tag with a null Value is permitted.
      - **Key** *(string) --*

        The key for the tag. May not be null.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      Represents the output from the ``AddTagsToResource`` , ``ListTagsForResource`` , and
      ``RemoveTagsFromResource`` operations.
      - **TagList** *(list) --*

        A list of cost allocation tags as key-value pairs.
        - *(dict) --*

          A cost allocation Tag that can be added to an ElastiCache cluster or replication group.
          Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
          - **Key** *(string) --*

            The key for the tag. May not be null.
    """


_ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef
):
    pass


_ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef
):
    pass


_ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef
):
    pass


_ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
):
    pass


_ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef
):
    pass


_ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef
):
    pass


_ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef
):
    pass


_ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef
):
    pass


_ClientModifyCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterTypeDef
):
    """
    - **CacheCluster** *(dict) --*

      Contains all of the attributes of a specific cluster.
      - **CacheClusterId** *(string) --*

        The user-supplied identifier of the cluster. This identifier is a unique key that identifies
        a cluster.
    """


_ClientModifyCacheClusterResponseTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseTypeDef",
    {"CacheCluster": ClientModifyCacheClusterResponseCacheClusterTypeDef},
    total=False,
)


class ClientModifyCacheClusterResponseTypeDef(_ClientModifyCacheClusterResponseTypeDef):
    """
    - *(dict) --*

      - **CacheCluster** *(dict) --*

        Contains all of the attributes of a specific cluster.
        - **CacheClusterId** *(string) --*

          The user-supplied identifier of the cluster. This identifier is a unique key that
          identifies a cluster.
    """


_ClientModifyCacheParameterGroupParameterNameValuesTypeDef = TypedDict(
    "_ClientModifyCacheParameterGroupParameterNameValuesTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientModifyCacheParameterGroupParameterNameValuesTypeDef(
    _ClientModifyCacheParameterGroupParameterNameValuesTypeDef
):
    """
    - *(dict) --*

      Describes a name-value pair that is used to update the value of a parameter.
      - **ParameterName** *(string) --*

        The name of the parameter.
    """


_ClientModifyCacheParameterGroupResponseTypeDef = TypedDict(
    "_ClientModifyCacheParameterGroupResponseTypeDef", {"CacheParameterGroupName": str}, total=False
)


class ClientModifyCacheParameterGroupResponseTypeDef(
    _ClientModifyCacheParameterGroupResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of one of the following operations:
      * ``ModifyCacheParameterGroup``
      * ``ResetCacheParameterGroup``
      - **CacheParameterGroupName** *(string) --*

        The name of the cache parameter group.
    """


_ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)


class ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef(
    _ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef
):
    pass


_ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef = TypedDict(
    "_ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef],
    },
    total=False,
)


class ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef(
    _ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef
):
    """
    - **CacheSubnetGroup** *(dict) --*

      Represents the output of one of the following operations:
      * ``CreateCacheSubnetGroup``
      * ``ModifyCacheSubnetGroup``
      - **CacheSubnetGroupName** *(string) --*

        The name of the cache subnet group.
    """


_ClientModifyCacheSubnetGroupResponseTypeDef = TypedDict(
    "_ClientModifyCacheSubnetGroupResponseTypeDef",
    {"CacheSubnetGroup": ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef},
    total=False,
)


class ClientModifyCacheSubnetGroupResponseTypeDef(_ClientModifyCacheSubnetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **CacheSubnetGroup** *(dict) --*

        Represents the output of one of the following operations:
        * ``CreateCacheSubnetGroup``
        * ``ModifyCacheSubnetGroup``
        - **CacheSubnetGroupName** *(string) --*

          The name of the cache subnet group.
    """


_ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef
):
    pass


_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    pass


_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    pass


_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    pass


_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    pass


_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef
):
    pass


_ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    pass


_ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    pass


_ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef
):
    pass


_ClientModifyReplicationGroupResponseReplicationGroupTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupTypeDef
):
    """
    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.
      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.
    """


_ClientModifyReplicationGroupResponseTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseTypeDef",
    {"ReplicationGroup": ClientModifyReplicationGroupResponseReplicationGroupTypeDef},
    total=False,
)


class ClientModifyReplicationGroupResponseTypeDef(_ClientModifyReplicationGroupResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationGroup** *(dict) --*

        Contains all of the attributes of a specific Redis replication group.
        - **ReplicationGroupId** *(string) --*

          The identifier for the replication group.
    """


_ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef",
    {"NodeGroupId": str, "PreferredAvailabilityZones": List[str]},
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef(
    _ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef
):
    """
    - *(dict) --*

      A list of ``PreferredAvailabilityZones`` objects that specifies the configuration of a node
      group in the resharded cluster.
      - **NodeGroupId** *(string) --*

        Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node
        group these configuration values apply to.
    """


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef
):
    pass


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    pass


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    pass


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    pass


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    pass


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef
):
    pass


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    pass


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    pass


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef
):
    pass


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef
):
    """
    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.
      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.
    """


_ClientModifyReplicationGroupShardConfigurationResponseTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseTypeDef",
    {
        "ReplicationGroup": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef
    },
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **ReplicationGroup** *(dict) --*

        Contains all of the attributes of a specific Redis replication group.
        - **ReplicationGroupId** *(string) --*

          The identifier for the replication group.
    """


_ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef = TypedDict(
    "_ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef(
    _ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef
):
    pass


_ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef = TypedDict(
    "_ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef",
    {
        "ReservedCacheNodeId": str,
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CacheNodeCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "State": str,
        "RecurringCharges": List[
            ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef
        ],
        "ReservationARN": str,
    },
    total=False,
)


class ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef(
    _ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef
):
    """
    - **ReservedCacheNode** *(dict) --*

      Represents the output of a ``PurchaseReservedCacheNodesOffering`` operation.
      - **ReservedCacheNodeId** *(string) --*

        The unique identifier for the reservation.
    """


_ClientPurchaseReservedCacheNodesOfferingResponseTypeDef = TypedDict(
    "_ClientPurchaseReservedCacheNodesOfferingResponseTypeDef",
    {"ReservedCacheNode": ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef},
    total=False,
)


class ClientPurchaseReservedCacheNodesOfferingResponseTypeDef(
    _ClientPurchaseReservedCacheNodesOfferingResponseTypeDef
):
    """
    - *(dict) --*

      - **ReservedCacheNode** *(dict) --*

        Represents the output of a ``PurchaseReservedCacheNodesOffering`` operation.
        - **ReservedCacheNodeId** *(string) --*

          The unique identifier for the reservation.
    """


_ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef
):
    pass


_ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef
):
    pass


_ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef
):
    pass


_ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
):
    pass


_ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef
):
    pass


_ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef
):
    pass


_ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef
):
    pass


_ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef
):
    pass


_ClientRebootCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterTypeDef
):
    """
    - **CacheCluster** *(dict) --*

      Contains all of the attributes of a specific cluster.
      - **CacheClusterId** *(string) --*

        The user-supplied identifier of the cluster. This identifier is a unique key that identifies
        a cluster.
    """


_ClientRebootCacheClusterResponseTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseTypeDef",
    {"CacheCluster": ClientRebootCacheClusterResponseCacheClusterTypeDef},
    total=False,
)


class ClientRebootCacheClusterResponseTypeDef(_ClientRebootCacheClusterResponseTypeDef):
    """
    - *(dict) --*

      - **CacheCluster** *(dict) --*

        Contains all of the attributes of a specific cluster.
        - **CacheClusterId** *(string) --*

          The user-supplied identifier of the cluster. This identifier is a unique key that
          identifies a cluster.
    """


_ClientRemoveTagsFromResourceResponseTagListTypeDef = TypedDict(
    "_ClientRemoveTagsFromResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRemoveTagsFromResourceResponseTagListTypeDef(
    _ClientRemoveTagsFromResourceResponseTagListTypeDef
):
    """
    - *(dict) --*

      A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags
      are composed of a Key/Value pair. A tag with a null Value is permitted.
      - **Key** *(string) --*

        The key for the tag. May not be null.
    """


_ClientRemoveTagsFromResourceResponseTypeDef = TypedDict(
    "_ClientRemoveTagsFromResourceResponseTypeDef",
    {"TagList": List[ClientRemoveTagsFromResourceResponseTagListTypeDef]},
    total=False,
)


class ClientRemoveTagsFromResourceResponseTypeDef(_ClientRemoveTagsFromResourceResponseTypeDef):
    """
    - *(dict) --*

      Represents the output from the ``AddTagsToResource`` , ``ListTagsForResource`` , and
      ``RemoveTagsFromResource`` operations.
      - **TagList** *(list) --*

        A list of cost allocation tags as key-value pairs.
        - *(dict) --*

          A cost allocation Tag that can be added to an ElastiCache cluster or replication group.
          Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
          - **Key** *(string) --*

            The key for the tag. May not be null.
    """


_ClientResetCacheParameterGroupParameterNameValuesTypeDef = TypedDict(
    "_ClientResetCacheParameterGroupParameterNameValuesTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientResetCacheParameterGroupParameterNameValuesTypeDef(
    _ClientResetCacheParameterGroupParameterNameValuesTypeDef
):
    """
    - *(dict) --*

      Describes a name-value pair that is used to update the value of a parameter.
      - **ParameterName** *(string) --*

        The name of the parameter.
    """


_ClientResetCacheParameterGroupResponseTypeDef = TypedDict(
    "_ClientResetCacheParameterGroupResponseTypeDef", {"CacheParameterGroupName": str}, total=False
)


class ClientResetCacheParameterGroupResponseTypeDef(_ClientResetCacheParameterGroupResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of one of the following operations:
      * ``ModifyCacheParameterGroup``
      * ``ResetCacheParameterGroup``
      - **CacheParameterGroupName** *(string) --*

        The name of the cache parameter group.
    """


_ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)


class ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef(
    _ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
):
    pass


_ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef = TypedDict(
    "_ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)


class ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef(
    _ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef
):
    """
    - **CacheSecurityGroup** *(dict) --*

      Represents the output of one of the following operations:
      * ``AuthorizeCacheSecurityGroupIngress``
      * ``CreateCacheSecurityGroup``
      * ``RevokeCacheSecurityGroupIngress``
      - **OwnerId** *(string) --*

        The AWS account ID of the cache security group owner.
    """


_ClientRevokeCacheSecurityGroupIngressResponseTypeDef = TypedDict(
    "_ClientRevokeCacheSecurityGroupIngressResponseTypeDef",
    {"CacheSecurityGroup": ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef},
    total=False,
)


class ClientRevokeCacheSecurityGroupIngressResponseTypeDef(
    _ClientRevokeCacheSecurityGroupIngressResponseTypeDef
):
    """
    - *(dict) --*

      - **CacheSecurityGroup** *(dict) --*

        Represents the output of one of the following operations:
        * ``AuthorizeCacheSecurityGroupIngress``
        * ``CreateCacheSecurityGroup``
        * ``RevokeCacheSecurityGroupIngress``
        - **OwnerId** *(string) --*

          The AWS account ID of the cache security group owner.
    """


_ClientStartMigrationCustomerNodeEndpointListTypeDef = TypedDict(
    "_ClientStartMigrationCustomerNodeEndpointListTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientStartMigrationCustomerNodeEndpointListTypeDef(
    _ClientStartMigrationCustomerNodeEndpointListTypeDef
):
    """
    - *(dict) --*

      The endpoint from which data should be migrated.
      - **Address** *(string) --*

        The address of the node endpoint
    """


_ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef
):
    pass


_ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    pass


_ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    pass


_ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    pass


_ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    pass


_ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef(
    _ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef
):
    pass


_ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    pass


_ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    pass


_ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef
):
    pass


_ClientStartMigrationResponseReplicationGroupTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientStartMigrationResponseReplicationGroupTypeDef(
    _ClientStartMigrationResponseReplicationGroupTypeDef
):
    """
    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.
      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.
    """


_ClientStartMigrationResponseTypeDef = TypedDict(
    "_ClientStartMigrationResponseTypeDef",
    {"ReplicationGroup": ClientStartMigrationResponseReplicationGroupTypeDef},
    total=False,
)


class ClientStartMigrationResponseTypeDef(_ClientStartMigrationResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationGroup** *(dict) --*

        Contains all of the attributes of a specific Redis replication group.
        - **ReplicationGroupId** *(string) --*

          The identifier for the replication group.
    """


_ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef
):
    pass


_ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    pass


_ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    pass


_ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    pass


_ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    pass


_ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef(
    _ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef
):
    pass


_ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    pass


_ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    pass


_ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef
):
    pass


_ClientTestFailoverResponseReplicationGroupTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientTestFailoverResponseReplicationGroupTypeDef(
    _ClientTestFailoverResponseReplicationGroupTypeDef
):
    """
    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.
      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.
    """


_ClientTestFailoverResponseTypeDef = TypedDict(
    "_ClientTestFailoverResponseTypeDef",
    {"ReplicationGroup": ClientTestFailoverResponseReplicationGroupTypeDef},
    total=False,
)


class ClientTestFailoverResponseTypeDef(_ClientTestFailoverResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationGroup** *(dict) --*

        Contains all of the attributes of a specific Redis replication group.
        - **ReplicationGroupId** *(string) --*

          The identifier for the replication group.
    """


_DescribeCacheClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCacheClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCacheClustersPaginatePaginationConfigTypeDef(
    _DescribeCacheClustersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef
):
    pass


_DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef
):
    pass


_DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef
):
    pass


_DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef
):
    pass


_DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef
):
    pass


_DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef
):
    pass


_DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef
):
    pass


_DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef
):
    pass


_DescribeCacheClustersPaginateResponseCacheClustersTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef,
        "NotificationConfiguration": DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[
            DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef
        ],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersTypeDef
):
    """
    - *(dict) --*

      Contains all of the attributes of a specific cluster.
      - **CacheClusterId** *(string) --*

        The user-supplied identifier of the cluster. This identifier is a unique key that identifies
        a cluster.
    """


_DescribeCacheClustersPaginateResponseTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseTypeDef",
    {
        "CacheClusters": List[DescribeCacheClustersPaginateResponseCacheClustersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeCacheClustersPaginateResponseTypeDef(_DescribeCacheClustersPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DescribeCacheClusters`` operation.
      - **CacheClusters** *(list) --*

        A list of clusters. Each item in the list contains detailed information about one cluster.
        - *(dict) --*

          Contains all of the attributes of a specific cluster.
          - **CacheClusterId** *(string) --*

            The user-supplied identifier of the cluster. This identifier is a unique key that
            identifies a cluster.
    """


_DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef(
    _DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef = TypedDict(
    "_DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupFamily": str,
        "CacheEngineDescription": str,
        "CacheEngineVersionDescription": str,
    },
    total=False,
)


class DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef(
    _DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef
):
    """
    - *(dict) --*

      Provides all of the details about a particular cache engine version.
      - **Engine** *(string) --*

        The name of the cache engine.
    """


_DescribeCacheEngineVersionsPaginateResponseTypeDef = TypedDict(
    "_DescribeCacheEngineVersionsPaginateResponseTypeDef",
    {
        "CacheEngineVersions": List[
            DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeCacheEngineVersionsPaginateResponseTypeDef(
    _DescribeCacheEngineVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a  DescribeCacheEngineVersions operation.
      - **CacheEngineVersions** *(list) --*

        A list of cache engine version details. Each element in the list contains detailed
        information about one cache engine version.
        - *(dict) --*

          Provides all of the details about a particular cache engine version.
          - **Engine** *(string) --*

            The name of the cache engine.
    """


_DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef(
    _DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef = TypedDict(
    "_DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef",
    {"CacheParameterGroupName": str, "CacheParameterGroupFamily": str, "Description": str},
    total=False,
)


class DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef(
    _DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``CreateCacheParameterGroup`` operation.
      - **CacheParameterGroupName** *(string) --*

        The name of the cache parameter group.
    """


_DescribeCacheParameterGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeCacheParameterGroupsPaginateResponseTypeDef",
    {
        "CacheParameterGroups": List[
            DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeCacheParameterGroupsPaginateResponseTypeDef(
    _DescribeCacheParameterGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeCacheParameterGroups`` operation.
      - **CacheParameterGroups** *(list) --*

        A list of cache parameter groups. Each element in the list contains detailed information
        about one cache parameter group.
        - *(dict) --*

          Represents the output of a ``CreateCacheParameterGroup`` operation.
          - **CacheParameterGroupName** *(string) --*

            The name of the cache parameter group.
    """


_DescribeCacheParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCacheParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCacheParametersPaginatePaginationConfigTypeDef(
    _DescribeCacheParametersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "_DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)


class DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef(
    _DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
):
    pass


_DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "_DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef",
    {
        "ParameterName": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "CacheNodeTypeSpecificValues": List[
            DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
        ],
        "ChangeType": Literal["immediate", "requires-reboot"],
    },
    total=False,
)


class DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef(
    _DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef
):
    pass


_DescribeCacheParametersPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeCacheParametersPaginateResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ChangeType": Literal["immediate", "requires-reboot"],
    },
    total=False,
)


class DescribeCacheParametersPaginateResponseParametersTypeDef(
    _DescribeCacheParametersPaginateResponseParametersTypeDef
):
    """
    - *(dict) --*

      Describes an individual setting that controls some aspect of ElastiCache behavior.
      - **ParameterName** *(string) --*

        The name of the parameter.
    """


_DescribeCacheParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeCacheParametersPaginateResponseTypeDef",
    {
        "Parameters": List[DescribeCacheParametersPaginateResponseParametersTypeDef],
        "CacheNodeTypeSpecificParameters": List[
            DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeCacheParametersPaginateResponseTypeDef(
    _DescribeCacheParametersPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeCacheParameters`` operation.
      - **Parameters** *(list) --*

        A list of  Parameter instances.
        - *(dict) --*

          Describes an individual setting that controls some aspect of ElastiCache behavior.
          - **ParameterName** *(string) --*

            The name of the parameter.
    """


_DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef(
    _DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef = TypedDict(
    "_DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)


class DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef(
    _DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef
):
    pass


_DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef = TypedDict(
    "_DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)


class DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef(
    _DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef
):
    """
    - *(dict) --*

      Represents the output of one of the following operations:
      * ``AuthorizeCacheSecurityGroupIngress``
      * ``CreateCacheSecurityGroup``
      * ``RevokeCacheSecurityGroupIngress``
      - **OwnerId** *(string) --*

        The AWS account ID of the cache security group owner.
    """


_DescribeCacheSecurityGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeCacheSecurityGroupsPaginateResponseTypeDef",
    {
        "CacheSecurityGroups": List[
            DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeCacheSecurityGroupsPaginateResponseTypeDef(
    _DescribeCacheSecurityGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeCacheSecurityGroups`` operation.
      - **CacheSecurityGroups** *(list) --*

        A list of cache security groups. Each element in the list contains detailed information
        about one group.
        - *(dict) --*

          Represents the output of one of the following operations:
          * ``AuthorizeCacheSecurityGroupIngress``
          * ``CreateCacheSecurityGroup``
          * ``RevokeCacheSecurityGroupIngress``
          - **OwnerId** *(string) --*

            The AWS account ID of the cache security group owner.
    """


_DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef(
    _DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef = TypedDict(
    "_DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)


class DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef(
    _DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef
):
    pass


_DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef = TypedDict(
    "_DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef],
    },
    total=False,
)


class DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef(
    _DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef
):
    """
    - *(dict) --*

      Represents the output of one of the following operations:
      * ``CreateCacheSubnetGroup``
      * ``ModifyCacheSubnetGroup``
      - **CacheSubnetGroupName** *(string) --*

        The name of the cache subnet group.
    """


_DescribeCacheSubnetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeCacheSubnetGroupsPaginateResponseTypeDef",
    {
        "CacheSubnetGroups": List[
            DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeCacheSubnetGroupsPaginateResponseTypeDef(
    _DescribeCacheSubnetGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeCacheSubnetGroups`` operation.
      - **CacheSubnetGroups** *(list) --*

        A list of cache subnet groups. Each element in the list contains detailed information about
        one group.
        - *(dict) --*

          Represents the output of one of the following operations:
          * ``CreateCacheSubnetGroup``
          * ``ModifyCacheSubnetGroup``
          - **CacheSubnetGroupName** *(string) --*

            The name of the cache subnet group.
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


_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)


class DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef(
    _DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
):
    pass


_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef",
    {
        "ParameterName": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "CacheNodeTypeSpecificValues": List[
            DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
        ],
        "ChangeType": Literal["immediate", "requires-reboot"],
    },
    total=False,
)


class DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef(
    _DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef
):
    pass


_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ChangeType": Literal["immediate", "requires-reboot"],
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
        "CacheParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef
        ],
        "CacheNodeTypeSpecificParameters": List[
            DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef
        ],
    },
    total=False,
)


class DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef(
    _DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef
):
    """
    - **EngineDefaults** *(dict) --*

      Represents the output of a ``DescribeEngineDefaultParameters`` operation.
      - **CacheParameterGroupFamily** *(string) --*

        Specifies the name of the cache parameter group family to which the engine default
        parameters apply.
        Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
        ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |
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

        Represents the output of a ``DescribeEngineDefaultParameters`` operation.
        - **CacheParameterGroupFamily** *(string) --*

          Specifies the name of the cache parameter group family to which the engine default
          parameters apply.
          Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8``
          |
          ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |
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
            "cache-cluster",
            "cache-parameter-group",
            "cache-security-group",
            "cache-subnet-group",
            "replication-group",
        ],
        "Message": str,
        "Date": datetime,
    },
    total=False,
)


class DescribeEventsPaginateResponseEventsTypeDef(_DescribeEventsPaginateResponseEventsTypeDef):
    """
    - *(dict) --*

      Represents a single occurrence of something interesting within the system. Some examples of
      events are creating a cluster, adding or removing a cache node, or rebooting a node.
      - **SourceIdentifier** *(string) --*

        The identifier for the source of the event. For example, if the event occurred at the
        cluster level, the identifier would be the name of the cluster.
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"Events": List[DescribeEventsPaginateResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DescribeEvents`` operation.
      - **Events** *(list) --*

        A list of events. Each element in the list contains detailed information about one event.
        - *(dict) --*

          Represents a single occurrence of something interesting within the system. Some examples
          of events are creating a cluster, adding or removing a cache node, or rebooting a node.
          - **SourceIdentifier** *(string) --*

            The identifier for the source of the event. For example, if the event occurred at the
            cluster level, the identifier would be the name of the cluster.
    """


_DescribeReplicationGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReplicationGroupsPaginatePaginationConfigTypeDef(
    _DescribeReplicationGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef
):
    pass


_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    pass


_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef
):
    pass


_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef
):
    pass


_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef
):
    pass


_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef
):
    pass


_DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    pass


_DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef
):
    pass


_DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef
):
    pass


_DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef
):
    """
    - *(dict) --*

      Contains all of the attributes of a specific Redis replication group.
      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.
    """


_DescribeReplicationGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseTypeDef",
    {
        "ReplicationGroups": List[
            DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReplicationGroupsPaginateResponseTypeDef(
    _DescribeReplicationGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeReplicationGroups`` operation.
      - **ReplicationGroups** *(list) --*

        A list of replication groups. Each item in the list contains detailed information about one
        replication group.
        - *(dict) --*

          Contains all of the attributes of a specific Redis replication group.
          - **ReplicationGroupId** *(string) --*

            The identifier for the replication group.
    """


_DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef(
    _DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef = TypedDict(
    "_DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef(
    _DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef
):
    pass


_DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef = TypedDict(
    "_DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "ProductDescription": str,
        "OfferingType": str,
        "RecurringCharges": List[
            DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef
        ],
    },
    total=False,
)


class DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef(
    _DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef
):
    """
    - *(dict) --*

      Describes all of the attributes of a reserved cache node offering.
      - **ReservedCacheNodesOfferingId** *(string) --*

        A unique identifier for the reserved cache node offering.
    """


_DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef = TypedDict(
    "_DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef",
    {
        "ReservedCacheNodesOfferings": List[
            DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef(
    _DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeReservedCacheNodesOfferings`` operation.
      - **ReservedCacheNodesOfferings** *(list) --*

        A list of reserved cache node offerings. Each element in the list contains detailed
        information about one offering.
        - *(dict) --*

          Describes all of the attributes of a reserved cache node offering.
          - **ReservedCacheNodesOfferingId** *(string) --*

            A unique identifier for the reserved cache node offering.
    """


_DescribeReservedCacheNodesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReservedCacheNodesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReservedCacheNodesPaginatePaginationConfigTypeDef(
    _DescribeReservedCacheNodesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReservedCacheNodesPaginateResponseReservedCacheNodesRecurringChargesTypeDef = TypedDict(
    "_DescribeReservedCacheNodesPaginateResponseReservedCacheNodesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class DescribeReservedCacheNodesPaginateResponseReservedCacheNodesRecurringChargesTypeDef(
    _DescribeReservedCacheNodesPaginateResponseReservedCacheNodesRecurringChargesTypeDef
):
    pass


_DescribeReservedCacheNodesPaginateResponseReservedCacheNodesTypeDef = TypedDict(
    "_DescribeReservedCacheNodesPaginateResponseReservedCacheNodesTypeDef",
    {
        "ReservedCacheNodeId": str,
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CacheNodeCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "State": str,
        "RecurringCharges": List[
            DescribeReservedCacheNodesPaginateResponseReservedCacheNodesRecurringChargesTypeDef
        ],
        "ReservationARN": str,
    },
    total=False,
)


class DescribeReservedCacheNodesPaginateResponseReservedCacheNodesTypeDef(
    _DescribeReservedCacheNodesPaginateResponseReservedCacheNodesTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``PurchaseReservedCacheNodesOffering`` operation.
      - **ReservedCacheNodeId** *(string) --*

        The unique identifier for the reservation.
    """


_DescribeReservedCacheNodesPaginateResponseTypeDef = TypedDict(
    "_DescribeReservedCacheNodesPaginateResponseTypeDef",
    {
        "ReservedCacheNodes": List[
            DescribeReservedCacheNodesPaginateResponseReservedCacheNodesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReservedCacheNodesPaginateResponseTypeDef(
    _DescribeReservedCacheNodesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeReservedCacheNodes`` operation.
      - **ReservedCacheNodes** *(list) --*

        A list of reserved cache nodes. Each element in the list contains detailed information about
        one node.
        - *(dict) --*

          Represents the output of a ``PurchaseReservedCacheNodesOffering`` operation.
          - **ReservedCacheNodeId** *(string) --*

            The unique identifier for the reservation.
    """


_DescribeServiceUpdatesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeServiceUpdatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeServiceUpdatesPaginatePaginationConfigTypeDef(
    _DescribeServiceUpdatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef = TypedDict(
    "_DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef",
    {
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateEndDate": datetime,
        "ServiceUpdateSeverity": Literal["critical", "important", "medium", "low"],
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateStatus": Literal["available", "cancelled", "expired"],
        "ServiceUpdateDescription": str,
        "ServiceUpdateType": str,
        "Engine": str,
        "EngineVersion": str,
        "AutoUpdateAfterRecommendedApplyByDate": bool,
        "EstimatedUpdateTime": str,
    },
    total=False,
)


class DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef(
    _DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef
):
    """
    - *(dict) --*

      An update that you can apply to your Redis clusters.
      - **ServiceUpdateName** *(string) --*

        The unique ID of the service update
    """


_DescribeServiceUpdatesPaginateResponseTypeDef = TypedDict(
    "_DescribeServiceUpdatesPaginateResponseTypeDef",
    {
        "ServiceUpdates": List[DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeServiceUpdatesPaginateResponseTypeDef(_DescribeServiceUpdatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ServiceUpdates** *(list) --*

        A list of service updates
        - *(dict) --*

          An update that you can apply to your Redis clusters.
          - **ServiceUpdateName** *(string) --*

            The unique ID of the service update
    """


_DescribeSnapshotsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSnapshotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSnapshotsPaginatePaginationConfigTypeDef(
    _DescribeSnapshotsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "_DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)


class DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef(
    _DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef
):
    pass


_DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef = TypedDict(
    "_DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)


class DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef(
    _DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef
):
    pass


_DescribeSnapshotsPaginateResponseSnapshotsTypeDef = TypedDict(
    "_DescribeSnapshotsPaginateResponseSnapshotsTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "NodeSnapshots": List[DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)


class DescribeSnapshotsPaginateResponseSnapshotsTypeDef(
    _DescribeSnapshotsPaginateResponseSnapshotsTypeDef
):
    """
    - *(dict) --*

      Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.
      - **SnapshotName** *(string) --*

        The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
        manual snapshot, this is the user-provided name.
    """


_DescribeSnapshotsPaginateResponseTypeDef = TypedDict(
    "_DescribeSnapshotsPaginateResponseTypeDef",
    {"Snapshots": List[DescribeSnapshotsPaginateResponseSnapshotsTypeDef], "NextToken": str},
    total=False,
)


class DescribeSnapshotsPaginateResponseTypeDef(_DescribeSnapshotsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DescribeSnapshots`` operation.
      - **Snapshots** *(list) --*

        A list of snapshots. Each item in the list contains detailed information about one snapshot.
        - *(dict) --*

          Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.
          - **SnapshotName** *(string) --*

            The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
            manual snapshot, this is the user-provided name.
    """


_DescribeUpdateActionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeUpdateActionsPaginatePaginationConfigTypeDef(
    _DescribeUpdateActionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef",
    {
        "CacheNodeId": str,
        "NodeUpdateStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": Literal["system", "customer"],
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)


class DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef(
    _DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef
):
    pass


_DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "NodeUpdateStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": Literal["system", "customer"],
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)


class DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef(
    _DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef
):
    pass


_DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef",
    {
        "NodeGroupId": str,
        "NodeGroupMemberUpdateStatus": List[
            DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef
        ],
    },
    total=False,
)


class DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef(
    _DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef
):
    pass


_DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateSeverity": Literal["critical", "important", "medium", "low"],
        "ServiceUpdateStatus": Literal["available", "cancelled", "expired"],
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateType": str,
        "UpdateActionAvailableDate": datetime,
        "UpdateActionStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
        "NodesUpdated": str,
        "UpdateActionStatusModifiedDate": datetime,
        "SlaMet": Literal["yes", "no", "n/a"],
        "NodeGroupUpdateStatus": List[
            DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef
        ],
        "CacheNodeUpdateStatus": List[
            DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef
        ],
        "EstimatedUpdateTime": str,
        "Engine": str,
    },
    total=False,
)


class DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef(
    _DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef
):
    """
    - *(dict) --*

      The status of the service update for a specific replication group
      - **ReplicationGroupId** *(string) --*

        The ID of the replication group
    """


_DescribeUpdateActionsPaginateResponseTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginateResponseTypeDef",
    {
        "UpdateActions": List[DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeUpdateActionsPaginateResponseTypeDef(_DescribeUpdateActionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **UpdateActions** *(list) --*

        Returns a list of update actions
        - *(dict) --*

          The status of the service update for a specific replication group
          - **ReplicationGroupId** *(string) --*

            The ID of the replication group
    """


_DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)


class DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef(
    _DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef
):
    """
    The range of time specified to search for service updates that are in available status
    - **StartTime** *(datetime) --*

      The start time of the time range filter
    """


_ReplicationGroupAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationGroupAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationGroupAvailableWaitWaiterConfigTypeDef(
    _ReplicationGroupAvailableWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_ReplicationGroupDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationGroupDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationGroupDeletedWaitWaiterConfigTypeDef(
    _ReplicationGroupDeletedWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """
