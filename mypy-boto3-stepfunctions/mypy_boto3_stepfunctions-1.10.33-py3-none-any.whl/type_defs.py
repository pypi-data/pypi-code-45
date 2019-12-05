"Main interface for stepfunctions service type defs"
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


ClientCreateActivityResponseTypeDef = TypedDict(
    "ClientCreateActivityResponseTypeDef",
    {"activityArn": str, "creationDate": datetime},
    total=False,
)

ClientCreateActivityTagsTypeDef = TypedDict(
    "ClientCreateActivityTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef = TypedDict(
    "ClientCreateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    {"logGroupArn": str},
    total=False,
)

ClientCreateStateMachineLoggingConfigurationdestinationsTypeDef = TypedDict(
    "ClientCreateStateMachineLoggingConfigurationdestinationsTypeDef",
    {
        "cloudWatchLogsLogGroup": ClientCreateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef
    },
    total=False,
)

ClientCreateStateMachineLoggingConfigurationTypeDef = TypedDict(
    "ClientCreateStateMachineLoggingConfigurationTypeDef",
    {
        "level": Literal["ALL", "ERROR", "FATAL", "OFF"],
        "includeExecutionData": bool,
        "destinations": List[ClientCreateStateMachineLoggingConfigurationdestinationsTypeDef],
    },
    total=False,
)

ClientCreateStateMachineResponseTypeDef = TypedDict(
    "ClientCreateStateMachineResponseTypeDef",
    {"stateMachineArn": str, "creationDate": datetime},
    total=False,
)

ClientCreateStateMachineTagsTypeDef = TypedDict(
    "ClientCreateStateMachineTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDescribeActivityResponseTypeDef = TypedDict(
    "ClientDescribeActivityResponseTypeDef",
    {"activityArn": str, "name": str, "creationDate": datetime},
    total=False,
)

ClientDescribeExecutionResponseTypeDef = TypedDict(
    "ClientDescribeExecutionResponseTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"],
        "startDate": datetime,
        "stopDate": datetime,
        "input": str,
        "output": str,
    },
    total=False,
)

ClientDescribeStateMachineForExecutionResponseTypeDef = TypedDict(
    "ClientDescribeStateMachineForExecutionResponseTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "definition": str,
        "roleArn": str,
        "updateDate": datetime,
    },
    total=False,
)

ClientDescribeStateMachineResponseloggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef = TypedDict(
    "ClientDescribeStateMachineResponseloggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    {"logGroupArn": str},
    total=False,
)

ClientDescribeStateMachineResponseloggingConfigurationdestinationsTypeDef = TypedDict(
    "ClientDescribeStateMachineResponseloggingConfigurationdestinationsTypeDef",
    {
        "cloudWatchLogsLogGroup": ClientDescribeStateMachineResponseloggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef
    },
    total=False,
)

ClientDescribeStateMachineResponseloggingConfigurationTypeDef = TypedDict(
    "ClientDescribeStateMachineResponseloggingConfigurationTypeDef",
    {
        "level": Literal["ALL", "ERROR", "FATAL", "OFF"],
        "includeExecutionData": bool,
        "destinations": List[
            ClientDescribeStateMachineResponseloggingConfigurationdestinationsTypeDef
        ],
    },
    total=False,
)

ClientDescribeStateMachineResponseTypeDef = TypedDict(
    "ClientDescribeStateMachineResponseTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "status": Literal["ACTIVE", "DELETING"],
        "definition": str,
        "roleArn": str,
        "type": Literal["STANDARD", "EXPRESS"],
        "creationDate": datetime,
        "loggingConfiguration": ClientDescribeStateMachineResponseloggingConfigurationTypeDef,
    },
    total=False,
)

ClientGetActivityTaskResponseTypeDef = TypedDict(
    "ClientGetActivityTaskResponseTypeDef", {"taskToken": str, "input": str}, total=False
)

ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int, "heartbeatInSeconds": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef",
    {"workerName": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef",
    {"input": str, "roleArn": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef",
    {"length": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef",
    {"name": str, "input": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef",
    {"name": str, "output": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "region": str,
        "parameters": str,
        "timeoutInSeconds": int,
    },
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef",
    {"resourceType": str, "resource": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsTypeDef",
    {
        "timestamp": datetime,
        "type": Literal[
            "ActivityFailed",
            "ActivityScheduled",
            "ActivityScheduleFailed",
            "ActivityStarted",
            "ActivitySucceeded",
            "ActivityTimedOut",
            "ChoiceStateEntered",
            "ChoiceStateExited",
            "ExecutionAborted",
            "ExecutionFailed",
            "ExecutionStarted",
            "ExecutionSucceeded",
            "ExecutionTimedOut",
            "FailStateEntered",
            "LambdaFunctionFailed",
            "LambdaFunctionScheduled",
            "LambdaFunctionScheduleFailed",
            "LambdaFunctionStarted",
            "LambdaFunctionStartFailed",
            "LambdaFunctionSucceeded",
            "LambdaFunctionTimedOut",
            "MapIterationAborted",
            "MapIterationFailed",
            "MapIterationStarted",
            "MapIterationSucceeded",
            "MapStateAborted",
            "MapStateEntered",
            "MapStateExited",
            "MapStateFailed",
            "MapStateStarted",
            "MapStateSucceeded",
            "ParallelStateAborted",
            "ParallelStateEntered",
            "ParallelStateExited",
            "ParallelStateFailed",
            "ParallelStateStarted",
            "ParallelStateSucceeded",
            "PassStateEntered",
            "PassStateExited",
            "SucceedStateEntered",
            "SucceedStateExited",
            "TaskFailed",
            "TaskScheduled",
            "TaskStarted",
            "TaskStartFailed",
            "TaskStateAborted",
            "TaskStateEntered",
            "TaskStateExited",
            "TaskSubmitFailed",
            "TaskSubmitted",
            "TaskSucceeded",
            "TaskTimedOut",
            "WaitStateAborted",
            "WaitStateEntered",
            "WaitStateExited",
        ],
        "id": int,
        "previousEventId": int,
        "activityFailedEventDetails": ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef,
        "activityScheduleFailedEventDetails": ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef,
        "activityScheduledEventDetails": ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef,
        "activityStartedEventDetails": ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef,
        "activitySucceededEventDetails": ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef,
        "activityTimedOutEventDetails": ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef,
        "taskFailedEventDetails": ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef,
        "taskScheduledEventDetails": ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef,
        "taskStartFailedEventDetails": ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef,
        "taskStartedEventDetails": ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef,
        "taskSubmitFailedEventDetails": ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef,
        "taskSubmittedEventDetails": ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef,
        "taskSucceededEventDetails": ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef,
        "taskTimedOutEventDetails": ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef,
        "executionFailedEventDetails": ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef,
        "executionStartedEventDetails": ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef,
        "executionSucceededEventDetails": ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef,
        "executionAbortedEventDetails": ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef,
        "executionTimedOutEventDetails": ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef,
        "mapStateStartedEventDetails": ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef,
        "mapIterationStartedEventDetails": ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef,
        "mapIterationSucceededEventDetails": ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef,
        "mapIterationFailedEventDetails": ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef,
        "mapIterationAbortedEventDetails": ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef,
        "lambdaFunctionFailedEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef,
        "lambdaFunctionScheduleFailedEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef,
        "lambdaFunctionScheduledEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef,
        "lambdaFunctionStartFailedEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef,
        "lambdaFunctionSucceededEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef,
        "lambdaFunctionTimedOutEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef,
        "stateEnteredEventDetails": ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef,
        "stateExitedEventDetails": ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef,
    },
    total=False,
)

ClientGetExecutionHistoryResponseTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseTypeDef",
    {"events": List[ClientGetExecutionHistoryResponseeventsTypeDef], "nextToken": str},
    total=False,
)

ClientListActivitiesResponseactivitiesTypeDef = TypedDict(
    "ClientListActivitiesResponseactivitiesTypeDef",
    {"activityArn": str, "name": str, "creationDate": datetime},
    total=False,
)

ClientListActivitiesResponseTypeDef = TypedDict(
    "ClientListActivitiesResponseTypeDef",
    {"activities": List[ClientListActivitiesResponseactivitiesTypeDef], "nextToken": str},
    total=False,
)

ClientListExecutionsResponseexecutionsTypeDef = TypedDict(
    "ClientListExecutionsResponseexecutionsTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"],
        "startDate": datetime,
        "stopDate": datetime,
    },
    total=False,
)

ClientListExecutionsResponseTypeDef = TypedDict(
    "ClientListExecutionsResponseTypeDef",
    {"executions": List[ClientListExecutionsResponseexecutionsTypeDef], "nextToken": str},
    total=False,
)

ClientListStateMachinesResponsestateMachinesTypeDef = TypedDict(
    "ClientListStateMachinesResponsestateMachinesTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "type": Literal["STANDARD", "EXPRESS"],
        "creationDate": datetime,
    },
    total=False,
)

ClientListStateMachinesResponseTypeDef = TypedDict(
    "ClientListStateMachinesResponseTypeDef",
    {"stateMachines": List[ClientListStateMachinesResponsestateMachinesTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)

ClientStartExecutionResponseTypeDef = TypedDict(
    "ClientStartExecutionResponseTypeDef", {"executionArn": str, "startDate": datetime}, total=False
)

ClientStopExecutionResponseTypeDef = TypedDict(
    "ClientStopExecutionResponseTypeDef", {"stopDate": datetime}, total=False
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientUpdateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef = TypedDict(
    "ClientUpdateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    {"logGroupArn": str},
    total=False,
)

ClientUpdateStateMachineLoggingConfigurationdestinationsTypeDef = TypedDict(
    "ClientUpdateStateMachineLoggingConfigurationdestinationsTypeDef",
    {
        "cloudWatchLogsLogGroup": ClientUpdateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef
    },
    total=False,
)

ClientUpdateStateMachineLoggingConfigurationTypeDef = TypedDict(
    "ClientUpdateStateMachineLoggingConfigurationTypeDef",
    {
        "level": Literal["ALL", "ERROR", "FATAL", "OFF"],
        "includeExecutionData": bool,
        "destinations": List[ClientUpdateStateMachineLoggingConfigurationdestinationsTypeDef],
    },
    total=False,
)

ClientUpdateStateMachineResponseTypeDef = TypedDict(
    "ClientUpdateStateMachineResponseTypeDef", {"updateDate": datetime}, total=False
)

GetExecutionHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "GetExecutionHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int, "heartbeatInSeconds": int},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef",
    {"workerName": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef",
    {"input": str, "roleArn": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int},
    total=False,
)

GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef",
    {"length": int},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef",
    {"name": str, "input": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef",
    {"name": str, "output": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "region": str,
        "parameters": str,
        "timeoutInSeconds": int,
    },
    total=False,
)

GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef",
    {"resourceType": str, "resource": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)

GetExecutionHistoryPaginateResponseeventsTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseeventsTypeDef",
    {
        "timestamp": datetime,
        "type": Literal[
            "ActivityFailed",
            "ActivityScheduled",
            "ActivityScheduleFailed",
            "ActivityStarted",
            "ActivitySucceeded",
            "ActivityTimedOut",
            "ChoiceStateEntered",
            "ChoiceStateExited",
            "ExecutionAborted",
            "ExecutionFailed",
            "ExecutionStarted",
            "ExecutionSucceeded",
            "ExecutionTimedOut",
            "FailStateEntered",
            "LambdaFunctionFailed",
            "LambdaFunctionScheduled",
            "LambdaFunctionScheduleFailed",
            "LambdaFunctionStarted",
            "LambdaFunctionStartFailed",
            "LambdaFunctionSucceeded",
            "LambdaFunctionTimedOut",
            "MapIterationAborted",
            "MapIterationFailed",
            "MapIterationStarted",
            "MapIterationSucceeded",
            "MapStateAborted",
            "MapStateEntered",
            "MapStateExited",
            "MapStateFailed",
            "MapStateStarted",
            "MapStateSucceeded",
            "ParallelStateAborted",
            "ParallelStateEntered",
            "ParallelStateExited",
            "ParallelStateFailed",
            "ParallelStateStarted",
            "ParallelStateSucceeded",
            "PassStateEntered",
            "PassStateExited",
            "SucceedStateEntered",
            "SucceedStateExited",
            "TaskFailed",
            "TaskScheduled",
            "TaskStarted",
            "TaskStartFailed",
            "TaskStateAborted",
            "TaskStateEntered",
            "TaskStateExited",
            "TaskSubmitFailed",
            "TaskSubmitted",
            "TaskSucceeded",
            "TaskTimedOut",
            "WaitStateAborted",
            "WaitStateEntered",
            "WaitStateExited",
        ],
        "id": int,
        "previousEventId": int,
        "activityFailedEventDetails": GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef,
        "activityScheduleFailedEventDetails": GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef,
        "activityScheduledEventDetails": GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef,
        "activityStartedEventDetails": GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef,
        "activitySucceededEventDetails": GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef,
        "activityTimedOutEventDetails": GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef,
        "taskFailedEventDetails": GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef,
        "taskScheduledEventDetails": GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef,
        "taskStartFailedEventDetails": GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef,
        "taskStartedEventDetails": GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef,
        "taskSubmitFailedEventDetails": GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef,
        "taskSubmittedEventDetails": GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef,
        "taskSucceededEventDetails": GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef,
        "taskTimedOutEventDetails": GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef,
        "executionFailedEventDetails": GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef,
        "executionStartedEventDetails": GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef,
        "executionSucceededEventDetails": GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef,
        "executionAbortedEventDetails": GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef,
        "executionTimedOutEventDetails": GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef,
        "mapStateStartedEventDetails": GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef,
        "mapIterationStartedEventDetails": GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef,
        "mapIterationSucceededEventDetails": GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef,
        "mapIterationFailedEventDetails": GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef,
        "mapIterationAbortedEventDetails": GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef,
        "lambdaFunctionFailedEventDetails": GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef,
        "lambdaFunctionScheduleFailedEventDetails": GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef,
        "lambdaFunctionScheduledEventDetails": GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef,
        "lambdaFunctionStartFailedEventDetails": GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef,
        "lambdaFunctionSucceededEventDetails": GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef,
        "lambdaFunctionTimedOutEventDetails": GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef,
        "stateEnteredEventDetails": GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef,
        "stateExitedEventDetails": GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef,
    },
    total=False,
)

GetExecutionHistoryPaginateResponseTypeDef = TypedDict(
    "GetExecutionHistoryPaginateResponseTypeDef",
    {"events": List[GetExecutionHistoryPaginateResponseeventsTypeDef], "NextToken": str},
    total=False,
)

ListActivitiesPaginatePaginationConfigTypeDef = TypedDict(
    "ListActivitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListActivitiesPaginateResponseactivitiesTypeDef = TypedDict(
    "ListActivitiesPaginateResponseactivitiesTypeDef",
    {"activityArn": str, "name": str, "creationDate": datetime},
    total=False,
)

ListActivitiesPaginateResponseTypeDef = TypedDict(
    "ListActivitiesPaginateResponseTypeDef",
    {"activities": List[ListActivitiesPaginateResponseactivitiesTypeDef], "NextToken": str},
    total=False,
)

ListExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListExecutionsPaginateResponseexecutionsTypeDef = TypedDict(
    "ListExecutionsPaginateResponseexecutionsTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"],
        "startDate": datetime,
        "stopDate": datetime,
    },
    total=False,
)

ListExecutionsPaginateResponseTypeDef = TypedDict(
    "ListExecutionsPaginateResponseTypeDef",
    {"executions": List[ListExecutionsPaginateResponseexecutionsTypeDef], "NextToken": str},
    total=False,
)

ListStateMachinesPaginatePaginationConfigTypeDef = TypedDict(
    "ListStateMachinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListStateMachinesPaginateResponsestateMachinesTypeDef = TypedDict(
    "ListStateMachinesPaginateResponsestateMachinesTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "type": Literal["STANDARD", "EXPRESS"],
        "creationDate": datetime,
    },
    total=False,
)

ListStateMachinesPaginateResponseTypeDef = TypedDict(
    "ListStateMachinesPaginateResponseTypeDef",
    {
        "stateMachines": List[ListStateMachinesPaginateResponsestateMachinesTypeDef],
        "NextToken": str,
    },
    total=False,
)
