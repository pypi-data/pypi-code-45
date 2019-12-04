"Main interface for logs service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateExportTaskResponseTypeDef",
    "ClientDescribeDestinationsResponsedestinationsTypeDef",
    "ClientDescribeDestinationsResponseTypeDef",
    "ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef",
    "ClientDescribeExportTasksResponseexportTasksstatusTypeDef",
    "ClientDescribeExportTasksResponseexportTasksTypeDef",
    "ClientDescribeExportTasksResponseTypeDef",
    "ClientDescribeLogGroupsResponselogGroupsTypeDef",
    "ClientDescribeLogGroupsResponseTypeDef",
    "ClientDescribeLogStreamsResponselogStreamsTypeDef",
    "ClientDescribeLogStreamsResponseTypeDef",
    "ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef",
    "ClientDescribeMetricFiltersResponsemetricFiltersTypeDef",
    "ClientDescribeMetricFiltersResponseTypeDef",
    "ClientDescribeQueriesResponsequeriesTypeDef",
    "ClientDescribeQueriesResponseTypeDef",
    "ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef",
    "ClientDescribeResourcePoliciesResponseTypeDef",
    "ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef",
    "ClientDescribeSubscriptionFiltersResponseTypeDef",
    "ClientFilterLogEventsResponseeventsTypeDef",
    "ClientFilterLogEventsResponsesearchedLogStreamsTypeDef",
    "ClientFilterLogEventsResponseTypeDef",
    "ClientGetLogEventsResponseeventsTypeDef",
    "ClientGetLogEventsResponseTypeDef",
    "ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef",
    "ClientGetLogGroupFieldsResponseTypeDef",
    "ClientGetLogRecordResponseTypeDef",
    "ClientGetQueryResultsResponseresultsTypeDef",
    "ClientGetQueryResultsResponsestatisticsTypeDef",
    "ClientGetQueryResultsResponseTypeDef",
    "ClientListTagsLogGroupResponseTypeDef",
    "ClientPutDestinationResponsedestinationTypeDef",
    "ClientPutDestinationResponseTypeDef",
    "ClientPutLogEventsLogEventsTypeDef",
    "ClientPutLogEventsResponserejectedLogEventsInfoTypeDef",
    "ClientPutLogEventsResponseTypeDef",
    "ClientPutMetricFilterMetricTransformationsTypeDef",
    "ClientPutResourcePolicyResponseresourcePolicyTypeDef",
    "ClientPutResourcePolicyResponseTypeDef",
    "ClientStartQueryResponseTypeDef",
    "ClientStopQueryResponseTypeDef",
    "ClientTestMetricFilterResponsematchesTypeDef",
    "ClientTestMetricFilterResponseTypeDef",
    "DescribeDestinationsPaginatePaginationConfigTypeDef",
    "DescribeDestinationsPaginateResponsedestinationsTypeDef",
    "DescribeDestinationsPaginateResponseTypeDef",
    "DescribeExportTasksPaginatePaginationConfigTypeDef",
    "DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef",
    "DescribeExportTasksPaginateResponseexportTasksstatusTypeDef",
    "DescribeExportTasksPaginateResponseexportTasksTypeDef",
    "DescribeExportTasksPaginateResponseTypeDef",
    "DescribeLogGroupsPaginatePaginationConfigTypeDef",
    "DescribeLogGroupsPaginateResponselogGroupsTypeDef",
    "DescribeLogGroupsPaginateResponseTypeDef",
    "DescribeLogStreamsPaginatePaginationConfigTypeDef",
    "DescribeLogStreamsPaginateResponselogStreamsTypeDef",
    "DescribeLogStreamsPaginateResponseTypeDef",
    "DescribeMetricFiltersPaginatePaginationConfigTypeDef",
    "DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef",
    "DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef",
    "DescribeMetricFiltersPaginateResponseTypeDef",
    "DescribeQueriesPaginatePaginationConfigTypeDef",
    "DescribeQueriesPaginateResponsequeriesTypeDef",
    "DescribeQueriesPaginateResponseTypeDef",
    "DescribeResourcePoliciesPaginatePaginationConfigTypeDef",
    "DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef",
    "DescribeResourcePoliciesPaginateResponseTypeDef",
    "DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef",
    "DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef",
    "DescribeSubscriptionFiltersPaginateResponseTypeDef",
    "FilterLogEventsPaginatePaginationConfigTypeDef",
    "FilterLogEventsPaginateResponseeventsTypeDef",
    "FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef",
    "FilterLogEventsPaginateResponseTypeDef",
)


_ClientCreateExportTaskResponseTypeDef = TypedDict(
    "_ClientCreateExportTaskResponseTypeDef", {"taskId": str}, total=False
)


class ClientCreateExportTaskResponseTypeDef(_ClientCreateExportTaskResponseTypeDef):
    """
    - *(dict) --*

      - **taskId** *(string) --*

        The ID of the export task.
    """


_ClientDescribeDestinationsResponsedestinationsTypeDef = TypedDict(
    "_ClientDescribeDestinationsResponsedestinationsTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
        "accessPolicy": str,
        "arn": str,
        "creationTime": int,
    },
    total=False,
)


class ClientDescribeDestinationsResponsedestinationsTypeDef(
    _ClientDescribeDestinationsResponsedestinationsTypeDef
):
    """
    - *(dict) --*

      Represents a cross-account destination that receives subscription log events.
      - **destinationName** *(string) --*

        The name of the destination.
    """


_ClientDescribeDestinationsResponseTypeDef = TypedDict(
    "_ClientDescribeDestinationsResponseTypeDef",
    {"destinations": List[ClientDescribeDestinationsResponsedestinationsTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeDestinationsResponseTypeDef(_ClientDescribeDestinationsResponseTypeDef):
    """
    - *(dict) --*

      - **destinations** *(list) --*

        The destinations.
        - *(dict) --*

          Represents a cross-account destination that receives subscription log events.
          - **destinationName** *(string) --*

            The name of the destination.
    """


_ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef = TypedDict(
    "_ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef",
    {"creationTime": int, "completionTime": int},
    total=False,
)


class ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef(
    _ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef
):
    pass


_ClientDescribeExportTasksResponseexportTasksstatusTypeDef = TypedDict(
    "_ClientDescribeExportTasksResponseexportTasksstatusTypeDef",
    {
        "code": Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"],
        "message": str,
    },
    total=False,
)


class ClientDescribeExportTasksResponseexportTasksstatusTypeDef(
    _ClientDescribeExportTasksResponseexportTasksstatusTypeDef
):
    pass


_ClientDescribeExportTasksResponseexportTasksTypeDef = TypedDict(
    "_ClientDescribeExportTasksResponseexportTasksTypeDef",
    {
        "taskId": str,
        "taskName": str,
        "logGroupName": str,
        "from": int,
        "to": int,
        "destination": str,
        "destinationPrefix": str,
        "status": ClientDescribeExportTasksResponseexportTasksstatusTypeDef,
        "executionInfo": ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef,
    },
    total=False,
)


class ClientDescribeExportTasksResponseexportTasksTypeDef(
    _ClientDescribeExportTasksResponseexportTasksTypeDef
):
    """
    - *(dict) --*

      Represents an export task.
      - **taskId** *(string) --*

        The ID of the export task.
    """


_ClientDescribeExportTasksResponseTypeDef = TypedDict(
    "_ClientDescribeExportTasksResponseTypeDef",
    {"exportTasks": List[ClientDescribeExportTasksResponseexportTasksTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeExportTasksResponseTypeDef(_ClientDescribeExportTasksResponseTypeDef):
    """
    - *(dict) --*

      - **exportTasks** *(list) --*

        The export tasks.
        - *(dict) --*

          Represents an export task.
          - **taskId** *(string) --*

            The ID of the export task.
    """


_ClientDescribeLogGroupsResponselogGroupsTypeDef = TypedDict(
    "_ClientDescribeLogGroupsResponselogGroupsTypeDef",
    {
        "logGroupName": str,
        "creationTime": int,
        "retentionInDays": int,
        "metricFilterCount": int,
        "arn": str,
        "storedBytes": int,
        "kmsKeyId": str,
    },
    total=False,
)


class ClientDescribeLogGroupsResponselogGroupsTypeDef(
    _ClientDescribeLogGroupsResponselogGroupsTypeDef
):
    """
    - *(dict) --*

      Represents a log group.
      - **logGroupName** *(string) --*

        The name of the log group.
    """


_ClientDescribeLogGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeLogGroupsResponseTypeDef",
    {"logGroups": List[ClientDescribeLogGroupsResponselogGroupsTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeLogGroupsResponseTypeDef(_ClientDescribeLogGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **logGroups** *(list) --*

        The log groups.
        - *(dict) --*

          Represents a log group.
          - **logGroupName** *(string) --*

            The name of the log group.
    """


_ClientDescribeLogStreamsResponselogStreamsTypeDef = TypedDict(
    "_ClientDescribeLogStreamsResponselogStreamsTypeDef",
    {
        "logStreamName": str,
        "creationTime": int,
        "firstEventTimestamp": int,
        "lastEventTimestamp": int,
        "lastIngestionTime": int,
        "uploadSequenceToken": str,
        "arn": str,
        "storedBytes": int,
    },
    total=False,
)


class ClientDescribeLogStreamsResponselogStreamsTypeDef(
    _ClientDescribeLogStreamsResponselogStreamsTypeDef
):
    """
    - *(dict) --*

      Represents a log stream, which is a sequence of log events from a single emitter of logs.
      - **logStreamName** *(string) --*

        The name of the log stream.
    """


_ClientDescribeLogStreamsResponseTypeDef = TypedDict(
    "_ClientDescribeLogStreamsResponseTypeDef",
    {"logStreams": List[ClientDescribeLogStreamsResponselogStreamsTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeLogStreamsResponseTypeDef(_ClientDescribeLogStreamsResponseTypeDef):
    """
    - *(dict) --*

      - **logStreams** *(list) --*

        The log streams.
        - *(dict) --*

          Represents a log stream, which is a sequence of log events from a single emitter of logs.
          - **logStreamName** *(string) --*

            The name of the log stream.
    """


_ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef = TypedDict(
    "_ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef",
    {"metricName": str, "metricNamespace": str, "metricValue": str, "defaultValue": float},
    total=False,
)


class ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef(
    _ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef
):
    pass


_ClientDescribeMetricFiltersResponsemetricFiltersTypeDef = TypedDict(
    "_ClientDescribeMetricFiltersResponsemetricFiltersTypeDef",
    {
        "filterName": str,
        "filterPattern": str,
        "metricTransformations": List[
            ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef
        ],
        "creationTime": int,
        "logGroupName": str,
    },
    total=False,
)


class ClientDescribeMetricFiltersResponsemetricFiltersTypeDef(
    _ClientDescribeMetricFiltersResponsemetricFiltersTypeDef
):
    """
    - *(dict) --*

      Metric filters express how CloudWatch Logs would extract metric observations from ingested log
      events and transform them into metric data in a CloudWatch metric.
      - **filterName** *(string) --*

        The name of the metric filter.
    """


_ClientDescribeMetricFiltersResponseTypeDef = TypedDict(
    "_ClientDescribeMetricFiltersResponseTypeDef",
    {
        "metricFilters": List[ClientDescribeMetricFiltersResponsemetricFiltersTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeMetricFiltersResponseTypeDef(_ClientDescribeMetricFiltersResponseTypeDef):
    """
    - *(dict) --*

      - **metricFilters** *(list) --*

        The metric filters.
        - *(dict) --*

          Metric filters express how CloudWatch Logs would extract metric observations from ingested
          log events and transform them into metric data in a CloudWatch metric.
          - **filterName** *(string) --*

            The name of the metric filter.
    """


_ClientDescribeQueriesResponsequeriesTypeDef = TypedDict(
    "_ClientDescribeQueriesResponsequeriesTypeDef",
    {
        "queryId": str,
        "queryString": str,
        "status": Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"],
        "createTime": int,
        "logGroupName": str,
    },
    total=False,
)


class ClientDescribeQueriesResponsequeriesTypeDef(_ClientDescribeQueriesResponsequeriesTypeDef):
    """
    - *(dict) --*

      Information about one CloudWatch Logs Insights query that matches the request in a
      ``DescribeQueries`` operation.
      - **queryId** *(string) --*

        The unique ID number of this query.
    """


_ClientDescribeQueriesResponseTypeDef = TypedDict(
    "_ClientDescribeQueriesResponseTypeDef",
    {"queries": List[ClientDescribeQueriesResponsequeriesTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeQueriesResponseTypeDef(_ClientDescribeQueriesResponseTypeDef):
    """
    - *(dict) --*

      - **queries** *(list) --*

        The list of queries that match the request.
        - *(dict) --*

          Information about one CloudWatch Logs Insights query that matches the request in a
          ``DescribeQueries`` operation.
          - **queryId** *(string) --*

            The unique ID number of this query.
    """


_ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef = TypedDict(
    "_ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef",
    {"policyName": str, "policyDocument": str, "lastUpdatedTime": int},
    total=False,
)


class ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef(
    _ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef
):
    """
    - *(dict) --*

      A policy enabling one or more entities to put logs to a log group in this account.
      - **policyName** *(string) --*

        The name of the resource policy.
    """


_ClientDescribeResourcePoliciesResponseTypeDef = TypedDict(
    "_ClientDescribeResourcePoliciesResponseTypeDef",
    {
        "resourcePolicies": List[ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeResourcePoliciesResponseTypeDef(_ClientDescribeResourcePoliciesResponseTypeDef):
    """
    - *(dict) --*

      - **resourcePolicies** *(list) --*

        The resource policies that exist in this account.
        - *(dict) --*

          A policy enabling one or more entities to put logs to a log group in this account.
          - **policyName** *(string) --*

            The name of the resource policy.
    """


_ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef = TypedDict(
    "_ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef",
    {
        "filterName": str,
        "logGroupName": str,
        "filterPattern": str,
        "destinationArn": str,
        "roleArn": str,
        "distribution": Literal["Random", "ByLogStream"],
        "creationTime": int,
    },
    total=False,
)


class ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef(
    _ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef
):
    """
    - *(dict) --*

      Represents a subscription filter.
      - **filterName** *(string) --*

        The name of the subscription filter.
    """


_ClientDescribeSubscriptionFiltersResponseTypeDef = TypedDict(
    "_ClientDescribeSubscriptionFiltersResponseTypeDef",
    {
        "subscriptionFilters": List[
            ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeSubscriptionFiltersResponseTypeDef(
    _ClientDescribeSubscriptionFiltersResponseTypeDef
):
    """
    - *(dict) --*

      - **subscriptionFilters** *(list) --*

        The subscription filters.
        - *(dict) --*

          Represents a subscription filter.
          - **filterName** *(string) --*

            The name of the subscription filter.
    """


_ClientFilterLogEventsResponseeventsTypeDef = TypedDict(
    "_ClientFilterLogEventsResponseeventsTypeDef",
    {"logStreamName": str, "timestamp": int, "message": str, "ingestionTime": int, "eventId": str},
    total=False,
)


class ClientFilterLogEventsResponseeventsTypeDef(_ClientFilterLogEventsResponseeventsTypeDef):
    """
    - *(dict) --*

      Represents a matched event.
      - **logStreamName** *(string) --*

        The name of the log stream to which this event belongs.
    """


_ClientFilterLogEventsResponsesearchedLogStreamsTypeDef = TypedDict(
    "_ClientFilterLogEventsResponsesearchedLogStreamsTypeDef",
    {"logStreamName": str, "searchedCompletely": bool},
    total=False,
)


class ClientFilterLogEventsResponsesearchedLogStreamsTypeDef(
    _ClientFilterLogEventsResponsesearchedLogStreamsTypeDef
):
    pass


_ClientFilterLogEventsResponseTypeDef = TypedDict(
    "_ClientFilterLogEventsResponseTypeDef",
    {
        "events": List[ClientFilterLogEventsResponseeventsTypeDef],
        "searchedLogStreams": List[ClientFilterLogEventsResponsesearchedLogStreamsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientFilterLogEventsResponseTypeDef(_ClientFilterLogEventsResponseTypeDef):
    """
    - *(dict) --*

      - **events** *(list) --*

        The matched events.
        - *(dict) --*

          Represents a matched event.
          - **logStreamName** *(string) --*

            The name of the log stream to which this event belongs.
    """


_ClientGetLogEventsResponseeventsTypeDef = TypedDict(
    "_ClientGetLogEventsResponseeventsTypeDef",
    {"timestamp": int, "message": str, "ingestionTime": int},
    total=False,
)


class ClientGetLogEventsResponseeventsTypeDef(_ClientGetLogEventsResponseeventsTypeDef):
    """
    - *(dict) --*

      Represents a log event.
      - **timestamp** *(integer) --*

        The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970
        00:00:00 UTC.
    """


_ClientGetLogEventsResponseTypeDef = TypedDict(
    "_ClientGetLogEventsResponseTypeDef",
    {
        "events": List[ClientGetLogEventsResponseeventsTypeDef],
        "nextForwardToken": str,
        "nextBackwardToken": str,
    },
    total=False,
)


class ClientGetLogEventsResponseTypeDef(_ClientGetLogEventsResponseTypeDef):
    """
    - *(dict) --*

      - **events** *(list) --*

        The events.
        - *(dict) --*

          Represents a log event.
          - **timestamp** *(integer) --*

            The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970
            00:00:00 UTC.
    """


_ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef = TypedDict(
    "_ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef",
    {"name": str, "percent": int},
    total=False,
)


class ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef(
    _ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef
):
    """
    - *(dict) --*

      The fields contained in log events found by a ``GetLogGroupFields`` operation, along with the
      percentage of queried log events in which each field appears.
      - **name** *(string) --*

        The name of a log field.
    """


_ClientGetLogGroupFieldsResponseTypeDef = TypedDict(
    "_ClientGetLogGroupFieldsResponseTypeDef",
    {"logGroupFields": List[ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef]},
    total=False,
)


class ClientGetLogGroupFieldsResponseTypeDef(_ClientGetLogGroupFieldsResponseTypeDef):
    """
    - *(dict) --*

      - **logGroupFields** *(list) --*

        The array of fields found in the query. Each object in the array contains the name of the
        field, along with the percentage of time it appeared in the log events that were queried.
        - *(dict) --*

          The fields contained in log events found by a ``GetLogGroupFields`` operation, along with
          the percentage of queried log events in which each field appears.
          - **name** *(string) --*

            The name of a log field.
    """


_ClientGetLogRecordResponseTypeDef = TypedDict(
    "_ClientGetLogRecordResponseTypeDef", {"logRecord": Dict[str, str]}, total=False
)


class ClientGetLogRecordResponseTypeDef(_ClientGetLogRecordResponseTypeDef):
    """
    - *(dict) --*

      - **logRecord** *(dict) --*

        The requested log event, as a JSON string.
        - *(string) --*

          - *(string) --*
    """


_ClientGetQueryResultsResponseresultsTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseresultsTypeDef", {"field": str, "value": str}, total=False
)


class ClientGetQueryResultsResponseresultsTypeDef(_ClientGetQueryResultsResponseresultsTypeDef):
    """
    - *(dict) --*

      Contains one field from one log event returned by a CloudWatch Logs Insights query, along with
      the value of that field.
      - **field** *(string) --*

        The log event field.
    """


_ClientGetQueryResultsResponsestatisticsTypeDef = TypedDict(
    "_ClientGetQueryResultsResponsestatisticsTypeDef",
    {"recordsMatched": float, "recordsScanned": float, "bytesScanned": float},
    total=False,
)


class ClientGetQueryResultsResponsestatisticsTypeDef(
    _ClientGetQueryResultsResponsestatisticsTypeDef
):
    pass


_ClientGetQueryResultsResponseTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseTypeDef",
    {
        "results": List[List[ClientGetQueryResultsResponseresultsTypeDef]],
        "statistics": ClientGetQueryResultsResponsestatisticsTypeDef,
        "status": Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"],
    },
    total=False,
)


class ClientGetQueryResultsResponseTypeDef(_ClientGetQueryResultsResponseTypeDef):
    """
    - *(dict) --*

      - **results** *(list) --*

        The log events that matched the query criteria during the most recent time it ran.
        The ``results`` value is an array of arrays. Each log event is one object in the top-level
        array. Each of these log event objects is an array of ``field`` /``value`` pairs.
        - *(list) --*

          - *(dict) --*

            Contains one field from one log event returned by a CloudWatch Logs Insights query,
            along with the value of that field.
            - **field** *(string) --*

              The log event field.
    """


_ClientListTagsLogGroupResponseTypeDef = TypedDict(
    "_ClientListTagsLogGroupResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsLogGroupResponseTypeDef(_ClientListTagsLogGroupResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(dict) --*

        The tags for the log group.
        - *(string) --*

          - *(string) --*
    """


_ClientPutDestinationResponsedestinationTypeDef = TypedDict(
    "_ClientPutDestinationResponsedestinationTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
        "accessPolicy": str,
        "arn": str,
        "creationTime": int,
    },
    total=False,
)


class ClientPutDestinationResponsedestinationTypeDef(
    _ClientPutDestinationResponsedestinationTypeDef
):
    """
    - **destination** *(dict) --*

      The destination.
      - **destinationName** *(string) --*

        The name of the destination.
    """


_ClientPutDestinationResponseTypeDef = TypedDict(
    "_ClientPutDestinationResponseTypeDef",
    {"destination": ClientPutDestinationResponsedestinationTypeDef},
    total=False,
)


class ClientPutDestinationResponseTypeDef(_ClientPutDestinationResponseTypeDef):
    """
    - *(dict) --*

      - **destination** *(dict) --*

        The destination.
        - **destinationName** *(string) --*

          The name of the destination.
    """


_RequiredClientPutLogEventsLogEventsTypeDef = TypedDict(
    "_RequiredClientPutLogEventsLogEventsTypeDef", {"timestamp": int}
)
_OptionalClientPutLogEventsLogEventsTypeDef = TypedDict(
    "_OptionalClientPutLogEventsLogEventsTypeDef", {"message": str}, total=False
)


class ClientPutLogEventsLogEventsTypeDef(
    _RequiredClientPutLogEventsLogEventsTypeDef, _OptionalClientPutLogEventsLogEventsTypeDef
):
    """
    - *(dict) --*

      Represents a log event, which is a record of activity that was recorded by the application or
      resource being monitored.
      - **timestamp** *(integer) --***[REQUIRED]**

        The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970
        00:00:00 UTC.
    """


_ClientPutLogEventsResponserejectedLogEventsInfoTypeDef = TypedDict(
    "_ClientPutLogEventsResponserejectedLogEventsInfoTypeDef",
    {
        "tooNewLogEventStartIndex": int,
        "tooOldLogEventEndIndex": int,
        "expiredLogEventEndIndex": int,
    },
    total=False,
)


class ClientPutLogEventsResponserejectedLogEventsInfoTypeDef(
    _ClientPutLogEventsResponserejectedLogEventsInfoTypeDef
):
    pass


_ClientPutLogEventsResponseTypeDef = TypedDict(
    "_ClientPutLogEventsResponseTypeDef",
    {
        "nextSequenceToken": str,
        "rejectedLogEventsInfo": ClientPutLogEventsResponserejectedLogEventsInfoTypeDef,
    },
    total=False,
)


class ClientPutLogEventsResponseTypeDef(_ClientPutLogEventsResponseTypeDef):
    """
    - *(dict) --*

      - **nextSequenceToken** *(string) --*

        The next sequence token.
    """


_RequiredClientPutMetricFilterMetricTransformationsTypeDef = TypedDict(
    "_RequiredClientPutMetricFilterMetricTransformationsTypeDef", {"metricName": str}
)
_OptionalClientPutMetricFilterMetricTransformationsTypeDef = TypedDict(
    "_OptionalClientPutMetricFilterMetricTransformationsTypeDef",
    {"metricNamespace": str, "metricValue": str, "defaultValue": float},
    total=False,
)


class ClientPutMetricFilterMetricTransformationsTypeDef(
    _RequiredClientPutMetricFilterMetricTransformationsTypeDef,
    _OptionalClientPutMetricFilterMetricTransformationsTypeDef,
):
    """
    - *(dict) --*

      Indicates how to transform ingested log events to metric data in a CloudWatch metric.
      - **metricName** *(string) --***[REQUIRED]**

        The name of the CloudWatch metric.
    """


_ClientPutResourcePolicyResponseresourcePolicyTypeDef = TypedDict(
    "_ClientPutResourcePolicyResponseresourcePolicyTypeDef",
    {"policyName": str, "policyDocument": str, "lastUpdatedTime": int},
    total=False,
)


class ClientPutResourcePolicyResponseresourcePolicyTypeDef(
    _ClientPutResourcePolicyResponseresourcePolicyTypeDef
):
    """
    - **resourcePolicy** *(dict) --*

      The new policy.
      - **policyName** *(string) --*

        The name of the resource policy.
    """


_ClientPutResourcePolicyResponseTypeDef = TypedDict(
    "_ClientPutResourcePolicyResponseTypeDef",
    {"resourcePolicy": ClientPutResourcePolicyResponseresourcePolicyTypeDef},
    total=False,
)


class ClientPutResourcePolicyResponseTypeDef(_ClientPutResourcePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **resourcePolicy** *(dict) --*

        The new policy.
        - **policyName** *(string) --*

          The name of the resource policy.
    """


_ClientStartQueryResponseTypeDef = TypedDict(
    "_ClientStartQueryResponseTypeDef", {"queryId": str}, total=False
)


class ClientStartQueryResponseTypeDef(_ClientStartQueryResponseTypeDef):
    """
    - *(dict) --*

      - **queryId** *(string) --*

        The unique ID of the query.
    """


_ClientStopQueryResponseTypeDef = TypedDict(
    "_ClientStopQueryResponseTypeDef", {"success": bool}, total=False
)


class ClientStopQueryResponseTypeDef(_ClientStopQueryResponseTypeDef):
    """
    - *(dict) --*

      - **success** *(boolean) --*

        This is true if the query was stopped by the ``StopQuery`` operation.
    """


_ClientTestMetricFilterResponsematchesTypeDef = TypedDict(
    "_ClientTestMetricFilterResponsematchesTypeDef",
    {"eventNumber": int, "eventMessage": str, "extractedValues": Dict[str, str]},
    total=False,
)


class ClientTestMetricFilterResponsematchesTypeDef(_ClientTestMetricFilterResponsematchesTypeDef):
    """
    - *(dict) --*

      Represents a matched event.
      - **eventNumber** *(integer) --*

        The event number.
    """


_ClientTestMetricFilterResponseTypeDef = TypedDict(
    "_ClientTestMetricFilterResponseTypeDef",
    {"matches": List[ClientTestMetricFilterResponsematchesTypeDef]},
    total=False,
)


class ClientTestMetricFilterResponseTypeDef(_ClientTestMetricFilterResponseTypeDef):
    """
    - *(dict) --*

      - **matches** *(list) --*

        The matched events.
        - *(dict) --*

          Represents a matched event.
          - **eventNumber** *(integer) --*

            The event number.
    """


_DescribeDestinationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDestinationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDestinationsPaginatePaginationConfigTypeDef(
    _DescribeDestinationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDestinationsPaginateResponsedestinationsTypeDef = TypedDict(
    "_DescribeDestinationsPaginateResponsedestinationsTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
        "accessPolicy": str,
        "arn": str,
        "creationTime": int,
    },
    total=False,
)


class DescribeDestinationsPaginateResponsedestinationsTypeDef(
    _DescribeDestinationsPaginateResponsedestinationsTypeDef
):
    """
    - *(dict) --*

      Represents a cross-account destination that receives subscription log events.
      - **destinationName** *(string) --*

        The name of the destination.
    """


_DescribeDestinationsPaginateResponseTypeDef = TypedDict(
    "_DescribeDestinationsPaginateResponseTypeDef",
    {
        "destinations": List[DescribeDestinationsPaginateResponsedestinationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDestinationsPaginateResponseTypeDef(_DescribeDestinationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **destinations** *(list) --*

        The destinations.
        - *(dict) --*

          Represents a cross-account destination that receives subscription log events.
          - **destinationName** *(string) --*

            The name of the destination.
    """


_DescribeExportTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeExportTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeExportTasksPaginatePaginationConfigTypeDef(
    _DescribeExportTasksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef = TypedDict(
    "_DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef",
    {"creationTime": int, "completionTime": int},
    total=False,
)


class DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef(
    _DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef
):
    pass


_DescribeExportTasksPaginateResponseexportTasksstatusTypeDef = TypedDict(
    "_DescribeExportTasksPaginateResponseexportTasksstatusTypeDef",
    {
        "code": Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"],
        "message": str,
    },
    total=False,
)


class DescribeExportTasksPaginateResponseexportTasksstatusTypeDef(
    _DescribeExportTasksPaginateResponseexportTasksstatusTypeDef
):
    pass


_DescribeExportTasksPaginateResponseexportTasksTypeDef = TypedDict(
    "_DescribeExportTasksPaginateResponseexportTasksTypeDef",
    {
        "taskId": str,
        "taskName": str,
        "logGroupName": str,
        "from": int,
        "to": int,
        "destination": str,
        "destinationPrefix": str,
        "status": DescribeExportTasksPaginateResponseexportTasksstatusTypeDef,
        "executionInfo": DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef,
    },
    total=False,
)


class DescribeExportTasksPaginateResponseexportTasksTypeDef(
    _DescribeExportTasksPaginateResponseexportTasksTypeDef
):
    """
    - *(dict) --*

      Represents an export task.
      - **taskId** *(string) --*

        The ID of the export task.
    """


_DescribeExportTasksPaginateResponseTypeDef = TypedDict(
    "_DescribeExportTasksPaginateResponseTypeDef",
    {"exportTasks": List[DescribeExportTasksPaginateResponseexportTasksTypeDef], "NextToken": str},
    total=False,
)


class DescribeExportTasksPaginateResponseTypeDef(_DescribeExportTasksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **exportTasks** *(list) --*

        The export tasks.
        - *(dict) --*

          Represents an export task.
          - **taskId** *(string) --*

            The ID of the export task.
    """


_DescribeLogGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeLogGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeLogGroupsPaginatePaginationConfigTypeDef(
    _DescribeLogGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeLogGroupsPaginateResponselogGroupsTypeDef = TypedDict(
    "_DescribeLogGroupsPaginateResponselogGroupsTypeDef",
    {
        "logGroupName": str,
        "creationTime": int,
        "retentionInDays": int,
        "metricFilterCount": int,
        "arn": str,
        "storedBytes": int,
        "kmsKeyId": str,
    },
    total=False,
)


class DescribeLogGroupsPaginateResponselogGroupsTypeDef(
    _DescribeLogGroupsPaginateResponselogGroupsTypeDef
):
    """
    - *(dict) --*

      Represents a log group.
      - **logGroupName** *(string) --*

        The name of the log group.
    """


_DescribeLogGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeLogGroupsPaginateResponseTypeDef",
    {"logGroups": List[DescribeLogGroupsPaginateResponselogGroupsTypeDef], "NextToken": str},
    total=False,
)


class DescribeLogGroupsPaginateResponseTypeDef(_DescribeLogGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **logGroups** *(list) --*

        The log groups.
        - *(dict) --*

          Represents a log group.
          - **logGroupName** *(string) --*

            The name of the log group.
    """


_DescribeLogStreamsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeLogStreamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeLogStreamsPaginatePaginationConfigTypeDef(
    _DescribeLogStreamsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeLogStreamsPaginateResponselogStreamsTypeDef = TypedDict(
    "_DescribeLogStreamsPaginateResponselogStreamsTypeDef",
    {
        "logStreamName": str,
        "creationTime": int,
        "firstEventTimestamp": int,
        "lastEventTimestamp": int,
        "lastIngestionTime": int,
        "uploadSequenceToken": str,
        "arn": str,
        "storedBytes": int,
    },
    total=False,
)


class DescribeLogStreamsPaginateResponselogStreamsTypeDef(
    _DescribeLogStreamsPaginateResponselogStreamsTypeDef
):
    """
    - *(dict) --*

      Represents a log stream, which is a sequence of log events from a single emitter of logs.
      - **logStreamName** *(string) --*

        The name of the log stream.
    """


_DescribeLogStreamsPaginateResponseTypeDef = TypedDict(
    "_DescribeLogStreamsPaginateResponseTypeDef",
    {"logStreams": List[DescribeLogStreamsPaginateResponselogStreamsTypeDef], "NextToken": str},
    total=False,
)


class DescribeLogStreamsPaginateResponseTypeDef(_DescribeLogStreamsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **logStreams** *(list) --*

        The log streams.
        - *(dict) --*

          Represents a log stream, which is a sequence of log events from a single emitter of logs.
          - **logStreamName** *(string) --*

            The name of the log stream.
    """


_DescribeMetricFiltersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMetricFiltersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMetricFiltersPaginatePaginationConfigTypeDef(
    _DescribeMetricFiltersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef = TypedDict(
    "_DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef",
    {"metricName": str, "metricNamespace": str, "metricValue": str, "defaultValue": float},
    total=False,
)


class DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef(
    _DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef
):
    pass


_DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef = TypedDict(
    "_DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef",
    {
        "filterName": str,
        "filterPattern": str,
        "metricTransformations": List[
            DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef
        ],
        "creationTime": int,
        "logGroupName": str,
    },
    total=False,
)


class DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef(
    _DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef
):
    """
    - *(dict) --*

      Metric filters express how CloudWatch Logs would extract metric observations from ingested log
      events and transform them into metric data in a CloudWatch metric.
      - **filterName** *(string) --*

        The name of the metric filter.
    """


_DescribeMetricFiltersPaginateResponseTypeDef = TypedDict(
    "_DescribeMetricFiltersPaginateResponseTypeDef",
    {
        "metricFilters": List[DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeMetricFiltersPaginateResponseTypeDef(_DescribeMetricFiltersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **metricFilters** *(list) --*

        The metric filters.
        - *(dict) --*

          Metric filters express how CloudWatch Logs would extract metric observations from ingested
          log events and transform them into metric data in a CloudWatch metric.
          - **filterName** *(string) --*

            The name of the metric filter.
    """


_DescribeQueriesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeQueriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeQueriesPaginatePaginationConfigTypeDef(
    _DescribeQueriesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeQueriesPaginateResponsequeriesTypeDef = TypedDict(
    "_DescribeQueriesPaginateResponsequeriesTypeDef",
    {
        "queryId": str,
        "queryString": str,
        "status": Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"],
        "createTime": int,
        "logGroupName": str,
    },
    total=False,
)


class DescribeQueriesPaginateResponsequeriesTypeDef(_DescribeQueriesPaginateResponsequeriesTypeDef):
    """
    - *(dict) --*

      Information about one CloudWatch Logs Insights query that matches the request in a
      ``DescribeQueries`` operation.
      - **queryId** *(string) --*

        The unique ID number of this query.
    """


_DescribeQueriesPaginateResponseTypeDef = TypedDict(
    "_DescribeQueriesPaginateResponseTypeDef",
    {"queries": List[DescribeQueriesPaginateResponsequeriesTypeDef], "NextToken": str},
    total=False,
)


class DescribeQueriesPaginateResponseTypeDef(_DescribeQueriesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **queries** *(list) --*

        The list of queries that match the request.
        - *(dict) --*

          Information about one CloudWatch Logs Insights query that matches the request in a
          ``DescribeQueries`` operation.
          - **queryId** *(string) --*

            The unique ID number of this query.
    """


_DescribeResourcePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeResourcePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeResourcePoliciesPaginatePaginationConfigTypeDef(
    _DescribeResourcePoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef = TypedDict(
    "_DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef",
    {"policyName": str, "policyDocument": str, "lastUpdatedTime": int},
    total=False,
)


class DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef(
    _DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef
):
    """
    - *(dict) --*

      A policy enabling one or more entities to put logs to a log group in this account.
      - **policyName** *(string) --*

        The name of the resource policy.
    """


_DescribeResourcePoliciesPaginateResponseTypeDef = TypedDict(
    "_DescribeResourcePoliciesPaginateResponseTypeDef",
    {
        "resourcePolicies": List[DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeResourcePoliciesPaginateResponseTypeDef(
    _DescribeResourcePoliciesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **resourcePolicies** *(list) --*

        The resource policies that exist in this account.
        - *(dict) --*

          A policy enabling one or more entities to put logs to a log group in this account.
          - **policyName** *(string) --*

            The name of the resource policy.
    """


_DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef(
    _DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef = TypedDict(
    "_DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef",
    {
        "filterName": str,
        "logGroupName": str,
        "filterPattern": str,
        "destinationArn": str,
        "roleArn": str,
        "distribution": Literal["Random", "ByLogStream"],
        "creationTime": int,
    },
    total=False,
)


class DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef(
    _DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef
):
    """
    - *(dict) --*

      Represents a subscription filter.
      - **filterName** *(string) --*

        The name of the subscription filter.
    """


_DescribeSubscriptionFiltersPaginateResponseTypeDef = TypedDict(
    "_DescribeSubscriptionFiltersPaginateResponseTypeDef",
    {
        "subscriptionFilters": List[
            DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeSubscriptionFiltersPaginateResponseTypeDef(
    _DescribeSubscriptionFiltersPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **subscriptionFilters** *(list) --*

        The subscription filters.
        - *(dict) --*

          Represents a subscription filter.
          - **filterName** *(string) --*

            The name of the subscription filter.
    """


_FilterLogEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_FilterLogEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class FilterLogEventsPaginatePaginationConfigTypeDef(
    _FilterLogEventsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_FilterLogEventsPaginateResponseeventsTypeDef = TypedDict(
    "_FilterLogEventsPaginateResponseeventsTypeDef",
    {"logStreamName": str, "timestamp": int, "message": str, "ingestionTime": int, "eventId": str},
    total=False,
)


class FilterLogEventsPaginateResponseeventsTypeDef(_FilterLogEventsPaginateResponseeventsTypeDef):
    """
    - *(dict) --*

      Represents a matched event.
      - **logStreamName** *(string) --*

        The name of the log stream to which this event belongs.
    """


_FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef = TypedDict(
    "_FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef",
    {"logStreamName": str, "searchedCompletely": bool},
    total=False,
)


class FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef(
    _FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef
):
    pass


_FilterLogEventsPaginateResponseTypeDef = TypedDict(
    "_FilterLogEventsPaginateResponseTypeDef",
    {
        "events": List[FilterLogEventsPaginateResponseeventsTypeDef],
        "searchedLogStreams": List[FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class FilterLogEventsPaginateResponseTypeDef(_FilterLogEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **events** *(list) --*

        The matched events.
        - *(dict) --*

          Represents a matched event.
          - **logStreamName** *(string) --*

            The name of the log stream to which this event belongs.
    """
