"Main interface for application-autoscaling service type defs"
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


ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef = TypedDict(
    "ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)

ClientDescribeScalableTargetsResponseScalableTargetsTypeDef = TypedDict(
    "ClientDescribeScalableTargetsResponseScalableTargetsTypeDef",
    {
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "CreationTime": datetime,
        "SuspendedState": ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef,
    },
    total=False,
)

ClientDescribeScalableTargetsResponseTypeDef = TypedDict(
    "ClientDescribeScalableTargetsResponseTypeDef",
    {
        "ScalableTargets": List[ClientDescribeScalableTargetsResponseScalableTargetsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef = TypedDict(
    "ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef",
    {
        "ActivityId": str,
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "Pending", "InProgress", "Successful", "Overridden", "Unfulfilled", "Failed"
        ],
        "StatusMessage": str,
        "Details": str,
    },
    total=False,
)

ClientDescribeScalingActivitiesResponseTypeDef = TypedDict(
    "ClientDescribeScalingActivitiesResponseTypeDef",
    {
        "ScalingActivities": List[ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal["ChangeInCapacity", "PercentChangeInCapacity", "ExactCapacity"],
        "StepAdjustments": List[
            ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef
        ],
        "MinAdjustmentMagnitude": int,
        "Cooldown": int,
        "MetricAggregationType": Literal["Average", "Minimum", "Maximum"],
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": Literal[
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
            "SageMakerVariantInvocationsPerInstance",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "AppStreamAverageCapacityUtilization",
            "ComprehendInferenceUtilization",
            "LambdaProvisionedConcurrencyUtilization",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricSpecification": ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "DisableScaleIn": bool,
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef",
    {
        "PolicyARN": str,
        "PolicyName": str,
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "PolicyType": Literal["StepScaling", "TargetTrackingScaling"],
        "StepScalingPolicyConfiguration": ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef,
        "TargetTrackingScalingPolicyConfiguration": ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
        "Alarms": List[ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef],
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseTypeDef",
    {
        "ScalingPolicies": List[ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)

ClientDescribeScheduledActionsResponseScheduledActionsTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseScheduledActionsTypeDef",
    {
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "Schedule": str,
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "ScalableTargetAction": ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeScheduledActionsResponseTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseTypeDef",
    {
        "ScheduledActions": List[ClientDescribeScheduledActionsResponseScheduledActionsTypeDef],
        "NextToken": str,
    },
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

ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef = TypedDict(
    "ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)

ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal["ChangeInCapacity", "PercentChangeInCapacity", "ExactCapacity"],
        "StepAdjustments": List[
            ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef
        ],
        "MinAdjustmentMagnitude": int,
        "Cooldown": int,
        "MetricAggregationType": Literal["Average", "Minimum", "Maximum"],
    },
    total=False,
)

ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": Literal[
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
            "SageMakerVariantInvocationsPerInstance",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "AppStreamAverageCapacityUtilization",
            "ComprehendInferenceUtilization",
            "LambdaProvisionedConcurrencyUtilization",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

_RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef",
    {"TargetValue": float},
)
_OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "DisableScaleIn": bool,
    },
    total=False,
)


class ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef(
    _RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef,
    _OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef,
):
    pass


ClientPutScheduledActionScalableTargetActionTypeDef = TypedDict(
    "ClientPutScheduledActionScalableTargetActionTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)

ClientRegisterScalableTargetSuspendedStateTypeDef = TypedDict(
    "ClientRegisterScalableTargetSuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)

DescribeScalableTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeScalableTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef = TypedDict(
    "DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)

DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef = TypedDict(
    "DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef",
    {
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "CreationTime": datetime,
        "SuspendedState": DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef,
    },
    total=False,
)

DescribeScalableTargetsPaginateResponseTypeDef = TypedDict(
    "DescribeScalableTargetsPaginateResponseTypeDef",
    {"ScalableTargets": List[DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef]},
    total=False,
)

DescribeScalingActivitiesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeScalingActivitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef = TypedDict(
    "DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef",
    {
        "ActivityId": str,
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "Pending", "InProgress", "Successful", "Overridden", "Unfulfilled", "Failed"
        ],
        "StatusMessage": str,
        "Details": str,
    },
    total=False,
)

DescribeScalingActivitiesPaginateResponseTypeDef = TypedDict(
    "DescribeScalingActivitiesPaginateResponseTypeDef",
    {"ScalingActivities": List[DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef]},
    total=False,
)

DescribeScalingPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)

DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)

DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal["ChangeInCapacity", "PercentChangeInCapacity", "ExactCapacity"],
        "StepAdjustments": List[
            DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef
        ],
        "MinAdjustmentMagnitude": int,
        "Cooldown": int,
        "MetricAggregationType": Literal["Average", "Minimum", "Maximum"],
    },
    total=False,
)

DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": Literal[
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
            "SageMakerVariantInvocationsPerInstance",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "AppStreamAverageCapacityUtilization",
            "ComprehendInferenceUtilization",
            "LambdaProvisionedConcurrencyUtilization",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricSpecification": DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "DisableScaleIn": bool,
    },
    total=False,
)

DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef",
    {
        "PolicyARN": str,
        "PolicyName": str,
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "PolicyType": Literal["StepScaling", "TargetTrackingScaling"],
        "StepScalingPolicyConfiguration": DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef,
        "TargetTrackingScalingPolicyConfiguration": DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
        "Alarms": List[DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef],
        "CreationTime": datetime,
    },
    total=False,
)

DescribeScalingPoliciesPaginateResponseTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginateResponseTypeDef",
    {"ScalingPolicies": List[DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef]},
    total=False,
)

DescribeScheduledActionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeScheduledActionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef = TypedDict(
    "DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)

DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef = TypedDict(
    "DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef",
    {
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "Schedule": str,
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "ScalableTargetAction": DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)

DescribeScheduledActionsPaginateResponseTypeDef = TypedDict(
    "DescribeScheduledActionsPaginateResponseTypeDef",
    {"ScheduledActions": List[DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef]},
    total=False,
)
