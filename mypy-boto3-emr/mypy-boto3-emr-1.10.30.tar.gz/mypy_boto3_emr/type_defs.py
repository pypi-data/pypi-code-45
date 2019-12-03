"Main interface for emr service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef",
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef",
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef",
    "ClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef",
    "ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef",
    "ClientAddInstanceFleetInstanceFleetTypeDef",
    "ClientAddInstanceFleetResponseTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsTypeDef",
    "ClientAddInstanceGroupsResponseTypeDef",
    "ClientAddJobFlowStepsResponseTypeDef",
    "ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef",
    "ClientAddJobFlowStepsStepsHadoopJarStepTypeDef",
    "ClientAddJobFlowStepsStepsTypeDef",
    "ClientAddTagsTagsTypeDef",
    "ClientCancelStepsResponseCancelStepsInfoListTypeDef",
    "ClientCancelStepsResponseTypeDef",
    "ClientCreateSecurityConfigurationResponseTypeDef",
    "ClientDescribeClusterResponseClusterApplicationsTypeDef",
    "ClientDescribeClusterResponseClusterConfigurationsTypeDef",
    "ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef",
    "ClientDescribeClusterResponseClusterKerberosAttributesTypeDef",
    "ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef",
    "ClientDescribeClusterResponseClusterStatusTimelineTypeDef",
    "ClientDescribeClusterResponseClusterStatusTypeDef",
    "ClientDescribeClusterResponseClusterTagsTypeDef",
    "ClientDescribeClusterResponseClusterTypeDef",
    "ClientDescribeClusterResponseTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsTypeDef",
    "ClientDescribeJobFlowsResponseTypeDef",
    "ClientDescribeSecurityConfigurationResponseTypeDef",
    "ClientDescribeStepResponseStepConfigTypeDef",
    "ClientDescribeStepResponseStepStatusFailureDetailsTypeDef",
    "ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef",
    "ClientDescribeStepResponseStepStatusTimelineTypeDef",
    "ClientDescribeStepResponseStepStatusTypeDef",
    "ClientDescribeStepResponseStepTypeDef",
    "ClientDescribeStepResponseTypeDef",
    "ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef",
    "ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef",
    "ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef",
    "ClientGetBlockPublicAccessConfigurationResponseTypeDef",
    "ClientListBootstrapActionsResponseBootstrapActionsTypeDef",
    "ClientListBootstrapActionsResponseTypeDef",
    "ClientListClustersResponseClustersStatusStateChangeReasonTypeDef",
    "ClientListClustersResponseClustersStatusTimelineTypeDef",
    "ClientListClustersResponseClustersStatusTypeDef",
    "ClientListClustersResponseClustersTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsTypeDef",
    "ClientListInstanceFleetsResponseTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsTypeDef",
    "ClientListInstanceGroupsResponseTypeDef",
    "ClientListInstancesResponseInstancesEbsVolumesTypeDef",
    "ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef",
    "ClientListInstancesResponseInstancesStatusTimelineTypeDef",
    "ClientListInstancesResponseInstancesStatusTypeDef",
    "ClientListInstancesResponseInstancesTypeDef",
    "ClientListInstancesResponseTypeDef",
    "ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef",
    "ClientListSecurityConfigurationsResponseTypeDef",
    "ClientListStepsResponseStepsConfigTypeDef",
    "ClientListStepsResponseStepsStatusFailureDetailsTypeDef",
    "ClientListStepsResponseStepsStatusStateChangeReasonTypeDef",
    "ClientListStepsResponseStepsStatusTimelineTypeDef",
    "ClientListStepsResponseStepsStatusTypeDef",
    "ClientListStepsResponseStepsTypeDef",
    "ClientListStepsResponseTypeDef",
    "ClientModifyClusterResponseTypeDef",
    "ClientModifyInstanceFleetInstanceFleetTypeDef",
    "ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef",
    "ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    "ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef",
    "ClientModifyInstanceGroupsInstanceGroupsTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef",
    "ClientPutAutoScalingPolicyResponseTypeDef",
    "ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef",
    "ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef",
    "ClientRunJobFlowApplicationsTypeDef",
    "ClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef",
    "ClientRunJobFlowBootstrapActionsTypeDef",
    "ClientRunJobFlowConfigurationsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsTypeDef",
    "ClientRunJobFlowInstancesPlacementTypeDef",
    "ClientRunJobFlowInstancesTypeDef",
    "ClientRunJobFlowKerberosAttributesTypeDef",
    "ClientRunJobFlowNewSupportedProductsTypeDef",
    "ClientRunJobFlowResponseTypeDef",
    "ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef",
    "ClientRunJobFlowStepsHadoopJarStepTypeDef",
    "ClientRunJobFlowStepsTypeDef",
    "ClientRunJobFlowTagsTypeDef",
    "ClusterRunningWaitWaiterConfigTypeDef",
    "ClusterTerminatedWaitWaiterConfigTypeDef",
    "ListBootstrapActionsPaginatePaginationConfigTypeDef",
    "ListBootstrapActionsPaginateResponseBootstrapActionsTypeDef",
    "ListBootstrapActionsPaginateResponseTypeDef",
    "ListClustersPaginatePaginationConfigTypeDef",
    "ListClustersPaginateResponseClustersStatusStateChangeReasonTypeDef",
    "ListClustersPaginateResponseClustersStatusTimelineTypeDef",
    "ListClustersPaginateResponseClustersStatusTypeDef",
    "ListClustersPaginateResponseClustersTypeDef",
    "ListClustersPaginateResponseTypeDef",
    "ListInstanceFleetsPaginatePaginationConfigTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsStatusStateChangeReasonTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsStatusTimelineTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsStatusTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsTypeDef",
    "ListInstanceFleetsPaginateResponseTypeDef",
    "ListInstanceGroupsPaginatePaginationConfigTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsConfigurationsTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsStatusStateChangeReasonTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsStatusTimelineTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsStatusTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsTypeDef",
    "ListInstanceGroupsPaginateResponseTypeDef",
    "ListInstancesPaginatePaginationConfigTypeDef",
    "ListInstancesPaginateResponseInstancesEbsVolumesTypeDef",
    "ListInstancesPaginateResponseInstancesStatusStateChangeReasonTypeDef",
    "ListInstancesPaginateResponseInstancesStatusTimelineTypeDef",
    "ListInstancesPaginateResponseInstancesStatusTypeDef",
    "ListInstancesPaginateResponseInstancesTypeDef",
    "ListInstancesPaginateResponseTypeDef",
    "ListSecurityConfigurationsPaginatePaginationConfigTypeDef",
    "ListSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef",
    "ListSecurityConfigurationsPaginateResponseTypeDef",
    "ListStepsPaginatePaginationConfigTypeDef",
    "ListStepsPaginateResponseStepsConfigTypeDef",
    "ListStepsPaginateResponseStepsStatusFailureDetailsTypeDef",
    "ListStepsPaginateResponseStepsStatusStateChangeReasonTypeDef",
    "ListStepsPaginateResponseStepsStatusTimelineTypeDef",
    "ListStepsPaginateResponseStepsStatusTypeDef",
    "ListStepsPaginateResponseStepsTypeDef",
    "ListStepsPaginateResponseTypeDef",
    "StepCompleteWaitWaiterConfigTypeDef",
)


_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef = TypedDict(
    "_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)


class ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef(
    _ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef
):
    pass


_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)


class ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef(
    _ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef
):
    pass


_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {
        "VolumeSpecification": ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
        "VolumesPerInstance": int,
    },
    total=False,
)


class ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef(
    _ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef
):
    pass


_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef = TypedDict(
    "_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List[
            ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)


class ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef(
    _ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef
):
    pass


_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef = TypedDict(
    "_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "EbsConfiguration": ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef,
        "Configurations": List[
            ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef(
    _ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef
):
    pass


_ClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef = TypedDict(
    "_ClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": int,
        "TimeoutAction": Literal["SWITCH_TO_ON_DEMAND", "TERMINATE_CLUSTER"],
        "BlockDurationMinutes": int,
    },
    total=False,
)


class ClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef(
    _ClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef
):
    pass


_ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef = TypedDict(
    "_ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef",
    {
        "SpotSpecification": ClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef
    },
    total=False,
)


class ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef(
    _ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef
):
    pass


_ClientAddInstanceFleetInstanceFleetTypeDef = TypedDict(
    "_ClientAddInstanceFleetInstanceFleetTypeDef",
    {
        "Name": str,
        "InstanceFleetType": Literal["MASTER", "CORE", "TASK"],
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "InstanceTypeConfigs": List[ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef],
        "LaunchSpecifications": ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef,
    },
    total=False,
)


class ClientAddInstanceFleetInstanceFleetTypeDef(_ClientAddInstanceFleetInstanceFleetTypeDef):
    """
    Specifies the configuration of the instance fleet.
    - **Name** *(string) --*

      The friendly name of the instance fleet.
    """


_ClientAddInstanceFleetResponseTypeDef = TypedDict(
    "_ClientAddInstanceFleetResponseTypeDef",
    {"ClusterId": str, "InstanceFleetId": str, "ClusterArn": str},
    total=False,
)


class ClientAddInstanceFleetResponseTypeDef(_ClientAddInstanceFleetResponseTypeDef):
    """
    - *(dict) --*

      - **ClusterId** *(string) --*

        The unique identifier of the cluster.
    """


_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef
):
    pass


_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal[
            "CHANGE_IN_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY", "EXACT_CAPACITY"
        ],
        "ScalingAdjustment": int,
        "CoolDown": int,
    },
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef
):
    pass


_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": Literal["ON_DEMAND", "SPOT"],
        "SimpleScalingPolicyConfiguration": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef
):
    pass


_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
):
    pass


_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": Literal[
            "GREATER_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ],
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": Literal["SAMPLE_COUNT", "AVERAGE", "SUM", "MINIMUM", "MAXIMUM"],
        "Threshold": float,
        "Unit": Literal[
            "NONE",
            "SECONDS",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "BYTES",
            "KILO_BYTES",
            "MEGA_BYTES",
            "GIGA_BYTES",
            "TERA_BYTES",
            "BITS",
            "KILO_BITS",
            "MEGA_BITS",
            "GIGA_BITS",
            "TERA_BITS",
            "PERCENT",
            "COUNT",
            "BYTES_PER_SECOND",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BYTES_PER_SECOND",
            "GIGA_BYTES_PER_SECOND",
            "TERA_BYTES_PER_SECOND",
            "BITS_PER_SECOND",
            "KILO_BITS_PER_SECOND",
            "MEGA_BITS_PER_SECOND",
            "GIGA_BITS_PER_SECOND",
            "TERA_BITS_PER_SECOND",
            "COUNT_PER_SECOND",
        ],
        "Dimensions": List[
            ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
):
    pass


_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef
):
    pass


_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef
):
    pass


_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef",
    {
        "Constraints": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef],
    },
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef
):
    pass


_ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef
):
    pass


_ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef
):
    pass


_ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {
        "VolumeSpecification": ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
        "VolumesPerInstance": int,
    },
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef
):
    pass


_ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List[
            ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef
):
    pass


_ClientAddInstanceGroupsInstanceGroupsTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsTypeDef",
    {
        "Name": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceRole": Literal["MASTER", "CORE", "TASK"],
        "BidPrice": str,
        "InstanceType": str,
        "InstanceCount": int,
        "Configurations": List[ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef],
        "EbsConfiguration": ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef,
        "AutoScalingPolicy": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef,
    },
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsTypeDef(_ClientAddInstanceGroupsInstanceGroupsTypeDef):
    """
    - *(dict) --*

      Configuration defining a new instance group.
      - **Name** *(string) --*

        Friendly name given to the instance group.
    """


_ClientAddInstanceGroupsResponseTypeDef = TypedDict(
    "_ClientAddInstanceGroupsResponseTypeDef",
    {"JobFlowId": str, "InstanceGroupIds": List[str], "ClusterArn": str},
    total=False,
)


class ClientAddInstanceGroupsResponseTypeDef(_ClientAddInstanceGroupsResponseTypeDef):
    """
    - *(dict) --*

      Output from an AddInstanceGroups call.
      - **JobFlowId** *(string) --*

        The job flow ID in which the instance groups are added.
    """


_ClientAddJobFlowStepsResponseTypeDef = TypedDict(
    "_ClientAddJobFlowStepsResponseTypeDef", {"StepIds": List[str]}, total=False
)


class ClientAddJobFlowStepsResponseTypeDef(_ClientAddJobFlowStepsResponseTypeDef):
    """
    - *(dict) --*

      The output for the  AddJobFlowSteps operation.
      - **StepIds** *(list) --*

        The identifiers of the list of steps added to the job flow.
        - *(string) --*
    """


_ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef = TypedDict(
    "_ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef(
    _ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef
):
    pass


_ClientAddJobFlowStepsStepsHadoopJarStepTypeDef = TypedDict(
    "_ClientAddJobFlowStepsStepsHadoopJarStepTypeDef",
    {
        "Properties": List[ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef],
        "Jar": str,
        "MainClass": str,
        "Args": List[str],
    },
    total=False,
)


class ClientAddJobFlowStepsStepsHadoopJarStepTypeDef(
    _ClientAddJobFlowStepsStepsHadoopJarStepTypeDef
):
    pass


_RequiredClientAddJobFlowStepsStepsTypeDef = TypedDict(
    "_RequiredClientAddJobFlowStepsStepsTypeDef", {"Name": str}
)
_OptionalClientAddJobFlowStepsStepsTypeDef = TypedDict(
    "_OptionalClientAddJobFlowStepsStepsTypeDef",
    {
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "HadoopJarStep": ClientAddJobFlowStepsStepsHadoopJarStepTypeDef,
    },
    total=False,
)


class ClientAddJobFlowStepsStepsTypeDef(
    _RequiredClientAddJobFlowStepsStepsTypeDef, _OptionalClientAddJobFlowStepsStepsTypeDef
):
    """
    - *(dict) --*

      Specification of a cluster (job flow) step.
      - **Name** *(string) --***[REQUIRED]**

        The name of the step.
    """


_ClientAddTagsTagsTypeDef = TypedDict(
    "_ClientAddTagsTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsTagsTypeDef(_ClientAddTagsTagsTypeDef):
    """
    - *(dict) --*

      A key/value pair containing user-defined metadata that you can associate with an Amazon EMR
      resource. Tags make it easier to associate clusters in various ways, such as grouping clusters
      to track your Amazon EMR resource allocation costs. For more information, see `Tag Clusters
      <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .
      - **Key** *(string) --*

        A user-defined key, which is the minimum required information for a valid tag. For more
        information, see `Tag
        <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .
    """


_ClientCancelStepsResponseCancelStepsInfoListTypeDef = TypedDict(
    "_ClientCancelStepsResponseCancelStepsInfoListTypeDef",
    {"StepId": str, "Status": Literal["SUBMITTED", "FAILED"], "Reason": str},
    total=False,
)


class ClientCancelStepsResponseCancelStepsInfoListTypeDef(
    _ClientCancelStepsResponseCancelStepsInfoListTypeDef
):
    """
    - *(dict) --*

      Specification of the status of a CancelSteps request. Available only in Amazon EMR version
      4.8.0 and later, excluding version 5.0.0.
      - **StepId** *(string) --*

        The encrypted StepId of a step.
    """


_ClientCancelStepsResponseTypeDef = TypedDict(
    "_ClientCancelStepsResponseTypeDef",
    {"CancelStepsInfoList": List[ClientCancelStepsResponseCancelStepsInfoListTypeDef]},
    total=False,
)


class ClientCancelStepsResponseTypeDef(_ClientCancelStepsResponseTypeDef):
    """
    - *(dict) --*

      The output for the  CancelSteps operation.
      - **CancelStepsInfoList** *(list) --*

        A list of  CancelStepsInfo , which shows the status of specified cancel requests for each
        ``StepID`` specified.
        - *(dict) --*

          Specification of the status of a CancelSteps request. Available only in Amazon EMR version
          4.8.0 and later, excluding version 5.0.0.
          - **StepId** *(string) --*

            The encrypted StepId of a step.
    """


_ClientCreateSecurityConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateSecurityConfigurationResponseTypeDef",
    {"Name": str, "CreationDateTime": datetime},
    total=False,
)


class ClientCreateSecurityConfigurationResponseTypeDef(
    _ClientCreateSecurityConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the security configuration.
    """


_ClientDescribeClusterResponseClusterApplicationsTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterApplicationsTypeDef",
    {"Name": str, "Version": str, "Args": List[str], "AdditionalInfo": Dict[str, str]},
    total=False,
)


class ClientDescribeClusterResponseClusterApplicationsTypeDef(
    _ClientDescribeClusterResponseClusterApplicationsTypeDef
):
    pass


_ClientDescribeClusterResponseClusterConfigurationsTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)


class ClientDescribeClusterResponseClusterConfigurationsTypeDef(
    _ClientDescribeClusterResponseClusterConfigurationsTypeDef
):
    pass


_ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef",
    {
        "Ec2KeyName": str,
        "Ec2SubnetId": str,
        "RequestedEc2SubnetIds": List[str],
        "Ec2AvailabilityZone": str,
        "RequestedEc2AvailabilityZones": List[str],
        "IamInstanceProfile": str,
        "EmrManagedMasterSecurityGroup": str,
        "EmrManagedSlaveSecurityGroup": str,
        "ServiceAccessSecurityGroup": str,
        "AdditionalMasterSecurityGroups": List[str],
        "AdditionalSlaveSecurityGroups": List[str],
    },
    total=False,
)


class ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef(
    _ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef
):
    pass


_ClientDescribeClusterResponseClusterKerberosAttributesTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterKerberosAttributesTypeDef",
    {
        "Realm": str,
        "KdcAdminPassword": str,
        "CrossRealmTrustPrincipalPassword": str,
        "ADDomainJoinUser": str,
        "ADDomainJoinPassword": str,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterKerberosAttributesTypeDef(
    _ClientDescribeClusterResponseClusterKerberosAttributesTypeDef
):
    pass


_ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
            "INSTANCE_FAILURE",
            "INSTANCE_FLEET_TIMEOUT",
            "BOOTSTRAP_FAILURE",
            "USER_REQUEST",
            "STEP_FAILURE",
            "ALL_STEPS_COMPLETED",
        ],
        "Message": str,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef(
    _ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef
):
    pass


_ClientDescribeClusterResponseClusterStatusTimelineTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientDescribeClusterResponseClusterStatusTimelineTypeDef(
    _ClientDescribeClusterResponseClusterStatusTimelineTypeDef
):
    pass


_ClientDescribeClusterResponseClusterStatusTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterStatusTypeDef",
    {
        "State": Literal[
            "STARTING",
            "BOOTSTRAPPING",
            "RUNNING",
            "WAITING",
            "TERMINATING",
            "TERMINATED",
            "TERMINATED_WITH_ERRORS",
        ],
        "StateChangeReason": ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef,
        "Timeline": ClientDescribeClusterResponseClusterStatusTimelineTypeDef,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterStatusTypeDef(
    _ClientDescribeClusterResponseClusterStatusTypeDef
):
    pass


_ClientDescribeClusterResponseClusterTagsTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeClusterResponseClusterTagsTypeDef(
    _ClientDescribeClusterResponseClusterTagsTypeDef
):
    pass


_ClientDescribeClusterResponseClusterTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ClientDescribeClusterResponseClusterStatusTypeDef,
        "Ec2InstanceAttributes": ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef,
        "InstanceCollectionType": Literal["INSTANCE_FLEET", "INSTANCE_GROUP"],
        "LogUri": str,
        "RequestedAmiVersion": str,
        "RunningAmiVersion": str,
        "ReleaseLabel": str,
        "AutoTerminate": bool,
        "TerminationProtected": bool,
        "VisibleToAllUsers": bool,
        "Applications": List[ClientDescribeClusterResponseClusterApplicationsTypeDef],
        "Tags": List[ClientDescribeClusterResponseClusterTagsTypeDef],
        "ServiceRole": str,
        "NormalizedInstanceHours": int,
        "MasterPublicDnsName": str,
        "Configurations": List[ClientDescribeClusterResponseClusterConfigurationsTypeDef],
        "SecurityConfiguration": str,
        "AutoScalingRole": str,
        "ScaleDownBehavior": Literal["TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"],
        "CustomAmiId": str,
        "EbsRootVolumeSize": int,
        "RepoUpgradeOnBoot": Literal["SECURITY", "NONE"],
        "KerberosAttributes": ClientDescribeClusterResponseClusterKerberosAttributesTypeDef,
        "ClusterArn": str,
        "StepConcurrencyLevel": int,
        "OutpostArn": str,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterTypeDef(_ClientDescribeClusterResponseClusterTypeDef):
    """
    - **Cluster** *(dict) --*

      This output contains the details for the requested cluster.
      - **Id** *(string) --*

        The unique identifier for the cluster.
    """


_ClientDescribeClusterResponseTypeDef = TypedDict(
    "_ClientDescribeClusterResponseTypeDef",
    {"Cluster": ClientDescribeClusterResponseClusterTypeDef},
    total=False,
)


class ClientDescribeClusterResponseTypeDef(_ClientDescribeClusterResponseTypeDef):
    """
    - *(dict) --*

      This output contains the description of the cluster.
      - **Cluster** *(dict) --*

        This output contains the details for the requested cluster.
        - **Id** *(string) --*

          The unique identifier for the cluster.
    """


_ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef",
    {"Path": str, "Args": List[str]},
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef
):
    pass


_ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef",
    {
        "Name": str,
        "ScriptBootstrapAction": ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef
):
    pass


_ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef",
    {
        "BootstrapActionConfig": ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef
):
    pass


_ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef",
    {
        "State": Literal[
            "STARTING",
            "BOOTSTRAPPING",
            "RUNNING",
            "WAITING",
            "SHUTTING_DOWN",
            "TERMINATED",
            "COMPLETED",
            "FAILED",
        ],
        "CreationDateTime": datetime,
        "StartDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
        "LastStateChangeReason": str,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef
):
    pass


_ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef",
    {
        "InstanceGroupId": str,
        "Name": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceRole": Literal["MASTER", "CORE", "TASK"],
        "BidPrice": str,
        "InstanceType": str,
        "InstanceRequestCount": int,
        "InstanceRunningCount": int,
        "State": Literal[
            "PROVISIONING",
            "BOOTSTRAPPING",
            "RUNNING",
            "RECONFIGURING",
            "RESIZING",
            "SUSPENDED",
            "TERMINATING",
            "TERMINATED",
            "ARRESTED",
            "SHUTTING_DOWN",
            "ENDED",
        ],
        "LastStateChangeReason": str,
        "CreationDateTime": datetime,
        "StartDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef
):
    pass


_ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef",
    {"AvailabilityZone": str, "AvailabilityZones": List[str]},
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef
):
    pass


_ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef",
    {
        "MasterInstanceType": str,
        "MasterPublicDnsName": str,
        "MasterInstanceId": str,
        "SlaveInstanceType": str,
        "InstanceCount": int,
        "InstanceGroups": List[
            ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef
        ],
        "NormalizedInstanceHours": int,
        "Ec2KeyName": str,
        "Ec2SubnetId": str,
        "Placement": ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef,
        "KeepJobFlowAliveWhenNoSteps": bool,
        "TerminationProtected": bool,
        "HadoopVersion": str,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef
):
    pass


_ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef",
    {
        "State": Literal[
            "PENDING", "RUNNING", "CONTINUE", "COMPLETED", "CANCELLED", "FAILED", "INTERRUPTED"
        ],
        "CreationDateTime": datetime,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
        "LastStateChangeReason": str,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef
):
    pass


_ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef
):
    pass


_ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef",
    {
        "Properties": List[
            ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef
        ],
        "Jar": str,
        "MainClass": str,
        "Args": List[str],
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef
):
    pass


_ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef",
    {
        "Name": str,
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "HadoopJarStep": ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef
):
    pass


_ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef",
    {
        "StepConfig": ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef,
        "ExecutionStatusDetail": ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef
):
    pass


_ClientDescribeJobFlowsResponseJobFlowsTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsTypeDef",
    {
        "JobFlowId": str,
        "Name": str,
        "LogUri": str,
        "AmiVersion": str,
        "ExecutionStatusDetail": ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef,
        "Instances": ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef,
        "Steps": List[ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef],
        "BootstrapActions": List[ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef],
        "SupportedProducts": List[str],
        "VisibleToAllUsers": bool,
        "JobFlowRole": str,
        "ServiceRole": str,
        "AutoScalingRole": str,
        "ScaleDownBehavior": Literal["TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"],
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsTypeDef(_ClientDescribeJobFlowsResponseJobFlowsTypeDef):
    """
    - *(dict) --*

      A description of a cluster (job flow).
      - **JobFlowId** *(string) --*

        The job flow identifier.
    """


_ClientDescribeJobFlowsResponseTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseTypeDef",
    {"JobFlows": List[ClientDescribeJobFlowsResponseJobFlowsTypeDef]},
    total=False,
)


class ClientDescribeJobFlowsResponseTypeDef(_ClientDescribeJobFlowsResponseTypeDef):
    """
    - *(dict) --*

      The output for the  DescribeJobFlows operation.
      - **JobFlows** *(list) --*

        A list of job flows matching the parameters supplied.
        - *(dict) --*

          A description of a cluster (job flow).
          - **JobFlowId** *(string) --*

            The job flow identifier.
    """


_ClientDescribeSecurityConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeSecurityConfigurationResponseTypeDef",
    {"Name": str, "SecurityConfiguration": str, "CreationDateTime": datetime},
    total=False,
)


class ClientDescribeSecurityConfigurationResponseTypeDef(
    _ClientDescribeSecurityConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the security configuration.
    """


_ClientDescribeStepResponseStepConfigTypeDef = TypedDict(
    "_ClientDescribeStepResponseStepConfigTypeDef",
    {"Jar": str, "Properties": Dict[str, str], "MainClass": str, "Args": List[str]},
    total=False,
)


class ClientDescribeStepResponseStepConfigTypeDef(_ClientDescribeStepResponseStepConfigTypeDef):
    pass


_ClientDescribeStepResponseStepStatusFailureDetailsTypeDef = TypedDict(
    "_ClientDescribeStepResponseStepStatusFailureDetailsTypeDef",
    {"Reason": str, "Message": str, "LogFile": str},
    total=False,
)


class ClientDescribeStepResponseStepStatusFailureDetailsTypeDef(
    _ClientDescribeStepResponseStepStatusFailureDetailsTypeDef
):
    pass


_ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef(
    _ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef
):
    pass


_ClientDescribeStepResponseStepStatusTimelineTypeDef = TypedDict(
    "_ClientDescribeStepResponseStepStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "StartDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientDescribeStepResponseStepStatusTimelineTypeDef(
    _ClientDescribeStepResponseStepStatusTimelineTypeDef
):
    pass


_ClientDescribeStepResponseStepStatusTypeDef = TypedDict(
    "_ClientDescribeStepResponseStepStatusTypeDef",
    {
        "State": Literal[
            "PENDING",
            "CANCEL_PENDING",
            "RUNNING",
            "COMPLETED",
            "CANCELLED",
            "FAILED",
            "INTERRUPTED",
        ],
        "StateChangeReason": ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef,
        "FailureDetails": ClientDescribeStepResponseStepStatusFailureDetailsTypeDef,
        "Timeline": ClientDescribeStepResponseStepStatusTimelineTypeDef,
    },
    total=False,
)


class ClientDescribeStepResponseStepStatusTypeDef(_ClientDescribeStepResponseStepStatusTypeDef):
    pass


_ClientDescribeStepResponseStepTypeDef = TypedDict(
    "_ClientDescribeStepResponseStepTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": ClientDescribeStepResponseStepConfigTypeDef,
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "Status": ClientDescribeStepResponseStepStatusTypeDef,
    },
    total=False,
)


class ClientDescribeStepResponseStepTypeDef(_ClientDescribeStepResponseStepTypeDef):
    """
    - **Step** *(dict) --*

      The step details for the requested step identifier.
      - **Id** *(string) --*

        The identifier of the cluster step.
    """


_ClientDescribeStepResponseTypeDef = TypedDict(
    "_ClientDescribeStepResponseTypeDef",
    {"Step": ClientDescribeStepResponseStepTypeDef},
    total=False,
)


class ClientDescribeStepResponseTypeDef(_ClientDescribeStepResponseTypeDef):
    """
    - *(dict) --*

      This output contains the description of the cluster step.
      - **Step** *(dict) --*

        The step details for the requested step identifier.
        - **Id** *(string) --*

          The identifier of the cluster step.
    """


_ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef = TypedDict(
    "_ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef",
    {"CreationDateTime": datetime, "CreatedByArn": str},
    total=False,
)


class ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef(
    _ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef
):
    pass


_ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef = TypedDict(
    "_ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef",
    {"MinRange": int, "MaxRange": int},
    total=False,
)


class ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef(
    _ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef
):
    pass


_ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef",
    {
        "BlockPublicSecurityGroupRules": bool,
        "PermittedPublicSecurityGroupRuleRanges": List[
            ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef
        ],
    },
    total=False,
)


class ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef(
    _ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef
):
    """
    - **BlockPublicAccessConfiguration** *(dict) --*

      A configuration for Amazon EMR block public access. The configuration applies to all clusters
      created in your account for the current Region. The configuration specifies whether block
      public access is enabled. If block public access is enabled, security groups associated with
      the cluster cannot have rules that allow inbound traffic from 0.0.0.0/0 or ::/0 on a port,
      unless the port is specified as an exception using ``PermittedPublicSecurityGroupRuleRanges``
      in the ``BlockPublicAccessConfiguration`` . By default, Port 22 (SSH) is an exception, and
      public access is allowed on this port. You can change this by updating the block public access
      configuration to remove the exception.
      - **BlockPublicSecurityGroupRules** *(boolean) --*

        Indicates whether EMR block public access is enabled (``true`` ) or disabled (``false`` ).
        By default, the value is ``false`` for accounts that have created EMR clusters before July
        2019. For accounts created after this, the default is ``true`` .
    """


_ClientGetBlockPublicAccessConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBlockPublicAccessConfigurationResponseTypeDef",
    {
        "BlockPublicAccessConfiguration": ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef,
        "BlockPublicAccessConfigurationMetadata": ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef,
    },
    total=False,
)


class ClientGetBlockPublicAccessConfigurationResponseTypeDef(
    _ClientGetBlockPublicAccessConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **BlockPublicAccessConfiguration** *(dict) --*

        A configuration for Amazon EMR block public access. The configuration applies to all
        clusters created in your account for the current Region. The configuration specifies whether
        block public access is enabled. If block public access is enabled, security groups
        associated with the cluster cannot have rules that allow inbound traffic from 0.0.0.0/0 or
        ::/0 on a port, unless the port is specified as an exception using
        ``PermittedPublicSecurityGroupRuleRanges`` in the ``BlockPublicAccessConfiguration`` . By
        default, Port 22 (SSH) is an exception, and public access is allowed on this port. You can
        change this by updating the block public access configuration to remove the exception.
        - **BlockPublicSecurityGroupRules** *(boolean) --*

          Indicates whether EMR block public access is enabled (``true`` ) or disabled (``false`` ).
          By default, the value is ``false`` for accounts that have created EMR clusters before July
          2019. For accounts created after this, the default is ``true`` .
    """


_ClientListBootstrapActionsResponseBootstrapActionsTypeDef = TypedDict(
    "_ClientListBootstrapActionsResponseBootstrapActionsTypeDef",
    {"Name": str, "ScriptPath": str, "Args": List[str]},
    total=False,
)


class ClientListBootstrapActionsResponseBootstrapActionsTypeDef(
    _ClientListBootstrapActionsResponseBootstrapActionsTypeDef
):
    """
    - *(dict) --*

      An entity describing an executable that runs on a cluster.
      - **Name** *(string) --*

        The name of the command.
    """


_ClientListBootstrapActionsResponseTypeDef = TypedDict(
    "_ClientListBootstrapActionsResponseTypeDef",
    {
        "BootstrapActions": List[ClientListBootstrapActionsResponseBootstrapActionsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientListBootstrapActionsResponseTypeDef(_ClientListBootstrapActionsResponseTypeDef):
    """
    - *(dict) --*

      This output contains the bootstrap actions detail.
      - **BootstrapActions** *(list) --*

        The bootstrap actions associated with the cluster.
        - *(dict) --*

          An entity describing an executable that runs on a cluster.
          - **Name** *(string) --*

            The name of the command.
    """


_ClientListClustersResponseClustersStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientListClustersResponseClustersStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
            "INSTANCE_FAILURE",
            "INSTANCE_FLEET_TIMEOUT",
            "BOOTSTRAP_FAILURE",
            "USER_REQUEST",
            "STEP_FAILURE",
            "ALL_STEPS_COMPLETED",
        ],
        "Message": str,
    },
    total=False,
)


class ClientListClustersResponseClustersStatusStateChangeReasonTypeDef(
    _ClientListClustersResponseClustersStatusStateChangeReasonTypeDef
):
    pass


_ClientListClustersResponseClustersStatusTimelineTypeDef = TypedDict(
    "_ClientListClustersResponseClustersStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientListClustersResponseClustersStatusTimelineTypeDef(
    _ClientListClustersResponseClustersStatusTimelineTypeDef
):
    pass


_ClientListClustersResponseClustersStatusTypeDef = TypedDict(
    "_ClientListClustersResponseClustersStatusTypeDef",
    {
        "State": Literal[
            "STARTING",
            "BOOTSTRAPPING",
            "RUNNING",
            "WAITING",
            "TERMINATING",
            "TERMINATED",
            "TERMINATED_WITH_ERRORS",
        ],
        "StateChangeReason": ClientListClustersResponseClustersStatusStateChangeReasonTypeDef,
        "Timeline": ClientListClustersResponseClustersStatusTimelineTypeDef,
    },
    total=False,
)


class ClientListClustersResponseClustersStatusTypeDef(
    _ClientListClustersResponseClustersStatusTypeDef
):
    pass


_ClientListClustersResponseClustersTypeDef = TypedDict(
    "_ClientListClustersResponseClustersTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ClientListClustersResponseClustersStatusTypeDef,
        "NormalizedInstanceHours": int,
        "ClusterArn": str,
        "OutpostArn": str,
    },
    total=False,
)


class ClientListClustersResponseClustersTypeDef(_ClientListClustersResponseClustersTypeDef):
    """
    - *(dict) --*

      The summary description of the cluster.
      - **Id** *(string) --*

        The unique identifier for the cluster.
    """


_ClientListClustersResponseTypeDef = TypedDict(
    "_ClientListClustersResponseTypeDef",
    {"Clusters": List[ClientListClustersResponseClustersTypeDef], "Marker": str},
    total=False,
)


class ClientListClustersResponseTypeDef(_ClientListClustersResponseTypeDef):
    """
    - *(dict) --*

      This contains a ClusterSummaryList with the cluster details; for example, the cluster IDs,
      names, and status.
      - **Clusters** *(list) --*

        The list of clusters for the account based on the given filters.
        - *(dict) --*

          The summary description of the cluster.
          - **Id** *(string) --*

            The unique identifier for the cluster.
    """


_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef
):
    pass


_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef
):
    pass


_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef",
    {
        "VolumeSpecification": ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef,
        "Device": str,
    },
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef
):
    pass


_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "Configurations": List[
            ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef
        ],
        "EbsBlockDevices": List[
            ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef
):
    pass


_ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": int,
        "TimeoutAction": Literal["SWITCH_TO_ON_DEMAND", "TERMINATE_CLUSTER"],
        "BlockDurationMinutes": int,
    },
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef
):
    pass


_ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef",
    {
        "SpotSpecification": ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef
    },
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef
):
    pass


_ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR", "VALIDATION_ERROR", "INSTANCE_FAILURE", "CLUSTER_TERMINATED"
        ],
        "Message": str,
    },
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef
):
    pass


_ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef
):
    pass


_ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef",
    {
        "State": Literal[
            "PROVISIONING",
            "BOOTSTRAPPING",
            "RUNNING",
            "RESIZING",
            "SUSPENDED",
            "TERMINATING",
            "TERMINATED",
        ],
        "StateChangeReason": ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef,
        "Timeline": ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef,
    },
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef
):
    pass


_ClientListInstanceFleetsResponseInstanceFleetsTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef,
        "InstanceFleetType": Literal["MASTER", "CORE", "TASK"],
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "ProvisionedOnDemandCapacity": int,
        "ProvisionedSpotCapacity": int,
        "InstanceTypeSpecifications": List[
            ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef
        ],
        "LaunchSpecifications": ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef,
    },
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsTypeDef
):
    """
    - *(dict) --*

      Describes an instance fleet, which is a group of EC2 instances that host a particular node
      type (master, core, or task) in an Amazon EMR cluster. Instance fleets can consist of a mix of
      instance types and On-Demand and Spot instances, which are provisioned to meet a defined
      target capacity.
      .. note::

        The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later,
        excluding 5.0.x versions.
    """


_ClientListInstanceFleetsResponseTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseTypeDef",
    {"InstanceFleets": List[ClientListInstanceFleetsResponseInstanceFleetsTypeDef], "Marker": str},
    total=False,
)


class ClientListInstanceFleetsResponseTypeDef(_ClientListInstanceFleetsResponseTypeDef):
    """
    - *(dict) --*

      - **InstanceFleets** *(list) --*

        The list of instance fleets for the cluster and given filters.
        - *(dict) --*

          Describes an instance fleet, which is a group of EC2 instances that host a particular node
          type (master, core, or task) in an Amazon EMR cluster. Instance fleets can consist of a
          mix of instance types and On-Demand and Spot instances, which are provisioned to meet a
          defined target capacity.
          .. note::

            The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
            later, excluding 5.0.x versions.
    """


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal[
            "CHANGE_IN_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY", "EXACT_CAPACITY"
        ],
        "ScalingAdjustment": int,
        "CoolDown": int,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": Literal["ON_DEMAND", "SPOT"],
        "SimpleScalingPolicyConfiguration": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": Literal[
            "GREATER_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ],
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": Literal["SAMPLE_COUNT", "AVERAGE", "SUM", "MINIMUM", "MAXIMUM"],
        "Threshold": float,
        "Unit": Literal[
            "NONE",
            "SECONDS",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "BYTES",
            "KILO_BYTES",
            "MEGA_BYTES",
            "GIGA_BYTES",
            "TERA_BYTES",
            "BITS",
            "KILO_BITS",
            "MEGA_BITS",
            "GIGA_BITS",
            "TERA_BITS",
            "PERCENT",
            "COUNT",
            "BYTES_PER_SECOND",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BYTES_PER_SECOND",
            "GIGA_BYTES_PER_SECOND",
            "TERA_BYTES_PER_SECOND",
            "BITS_PER_SECOND",
            "KILO_BITS_PER_SECOND",
            "MEGA_BITS_PER_SECOND",
            "GIGA_BITS_PER_SECOND",
            "TERA_BITS_PER_SECOND",
            "COUNT_PER_SECOND",
        ],
        "Dimensions": List[
            ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef",
    {"Code": Literal["USER_REQUEST", "PROVISION_FAILURE", "CLEANUP_FAILURE"], "Message": str},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef",
    {
        "State": Literal["PENDING", "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", "FAILED"],
        "StateChangeReason": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef",
    {
        "Status": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef,
        "Constraints": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef],
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef",
    {
        "VolumeSpecification": ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef,
        "Device": str,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    {
        "InstancesToTerminate": List[str],
        "InstancesToProtect": List[str],
        "InstanceTerminationTimeout": int,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef",
    {
        "DecommissionTimeout": int,
        "InstanceResizePolicy": ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR", "VALIDATION_ERROR", "INSTANCE_FAILURE", "CLUSTER_TERMINATED"
        ],
        "Message": str,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef",
    {
        "State": Literal[
            "PROVISIONING",
            "BOOTSTRAPPING",
            "RUNNING",
            "RECONFIGURING",
            "RESIZING",
            "SUSPENDED",
            "TERMINATING",
            "TERMINATED",
            "ARRESTED",
            "SHUTTING_DOWN",
            "ENDED",
        ],
        "StateChangeReason": ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef,
        "Timeline": ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef
):
    pass


_ClientListInstanceGroupsResponseInstanceGroupsTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceGroupType": Literal["MASTER", "CORE", "TASK"],
        "BidPrice": str,
        "InstanceType": str,
        "RequestedInstanceCount": int,
        "RunningInstanceCount": int,
        "Status": ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef,
        "Configurations": List[ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef],
        "ConfigurationsVersion": int,
        "LastSuccessfullyAppliedConfigurations": List[
            ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef
        ],
        "LastSuccessfullyAppliedConfigurationsVersion": int,
        "EbsBlockDevices": List[
            ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef
        ],
        "EbsOptimized": bool,
        "ShrinkPolicy": ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef,
        "AutoScalingPolicy": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsTypeDef
):
    """
    - *(dict) --*

      This entity represents an instance group, which is a group of instances that have common
      purpose. For example, CORE instance group is used for HDFS.
      - **Id** *(string) --*

        The identifier of the instance group.
    """


_ClientListInstanceGroupsResponseTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseTypeDef",
    {"InstanceGroups": List[ClientListInstanceGroupsResponseInstanceGroupsTypeDef], "Marker": str},
    total=False,
)


class ClientListInstanceGroupsResponseTypeDef(_ClientListInstanceGroupsResponseTypeDef):
    """
    - *(dict) --*

      This input determines which instance groups to retrieve.
      - **InstanceGroups** *(list) --*

        The list of instance groups for the cluster and given filters.
        - *(dict) --*

          This entity represents an instance group, which is a group of instances that have common
          purpose. For example, CORE instance group is used for HDFS.
          - **Id** *(string) --*

            The identifier of the instance group.
    """


_ClientListInstancesResponseInstancesEbsVolumesTypeDef = TypedDict(
    "_ClientListInstancesResponseInstancesEbsVolumesTypeDef",
    {"Device": str, "VolumeId": str},
    total=False,
)


class ClientListInstancesResponseInstancesEbsVolumesTypeDef(
    _ClientListInstancesResponseInstancesEbsVolumesTypeDef
):
    pass


_ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
            "INSTANCE_FAILURE",
            "BOOTSTRAP_FAILURE",
            "CLUSTER_TERMINATED",
        ],
        "Message": str,
    },
    total=False,
)


class ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef(
    _ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef
):
    pass


_ClientListInstancesResponseInstancesStatusTimelineTypeDef = TypedDict(
    "_ClientListInstancesResponseInstancesStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientListInstancesResponseInstancesStatusTimelineTypeDef(
    _ClientListInstancesResponseInstancesStatusTimelineTypeDef
):
    pass


_ClientListInstancesResponseInstancesStatusTypeDef = TypedDict(
    "_ClientListInstancesResponseInstancesStatusTypeDef",
    {
        "State": Literal[
            "AWAITING_FULFILLMENT", "PROVISIONING", "BOOTSTRAPPING", "RUNNING", "TERMINATED"
        ],
        "StateChangeReason": ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef,
        "Timeline": ClientListInstancesResponseInstancesStatusTimelineTypeDef,
    },
    total=False,
)


class ClientListInstancesResponseInstancesStatusTypeDef(
    _ClientListInstancesResponseInstancesStatusTypeDef
):
    pass


_ClientListInstancesResponseInstancesTypeDef = TypedDict(
    "_ClientListInstancesResponseInstancesTypeDef",
    {
        "Id": str,
        "Ec2InstanceId": str,
        "PublicDnsName": str,
        "PublicIpAddress": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "Status": ClientListInstancesResponseInstancesStatusTypeDef,
        "InstanceGroupId": str,
        "InstanceFleetId": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceType": str,
        "EbsVolumes": List[ClientListInstancesResponseInstancesEbsVolumesTypeDef],
    },
    total=False,
)


class ClientListInstancesResponseInstancesTypeDef(_ClientListInstancesResponseInstancesTypeDef):
    """
    - *(dict) --*

      Represents an EC2 instance provisioned as part of cluster.
      - **Id** *(string) --*

        The unique identifier for the instance in Amazon EMR.
    """


_ClientListInstancesResponseTypeDef = TypedDict(
    "_ClientListInstancesResponseTypeDef",
    {"Instances": List[ClientListInstancesResponseInstancesTypeDef], "Marker": str},
    total=False,
)


class ClientListInstancesResponseTypeDef(_ClientListInstancesResponseTypeDef):
    """
    - *(dict) --*

      This output contains the list of instances.
      - **Instances** *(list) --*

        The list of instances for the cluster and given filters.
        - *(dict) --*

          Represents an EC2 instance provisioned as part of cluster.
          - **Id** *(string) --*

            The unique identifier for the instance in Amazon EMR.
    """


_ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef = TypedDict(
    "_ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef",
    {"Name": str, "CreationDateTime": datetime},
    total=False,
)


class ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef(
    _ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef
):
    """
    - *(dict) --*

      The creation date and time, and name, of a security configuration.
      - **Name** *(string) --*

        The name of the security configuration.
    """


_ClientListSecurityConfigurationsResponseTypeDef = TypedDict(
    "_ClientListSecurityConfigurationsResponseTypeDef",
    {
        "SecurityConfigurations": List[
            ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientListSecurityConfigurationsResponseTypeDef(
    _ClientListSecurityConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **SecurityConfigurations** *(list) --*

        The creation date and time, and name, of each security configuration.
        - *(dict) --*

          The creation date and time, and name, of a security configuration.
          - **Name** *(string) --*

            The name of the security configuration.
    """


_ClientListStepsResponseStepsConfigTypeDef = TypedDict(
    "_ClientListStepsResponseStepsConfigTypeDef",
    {"Jar": str, "Properties": Dict[str, str], "MainClass": str, "Args": List[str]},
    total=False,
)


class ClientListStepsResponseStepsConfigTypeDef(_ClientListStepsResponseStepsConfigTypeDef):
    pass


_ClientListStepsResponseStepsStatusFailureDetailsTypeDef = TypedDict(
    "_ClientListStepsResponseStepsStatusFailureDetailsTypeDef",
    {"Reason": str, "Message": str, "LogFile": str},
    total=False,
)


class ClientListStepsResponseStepsStatusFailureDetailsTypeDef(
    _ClientListStepsResponseStepsStatusFailureDetailsTypeDef
):
    pass


_ClientListStepsResponseStepsStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientListStepsResponseStepsStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientListStepsResponseStepsStatusStateChangeReasonTypeDef(
    _ClientListStepsResponseStepsStatusStateChangeReasonTypeDef
):
    pass


_ClientListStepsResponseStepsStatusTimelineTypeDef = TypedDict(
    "_ClientListStepsResponseStepsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "StartDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientListStepsResponseStepsStatusTimelineTypeDef(
    _ClientListStepsResponseStepsStatusTimelineTypeDef
):
    pass


_ClientListStepsResponseStepsStatusTypeDef = TypedDict(
    "_ClientListStepsResponseStepsStatusTypeDef",
    {
        "State": Literal[
            "PENDING",
            "CANCEL_PENDING",
            "RUNNING",
            "COMPLETED",
            "CANCELLED",
            "FAILED",
            "INTERRUPTED",
        ],
        "StateChangeReason": ClientListStepsResponseStepsStatusStateChangeReasonTypeDef,
        "FailureDetails": ClientListStepsResponseStepsStatusFailureDetailsTypeDef,
        "Timeline": ClientListStepsResponseStepsStatusTimelineTypeDef,
    },
    total=False,
)


class ClientListStepsResponseStepsStatusTypeDef(_ClientListStepsResponseStepsStatusTypeDef):
    pass


_ClientListStepsResponseStepsTypeDef = TypedDict(
    "_ClientListStepsResponseStepsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": ClientListStepsResponseStepsConfigTypeDef,
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "Status": ClientListStepsResponseStepsStatusTypeDef,
    },
    total=False,
)


class ClientListStepsResponseStepsTypeDef(_ClientListStepsResponseStepsTypeDef):
    """
    - *(dict) --*

      The summary of the cluster step.
      - **Id** *(string) --*

        The identifier of the cluster step.
    """


_ClientListStepsResponseTypeDef = TypedDict(
    "_ClientListStepsResponseTypeDef",
    {"Steps": List[ClientListStepsResponseStepsTypeDef], "Marker": str},
    total=False,
)


class ClientListStepsResponseTypeDef(_ClientListStepsResponseTypeDef):
    """
    - *(dict) --*

      This output contains the list of steps returned in reverse order. This means that the last
      step is the first element in the list.
      - **Steps** *(list) --*

        The filtered list of steps for the cluster.
        - *(dict) --*

          The summary of the cluster step.
          - **Id** *(string) --*

            The identifier of the cluster step.
    """


_ClientModifyClusterResponseTypeDef = TypedDict(
    "_ClientModifyClusterResponseTypeDef", {"StepConcurrencyLevel": int}, total=False
)


class ClientModifyClusterResponseTypeDef(_ClientModifyClusterResponseTypeDef):
    """
    - *(dict) --*

      - **StepConcurrencyLevel** *(integer) --*

        The number of steps that can be executed concurrently.
    """


_RequiredClientModifyInstanceFleetInstanceFleetTypeDef = TypedDict(
    "_RequiredClientModifyInstanceFleetInstanceFleetTypeDef", {"InstanceFleetId": str}
)
_OptionalClientModifyInstanceFleetInstanceFleetTypeDef = TypedDict(
    "_OptionalClientModifyInstanceFleetInstanceFleetTypeDef",
    {"TargetOnDemandCapacity": int, "TargetSpotCapacity": int},
    total=False,
)


class ClientModifyInstanceFleetInstanceFleetTypeDef(
    _RequiredClientModifyInstanceFleetInstanceFleetTypeDef,
    _OptionalClientModifyInstanceFleetInstanceFleetTypeDef,
):
    """
    The unique identifier of the instance fleet.
    - **InstanceFleetId** *(string) --***[REQUIRED]**

      A unique identifier for the instance fleet.
    """


_ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef = TypedDict(
    "_ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)


class ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef(
    _ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef
):
    pass


_ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef = TypedDict(
    "_ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    {
        "InstancesToTerminate": List[str],
        "InstancesToProtect": List[str],
        "InstanceTerminationTimeout": int,
    },
    total=False,
)


class ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef(
    _ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef
):
    pass


_ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef = TypedDict(
    "_ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef",
    {
        "DecommissionTimeout": int,
        "InstanceResizePolicy": ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef,
    },
    total=False,
)


class ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef(
    _ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef
):
    pass


_RequiredClientModifyInstanceGroupsInstanceGroupsTypeDef = TypedDict(
    "_RequiredClientModifyInstanceGroupsInstanceGroupsTypeDef", {"InstanceGroupId": str}
)
_OptionalClientModifyInstanceGroupsInstanceGroupsTypeDef = TypedDict(
    "_OptionalClientModifyInstanceGroupsInstanceGroupsTypeDef",
    {
        "InstanceCount": int,
        "EC2InstanceIdsToTerminate": List[str],
        "ShrinkPolicy": ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef,
        "Configurations": List[ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef],
    },
    total=False,
)


class ClientModifyInstanceGroupsInstanceGroupsTypeDef(
    _RequiredClientModifyInstanceGroupsInstanceGroupsTypeDef,
    _OptionalClientModifyInstanceGroupsInstanceGroupsTypeDef,
):
    """
    - *(dict) --*

      Modify the size or configurations of an instance group.
      - **InstanceGroupId** *(string) --***[REQUIRED]**

        Unique ID of the instance group to expand or shrink.
    """


_RequiredClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_RequiredClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef", {"MinCapacity": int}
)
_OptionalClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_OptionalClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef",
    {"MaxCapacity": int},
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef(
    _RequiredClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef,
    _OptionalClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef,
):
    """
    - **Constraints** *(dict) --***[REQUIRED]**

      The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling
      activity will not cause an instance group to grow above or below these limits.
      - **MinCapacity** *(integer) --***[REQUIRED]**

        The lower boundary of EC2 instances in an instance group below which scaling activities are
        not allowed to shrink. Scale-in activities will not terminate instances below this boundary.
    """


_ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal[
            "CHANGE_IN_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY", "EXACT_CAPACITY"
        ],
        "ScalingAdjustment": int,
        "CoolDown": int,
    },
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef(
    _ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef
):
    pass


_ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": Literal["ON_DEMAND", "SPOT"],
        "SimpleScalingPolicyConfiguration": ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef(
    _ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef
):
    pass


_ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef(
    _ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
):
    pass


_ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": Literal[
            "GREATER_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ],
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": Literal["SAMPLE_COUNT", "AVERAGE", "SUM", "MINIMUM", "MAXIMUM"],
        "Threshold": float,
        "Unit": Literal[
            "NONE",
            "SECONDS",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "BYTES",
            "KILO_BYTES",
            "MEGA_BYTES",
            "GIGA_BYTES",
            "TERA_BYTES",
            "BITS",
            "KILO_BITS",
            "MEGA_BITS",
            "GIGA_BITS",
            "TERA_BITS",
            "PERCENT",
            "COUNT",
            "BYTES_PER_SECOND",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BYTES_PER_SECOND",
            "GIGA_BYTES_PER_SECOND",
            "TERA_BYTES_PER_SECOND",
            "BITS_PER_SECOND",
            "KILO_BITS_PER_SECOND",
            "MEGA_BITS_PER_SECOND",
            "GIGA_BITS_PER_SECOND",
            "TERA_BITS_PER_SECOND",
            "COUNT_PER_SECOND",
        ],
        "Dimensions": List[
            ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef(
    _ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
):
    pass


_ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef(
    _ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef
):
    pass


_ClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef(
    _ClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef
):
    pass


_RequiredClientPutAutoScalingPolicyAutoScalingPolicyTypeDef = TypedDict(
    "_RequiredClientPutAutoScalingPolicyAutoScalingPolicyTypeDef",
    {"Constraints": ClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef},
)
_OptionalClientPutAutoScalingPolicyAutoScalingPolicyTypeDef = TypedDict(
    "_OptionalClientPutAutoScalingPolicyAutoScalingPolicyTypeDef",
    {"Rules": List[ClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef]},
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyTypeDef(
    _RequiredClientPutAutoScalingPolicyAutoScalingPolicyTypeDef,
    _OptionalClientPutAutoScalingPolicyAutoScalingPolicyTypeDef,
):
    """
    Specifies the definition of the automatic scaling policy.
    - **Constraints** *(dict) --***[REQUIRED]**

      The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling
      activity will not cause an instance group to grow above or below these limits.
      - **MinCapacity** *(integer) --***[REQUIRED]**

        The lower boundary of EC2 instances in an instance group below which scaling activities are
        not allowed to shrink. Scale-in activities will not terminate instances below this boundary.
    """


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef
):
    pass


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal[
            "CHANGE_IN_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY", "EXACT_CAPACITY"
        ],
        "ScalingAdjustment": int,
        "CoolDown": int,
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef
):
    pass


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": Literal["ON_DEMAND", "SPOT"],
        "SimpleScalingPolicyConfiguration": ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef
):
    pass


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
):
    pass


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": Literal[
            "GREATER_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ],
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": Literal["SAMPLE_COUNT", "AVERAGE", "SUM", "MINIMUM", "MAXIMUM"],
        "Threshold": float,
        "Unit": Literal[
            "NONE",
            "SECONDS",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "BYTES",
            "KILO_BYTES",
            "MEGA_BYTES",
            "GIGA_BYTES",
            "TERA_BYTES",
            "BITS",
            "KILO_BITS",
            "MEGA_BITS",
            "GIGA_BITS",
            "TERA_BITS",
            "PERCENT",
            "COUNT",
            "BYTES_PER_SECOND",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BYTES_PER_SECOND",
            "GIGA_BYTES_PER_SECOND",
            "TERA_BYTES_PER_SECOND",
            "BITS_PER_SECOND",
            "KILO_BITS_PER_SECOND",
            "MEGA_BITS_PER_SECOND",
            "GIGA_BITS_PER_SECOND",
            "TERA_BITS_PER_SECOND",
            "COUNT_PER_SECOND",
        ],
        "Dimensions": List[
            ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
):
    pass


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef
):
    pass


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef
):
    pass


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef",
    {"Code": Literal["USER_REQUEST", "PROVISION_FAILURE", "CLEANUP_FAILURE"], "Message": str},
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef
):
    pass


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef",
    {
        "State": Literal["PENDING", "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", "FAILED"],
        "StateChangeReason": ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef,
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef
):
    pass


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef",
    {
        "Status": ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef,
        "Constraints": ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef],
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef
):
    pass


_ClientPutAutoScalingPolicyResponseTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
        "AutoScalingPolicy": ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef,
        "ClusterArn": str,
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseTypeDef(_ClientPutAutoScalingPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **ClusterId** *(string) --*

        Specifies the ID of a cluster. The instance group to which the automatic scaling policy is
        applied is within this cluster.
    """


_ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef = TypedDict(
    "_ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef",
    {"MinRange": int, "MaxRange": int},
    total=False,
)


class ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef(
    _ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef
):
    pass


_RequiredClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_RequiredClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef",
    {"BlockPublicSecurityGroupRules": bool},
)
_OptionalClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_OptionalClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef",
    {
        "PermittedPublicSecurityGroupRuleRanges": List[
            ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef
        ]
    },
    total=False,
)


class ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef(
    _RequiredClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef,
    _OptionalClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef,
):
    """
    A configuration for Amazon EMR block public access. The configuration applies to all clusters
    created in your account for the current Region. The configuration specifies whether block public
    access is enabled. If block public access is enabled, security groups associated with the
    cluster cannot have rules that allow inbound traffic from 0.0.0.0/0 or ::/0 on a port, unless
    the port is specified as an exception using ``PermittedPublicSecurityGroupRuleRanges`` in the
    ``BlockPublicAccessConfiguration`` . By default, Port 22 (SSH) is an exception, and public
    access is allowed on this port. You can change this by updating
    ``BlockPublicSecurityGroupRules`` to remove the exception.
    - **BlockPublicSecurityGroupRules** *(boolean) --***[REQUIRED]**

      Indicates whether EMR block public access is enabled (``true`` ) or disabled (``false`` ). By
      default, the value is ``false`` for accounts that have created EMR clusters before July 2019.
      For accounts created after this, the default is ``true`` .
    """


_ClientRunJobFlowApplicationsTypeDef = TypedDict(
    "_ClientRunJobFlowApplicationsTypeDef",
    {"Name": str, "Version": str, "Args": List[str], "AdditionalInfo": Dict[str, str]},
    total=False,
)


class ClientRunJobFlowApplicationsTypeDef(_ClientRunJobFlowApplicationsTypeDef):
    """
    - *(dict) --*

      With Amazon EMR release version 4.0 and later, the only accepted parameter is the application
      name. To pass arguments to applications, you use configuration classifications specified using
      configuration JSON objects. For more information, see `Configuring Applications
      <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .
      With earlier Amazon EMR releases, the application is any Amazon or third-party software that
      you can add to the cluster. This structure contains a list of strings that indicates the
      software to use with the cluster and accepts a user argument list. Amazon EMR accepts and
      forwards the argument list to the corresponding installation script as bootstrap action
      argument.
      - **Name** *(string) --*

        The name of the application.
    """


_ClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef = TypedDict(
    "_ClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef",
    {"Path": str, "Args": List[str]},
    total=False,
)


class ClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef(
    _ClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef
):
    pass


_RequiredClientRunJobFlowBootstrapActionsTypeDef = TypedDict(
    "_RequiredClientRunJobFlowBootstrapActionsTypeDef", {"Name": str}
)
_OptionalClientRunJobFlowBootstrapActionsTypeDef = TypedDict(
    "_OptionalClientRunJobFlowBootstrapActionsTypeDef",
    {"ScriptBootstrapAction": ClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef},
    total=False,
)


class ClientRunJobFlowBootstrapActionsTypeDef(
    _RequiredClientRunJobFlowBootstrapActionsTypeDef,
    _OptionalClientRunJobFlowBootstrapActionsTypeDef,
):
    """
    - *(dict) --*

      Configuration of a bootstrap action.
      - **Name** *(string) --***[REQUIRED]**

        The name of the bootstrap action.
    """


_ClientRunJobFlowConfigurationsTypeDef = TypedDict(
    "_ClientRunJobFlowConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)


class ClientRunJobFlowConfigurationsTypeDef(_ClientRunJobFlowConfigurationsTypeDef):
    """
    - *(dict) --*

      .. note::

        Amazon EMR releases 4.x or later.
    """


_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef(
    _ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef(
    _ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {
        "VolumeSpecification": ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
        "VolumesPerInstance": int,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef(
    _ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List[
            ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef(
    _ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "EbsConfiguration": ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef,
        "Configurations": List[
            ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef(
    _ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": int,
        "TimeoutAction": Literal["SWITCH_TO_ON_DEMAND", "TERMINATE_CLUSTER"],
        "BlockDurationMinutes": int,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef(
    _ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef",
    {
        "SpotSpecification": ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef(
    _ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceFleetsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceFleetsTypeDef",
    {
        "Name": str,
        "InstanceFleetType": Literal["MASTER", "CORE", "TASK"],
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "InstanceTypeConfigs": List[
            ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef
        ],
        "LaunchSpecifications": ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsTypeDef(
    _ClientRunJobFlowInstancesInstanceFleetsTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal[
            "CHANGE_IN_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY", "EXACT_CAPACITY"
        ],
        "ScalingAdjustment": int,
        "CoolDown": int,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": Literal["ON_DEMAND", "SPOT"],
        "SimpleScalingPolicyConfiguration": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": Literal[
            "GREATER_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ],
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": Literal["SAMPLE_COUNT", "AVERAGE", "SUM", "MINIMUM", "MAXIMUM"],
        "Threshold": float,
        "Unit": Literal[
            "NONE",
            "SECONDS",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "BYTES",
            "KILO_BYTES",
            "MEGA_BYTES",
            "GIGA_BYTES",
            "TERA_BYTES",
            "BITS",
            "KILO_BITS",
            "MEGA_BITS",
            "GIGA_BITS",
            "TERA_BITS",
            "PERCENT",
            "COUNT",
            "BYTES_PER_SECOND",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BYTES_PER_SECOND",
            "GIGA_BYTES_PER_SECOND",
            "TERA_BYTES_PER_SECOND",
            "BITS_PER_SECOND",
            "KILO_BITS_PER_SECOND",
            "MEGA_BITS_PER_SECOND",
            "GIGA_BITS_PER_SECOND",
            "TERA_BITS_PER_SECOND",
            "COUNT_PER_SECOND",
        ],
        "Dimensions": List[
            ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef",
    {
        "Constraints": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef],
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {
        "VolumeSpecification": ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
        "VolumesPerInstance": int,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List[
            ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef
):
    pass


_ClientRunJobFlowInstancesInstanceGroupsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsTypeDef",
    {
        "Name": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceRole": Literal["MASTER", "CORE", "TASK"],
        "BidPrice": str,
        "InstanceType": str,
        "InstanceCount": int,
        "Configurations": List[ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef],
        "EbsConfiguration": ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef,
        "AutoScalingPolicy": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsTypeDef
):
    pass


_ClientRunJobFlowInstancesPlacementTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesPlacementTypeDef",
    {"AvailabilityZone": str, "AvailabilityZones": List[str]},
    total=False,
)


class ClientRunJobFlowInstancesPlacementTypeDef(_ClientRunJobFlowInstancesPlacementTypeDef):
    pass


_ClientRunJobFlowInstancesTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesTypeDef",
    {
        "MasterInstanceType": str,
        "SlaveInstanceType": str,
        "InstanceCount": int,
        "InstanceGroups": List[ClientRunJobFlowInstancesInstanceGroupsTypeDef],
        "InstanceFleets": List[ClientRunJobFlowInstancesInstanceFleetsTypeDef],
        "Ec2KeyName": str,
        "Placement": ClientRunJobFlowInstancesPlacementTypeDef,
        "KeepJobFlowAliveWhenNoSteps": bool,
        "TerminationProtected": bool,
        "HadoopVersion": str,
        "Ec2SubnetId": str,
        "Ec2SubnetIds": List[str],
        "EmrManagedMasterSecurityGroup": str,
        "EmrManagedSlaveSecurityGroup": str,
        "ServiceAccessSecurityGroup": str,
        "AdditionalMasterSecurityGroups": List[str],
        "AdditionalSlaveSecurityGroups": List[str],
    },
    total=False,
)


class ClientRunJobFlowInstancesTypeDef(_ClientRunJobFlowInstancesTypeDef):
    """
    A specification of the number and type of Amazon EC2 instances.
    - **MasterInstanceType** *(string) --*

      The EC2 instance type of the master node.
    """


_RequiredClientRunJobFlowKerberosAttributesTypeDef = TypedDict(
    "_RequiredClientRunJobFlowKerberosAttributesTypeDef", {"Realm": str}
)
_OptionalClientRunJobFlowKerberosAttributesTypeDef = TypedDict(
    "_OptionalClientRunJobFlowKerberosAttributesTypeDef",
    {
        "KdcAdminPassword": str,
        "CrossRealmTrustPrincipalPassword": str,
        "ADDomainJoinUser": str,
        "ADDomainJoinPassword": str,
    },
    total=False,
)


class ClientRunJobFlowKerberosAttributesTypeDef(
    _RequiredClientRunJobFlowKerberosAttributesTypeDef,
    _OptionalClientRunJobFlowKerberosAttributesTypeDef,
):
    """
    Attributes for Kerberos configuration when Kerberos authentication is enabled using a security
    configuration. For more information see `Use Kerberos Authentication
    <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html>`__ in the *EMR
    Management Guide* .
    - **Realm** *(string) --***[REQUIRED]**

      The name of the Kerberos realm to which all nodes in a cluster belong. For example,
      ``EC2.INTERNAL`` .
    """


_ClientRunJobFlowNewSupportedProductsTypeDef = TypedDict(
    "_ClientRunJobFlowNewSupportedProductsTypeDef", {"Name": str, "Args": List[str]}, total=False
)


class ClientRunJobFlowNewSupportedProductsTypeDef(_ClientRunJobFlowNewSupportedProductsTypeDef):
    pass


_ClientRunJobFlowResponseTypeDef = TypedDict(
    "_ClientRunJobFlowResponseTypeDef", {"JobFlowId": str, "ClusterArn": str}, total=False
)


class ClientRunJobFlowResponseTypeDef(_ClientRunJobFlowResponseTypeDef):
    """
    - *(dict) --*

      The result of the  RunJobFlow operation.
      - **JobFlowId** *(string) --*

        An unique identifier for the job flow.
    """


_ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef = TypedDict(
    "_ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef(
    _ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef
):
    pass


_ClientRunJobFlowStepsHadoopJarStepTypeDef = TypedDict(
    "_ClientRunJobFlowStepsHadoopJarStepTypeDef",
    {
        "Properties": List[ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef],
        "Jar": str,
        "MainClass": str,
        "Args": List[str],
    },
    total=False,
)


class ClientRunJobFlowStepsHadoopJarStepTypeDef(_ClientRunJobFlowStepsHadoopJarStepTypeDef):
    pass


_RequiredClientRunJobFlowStepsTypeDef = TypedDict(
    "_RequiredClientRunJobFlowStepsTypeDef", {"Name": str}
)
_OptionalClientRunJobFlowStepsTypeDef = TypedDict(
    "_OptionalClientRunJobFlowStepsTypeDef",
    {
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "HadoopJarStep": ClientRunJobFlowStepsHadoopJarStepTypeDef,
    },
    total=False,
)


class ClientRunJobFlowStepsTypeDef(
    _RequiredClientRunJobFlowStepsTypeDef, _OptionalClientRunJobFlowStepsTypeDef
):
    """
    - *(dict) --*

      Specification of a cluster (job flow) step.
      - **Name** *(string) --***[REQUIRED]**

        The name of the step.
    """


_ClientRunJobFlowTagsTypeDef = TypedDict(
    "_ClientRunJobFlowTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRunJobFlowTagsTypeDef(_ClientRunJobFlowTagsTypeDef):
    """
    - *(dict) --*

      A key/value pair containing user-defined metadata that you can associate with an Amazon EMR
      resource. Tags make it easier to associate clusters in various ways, such as grouping clusters
      to track your Amazon EMR resource allocation costs. For more information, see `Tag Clusters
      <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .
      - **Key** *(string) --*

        A user-defined key, which is the minimum required information for a valid tag. For more
        information, see `Tag
        <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .
    """


_ClusterRunningWaitWaiterConfigTypeDef = TypedDict(
    "_ClusterRunningWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class ClusterRunningWaitWaiterConfigTypeDef(_ClusterRunningWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_ClusterTerminatedWaitWaiterConfigTypeDef = TypedDict(
    "_ClusterTerminatedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class ClusterTerminatedWaitWaiterConfigTypeDef(_ClusterTerminatedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_ListBootstrapActionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBootstrapActionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListBootstrapActionsPaginatePaginationConfigTypeDef(
    _ListBootstrapActionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBootstrapActionsPaginateResponseBootstrapActionsTypeDef = TypedDict(
    "_ListBootstrapActionsPaginateResponseBootstrapActionsTypeDef",
    {"Name": str, "ScriptPath": str, "Args": List[str]},
    total=False,
)


class ListBootstrapActionsPaginateResponseBootstrapActionsTypeDef(
    _ListBootstrapActionsPaginateResponseBootstrapActionsTypeDef
):
    """
    - *(dict) --*

      An entity describing an executable that runs on a cluster.
      - **Name** *(string) --*

        The name of the command.
    """


_ListBootstrapActionsPaginateResponseTypeDef = TypedDict(
    "_ListBootstrapActionsPaginateResponseTypeDef",
    {
        "BootstrapActions": List[ListBootstrapActionsPaginateResponseBootstrapActionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListBootstrapActionsPaginateResponseTypeDef(_ListBootstrapActionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      This output contains the bootstrap actions detail.
      - **BootstrapActions** *(list) --*

        The bootstrap actions associated with the cluster.
        - *(dict) --*

          An entity describing an executable that runs on a cluster.
          - **Name** *(string) --*

            The name of the command.
    """


_ListClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListClustersPaginatePaginationConfigTypeDef(_ListClustersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListClustersPaginateResponseClustersStatusStateChangeReasonTypeDef = TypedDict(
    "_ListClustersPaginateResponseClustersStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
            "INSTANCE_FAILURE",
            "INSTANCE_FLEET_TIMEOUT",
            "BOOTSTRAP_FAILURE",
            "USER_REQUEST",
            "STEP_FAILURE",
            "ALL_STEPS_COMPLETED",
        ],
        "Message": str,
    },
    total=False,
)


class ListClustersPaginateResponseClustersStatusStateChangeReasonTypeDef(
    _ListClustersPaginateResponseClustersStatusStateChangeReasonTypeDef
):
    pass


_ListClustersPaginateResponseClustersStatusTimelineTypeDef = TypedDict(
    "_ListClustersPaginateResponseClustersStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ListClustersPaginateResponseClustersStatusTimelineTypeDef(
    _ListClustersPaginateResponseClustersStatusTimelineTypeDef
):
    pass


_ListClustersPaginateResponseClustersStatusTypeDef = TypedDict(
    "_ListClustersPaginateResponseClustersStatusTypeDef",
    {
        "State": Literal[
            "STARTING",
            "BOOTSTRAPPING",
            "RUNNING",
            "WAITING",
            "TERMINATING",
            "TERMINATED",
            "TERMINATED_WITH_ERRORS",
        ],
        "StateChangeReason": ListClustersPaginateResponseClustersStatusStateChangeReasonTypeDef,
        "Timeline": ListClustersPaginateResponseClustersStatusTimelineTypeDef,
    },
    total=False,
)


class ListClustersPaginateResponseClustersStatusTypeDef(
    _ListClustersPaginateResponseClustersStatusTypeDef
):
    pass


_ListClustersPaginateResponseClustersTypeDef = TypedDict(
    "_ListClustersPaginateResponseClustersTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ListClustersPaginateResponseClustersStatusTypeDef,
        "NormalizedInstanceHours": int,
        "ClusterArn": str,
        "OutpostArn": str,
    },
    total=False,
)


class ListClustersPaginateResponseClustersTypeDef(_ListClustersPaginateResponseClustersTypeDef):
    """
    - *(dict) --*

      The summary description of the cluster.
      - **Id** *(string) --*

        The unique identifier for the cluster.
    """


_ListClustersPaginateResponseTypeDef = TypedDict(
    "_ListClustersPaginateResponseTypeDef",
    {"Clusters": List[ListClustersPaginateResponseClustersTypeDef], "NextToken": str},
    total=False,
)


class ListClustersPaginateResponseTypeDef(_ListClustersPaginateResponseTypeDef):
    """
    - *(dict) --*

      This contains a ClusterSummaryList with the cluster details; for example, the cluster IDs,
      names, and status.
      - **Clusters** *(list) --*

        The list of clusters for the account based on the given filters.
        - *(dict) --*

          The summary description of the cluster.
          - **Id** *(string) --*

            The unique identifier for the cluster.
    """


_ListInstanceFleetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInstanceFleetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListInstanceFleetsPaginatePaginationConfigTypeDef(
    _ListInstanceFleetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef
):
    pass


_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef
):
    pass


_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef",
    {
        "VolumeSpecification": ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef,
        "Device": str,
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef
):
    pass


_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "Configurations": List[
            ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef
        ],
        "EbsBlockDevices": List[
            ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsTypeDef
):
    pass


_ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": int,
        "TimeoutAction": Literal["SWITCH_TO_ON_DEMAND", "TERMINATE_CLUSTER"],
        "BlockDurationMinutes": int,
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef
):
    pass


_ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsTypeDef",
    {
        "SpotSpecification": ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsTypeDef
):
    pass


_ListInstanceFleetsPaginateResponseInstanceFleetsStatusStateChangeReasonTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR", "VALIDATION_ERROR", "INSTANCE_FAILURE", "CLUSTER_TERMINATED"
        ],
        "Message": str,
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsStatusStateChangeReasonTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsStatusStateChangeReasonTypeDef
):
    pass


_ListInstanceFleetsPaginateResponseInstanceFleetsStatusTimelineTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsStatusTimelineTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsStatusTimelineTypeDef
):
    pass


_ListInstanceFleetsPaginateResponseInstanceFleetsStatusTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsStatusTypeDef",
    {
        "State": Literal[
            "PROVISIONING",
            "BOOTSTRAPPING",
            "RUNNING",
            "RESIZING",
            "SUSPENDED",
            "TERMINATING",
            "TERMINATED",
        ],
        "StateChangeReason": ListInstanceFleetsPaginateResponseInstanceFleetsStatusStateChangeReasonTypeDef,
        "Timeline": ListInstanceFleetsPaginateResponseInstanceFleetsStatusTimelineTypeDef,
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsStatusTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsStatusTypeDef
):
    pass


_ListInstanceFleetsPaginateResponseInstanceFleetsTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ListInstanceFleetsPaginateResponseInstanceFleetsStatusTypeDef,
        "InstanceFleetType": Literal["MASTER", "CORE", "TASK"],
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "ProvisionedOnDemandCapacity": int,
        "ProvisionedSpotCapacity": int,
        "InstanceTypeSpecifications": List[
            ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsTypeDef
        ],
        "LaunchSpecifications": ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsTypeDef,
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsTypeDef
):
    """
    - *(dict) --*

      Describes an instance fleet, which is a group of EC2 instances that host a particular node
      type (master, core, or task) in an Amazon EMR cluster. Instance fleets can consist of a mix of
      instance types and On-Demand and Spot instances, which are provisioned to meet a defined
      target capacity.
      .. note::

        The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later,
        excluding 5.0.x versions.
    """


_ListInstanceFleetsPaginateResponseTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseTypeDef",
    {
        "InstanceFleets": List[ListInstanceFleetsPaginateResponseInstanceFleetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseTypeDef(_ListInstanceFleetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **InstanceFleets** *(list) --*

        The list of instance fleets for the cluster and given filters.
        - *(dict) --*

          Describes an instance fleet, which is a group of EC2 instances that host a particular node
          type (master, core, or task) in an Amazon EMR cluster. Instance fleets can consist of a
          mix of instance types and On-Demand and Spot instances, which are provisioned to meet a
          defined target capacity.
          .. note::

            The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
            later, excluding 5.0.x versions.
    """


_ListInstanceGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInstanceGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListInstanceGroupsPaginatePaginationConfigTypeDef(
    _ListInstanceGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal[
            "CHANGE_IN_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY", "EXACT_CAPACITY"
        ],
        "ScalingAdjustment": int,
        "CoolDown": int,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": Literal["ON_DEMAND", "SPOT"],
        "SimpleScalingPolicyConfiguration": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": Literal[
            "GREATER_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ],
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": Literal["SAMPLE_COUNT", "AVERAGE", "SUM", "MINIMUM", "MAXIMUM"],
        "Threshold": float,
        "Unit": Literal[
            "NONE",
            "SECONDS",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "BYTES",
            "KILO_BYTES",
            "MEGA_BYTES",
            "GIGA_BYTES",
            "TERA_BYTES",
            "BITS",
            "KILO_BITS",
            "MEGA_BITS",
            "GIGA_BITS",
            "TERA_BITS",
            "PERCENT",
            "COUNT",
            "BYTES_PER_SECOND",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BYTES_PER_SECOND",
            "GIGA_BYTES_PER_SECOND",
            "TERA_BYTES_PER_SECOND",
            "BITS_PER_SECOND",
            "KILO_BITS_PER_SECOND",
            "MEGA_BITS_PER_SECOND",
            "GIGA_BITS_PER_SECOND",
            "TERA_BITS_PER_SECOND",
            "COUNT_PER_SECOND",
        ],
        "Dimensions": List[
            ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef",
    {"Code": Literal["USER_REQUEST", "PROVISION_FAILURE", "CLEANUP_FAILURE"], "Message": str},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusTypeDef",
    {
        "State": Literal["PENDING", "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", "FAILED"],
        "StateChangeReason": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyTypeDef",
    {
        "Status": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusTypeDef,
        "Constraints": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[
            ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTypeDef
        ],
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsConfigurationsTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsConfigurationsTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsConfigurationsTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesTypeDef",
    {
        "VolumeSpecification": ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef,
        "Device": str,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    {
        "InstancesToTerminate": List[str],
        "InstancesToProtect": List[str],
        "InstanceTerminationTimeout": int,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyTypeDef",
    {
        "DecommissionTimeout": int,
        "InstanceResizePolicy": ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsStatusStateChangeReasonTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR", "VALIDATION_ERROR", "INSTANCE_FAILURE", "CLUSTER_TERMINATED"
        ],
        "Message": str,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsStatusStateChangeReasonTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsStatusStateChangeReasonTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsStatusTimelineTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsStatusTimelineTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsStatusTimelineTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsStatusTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsStatusTypeDef",
    {
        "State": Literal[
            "PROVISIONING",
            "BOOTSTRAPPING",
            "RUNNING",
            "RECONFIGURING",
            "RESIZING",
            "SUSPENDED",
            "TERMINATING",
            "TERMINATED",
            "ARRESTED",
            "SHUTTING_DOWN",
            "ENDED",
        ],
        "StateChangeReason": ListInstanceGroupsPaginateResponseInstanceGroupsStatusStateChangeReasonTypeDef,
        "Timeline": ListInstanceGroupsPaginateResponseInstanceGroupsStatusTimelineTypeDef,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsStatusTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsStatusTypeDef
):
    pass


_ListInstanceGroupsPaginateResponseInstanceGroupsTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceGroupType": Literal["MASTER", "CORE", "TASK"],
        "BidPrice": str,
        "InstanceType": str,
        "RequestedInstanceCount": int,
        "RunningInstanceCount": int,
        "Status": ListInstanceGroupsPaginateResponseInstanceGroupsStatusTypeDef,
        "Configurations": List[
            ListInstanceGroupsPaginateResponseInstanceGroupsConfigurationsTypeDef
        ],
        "ConfigurationsVersion": int,
        "LastSuccessfullyAppliedConfigurations": List[
            ListInstanceGroupsPaginateResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef
        ],
        "LastSuccessfullyAppliedConfigurationsVersion": int,
        "EbsBlockDevices": List[
            ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesTypeDef
        ],
        "EbsOptimized": bool,
        "ShrinkPolicy": ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyTypeDef,
        "AutoScalingPolicy": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyTypeDef,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsTypeDef
):
    """
    - *(dict) --*

      This entity represents an instance group, which is a group of instances that have common
      purpose. For example, CORE instance group is used for HDFS.
      - **Id** *(string) --*

        The identifier of the instance group.
    """


_ListInstanceGroupsPaginateResponseTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseTypeDef",
    {
        "InstanceGroups": List[ListInstanceGroupsPaginateResponseInstanceGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseTypeDef(_ListInstanceGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      This input determines which instance groups to retrieve.
      - **InstanceGroups** *(list) --*

        The list of instance groups for the cluster and given filters.
        - *(dict) --*

          This entity represents an instance group, which is a group of instances that have common
          purpose. For example, CORE instance group is used for HDFS.
          - **Id** *(string) --*

            The identifier of the instance group.
    """


_ListInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListInstancesPaginatePaginationConfigTypeDef(_ListInstancesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListInstancesPaginateResponseInstancesEbsVolumesTypeDef = TypedDict(
    "_ListInstancesPaginateResponseInstancesEbsVolumesTypeDef",
    {"Device": str, "VolumeId": str},
    total=False,
)


class ListInstancesPaginateResponseInstancesEbsVolumesTypeDef(
    _ListInstancesPaginateResponseInstancesEbsVolumesTypeDef
):
    pass


_ListInstancesPaginateResponseInstancesStatusStateChangeReasonTypeDef = TypedDict(
    "_ListInstancesPaginateResponseInstancesStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
            "INSTANCE_FAILURE",
            "BOOTSTRAP_FAILURE",
            "CLUSTER_TERMINATED",
        ],
        "Message": str,
    },
    total=False,
)


class ListInstancesPaginateResponseInstancesStatusStateChangeReasonTypeDef(
    _ListInstancesPaginateResponseInstancesStatusStateChangeReasonTypeDef
):
    pass


_ListInstancesPaginateResponseInstancesStatusTimelineTypeDef = TypedDict(
    "_ListInstancesPaginateResponseInstancesStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ListInstancesPaginateResponseInstancesStatusTimelineTypeDef(
    _ListInstancesPaginateResponseInstancesStatusTimelineTypeDef
):
    pass


_ListInstancesPaginateResponseInstancesStatusTypeDef = TypedDict(
    "_ListInstancesPaginateResponseInstancesStatusTypeDef",
    {
        "State": Literal[
            "AWAITING_FULFILLMENT", "PROVISIONING", "BOOTSTRAPPING", "RUNNING", "TERMINATED"
        ],
        "StateChangeReason": ListInstancesPaginateResponseInstancesStatusStateChangeReasonTypeDef,
        "Timeline": ListInstancesPaginateResponseInstancesStatusTimelineTypeDef,
    },
    total=False,
)


class ListInstancesPaginateResponseInstancesStatusTypeDef(
    _ListInstancesPaginateResponseInstancesStatusTypeDef
):
    pass


_ListInstancesPaginateResponseInstancesTypeDef = TypedDict(
    "_ListInstancesPaginateResponseInstancesTypeDef",
    {
        "Id": str,
        "Ec2InstanceId": str,
        "PublicDnsName": str,
        "PublicIpAddress": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "Status": ListInstancesPaginateResponseInstancesStatusTypeDef,
        "InstanceGroupId": str,
        "InstanceFleetId": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceType": str,
        "EbsVolumes": List[ListInstancesPaginateResponseInstancesEbsVolumesTypeDef],
    },
    total=False,
)


class ListInstancesPaginateResponseInstancesTypeDef(_ListInstancesPaginateResponseInstancesTypeDef):
    """
    - *(dict) --*

      Represents an EC2 instance provisioned as part of cluster.
      - **Id** *(string) --*

        The unique identifier for the instance in Amazon EMR.
    """


_ListInstancesPaginateResponseTypeDef = TypedDict(
    "_ListInstancesPaginateResponseTypeDef",
    {"Instances": List[ListInstancesPaginateResponseInstancesTypeDef], "NextToken": str},
    total=False,
)


class ListInstancesPaginateResponseTypeDef(_ListInstancesPaginateResponseTypeDef):
    """
    - *(dict) --*

      This output contains the list of instances.
      - **Instances** *(list) --*

        The list of instances for the cluster and given filters.
        - *(dict) --*

          Represents an EC2 instance provisioned as part of cluster.
          - **Id** *(string) --*

            The unique identifier for the instance in Amazon EMR.
    """


_ListSecurityConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSecurityConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListSecurityConfigurationsPaginatePaginationConfigTypeDef(
    _ListSecurityConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef = TypedDict(
    "_ListSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef",
    {"Name": str, "CreationDateTime": datetime},
    total=False,
)


class ListSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef(
    _ListSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef
):
    """
    - *(dict) --*

      The creation date and time, and name, of a security configuration.
      - **Name** *(string) --*

        The name of the security configuration.
    """


_ListSecurityConfigurationsPaginateResponseTypeDef = TypedDict(
    "_ListSecurityConfigurationsPaginateResponseTypeDef",
    {
        "SecurityConfigurations": List[
            ListSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListSecurityConfigurationsPaginateResponseTypeDef(
    _ListSecurityConfigurationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **SecurityConfigurations** *(list) --*

        The creation date and time, and name, of each security configuration.
        - *(dict) --*

          The creation date and time, and name, of a security configuration.
          - **Name** *(string) --*

            The name of the security configuration.
    """


_ListStepsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStepsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListStepsPaginatePaginationConfigTypeDef(_ListStepsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListStepsPaginateResponseStepsConfigTypeDef = TypedDict(
    "_ListStepsPaginateResponseStepsConfigTypeDef",
    {"Jar": str, "Properties": Dict[str, str], "MainClass": str, "Args": List[str]},
    total=False,
)


class ListStepsPaginateResponseStepsConfigTypeDef(_ListStepsPaginateResponseStepsConfigTypeDef):
    pass


_ListStepsPaginateResponseStepsStatusFailureDetailsTypeDef = TypedDict(
    "_ListStepsPaginateResponseStepsStatusFailureDetailsTypeDef",
    {"Reason": str, "Message": str, "LogFile": str},
    total=False,
)


class ListStepsPaginateResponseStepsStatusFailureDetailsTypeDef(
    _ListStepsPaginateResponseStepsStatusFailureDetailsTypeDef
):
    pass


_ListStepsPaginateResponseStepsStatusStateChangeReasonTypeDef = TypedDict(
    "_ListStepsPaginateResponseStepsStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ListStepsPaginateResponseStepsStatusStateChangeReasonTypeDef(
    _ListStepsPaginateResponseStepsStatusStateChangeReasonTypeDef
):
    pass


_ListStepsPaginateResponseStepsStatusTimelineTypeDef = TypedDict(
    "_ListStepsPaginateResponseStepsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "StartDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ListStepsPaginateResponseStepsStatusTimelineTypeDef(
    _ListStepsPaginateResponseStepsStatusTimelineTypeDef
):
    pass


_ListStepsPaginateResponseStepsStatusTypeDef = TypedDict(
    "_ListStepsPaginateResponseStepsStatusTypeDef",
    {
        "State": Literal[
            "PENDING",
            "CANCEL_PENDING",
            "RUNNING",
            "COMPLETED",
            "CANCELLED",
            "FAILED",
            "INTERRUPTED",
        ],
        "StateChangeReason": ListStepsPaginateResponseStepsStatusStateChangeReasonTypeDef,
        "FailureDetails": ListStepsPaginateResponseStepsStatusFailureDetailsTypeDef,
        "Timeline": ListStepsPaginateResponseStepsStatusTimelineTypeDef,
    },
    total=False,
)


class ListStepsPaginateResponseStepsStatusTypeDef(_ListStepsPaginateResponseStepsStatusTypeDef):
    pass


_ListStepsPaginateResponseStepsTypeDef = TypedDict(
    "_ListStepsPaginateResponseStepsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": ListStepsPaginateResponseStepsConfigTypeDef,
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "Status": ListStepsPaginateResponseStepsStatusTypeDef,
    },
    total=False,
)


class ListStepsPaginateResponseStepsTypeDef(_ListStepsPaginateResponseStepsTypeDef):
    """
    - *(dict) --*

      The summary of the cluster step.
      - **Id** *(string) --*

        The identifier of the cluster step.
    """


_ListStepsPaginateResponseTypeDef = TypedDict(
    "_ListStepsPaginateResponseTypeDef",
    {"Steps": List[ListStepsPaginateResponseStepsTypeDef], "NextToken": str},
    total=False,
)


class ListStepsPaginateResponseTypeDef(_ListStepsPaginateResponseTypeDef):
    """
    - *(dict) --*

      This output contains the list of steps returned in reverse order. This means that the last
      step is the first element in the list.
      - **Steps** *(list) --*

        The filtered list of steps for the cluster.
        - *(dict) --*

          The summary of the cluster step.
          - **Id** *(string) --*

            The identifier of the cluster step.
    """


_StepCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_StepCompleteWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class StepCompleteWaitWaiterConfigTypeDef(_StepCompleteWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """
