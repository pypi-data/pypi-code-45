"Main interface for logs service type defs"
from __future__ import annotations

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


ClientCreateExportTaskResponseTypeDef = TypedDict(
    "ClientCreateExportTaskResponseTypeDef", {"taskId": str}, total=False
)

ClientDescribeDestinationsResponsedestinationsTypeDef = TypedDict(
    "ClientDescribeDestinationsResponsedestinationsTypeDef",
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

ClientDescribeDestinationsResponseTypeDef = TypedDict(
    "ClientDescribeDestinationsResponseTypeDef",
    {"destinations": List[ClientDescribeDestinationsResponsedestinationsTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef",
    {"creationTime": int, "completionTime": int},
    total=False,
)

ClientDescribeExportTasksResponseexportTasksstatusTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseexportTasksstatusTypeDef",
    {
        "code": Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"],
        "message": str,
    },
    total=False,
)

ClientDescribeExportTasksResponseexportTasksTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseexportTasksTypeDef",
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

ClientDescribeExportTasksResponseTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseTypeDef",
    {"exportTasks": List[ClientDescribeExportTasksResponseexportTasksTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeLogGroupsResponselogGroupsTypeDef = TypedDict(
    "ClientDescribeLogGroupsResponselogGroupsTypeDef",
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

ClientDescribeLogGroupsResponseTypeDef = TypedDict(
    "ClientDescribeLogGroupsResponseTypeDef",
    {"logGroups": List[ClientDescribeLogGroupsResponselogGroupsTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeLogStreamsResponselogStreamsTypeDef = TypedDict(
    "ClientDescribeLogStreamsResponselogStreamsTypeDef",
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

ClientDescribeLogStreamsResponseTypeDef = TypedDict(
    "ClientDescribeLogStreamsResponseTypeDef",
    {"logStreams": List[ClientDescribeLogStreamsResponselogStreamsTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef = TypedDict(
    "ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef",
    {"metricName": str, "metricNamespace": str, "metricValue": str, "defaultValue": float},
    total=False,
)

ClientDescribeMetricFiltersResponsemetricFiltersTypeDef = TypedDict(
    "ClientDescribeMetricFiltersResponsemetricFiltersTypeDef",
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

ClientDescribeMetricFiltersResponseTypeDef = TypedDict(
    "ClientDescribeMetricFiltersResponseTypeDef",
    {
        "metricFilters": List[ClientDescribeMetricFiltersResponsemetricFiltersTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeQueriesResponsequeriesTypeDef = TypedDict(
    "ClientDescribeQueriesResponsequeriesTypeDef",
    {
        "queryId": str,
        "queryString": str,
        "status": Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"],
        "createTime": int,
        "logGroupName": str,
    },
    total=False,
)

ClientDescribeQueriesResponseTypeDef = TypedDict(
    "ClientDescribeQueriesResponseTypeDef",
    {"queries": List[ClientDescribeQueriesResponsequeriesTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef = TypedDict(
    "ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef",
    {"policyName": str, "policyDocument": str, "lastUpdatedTime": int},
    total=False,
)

ClientDescribeResourcePoliciesResponseTypeDef = TypedDict(
    "ClientDescribeResourcePoliciesResponseTypeDef",
    {
        "resourcePolicies": List[ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef = TypedDict(
    "ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef",
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

ClientDescribeSubscriptionFiltersResponseTypeDef = TypedDict(
    "ClientDescribeSubscriptionFiltersResponseTypeDef",
    {
        "subscriptionFilters": List[
            ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientFilterLogEventsResponseeventsTypeDef = TypedDict(
    "ClientFilterLogEventsResponseeventsTypeDef",
    {"logStreamName": str, "timestamp": int, "message": str, "ingestionTime": int, "eventId": str},
    total=False,
)

ClientFilterLogEventsResponsesearchedLogStreamsTypeDef = TypedDict(
    "ClientFilterLogEventsResponsesearchedLogStreamsTypeDef",
    {"logStreamName": str, "searchedCompletely": bool},
    total=False,
)

ClientFilterLogEventsResponseTypeDef = TypedDict(
    "ClientFilterLogEventsResponseTypeDef",
    {
        "events": List[ClientFilterLogEventsResponseeventsTypeDef],
        "searchedLogStreams": List[ClientFilterLogEventsResponsesearchedLogStreamsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientGetLogEventsResponseeventsTypeDef = TypedDict(
    "ClientGetLogEventsResponseeventsTypeDef",
    {"timestamp": int, "message": str, "ingestionTime": int},
    total=False,
)

ClientGetLogEventsResponseTypeDef = TypedDict(
    "ClientGetLogEventsResponseTypeDef",
    {
        "events": List[ClientGetLogEventsResponseeventsTypeDef],
        "nextForwardToken": str,
        "nextBackwardToken": str,
    },
    total=False,
)

ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef = TypedDict(
    "ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef",
    {"name": str, "percent": int},
    total=False,
)

ClientGetLogGroupFieldsResponseTypeDef = TypedDict(
    "ClientGetLogGroupFieldsResponseTypeDef",
    {"logGroupFields": List[ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef]},
    total=False,
)

ClientGetLogRecordResponseTypeDef = TypedDict(
    "ClientGetLogRecordResponseTypeDef", {"logRecord": Dict[str, str]}, total=False
)

ClientGetQueryResultsResponseresultsTypeDef = TypedDict(
    "ClientGetQueryResultsResponseresultsTypeDef", {"field": str, "value": str}, total=False
)

ClientGetQueryResultsResponsestatisticsTypeDef = TypedDict(
    "ClientGetQueryResultsResponsestatisticsTypeDef",
    {"recordsMatched": float, "recordsScanned": float, "bytesScanned": float},
    total=False,
)

ClientGetQueryResultsResponseTypeDef = TypedDict(
    "ClientGetQueryResultsResponseTypeDef",
    {
        "results": List[List[ClientGetQueryResultsResponseresultsTypeDef]],
        "statistics": ClientGetQueryResultsResponsestatisticsTypeDef,
        "status": Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"],
    },
    total=False,
)

ClientListTagsLogGroupResponseTypeDef = TypedDict(
    "ClientListTagsLogGroupResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientPutDestinationResponsedestinationTypeDef = TypedDict(
    "ClientPutDestinationResponsedestinationTypeDef",
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

ClientPutDestinationResponseTypeDef = TypedDict(
    "ClientPutDestinationResponseTypeDef",
    {"destination": ClientPutDestinationResponsedestinationTypeDef},
    total=False,
)

_RequiredClientPutLogEventsLogEventsTypeDef = TypedDict(
    "_RequiredClientPutLogEventsLogEventsTypeDef", {"timestamp": int}
)
_OptionalClientPutLogEventsLogEventsTypeDef = TypedDict(
    "_OptionalClientPutLogEventsLogEventsTypeDef", {"message": str}, total=False
)


class ClientPutLogEventsLogEventsTypeDef(
    _RequiredClientPutLogEventsLogEventsTypeDef, _OptionalClientPutLogEventsLogEventsTypeDef
):
    pass


ClientPutLogEventsResponserejectedLogEventsInfoTypeDef = TypedDict(
    "ClientPutLogEventsResponserejectedLogEventsInfoTypeDef",
    {
        "tooNewLogEventStartIndex": int,
        "tooOldLogEventEndIndex": int,
        "expiredLogEventEndIndex": int,
    },
    total=False,
)

ClientPutLogEventsResponseTypeDef = TypedDict(
    "ClientPutLogEventsResponseTypeDef",
    {
        "nextSequenceToken": str,
        "rejectedLogEventsInfo": ClientPutLogEventsResponserejectedLogEventsInfoTypeDef,
    },
    total=False,
)

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
    pass


ClientPutResourcePolicyResponseresourcePolicyTypeDef = TypedDict(
    "ClientPutResourcePolicyResponseresourcePolicyTypeDef",
    {"policyName": str, "policyDocument": str, "lastUpdatedTime": int},
    total=False,
)

ClientPutResourcePolicyResponseTypeDef = TypedDict(
    "ClientPutResourcePolicyResponseTypeDef",
    {"resourcePolicy": ClientPutResourcePolicyResponseresourcePolicyTypeDef},
    total=False,
)

ClientStartQueryResponseTypeDef = TypedDict(
    "ClientStartQueryResponseTypeDef", {"queryId": str}, total=False
)

ClientStopQueryResponseTypeDef = TypedDict(
    "ClientStopQueryResponseTypeDef", {"success": bool}, total=False
)

ClientTestMetricFilterResponsematchesTypeDef = TypedDict(
    "ClientTestMetricFilterResponsematchesTypeDef",
    {"eventNumber": int, "eventMessage": str, "extractedValues": Dict[str, str]},
    total=False,
)

ClientTestMetricFilterResponseTypeDef = TypedDict(
    "ClientTestMetricFilterResponseTypeDef",
    {"matches": List[ClientTestMetricFilterResponsematchesTypeDef]},
    total=False,
)

DescribeDestinationsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeDestinationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeDestinationsPaginateResponsedestinationsTypeDef = TypedDict(
    "DescribeDestinationsPaginateResponsedestinationsTypeDef",
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

DescribeDestinationsPaginateResponseTypeDef = TypedDict(
    "DescribeDestinationsPaginateResponseTypeDef",
    {
        "destinations": List[DescribeDestinationsPaginateResponsedestinationsTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeExportTasksPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeExportTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef = TypedDict(
    "DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef",
    {"creationTime": int, "completionTime": int},
    total=False,
)

DescribeExportTasksPaginateResponseexportTasksstatusTypeDef = TypedDict(
    "DescribeExportTasksPaginateResponseexportTasksstatusTypeDef",
    {
        "code": Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"],
        "message": str,
    },
    total=False,
)

DescribeExportTasksPaginateResponseexportTasksTypeDef = TypedDict(
    "DescribeExportTasksPaginateResponseexportTasksTypeDef",
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

DescribeExportTasksPaginateResponseTypeDef = TypedDict(
    "DescribeExportTasksPaginateResponseTypeDef",
    {"exportTasks": List[DescribeExportTasksPaginateResponseexportTasksTypeDef], "NextToken": str},
    total=False,
)

DescribeLogGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeLogGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeLogGroupsPaginateResponselogGroupsTypeDef = TypedDict(
    "DescribeLogGroupsPaginateResponselogGroupsTypeDef",
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

DescribeLogGroupsPaginateResponseTypeDef = TypedDict(
    "DescribeLogGroupsPaginateResponseTypeDef",
    {"logGroups": List[DescribeLogGroupsPaginateResponselogGroupsTypeDef], "NextToken": str},
    total=False,
)

DescribeLogStreamsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeLogStreamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeLogStreamsPaginateResponselogStreamsTypeDef = TypedDict(
    "DescribeLogStreamsPaginateResponselogStreamsTypeDef",
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

DescribeLogStreamsPaginateResponseTypeDef = TypedDict(
    "DescribeLogStreamsPaginateResponseTypeDef",
    {"logStreams": List[DescribeLogStreamsPaginateResponselogStreamsTypeDef], "NextToken": str},
    total=False,
)

DescribeMetricFiltersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeMetricFiltersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef = TypedDict(
    "DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef",
    {"metricName": str, "metricNamespace": str, "metricValue": str, "defaultValue": float},
    total=False,
)

DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef = TypedDict(
    "DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef",
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

DescribeMetricFiltersPaginateResponseTypeDef = TypedDict(
    "DescribeMetricFiltersPaginateResponseTypeDef",
    {
        "metricFilters": List[DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeQueriesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeQueriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeQueriesPaginateResponsequeriesTypeDef = TypedDict(
    "DescribeQueriesPaginateResponsequeriesTypeDef",
    {
        "queryId": str,
        "queryString": str,
        "status": Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"],
        "createTime": int,
        "logGroupName": str,
    },
    total=False,
)

DescribeQueriesPaginateResponseTypeDef = TypedDict(
    "DescribeQueriesPaginateResponseTypeDef",
    {"queries": List[DescribeQueriesPaginateResponsequeriesTypeDef], "NextToken": str},
    total=False,
)

DescribeResourcePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeResourcePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef = TypedDict(
    "DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef",
    {"policyName": str, "policyDocument": str, "lastUpdatedTime": int},
    total=False,
)

DescribeResourcePoliciesPaginateResponseTypeDef = TypedDict(
    "DescribeResourcePoliciesPaginateResponseTypeDef",
    {
        "resourcePolicies": List[DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef = TypedDict(
    "DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef",
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

DescribeSubscriptionFiltersPaginateResponseTypeDef = TypedDict(
    "DescribeSubscriptionFiltersPaginateResponseTypeDef",
    {
        "subscriptionFilters": List[
            DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

FilterLogEventsPaginatePaginationConfigTypeDef = TypedDict(
    "FilterLogEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

FilterLogEventsPaginateResponseeventsTypeDef = TypedDict(
    "FilterLogEventsPaginateResponseeventsTypeDef",
    {"logStreamName": str, "timestamp": int, "message": str, "ingestionTime": int, "eventId": str},
    total=False,
)

FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef = TypedDict(
    "FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef",
    {"logStreamName": str, "searchedCompletely": bool},
    total=False,
)

FilterLogEventsPaginateResponseTypeDef = TypedDict(
    "FilterLogEventsPaginateResponseTypeDef",
    {
        "events": List[FilterLogEventsPaginateResponseeventsTypeDef],
        "searchedLogStreams": List[FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef],
        "NextToken": str,
    },
    total=False,
)
