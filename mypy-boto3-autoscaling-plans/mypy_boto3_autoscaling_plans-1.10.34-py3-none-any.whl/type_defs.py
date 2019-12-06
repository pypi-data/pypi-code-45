"Main interface for autoscaling-plans service type defs"
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


ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef = TypedDict(
    "ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateScalingPlanApplicationSourceTypeDef = TypedDict(
    "ClientCreateScalingPlanApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef],
    },
    total=False,
)

ClientCreateScalingPlanResponseTypeDef = TypedDict(
    "ClientCreateScalingPlanResponseTypeDef", {"ScalingPlanVersion": int}, total=False
)

ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": Literal[
            "ASGTotalCPUUtilization",
            "ASGTotalNetworkIn",
            "ASGTotalNetworkOut",
            "ALBTargetGroupRequestCount",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    {
        "PredefinedScalingMetricSpecification": ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)

_RequiredClientCreateScalingPlanScalingInstructionsTypeDef = TypedDict(
    "_RequiredClientCreateScalingPlanScalingInstructionsTypeDef",
    {"ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"]},
)
_OptionalClientCreateScalingPlanScalingInstructionsTypeDef = TypedDict(
    "_OptionalClientCreateScalingPlanScalingInstructionsTypeDef",
    {
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[
            ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef
        ],
        "PredefinedLoadMetricSpecification": ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
        "CustomizedLoadMetricSpecification": ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": Literal[
            "SetForecastCapacityToMaxCapacity",
            "SetMaxCapacityToForecastCapacity",
            "SetMaxCapacityAboveForecastCapacity",
        ],
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": Literal["ForecastAndScale", "ForecastOnly"],
        "ScalingPolicyUpdateBehavior": Literal["KeepExternalPolicies", "ReplaceExternalPolicies"],
        "DisableDynamicScaling": bool,
    },
    total=False,
)


class ClientCreateScalingPlanScalingInstructionsTypeDef(
    _RequiredClientCreateScalingPlanScalingInstructionsTypeDef,
    _OptionalClientCreateScalingPlanScalingInstructionsTypeDef,
):
    pass


ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef",
    {
        "PredefinedScalingMetricSpecification": ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)

ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyType": str,
        "TargetTrackingConfiguration": ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "ScalingPolicies": List[
            ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef
        ],
        "ScalingStatusCode": Literal["Inactive", "PartiallyActive", "Active"],
        "ScalingStatusMessage": str,
    },
    total=False,
)

ClientDescribeScalingPlanResourcesResponseTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseTypeDef",
    {
        "ScalingPlanResources": List[
            ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef = TypedDict(
    "ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeScalingPlansApplicationSourcesTypeDef = TypedDict(
    "ClientDescribeScalingPlansApplicationSourcesTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef],
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[
            ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef
        ],
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": Literal[
            "ASGTotalCPUUtilization",
            "ASGTotalNetworkIn",
            "ASGTotalNetworkOut",
            "ALBTargetGroupRequestCount",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef",
    {
        "PredefinedScalingMetricSpecification": ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef",
    {
        "ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[
            ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef
        ],
        "PredefinedLoadMetricSpecification": ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
        "CustomizedLoadMetricSpecification": ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": Literal[
            "SetForecastCapacityToMaxCapacity",
            "SetMaxCapacityToForecastCapacity",
            "SetMaxCapacityAboveForecastCapacity",
        ],
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": Literal["ForecastAndScale", "ForecastOnly"],
        "ScalingPolicyUpdateBehavior": Literal["KeepExternalPolicies", "ReplaceExternalPolicies"],
        "DisableDynamicScaling": bool,
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef,
        "ScalingInstructions": List[
            ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef
        ],
        "StatusCode": Literal[
            "Active",
            "ActiveWithProblems",
            "CreationInProgress",
            "CreationFailed",
            "DeletionInProgress",
            "DeletionFailed",
            "UpdateInProgress",
            "UpdateFailed",
        ],
        "StatusMessage": str,
        "StatusStartTime": datetime,
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeScalingPlansResponseTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseTypeDef",
    {"ScalingPlans": List[ClientDescribeScalingPlansResponseScalingPlansTypeDef], "NextToken": str},
    total=False,
)

ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef = TypedDict(
    "ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef",
    {"Timestamp": datetime, "Value": float},
    total=False,
)

ClientGetScalingPlanResourceForecastDataResponseTypeDef = TypedDict(
    "ClientGetScalingPlanResourceForecastDataResponseTypeDef",
    {"Datapoints": List[ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef]},
    total=False,
)

ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef = TypedDict(
    "ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateScalingPlanApplicationSourceTypeDef = TypedDict(
    "ClientUpdateScalingPlanApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef],
    },
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": Literal[
            "ASGTotalCPUUtilization",
            "ASGTotalNetworkIn",
            "ASGTotalNetworkOut",
            "ALBTargetGroupRequestCount",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    {
        "PredefinedScalingMetricSpecification": ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)

_RequiredClientUpdateScalingPlanScalingInstructionsTypeDef = TypedDict(
    "_RequiredClientUpdateScalingPlanScalingInstructionsTypeDef",
    {"ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"]},
)
_OptionalClientUpdateScalingPlanScalingInstructionsTypeDef = TypedDict(
    "_OptionalClientUpdateScalingPlanScalingInstructionsTypeDef",
    {
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[
            ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef
        ],
        "PredefinedLoadMetricSpecification": ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
        "CustomizedLoadMetricSpecification": ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": Literal[
            "SetForecastCapacityToMaxCapacity",
            "SetMaxCapacityToForecastCapacity",
            "SetMaxCapacityAboveForecastCapacity",
        ],
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": Literal["ForecastAndScale", "ForecastOnly"],
        "ScalingPolicyUpdateBehavior": Literal["KeepExternalPolicies", "ReplaceExternalPolicies"],
        "DisableDynamicScaling": bool,
    },
    total=False,
)


class ClientUpdateScalingPlanScalingInstructionsTypeDef(
    _RequiredClientUpdateScalingPlanScalingInstructionsTypeDef,
    _OptionalClientUpdateScalingPlanScalingInstructionsTypeDef,
):
    pass


DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef",
    {
        "PredefinedScalingMetricSpecification": DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)

DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef = TypedDict(
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyType": str,
        "TargetTrackingConfiguration": DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef,
    },
    total=False,
)

DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef = TypedDict(
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "ScalingPolicies": List[
            DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef
        ],
        "ScalingStatusCode": Literal["Inactive", "PartiallyActive", "Active"],
        "ScalingStatusMessage": str,
    },
    total=False,
)

DescribeScalingPlanResourcesPaginateResponseTypeDef = TypedDict(
    "DescribeScalingPlanResourcesPaginateResponseTypeDef",
    {
        "ScalingPlanResources": List[
            DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef
        ]
    },
    total=False,
)

DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef = TypedDict(
    "DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeScalingPlansPaginateApplicationSourcesTypeDef = TypedDict(
    "DescribeScalingPlansPaginateApplicationSourcesTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef],
    },
    total=False,
)

DescribeScalingPlansPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeScalingPlansPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef = TypedDict(
    "DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef = TypedDict(
    "DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[
            DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef
        ],
    },
    total=False,
)

DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": Literal[
            "ASGTotalCPUUtilization",
            "ASGTotalNetworkIn",
            "ASGTotalNetworkOut",
            "ALBTargetGroupRequestCount",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef",
    {
        "PredefinedScalingMetricSpecification": DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)

DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef = TypedDict(
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef",
    {
        "ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[
            DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef
        ],
        "PredefinedLoadMetricSpecification": DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
        "CustomizedLoadMetricSpecification": DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": Literal[
            "SetForecastCapacityToMaxCapacity",
            "SetMaxCapacityToForecastCapacity",
            "SetMaxCapacityAboveForecastCapacity",
        ],
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": Literal["ForecastAndScale", "ForecastOnly"],
        "ScalingPolicyUpdateBehavior": Literal["KeepExternalPolicies", "ReplaceExternalPolicies"],
        "DisableDynamicScaling": bool,
    },
    total=False,
)

DescribeScalingPlansPaginateResponseScalingPlansTypeDef = TypedDict(
    "DescribeScalingPlansPaginateResponseScalingPlansTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef,
        "ScalingInstructions": List[
            DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef
        ],
        "StatusCode": Literal[
            "Active",
            "ActiveWithProblems",
            "CreationInProgress",
            "CreationFailed",
            "DeletionInProgress",
            "DeletionFailed",
            "UpdateInProgress",
            "UpdateFailed",
        ],
        "StatusMessage": str,
        "StatusStartTime": datetime,
        "CreationTime": datetime,
    },
    total=False,
)

DescribeScalingPlansPaginateResponseTypeDef = TypedDict(
    "DescribeScalingPlansPaginateResponseTypeDef",
    {"ScalingPlans": List[DescribeScalingPlansPaginateResponseScalingPlansTypeDef]},
    total=False,
)
