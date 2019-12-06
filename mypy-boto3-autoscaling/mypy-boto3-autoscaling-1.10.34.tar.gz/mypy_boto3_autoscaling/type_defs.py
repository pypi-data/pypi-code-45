"Main interface for autoscaling service type defs"
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


ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef = TypedDict(
    "ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef",
    {"ScheduledActionName": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchDeleteScheduledActionResponseTypeDef = TypedDict(
    "ClientBatchDeleteScheduledActionResponseTypeDef",
    {
        "FailedScheduledActions": List[
            ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef
        ]
    },
    total=False,
)

ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef = TypedDict(
    "ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef",
    {"ScheduledActionName": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchPutScheduledUpdateGroupActionResponseTypeDef = TypedDict(
    "ClientBatchPutScheduledUpdateGroupActionResponseTypeDef",
    {
        "FailedScheduledUpdateGroupActions": List[
            ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef
        ]
    },
    total=False,
)

_RequiredClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef = TypedDict(
    "_RequiredClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef",
    {"ScheduledActionName": str},
)
_OptionalClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef = TypedDict(
    "_OptionalClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
    },
    total=False,
)


class ClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef(
    _RequiredClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef,
    _OptionalClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef,
):
    pass


ClientCreateAutoScalingGroupLaunchTemplateTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

_RequiredClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef = TypedDict(
    "_RequiredClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef",
    {"LifecycleHookName": str},
)
_OptionalClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef = TypedDict(
    "_OptionalClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef",
    {
        "LifecycleTransition": str,
        "NotificationMetadata": str,
        "HeartbeatTimeout": int,
        "DefaultResult": str,
        "NotificationTargetARN": str,
        "RoleARN": str,
    },
    total=False,
)


class ClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef(
    _RequiredClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef,
    _OptionalClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef,
):
    pass


ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)

ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)

ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)

ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)

ClientCreateAutoScalingGroupTagsTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef = TypedDict(
    "ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef",
    {
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
        "DeleteOnTermination": bool,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)

ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef = TypedDict(
    "ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef",
    {
        "VirtualName": str,
        "DeviceName": str,
        "Ebs": ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef,
        "NoDevice": bool,
    },
    total=False,
)

ClientCreateLaunchConfigurationInstanceMonitoringTypeDef = TypedDict(
    "ClientCreateLaunchConfigurationInstanceMonitoringTypeDef", {"Enabled": bool}, total=False
)

ClientCreateOrUpdateTagsTagsTypeDef = TypedDict(
    "ClientCreateOrUpdateTagsTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

ClientDeleteTagsTagsTypeDef = TypedDict(
    "ClientDeleteTagsTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

ClientDescribeAccountLimitsResponseTypeDef = TypedDict(
    "ClientDescribeAccountLimitsResponseTypeDef",
    {
        "MaxNumberOfAutoScalingGroups": int,
        "MaxNumberOfLaunchConfigurations": int,
        "NumberOfAutoScalingGroups": int,
        "NumberOfLaunchConfigurations": int,
    },
    total=False,
)

ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef = TypedDict(
    "ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef",
    {"AdjustmentType": str},
    total=False,
)

ClientDescribeAdjustmentTypesResponseTypeDef = TypedDict(
    "ClientDescribeAdjustmentTypesResponseTypeDef",
    {"AdjustmentTypes": List[ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef]},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef",
    {"Metric": str, "Granularity": str},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "AvailabilityZone": str,
        "LifecycleState": Literal[
            "Pending",
            "Pending:Wait",
            "Pending:Proceed",
            "Quarantined",
            "InService",
            "Terminating",
            "Terminating:Wait",
            "Terminating:Proceed",
            "Terminated",
            "Detaching",
            "Detached",
            "EnteringStandby",
            "Standby",
        ],
        "HealthStatus": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef,
        "ProtectedFromScaleIn": bool,
        "WeightedCapacity": str,
    },
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef",
    {"ProcessName": str, "SuspensionReason": str},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef",
    {
        "AutoScalingGroupName": str,
        "AutoScalingGroupARN": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef,
        "MixedInstancesPolicy": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "LoadBalancerNames": List[str],
        "TargetGroupARNs": List[str],
        "HealthCheckType": str,
        "HealthCheckGracePeriod": int,
        "Instances": List[ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef],
        "CreatedTime": datetime,
        "SuspendedProcesses": List[
            ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef
        ],
        "PlacementGroup": str,
        "VPCZoneIdentifier": str,
        "EnabledMetrics": List[
            ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef
        ],
        "Status": str,
        "Tags": List[ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef],
        "TerminationPolicies": List[str],
        "NewInstancesProtectedFromScaleIn": bool,
        "ServiceLinkedRoleARN": str,
        "MaxInstanceLifetime": int,
    },
    total=False,
)

ClientDescribeAutoScalingGroupsResponseTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseTypeDef",
    {
        "AutoScalingGroups": List[ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef = TypedDict(
    "ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef = TypedDict(
    "ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "AutoScalingGroupName": str,
        "AvailabilityZone": str,
        "LifecycleState": str,
        "HealthStatus": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef,
        "ProtectedFromScaleIn": bool,
        "WeightedCapacity": str,
    },
    total=False,
)

ClientDescribeAutoScalingInstancesResponseTypeDef = TypedDict(
    "ClientDescribeAutoScalingInstancesResponseTypeDef",
    {
        "AutoScalingInstances": List[
            ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeAutoScalingNotificationTypesResponseTypeDef = TypedDict(
    "ClientDescribeAutoScalingNotificationTypesResponseTypeDef",
    {"AutoScalingNotificationTypes": List[str]},
    total=False,
)

ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef = TypedDict(
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef",
    {
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
        "DeleteOnTermination": bool,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)

ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef = TypedDict(
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef",
    {
        "VirtualName": str,
        "DeviceName": str,
        "Ebs": ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef,
        "NoDevice": bool,
    },
    total=False,
)

ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef = TypedDict(
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef = TypedDict(
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef",
    {
        "LaunchConfigurationName": str,
        "LaunchConfigurationARN": str,
        "ImageId": str,
        "KeyName": str,
        "SecurityGroups": List[str],
        "ClassicLinkVPCId": str,
        "ClassicLinkVPCSecurityGroups": List[str],
        "UserData": str,
        "InstanceType": str,
        "KernelId": str,
        "RamdiskId": str,
        "BlockDeviceMappings": List[
            ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef
        ],
        "InstanceMonitoring": ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef,
        "SpotPrice": str,
        "IamInstanceProfile": str,
        "CreatedTime": datetime,
        "EbsOptimized": bool,
        "AssociatePublicIpAddress": bool,
        "PlacementTenancy": str,
    },
    total=False,
)

ClientDescribeLaunchConfigurationsResponseTypeDef = TypedDict(
    "ClientDescribeLaunchConfigurationsResponseTypeDef",
    {
        "LaunchConfigurations": List[
            ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeLifecycleHookTypesResponseTypeDef = TypedDict(
    "ClientDescribeLifecycleHookTypesResponseTypeDef",
    {"LifecycleHookTypes": List[str]},
    total=False,
)

ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef = TypedDict(
    "ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
        "LifecycleTransition": str,
        "NotificationTargetARN": str,
        "RoleARN": str,
        "NotificationMetadata": str,
        "HeartbeatTimeout": int,
        "GlobalTimeout": int,
        "DefaultResult": str,
    },
    total=False,
)

ClientDescribeLifecycleHooksResponseTypeDef = TypedDict(
    "ClientDescribeLifecycleHooksResponseTypeDef",
    {"LifecycleHooks": List[ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef]},
    total=False,
)

ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef = TypedDict(
    "ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef",
    {"LoadBalancerTargetGroupARN": str, "State": str},
    total=False,
)

ClientDescribeLoadBalancerTargetGroupsResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancerTargetGroupsResponseTypeDef",
    {
        "LoadBalancerTargetGroups": List[
            ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancersTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancersTypeDef",
    {"LoadBalancerName": str, "State": str},
    total=False,
)

ClientDescribeLoadBalancersResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancers": List[ClientDescribeLoadBalancersResponseLoadBalancersTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef = TypedDict(
    "ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef",
    {"Granularity": str},
    total=False,
)

ClientDescribeMetricCollectionTypesResponseMetricsTypeDef = TypedDict(
    "ClientDescribeMetricCollectionTypesResponseMetricsTypeDef", {"Metric": str}, total=False
)

ClientDescribeMetricCollectionTypesResponseTypeDef = TypedDict(
    "ClientDescribeMetricCollectionTypesResponseTypeDef",
    {
        "Metrics": List[ClientDescribeMetricCollectionTypesResponseMetricsTypeDef],
        "Granularities": List[ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef],
    },
    total=False,
)

ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef = TypedDict(
    "ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef",
    {"AutoScalingGroupName": str, "TopicARN": str, "NotificationType": str},
    total=False,
)

ClientDescribeNotificationConfigurationsResponseTypeDef = TypedDict(
    "ClientDescribeNotificationConfigurationsResponseTypeDef",
    {
        "NotificationConfigurations": List[
            ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "ALBRequestCountPerTarget",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
    },
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "PolicyARN": str,
        "PolicyType": str,
        "AdjustmentType": str,
        "MinAdjustmentStep": int,
        "MinAdjustmentMagnitude": int,
        "ScalingAdjustment": int,
        "Cooldown": int,
        "StepAdjustments": List[
            ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef
        ],
        "MetricAggregationType": str,
        "EstimatedInstanceWarmup": int,
        "Alarms": List[ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef],
        "TargetTrackingConfiguration": ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef,
    },
    total=False,
)

ClientDescribePoliciesResponseTypeDef = TypedDict(
    "ClientDescribePoliciesResponseTypeDef",
    {
        "ScalingPolicies": List[ClientDescribePoliciesResponseScalingPoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeScalingActivitiesResponseActivitiesTypeDef = TypedDict(
    "ClientDescribeScalingActivitiesResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "PendingSpotBidPlacement",
            "WaitingForSpotInstanceRequestId",
            "WaitingForSpotInstanceId",
            "WaitingForInstanceId",
            "PreInService",
            "InProgress",
            "WaitingForELBConnectionDraining",
            "MidLifecycleAction",
            "WaitingForInstanceWarmup",
            "Successful",
            "Failed",
            "Cancelled",
        ],
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)

ClientDescribeScalingActivitiesResponseTypeDef = TypedDict(
    "ClientDescribeScalingActivitiesResponseTypeDef",
    {
        "Activities": List[ClientDescribeScalingActivitiesResponseActivitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeScalingProcessTypesResponseProcessesTypeDef = TypedDict(
    "ClientDescribeScalingProcessTypesResponseProcessesTypeDef", {"ProcessName": str}, total=False
)

ClientDescribeScalingProcessTypesResponseTypeDef = TypedDict(
    "ClientDescribeScalingProcessTypesResponseTypeDef",
    {"Processes": List[ClientDescribeScalingProcessTypesResponseProcessesTypeDef]},
    total=False,
)

ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "Time": datetime,
        "StartTime": datetime,
        "EndTime": datetime,
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
    },
    total=False,
)

ClientDescribeScheduledActionsResponseTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseTypeDef",
    {
        "ScheduledUpdateGroupActions": List[
            ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeTagsFiltersTypeDef = TypedDict(
    "ClientDescribeTagsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeTagsResponseTagsTypeDef = TypedDict(
    "ClientDescribeTagsResponseTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

ClientDescribeTagsResponseTypeDef = TypedDict(
    "ClientDescribeTagsResponseTypeDef",
    {"Tags": List[ClientDescribeTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeTerminationPolicyTypesResponseTypeDef = TypedDict(
    "ClientDescribeTerminationPolicyTypesResponseTypeDef",
    {"TerminationPolicyTypes": List[str]},
    total=False,
)

ClientDetachInstancesResponseActivitiesTypeDef = TypedDict(
    "ClientDetachInstancesResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "PendingSpotBidPlacement",
            "WaitingForSpotInstanceRequestId",
            "WaitingForSpotInstanceId",
            "WaitingForInstanceId",
            "PreInService",
            "InProgress",
            "WaitingForELBConnectionDraining",
            "MidLifecycleAction",
            "WaitingForInstanceWarmup",
            "Successful",
            "Failed",
            "Cancelled",
        ],
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)

ClientDetachInstancesResponseTypeDef = TypedDict(
    "ClientDetachInstancesResponseTypeDef",
    {"Activities": List[ClientDetachInstancesResponseActivitiesTypeDef]},
    total=False,
)

ClientEnterStandbyResponseActivitiesTypeDef = TypedDict(
    "ClientEnterStandbyResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "PendingSpotBidPlacement",
            "WaitingForSpotInstanceRequestId",
            "WaitingForSpotInstanceId",
            "WaitingForInstanceId",
            "PreInService",
            "InProgress",
            "WaitingForELBConnectionDraining",
            "MidLifecycleAction",
            "WaitingForInstanceWarmup",
            "Successful",
            "Failed",
            "Cancelled",
        ],
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)

ClientEnterStandbyResponseTypeDef = TypedDict(
    "ClientEnterStandbyResponseTypeDef",
    {"Activities": List[ClientEnterStandbyResponseActivitiesTypeDef]},
    total=False,
)

ClientExitStandbyResponseActivitiesTypeDef = TypedDict(
    "ClientExitStandbyResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "PendingSpotBidPlacement",
            "WaitingForSpotInstanceRequestId",
            "WaitingForSpotInstanceId",
            "WaitingForInstanceId",
            "PreInService",
            "InProgress",
            "WaitingForELBConnectionDraining",
            "MidLifecycleAction",
            "WaitingForInstanceWarmup",
            "Successful",
            "Failed",
            "Cancelled",
        ],
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)

ClientExitStandbyResponseTypeDef = TypedDict(
    "ClientExitStandbyResponseTypeDef",
    {"Activities": List[ClientExitStandbyResponseActivitiesTypeDef]},
    total=False,
)

ClientPutScalingPolicyResponseAlarmsTypeDef = TypedDict(
    "ClientPutScalingPolicyResponseAlarmsTypeDef", {"AlarmName": str, "AlarmARN": str}, total=False
)

ClientPutScalingPolicyResponseTypeDef = TypedDict(
    "ClientPutScalingPolicyResponseTypeDef",
    {"PolicyARN": str, "Alarms": List[ClientPutScalingPolicyResponseAlarmsTypeDef]},
    total=False,
)

ClientPutScalingPolicyStepAdjustmentsTypeDef = TypedDict(
    "ClientPutScalingPolicyStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)

ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

_RequiredClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "ALBRequestCountPerTarget",
        ]
    },
)
_OptionalClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    {"ResourceLabel": str},
    total=False,
)


class ClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef(
    _RequiredClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
    _OptionalClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
):
    pass


ClientPutScalingPolicyTargetTrackingConfigurationTypeDef = TypedDict(
    "ClientPutScalingPolicyTargetTrackingConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": ClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
    },
    total=False,
)

ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef = TypedDict(
    "ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "PendingSpotBidPlacement",
            "WaitingForSpotInstanceRequestId",
            "WaitingForSpotInstanceId",
            "WaitingForInstanceId",
            "PreInService",
            "InProgress",
            "WaitingForELBConnectionDraining",
            "MidLifecycleAction",
            "WaitingForInstanceWarmup",
            "Successful",
            "Failed",
            "Cancelled",
        ],
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)

ClientTerminateInstanceInAutoScalingGroupResponseTypeDef = TypedDict(
    "ClientTerminateInstanceInAutoScalingGroupResponseTypeDef",
    {"Activity": ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef},
    total=False,
)

ClientUpdateAutoScalingGroupLaunchTemplateTypeDef = TypedDict(
    "ClientUpdateAutoScalingGroupLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)

ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)

ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)

ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef = TypedDict(
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)

DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef",
    {"Metric": str, "Granularity": str},
    total=False,
)

DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "AvailabilityZone": str,
        "LifecycleState": Literal[
            "Pending",
            "Pending:Wait",
            "Pending:Proceed",
            "Quarantined",
            "InService",
            "Terminating",
            "Terminating:Wait",
            "Terminating:Proceed",
            "Terminated",
            "Detaching",
            "Detached",
            "EnteringStandby",
            "Standby",
        ],
        "HealthStatus": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef,
        "ProtectedFromScaleIn": bool,
        "WeightedCapacity": str,
    },
    total=False,
)

DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)

DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)

DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)

DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)

DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef",
    {"ProcessName": str, "SuspensionReason": str},
    total=False,
)

DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef",
    {
        "AutoScalingGroupName": str,
        "AutoScalingGroupARN": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef,
        "MixedInstancesPolicy": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "LoadBalancerNames": List[str],
        "TargetGroupARNs": List[str],
        "HealthCheckType": str,
        "HealthCheckGracePeriod": int,
        "Instances": List[
            DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef
        ],
        "CreatedTime": datetime,
        "SuspendedProcesses": List[
            DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef
        ],
        "PlacementGroup": str,
        "VPCZoneIdentifier": str,
        "EnabledMetrics": List[
            DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef
        ],
        "Status": str,
        "Tags": List[DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef],
        "TerminationPolicies": List[str],
        "NewInstancesProtectedFromScaleIn": bool,
        "ServiceLinkedRoleARN": str,
        "MaxInstanceLifetime": int,
    },
    total=False,
)

DescribeAutoScalingGroupsPaginateResponseTypeDef = TypedDict(
    "DescribeAutoScalingGroupsPaginateResponseTypeDef",
    {"AutoScalingGroups": List[DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef]},
    total=False,
)

DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef = TypedDict(
    "DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef = TypedDict(
    "DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "AutoScalingGroupName": str,
        "AvailabilityZone": str,
        "LifecycleState": str,
        "HealthStatus": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef,
        "ProtectedFromScaleIn": bool,
        "WeightedCapacity": str,
    },
    total=False,
)

DescribeAutoScalingInstancesPaginateResponseTypeDef = TypedDict(
    "DescribeAutoScalingInstancesPaginateResponseTypeDef",
    {
        "AutoScalingInstances": List[
            DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef
        ]
    },
    total=False,
)

DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef = TypedDict(
    "DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef",
    {
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
        "DeleteOnTermination": bool,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)

DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef = TypedDict(
    "DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef",
    {
        "VirtualName": str,
        "DeviceName": str,
        "Ebs": DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef,
        "NoDevice": bool,
    },
    total=False,
)

DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef = TypedDict(
    "DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef",
    {"Enabled": bool},
    total=False,
)

DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef = TypedDict(
    "DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef",
    {
        "LaunchConfigurationName": str,
        "LaunchConfigurationARN": str,
        "ImageId": str,
        "KeyName": str,
        "SecurityGroups": List[str],
        "ClassicLinkVPCId": str,
        "ClassicLinkVPCSecurityGroups": List[str],
        "UserData": str,
        "InstanceType": str,
        "KernelId": str,
        "RamdiskId": str,
        "BlockDeviceMappings": List[
            DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef
        ],
        "InstanceMonitoring": DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef,
        "SpotPrice": str,
        "IamInstanceProfile": str,
        "CreatedTime": datetime,
        "EbsOptimized": bool,
        "AssociatePublicIpAddress": bool,
        "PlacementTenancy": str,
    },
    total=False,
)

DescribeLaunchConfigurationsPaginateResponseTypeDef = TypedDict(
    "DescribeLaunchConfigurationsPaginateResponseTypeDef",
    {
        "LaunchConfigurations": List[
            DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef
        ]
    },
    total=False,
)

DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef = TypedDict(
    "DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef",
    {"LoadBalancerTargetGroupARN": str, "State": str},
    total=False,
)

DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef = TypedDict(
    "DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef",
    {
        "LoadBalancerTargetGroups": List[
            DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef
        ]
    },
    total=False,
)

DescribeLoadBalancersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeLoadBalancersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef = TypedDict(
    "DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef",
    {"LoadBalancerName": str, "State": str},
    total=False,
)

DescribeLoadBalancersPaginateResponseTypeDef = TypedDict(
    "DescribeLoadBalancersPaginateResponseTypeDef",
    {"LoadBalancers": List[DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef]},
    total=False,
)

DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef = TypedDict(
    "DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef",
    {"AutoScalingGroupName": str, "TopicARN": str, "NotificationType": str},
    total=False,
)

DescribeNotificationConfigurationsPaginateResponseTypeDef = TypedDict(
    "DescribeNotificationConfigurationsPaginateResponseTypeDef",
    {
        "NotificationConfigurations": List[
            DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef
        ]
    },
    total=False,
)

DescribePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)

DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef = TypedDict(
    "DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)

DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "ALBRequestCountPerTarget",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
    },
    total=False,
)

DescribePoliciesPaginateResponseScalingPoliciesTypeDef = TypedDict(
    "DescribePoliciesPaginateResponseScalingPoliciesTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "PolicyARN": str,
        "PolicyType": str,
        "AdjustmentType": str,
        "MinAdjustmentStep": int,
        "MinAdjustmentMagnitude": int,
        "ScalingAdjustment": int,
        "Cooldown": int,
        "StepAdjustments": List[
            DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef
        ],
        "MetricAggregationType": str,
        "EstimatedInstanceWarmup": int,
        "Alarms": List[DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef],
        "TargetTrackingConfiguration": DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef,
    },
    total=False,
)

DescribePoliciesPaginateResponseTypeDef = TypedDict(
    "DescribePoliciesPaginateResponseTypeDef",
    {"ScalingPolicies": List[DescribePoliciesPaginateResponseScalingPoliciesTypeDef]},
    total=False,
)

DescribeScalingActivitiesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeScalingActivitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeScalingActivitiesPaginateResponseActivitiesTypeDef = TypedDict(
    "DescribeScalingActivitiesPaginateResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "PendingSpotBidPlacement",
            "WaitingForSpotInstanceRequestId",
            "WaitingForSpotInstanceId",
            "WaitingForInstanceId",
            "PreInService",
            "InProgress",
            "WaitingForELBConnectionDraining",
            "MidLifecycleAction",
            "WaitingForInstanceWarmup",
            "Successful",
            "Failed",
            "Cancelled",
        ],
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)

DescribeScalingActivitiesPaginateResponseTypeDef = TypedDict(
    "DescribeScalingActivitiesPaginateResponseTypeDef",
    {"Activities": List[DescribeScalingActivitiesPaginateResponseActivitiesTypeDef]},
    total=False,
)

DescribeScheduledActionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeScheduledActionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef = TypedDict(
    "DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "Time": datetime,
        "StartTime": datetime,
        "EndTime": datetime,
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
    },
    total=False,
)

DescribeScheduledActionsPaginateResponseTypeDef = TypedDict(
    "DescribeScheduledActionsPaginateResponseTypeDef",
    {
        "ScheduledUpdateGroupActions": List[
            DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef
        ]
    },
    total=False,
)

DescribeTagsPaginateFiltersTypeDef = TypedDict(
    "DescribeTagsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

DescribeTagsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeTagsPaginateResponseTagsTypeDef = TypedDict(
    "DescribeTagsPaginateResponseTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

DescribeTagsPaginateResponseTypeDef = TypedDict(
    "DescribeTagsPaginateResponseTypeDef",
    {"Tags": List[DescribeTagsPaginateResponseTagsTypeDef]},
    total=False,
)
