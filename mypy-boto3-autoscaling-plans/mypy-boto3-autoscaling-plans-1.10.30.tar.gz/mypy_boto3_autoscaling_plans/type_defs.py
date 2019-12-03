"Main interface for autoscaling-plans service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef",
    "ClientCreateScalingPlanApplicationSourceTypeDef",
    "ClientCreateScalingPlanResponseTypeDef",
    "ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    "ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    "ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef",
    "ClientDescribeScalingPlanResourcesResponseTypeDef",
    "ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef",
    "ClientDescribeScalingPlansApplicationSourcesTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansTypeDef",
    "ClientDescribeScalingPlansResponseTypeDef",
    "ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef",
    "ClientGetScalingPlanResourceForecastDataResponseTypeDef",
    "ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef",
    "ClientUpdateScalingPlanApplicationSourceTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTypeDef",
    "DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseTypeDef",
    "DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef",
    "DescribeScalingPlansPaginateApplicationSourcesTypeDef",
    "DescribeScalingPlansPaginatePaginationConfigTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansTypeDef",
    "DescribeScalingPlansPaginateResponseTypeDef",
)


_ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef = TypedDict(
    "_ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef(
    _ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef
):
    pass


_ClientCreateScalingPlanApplicationSourceTypeDef = TypedDict(
    "_ClientCreateScalingPlanApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef],
    },
    total=False,
)


class ClientCreateScalingPlanApplicationSourceTypeDef(
    _ClientCreateScalingPlanApplicationSourceTypeDef
):
    """
    A CloudFormation stack or set of tags. You can create one scaling plan per application source.
    - **CloudFormationStackARN** *(string) --*

      The Amazon Resource Name (ARN) of a AWS CloudFormation stack.
    """


_ClientCreateScalingPlanResponseTypeDef = TypedDict(
    "_ClientCreateScalingPlanResponseTypeDef", {"ScalingPlanVersion": int}, total=False
)


class ClientCreateScalingPlanResponseTypeDef(_ClientCreateScalingPlanResponseTypeDef):
    """
    - *(dict) --*

      - **ScalingPlanVersion** *(integer) --*

        The version number of the scaling plan. This value is always 1.
        Currently, you cannot specify multiple scaling plan versions.
    """


_ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef(
    _ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
):
    pass


_ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
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


class ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef(
    _ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef
):
    pass


_ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
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


class ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef(
    _ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef
):
    pass


_ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef(
    _ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
):
    pass


_ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
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


class ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef(
    _ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef
):
    pass


_ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
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


class ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef(
    _ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef
):
    pass


_ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "_ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
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


class ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef(
    _ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef
):
    pass


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
    """
    - *(dict) --*

      Describes a scaling instruction for a scalable resource.
      The scaling instruction is used in combination with a scaling plan, which is a set of
      instructions for configuring dynamic scaling and predictive scaling for the scalable resources
      in your application. Each scaling instruction applies to one resource.
      AWS Auto Scaling creates target tracking scaling policies based on the scaling instructions.
      Target tracking scaling policies adjust the capacity of your scalable resource as required to
      maintain resource utilization at the target value that you specified.
      AWS Auto Scaling also configures predictive scaling for your Amazon EC2 Auto Scaling groups
      using a subset of parameters, including the load metric, the scaling metric, the target value
      for the scaling metric, the predictive scaling mode (forecast and scale or forecast only), and
      the desired behavior when the forecast capacity exceeds the maximum capacity of the resource.
      With predictive scaling, AWS Auto Scaling generates forecasts with traffic predictions for the
      two days ahead and schedules scaling actions that proactively add and remove resource capacity
      to match the forecast.
      We recommend waiting a minimum of 24 hours after creating an Auto Scaling group to configure
      predictive scaling. At minimum, there must be 24 hours of historical data to generate a
      forecast.
      For more information, see `Getting Started with AWS Auto Scaling
      <https://docs.aws.amazon.com/autoscaling/plans/userguide/auto-scaling-getting-started.html>`__
      .
      - **ServiceNamespace** *(string) --***[REQUIRED]**

        The namespace of the AWS service.
    """


_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef(
    _ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef
):
    pass


_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef",
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


class ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef(
    _ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef
):
    pass


_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef",
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


class ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef(
    _ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef
):
    pass


_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef",
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


class ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef(
    _ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef
):
    pass


_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyType": str,
        "TargetTrackingConfiguration": ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef(
    _ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef
):
    pass


_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef",
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


class ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef(
    _ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef
):
    """
    - *(dict) --*

      Represents a scalable resource.
      - **ScalingPlanName** *(string) --*

        The name of the scaling plan.
    """


_ClientDescribeScalingPlanResourcesResponseTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseTypeDef",
    {
        "ScalingPlanResources": List[
            ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScalingPlanResourcesResponseTypeDef(
    _ClientDescribeScalingPlanResourcesResponseTypeDef
):
    """
    - *(dict) --*

      - **ScalingPlanResources** *(list) --*

        Information about the scalable resources.
        - *(dict) --*

          Represents a scalable resource.
          - **ScalingPlanName** *(string) --*

            The name of the scaling plan.
    """


_ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef = TypedDict(
    "_ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef(
    _ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef
):
    pass


_ClientDescribeScalingPlansApplicationSourcesTypeDef = TypedDict(
    "_ClientDescribeScalingPlansApplicationSourcesTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef],
    },
    total=False,
)


class ClientDescribeScalingPlansApplicationSourcesTypeDef(
    _ClientDescribeScalingPlansApplicationSourcesTypeDef
):
    """
    - *(dict) --*

      Represents an application source.
      - **CloudFormationStackARN** *(string) --*

        The Amazon Resource Name (ARN) of a AWS CloudFormation stack.
    """


_ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef
):
    pass


_ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[
            ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef
):
    pass


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
):
    pass


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
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


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef
):
    pass


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
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


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef
):
    pass


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
):
    pass


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
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


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef
):
    pass


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
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


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef
):
    pass


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef",
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


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef
):
    pass


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef",
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


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef
):
    pass


_ClientDescribeScalingPlansResponseScalingPlansTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansTypeDef",
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


class ClientDescribeScalingPlansResponseScalingPlansTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansTypeDef
):
    """
    - *(dict) --*

      Represents a scaling plan.
      - **ScalingPlanName** *(string) --*

        The name of the scaling plan.
    """


_ClientDescribeScalingPlansResponseTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseTypeDef",
    {"ScalingPlans": List[ClientDescribeScalingPlansResponseScalingPlansTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeScalingPlansResponseTypeDef(_ClientDescribeScalingPlansResponseTypeDef):
    """
    - *(dict) --*

      - **ScalingPlans** *(list) --*

        Information about the scaling plans.
        - *(dict) --*

          Represents a scaling plan.
          - **ScalingPlanName** *(string) --*

            The name of the scaling plan.
    """


_ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef = TypedDict(
    "_ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef",
    {"Timestamp": datetime, "Value": float},
    total=False,
)


class ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef(
    _ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef
):
    """
    - *(dict) --*

      Represents a single value in the forecast data used for predictive scaling.
      - **Timestamp** *(datetime) --*

        The time stamp for the data point in UTC format.
    """


_ClientGetScalingPlanResourceForecastDataResponseTypeDef = TypedDict(
    "_ClientGetScalingPlanResourceForecastDataResponseTypeDef",
    {"Datapoints": List[ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef]},
    total=False,
)


class ClientGetScalingPlanResourceForecastDataResponseTypeDef(
    _ClientGetScalingPlanResourceForecastDataResponseTypeDef
):
    """
    - *(dict) --*

      - **Datapoints** *(list) --*

        The data points to return.
        - *(dict) --*

          Represents a single value in the forecast data used for predictive scaling.
          - **Timestamp** *(datetime) --*

            The time stamp for the data point in UTC format.
    """


_ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef = TypedDict(
    "_ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef(
    _ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef
):
    pass


_ClientUpdateScalingPlanApplicationSourceTypeDef = TypedDict(
    "_ClientUpdateScalingPlanApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef],
    },
    total=False,
)


class ClientUpdateScalingPlanApplicationSourceTypeDef(
    _ClientUpdateScalingPlanApplicationSourceTypeDef
):
    """
    A CloudFormation stack or set of tags.
    - **CloudFormationStackARN** *(string) --*

      The Amazon Resource Name (ARN) of a AWS CloudFormation stack.
    """


_ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef(
    _ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
):
    pass


_ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
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


class ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef(
    _ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef
):
    pass


_ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
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


class ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef(
    _ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef
):
    pass


_ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef(
    _ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
):
    pass


_ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
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


class ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef(
    _ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef
):
    pass


_ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
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


class ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef(
    _ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef
):
    pass


_ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "_ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
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


class ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef(
    _ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef
):
    pass


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
    """
    - *(dict) --*

      Describes a scaling instruction for a scalable resource.
      The scaling instruction is used in combination with a scaling plan, which is a set of
      instructions for configuring dynamic scaling and predictive scaling for the scalable resources
      in your application. Each scaling instruction applies to one resource.
      AWS Auto Scaling creates target tracking scaling policies based on the scaling instructions.
      Target tracking scaling policies adjust the capacity of your scalable resource as required to
      maintain resource utilization at the target value that you specified.
      AWS Auto Scaling also configures predictive scaling for your Amazon EC2 Auto Scaling groups
      using a subset of parameters, including the load metric, the scaling metric, the target value
      for the scaling metric, the predictive scaling mode (forecast and scale or forecast only), and
      the desired behavior when the forecast capacity exceeds the maximum capacity of the resource.
      With predictive scaling, AWS Auto Scaling generates forecasts with traffic predictions for the
      two days ahead and schedules scaling actions that proactively add and remove resource capacity
      to match the forecast.
      We recommend waiting a minimum of 24 hours after creating an Auto Scaling group to configure
      predictive scaling. At minimum, there must be 24 hours of historical data to generate a
      forecast.
      For more information, see `Getting Started with AWS Auto Scaling
      <https://docs.aws.amazon.com/autoscaling/plans/userguide/auto-scaling-getting-started.html>`__
      .
      - **ServiceNamespace** *(string) --***[REQUIRED]**

        The namespace of the AWS service.
    """


_DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef(
    _DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef
):
    pass


_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef",
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


class DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef
):
    pass


_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef",
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


class DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef
):
    pass


_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef",
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


class DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef
):
    pass


_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyType": str,
        "TargetTrackingConfiguration": DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef,
    },
    total=False,
)


class DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef
):
    pass


_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef",
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


class DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef
):
    """
    - *(dict) --*

      Represents a scalable resource.
      - **ScalingPlanName** *(string) --*

        The name of the scaling plan.
    """


_DescribeScalingPlanResourcesPaginateResponseTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseTypeDef",
    {
        "ScalingPlanResources": List[
            DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef
        ]
    },
    total=False,
)


class DescribeScalingPlanResourcesPaginateResponseTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ScalingPlanResources** *(list) --*

        Information about the scalable resources.
        - *(dict) --*

          Represents a scalable resource.
          - **ScalingPlanName** *(string) --*

            The name of the scaling plan.
    """


_DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef(
    _DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef
):
    pass


_DescribeScalingPlansPaginateApplicationSourcesTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateApplicationSourcesTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef],
    },
    total=False,
)


class DescribeScalingPlansPaginateApplicationSourcesTypeDef(
    _DescribeScalingPlansPaginateApplicationSourcesTypeDef
):
    """
    - *(dict) --*

      Represents an application source.
      - **CloudFormationStackARN** *(string) --*

        The Amazon Resource Name (ARN) of a AWS CloudFormation stack.
    """


_DescribeScalingPlansPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScalingPlansPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScalingPlansPaginatePaginationConfigTypeDef(
    _DescribeScalingPlansPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef
):
    pass


_DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[
            DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef
        ],
    },
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef
):
    pass


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
):
    pass


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
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


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef
):
    pass


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
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


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef
):
    pass


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
):
    pass


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
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


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef
):
    pass


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
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


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef
):
    pass


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef",
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


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef
):
    pass


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef",
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


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef
):
    pass


_DescribeScalingPlansPaginateResponseScalingPlansTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansTypeDef",
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


class DescribeScalingPlansPaginateResponseScalingPlansTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansTypeDef
):
    """
    - *(dict) --*

      Represents a scaling plan.
      - **ScalingPlanName** *(string) --*

        The name of the scaling plan.
    """


_DescribeScalingPlansPaginateResponseTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseTypeDef",
    {"ScalingPlans": List[DescribeScalingPlansPaginateResponseScalingPlansTypeDef]},
    total=False,
)


class DescribeScalingPlansPaginateResponseTypeDef(_DescribeScalingPlansPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ScalingPlans** *(list) --*

        Information about the scaling plans.
        - *(dict) --*

          Represents a scaling plan.
          - **ScalingPlanName** *(string) --*

            The name of the scaling plan.
    """
