"Main interface for autoscaling service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef",
    "ClientBatchDeleteScheduledActionResponseTypeDef",
    "ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef",
    "ClientBatchPutScheduledUpdateGroupActionResponseTypeDef",
    "ClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef",
    "ClientCreateAutoScalingGroupLaunchTemplateTypeDef",
    "ClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef",
    "ClientCreateAutoScalingGroupTagsTypeDef",
    "ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef",
    "ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef",
    "ClientCreateLaunchConfigurationInstanceMonitoringTypeDef",
    "ClientCreateOrUpdateTagsTagsTypeDef",
    "ClientDeleteTagsTagsTypeDef",
    "ClientDescribeAccountLimitsResponseTypeDef",
    "ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef",
    "ClientDescribeAdjustmentTypesResponseTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef",
    "ClientDescribeAutoScalingGroupsResponseTypeDef",
    "ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef",
    "ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef",
    "ClientDescribeAutoScalingInstancesResponseTypeDef",
    "ClientDescribeAutoScalingNotificationTypesResponseTypeDef",
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef",
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef",
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef",
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef",
    "ClientDescribeLaunchConfigurationsResponseTypeDef",
    "ClientDescribeLifecycleHookTypesResponseTypeDef",
    "ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef",
    "ClientDescribeLifecycleHooksResponseTypeDef",
    "ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef",
    "ClientDescribeLoadBalancerTargetGroupsResponseTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersTypeDef",
    "ClientDescribeLoadBalancersResponseTypeDef",
    "ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef",
    "ClientDescribeMetricCollectionTypesResponseMetricsTypeDef",
    "ClientDescribeMetricCollectionTypesResponseTypeDef",
    "ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef",
    "ClientDescribeNotificationConfigurationsResponseTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTypeDef",
    "ClientDescribePoliciesResponseTypeDef",
    "ClientDescribeScalingActivitiesResponseActivitiesTypeDef",
    "ClientDescribeScalingActivitiesResponseTypeDef",
    "ClientDescribeScalingProcessTypesResponseProcessesTypeDef",
    "ClientDescribeScalingProcessTypesResponseTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef",
    "ClientDescribeScheduledActionsResponseTypeDef",
    "ClientDescribeTagsFiltersTypeDef",
    "ClientDescribeTagsResponseTagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDescribeTerminationPolicyTypesResponseTypeDef",
    "ClientDetachInstancesResponseActivitiesTypeDef",
    "ClientDetachInstancesResponseTypeDef",
    "ClientEnterStandbyResponseActivitiesTypeDef",
    "ClientEnterStandbyResponseTypeDef",
    "ClientExitStandbyResponseActivitiesTypeDef",
    "ClientExitStandbyResponseTypeDef",
    "ClientPutScalingPolicyResponseAlarmsTypeDef",
    "ClientPutScalingPolicyResponseTypeDef",
    "ClientPutScalingPolicyStepAdjustmentsTypeDef",
    "ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    "ClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    "ClientPutScalingPolicyTargetTrackingConfigurationTypeDef",
    "ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef",
    "ClientTerminateInstanceInAutoScalingGroupResponseTypeDef",
    "ClientUpdateAutoScalingGroupLaunchTemplateTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef",
    "DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseTypeDef",
    "DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef",
    "DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef",
    "DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef",
    "DescribeAutoScalingInstancesPaginateResponseTypeDef",
    "DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef",
    "DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef",
    "DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef",
    "DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef",
    "DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef",
    "DescribeLaunchConfigurationsPaginateResponseTypeDef",
    "DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef",
    "DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef",
    "DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef",
    "DescribeLoadBalancersPaginatePaginationConfigTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef",
    "DescribeLoadBalancersPaginateResponseTypeDef",
    "DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef",
    "DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef",
    "DescribeNotificationConfigurationsPaginateResponseTypeDef",
    "DescribePoliciesPaginatePaginationConfigTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesTypeDef",
    "DescribePoliciesPaginateResponseTypeDef",
    "DescribeScalingActivitiesPaginatePaginationConfigTypeDef",
    "DescribeScalingActivitiesPaginateResponseActivitiesTypeDef",
    "DescribeScalingActivitiesPaginateResponseTypeDef",
    "DescribeScheduledActionsPaginatePaginationConfigTypeDef",
    "DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef",
    "DescribeScheduledActionsPaginateResponseTypeDef",
    "DescribeTagsPaginateFiltersTypeDef",
    "DescribeTagsPaginatePaginationConfigTypeDef",
    "DescribeTagsPaginateResponseTagsTypeDef",
    "DescribeTagsPaginateResponseTypeDef",
)


_ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef = TypedDict(
    "_ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef",
    {"ScheduledActionName": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef(
    _ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef
):
    """
    - *(dict) --*

      Describes a scheduled action that could not be created, updated, or deleted.
      - **ScheduledActionName** *(string) --*

        The name of the scheduled action.
    """


_ClientBatchDeleteScheduledActionResponseTypeDef = TypedDict(
    "_ClientBatchDeleteScheduledActionResponseTypeDef",
    {
        "FailedScheduledActions": List[
            ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef
        ]
    },
    total=False,
)


class ClientBatchDeleteScheduledActionResponseTypeDef(
    _ClientBatchDeleteScheduledActionResponseTypeDef
):
    """
    - *(dict) --*

      - **FailedScheduledActions** *(list) --*

        The names of the scheduled actions that could not be deleted, including an error message.
        - *(dict) --*

          Describes a scheduled action that could not be created, updated, or deleted.
          - **ScheduledActionName** *(string) --*

            The name of the scheduled action.
    """


_ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef = TypedDict(
    "_ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef",
    {"ScheduledActionName": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef(
    _ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef
):
    """
    - *(dict) --*

      Describes a scheduled action that could not be created, updated, or deleted.
      - **ScheduledActionName** *(string) --*

        The name of the scheduled action.
    """


_ClientBatchPutScheduledUpdateGroupActionResponseTypeDef = TypedDict(
    "_ClientBatchPutScheduledUpdateGroupActionResponseTypeDef",
    {
        "FailedScheduledUpdateGroupActions": List[
            ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef
        ]
    },
    total=False,
)


class ClientBatchPutScheduledUpdateGroupActionResponseTypeDef(
    _ClientBatchPutScheduledUpdateGroupActionResponseTypeDef
):
    """
    - *(dict) --*

      - **FailedScheduledUpdateGroupActions** *(list) --*

        The names of the scheduled actions that could not be created or updated, including an error
        message.
        - *(dict) --*

          Describes a scheduled action that could not be created, updated, or deleted.
          - **ScheduledActionName** *(string) --*

            The name of the scheduled action.
    """


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
    """
    - *(dict) --*

      Describes one or more scheduled scaling action updates for a specified Auto Scaling group.
      Used in combination with  BatchPutScheduledUpdateGroupAction .
      When updating a scheduled scaling action, all optional parameters are left unchanged if not
      specified.
      - **ScheduledActionName** *(string) --***[REQUIRED]**

        The name of the scaling action.
    """


_ClientCreateAutoScalingGroupLaunchTemplateTypeDef = TypedDict(
    "_ClientCreateAutoScalingGroupLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientCreateAutoScalingGroupLaunchTemplateTypeDef(
    _ClientCreateAutoScalingGroupLaunchTemplateTypeDef
):
    """
    The launch template to use to launch instances.
    For more information, see `LaunchTemplateSpecification
    <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LaunchTemplateSpecification.html>`__
    in the *Amazon EC2 Auto Scaling API Reference* .
    If you do not specify ``LaunchTemplate`` , you must specify one of the following parameters:
    ``InstanceId`` , ``LaunchConfigurationName`` , or ``MixedInstancesPolicy`` .
    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template name.
    """


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
    """
    - *(dict) --*

      Describes a lifecycle hook. Used in combination with  CreateAutoScalingGroup .
      A lifecycle hook tells Amazon EC2 Auto Scaling to perform an action on an instance when the
      instance launches (before it is put into service) or as the instance terminates (before it is
      fully terminated).
      This step is a part of the procedure for creating a lifecycle hook for an Auto Scaling group:
      * (Optional) Create a Lambda function and a rule that allows CloudWatch Events to invoke your
      Lambda function when Amazon EC2 Auto Scaling launches or terminates instances.
      * (Optional) Create a notification target and an IAM role. The target can be either an Amazon
      SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle
      notifications to the target.
      * **Create the lifecycle hook. Specify whether the hook is used when the instances launch or
      terminate.**
      * If you need more time, record the lifecycle action heartbeat to keep the instance in a
      pending state using  RecordLifecycleActionHeartbeat .
      * If you finish before the timeout period ends, complete the lifecycle action using
      CompleteLifecycleAction .
      For more information, see `Amazon EC2 Auto Scaling Lifecycle Hooks
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html>`__ in the *Amazon
      EC2 Auto Scaling User Guide* .
      You can view the lifecycle hooks for an Auto Scaling group using  DescribeLifecycleHooks . You
      can modify an existing lifecycle hook or create new lifecycle hooks using  PutLifecycleHook .
      If you are no longer using a lifecycle hook, you can delete it using  DeleteLifecycleHook .
      - **LifecycleHookName** *(string) --***[REQUIRED]**

        The name of the lifecycle hook.
    """


_ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "_ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
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


class ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef(
    _ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef
):
    pass


_ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "_ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef(
    _ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
):
    """
    - **LaunchTemplateSpecification** *(dict) --*

      The launch template to use. You must specify either the launch template ID or launch template
      name in the request.
      - **LaunchTemplateId** *(string) --*

        The ID of the launch template. You must specify either a template ID or a template name.
    """


_ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "_ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)


class ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef(
    _ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef
):
    pass


_ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "_ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)


class ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef(
    _ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef
):
    """
    - **LaunchTemplate** *(dict) --*

      The launch template and instance types (overrides).
      This parameter must be specified when creating a mixed instances policy.
      - **LaunchTemplateSpecification** *(dict) --*

        The launch template to use. You must specify either the launch template ID or launch
        template name in the request.
        - **LaunchTemplateId** *(string) --*

          The ID of the launch template. You must specify either a template ID or a template name.
    """


_ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef = TypedDict(
    "_ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)


class ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef(
    _ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef
):
    """
    An embedded object that specifies a mixed instances policy. The required parameters must be
    specified. If optional parameters are unspecified, their default values are used.
    The policy includes parameters that not only define the distribution of On-Demand Instances and
    Spot Instances, the maximum price to pay for Spot Instances, and how the Auto Scaling group
    allocates instance types to fulfill On-Demand and Spot capacity, but also the parameters that
    specify the instance configuration information—the launch template and instance types.
    For more information, see `MixedInstancesPolicy
    <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_MixedInstancesPolicy.html>`__ in
    the *Amazon EC2 Auto Scaling API Reference* and `Auto Scaling Groups with Multiple Instance
    Types and Purchase Options
    <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html>`__ in the
    *Amazon EC2 Auto Scaling User Guide* .
    You must specify one of the following parameters in your request: ``LaunchConfigurationName`` ,
    ``LaunchTemplate`` , ``InstanceId`` , or ``MixedInstancesPolicy`` .
    - **LaunchTemplate** *(dict) --*

      The launch template and instance types (overrides).
      This parameter must be specified when creating a mixed instances policy.
      - **LaunchTemplateSpecification** *(dict) --*

        The launch template to use. You must specify either the launch template ID or launch
        template name in the request.
        - **LaunchTemplateId** *(string) --*

          The ID of the launch template. You must specify either a template ID or a template name.
    """


_ClientCreateAutoScalingGroupTagsTypeDef = TypedDict(
    "_ClientCreateAutoScalingGroupTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)


class ClientCreateAutoScalingGroupTagsTypeDef(_ClientCreateAutoScalingGroupTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag for an Auto Scaling group.
      - **ResourceId** *(string) --*

        The name of the group.
    """


_ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef = TypedDict(
    "_ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef",
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


class ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef(
    _ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef
):
    pass


_ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef = TypedDict(
    "_ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef",
    {
        "VirtualName": str,
        "DeviceName": str,
        "Ebs": ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef,
        "NoDevice": bool,
    },
    total=False,
)


class ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef(
    _ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef
):
    """
    - *(dict) --*

      Describes a block device mapping.
      - **VirtualName** *(string) --*

        The name of the virtual device (for example, ``ephemeral0`` ).
    """


_ClientCreateLaunchConfigurationInstanceMonitoringTypeDef = TypedDict(
    "_ClientCreateLaunchConfigurationInstanceMonitoringTypeDef", {"Enabled": bool}, total=False
)


class ClientCreateLaunchConfigurationInstanceMonitoringTypeDef(
    _ClientCreateLaunchConfigurationInstanceMonitoringTypeDef
):
    """
    Controls whether instances in this group are launched with detailed (``true`` ) or basic
    (``false`` ) monitoring.
    The default value is ``true`` (enabled).
    .. warning::

      When detailed monitoring is enabled, Amazon CloudWatch generates metrics every minute and your
      account is charged a fee. When you disable detailed monitoring, CloudWatch generates metrics
      every 5 minutes. For more information, see `Configure Monitoring for Auto Scaling Instances
      <https://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-monitoring.html#enable-as-instance-metrics>`__
      in the *Amazon EC2 Auto Scaling User Guide* .
    """


_ClientCreateOrUpdateTagsTagsTypeDef = TypedDict(
    "_ClientCreateOrUpdateTagsTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)


class ClientCreateOrUpdateTagsTagsTypeDef(_ClientCreateOrUpdateTagsTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag for an Auto Scaling group.
      - **ResourceId** *(string) --*

        The name of the group.
    """


_ClientDeleteTagsTagsTypeDef = TypedDict(
    "_ClientDeleteTagsTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)


class ClientDeleteTagsTagsTypeDef(_ClientDeleteTagsTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag for an Auto Scaling group.
      - **ResourceId** *(string) --*

        The name of the group.
    """


_ClientDescribeAccountLimitsResponseTypeDef = TypedDict(
    "_ClientDescribeAccountLimitsResponseTypeDef",
    {
        "MaxNumberOfAutoScalingGroups": int,
        "MaxNumberOfLaunchConfigurations": int,
        "NumberOfAutoScalingGroups": int,
        "NumberOfLaunchConfigurations": int,
    },
    total=False,
)


class ClientDescribeAccountLimitsResponseTypeDef(_ClientDescribeAccountLimitsResponseTypeDef):
    """
    - *(dict) --*

      - **MaxNumberOfAutoScalingGroups** *(integer) --*

        The maximum number of groups allowed for your AWS account. The default limit is 200 per AWS
        Region.
    """


_ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef = TypedDict(
    "_ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef",
    {"AdjustmentType": str},
    total=False,
)


class ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef(
    _ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef
):
    """
    - *(dict) --*

      Describes a policy adjustment type.
      - **AdjustmentType** *(string) --*

        The policy adjustment type. The valid values are ``ChangeInCapacity`` , ``ExactCapacity`` ,
        and ``PercentChangeInCapacity`` .
    """


_ClientDescribeAdjustmentTypesResponseTypeDef = TypedDict(
    "_ClientDescribeAdjustmentTypesResponseTypeDef",
    {"AdjustmentTypes": List[ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef]},
    total=False,
)


class ClientDescribeAdjustmentTypesResponseTypeDef(_ClientDescribeAdjustmentTypesResponseTypeDef):
    """
    - *(dict) --*

      - **AdjustmentTypes** *(list) --*

        The policy adjustment types.
        - *(dict) --*

          Describes a policy adjustment type.
          - **AdjustmentType** *(string) --*

            The policy adjustment type. The valid values are ``ChangeInCapacity`` ,
            ``ExactCapacity`` , and ``PercentChangeInCapacity`` .
    """


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef",
    {"Metric": str, "Granularity": str},
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef
):
    pass


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef
):
    pass


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef",
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


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef
):
    pass


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef
):
    pass


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef",
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


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef
):
    pass


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
):
    pass


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef
):
    pass


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef
):
    pass


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef
):
    pass


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef",
    {"ProcessName": str, "SuspensionReason": str},
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef
):
    pass


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef
):
    pass


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef",
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


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef
):
    """
    - *(dict) --*

      Describes an Auto Scaling group.
      - **AutoScalingGroupName** *(string) --*

        The name of the Auto Scaling group.
    """


_ClientDescribeAutoScalingGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseTypeDef",
    {
        "AutoScalingGroups": List[ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseTypeDef(
    _ClientDescribeAutoScalingGroupsResponseTypeDef
):
    """
    - *(dict) --*

      - **AutoScalingGroups** *(list) --*

        The groups.
        - *(dict) --*

          Describes an Auto Scaling group.
          - **AutoScalingGroupName** *(string) --*

            The name of the Auto Scaling group.
    """


_ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef = TypedDict(
    "_ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef(
    _ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef
):
    pass


_ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef = TypedDict(
    "_ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef",
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


class ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef(
    _ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef
):
    """
    - *(dict) --*

      Describes an EC2 instance associated with an Auto Scaling group.
      - **InstanceId** *(string) --*

        The ID of the instance.
    """


_ClientDescribeAutoScalingInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeAutoScalingInstancesResponseTypeDef",
    {
        "AutoScalingInstances": List[
            ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAutoScalingInstancesResponseTypeDef(
    _ClientDescribeAutoScalingInstancesResponseTypeDef
):
    """
    - *(dict) --*

      - **AutoScalingInstances** *(list) --*

        The instances.
        - *(dict) --*

          Describes an EC2 instance associated with an Auto Scaling group.
          - **InstanceId** *(string) --*

            The ID of the instance.
    """


_ClientDescribeAutoScalingNotificationTypesResponseTypeDef = TypedDict(
    "_ClientDescribeAutoScalingNotificationTypesResponseTypeDef",
    {"AutoScalingNotificationTypes": List[str]},
    total=False,
)


class ClientDescribeAutoScalingNotificationTypesResponseTypeDef(
    _ClientDescribeAutoScalingNotificationTypesResponseTypeDef
):
    """
    - *(dict) --*

      - **AutoScalingNotificationTypes** *(list) --*

        The notification types.
        - *(string) --*
    """


_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef = TypedDict(
    "_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef",
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


class ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef(
    _ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef
):
    pass


_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef = TypedDict(
    "_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef",
    {
        "VirtualName": str,
        "DeviceName": str,
        "Ebs": ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef,
        "NoDevice": bool,
    },
    total=False,
)


class ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef(
    _ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef
):
    pass


_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef = TypedDict(
    "_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef(
    _ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef
):
    pass


_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef = TypedDict(
    "_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef",
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


class ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef(
    _ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef
):
    """
    - *(dict) --*

      Describes a launch configuration.
      - **LaunchConfigurationName** *(string) --*

        The name of the launch configuration.
    """


_ClientDescribeLaunchConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeLaunchConfigurationsResponseTypeDef",
    {
        "LaunchConfigurations": List[
            ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeLaunchConfigurationsResponseTypeDef(
    _ClientDescribeLaunchConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **LaunchConfigurations** *(list) --*

        The launch configurations.
        - *(dict) --*

          Describes a launch configuration.
          - **LaunchConfigurationName** *(string) --*

            The name of the launch configuration.
    """


_ClientDescribeLifecycleHookTypesResponseTypeDef = TypedDict(
    "_ClientDescribeLifecycleHookTypesResponseTypeDef",
    {"LifecycleHookTypes": List[str]},
    total=False,
)


class ClientDescribeLifecycleHookTypesResponseTypeDef(
    _ClientDescribeLifecycleHookTypesResponseTypeDef
):
    """
    - *(dict) --*

      - **LifecycleHookTypes** *(list) --*

        The lifecycle hook types.
        - *(string) --*
    """


_ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef = TypedDict(
    "_ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef",
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


class ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef(
    _ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef
):
    """
    - *(dict) --*

      Describes a lifecycle hook, which tells Amazon EC2 Auto Scaling that you want to perform an
      action whenever it launches instances or terminates instances. Used in response to
      DescribeLifecycleHooks .
      - **LifecycleHookName** *(string) --*

        The name of the lifecycle hook.
    """


_ClientDescribeLifecycleHooksResponseTypeDef = TypedDict(
    "_ClientDescribeLifecycleHooksResponseTypeDef",
    {"LifecycleHooks": List[ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef]},
    total=False,
)


class ClientDescribeLifecycleHooksResponseTypeDef(_ClientDescribeLifecycleHooksResponseTypeDef):
    """
    - *(dict) --*

      - **LifecycleHooks** *(list) --*

        The lifecycle hooks for the specified group.
        - *(dict) --*

          Describes a lifecycle hook, which tells Amazon EC2 Auto Scaling that you want to perform
          an action whenever it launches instances or terminates instances. Used in response to
          DescribeLifecycleHooks .
          - **LifecycleHookName** *(string) --*

            The name of the lifecycle hook.
    """


_ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef",
    {"LoadBalancerTargetGroupARN": str, "State": str},
    total=False,
)


class ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef(
    _ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef
):
    """
    - *(dict) --*

      Describes the state of a target group.
      If you attach a target group to an existing Auto Scaling group, the initial state is
      ``Adding`` . The state transitions to ``Added`` after all Auto Scaling instances are
      registered with the target group. If Elastic Load Balancing health checks are enabled, the
      state transitions to ``InService`` after at least one Auto Scaling instance passes the health
      check. If EC2 health checks are enabled instead, the target group remains in the ``Added``
      state.
      - **LoadBalancerTargetGroupARN** *(string) --*

        The Amazon Resource Name (ARN) of the target group.
    """


_ClientDescribeLoadBalancerTargetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerTargetGroupsResponseTypeDef",
    {
        "LoadBalancerTargetGroups": List[
            ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeLoadBalancerTargetGroupsResponseTypeDef(
    _ClientDescribeLoadBalancerTargetGroupsResponseTypeDef
):
    """
    - *(dict) --*

      - **LoadBalancerTargetGroups** *(list) --*

        Information about the target groups.
        - *(dict) --*

          Describes the state of a target group.
          If you attach a target group to an existing Auto Scaling group, the initial state is
          ``Adding`` . The state transitions to ``Added`` after all Auto Scaling instances are
          registered with the target group. If Elastic Load Balancing health checks are enabled, the
          state transitions to ``InService`` after at least one Auto Scaling instance passes the
          health check. If EC2 health checks are enabled instead, the target group remains in the
          ``Added`` state.
          - **LoadBalancerTargetGroupARN** *(string) --*

            The Amazon Resource Name (ARN) of the target group.
    """


_ClientDescribeLoadBalancersResponseLoadBalancersTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancersTypeDef",
    {"LoadBalancerName": str, "State": str},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancersTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancersTypeDef
):
    """
    - *(dict) --*

      Describes the state of a Classic Load Balancer.
      If you specify a load balancer when creating the Auto Scaling group, the state of the load
      balancer is ``InService`` .
      If you attach a load balancer to an existing Auto Scaling group, the initial state is
      ``Adding`` . The state transitions to ``Added`` after all instances in the group are
      registered with the load balancer. If Elastic Load Balancing health checks are enabled for the
      load balancer, the state transitions to ``InService`` after at least one instance in the group
      passes the health check. If EC2 health checks are enabled instead, the load balancer remains
      in the ``Added`` state.
      - **LoadBalancerName** *(string) --*

        The name of the load balancer.
    """


_ClientDescribeLoadBalancersResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancers": List[ClientDescribeLoadBalancersResponseLoadBalancersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseTypeDef(_ClientDescribeLoadBalancersResponseTypeDef):
    """
    - *(dict) --*

      - **LoadBalancers** *(list) --*

        The load balancers.
        - *(dict) --*

          Describes the state of a Classic Load Balancer.
          If you specify a load balancer when creating the Auto Scaling group, the state of the load
          balancer is ``InService`` .
          If you attach a load balancer to an existing Auto Scaling group, the initial state is
          ``Adding`` . The state transitions to ``Added`` after all instances in the group are
          registered with the load balancer. If Elastic Load Balancing health checks are enabled for
          the load balancer, the state transitions to ``InService`` after at least one instance in
          the group passes the health check. If EC2 health checks are enabled instead, the load
          balancer remains in the ``Added`` state.
          - **LoadBalancerName** *(string) --*

            The name of the load balancer.
    """


_ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef = TypedDict(
    "_ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef",
    {"Granularity": str},
    total=False,
)


class ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef(
    _ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef
):
    pass


_ClientDescribeMetricCollectionTypesResponseMetricsTypeDef = TypedDict(
    "_ClientDescribeMetricCollectionTypesResponseMetricsTypeDef", {"Metric": str}, total=False
)


class ClientDescribeMetricCollectionTypesResponseMetricsTypeDef(
    _ClientDescribeMetricCollectionTypesResponseMetricsTypeDef
):
    """
    - *(dict) --*

      Describes a metric.
      - **Metric** *(string) --*

        One of the following metrics:
        * ``GroupMinSize``
        * ``GroupMaxSize``
        * ``GroupDesiredCapacity``
        * ``GroupInServiceInstances``
        * ``GroupPendingInstances``
        * ``GroupStandbyInstances``
        * ``GroupTerminatingInstances``
        * ``GroupTotalInstances``
    """


_ClientDescribeMetricCollectionTypesResponseTypeDef = TypedDict(
    "_ClientDescribeMetricCollectionTypesResponseTypeDef",
    {
        "Metrics": List[ClientDescribeMetricCollectionTypesResponseMetricsTypeDef],
        "Granularities": List[ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef],
    },
    total=False,
)


class ClientDescribeMetricCollectionTypesResponseTypeDef(
    _ClientDescribeMetricCollectionTypesResponseTypeDef
):
    """
    - *(dict) --*

      - **Metrics** *(list) --*

        One or more metrics.
        - *(dict) --*

          Describes a metric.
          - **Metric** *(string) --*

            One of the following metrics:
            * ``GroupMinSize``
            * ``GroupMaxSize``
            * ``GroupDesiredCapacity``
            * ``GroupInServiceInstances``
            * ``GroupPendingInstances``
            * ``GroupStandbyInstances``
            * ``GroupTerminatingInstances``
            * ``GroupTotalInstances``
    """


_ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef = TypedDict(
    "_ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef",
    {"AutoScalingGroupName": str, "TopicARN": str, "NotificationType": str},
    total=False,
)


class ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef(
    _ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef
):
    """
    - *(dict) --*

      Describes a notification.
      - **AutoScalingGroupName** *(string) --*

        The name of the Auto Scaling group.
    """


_ClientDescribeNotificationConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeNotificationConfigurationsResponseTypeDef",
    {
        "NotificationConfigurations": List[
            ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeNotificationConfigurationsResponseTypeDef(
    _ClientDescribeNotificationConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **NotificationConfigurations** *(list) --*

        The notification configurations.
        - *(dict) --*

          Describes a notification.
          - **AutoScalingGroupName** *(string) --*

            The name of the Auto Scaling group.
    """


_ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)


class ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef
):
    pass


_ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)


class ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef
):
    pass


_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
):
    pass


_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
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


class ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef
):
    pass


_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
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


class ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef
):
    pass


_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
    },
    total=False,
)


class ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef
):
    pass


_ClientDescribePoliciesResponseScalingPoliciesTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesTypeDef",
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


class ClientDescribePoliciesResponseScalingPoliciesTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesTypeDef
):
    """
    - *(dict) --*

      Describes a scaling policy.
      - **AutoScalingGroupName** *(string) --*

        The name of the Auto Scaling group.
    """


_ClientDescribePoliciesResponseTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseTypeDef",
    {
        "ScalingPolicies": List[ClientDescribePoliciesResponseScalingPoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribePoliciesResponseTypeDef(_ClientDescribePoliciesResponseTypeDef):
    """
    - *(dict) --*

      - **ScalingPolicies** *(list) --*

        The scaling policies.
        - *(dict) --*

          Describes a scaling policy.
          - **AutoScalingGroupName** *(string) --*

            The name of the Auto Scaling group.
    """


_ClientDescribeScalingActivitiesResponseActivitiesTypeDef = TypedDict(
    "_ClientDescribeScalingActivitiesResponseActivitiesTypeDef",
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


class ClientDescribeScalingActivitiesResponseActivitiesTypeDef(
    _ClientDescribeScalingActivitiesResponseActivitiesTypeDef
):
    """
    - *(dict) --*

      Describes scaling activity, which is a long-running process that represents a change to your
      Auto Scaling group, such as changing its size or replacing an instance.
      - **ActivityId** *(string) --*

        The ID of the activity.
    """


_ClientDescribeScalingActivitiesResponseTypeDef = TypedDict(
    "_ClientDescribeScalingActivitiesResponseTypeDef",
    {
        "Activities": List[ClientDescribeScalingActivitiesResponseActivitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScalingActivitiesResponseTypeDef(
    _ClientDescribeScalingActivitiesResponseTypeDef
):
    """
    - *(dict) --*

      - **Activities** *(list) --*

        The scaling activities. Activities are sorted by start time. Activities still in progress
        are described first.
        - *(dict) --*

          Describes scaling activity, which is a long-running process that represents a change to
          your Auto Scaling group, such as changing its size or replacing an instance.
          - **ActivityId** *(string) --*

            The ID of the activity.
    """


_ClientDescribeScalingProcessTypesResponseProcessesTypeDef = TypedDict(
    "_ClientDescribeScalingProcessTypesResponseProcessesTypeDef", {"ProcessName": str}, total=False
)


class ClientDescribeScalingProcessTypesResponseProcessesTypeDef(
    _ClientDescribeScalingProcessTypesResponseProcessesTypeDef
):
    """
    - *(dict) --*

      Describes a process type.
      For more information, see `Scaling Processes
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html#process-types>`__
      in the *Amazon EC2 Auto Scaling User Guide* .
      - **ProcessName** *(string) --*

        One of the following processes:
        * ``Launch``
        * ``Terminate``
        * ``AddToLoadBalancer``
        * ``AlarmNotification``
        * ``AZRebalance``
        * ``HealthCheck``
        * ``ReplaceUnhealthy``
        * ``ScheduledActions``
    """


_ClientDescribeScalingProcessTypesResponseTypeDef = TypedDict(
    "_ClientDescribeScalingProcessTypesResponseTypeDef",
    {"Processes": List[ClientDescribeScalingProcessTypesResponseProcessesTypeDef]},
    total=False,
)


class ClientDescribeScalingProcessTypesResponseTypeDef(
    _ClientDescribeScalingProcessTypesResponseTypeDef
):
    """
    - *(dict) --*

      - **Processes** *(list) --*

        The names of the process types.
        - *(dict) --*

          Describes a process type.
          For more information, see `Scaling Processes
          <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html#process-types>`__
          in the *Amazon EC2 Auto Scaling User Guide* .
          - **ProcessName** *(string) --*

            One of the following processes:
            * ``Launch``
            * ``Terminate``
            * ``AddToLoadBalancer``
            * ``AlarmNotification``
            * ``AZRebalance``
            * ``HealthCheck``
            * ``ReplaceUnhealthy``
            * ``ScheduledActions``
    """


_ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef",
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


class ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef(
    _ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef
):
    """
    - *(dict) --*

      Describes a scheduled scaling action. Used in response to  DescribeScheduledActions .
      - **AutoScalingGroupName** *(string) --*

        The name of the Auto Scaling group.
    """


_ClientDescribeScheduledActionsResponseTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseTypeDef",
    {
        "ScheduledUpdateGroupActions": List[
            ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScheduledActionsResponseTypeDef(_ClientDescribeScheduledActionsResponseTypeDef):
    """
    - *(dict) --*

      - **ScheduledUpdateGroupActions** *(list) --*

        The scheduled actions.
        - *(dict) --*

          Describes a scheduled scaling action. Used in response to  DescribeScheduledActions .
          - **AutoScalingGroupName** *(string) --*

            The name of the Auto Scaling group.
    """


_ClientDescribeTagsFiltersTypeDef = TypedDict(
    "_ClientDescribeTagsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeTagsFiltersTypeDef(_ClientDescribeTagsFiltersTypeDef):
    """
    - *(dict) --*

      Describes a filter.
      - **Name** *(string) --*

        The name of the filter. The valid values are: ``"auto-scaling-group"`` , ``"key"`` ,
        ``"value"`` , and ``"propagate-at-launch"`` .
    """


_ClientDescribeTagsResponseTagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)


class ClientDescribeTagsResponseTagsTypeDef(_ClientDescribeTagsResponseTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag for an Auto Scaling group.
      - **ResourceId** *(string) --*

        The name of the group.
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {"Tags": List[ClientDescribeTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        One or more tags.
        - *(dict) --*

          Describes a tag for an Auto Scaling group.
          - **ResourceId** *(string) --*

            The name of the group.
    """


_ClientDescribeTerminationPolicyTypesResponseTypeDef = TypedDict(
    "_ClientDescribeTerminationPolicyTypesResponseTypeDef",
    {"TerminationPolicyTypes": List[str]},
    total=False,
)


class ClientDescribeTerminationPolicyTypesResponseTypeDef(
    _ClientDescribeTerminationPolicyTypesResponseTypeDef
):
    """
    - *(dict) --*

      - **TerminationPolicyTypes** *(list) --*

        The termination policies supported by Amazon EC2 Auto Scaling: ``OldestInstance`` ,
        ``OldestLaunchConfiguration`` , ``NewestInstance`` , ``ClosestToNextInstanceHour`` ,
        ``Default`` , ``OldestLaunchTemplate`` , and ``AllocationStrategy`` .
        - *(string) --*
    """


_ClientDetachInstancesResponseActivitiesTypeDef = TypedDict(
    "_ClientDetachInstancesResponseActivitiesTypeDef",
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


class ClientDetachInstancesResponseActivitiesTypeDef(
    _ClientDetachInstancesResponseActivitiesTypeDef
):
    """
    - *(dict) --*

      Describes scaling activity, which is a long-running process that represents a change to your
      Auto Scaling group, such as changing its size or replacing an instance.
      - **ActivityId** *(string) --*

        The ID of the activity.
    """


_ClientDetachInstancesResponseTypeDef = TypedDict(
    "_ClientDetachInstancesResponseTypeDef",
    {"Activities": List[ClientDetachInstancesResponseActivitiesTypeDef]},
    total=False,
)


class ClientDetachInstancesResponseTypeDef(_ClientDetachInstancesResponseTypeDef):
    """
    - *(dict) --*

      - **Activities** *(list) --*

        The activities related to detaching the instances from the Auto Scaling group.
        - *(dict) --*

          Describes scaling activity, which is a long-running process that represents a change to
          your Auto Scaling group, such as changing its size or replacing an instance.
          - **ActivityId** *(string) --*

            The ID of the activity.
    """


_ClientEnterStandbyResponseActivitiesTypeDef = TypedDict(
    "_ClientEnterStandbyResponseActivitiesTypeDef",
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


class ClientEnterStandbyResponseActivitiesTypeDef(_ClientEnterStandbyResponseActivitiesTypeDef):
    """
    - *(dict) --*

      Describes scaling activity, which is a long-running process that represents a change to your
      Auto Scaling group, such as changing its size or replacing an instance.
      - **ActivityId** *(string) --*

        The ID of the activity.
    """


_ClientEnterStandbyResponseTypeDef = TypedDict(
    "_ClientEnterStandbyResponseTypeDef",
    {"Activities": List[ClientEnterStandbyResponseActivitiesTypeDef]},
    total=False,
)


class ClientEnterStandbyResponseTypeDef(_ClientEnterStandbyResponseTypeDef):
    """
    - *(dict) --*

      - **Activities** *(list) --*

        The activities related to moving instances into ``Standby`` mode.
        - *(dict) --*

          Describes scaling activity, which is a long-running process that represents a change to
          your Auto Scaling group, such as changing its size or replacing an instance.
          - **ActivityId** *(string) --*

            The ID of the activity.
    """


_ClientExitStandbyResponseActivitiesTypeDef = TypedDict(
    "_ClientExitStandbyResponseActivitiesTypeDef",
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


class ClientExitStandbyResponseActivitiesTypeDef(_ClientExitStandbyResponseActivitiesTypeDef):
    """
    - *(dict) --*

      Describes scaling activity, which is a long-running process that represents a change to your
      Auto Scaling group, such as changing its size or replacing an instance.
      - **ActivityId** *(string) --*

        The ID of the activity.
    """


_ClientExitStandbyResponseTypeDef = TypedDict(
    "_ClientExitStandbyResponseTypeDef",
    {"Activities": List[ClientExitStandbyResponseActivitiesTypeDef]},
    total=False,
)


class ClientExitStandbyResponseTypeDef(_ClientExitStandbyResponseTypeDef):
    """
    - *(dict) --*

      - **Activities** *(list) --*

        The activities related to moving instances out of ``Standby`` mode.
        - *(dict) --*

          Describes scaling activity, which is a long-running process that represents a change to
          your Auto Scaling group, such as changing its size or replacing an instance.
          - **ActivityId** *(string) --*

            The ID of the activity.
    """


_ClientPutScalingPolicyResponseAlarmsTypeDef = TypedDict(
    "_ClientPutScalingPolicyResponseAlarmsTypeDef", {"AlarmName": str, "AlarmARN": str}, total=False
)


class ClientPutScalingPolicyResponseAlarmsTypeDef(_ClientPutScalingPolicyResponseAlarmsTypeDef):
    pass


_ClientPutScalingPolicyResponseTypeDef = TypedDict(
    "_ClientPutScalingPolicyResponseTypeDef",
    {"PolicyARN": str, "Alarms": List[ClientPutScalingPolicyResponseAlarmsTypeDef]},
    total=False,
)


class ClientPutScalingPolicyResponseTypeDef(_ClientPutScalingPolicyResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of PutScalingPolicy.
      - **PolicyARN** *(string) --*

        The Amazon Resource Name (ARN) of the policy.
    """


_ClientPutScalingPolicyStepAdjustmentsTypeDef = TypedDict(
    "_ClientPutScalingPolicyStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)


class ClientPutScalingPolicyStepAdjustmentsTypeDef(_ClientPutScalingPolicyStepAdjustmentsTypeDef):
    """
    - *(dict) --*

      Describes an adjustment based on the difference between the value of the aggregated CloudWatch
      metric and the breach threshold that you've defined for the alarm. Used in combination with
      PutScalingPolicy .
      For the following examples, suppose that you have an alarm with a breach threshold of 50:
      * To trigger the adjustment when the metric is greater than or equal to 50 and less than 60,
      specify a lower bound of 0 and an upper bound of 10.
      * To trigger the adjustment when the metric is greater than 40 and less than or equal to 50,
      specify a lower bound of -10 and an upper bound of 0.
      There are a few rules for the step adjustments for your step policy:
      * The ranges of your step adjustments can't overlap or have a gap.
      * At most, one step adjustment can have a null lower bound. If one step adjustment has a
      negative lower bound, then there must be a step adjustment with a null lower bound.
      * At most, one step adjustment can have a null upper bound. If one step adjustment has a
      positive upper bound, then there must be a step adjustment with a null upper bound.
      * The upper and lower bound can't be null in the same step adjustment.
      - **MetricIntervalLowerBound** *(float) --*

        The lower bound for the difference between the alarm threshold and the CloudWatch metric. If
        the metric value is above the breach threshold, the lower bound is inclusive (the metric
        must be greater than or equal to the threshold plus the lower bound). Otherwise, it is
        exclusive (the metric must be greater than the threshold plus the lower bound). A null value
        indicates negative infinity.
    """


_ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef(
    _ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
):
    pass


_ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
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


class ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef(
    _ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef
):
    pass


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
    """
    - **PredefinedMetricSpecification** *(dict) --*

      A predefined metric. You must specify either a predefined metric or a customized metric.
      - **PredefinedMetricType** *(string) --***[REQUIRED]**

        The metric type. The following predefined metrics are available:
        * ``ASGAverageCPUUtilization`` - Average CPU utilization of the Auto Scaling group.
        * ``ASGAverageNetworkIn`` - Average number of bytes received on all network interfaces by
        the Auto Scaling group.
        * ``ASGAverageNetworkOut`` - Average number of bytes sent out on all network interfaces by
        the Auto Scaling group.
        * ``ALBRequestCountPerTarget`` - Number of requests completed per target in an Application
        Load Balancer target group.
    """


_ClientPutScalingPolicyTargetTrackingConfigurationTypeDef = TypedDict(
    "_ClientPutScalingPolicyTargetTrackingConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": ClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
    },
    total=False,
)


class ClientPutScalingPolicyTargetTrackingConfigurationTypeDef(
    _ClientPutScalingPolicyTargetTrackingConfigurationTypeDef
):
    """
    A target tracking scaling policy. Includes support for predefined or customized metrics.
    For more information, see `TargetTrackingConfiguration
    <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TargetTrackingConfiguration.html>`__
    in the *Amazon EC2 Auto Scaling API Reference* .
    Conditional: If you specify ``TargetTrackingScaling`` for the policy type, you must specify this
    parameter. (Not used with any other policy type.)
    - **PredefinedMetricSpecification** *(dict) --*

      A predefined metric. You must specify either a predefined metric or a customized metric.
      - **PredefinedMetricType** *(string) --***[REQUIRED]**

        The metric type. The following predefined metrics are available:
        * ``ASGAverageCPUUtilization`` - Average CPU utilization of the Auto Scaling group.
        * ``ASGAverageNetworkIn`` - Average number of bytes received on all network interfaces by
        the Auto Scaling group.
        * ``ASGAverageNetworkOut`` - Average number of bytes sent out on all network interfaces by
        the Auto Scaling group.
        * ``ALBRequestCountPerTarget`` - Number of requests completed per target in an Application
        Load Balancer target group.
    """


_ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef = TypedDict(
    "_ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef",
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


class ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef(
    _ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef
):
    """
    - **Activity** *(dict) --*

      A scaling activity.
      - **ActivityId** *(string) --*

        The ID of the activity.
    """


_ClientTerminateInstanceInAutoScalingGroupResponseTypeDef = TypedDict(
    "_ClientTerminateInstanceInAutoScalingGroupResponseTypeDef",
    {"Activity": ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef},
    total=False,
)


class ClientTerminateInstanceInAutoScalingGroupResponseTypeDef(
    _ClientTerminateInstanceInAutoScalingGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **Activity** *(dict) --*

        A scaling activity.
        - **ActivityId** *(string) --*

          The ID of the activity.
    """


_ClientUpdateAutoScalingGroupLaunchTemplateTypeDef = TypedDict(
    "_ClientUpdateAutoScalingGroupLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientUpdateAutoScalingGroupLaunchTemplateTypeDef(
    _ClientUpdateAutoScalingGroupLaunchTemplateTypeDef
):
    """
    The launch template and version to use to specify the updates. If you specify ``LaunchTemplate``
    in your update request, you can't specify ``LaunchConfigurationName`` or
    ``MixedInstancesPolicy`` .
    For more information, see `LaunchTemplateSpecification
    <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LaunchTemplateSpecification.html>`__
    in the *Amazon EC2 Auto Scaling API Reference* .
    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template name.
    """


_ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "_ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
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


class ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef(
    _ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef
):
    pass


_ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "_ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef(
    _ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
):
    """
    - **LaunchTemplateSpecification** *(dict) --*

      The launch template to use. You must specify either the launch template ID or launch template
      name in the request.
      - **LaunchTemplateId** *(string) --*

        The ID of the launch template. You must specify either a template ID or a template name.
    """


_ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "_ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)


class ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef(
    _ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef
):
    pass


_ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "_ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef(
    _ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef
):
    """
    - **LaunchTemplate** *(dict) --*

      The launch template and instance types (overrides).
      This parameter must be specified when creating a mixed instances policy.
      - **LaunchTemplateSpecification** *(dict) --*

        The launch template to use. You must specify either the launch template ID or launch
        template name in the request.
        - **LaunchTemplateId** *(string) --*

          The ID of the launch template. You must specify either a template ID or a template name.
    """


_ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef = TypedDict(
    "_ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)


class ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef(
    _ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef
):
    """
    An embedded object that specifies a mixed instances policy.
    In your call to ``UpdateAutoScalingGroup`` , you can make changes to the policy that is
    specified. All optional parameters are left unchanged if not specified.
    For more information, see `MixedInstancesPolicy
    <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_MixedInstancesPolicy.html>`__ in
    the *Amazon EC2 Auto Scaling API Reference* and `Auto Scaling Groups with Multiple Instance
    Types and Purchase Options
    <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html>`__ in the
    *Amazon EC2 Auto Scaling User Guide* .
    - **LaunchTemplate** *(dict) --*

      The launch template and instance types (overrides).
      This parameter must be specified when creating a mixed instances policy.
      - **LaunchTemplateSpecification** *(dict) --*

        The launch template to use. You must specify either the launch template ID or launch
        template name in the request.
        - **LaunchTemplateId** *(string) --*

          The ID of the launch template. You must specify either a template ID or a template name.
    """


_DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef(
    _DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef",
    {"Metric": str, "Granularity": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef
):
    pass


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef
):
    pass


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef",
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


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef
):
    pass


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef
):
    pass


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef",
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


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef
):
    pass


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
):
    pass


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef
):
    pass


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef
):
    pass


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef
):
    pass


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef",
    {"ProcessName": str, "SuspensionReason": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef
):
    pass


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef
):
    pass


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef",
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


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef
):
    """
    - *(dict) --*

      Describes an Auto Scaling group.
      - **AutoScalingGroupName** *(string) --*

        The name of the Auto Scaling group.
    """


_DescribeAutoScalingGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseTypeDef",
    {"AutoScalingGroups": List[DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef]},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **AutoScalingGroups** *(list) --*

        The groups.
        - *(dict) --*

          Describes an Auto Scaling group.
          - **AutoScalingGroupName** *(string) --*

            The name of the Auto Scaling group.
    """


_DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef(
    _DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef = TypedDict(
    "_DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef(
    _DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef
):
    pass


_DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef = TypedDict(
    "_DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef",
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


class DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef(
    _DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef
):
    """
    - *(dict) --*

      Describes an EC2 instance associated with an Auto Scaling group.
      - **InstanceId** *(string) --*

        The ID of the instance.
    """


_DescribeAutoScalingInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeAutoScalingInstancesPaginateResponseTypeDef",
    {
        "AutoScalingInstances": List[
            DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef
        ]
    },
    total=False,
)


class DescribeAutoScalingInstancesPaginateResponseTypeDef(
    _DescribeAutoScalingInstancesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **AutoScalingInstances** *(list) --*

        The instances.
        - *(dict) --*

          Describes an EC2 instance associated with an Auto Scaling group.
          - **InstanceId** *(string) --*

            The ID of the instance.
    """


_DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef(
    _DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef = TypedDict(
    "_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef",
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


class DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef(
    _DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef
):
    pass


_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef = TypedDict(
    "_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef",
    {
        "VirtualName": str,
        "DeviceName": str,
        "Ebs": DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef,
        "NoDevice": bool,
    },
    total=False,
)


class DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef(
    _DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef
):
    pass


_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef = TypedDict(
    "_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef",
    {"Enabled": bool},
    total=False,
)


class DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef(
    _DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef
):
    pass


_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef = TypedDict(
    "_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef",
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


class DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef(
    _DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef
):
    """
    - *(dict) --*

      Describes a launch configuration.
      - **LaunchConfigurationName** *(string) --*

        The name of the launch configuration.
    """


_DescribeLaunchConfigurationsPaginateResponseTypeDef = TypedDict(
    "_DescribeLaunchConfigurationsPaginateResponseTypeDef",
    {
        "LaunchConfigurations": List[
            DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef
        ]
    },
    total=False,
)


class DescribeLaunchConfigurationsPaginateResponseTypeDef(
    _DescribeLaunchConfigurationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **LaunchConfigurations** *(list) --*

        The launch configurations.
        - *(dict) --*

          Describes a launch configuration.
          - **LaunchConfigurationName** *(string) --*

            The name of the launch configuration.
    """


_DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef(
    _DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef = TypedDict(
    "_DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef",
    {"LoadBalancerTargetGroupARN": str, "State": str},
    total=False,
)


class DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef(
    _DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef
):
    """
    - *(dict) --*

      Describes the state of a target group.
      If you attach a target group to an existing Auto Scaling group, the initial state is
      ``Adding`` . The state transitions to ``Added`` after all Auto Scaling instances are
      registered with the target group. If Elastic Load Balancing health checks are enabled, the
      state transitions to ``InService`` after at least one Auto Scaling instance passes the health
      check. If EC2 health checks are enabled instead, the target group remains in the ``Added``
      state.
      - **LoadBalancerTargetGroupARN** *(string) --*

        The Amazon Resource Name (ARN) of the target group.
    """


_DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef",
    {
        "LoadBalancerTargetGroups": List[
            DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef
        ]
    },
    total=False,
)


class DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef(
    _DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **LoadBalancerTargetGroups** *(list) --*

        Information about the target groups.
        - *(dict) --*

          Describes the state of a target group.
          If you attach a target group to an existing Auto Scaling group, the initial state is
          ``Adding`` . The state transitions to ``Added`` after all Auto Scaling instances are
          registered with the target group. If Elastic Load Balancing health checks are enabled, the
          state transitions to ``InService`` after at least one Auto Scaling instance passes the
          health check. If EC2 health checks are enabled instead, the target group remains in the
          ``Added`` state.
          - **LoadBalancerTargetGroupARN** *(string) --*

            The Amazon Resource Name (ARN) of the target group.
    """


_DescribeLoadBalancersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeLoadBalancersPaginatePaginationConfigTypeDef(
    _DescribeLoadBalancersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef",
    {"LoadBalancerName": str, "State": str},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef
):
    """
    - *(dict) --*

      Describes the state of a Classic Load Balancer.
      If you specify a load balancer when creating the Auto Scaling group, the state of the load
      balancer is ``InService`` .
      If you attach a load balancer to an existing Auto Scaling group, the initial state is
      ``Adding`` . The state transitions to ``Added`` after all instances in the group are
      registered with the load balancer. If Elastic Load Balancing health checks are enabled for the
      load balancer, the state transitions to ``InService`` after at least one instance in the group
      passes the health check. If EC2 health checks are enabled instead, the load balancer remains
      in the ``Added`` state.
      - **LoadBalancerName** *(string) --*

        The name of the load balancer.
    """


_DescribeLoadBalancersPaginateResponseTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseTypeDef",
    {"LoadBalancers": List[DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef]},
    total=False,
)


class DescribeLoadBalancersPaginateResponseTypeDef(_DescribeLoadBalancersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **LoadBalancers** *(list) --*

        The load balancers.
        - *(dict) --*

          Describes the state of a Classic Load Balancer.
          If you specify a load balancer when creating the Auto Scaling group, the state of the load
          balancer is ``InService`` .
          If you attach a load balancer to an existing Auto Scaling group, the initial state is
          ``Adding`` . The state transitions to ``Added`` after all instances in the group are
          registered with the load balancer. If Elastic Load Balancing health checks are enabled for
          the load balancer, the state transitions to ``InService`` after at least one instance in
          the group passes the health check. If EC2 health checks are enabled instead, the load
          balancer remains in the ``Added`` state.
          - **LoadBalancerName** *(string) --*

            The name of the load balancer.
    """


_DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef(
    _DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef = TypedDict(
    "_DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef",
    {"AutoScalingGroupName": str, "TopicARN": str, "NotificationType": str},
    total=False,
)


class DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef(
    _DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef
):
    """
    - *(dict) --*

      Describes a notification.
      - **AutoScalingGroupName** *(string) --*

        The name of the Auto Scaling group.
    """


_DescribeNotificationConfigurationsPaginateResponseTypeDef = TypedDict(
    "_DescribeNotificationConfigurationsPaginateResponseTypeDef",
    {
        "NotificationConfigurations": List[
            DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef
        ]
    },
    total=False,
)


class DescribeNotificationConfigurationsPaginateResponseTypeDef(
    _DescribeNotificationConfigurationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **NotificationConfigurations** *(list) --*

        The notification configurations.
        - *(dict) --*

          Describes a notification.
          - **AutoScalingGroupName** *(string) --*

            The name of the Auto Scaling group.
    """


_DescribePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribePoliciesPaginatePaginationConfigTypeDef(
    _DescribePoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)


class DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef
):
    pass


_DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)


class DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef
):
    pass


_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
):
    pass


_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
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


class DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef
):
    pass


_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
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


class DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef
):
    pass


_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
    },
    total=False,
)


class DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef
):
    pass


_DescribePoliciesPaginateResponseScalingPoliciesTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesTypeDef",
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


class DescribePoliciesPaginateResponseScalingPoliciesTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesTypeDef
):
    """
    - *(dict) --*

      Describes a scaling policy.
      - **AutoScalingGroupName** *(string) --*

        The name of the Auto Scaling group.
    """


_DescribePoliciesPaginateResponseTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseTypeDef",
    {"ScalingPolicies": List[DescribePoliciesPaginateResponseScalingPoliciesTypeDef]},
    total=False,
)


class DescribePoliciesPaginateResponseTypeDef(_DescribePoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ScalingPolicies** *(list) --*

        The scaling policies.
        - *(dict) --*

          Describes a scaling policy.
          - **AutoScalingGroupName** *(string) --*

            The name of the Auto Scaling group.
    """


_DescribeScalingActivitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScalingActivitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScalingActivitiesPaginatePaginationConfigTypeDef(
    _DescribeScalingActivitiesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeScalingActivitiesPaginateResponseActivitiesTypeDef = TypedDict(
    "_DescribeScalingActivitiesPaginateResponseActivitiesTypeDef",
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


class DescribeScalingActivitiesPaginateResponseActivitiesTypeDef(
    _DescribeScalingActivitiesPaginateResponseActivitiesTypeDef
):
    """
    - *(dict) --*

      Describes scaling activity, which is a long-running process that represents a change to your
      Auto Scaling group, such as changing its size or replacing an instance.
      - **ActivityId** *(string) --*

        The ID of the activity.
    """


_DescribeScalingActivitiesPaginateResponseTypeDef = TypedDict(
    "_DescribeScalingActivitiesPaginateResponseTypeDef",
    {"Activities": List[DescribeScalingActivitiesPaginateResponseActivitiesTypeDef]},
    total=False,
)


class DescribeScalingActivitiesPaginateResponseTypeDef(
    _DescribeScalingActivitiesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Activities** *(list) --*

        The scaling activities. Activities are sorted by start time. Activities still in progress
        are described first.
        - *(dict) --*

          Describes scaling activity, which is a long-running process that represents a change to
          your Auto Scaling group, such as changing its size or replacing an instance.
          - **ActivityId** *(string) --*

            The ID of the activity.
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


_DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef",
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


class DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef(
    _DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef
):
    """
    - *(dict) --*

      Describes a scheduled scaling action. Used in response to  DescribeScheduledActions .
      - **AutoScalingGroupName** *(string) --*

        The name of the Auto Scaling group.
    """


_DescribeScheduledActionsPaginateResponseTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseTypeDef",
    {
        "ScheduledUpdateGroupActions": List[
            DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef
        ]
    },
    total=False,
)


class DescribeScheduledActionsPaginateResponseTypeDef(
    _DescribeScheduledActionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ScheduledUpdateGroupActions** *(list) --*

        The scheduled actions.
        - *(dict) --*

          Describes a scheduled scaling action. Used in response to  DescribeScheduledActions .
          - **AutoScalingGroupName** *(string) --*

            The name of the Auto Scaling group.
    """


_DescribeTagsPaginateFiltersTypeDef = TypedDict(
    "_DescribeTagsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class DescribeTagsPaginateFiltersTypeDef(_DescribeTagsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      Describes a filter.
      - **Name** *(string) --*

        The name of the filter. The valid values are: ``"auto-scaling-group"`` , ``"key"`` ,
        ``"value"`` , and ``"propagate-at-launch"`` .
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


_DescribeTagsPaginateResponseTagsTypeDef = TypedDict(
    "_DescribeTagsPaginateResponseTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)


class DescribeTagsPaginateResponseTagsTypeDef(_DescribeTagsPaginateResponseTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag for an Auto Scaling group.
      - **ResourceId** *(string) --*

        The name of the group.
    """


_DescribeTagsPaginateResponseTypeDef = TypedDict(
    "_DescribeTagsPaginateResponseTypeDef",
    {"Tags": List[DescribeTagsPaginateResponseTagsTypeDef]},
    total=False,
)


class DescribeTagsPaginateResponseTypeDef(_DescribeTagsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        One or more tags.
        - *(dict) --*

          Describes a tag for an Auto Scaling group.
          - **ResourceId** *(string) --*

            The name of the group.
    """
