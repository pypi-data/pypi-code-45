"Main interface for application-autoscaling service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef",
    "ClientDescribeScalableTargetsResponseScalableTargetsTypeDef",
    "ClientDescribeScalableTargetsResponseTypeDef",
    "ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef",
    "ClientDescribeScalingActivitiesResponseTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef",
    "ClientDescribeScalingPoliciesResponseTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledActionsTypeDef",
    "ClientDescribeScheduledActionsResponseTypeDef",
    "ClientPutScalingPolicyResponseAlarmsTypeDef",
    "ClientPutScalingPolicyResponseTypeDef",
    "ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    "ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef",
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef",
    "ClientPutScheduledActionScalableTargetActionTypeDef",
    "ClientRegisterScalableTargetSuspendedStateTypeDef",
    "DescribeScalableTargetsPaginatePaginationConfigTypeDef",
    "DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef",
    "DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef",
    "DescribeScalableTargetsPaginateResponseTypeDef",
    "DescribeScalingActivitiesPaginatePaginationConfigTypeDef",
    "DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef",
    "DescribeScalingActivitiesPaginateResponseTypeDef",
    "DescribeScalingPoliciesPaginatePaginationConfigTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef",
    "DescribeScalingPoliciesPaginateResponseTypeDef",
    "DescribeScheduledActionsPaginatePaginationConfigTypeDef",
    "DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef",
    "DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef",
    "DescribeScheduledActionsPaginateResponseTypeDef",
)


_ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef = TypedDict(
    "_ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)


class ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef(
    _ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef
):
    pass


_ClientDescribeScalableTargetsResponseScalableTargetsTypeDef = TypedDict(
    "_ClientDescribeScalableTargetsResponseScalableTargetsTypeDef",
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
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "CreationTime": datetime,
        "SuspendedState": ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef,
    },
    total=False,
)


class ClientDescribeScalableTargetsResponseScalableTargetsTypeDef(
    _ClientDescribeScalableTargetsResponseScalableTargetsTypeDef
):
    """
    - *(dict) --*

      Represents a scalable target.
      - **ServiceNamespace** *(string) --*

        The namespace of the AWS service that provides the resource or ``custom-resource`` for a
        resource provided by your own application or service. For more information, see `AWS Service
        Namespaces
        <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
        in the *Amazon Web Services General Reference* .
    """


_ClientDescribeScalableTargetsResponseTypeDef = TypedDict(
    "_ClientDescribeScalableTargetsResponseTypeDef",
    {
        "ScalableTargets": List[ClientDescribeScalableTargetsResponseScalableTargetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScalableTargetsResponseTypeDef(_ClientDescribeScalableTargetsResponseTypeDef):
    """
    - *(dict) --*

      - **ScalableTargets** *(list) --*

        The scalable targets that match the request parameters.
        - *(dict) --*

          Represents a scalable target.
          - **ServiceNamespace** *(string) --*

            The namespace of the AWS service that provides the resource or ``custom-resource`` for a
            resource provided by your own application or service. For more information, see `AWS
            Service Namespaces
            <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
            in the *Amazon Web Services General Reference* .
    """


_ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef = TypedDict(
    "_ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef",
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


class ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef(
    _ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef
):
    """
    - *(dict) --*

      Represents a scaling activity.
      - **ActivityId** *(string) --*

        The unique identifier of the scaling activity.
    """


_ClientDescribeScalingActivitiesResponseTypeDef = TypedDict(
    "_ClientDescribeScalingActivitiesResponseTypeDef",
    {
        "ScalingActivities": List[ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScalingActivitiesResponseTypeDef(
    _ClientDescribeScalingActivitiesResponseTypeDef
):
    """
    - *(dict) --*

      - **ScalingActivities** *(list) --*

        A list of scaling activity objects.
        - *(dict) --*

          Represents a scaling activity.
          - **ActivityId** *(string) --*

            The unique identifier of the scaling activity.
    """


_ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef
):
    pass


_ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef
):
    pass


_ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef",
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


class ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef
):
    pass


_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
):
    pass


_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
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


class ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef
):
    pass


_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
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
        ],
        "ResourceLabel": str,
    },
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef
):
    pass


_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
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


class ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef
):
    pass


_ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef",
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
        ],
        "PolicyType": Literal["StepScaling", "TargetTrackingScaling"],
        "StepScalingPolicyConfiguration": ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef,
        "TargetTrackingScalingPolicyConfiguration": ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
        "Alarms": List[ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef],
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef
):
    """
    - *(dict) --*

      Represents a scaling policy to use with Application Auto Scaling.
      - **PolicyARN** *(string) --*

        The Amazon Resource Name (ARN) of the scaling policy.
    """


_ClientDescribeScalingPoliciesResponseTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseTypeDef",
    {
        "ScalingPolicies": List[ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScalingPoliciesResponseTypeDef(_ClientDescribeScalingPoliciesResponseTypeDef):
    """
    - *(dict) --*

      - **ScalingPolicies** *(list) --*

        Information about the scaling policies.
        - *(dict) --*

          Represents a scaling policy to use with Application Auto Scaling.
          - **PolicyARN** *(string) --*

            The Amazon Resource Name (ARN) of the scaling policy.
    """


_ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef(
    _ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef
):
    pass


_ClientDescribeScheduledActionsResponseScheduledActionsTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseScheduledActionsTypeDef",
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
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "ScalableTargetAction": ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeScheduledActionsResponseScheduledActionsTypeDef(
    _ClientDescribeScheduledActionsResponseScheduledActionsTypeDef
):
    """
    - *(dict) --*

      Represents a scheduled action.
      - **ScheduledActionName** *(string) --*

        The name of the scheduled action.
    """


_ClientDescribeScheduledActionsResponseTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseTypeDef",
    {
        "ScheduledActions": List[ClientDescribeScheduledActionsResponseScheduledActionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScheduledActionsResponseTypeDef(_ClientDescribeScheduledActionsResponseTypeDef):
    """
    - *(dict) --*

      - **ScheduledActions** *(list) --*

        Information about the scheduled actions.
        - *(dict) --*

          Represents a scheduled action.
          - **ScheduledActionName** *(string) --*

            The name of the scheduled action.
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

      - **PolicyARN** *(string) --*

        The Amazon Resource Name (ARN) of the resulting scaling policy.
    """


_ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef = TypedDict(
    "_ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)


class ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef(
    _ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef
):
    pass


_ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef = TypedDict(
    "_ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef",
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


class ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef(
    _ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef
):
    """
    A step scaling policy.
    This parameter is required if you are creating a policy and the policy type is ``StepScaling`` .
    - **AdjustmentType** *(string) --*

      Specifies whether the ``ScalingAdjustment`` value in a  StepAdjustment is an absolute number
      or a percentage of the current capacity.
    """


_ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef(
    _ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
):
    pass


_ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
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


class ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef(
    _ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef
):
    pass


_ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
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
        ],
        "ResourceLabel": str,
    },
    total=False,
)


class ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef(
    _ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef
):
    pass


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
    """
    A target tracking scaling policy. Includes support for predefined or customized metrics.
    This parameter is required if you are creating a policy and the policy type is
    ``TargetTrackingScaling`` .
    - **TargetValue** *(float) --***[REQUIRED]**

      The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or
      2e-360 to 2e360 (Base 2).
    """


_ClientPutScheduledActionScalableTargetActionTypeDef = TypedDict(
    "_ClientPutScheduledActionScalableTargetActionTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class ClientPutScheduledActionScalableTargetActionTypeDef(
    _ClientPutScheduledActionScalableTargetActionTypeDef
):
    """
    The new minimum and maximum capacity. You can set both values or just one. During the scheduled
    time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out
    to the minimum capacity. If the current capacity is above the maximum capacity, Application Auto
    Scaling scales in to the maximum capacity.
    - **MinCapacity** *(integer) --*

      The minimum capacity.
    """


_ClientRegisterScalableTargetSuspendedStateTypeDef = TypedDict(
    "_ClientRegisterScalableTargetSuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)


class ClientRegisterScalableTargetSuspendedStateTypeDef(
    _ClientRegisterScalableTargetSuspendedStateTypeDef
):
    """
    An embedded object that contains attributes and attribute values that are used to suspend and
    resume automatic scaling. Setting the value of an attribute to ``true`` suspends the specified
    scaling activities. Setting it to ``false`` (default) resumes the specified scaling activities.

      **Suspension Outcomes**
    """


_DescribeScalableTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScalableTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScalableTargetsPaginatePaginationConfigTypeDef(
    _DescribeScalableTargetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef = TypedDict(
    "_DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)


class DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef(
    _DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef
):
    pass


_DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef = TypedDict(
    "_DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef",
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
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "CreationTime": datetime,
        "SuspendedState": DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef,
    },
    total=False,
)


class DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef(
    _DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef
):
    """
    - *(dict) --*

      Represents a scalable target.
      - **ServiceNamespace** *(string) --*

        The namespace of the AWS service that provides the resource or ``custom-resource`` for a
        resource provided by your own application or service. For more information, see `AWS Service
        Namespaces
        <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
        in the *Amazon Web Services General Reference* .
    """


_DescribeScalableTargetsPaginateResponseTypeDef = TypedDict(
    "_DescribeScalableTargetsPaginateResponseTypeDef",
    {"ScalableTargets": List[DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef]},
    total=False,
)


class DescribeScalableTargetsPaginateResponseTypeDef(
    _DescribeScalableTargetsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ScalableTargets** *(list) --*

        The scalable targets that match the request parameters.
        - *(dict) --*

          Represents a scalable target.
          - **ServiceNamespace** *(string) --*

            The namespace of the AWS service that provides the resource or ``custom-resource`` for a
            resource provided by your own application or service. For more information, see `AWS
            Service Namespaces
            <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
            in the *Amazon Web Services General Reference* .
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


_DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef = TypedDict(
    "_DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef",
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


class DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef(
    _DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef
):
    """
    - *(dict) --*

      Represents a scaling activity.
      - **ActivityId** *(string) --*

        The unique identifier of the scaling activity.
    """


_DescribeScalingActivitiesPaginateResponseTypeDef = TypedDict(
    "_DescribeScalingActivitiesPaginateResponseTypeDef",
    {"ScalingActivities": List[DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef]},
    total=False,
)


class DescribeScalingActivitiesPaginateResponseTypeDef(
    _DescribeScalingActivitiesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ScalingActivities** *(list) --*

        A list of scaling activity objects.
        - *(dict) --*

          Represents a scaling activity.
          - **ActivityId** *(string) --*

            The unique identifier of the scaling activity.
    """


_DescribeScalingPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScalingPoliciesPaginatePaginationConfigTypeDef(
    _DescribeScalingPoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef
):
    pass


_DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef
):
    pass


_DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef",
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


class DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef
):
    pass


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
):
    pass


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
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


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef
):
    pass


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
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
        ],
        "ResourceLabel": str,
    },
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef
):
    pass


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
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


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef
):
    pass


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef",
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
        ],
        "PolicyType": Literal["StepScaling", "TargetTrackingScaling"],
        "StepScalingPolicyConfiguration": DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef,
        "TargetTrackingScalingPolicyConfiguration": DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
        "Alarms": List[DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef],
        "CreationTime": datetime,
    },
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef
):
    """
    - *(dict) --*

      Represents a scaling policy to use with Application Auto Scaling.
      - **PolicyARN** *(string) --*

        The Amazon Resource Name (ARN) of the scaling policy.
    """


_DescribeScalingPoliciesPaginateResponseTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseTypeDef",
    {"ScalingPolicies": List[DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef]},
    total=False,
)


class DescribeScalingPoliciesPaginateResponseTypeDef(
    _DescribeScalingPoliciesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ScalingPolicies** *(list) --*

        Information about the scaling policies.
        - *(dict) --*

          Represents a scaling policy to use with Application Auto Scaling.
          - **PolicyARN** *(string) --*

            The Amazon Resource Name (ARN) of the scaling policy.
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


_DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef(
    _DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef
):
    pass


_DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef",
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
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "ScalableTargetAction": DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)


class DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef(
    _DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef
):
    """
    - *(dict) --*

      Represents a scheduled action.
      - **ScheduledActionName** *(string) --*

        The name of the scheduled action.
    """


_DescribeScheduledActionsPaginateResponseTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseTypeDef",
    {"ScheduledActions": List[DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef]},
    total=False,
)


class DescribeScheduledActionsPaginateResponseTypeDef(
    _DescribeScheduledActionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ScheduledActions** *(list) --*

        Information about the scheduled actions.
        - *(dict) --*

          Represents a scheduled action.
          - **ScheduledActionName** *(string) --*

            The name of the scheduled action.
    """
