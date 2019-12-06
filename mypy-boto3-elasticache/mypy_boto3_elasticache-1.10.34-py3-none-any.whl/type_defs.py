"Main interface for elasticache service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


CacheClusterAvailableWaitWaiterConfigTypeDef = TypedDict(
    "CacheClusterAvailableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

CacheClusterDeletedWaitWaiterConfigTypeDef = TypedDict(
    "CacheClusterDeletedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

ClientAddTagsToResourceResponseTagListTypeDef = TypedDict(
    "ClientAddTagsToResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientAddTagsToResourceResponseTypeDef = TypedDict(
    "ClientAddTagsToResourceResponseTypeDef",
    {"TagList": List[ClientAddTagsToResourceResponseTagListTypeDef]},
    total=False,
)

ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)

ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef = TypedDict(
    "ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
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

ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef = TypedDict(
    "ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef",
    {
        "CacheSecurityGroup": ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef
    },
    total=False,
)

ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef = TypedDict(
    "ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef",
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

ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef = TypedDict(
    "ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ErrorType": str,
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchApplyUpdateActionResponseTypeDef = TypedDict(
    "ClientBatchApplyUpdateActionResponseTypeDef",
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

ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef = TypedDict(
    "ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef",
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

ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef = TypedDict(
    "ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ErrorType": str,
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchStopUpdateActionResponseTypeDef = TypedDict(
    "ClientBatchStopUpdateActionResponseTypeDef",
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

ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef",
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

ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupTypeDef",
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

ClientCompleteMigrationResponseTypeDef = TypedDict(
    "ClientCompleteMigrationResponseTypeDef",
    {"ReplicationGroup": ClientCompleteMigrationResponseReplicationGroupTypeDef},
    total=False,
)

ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)

ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef = TypedDict(
    "ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef",
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

ClientCopySnapshotResponseSnapshotTypeDef = TypedDict(
    "ClientCopySnapshotResponseSnapshotTypeDef",
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

ClientCopySnapshotResponseTypeDef = TypedDict(
    "ClientCopySnapshotResponseTypeDef",
    {"Snapshot": ClientCopySnapshotResponseSnapshotTypeDef},
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef",
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

ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterTypeDef",
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

ClientCreateCacheClusterResponseTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseTypeDef",
    {"CacheCluster": ClientCreateCacheClusterResponseCacheClusterTypeDef},
    total=False,
)

ClientCreateCacheClusterTagsTypeDef = TypedDict(
    "ClientCreateCacheClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef = TypedDict(
    "ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef",
    {"CacheParameterGroupName": str, "CacheParameterGroupFamily": str, "Description": str},
    total=False,
)

ClientCreateCacheParameterGroupResponseTypeDef = TypedDict(
    "ClientCreateCacheParameterGroupResponseTypeDef",
    {"CacheParameterGroup": ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef},
    total=False,
)

ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)

ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef = TypedDict(
    "ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef",
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

ClientCreateCacheSecurityGroupResponseTypeDef = TypedDict(
    "ClientCreateCacheSecurityGroupResponseTypeDef",
    {"CacheSecurityGroup": ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef},
    total=False,
)

ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)

ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef = TypedDict(
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef],
    },
    total=False,
)

ClientCreateCacheSubnetGroupResponseTypeDef = TypedDict(
    "ClientCreateCacheSubnetGroupResponseTypeDef",
    {"CacheSubnetGroup": ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef},
    total=False,
)

ClientCreateReplicationGroupNodeGroupConfigurationTypeDef = TypedDict(
    "ClientCreateReplicationGroupNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
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

ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupTypeDef",
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

ClientCreateReplicationGroupResponseTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseTypeDef",
    {"ReplicationGroup": ClientCreateReplicationGroupResponseReplicationGroupTypeDef},
    total=False,
)

ClientCreateReplicationGroupTagsTypeDef = TypedDict(
    "ClientCreateReplicationGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)

ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef = TypedDict(
    "ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef",
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

ClientCreateSnapshotResponseSnapshotTypeDef = TypedDict(
    "ClientCreateSnapshotResponseSnapshotTypeDef",
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

ClientCreateSnapshotResponseTypeDef = TypedDict(
    "ClientCreateSnapshotResponseTypeDef",
    {"Snapshot": ClientCreateSnapshotResponseSnapshotTypeDef},
    total=False,
)

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
    pass


ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
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

ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupTypeDef",
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

ClientDecreaseReplicaCountResponseTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseTypeDef",
    {"ReplicationGroup": ClientDecreaseReplicaCountResponseReplicationGroupTypeDef},
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef",
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

ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterTypeDef",
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

ClientDeleteCacheClusterResponseTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseTypeDef",
    {"CacheCluster": ClientDeleteCacheClusterResponseCacheClusterTypeDef},
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
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

ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupTypeDef",
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

ClientDeleteReplicationGroupResponseTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseTypeDef",
    {"ReplicationGroup": ClientDeleteReplicationGroupResponseReplicationGroupTypeDef},
    total=False,
)

ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)

ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef = TypedDict(
    "ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef",
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

ClientDeleteSnapshotResponseSnapshotTypeDef = TypedDict(
    "ClientDeleteSnapshotResponseSnapshotTypeDef",
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

ClientDeleteSnapshotResponseTypeDef = TypedDict(
    "ClientDeleteSnapshotResponseTypeDef",
    {"Snapshot": ClientDeleteSnapshotResponseSnapshotTypeDef},
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef",
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

ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersTypeDef",
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

ClientDescribeCacheClustersResponseTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseTypeDef",
    {"Marker": str, "CacheClusters": List[ClientDescribeCacheClustersResponseCacheClustersTypeDef]},
    total=False,
)

ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef = TypedDict(
    "ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupFamily": str,
        "CacheEngineDescription": str,
        "CacheEngineVersionDescription": str,
    },
    total=False,
)

ClientDescribeCacheEngineVersionsResponseTypeDef = TypedDict(
    "ClientDescribeCacheEngineVersionsResponseTypeDef",
    {
        "Marker": str,
        "CacheEngineVersions": List[
            ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef = TypedDict(
    "ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef",
    {"CacheParameterGroupName": str, "CacheParameterGroupFamily": str, "Description": str},
    total=False,
)

ClientDescribeCacheParameterGroupsResponseTypeDef = TypedDict(
    "ClientDescribeCacheParameterGroupsResponseTypeDef",
    {
        "Marker": str,
        "CacheParameterGroups": List[
            ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef
        ],
    },
    total=False,
)

ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)

ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef",
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

ClientDescribeCacheParametersResponseParametersTypeDef = TypedDict(
    "ClientDescribeCacheParametersResponseParametersTypeDef",
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

ClientDescribeCacheParametersResponseTypeDef = TypedDict(
    "ClientDescribeCacheParametersResponseTypeDef",
    {
        "Marker": str,
        "Parameters": List[ClientDescribeCacheParametersResponseParametersTypeDef],
        "CacheNodeTypeSpecificParameters": List[
            ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef
        ],
    },
    total=False,
)

ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef = TypedDict(
    "ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)

ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef",
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

ClientDescribeCacheSecurityGroupsResponseTypeDef = TypedDict(
    "ClientDescribeCacheSecurityGroupsResponseTypeDef",
    {
        "Marker": str,
        "CacheSecurityGroups": List[
            ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef
        ],
    },
    total=False,
)

ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef = TypedDict(
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)

ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef = TypedDict(
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef],
    },
    total=False,
)

ClientDescribeCacheSubnetGroupsResponseTypeDef = TypedDict(
    "ClientDescribeCacheSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "CacheSubnetGroups": List[ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef],
    },
    total=False,
)

ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)

ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef",
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

ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef",
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

ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef",
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

ClientDescribeEngineDefaultParametersResponseTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersResponseTypeDef",
    {"EngineDefaults": ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef},
    total=False,
)

ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "ClientDescribeEventsResponseEventsTypeDef",
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

ClientDescribeEventsResponseTypeDef = TypedDict(
    "ClientDescribeEventsResponseTypeDef",
    {"Marker": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef",
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

ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef",
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

ClientDescribeReplicationGroupsResponseTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationGroups": List[ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef],
    },
    total=False,
)

ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef = TypedDict(
    "ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef = TypedDict(
    "ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef",
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

ClientDescribeReservedCacheNodesOfferingsResponseTypeDef = TypedDict(
    "ClientDescribeReservedCacheNodesOfferingsResponseTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodesOfferings": List[
            ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef
        ],
    },
    total=False,
)

ClientDescribeReservedCacheNodesResponseReservedCacheNodesRecurringChargesTypeDef = TypedDict(
    "ClientDescribeReservedCacheNodesResponseReservedCacheNodesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientDescribeReservedCacheNodesResponseReservedCacheNodesTypeDef = TypedDict(
    "ClientDescribeReservedCacheNodesResponseReservedCacheNodesTypeDef",
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

ClientDescribeReservedCacheNodesResponseTypeDef = TypedDict(
    "ClientDescribeReservedCacheNodesResponseTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodes": List[
            ClientDescribeReservedCacheNodesResponseReservedCacheNodesTypeDef
        ],
    },
    total=False,
)

ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef = TypedDict(
    "ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef",
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

ClientDescribeServiceUpdatesResponseTypeDef = TypedDict(
    "ClientDescribeServiceUpdatesResponseTypeDef",
    {
        "Marker": str,
        "ServiceUpdates": List[ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef],
    },
    total=False,
)

ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)

ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef = TypedDict(
    "ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef",
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

ClientDescribeSnapshotsResponseSnapshotsTypeDef = TypedDict(
    "ClientDescribeSnapshotsResponseSnapshotsTypeDef",
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

ClientDescribeSnapshotsResponseTypeDef = TypedDict(
    "ClientDescribeSnapshotsResponseTypeDef",
    {"Marker": str, "Snapshots": List[ClientDescribeSnapshotsResponseSnapshotsTypeDef]},
    total=False,
)

ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef = TypedDict(
    "ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef",
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

ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef = TypedDict(
    "ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef",
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

ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef = TypedDict(
    "ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef",
    {
        "NodeGroupId": str,
        "NodeGroupMemberUpdateStatus": List[
            ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef
        ],
    },
    total=False,
)

ClientDescribeUpdateActionsResponseUpdateActionsTypeDef = TypedDict(
    "ClientDescribeUpdateActionsResponseUpdateActionsTypeDef",
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

ClientDescribeUpdateActionsResponseTypeDef = TypedDict(
    "ClientDescribeUpdateActionsResponseTypeDef",
    {"Marker": str, "UpdateActions": List[ClientDescribeUpdateActionsResponseUpdateActionsTypeDef]},
    total=False,
)

ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef = TypedDict(
    "ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)

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
    pass


ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
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

ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupTypeDef",
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

ClientIncreaseReplicaCountResponseTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseTypeDef",
    {"ReplicationGroup": ClientIncreaseReplicaCountResponseReplicationGroupTypeDef},
    total=False,
)

ClientListAllowedNodeTypeModificationsResponseTypeDef = TypedDict(
    "ClientListAllowedNodeTypeModificationsResponseTypeDef",
    {"ScaleUpModifications": List[str], "ScaleDownModifications": List[str]},
    total=False,
)

ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef",
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

ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterTypeDef",
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

ClientModifyCacheClusterResponseTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseTypeDef",
    {"CacheCluster": ClientModifyCacheClusterResponseCacheClusterTypeDef},
    total=False,
)

ClientModifyCacheParameterGroupParameterNameValuesTypeDef = TypedDict(
    "ClientModifyCacheParameterGroupParameterNameValuesTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)

ClientModifyCacheParameterGroupResponseTypeDef = TypedDict(
    "ClientModifyCacheParameterGroupResponseTypeDef", {"CacheParameterGroupName": str}, total=False
)

ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)

ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef = TypedDict(
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef],
    },
    total=False,
)

ClientModifyCacheSubnetGroupResponseTypeDef = TypedDict(
    "ClientModifyCacheSubnetGroupResponseTypeDef",
    {"CacheSubnetGroup": ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef},
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
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

ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupTypeDef",
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

ClientModifyReplicationGroupResponseTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseTypeDef",
    {"ReplicationGroup": ClientModifyReplicationGroupResponseReplicationGroupTypeDef},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef",
    {"NodeGroupId": str, "PreferredAvailabilityZones": List[str]},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef",
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

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef",
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

ClientModifyReplicationGroupShardConfigurationResponseTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseTypeDef",
    {
        "ReplicationGroup": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef
    },
    total=False,
)

ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef = TypedDict(
    "ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef = TypedDict(
    "ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef",
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

ClientPurchaseReservedCacheNodesOfferingResponseTypeDef = TypedDict(
    "ClientPurchaseReservedCacheNodesOfferingResponseTypeDef",
    {"ReservedCacheNode": ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef},
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef",
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

ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterTypeDef",
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

ClientRebootCacheClusterResponseTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseTypeDef",
    {"CacheCluster": ClientRebootCacheClusterResponseCacheClusterTypeDef},
    total=False,
)

ClientRemoveTagsFromResourceResponseTagListTypeDef = TypedDict(
    "ClientRemoveTagsFromResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRemoveTagsFromResourceResponseTypeDef = TypedDict(
    "ClientRemoveTagsFromResourceResponseTypeDef",
    {"TagList": List[ClientRemoveTagsFromResourceResponseTagListTypeDef]},
    total=False,
)

ClientResetCacheParameterGroupParameterNameValuesTypeDef = TypedDict(
    "ClientResetCacheParameterGroupParameterNameValuesTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)

ClientResetCacheParameterGroupResponseTypeDef = TypedDict(
    "ClientResetCacheParameterGroupResponseTypeDef", {"CacheParameterGroupName": str}, total=False
)

ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)

ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef = TypedDict(
    "ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
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

ClientRevokeCacheSecurityGroupIngressResponseTypeDef = TypedDict(
    "ClientRevokeCacheSecurityGroupIngressResponseTypeDef",
    {"CacheSecurityGroup": ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef},
    total=False,
)

ClientStartMigrationCustomerNodeEndpointListTypeDef = TypedDict(
    "ClientStartMigrationCustomerNodeEndpointListTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef",
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

ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientStartMigrationResponseReplicationGroupTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupTypeDef",
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

ClientStartMigrationResponseTypeDef = TypedDict(
    "ClientStartMigrationResponseTypeDef",
    {"ReplicationGroup": ClientStartMigrationResponseReplicationGroupTypeDef},
    total=False,
)

ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef",
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

ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientTestFailoverResponseReplicationGroupTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupTypeDef",
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

ClientTestFailoverResponseTypeDef = TypedDict(
    "ClientTestFailoverResponseTypeDef",
    {"ReplicationGroup": ClientTestFailoverResponseReplicationGroupTypeDef},
    total=False,
)

DescribeCacheClustersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeCacheClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef = TypedDict(
    "DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef = TypedDict(
    "DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef",
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

DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef = TypedDict(
    "DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef = TypedDict(
    "DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)

DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef = TypedDict(
    "DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef = TypedDict(
    "DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef = TypedDict(
    "DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef = TypedDict(
    "DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)

DescribeCacheClustersPaginateResponseCacheClustersTypeDef = TypedDict(
    "DescribeCacheClustersPaginateResponseCacheClustersTypeDef",
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

DescribeCacheClustersPaginateResponseTypeDef = TypedDict(
    "DescribeCacheClustersPaginateResponseTypeDef",
    {
        "CacheClusters": List[DescribeCacheClustersPaginateResponseCacheClustersTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef = TypedDict(
    "DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupFamily": str,
        "CacheEngineDescription": str,
        "CacheEngineVersionDescription": str,
    },
    total=False,
)

DescribeCacheEngineVersionsPaginateResponseTypeDef = TypedDict(
    "DescribeCacheEngineVersionsPaginateResponseTypeDef",
    {
        "CacheEngineVersions": List[
            DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef = TypedDict(
    "DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef",
    {"CacheParameterGroupName": str, "CacheParameterGroupFamily": str, "Description": str},
    total=False,
)

DescribeCacheParameterGroupsPaginateResponseTypeDef = TypedDict(
    "DescribeCacheParameterGroupsPaginateResponseTypeDef",
    {
        "CacheParameterGroups": List[
            DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeCacheParametersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeCacheParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)

DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef",
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

DescribeCacheParametersPaginateResponseParametersTypeDef = TypedDict(
    "DescribeCacheParametersPaginateResponseParametersTypeDef",
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

DescribeCacheParametersPaginateResponseTypeDef = TypedDict(
    "DescribeCacheParametersPaginateResponseTypeDef",
    {
        "Parameters": List[DescribeCacheParametersPaginateResponseParametersTypeDef],
        "CacheNodeTypeSpecificParameters": List[
            DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef = TypedDict(
    "DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)

DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef = TypedDict(
    "DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef",
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

DescribeCacheSecurityGroupsPaginateResponseTypeDef = TypedDict(
    "DescribeCacheSecurityGroupsPaginateResponseTypeDef",
    {
        "CacheSecurityGroups": List[
            DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef = TypedDict(
    "DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)

DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef = TypedDict(
    "DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef],
    },
    total=False,
)

DescribeCacheSubnetGroupsPaginateResponseTypeDef = TypedDict(
    "DescribeCacheSubnetGroupsPaginateResponseTypeDef",
    {
        "CacheSubnetGroups": List[
            DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)

DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef",
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

DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef = TypedDict(
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef",
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

DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef = TypedDict(
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef",
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

DescribeEngineDefaultParametersPaginateResponseTypeDef = TypedDict(
    "DescribeEngineDefaultParametersPaginateResponseTypeDef",
    {
        "EngineDefaults": DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef,
        "NextToken": str,
    },
    total=False,
)

DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeEventsPaginateResponseEventsTypeDef = TypedDict(
    "DescribeEventsPaginateResponseEventsTypeDef",
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

DescribeEventsPaginateResponseTypeDef = TypedDict(
    "DescribeEventsPaginateResponseTypeDef",
    {"Events": List[DescribeEventsPaginateResponseEventsTypeDef], "NextToken": str},
    total=False,
)

DescribeReplicationGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeReplicationGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef = TypedDict(
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef = TypedDict(
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef = TypedDict(
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef",
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

DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef = TypedDict(
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef = TypedDict(
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef = TypedDict(
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef",
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

DescribeReplicationGroupsPaginateResponseTypeDef = TypedDict(
    "DescribeReplicationGroupsPaginateResponseTypeDef",
    {
        "ReplicationGroups": List[
            DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef = TypedDict(
    "DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef = TypedDict(
    "DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef",
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

DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef = TypedDict(
    "DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef",
    {
        "ReservedCacheNodesOfferings": List[
            DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeReservedCacheNodesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeReservedCacheNodesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeReservedCacheNodesPaginateResponseReservedCacheNodesRecurringChargesTypeDef = TypedDict(
    "DescribeReservedCacheNodesPaginateResponseReservedCacheNodesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

DescribeReservedCacheNodesPaginateResponseReservedCacheNodesTypeDef = TypedDict(
    "DescribeReservedCacheNodesPaginateResponseReservedCacheNodesTypeDef",
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

DescribeReservedCacheNodesPaginateResponseTypeDef = TypedDict(
    "DescribeReservedCacheNodesPaginateResponseTypeDef",
    {
        "ReservedCacheNodes": List[
            DescribeReservedCacheNodesPaginateResponseReservedCacheNodesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeServiceUpdatesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeServiceUpdatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef = TypedDict(
    "DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef",
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

DescribeServiceUpdatesPaginateResponseTypeDef = TypedDict(
    "DescribeServiceUpdatesPaginateResponseTypeDef",
    {
        "ServiceUpdates": List[DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeSnapshotsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeSnapshotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)

DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef = TypedDict(
    "DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef",
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

DescribeSnapshotsPaginateResponseSnapshotsTypeDef = TypedDict(
    "DescribeSnapshotsPaginateResponseSnapshotsTypeDef",
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

DescribeSnapshotsPaginateResponseTypeDef = TypedDict(
    "DescribeSnapshotsPaginateResponseTypeDef",
    {"Snapshots": List[DescribeSnapshotsPaginateResponseSnapshotsTypeDef], "NextToken": str},
    total=False,
)

DescribeUpdateActionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeUpdateActionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef = TypedDict(
    "DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef",
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

DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef = TypedDict(
    "DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef",
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

DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef = TypedDict(
    "DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef",
    {
        "NodeGroupId": str,
        "NodeGroupMemberUpdateStatus": List[
            DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef
        ],
    },
    total=False,
)

DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef = TypedDict(
    "DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef",
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

DescribeUpdateActionsPaginateResponseTypeDef = TypedDict(
    "DescribeUpdateActionsPaginateResponseTypeDef",
    {
        "UpdateActions": List[DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef = TypedDict(
    "DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)

ReplicationGroupAvailableWaitWaiterConfigTypeDef = TypedDict(
    "ReplicationGroupAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)

ReplicationGroupDeletedWaitWaiterConfigTypeDef = TypedDict(
    "ReplicationGroupDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)
