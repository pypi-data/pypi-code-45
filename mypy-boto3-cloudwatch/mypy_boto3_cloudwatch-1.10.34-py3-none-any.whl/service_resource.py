"Main interface for cloudwatch service ServiceResource"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, List
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_cloudwatch.service_resource as service_resource_scope
from mypy_boto3_cloudwatch.type_defs import (
    AlarmDescribeHistoryResponseTypeDef,
    AlarmsFilterDimensionsTypeDef,
    MetricGetStatisticsDimensionsTypeDef,
    MetricGetStatisticsResponseTypeDef,
    MetricPutAlarmDimensionsTypeDef,
    MetricPutAlarmMetricsTypeDef,
    MetricPutAlarmTagsTypeDef,
    MetricsFilterDimensionsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ServiceResource",
    "Alarm",
    "Metric",
    "ServiceResourceAlarmsCollection",
    "ServiceResourceMetricsCollection",
    "MetricAlarmsCollection",
)


class ServiceResource(Boto3ServiceResource):
    """
    [CloudWatch.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudwatch.html#CloudWatch.ServiceResource)
    """

    alarms: service_resource_scope.ServiceResourceAlarmsCollection
    metrics: service_resource_scope.ServiceResourceMetricsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Alarm(self, name: str) -> service_resource_scope.Alarm:
        """
        [ServiceResource.Alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Alarm)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Metric(self, namespace: str, name: str) -> service_resource_scope.Metric:
        """
        [ServiceResource.Metric documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Metric)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudwatch.html#CloudWatch.ServiceResource.get_available_subresources)
        """


class Alarm(Boto3ServiceResource):
    """
    [Alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Alarm)
    """

    alarm_name: str
    alarm_arn: str
    alarm_description: str
    alarm_configuration_updated_timestamp: datetime
    actions_enabled: bool
    ok_actions: List[Any]
    alarm_actions: List[Any]
    insufficient_data_actions: List[Any]
    state_value: str
    state_reason: str
    state_reason_data: str
    state_updated_timestamp: datetime
    metric_name: str
    namespace: str
    statistic: str
    extended_statistic: str
    dimensions: List[Any]
    period: int
    unit: str
    evaluation_periods: int
    datapoints_to_alarm: int
    threshold: float
    comparison_operator: str
    treat_missing_data: str
    evaluate_low_sample_count_percentile: str
    metrics: List[Any]
    threshold_metric_id: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_history(
        self,
        HistoryItemType: Literal["ConfigurationUpdate", "StateUpdate", "Action"] = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> AlarmDescribeHistoryResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_actions(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_actions(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_state(
        self,
        StateValue: Literal["OK", "ALARM", "INSUFFICIENT_DATA"],
        StateReason: str,
        StateReasonData: str = None,
    ) -> None:
        pass


class Metric(Boto3ServiceResource):
    """
    [Metric documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Metric)
    """

    metric_name: str
    dimensions: List[Any]
    namespace: str
    name: str
    alarms: service_resource_scope.MetricAlarmsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_statistics(
        self,
        StartTime: datetime,
        EndTime: datetime,
        Period: int,
        Dimensions: List[MetricGetStatisticsDimensionsTypeDef] = None,
        Statistics: List[Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"]] = None,
        ExtendedStatistics: List[str] = None,
        Unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ] = None,
    ) -> MetricGetStatisticsResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_alarm(
        self,
        AlarmName: str,
        EvaluationPeriods: int,
        ComparisonOperator: Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanLowerOrGreaterThanUpperThreshold",
            "LessThanLowerThreshold",
            "GreaterThanUpperThreshold",
        ],
        AlarmDescription: str = None,
        ActionsEnabled: bool = None,
        OKActions: List[str] = None,
        AlarmActions: List[str] = None,
        InsufficientDataActions: List[str] = None,
        Statistic: Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"] = None,
        ExtendedStatistic: str = None,
        Dimensions: List[MetricPutAlarmDimensionsTypeDef] = None,
        Period: int = None,
        Unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ] = None,
        DatapointsToAlarm: int = None,
        Threshold: float = None,
        TreatMissingData: str = None,
        EvaluateLowSampleCountPercentile: str = None,
        Metrics: List[MetricPutAlarmMetricsTypeDef] = None,
        Tags: List[MetricPutAlarmTagsTypeDef] = None,
        ThresholdMetricId: str = None,
    ) -> service_resource_scope.Alarm:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_data(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class ServiceResourceAlarmsCollection(ResourceCollection):
    """
    [ServiceResource.alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudwatch.html#CloudWatch.ServiceResource.alarms)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Alarm]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_actions(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_actions(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        StateValue: Literal["OK", "ALARM", "INSUFFICIENT_DATA"] = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> List[service_resource_scope.Alarm]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Alarm]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Alarm]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceMetricsCollection(ResourceCollection):
    """
    [ServiceResource.metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudwatch.html#CloudWatch.ServiceResource.metrics)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Metric]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[MetricsFilterDimensionsTypeDef] = None,
        NextToken: str = None,
    ) -> List[service_resource_scope.Metric]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Metric]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Metric]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class MetricAlarmsCollection(ResourceCollection):
    """
    [Metric.alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudwatch.html#CloudWatch.Metric.alarms)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Alarm]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_actions(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_actions(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Statistic: Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"] = None,
        ExtendedStatistic: str = None,
        Dimensions: List[AlarmsFilterDimensionsTypeDef] = None,
        Period: int = None,
        Unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ] = None,
    ) -> List[service_resource_scope.Alarm]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Alarm]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Alarm]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass
