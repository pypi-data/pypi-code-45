"Main interface for cloudwatch service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef = TypedDict(
    "AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef",
    {
        "AlarmName": str,
        "Timestamp": datetime,
        "HistoryItemType": Literal["ConfigurationUpdate", "StateUpdate", "Action"],
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)

AlarmDescribeHistoryResponseTypeDef = TypedDict(
    "AlarmDescribeHistoryResponseTypeDef",
    {
        "AlarmHistoryItems": List[AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef],
        "NextToken": str,
    },
    total=False,
)

AlarmExistsWaitWaiterConfigTypeDef = TypedDict(
    "AlarmExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

_RequiredAlarmsFilterDimensionsTypeDef = TypedDict(
    "_RequiredAlarmsFilterDimensionsTypeDef", {"Name": str}
)
_OptionalAlarmsFilterDimensionsTypeDef = TypedDict(
    "_OptionalAlarmsFilterDimensionsTypeDef", {"Value": str}, total=False
)


class AlarmsFilterDimensionsTypeDef(
    _RequiredAlarmsFilterDimensionsTypeDef, _OptionalAlarmsFilterDimensionsTypeDef
):
    pass


_RequiredClientDeleteAnomalyDetectorDimensionsTypeDef = TypedDict(
    "_RequiredClientDeleteAnomalyDetectorDimensionsTypeDef", {"Name": str}
)
_OptionalClientDeleteAnomalyDetectorDimensionsTypeDef = TypedDict(
    "_OptionalClientDeleteAnomalyDetectorDimensionsTypeDef", {"Value": str}, total=False
)


class ClientDeleteAnomalyDetectorDimensionsTypeDef(
    _RequiredClientDeleteAnomalyDetectorDimensionsTypeDef,
    _OptionalClientDeleteAnomalyDetectorDimensionsTypeDef,
):
    pass


ClientDeleteInsightRulesResponseFailuresTypeDef = TypedDict(
    "ClientDeleteInsightRulesResponseFailuresTypeDef",
    {"FailureResource": str, "ExceptionType": str, "FailureCode": str, "FailureDescription": str},
    total=False,
)

ClientDeleteInsightRulesResponseTypeDef = TypedDict(
    "ClientDeleteInsightRulesResponseTypeDef",
    {"Failures": List[ClientDeleteInsightRulesResponseFailuresTypeDef]},
    total=False,
)

ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef = TypedDict(
    "ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef",
    {
        "AlarmName": str,
        "Timestamp": datetime,
        "HistoryItemType": Literal["ConfigurationUpdate", "StateUpdate", "Action"],
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)

ClientDescribeAlarmHistoryResponseTypeDef = TypedDict(
    "ClientDescribeAlarmHistoryResponseTypeDef",
    {
        "AlarmHistoryItems": List[ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeAlarmsForMetricDimensionsTypeDef = TypedDict(
    "_RequiredClientDescribeAlarmsForMetricDimensionsTypeDef", {"Name": str}
)
_OptionalClientDescribeAlarmsForMetricDimensionsTypeDef = TypedDict(
    "_OptionalClientDescribeAlarmsForMetricDimensionsTypeDef", {"Value": str}, total=False
)


class ClientDescribeAlarmsForMetricDimensionsTypeDef(
    _RequiredClientDescribeAlarmsForMetricDimensionsTypeDef,
    _OptionalClientDescribeAlarmsForMetricDimensionsTypeDef,
):
    pass


ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef",
    {
        "Metric": ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": Literal[
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
        ],
    },
    total=False,
)

ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef",
    {
        "Id": str,
        "MetricStat": ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)

ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef",
    {
        "AlarmName": str,
        "AlarmArn": str,
        "AlarmDescription": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "StateValue": Literal["OK", "ALARM", "INSUFFICIENT_DATA"],
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"],
        "ExtendedStatistic": str,
        "Dimensions": List[ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef],
        "Period": int,
        "Unit": Literal[
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
        ],
        "EvaluationPeriods": int,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanLowerOrGreaterThanUpperThreshold",
            "LessThanLowerThreshold",
            "GreaterThanUpperThreshold",
        ],
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List[ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef],
        "ThresholdMetricId": str,
    },
    total=False,
)

ClientDescribeAlarmsForMetricResponseTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseTypeDef",
    {"MetricAlarms": List[ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef]},
    total=False,
)

ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef",
    {
        "Metric": ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": Literal[
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
        ],
    },
    total=False,
)

ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef",
    {
        "Id": str,
        "MetricStat": ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)

ClientDescribeAlarmsResponseMetricAlarmsTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseMetricAlarmsTypeDef",
    {
        "AlarmName": str,
        "AlarmArn": str,
        "AlarmDescription": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "StateValue": Literal["OK", "ALARM", "INSUFFICIENT_DATA"],
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"],
        "ExtendedStatistic": str,
        "Dimensions": List[ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef],
        "Period": int,
        "Unit": Literal[
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
        ],
        "EvaluationPeriods": int,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanLowerOrGreaterThanUpperThreshold",
            "LessThanLowerThreshold",
            "GreaterThanUpperThreshold",
        ],
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List[ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef],
        "ThresholdMetricId": str,
    },
    total=False,
)

ClientDescribeAlarmsResponseTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseTypeDef",
    {"MetricAlarms": List[ClientDescribeAlarmsResponseMetricAlarmsTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientDescribeAnomalyDetectorsDimensionsTypeDef = TypedDict(
    "_RequiredClientDescribeAnomalyDetectorsDimensionsTypeDef", {"Name": str}
)
_OptionalClientDescribeAnomalyDetectorsDimensionsTypeDef = TypedDict(
    "_OptionalClientDescribeAnomalyDetectorsDimensionsTypeDef", {"Value": str}, total=False
)


class ClientDescribeAnomalyDetectorsDimensionsTypeDef(
    _RequiredClientDescribeAnomalyDetectorsDimensionsTypeDef,
    _OptionalClientDescribeAnomalyDetectorsDimensionsTypeDef,
):
    pass


ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef = TypedDict(
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)

ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef = TypedDict(
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef",
    {
        "ExcludedTimeRanges": List[
            ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef
        ],
        "MetricTimezone": str,
    },
    total=False,
)

ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef = TypedDict(
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef = TypedDict(
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef],
        "Stat": str,
        "Configuration": ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeAnomalyDetectorsResponseTypeDef = TypedDict(
    "ClientDescribeAnomalyDetectorsResponseTypeDef",
    {
        "AnomalyDetectors": List[ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeInsightRulesResponseInsightRulesTypeDef = TypedDict(
    "ClientDescribeInsightRulesResponseInsightRulesTypeDef",
    {"Name": str, "State": str, "Schema": str, "Definition": str},
    total=False,
)

ClientDescribeInsightRulesResponseTypeDef = TypedDict(
    "ClientDescribeInsightRulesResponseTypeDef",
    {"NextToken": str, "InsightRules": List[ClientDescribeInsightRulesResponseInsightRulesTypeDef]},
    total=False,
)

ClientDisableInsightRulesResponseFailuresTypeDef = TypedDict(
    "ClientDisableInsightRulesResponseFailuresTypeDef",
    {"FailureResource": str, "ExceptionType": str, "FailureCode": str, "FailureDescription": str},
    total=False,
)

ClientDisableInsightRulesResponseTypeDef = TypedDict(
    "ClientDisableInsightRulesResponseTypeDef",
    {"Failures": List[ClientDisableInsightRulesResponseFailuresTypeDef]},
    total=False,
)

ClientEnableInsightRulesResponseFailuresTypeDef = TypedDict(
    "ClientEnableInsightRulesResponseFailuresTypeDef",
    {"FailureResource": str, "ExceptionType": str, "FailureCode": str, "FailureDescription": str},
    total=False,
)

ClientEnableInsightRulesResponseTypeDef = TypedDict(
    "ClientEnableInsightRulesResponseTypeDef",
    {"Failures": List[ClientEnableInsightRulesResponseFailuresTypeDef]},
    total=False,
)

ClientGetDashboardResponseTypeDef = TypedDict(
    "ClientGetDashboardResponseTypeDef",
    {"DashboardArn": str, "DashboardBody": str, "DashboardName": str},
    total=False,
)

ClientGetInsightRuleReportResponseContributorsDatapointsTypeDef = TypedDict(
    "ClientGetInsightRuleReportResponseContributorsDatapointsTypeDef",
    {"Timestamp": datetime, "ApproximateValue": float},
    total=False,
)

ClientGetInsightRuleReportResponseContributorsTypeDef = TypedDict(
    "ClientGetInsightRuleReportResponseContributorsTypeDef",
    {
        "Keys": List[str],
        "ApproximateAggregateValue": float,
        "Datapoints": List[ClientGetInsightRuleReportResponseContributorsDatapointsTypeDef],
    },
    total=False,
)

ClientGetInsightRuleReportResponseMetricDatapointsTypeDef = TypedDict(
    "ClientGetInsightRuleReportResponseMetricDatapointsTypeDef",
    {
        "Timestamp": datetime,
        "UniqueContributors": float,
        "MaxContributorValue": float,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
    },
    total=False,
)

ClientGetInsightRuleReportResponseTypeDef = TypedDict(
    "ClientGetInsightRuleReportResponseTypeDef",
    {
        "KeyLabels": List[str],
        "AggregationStatistic": str,
        "AggregateValue": float,
        "ApproximateUniqueCount": int,
        "Contributors": List[ClientGetInsightRuleReportResponseContributorsTypeDef],
        "MetricDatapoints": List[ClientGetInsightRuleReportResponseMetricDatapointsTypeDef],
    },
    total=False,
)

ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef = TypedDict(
    "ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef = TypedDict(
    "ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef],
    },
    total=False,
)

ClientGetMetricDataMetricDataQueriesMetricStatTypeDef = TypedDict(
    "ClientGetMetricDataMetricDataQueriesMetricStatTypeDef",
    {
        "Metric": ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": Literal[
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
        ],
    },
    total=False,
)

_RequiredClientGetMetricDataMetricDataQueriesTypeDef = TypedDict(
    "_RequiredClientGetMetricDataMetricDataQueriesTypeDef", {"Id": str}
)
_OptionalClientGetMetricDataMetricDataQueriesTypeDef = TypedDict(
    "_OptionalClientGetMetricDataMetricDataQueriesTypeDef",
    {
        "MetricStat": ClientGetMetricDataMetricDataQueriesMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class ClientGetMetricDataMetricDataQueriesTypeDef(
    _RequiredClientGetMetricDataMetricDataQueriesTypeDef,
    _OptionalClientGetMetricDataMetricDataQueriesTypeDef,
):
    pass


ClientGetMetricDataResponseMessagesTypeDef = TypedDict(
    "ClientGetMetricDataResponseMessagesTypeDef", {"Code": str, "Value": str}, total=False
)

ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef = TypedDict(
    "ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef",
    {"Code": str, "Value": str},
    total=False,
)

ClientGetMetricDataResponseMetricDataResultsTypeDef = TypedDict(
    "ClientGetMetricDataResponseMetricDataResultsTypeDef",
    {
        "Id": str,
        "Label": str,
        "Timestamps": List[datetime],
        "Values": List[float],
        "StatusCode": Literal["Complete", "InternalError", "PartialData"],
        "Messages": List[ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef],
    },
    total=False,
)

ClientGetMetricDataResponseTypeDef = TypedDict(
    "ClientGetMetricDataResponseTypeDef",
    {
        "MetricDataResults": List[ClientGetMetricDataResponseMetricDataResultsTypeDef],
        "NextToken": str,
        "Messages": List[ClientGetMetricDataResponseMessagesTypeDef],
    },
    total=False,
)

_RequiredClientGetMetricStatisticsDimensionsTypeDef = TypedDict(
    "_RequiredClientGetMetricStatisticsDimensionsTypeDef", {"Name": str}
)
_OptionalClientGetMetricStatisticsDimensionsTypeDef = TypedDict(
    "_OptionalClientGetMetricStatisticsDimensionsTypeDef", {"Value": str}, total=False
)


class ClientGetMetricStatisticsDimensionsTypeDef(
    _RequiredClientGetMetricStatisticsDimensionsTypeDef,
    _OptionalClientGetMetricStatisticsDimensionsTypeDef,
):
    pass


ClientGetMetricStatisticsResponseDatapointsTypeDef = TypedDict(
    "ClientGetMetricStatisticsResponseDatapointsTypeDef",
    {
        "Timestamp": datetime,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
        "Unit": Literal[
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
        ],
        "ExtendedStatistics": Dict[str, float],
    },
    total=False,
)

ClientGetMetricStatisticsResponseTypeDef = TypedDict(
    "ClientGetMetricStatisticsResponseTypeDef",
    {"Label": str, "Datapoints": List[ClientGetMetricStatisticsResponseDatapointsTypeDef]},
    total=False,
)

ClientGetMetricWidgetImageResponseTypeDef = TypedDict(
    "ClientGetMetricWidgetImageResponseTypeDef", {"MetricWidgetImage": bytes}, total=False
)

ClientListDashboardsResponseDashboardEntriesTypeDef = TypedDict(
    "ClientListDashboardsResponseDashboardEntriesTypeDef",
    {"DashboardName": str, "DashboardArn": str, "LastModified": datetime, "Size": int},
    total=False,
)

ClientListDashboardsResponseTypeDef = TypedDict(
    "ClientListDashboardsResponseTypeDef",
    {
        "DashboardEntries": List[ClientListDashboardsResponseDashboardEntriesTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientListMetricsDimensionsTypeDef = TypedDict(
    "_RequiredClientListMetricsDimensionsTypeDef", {"Name": str}
)
_OptionalClientListMetricsDimensionsTypeDef = TypedDict(
    "_OptionalClientListMetricsDimensionsTypeDef", {"Value": str}, total=False
)


class ClientListMetricsDimensionsTypeDef(
    _RequiredClientListMetricsDimensionsTypeDef, _OptionalClientListMetricsDimensionsTypeDef
):
    pass


ClientListMetricsResponseMetricsDimensionsTypeDef = TypedDict(
    "ClientListMetricsResponseMetricsDimensionsTypeDef", {"Name": str, "Value": str}, total=False
)

ClientListMetricsResponseMetricsTypeDef = TypedDict(
    "ClientListMetricsResponseMetricsTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ClientListMetricsResponseMetricsDimensionsTypeDef],
    },
    total=False,
)

ClientListMetricsResponseTypeDef = TypedDict(
    "ClientListMetricsResponseTypeDef",
    {"Metrics": List[ClientListMetricsResponseMetricsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

_RequiredClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef = TypedDict(
    "_RequiredClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef",
    {"StartTime": datetime},
)
_OptionalClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef = TypedDict(
    "_OptionalClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef",
    {"EndTime": datetime},
    total=False,
)


class ClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef(
    _RequiredClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef,
    _OptionalClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef,
):
    pass


ClientPutAnomalyDetectorConfigurationTypeDef = TypedDict(
    "ClientPutAnomalyDetectorConfigurationTypeDef",
    {
        "ExcludedTimeRanges": List[ClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef],
        "MetricTimezone": str,
    },
    total=False,
)

_RequiredClientPutAnomalyDetectorDimensionsTypeDef = TypedDict(
    "_RequiredClientPutAnomalyDetectorDimensionsTypeDef", {"Name": str}
)
_OptionalClientPutAnomalyDetectorDimensionsTypeDef = TypedDict(
    "_OptionalClientPutAnomalyDetectorDimensionsTypeDef", {"Value": str}, total=False
)


class ClientPutAnomalyDetectorDimensionsTypeDef(
    _RequiredClientPutAnomalyDetectorDimensionsTypeDef,
    _OptionalClientPutAnomalyDetectorDimensionsTypeDef,
):
    pass


ClientPutDashboardResponseDashboardValidationMessagesTypeDef = TypedDict(
    "ClientPutDashboardResponseDashboardValidationMessagesTypeDef",
    {"DataPath": str, "Message": str},
    total=False,
)

ClientPutDashboardResponseTypeDef = TypedDict(
    "ClientPutDashboardResponseTypeDef",
    {
        "DashboardValidationMessages": List[
            ClientPutDashboardResponseDashboardValidationMessagesTypeDef
        ]
    },
    total=False,
)

_RequiredClientPutMetricAlarmDimensionsTypeDef = TypedDict(
    "_RequiredClientPutMetricAlarmDimensionsTypeDef", {"Name": str}
)
_OptionalClientPutMetricAlarmDimensionsTypeDef = TypedDict(
    "_OptionalClientPutMetricAlarmDimensionsTypeDef", {"Value": str}, total=False
)


class ClientPutMetricAlarmDimensionsTypeDef(
    _RequiredClientPutMetricAlarmDimensionsTypeDef, _OptionalClientPutMetricAlarmDimensionsTypeDef
):
    pass


ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientPutMetricAlarmMetricsMetricStatMetricTypeDef = TypedDict(
    "ClientPutMetricAlarmMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef],
    },
    total=False,
)

ClientPutMetricAlarmMetricsMetricStatTypeDef = TypedDict(
    "ClientPutMetricAlarmMetricsMetricStatTypeDef",
    {
        "Metric": ClientPutMetricAlarmMetricsMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": Literal[
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
        ],
    },
    total=False,
)

_RequiredClientPutMetricAlarmMetricsTypeDef = TypedDict(
    "_RequiredClientPutMetricAlarmMetricsTypeDef", {"Id": str}
)
_OptionalClientPutMetricAlarmMetricsTypeDef = TypedDict(
    "_OptionalClientPutMetricAlarmMetricsTypeDef",
    {
        "MetricStat": ClientPutMetricAlarmMetricsMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class ClientPutMetricAlarmMetricsTypeDef(
    _RequiredClientPutMetricAlarmMetricsTypeDef, _OptionalClientPutMetricAlarmMetricsTypeDef
):
    pass


_RequiredClientPutMetricAlarmTagsTypeDef = TypedDict(
    "_RequiredClientPutMetricAlarmTagsTypeDef", {"Key": str}
)
_OptionalClientPutMetricAlarmTagsTypeDef = TypedDict(
    "_OptionalClientPutMetricAlarmTagsTypeDef", {"Value": str}, total=False
)


class ClientPutMetricAlarmTagsTypeDef(
    _RequiredClientPutMetricAlarmTagsTypeDef, _OptionalClientPutMetricAlarmTagsTypeDef
):
    pass


ClientPutMetricDataMetricDataDimensionsTypeDef = TypedDict(
    "ClientPutMetricDataMetricDataDimensionsTypeDef", {"Name": str, "Value": str}, total=False
)

ClientPutMetricDataMetricDataStatisticValuesTypeDef = TypedDict(
    "ClientPutMetricDataMetricDataStatisticValuesTypeDef",
    {"SampleCount": float, "Sum": float, "Minimum": float, "Maximum": float},
    total=False,
)

_RequiredClientPutMetricDataMetricDataTypeDef = TypedDict(
    "_RequiredClientPutMetricDataMetricDataTypeDef", {"MetricName": str}
)
_OptionalClientPutMetricDataMetricDataTypeDef = TypedDict(
    "_OptionalClientPutMetricDataMetricDataTypeDef",
    {
        "Dimensions": List[ClientPutMetricDataMetricDataDimensionsTypeDef],
        "Timestamp": datetime,
        "Value": float,
        "StatisticValues": ClientPutMetricDataMetricDataStatisticValuesTypeDef,
        "Values": List[float],
        "Counts": List[float],
        "Unit": Literal[
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
        ],
        "StorageResolution": int,
    },
    total=False,
)


class ClientPutMetricDataMetricDataTypeDef(
    _RequiredClientPutMetricDataMetricDataTypeDef, _OptionalClientPutMetricDataMetricDataTypeDef
):
    pass


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


DescribeAlarmHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAlarmHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef = TypedDict(
    "DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef",
    {
        "AlarmName": str,
        "Timestamp": datetime,
        "HistoryItemType": Literal["ConfigurationUpdate", "StateUpdate", "Action"],
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)

DescribeAlarmHistoryPaginateResponseTypeDef = TypedDict(
    "DescribeAlarmHistoryPaginateResponseTypeDef",
    {"AlarmHistoryItems": List[DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef]},
    total=False,
)

DescribeAlarmsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAlarmsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef = TypedDict(
    "DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef = TypedDict(
    "DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)

DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef = TypedDict(
    "DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef",
    {
        "Metric": DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": Literal[
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
        ],
    },
    total=False,
)

DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef = TypedDict(
    "DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef",
    {
        "Id": str,
        "MetricStat": DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)

DescribeAlarmsPaginateResponseMetricAlarmsTypeDef = TypedDict(
    "DescribeAlarmsPaginateResponseMetricAlarmsTypeDef",
    {
        "AlarmName": str,
        "AlarmArn": str,
        "AlarmDescription": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "StateValue": Literal["OK", "ALARM", "INSUFFICIENT_DATA"],
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"],
        "ExtendedStatistic": str,
        "Dimensions": List[DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef],
        "Period": int,
        "Unit": Literal[
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
        ],
        "EvaluationPeriods": int,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanLowerOrGreaterThanUpperThreshold",
            "LessThanLowerThreshold",
            "GreaterThanUpperThreshold",
        ],
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List[DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef],
        "ThresholdMetricId": str,
    },
    total=False,
)

DescribeAlarmsPaginateResponseTypeDef = TypedDict(
    "DescribeAlarmsPaginateResponseTypeDef",
    {"MetricAlarms": List[DescribeAlarmsPaginateResponseMetricAlarmsTypeDef]},
    total=False,
)

GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef = TypedDict(
    "GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef = TypedDict(
    "GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef],
    },
    total=False,
)

GetMetricDataPaginateMetricDataQueriesMetricStatTypeDef = TypedDict(
    "GetMetricDataPaginateMetricDataQueriesMetricStatTypeDef",
    {
        "Metric": GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": Literal[
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
        ],
    },
    total=False,
)

_RequiredGetMetricDataPaginateMetricDataQueriesTypeDef = TypedDict(
    "_RequiredGetMetricDataPaginateMetricDataQueriesTypeDef", {"Id": str}
)
_OptionalGetMetricDataPaginateMetricDataQueriesTypeDef = TypedDict(
    "_OptionalGetMetricDataPaginateMetricDataQueriesTypeDef",
    {
        "MetricStat": GetMetricDataPaginateMetricDataQueriesMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class GetMetricDataPaginateMetricDataQueriesTypeDef(
    _RequiredGetMetricDataPaginateMetricDataQueriesTypeDef,
    _OptionalGetMetricDataPaginateMetricDataQueriesTypeDef,
):
    pass


GetMetricDataPaginatePaginationConfigTypeDef = TypedDict(
    "GetMetricDataPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetMetricDataPaginateResponseMessagesTypeDef = TypedDict(
    "GetMetricDataPaginateResponseMessagesTypeDef", {"Code": str, "Value": str}, total=False
)

GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef = TypedDict(
    "GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef",
    {"Code": str, "Value": str},
    total=False,
)

GetMetricDataPaginateResponseMetricDataResultsTypeDef = TypedDict(
    "GetMetricDataPaginateResponseMetricDataResultsTypeDef",
    {
        "Id": str,
        "Label": str,
        "Timestamps": List[datetime],
        "Values": List[float],
        "StatusCode": Literal["Complete", "InternalError", "PartialData"],
        "Messages": List[GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef],
    },
    total=False,
)

GetMetricDataPaginateResponseTypeDef = TypedDict(
    "GetMetricDataPaginateResponseTypeDef",
    {
        "MetricDataResults": List[GetMetricDataPaginateResponseMetricDataResultsTypeDef],
        "Messages": List[GetMetricDataPaginateResponseMessagesTypeDef],
    },
    total=False,
)

ListDashboardsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDashboardsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListDashboardsPaginateResponseDashboardEntriesTypeDef = TypedDict(
    "ListDashboardsPaginateResponseDashboardEntriesTypeDef",
    {"DashboardName": str, "DashboardArn": str, "LastModified": datetime, "Size": int},
    total=False,
)

ListDashboardsPaginateResponseTypeDef = TypedDict(
    "ListDashboardsPaginateResponseTypeDef",
    {"DashboardEntries": List[ListDashboardsPaginateResponseDashboardEntriesTypeDef]},
    total=False,
)

_RequiredListMetricsPaginateDimensionsTypeDef = TypedDict(
    "_RequiredListMetricsPaginateDimensionsTypeDef", {"Name": str}
)
_OptionalListMetricsPaginateDimensionsTypeDef = TypedDict(
    "_OptionalListMetricsPaginateDimensionsTypeDef", {"Value": str}, total=False
)


class ListMetricsPaginateDimensionsTypeDef(
    _RequiredListMetricsPaginateDimensionsTypeDef, _OptionalListMetricsPaginateDimensionsTypeDef
):
    pass


ListMetricsPaginatePaginationConfigTypeDef = TypedDict(
    "ListMetricsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListMetricsPaginateResponseMetricsDimensionsTypeDef = TypedDict(
    "ListMetricsPaginateResponseMetricsDimensionsTypeDef", {"Name": str, "Value": str}, total=False
)

ListMetricsPaginateResponseMetricsTypeDef = TypedDict(
    "ListMetricsPaginateResponseMetricsTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ListMetricsPaginateResponseMetricsDimensionsTypeDef],
    },
    total=False,
)

ListMetricsPaginateResponseTypeDef = TypedDict(
    "ListMetricsPaginateResponseTypeDef",
    {"Metrics": List[ListMetricsPaginateResponseMetricsTypeDef]},
    total=False,
)

_RequiredMetricGetStatisticsDimensionsTypeDef = TypedDict(
    "_RequiredMetricGetStatisticsDimensionsTypeDef", {"Name": str}
)
_OptionalMetricGetStatisticsDimensionsTypeDef = TypedDict(
    "_OptionalMetricGetStatisticsDimensionsTypeDef", {"Value": str}, total=False
)


class MetricGetStatisticsDimensionsTypeDef(
    _RequiredMetricGetStatisticsDimensionsTypeDef, _OptionalMetricGetStatisticsDimensionsTypeDef
):
    pass


MetricGetStatisticsResponseDatapointsTypeDef = TypedDict(
    "MetricGetStatisticsResponseDatapointsTypeDef",
    {
        "Timestamp": datetime,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
        "Unit": Literal[
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
        ],
        "ExtendedStatistics": Dict[str, float],
    },
    total=False,
)

MetricGetStatisticsResponseTypeDef = TypedDict(
    "MetricGetStatisticsResponseTypeDef",
    {"Label": str, "Datapoints": List[MetricGetStatisticsResponseDatapointsTypeDef]},
    total=False,
)

_RequiredMetricPutAlarmDimensionsTypeDef = TypedDict(
    "_RequiredMetricPutAlarmDimensionsTypeDef", {"Name": str}
)
_OptionalMetricPutAlarmDimensionsTypeDef = TypedDict(
    "_OptionalMetricPutAlarmDimensionsTypeDef", {"Value": str}, total=False
)


class MetricPutAlarmDimensionsTypeDef(
    _RequiredMetricPutAlarmDimensionsTypeDef, _OptionalMetricPutAlarmDimensionsTypeDef
):
    pass


MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

MetricPutAlarmMetricsMetricStatMetricTypeDef = TypedDict(
    "MetricPutAlarmMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef],
    },
    total=False,
)

MetricPutAlarmMetricsMetricStatTypeDef = TypedDict(
    "MetricPutAlarmMetricsMetricStatTypeDef",
    {
        "Metric": MetricPutAlarmMetricsMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": Literal[
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
        ],
    },
    total=False,
)

_RequiredMetricPutAlarmMetricsTypeDef = TypedDict(
    "_RequiredMetricPutAlarmMetricsTypeDef", {"Id": str}
)
_OptionalMetricPutAlarmMetricsTypeDef = TypedDict(
    "_OptionalMetricPutAlarmMetricsTypeDef",
    {
        "MetricStat": MetricPutAlarmMetricsMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class MetricPutAlarmMetricsTypeDef(
    _RequiredMetricPutAlarmMetricsTypeDef, _OptionalMetricPutAlarmMetricsTypeDef
):
    pass


_RequiredMetricPutAlarmTagsTypeDef = TypedDict("_RequiredMetricPutAlarmTagsTypeDef", {"Key": str})
_OptionalMetricPutAlarmTagsTypeDef = TypedDict(
    "_OptionalMetricPutAlarmTagsTypeDef", {"Value": str}, total=False
)


class MetricPutAlarmTagsTypeDef(
    _RequiredMetricPutAlarmTagsTypeDef, _OptionalMetricPutAlarmTagsTypeDef
):
    pass


_RequiredMetricsFilterDimensionsTypeDef = TypedDict(
    "_RequiredMetricsFilterDimensionsTypeDef", {"Name": str}
)
_OptionalMetricsFilterDimensionsTypeDef = TypedDict(
    "_OptionalMetricsFilterDimensionsTypeDef", {"Value": str}, total=False
)


class MetricsFilterDimensionsTypeDef(
    _RequiredMetricsFilterDimensionsTypeDef, _OptionalMetricsFilterDimensionsTypeDef
):
    pass
