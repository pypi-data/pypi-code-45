"Main interface for cloudwatch service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef",
    "AlarmDescribeHistoryResponseTypeDef",
    "AlarmExistsWaitWaiterConfigTypeDef",
    "AlarmsFilterDimensionsTypeDef",
    "ClientDeleteAnomalyDetectorDimensionsTypeDef",
    "ClientDeleteInsightRulesResponseFailuresTypeDef",
    "ClientDeleteInsightRulesResponseTypeDef",
    "ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef",
    "ClientDescribeAlarmHistoryResponseTypeDef",
    "ClientDescribeAlarmsForMetricDimensionsTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef",
    "ClientDescribeAlarmsForMetricResponseTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsTypeDef",
    "ClientDescribeAlarmsResponseTypeDef",
    "ClientDescribeAnomalyDetectorsDimensionsTypeDef",
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef",
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef",
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef",
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef",
    "ClientDescribeAnomalyDetectorsResponseTypeDef",
    "ClientDescribeInsightRulesResponseInsightRulesTypeDef",
    "ClientDescribeInsightRulesResponseTypeDef",
    "ClientDisableInsightRulesResponseFailuresTypeDef",
    "ClientDisableInsightRulesResponseTypeDef",
    "ClientEnableInsightRulesResponseFailuresTypeDef",
    "ClientEnableInsightRulesResponseTypeDef",
    "ClientGetDashboardResponseTypeDef",
    "ClientGetInsightRuleReportResponseContributorsDatapointsTypeDef",
    "ClientGetInsightRuleReportResponseContributorsTypeDef",
    "ClientGetInsightRuleReportResponseMetricDatapointsTypeDef",
    "ClientGetInsightRuleReportResponseTypeDef",
    "ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef",
    "ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef",
    "ClientGetMetricDataMetricDataQueriesMetricStatTypeDef",
    "ClientGetMetricDataMetricDataQueriesTypeDef",
    "ClientGetMetricDataResponseMessagesTypeDef",
    "ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef",
    "ClientGetMetricDataResponseMetricDataResultsTypeDef",
    "ClientGetMetricDataResponseTypeDef",
    "ClientGetMetricStatisticsDimensionsTypeDef",
    "ClientGetMetricStatisticsResponseDatapointsTypeDef",
    "ClientGetMetricStatisticsResponseTypeDef",
    "ClientGetMetricWidgetImageResponseTypeDef",
    "ClientListDashboardsResponseDashboardEntriesTypeDef",
    "ClientListDashboardsResponseTypeDef",
    "ClientListMetricsDimensionsTypeDef",
    "ClientListMetricsResponseMetricsDimensionsTypeDef",
    "ClientListMetricsResponseMetricsTypeDef",
    "ClientListMetricsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef",
    "ClientPutAnomalyDetectorConfigurationTypeDef",
    "ClientPutAnomalyDetectorDimensionsTypeDef",
    "ClientPutDashboardResponseDashboardValidationMessagesTypeDef",
    "ClientPutDashboardResponseTypeDef",
    "ClientPutMetricAlarmDimensionsTypeDef",
    "ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef",
    "ClientPutMetricAlarmMetricsMetricStatMetricTypeDef",
    "ClientPutMetricAlarmMetricsMetricStatTypeDef",
    "ClientPutMetricAlarmMetricsTypeDef",
    "ClientPutMetricAlarmTagsTypeDef",
    "ClientPutMetricDataMetricDataDimensionsTypeDef",
    "ClientPutMetricDataMetricDataStatisticValuesTypeDef",
    "ClientPutMetricDataMetricDataTypeDef",
    "ClientTagResourceTagsTypeDef",
    "DescribeAlarmHistoryPaginatePaginationConfigTypeDef",
    "DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef",
    "DescribeAlarmHistoryPaginateResponseTypeDef",
    "DescribeAlarmsPaginatePaginationConfigTypeDef",
    "DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef",
    "DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    "DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    "DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef",
    "DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef",
    "DescribeAlarmsPaginateResponseMetricAlarmsTypeDef",
    "DescribeAlarmsPaginateResponseTypeDef",
    "GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef",
    "GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef",
    "GetMetricDataPaginateMetricDataQueriesMetricStatTypeDef",
    "GetMetricDataPaginateMetricDataQueriesTypeDef",
    "GetMetricDataPaginatePaginationConfigTypeDef",
    "GetMetricDataPaginateResponseMessagesTypeDef",
    "GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef",
    "GetMetricDataPaginateResponseMetricDataResultsTypeDef",
    "GetMetricDataPaginateResponseTypeDef",
    "ListDashboardsPaginatePaginationConfigTypeDef",
    "ListDashboardsPaginateResponseDashboardEntriesTypeDef",
    "ListDashboardsPaginateResponseTypeDef",
    "ListMetricsPaginateDimensionsTypeDef",
    "ListMetricsPaginatePaginationConfigTypeDef",
    "ListMetricsPaginateResponseMetricsDimensionsTypeDef",
    "ListMetricsPaginateResponseMetricsTypeDef",
    "ListMetricsPaginateResponseTypeDef",
    "MetricGetStatisticsDimensionsTypeDef",
    "MetricGetStatisticsResponseDatapointsTypeDef",
    "MetricGetStatisticsResponseTypeDef",
    "MetricPutAlarmDimensionsTypeDef",
    "MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef",
    "MetricPutAlarmMetricsMetricStatMetricTypeDef",
    "MetricPutAlarmMetricsMetricStatTypeDef",
    "MetricPutAlarmMetricsTypeDef",
    "MetricPutAlarmTagsTypeDef",
    "MetricsFilterDimensionsTypeDef",
)


_AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef = TypedDict(
    "_AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef",
    {
        "AlarmName": str,
        "Timestamp": datetime,
        "HistoryItemType": Literal["ConfigurationUpdate", "StateUpdate", "Action"],
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)


class AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef(
    _AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef
):
    """
    - *(dict) --*

      Represents the history of a specific alarm.
      - **AlarmName** *(string) --*

        The descriptive name for the alarm.
    """


_AlarmDescribeHistoryResponseTypeDef = TypedDict(
    "_AlarmDescribeHistoryResponseTypeDef",
    {
        "AlarmHistoryItems": List[AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class AlarmDescribeHistoryResponseTypeDef(_AlarmDescribeHistoryResponseTypeDef):
    """
    - *(dict) --*

      - **AlarmHistoryItems** *(list) --*

        The alarm histories, in JSON format.
        - *(dict) --*

          Represents the history of a specific alarm.
          - **AlarmName** *(string) --*

            The descriptive name for the alarm.
    """


_AlarmExistsWaitWaiterConfigTypeDef = TypedDict(
    "_AlarmExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class AlarmExistsWaitWaiterConfigTypeDef(_AlarmExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5
    """


_RequiredAlarmsFilterDimensionsTypeDef = TypedDict(
    "_RequiredAlarmsFilterDimensionsTypeDef", {"Name": str}
)
_OptionalAlarmsFilterDimensionsTypeDef = TypedDict(
    "_OptionalAlarmsFilterDimensionsTypeDef", {"Value": str}, total=False
)


class AlarmsFilterDimensionsTypeDef(
    _RequiredAlarmsFilterDimensionsTypeDef, _OptionalAlarmsFilterDimensionsTypeDef
):
    """
    - *(dict) --*

      Expands the identity of a metric.
      - **Name** *(string) --***[REQUIRED]**

        The name of the dimension.
    """


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
    """
    - *(dict) --*

      Expands the identity of a metric.
      - **Name** *(string) --***[REQUIRED]**

        The name of the dimension.
    """


_ClientDeleteInsightRulesResponseFailuresTypeDef = TypedDict(
    "_ClientDeleteInsightRulesResponseFailuresTypeDef",
    {"FailureResource": str, "ExceptionType": str, "FailureCode": str, "FailureDescription": str},
    total=False,
)


class ClientDeleteInsightRulesResponseFailuresTypeDef(
    _ClientDeleteInsightRulesResponseFailuresTypeDef
):
    """
    - *(dict) --*

      This array is empty if the API operation was successful for all the rules specified in the
      request. If the operation could not process one of the rules, the following data is returned
      for each of those rules.
      - **FailureResource** *(string) --*

        The specified rule that could not be deleted.
    """


_ClientDeleteInsightRulesResponseTypeDef = TypedDict(
    "_ClientDeleteInsightRulesResponseTypeDef",
    {"Failures": List[ClientDeleteInsightRulesResponseFailuresTypeDef]},
    total=False,
)


class ClientDeleteInsightRulesResponseTypeDef(_ClientDeleteInsightRulesResponseTypeDef):
    """
    - *(dict) --*

      - **Failures** *(list) --*

        An array listing the rules that could not be deleted. You cannot delete built-in rules.
        - *(dict) --*

          This array is empty if the API operation was successful for all the rules specified in the
          request. If the operation could not process one of the rules, the following data is
          returned for each of those rules.
          - **FailureResource** *(string) --*

            The specified rule that could not be deleted.
    """


_ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef = TypedDict(
    "_ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef",
    {
        "AlarmName": str,
        "Timestamp": datetime,
        "HistoryItemType": Literal["ConfigurationUpdate", "StateUpdate", "Action"],
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)


class ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef(
    _ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef
):
    """
    - *(dict) --*

      Represents the history of a specific alarm.
      - **AlarmName** *(string) --*

        The descriptive name for the alarm.
    """


_ClientDescribeAlarmHistoryResponseTypeDef = TypedDict(
    "_ClientDescribeAlarmHistoryResponseTypeDef",
    {
        "AlarmHistoryItems": List[ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAlarmHistoryResponseTypeDef(_ClientDescribeAlarmHistoryResponseTypeDef):
    """
    - *(dict) --*

      - **AlarmHistoryItems** *(list) --*

        The alarm histories, in JSON format.
        - *(dict) --*

          Represents the history of a specific alarm.
          - **AlarmName** *(string) --*

            The descriptive name for the alarm.
    """


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
    """
    - *(dict) --*

      Expands the identity of a metric.
      - **Name** *(string) --***[REQUIRED]**

        The name of the dimension.
    """


_ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef(
    _ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef
):
    pass


_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef(
    _ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
):
    pass


_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef(
    _ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef
):
    pass


_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef",
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


class ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef(
    _ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef
):
    pass


_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef",
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


class ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef(
    _ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef
):
    pass


_ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef",
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


class ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef(
    _ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef
):
    """
    - *(dict) --*

      Represents an alarm.
      - **AlarmName** *(string) --*

        The name of the alarm.
    """


_ClientDescribeAlarmsForMetricResponseTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseTypeDef",
    {"MetricAlarms": List[ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef]},
    total=False,
)


class ClientDescribeAlarmsForMetricResponseTypeDef(_ClientDescribeAlarmsForMetricResponseTypeDef):
    """
    - *(dict) --*

      - **MetricAlarms** *(list) --*

        The information for each alarm with the specified metric.
        - *(dict) --*

          Represents an alarm.
          - **AlarmName** *(string) --*

            The name of the alarm.
    """


_ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef(
    _ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef
):
    pass


_ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef(
    _ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
):
    pass


_ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef(
    _ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef
):
    pass


_ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef",
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


class ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef(
    _ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef
):
    pass


_ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef",
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


class ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef(
    _ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef
):
    pass


_ClientDescribeAlarmsResponseMetricAlarmsTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseMetricAlarmsTypeDef",
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


class ClientDescribeAlarmsResponseMetricAlarmsTypeDef(
    _ClientDescribeAlarmsResponseMetricAlarmsTypeDef
):
    """
    - *(dict) --*

      Represents an alarm.
      - **AlarmName** *(string) --*

        The name of the alarm.
    """


_ClientDescribeAlarmsResponseTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseTypeDef",
    {"MetricAlarms": List[ClientDescribeAlarmsResponseMetricAlarmsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeAlarmsResponseTypeDef(_ClientDescribeAlarmsResponseTypeDef):
    """
    - *(dict) --*

      - **MetricAlarms** *(list) --*

        The information for the specified alarms.
        - *(dict) --*

          Represents an alarm.
          - **AlarmName** *(string) --*

            The name of the alarm.
    """


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
    """
    - *(dict) --*

      Expands the identity of a metric.
      - **Name** *(string) --***[REQUIRED]**

        The name of the dimension.
    """


_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef = TypedDict(
    "_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)


class ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef(
    _ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef
):
    pass


_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef = TypedDict(
    "_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef",
    {
        "ExcludedTimeRanges": List[
            ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef
        ],
        "MetricTimezone": str,
    },
    total=False,
)


class ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef(
    _ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef
):
    pass


_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef = TypedDict(
    "_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef(
    _ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef
):
    pass


_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef = TypedDict(
    "_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef],
        "Stat": str,
        "Configuration": ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef(
    _ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef
):
    """
    - *(dict) --*

      An anomaly detection model associated with a particular CloudWatch metric and statistic. You
      can use the model to display a band of expected normal values when the metric is graphed.
      - **Namespace** *(string) --*

        The namespace of the metric associated with the anomaly detection model.
    """


_ClientDescribeAnomalyDetectorsResponseTypeDef = TypedDict(
    "_ClientDescribeAnomalyDetectorsResponseTypeDef",
    {
        "AnomalyDetectors": List[ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAnomalyDetectorsResponseTypeDef(_ClientDescribeAnomalyDetectorsResponseTypeDef):
    """
    - *(dict) --*

      - **AnomalyDetectors** *(list) --*

        The list of anomaly detection models returned by the operation.
        - *(dict) --*

          An anomaly detection model associated with a particular CloudWatch metric and statistic.
          You can use the model to display a band of expected normal values when the metric is
          graphed.
          - **Namespace** *(string) --*

            The namespace of the metric associated with the anomaly detection model.
    """


_ClientDescribeInsightRulesResponseInsightRulesTypeDef = TypedDict(
    "_ClientDescribeInsightRulesResponseInsightRulesTypeDef",
    {"Name": str, "State": str, "Schema": str, "Definition": str},
    total=False,
)


class ClientDescribeInsightRulesResponseInsightRulesTypeDef(
    _ClientDescribeInsightRulesResponseInsightRulesTypeDef
):
    pass


_ClientDescribeInsightRulesResponseTypeDef = TypedDict(
    "_ClientDescribeInsightRulesResponseTypeDef",
    {"NextToken": str, "InsightRules": List[ClientDescribeInsightRulesResponseInsightRulesTypeDef]},
    total=False,
)


class ClientDescribeInsightRulesResponseTypeDef(_ClientDescribeInsightRulesResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        Reserved for future use.
    """


_ClientDisableInsightRulesResponseFailuresTypeDef = TypedDict(
    "_ClientDisableInsightRulesResponseFailuresTypeDef",
    {"FailureResource": str, "ExceptionType": str, "FailureCode": str, "FailureDescription": str},
    total=False,
)


class ClientDisableInsightRulesResponseFailuresTypeDef(
    _ClientDisableInsightRulesResponseFailuresTypeDef
):
    """
    - *(dict) --*

      This array is empty if the API operation was successful for all the rules specified in the
      request. If the operation could not process one of the rules, the following data is returned
      for each of those rules.
      - **FailureResource** *(string) --*

        The specified rule that could not be deleted.
    """


_ClientDisableInsightRulesResponseTypeDef = TypedDict(
    "_ClientDisableInsightRulesResponseTypeDef",
    {"Failures": List[ClientDisableInsightRulesResponseFailuresTypeDef]},
    total=False,
)


class ClientDisableInsightRulesResponseTypeDef(_ClientDisableInsightRulesResponseTypeDef):
    """
    - *(dict) --*

      - **Failures** *(list) --*

        An array listing the rules that could not be disabled. You cannot disable built-in rules.
        - *(dict) --*

          This array is empty if the API operation was successful for all the rules specified in the
          request. If the operation could not process one of the rules, the following data is
          returned for each of those rules.
          - **FailureResource** *(string) --*

            The specified rule that could not be deleted.
    """


_ClientEnableInsightRulesResponseFailuresTypeDef = TypedDict(
    "_ClientEnableInsightRulesResponseFailuresTypeDef",
    {"FailureResource": str, "ExceptionType": str, "FailureCode": str, "FailureDescription": str},
    total=False,
)


class ClientEnableInsightRulesResponseFailuresTypeDef(
    _ClientEnableInsightRulesResponseFailuresTypeDef
):
    """
    - *(dict) --*

      This array is empty if the API operation was successful for all the rules specified in the
      request. If the operation could not process one of the rules, the following data is returned
      for each of those rules.
      - **FailureResource** *(string) --*

        The specified rule that could not be deleted.
    """


_ClientEnableInsightRulesResponseTypeDef = TypedDict(
    "_ClientEnableInsightRulesResponseTypeDef",
    {"Failures": List[ClientEnableInsightRulesResponseFailuresTypeDef]},
    total=False,
)


class ClientEnableInsightRulesResponseTypeDef(_ClientEnableInsightRulesResponseTypeDef):
    """
    - *(dict) --*

      - **Failures** *(list) --*

        An array listing the rules that could not be enabled. You cannot disable or enable built-in
        rules.
        - *(dict) --*

          This array is empty if the API operation was successful for all the rules specified in the
          request. If the operation could not process one of the rules, the following data is
          returned for each of those rules.
          - **FailureResource** *(string) --*

            The specified rule that could not be deleted.
    """


_ClientGetDashboardResponseTypeDef = TypedDict(
    "_ClientGetDashboardResponseTypeDef",
    {"DashboardArn": str, "DashboardBody": str, "DashboardName": str},
    total=False,
)


class ClientGetDashboardResponseTypeDef(_ClientGetDashboardResponseTypeDef):
    """
    - *(dict) --*

      - **DashboardArn** *(string) --*

        The Amazon Resource Name (ARN) of the dashboard.
    """


_ClientGetInsightRuleReportResponseContributorsDatapointsTypeDef = TypedDict(
    "_ClientGetInsightRuleReportResponseContributorsDatapointsTypeDef",
    {"Timestamp": datetime, "ApproximateValue": float},
    total=False,
)


class ClientGetInsightRuleReportResponseContributorsDatapointsTypeDef(
    _ClientGetInsightRuleReportResponseContributorsDatapointsTypeDef
):
    pass


_ClientGetInsightRuleReportResponseContributorsTypeDef = TypedDict(
    "_ClientGetInsightRuleReportResponseContributorsTypeDef",
    {
        "Keys": List[str],
        "ApproximateAggregateValue": float,
        "Datapoints": List[ClientGetInsightRuleReportResponseContributorsDatapointsTypeDef],
    },
    total=False,
)


class ClientGetInsightRuleReportResponseContributorsTypeDef(
    _ClientGetInsightRuleReportResponseContributorsTypeDef
):
    pass


_ClientGetInsightRuleReportResponseMetricDatapointsTypeDef = TypedDict(
    "_ClientGetInsightRuleReportResponseMetricDatapointsTypeDef",
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


class ClientGetInsightRuleReportResponseMetricDatapointsTypeDef(
    _ClientGetInsightRuleReportResponseMetricDatapointsTypeDef
):
    pass


_ClientGetInsightRuleReportResponseTypeDef = TypedDict(
    "_ClientGetInsightRuleReportResponseTypeDef",
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


class ClientGetInsightRuleReportResponseTypeDef(_ClientGetInsightRuleReportResponseTypeDef):
    """
    - *(dict) --*

      - **KeyLabels** *(list) --*

        An array of the strings used as the keys for this rule. The keys are the dimensions used to
        classify contributors. If the rule contains more than one key, then each unique combination
        of values for the keys is counted as a unique contributor.
        - *(string) --*
    """


_ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef = TypedDict(
    "_ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef(
    _ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef
):
    pass


_ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef = TypedDict(
    "_ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef],
    },
    total=False,
)


class ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef(
    _ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef
):
    pass


_ClientGetMetricDataMetricDataQueriesMetricStatTypeDef = TypedDict(
    "_ClientGetMetricDataMetricDataQueriesMetricStatTypeDef",
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


class ClientGetMetricDataMetricDataQueriesMetricStatTypeDef(
    _ClientGetMetricDataMetricDataQueriesMetricStatTypeDef
):
    pass


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
    """
    - *(dict) --*

      This structure is used in both ``GetMetricData`` and ``PutMetricAlarm`` . The supported use of
      this structure is different for those two operations.
      When used in ``GetMetricData`` , it indicates the metric data to return, and whether this call
      is just retrieving a batch set of data for one metric, or is performing a math expression on
      metric data. A single ``GetMetricData`` call can include up to 100 ``MetricDataQuery``
      structures.
      When used in ``PutMetricAlarm`` , it enables you to create an alarm based on a metric math
      expression. Each ``MetricDataQuery`` in the array specifies either a metric to retrieve, or a
      math expression to be performed on retrieved metrics. A single ``PutMetricAlarm`` call can
      include up to 20 ``MetricDataQuery`` structures in the array. The 20 structures can include as
      many as 10 structures that contain a ``MetricStat`` parameter to retrieve a metric, and as
      many as 10 structures that contain the ``Expression`` parameter to perform a math expression.
      Of those ``Expression`` structures, one must have ``True`` as the value for ``ReturnData`` .
      The result of this expression is the value the alarm watches.
      Any expression used in a ``PutMetricAlarm`` operation must return a single time series. For
      more information, see `Metric Math Syntax and Functions
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
      in the *Amazon CloudWatch User Guide* .
      Some of the parameters of this structure also have different uses whether you are using this
      structure in a ``GetMetricData`` operation or a ``PutMetricAlarm`` operation. These
      differences are explained in the following parameter list.
      - **Id** *(string) --***[REQUIRED]**

        A short name used to tie this object to the results in the response. This name must be
        unique within a single call to ``GetMetricData`` . If you are performing math expressions on
        this set of data, this name represents that data and can serve as a variable in the
        mathematical expression. The valid characters are letters, numbers, and underscore. The
        first character must be a lowercase letter.
    """


_ClientGetMetricDataResponseMessagesTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMessagesTypeDef", {"Code": str, "Value": str}, total=False
)


class ClientGetMetricDataResponseMessagesTypeDef(_ClientGetMetricDataResponseMessagesTypeDef):
    pass


_ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef",
    {"Code": str, "Value": str},
    total=False,
)


class ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef(
    _ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef
):
    pass


_ClientGetMetricDataResponseMetricDataResultsTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricDataResultsTypeDef",
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


class ClientGetMetricDataResponseMetricDataResultsTypeDef(
    _ClientGetMetricDataResponseMetricDataResultsTypeDef
):
    """
    - *(dict) --*

      A ``GetMetricData`` call returns an array of ``MetricDataResult`` structures. Each of these
      structures includes the data points for that metric, along with the timestamps of those data
      points and other identifying information.
      - **Id** *(string) --*

        The short name you specified to represent this metric.
    """


_ClientGetMetricDataResponseTypeDef = TypedDict(
    "_ClientGetMetricDataResponseTypeDef",
    {
        "MetricDataResults": List[ClientGetMetricDataResponseMetricDataResultsTypeDef],
        "NextToken": str,
        "Messages": List[ClientGetMetricDataResponseMessagesTypeDef],
    },
    total=False,
)


class ClientGetMetricDataResponseTypeDef(_ClientGetMetricDataResponseTypeDef):
    """
    - *(dict) --*

      - **MetricDataResults** *(list) --*

        The metrics that are returned, including the metric name, namespace, and dimensions.
        - *(dict) --*

          A ``GetMetricData`` call returns an array of ``MetricDataResult`` structures. Each of
          these structures includes the data points for that metric, along with the timestamps of
          those data points and other identifying information.
          - **Id** *(string) --*

            The short name you specified to represent this metric.
    """


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
    """
    - *(dict) --*

      Expands the identity of a metric.
      - **Name** *(string) --***[REQUIRED]**

        The name of the dimension.
    """


_ClientGetMetricStatisticsResponseDatapointsTypeDef = TypedDict(
    "_ClientGetMetricStatisticsResponseDatapointsTypeDef",
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


class ClientGetMetricStatisticsResponseDatapointsTypeDef(
    _ClientGetMetricStatisticsResponseDatapointsTypeDef
):
    pass


_ClientGetMetricStatisticsResponseTypeDef = TypedDict(
    "_ClientGetMetricStatisticsResponseTypeDef",
    {"Label": str, "Datapoints": List[ClientGetMetricStatisticsResponseDatapointsTypeDef]},
    total=False,
)


class ClientGetMetricStatisticsResponseTypeDef(_ClientGetMetricStatisticsResponseTypeDef):
    """
    - *(dict) --*

      - **Label** *(string) --*

        A label for the specified metric.
    """


_ClientGetMetricWidgetImageResponseTypeDef = TypedDict(
    "_ClientGetMetricWidgetImageResponseTypeDef", {"MetricWidgetImage": bytes}, total=False
)


class ClientGetMetricWidgetImageResponseTypeDef(_ClientGetMetricWidgetImageResponseTypeDef):
    """
    - *(dict) --*

      - **MetricWidgetImage** *(bytes) --*

        The image of the graph, in the output format specified.
    """


_ClientListDashboardsResponseDashboardEntriesTypeDef = TypedDict(
    "_ClientListDashboardsResponseDashboardEntriesTypeDef",
    {"DashboardName": str, "DashboardArn": str, "LastModified": datetime, "Size": int},
    total=False,
)


class ClientListDashboardsResponseDashboardEntriesTypeDef(
    _ClientListDashboardsResponseDashboardEntriesTypeDef
):
    """
    - *(dict) --*

      Represents a specific dashboard.
      - **DashboardName** *(string) --*

        The name of the dashboard.
    """


_ClientListDashboardsResponseTypeDef = TypedDict(
    "_ClientListDashboardsResponseTypeDef",
    {
        "DashboardEntries": List[ClientListDashboardsResponseDashboardEntriesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListDashboardsResponseTypeDef(_ClientListDashboardsResponseTypeDef):
    """
    - *(dict) --*

      - **DashboardEntries** *(list) --*

        The list of matching dashboards.
        - *(dict) --*

          Represents a specific dashboard.
          - **DashboardName** *(string) --*

            The name of the dashboard.
    """


_RequiredClientListMetricsDimensionsTypeDef = TypedDict(
    "_RequiredClientListMetricsDimensionsTypeDef", {"Name": str}
)
_OptionalClientListMetricsDimensionsTypeDef = TypedDict(
    "_OptionalClientListMetricsDimensionsTypeDef", {"Value": str}, total=False
)


class ClientListMetricsDimensionsTypeDef(
    _RequiredClientListMetricsDimensionsTypeDef, _OptionalClientListMetricsDimensionsTypeDef
):
    """
    - *(dict) --*

      Represents filters for a dimension.
      - **Name** *(string) --***[REQUIRED]**

        The dimension name to be matched.
    """


_ClientListMetricsResponseMetricsDimensionsTypeDef = TypedDict(
    "_ClientListMetricsResponseMetricsDimensionsTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientListMetricsResponseMetricsDimensionsTypeDef(
    _ClientListMetricsResponseMetricsDimensionsTypeDef
):
    pass


_ClientListMetricsResponseMetricsTypeDef = TypedDict(
    "_ClientListMetricsResponseMetricsTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ClientListMetricsResponseMetricsDimensionsTypeDef],
    },
    total=False,
)


class ClientListMetricsResponseMetricsTypeDef(_ClientListMetricsResponseMetricsTypeDef):
    """
    - *(dict) --*

      Represents a specific metric.
      - **Namespace** *(string) --*

        The namespace of the metric.
    """


_ClientListMetricsResponseTypeDef = TypedDict(
    "_ClientListMetricsResponseTypeDef",
    {"Metrics": List[ClientListMetricsResponseMetricsTypeDef], "NextToken": str},
    total=False,
)


class ClientListMetricsResponseTypeDef(_ClientListMetricsResponseTypeDef):
    """
    - *(dict) --*

      - **Metrics** *(list) --*

        The metrics.
        - *(dict) --*

          Represents a specific metric.
          - **Namespace** *(string) --*

            The namespace of the metric.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      A key-value pair associated with a CloudWatch resource.
      - **Key** *(string) --*

        A string that you can use to assign a value. The combination of tag keys and values can help
        you organize and categorize your resources.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The list of tag keys and values associated with the resource you specified.
        - *(dict) --*

          A key-value pair associated with a CloudWatch resource.
          - **Key** *(string) --*

            A string that you can use to assign a value. The combination of tag keys and values can
            help you organize and categorize your resources.
    """


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
    """
    - *(dict) --*

      Specifies one range of days or times to exclude from use for training an anomaly detection
      model.
      - **StartTime** *(datetime) --***[REQUIRED]**

        The start time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For
        example, ``2019-07-01T23:59:59`` .
    """


_ClientPutAnomalyDetectorConfigurationTypeDef = TypedDict(
    "_ClientPutAnomalyDetectorConfigurationTypeDef",
    {
        "ExcludedTimeRanges": List[ClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef],
        "MetricTimezone": str,
    },
    total=False,
)


class ClientPutAnomalyDetectorConfigurationTypeDef(_ClientPutAnomalyDetectorConfigurationTypeDef):
    """
    The configuration specifies details about how the anomaly detection model is to be trained,
    including time ranges to exclude when training and updating the model. You can specify as many
    as 10 time ranges.
    The configuration can also include the time zone to use for the metric.
    You can in
    - **ExcludedTimeRanges** *(list) --*

      An array of time ranges to exclude from use when the anomaly detection model is trained. Use
      this to make sure that events that could cause unusual values for the metric, such as
      deployments, aren't used when CloudWatch creates the model.
      - *(dict) --*

        Specifies one range of days or times to exclude from use for training an anomaly detection
        model.
        - **StartTime** *(datetime) --***[REQUIRED]**

          The start time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For
          example, ``2019-07-01T23:59:59`` .
    """


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
    """
    - *(dict) --*

      Expands the identity of a metric.
      - **Name** *(string) --***[REQUIRED]**

        The name of the dimension.
    """


_ClientPutDashboardResponseDashboardValidationMessagesTypeDef = TypedDict(
    "_ClientPutDashboardResponseDashboardValidationMessagesTypeDef",
    {"DataPath": str, "Message": str},
    total=False,
)


class ClientPutDashboardResponseDashboardValidationMessagesTypeDef(
    _ClientPutDashboardResponseDashboardValidationMessagesTypeDef
):
    """
    - *(dict) --*

      An error or warning for the operation.
      - **DataPath** *(string) --*

        The data path related to the message.
    """


_ClientPutDashboardResponseTypeDef = TypedDict(
    "_ClientPutDashboardResponseTypeDef",
    {
        "DashboardValidationMessages": List[
            ClientPutDashboardResponseDashboardValidationMessagesTypeDef
        ]
    },
    total=False,
)


class ClientPutDashboardResponseTypeDef(_ClientPutDashboardResponseTypeDef):
    """
    - *(dict) --*

      - **DashboardValidationMessages** *(list) --*

        If the input for ``PutDashboard`` was correct and the dashboard was successfully created or
        modified, this result is empty.
        If this result includes only warning messages, then the input was valid enough for the
        dashboard to be created or modified, but some elements of the dashboard may not render.
        If this result includes error messages, the input was not valid and the operation failed.
        - *(dict) --*

          An error or warning for the operation.
          - **DataPath** *(string) --*

            The data path related to the message.
    """


_RequiredClientPutMetricAlarmDimensionsTypeDef = TypedDict(
    "_RequiredClientPutMetricAlarmDimensionsTypeDef", {"Name": str}
)
_OptionalClientPutMetricAlarmDimensionsTypeDef = TypedDict(
    "_OptionalClientPutMetricAlarmDimensionsTypeDef", {"Value": str}, total=False
)


class ClientPutMetricAlarmDimensionsTypeDef(
    _RequiredClientPutMetricAlarmDimensionsTypeDef, _OptionalClientPutMetricAlarmDimensionsTypeDef
):
    """
    - *(dict) --*

      Expands the identity of a metric.
      - **Name** *(string) --***[REQUIRED]**

        The name of the dimension.
    """


_ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "_ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef(
    _ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef
):
    pass


_ClientPutMetricAlarmMetricsMetricStatMetricTypeDef = TypedDict(
    "_ClientPutMetricAlarmMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef],
    },
    total=False,
)


class ClientPutMetricAlarmMetricsMetricStatMetricTypeDef(
    _ClientPutMetricAlarmMetricsMetricStatMetricTypeDef
):
    pass


_ClientPutMetricAlarmMetricsMetricStatTypeDef = TypedDict(
    "_ClientPutMetricAlarmMetricsMetricStatTypeDef",
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


class ClientPutMetricAlarmMetricsMetricStatTypeDef(_ClientPutMetricAlarmMetricsMetricStatTypeDef):
    pass


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
    """
    - *(dict) --*

      This structure is used in both ``GetMetricData`` and ``PutMetricAlarm`` . The supported use of
      this structure is different for those two operations.
      When used in ``GetMetricData`` , it indicates the metric data to return, and whether this call
      is just retrieving a batch set of data for one metric, or is performing a math expression on
      metric data. A single ``GetMetricData`` call can include up to 100 ``MetricDataQuery``
      structures.
      When used in ``PutMetricAlarm`` , it enables you to create an alarm based on a metric math
      expression. Each ``MetricDataQuery`` in the array specifies either a metric to retrieve, or a
      math expression to be performed on retrieved metrics. A single ``PutMetricAlarm`` call can
      include up to 20 ``MetricDataQuery`` structures in the array. The 20 structures can include as
      many as 10 structures that contain a ``MetricStat`` parameter to retrieve a metric, and as
      many as 10 structures that contain the ``Expression`` parameter to perform a math expression.
      Of those ``Expression`` structures, one must have ``True`` as the value for ``ReturnData`` .
      The result of this expression is the value the alarm watches.
      Any expression used in a ``PutMetricAlarm`` operation must return a single time series. For
      more information, see `Metric Math Syntax and Functions
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
      in the *Amazon CloudWatch User Guide* .
      Some of the parameters of this structure also have different uses whether you are using this
      structure in a ``GetMetricData`` operation or a ``PutMetricAlarm`` operation. These
      differences are explained in the following parameter list.
      - **Id** *(string) --***[REQUIRED]**

        A short name used to tie this object to the results in the response. This name must be
        unique within a single call to ``GetMetricData`` . If you are performing math expressions on
        this set of data, this name represents that data and can serve as a variable in the
        mathematical expression. The valid characters are letters, numbers, and underscore. The
        first character must be a lowercase letter.
    """


_RequiredClientPutMetricAlarmTagsTypeDef = TypedDict(
    "_RequiredClientPutMetricAlarmTagsTypeDef", {"Key": str}
)
_OptionalClientPutMetricAlarmTagsTypeDef = TypedDict(
    "_OptionalClientPutMetricAlarmTagsTypeDef", {"Value": str}, total=False
)


class ClientPutMetricAlarmTagsTypeDef(
    _RequiredClientPutMetricAlarmTagsTypeDef, _OptionalClientPutMetricAlarmTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair associated with a CloudWatch resource.
      - **Key** *(string) --***[REQUIRED]**

        A string that you can use to assign a value. The combination of tag keys and values can help
        you organize and categorize your resources.
    """


_ClientPutMetricDataMetricDataDimensionsTypeDef = TypedDict(
    "_ClientPutMetricDataMetricDataDimensionsTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientPutMetricDataMetricDataDimensionsTypeDef(
    _ClientPutMetricDataMetricDataDimensionsTypeDef
):
    pass


_ClientPutMetricDataMetricDataStatisticValuesTypeDef = TypedDict(
    "_ClientPutMetricDataMetricDataStatisticValuesTypeDef",
    {"SampleCount": float, "Sum": float, "Minimum": float, "Maximum": float},
    total=False,
)


class ClientPutMetricDataMetricDataStatisticValuesTypeDef(
    _ClientPutMetricDataMetricDataStatisticValuesTypeDef
):
    pass


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
    """
    - *(dict) --*

      Encapsulates the information sent to either create a metric or add new values to be aggregated
      into an existing metric.
      - **MetricName** *(string) --***[REQUIRED]**

        The name of the metric.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair associated with a CloudWatch resource.
      - **Key** *(string) --***[REQUIRED]**

        A string that you can use to assign a value. The combination of tag keys and values can help
        you organize and categorize your resources.
    """


_DescribeAlarmHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAlarmHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAlarmHistoryPaginatePaginationConfigTypeDef(
    _DescribeAlarmHistoryPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef = TypedDict(
    "_DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef",
    {
        "AlarmName": str,
        "Timestamp": datetime,
        "HistoryItemType": Literal["ConfigurationUpdate", "StateUpdate", "Action"],
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)


class DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef(
    _DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef
):
    """
    - *(dict) --*

      Represents the history of a specific alarm.
      - **AlarmName** *(string) --*

        The descriptive name for the alarm.
    """


_DescribeAlarmHistoryPaginateResponseTypeDef = TypedDict(
    "_DescribeAlarmHistoryPaginateResponseTypeDef",
    {"AlarmHistoryItems": List[DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef]},
    total=False,
)


class DescribeAlarmHistoryPaginateResponseTypeDef(_DescribeAlarmHistoryPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **AlarmHistoryItems** *(list) --*

        The alarm histories, in JSON format.
        - *(dict) --*

          Represents the history of a specific alarm.
          - **AlarmName** *(string) --*

            The descriptive name for the alarm.
    """


_DescribeAlarmsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAlarmsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAlarmsPaginatePaginationConfigTypeDef(_DescribeAlarmsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef(
    _DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef
):
    pass


_DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef(
    _DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
):
    pass


_DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)


class DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef(
    _DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef
):
    pass


_DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef",
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


class DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef(
    _DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef
):
    pass


_DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef",
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


class DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef(
    _DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef
):
    pass


_DescribeAlarmsPaginateResponseMetricAlarmsTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseMetricAlarmsTypeDef",
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


class DescribeAlarmsPaginateResponseMetricAlarmsTypeDef(
    _DescribeAlarmsPaginateResponseMetricAlarmsTypeDef
):
    """
    - *(dict) --*

      Represents an alarm.
      - **AlarmName** *(string) --*

        The name of the alarm.
    """


_DescribeAlarmsPaginateResponseTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseTypeDef",
    {"MetricAlarms": List[DescribeAlarmsPaginateResponseMetricAlarmsTypeDef]},
    total=False,
)


class DescribeAlarmsPaginateResponseTypeDef(_DescribeAlarmsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **MetricAlarms** *(list) --*

        The information for the specified alarms.
        - *(dict) --*

          Represents an alarm.
          - **AlarmName** *(string) --*

            The name of the alarm.
    """


_GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef = TypedDict(
    "_GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef(
    _GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef
):
    pass


_GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef = TypedDict(
    "_GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef],
    },
    total=False,
)


class GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef(
    _GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef
):
    pass


_GetMetricDataPaginateMetricDataQueriesMetricStatTypeDef = TypedDict(
    "_GetMetricDataPaginateMetricDataQueriesMetricStatTypeDef",
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


class GetMetricDataPaginateMetricDataQueriesMetricStatTypeDef(
    _GetMetricDataPaginateMetricDataQueriesMetricStatTypeDef
):
    pass


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
    """
    - *(dict) --*

      This structure is used in both ``GetMetricData`` and ``PutMetricAlarm`` . The supported use of
      this structure is different for those two operations.
      When used in ``GetMetricData`` , it indicates the metric data to return, and whether this call
      is just retrieving a batch set of data for one metric, or is performing a math expression on
      metric data. A single ``GetMetricData`` call can include up to 100 ``MetricDataQuery``
      structures.
      When used in ``PutMetricAlarm`` , it enables you to create an alarm based on a metric math
      expression. Each ``MetricDataQuery`` in the array specifies either a metric to retrieve, or a
      math expression to be performed on retrieved metrics. A single ``PutMetricAlarm`` call can
      include up to 20 ``MetricDataQuery`` structures in the array. The 20 structures can include as
      many as 10 structures that contain a ``MetricStat`` parameter to retrieve a metric, and as
      many as 10 structures that contain the ``Expression`` parameter to perform a math expression.
      Of those ``Expression`` structures, one must have ``True`` as the value for ``ReturnData`` .
      The result of this expression is the value the alarm watches.
      Any expression used in a ``PutMetricAlarm`` operation must return a single time series. For
      more information, see `Metric Math Syntax and Functions
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
      in the *Amazon CloudWatch User Guide* .
      Some of the parameters of this structure also have different uses whether you are using this
      structure in a ``GetMetricData`` operation or a ``PutMetricAlarm`` operation. These
      differences are explained in the following parameter list.
      - **Id** *(string) --***[REQUIRED]**

        A short name used to tie this object to the results in the response. This name must be
        unique within a single call to ``GetMetricData`` . If you are performing math expressions on
        this set of data, this name represents that data and can serve as a variable in the
        mathematical expression. The valid characters are letters, numbers, and underscore. The
        first character must be a lowercase letter.
    """


_GetMetricDataPaginatePaginationConfigTypeDef = TypedDict(
    "_GetMetricDataPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetMetricDataPaginatePaginationConfigTypeDef(_GetMetricDataPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetMetricDataPaginateResponseMessagesTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMessagesTypeDef", {"Code": str, "Value": str}, total=False
)


class GetMetricDataPaginateResponseMessagesTypeDef(_GetMetricDataPaginateResponseMessagesTypeDef):
    pass


_GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef",
    {"Code": str, "Value": str},
    total=False,
)


class GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef(
    _GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef
):
    pass


_GetMetricDataPaginateResponseMetricDataResultsTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricDataResultsTypeDef",
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


class GetMetricDataPaginateResponseMetricDataResultsTypeDef(
    _GetMetricDataPaginateResponseMetricDataResultsTypeDef
):
    """
    - *(dict) --*

      A ``GetMetricData`` call returns an array of ``MetricDataResult`` structures. Each of these
      structures includes the data points for that metric, along with the timestamps of those data
      points and other identifying information.
      - **Id** *(string) --*

        The short name you specified to represent this metric.
    """


_GetMetricDataPaginateResponseTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseTypeDef",
    {
        "MetricDataResults": List[GetMetricDataPaginateResponseMetricDataResultsTypeDef],
        "Messages": List[GetMetricDataPaginateResponseMessagesTypeDef],
    },
    total=False,
)


class GetMetricDataPaginateResponseTypeDef(_GetMetricDataPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **MetricDataResults** *(list) --*

        The metrics that are returned, including the metric name, namespace, and dimensions.
        - *(dict) --*

          A ``GetMetricData`` call returns an array of ``MetricDataResult`` structures. Each of
          these structures includes the data points for that metric, along with the timestamps of
          those data points and other identifying information.
          - **Id** *(string) --*

            The short name you specified to represent this metric.
    """


_ListDashboardsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDashboardsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDashboardsPaginatePaginationConfigTypeDef(_ListDashboardsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDashboardsPaginateResponseDashboardEntriesTypeDef = TypedDict(
    "_ListDashboardsPaginateResponseDashboardEntriesTypeDef",
    {"DashboardName": str, "DashboardArn": str, "LastModified": datetime, "Size": int},
    total=False,
)


class ListDashboardsPaginateResponseDashboardEntriesTypeDef(
    _ListDashboardsPaginateResponseDashboardEntriesTypeDef
):
    """
    - *(dict) --*

      Represents a specific dashboard.
      - **DashboardName** *(string) --*

        The name of the dashboard.
    """


_ListDashboardsPaginateResponseTypeDef = TypedDict(
    "_ListDashboardsPaginateResponseTypeDef",
    {"DashboardEntries": List[ListDashboardsPaginateResponseDashboardEntriesTypeDef]},
    total=False,
)


class ListDashboardsPaginateResponseTypeDef(_ListDashboardsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **DashboardEntries** *(list) --*

        The list of matching dashboards.
        - *(dict) --*

          Represents a specific dashboard.
          - **DashboardName** *(string) --*

            The name of the dashboard.
    """


_RequiredListMetricsPaginateDimensionsTypeDef = TypedDict(
    "_RequiredListMetricsPaginateDimensionsTypeDef", {"Name": str}
)
_OptionalListMetricsPaginateDimensionsTypeDef = TypedDict(
    "_OptionalListMetricsPaginateDimensionsTypeDef", {"Value": str}, total=False
)


class ListMetricsPaginateDimensionsTypeDef(
    _RequiredListMetricsPaginateDimensionsTypeDef, _OptionalListMetricsPaginateDimensionsTypeDef
):
    """
    - *(dict) --*

      Represents filters for a dimension.
      - **Name** *(string) --***[REQUIRED]**

        The dimension name to be matched.
    """


_ListMetricsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMetricsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListMetricsPaginatePaginationConfigTypeDef(_ListMetricsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListMetricsPaginateResponseMetricsDimensionsTypeDef = TypedDict(
    "_ListMetricsPaginateResponseMetricsDimensionsTypeDef", {"Name": str, "Value": str}, total=False
)


class ListMetricsPaginateResponseMetricsDimensionsTypeDef(
    _ListMetricsPaginateResponseMetricsDimensionsTypeDef
):
    pass


_ListMetricsPaginateResponseMetricsTypeDef = TypedDict(
    "_ListMetricsPaginateResponseMetricsTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ListMetricsPaginateResponseMetricsDimensionsTypeDef],
    },
    total=False,
)


class ListMetricsPaginateResponseMetricsTypeDef(_ListMetricsPaginateResponseMetricsTypeDef):
    """
    - *(dict) --*

      Represents a specific metric.
      - **Namespace** *(string) --*

        The namespace of the metric.
    """


_ListMetricsPaginateResponseTypeDef = TypedDict(
    "_ListMetricsPaginateResponseTypeDef",
    {"Metrics": List[ListMetricsPaginateResponseMetricsTypeDef]},
    total=False,
)


class ListMetricsPaginateResponseTypeDef(_ListMetricsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Metrics** *(list) --*

        The metrics.
        - *(dict) --*

          Represents a specific metric.
          - **Namespace** *(string) --*

            The namespace of the metric.
    """


_RequiredMetricGetStatisticsDimensionsTypeDef = TypedDict(
    "_RequiredMetricGetStatisticsDimensionsTypeDef", {"Name": str}
)
_OptionalMetricGetStatisticsDimensionsTypeDef = TypedDict(
    "_OptionalMetricGetStatisticsDimensionsTypeDef", {"Value": str}, total=False
)


class MetricGetStatisticsDimensionsTypeDef(
    _RequiredMetricGetStatisticsDimensionsTypeDef, _OptionalMetricGetStatisticsDimensionsTypeDef
):
    """
    - *(dict) --*

      Expands the identity of a metric.
      - **Name** *(string) --***[REQUIRED]**

        The name of the dimension.
    """


_MetricGetStatisticsResponseDatapointsTypeDef = TypedDict(
    "_MetricGetStatisticsResponseDatapointsTypeDef",
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


class MetricGetStatisticsResponseDatapointsTypeDef(_MetricGetStatisticsResponseDatapointsTypeDef):
    pass


_MetricGetStatisticsResponseTypeDef = TypedDict(
    "_MetricGetStatisticsResponseTypeDef",
    {"Label": str, "Datapoints": List[MetricGetStatisticsResponseDatapointsTypeDef]},
    total=False,
)


class MetricGetStatisticsResponseTypeDef(_MetricGetStatisticsResponseTypeDef):
    """
    - *(dict) --*

      - **Label** *(string) --*

        A label for the specified metric.
    """


_RequiredMetricPutAlarmDimensionsTypeDef = TypedDict(
    "_RequiredMetricPutAlarmDimensionsTypeDef", {"Name": str}
)
_OptionalMetricPutAlarmDimensionsTypeDef = TypedDict(
    "_OptionalMetricPutAlarmDimensionsTypeDef", {"Value": str}, total=False
)


class MetricPutAlarmDimensionsTypeDef(
    _RequiredMetricPutAlarmDimensionsTypeDef, _OptionalMetricPutAlarmDimensionsTypeDef
):
    """
    - *(dict) --*

      Expands the identity of a metric.
      - **Name** *(string) --***[REQUIRED]**

        The name of the dimension.
    """


_MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "_MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef(
    _MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef
):
    pass


_MetricPutAlarmMetricsMetricStatMetricTypeDef = TypedDict(
    "_MetricPutAlarmMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef],
    },
    total=False,
)


class MetricPutAlarmMetricsMetricStatMetricTypeDef(_MetricPutAlarmMetricsMetricStatMetricTypeDef):
    pass


_MetricPutAlarmMetricsMetricStatTypeDef = TypedDict(
    "_MetricPutAlarmMetricsMetricStatTypeDef",
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


class MetricPutAlarmMetricsMetricStatTypeDef(_MetricPutAlarmMetricsMetricStatTypeDef):
    pass


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
    """
    - *(dict) --*

      This structure is used in both ``GetMetricData`` and ``PutMetricAlarm`` . The supported use of
      this structure is different for those two operations.
      When used in ``GetMetricData`` , it indicates the metric data to return, and whether this call
      is just retrieving a batch set of data for one metric, or is performing a math expression on
      metric data. A single ``GetMetricData`` call can include up to 100 ``MetricDataQuery``
      structures.
      When used in ``PutMetricAlarm`` , it enables you to create an alarm based on a metric math
      expression. Each ``MetricDataQuery`` in the array specifies either a metric to retrieve, or a
      math expression to be performed on retrieved metrics. A single ``PutMetricAlarm`` call can
      include up to 20 ``MetricDataQuery`` structures in the array. The 20 structures can include as
      many as 10 structures that contain a ``MetricStat`` parameter to retrieve a metric, and as
      many as 10 structures that contain the ``Expression`` parameter to perform a math expression.
      Of those ``Expression`` structures, one must have ``True`` as the value for ``ReturnData`` .
      The result of this expression is the value the alarm watches.
      Any expression used in a ``PutMetricAlarm`` operation must return a single time series. For
      more information, see `Metric Math Syntax and Functions
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
      in the *Amazon CloudWatch User Guide* .
      Some of the parameters of this structure also have different uses whether you are using this
      structure in a ``GetMetricData`` operation or a ``PutMetricAlarm`` operation. These
      differences are explained in the following parameter list.
      - **Id** *(string) --***[REQUIRED]**

        A short name used to tie this object to the results in the response. This name must be
        unique within a single call to ``GetMetricData`` . If you are performing math expressions on
        this set of data, this name represents that data and can serve as a variable in the
        mathematical expression. The valid characters are letters, numbers, and underscore. The
        first character must be a lowercase letter.
    """


_RequiredMetricPutAlarmTagsTypeDef = TypedDict("_RequiredMetricPutAlarmTagsTypeDef", {"Key": str})
_OptionalMetricPutAlarmTagsTypeDef = TypedDict(
    "_OptionalMetricPutAlarmTagsTypeDef", {"Value": str}, total=False
)


class MetricPutAlarmTagsTypeDef(
    _RequiredMetricPutAlarmTagsTypeDef, _OptionalMetricPutAlarmTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair associated with a CloudWatch resource.
      - **Key** *(string) --***[REQUIRED]**

        A string that you can use to assign a value. The combination of tag keys and values can help
        you organize and categorize your resources.
    """


_RequiredMetricsFilterDimensionsTypeDef = TypedDict(
    "_RequiredMetricsFilterDimensionsTypeDef", {"Name": str}
)
_OptionalMetricsFilterDimensionsTypeDef = TypedDict(
    "_OptionalMetricsFilterDimensionsTypeDef", {"Value": str}, total=False
)


class MetricsFilterDimensionsTypeDef(
    _RequiredMetricsFilterDimensionsTypeDef, _OptionalMetricsFilterDimensionsTypeDef
):
    """
    - *(dict) --*

      Represents filters for a dimension.
      - **Name** *(string) --***[REQUIRED]**

        The dimension name to be matched.
    """
