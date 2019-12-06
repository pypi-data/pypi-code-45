"Main interface for swf service type defs"
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


ClientCountClosedWorkflowExecutionsCloseStatusFilterTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsCloseStatusFilterTypeDef",
    {
        "status": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ]
    },
    total=False,
)

ClientCountClosedWorkflowExecutionsCloseTimeFilterTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsCloseTimeFilterTypeDef",
    {"oldestDate": datetime, "latestDate": datetime},
    total=False,
)

ClientCountClosedWorkflowExecutionsExecutionFilterTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsExecutionFilterTypeDef", {"workflowId": str}, total=False
)

ClientCountClosedWorkflowExecutionsResponseTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsResponseTypeDef",
    {"count": int, "truncated": bool},
    total=False,
)

ClientCountClosedWorkflowExecutionsStartTimeFilterTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsStartTimeFilterTypeDef",
    {"oldestDate": datetime, "latestDate": datetime},
    total=False,
)

ClientCountClosedWorkflowExecutionsTagFilterTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsTagFilterTypeDef", {"tag": str}, total=False
)

ClientCountClosedWorkflowExecutionsTypeFilterTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsTypeFilterTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientCountOpenWorkflowExecutionsExecutionFilterTypeDef = TypedDict(
    "ClientCountOpenWorkflowExecutionsExecutionFilterTypeDef", {"workflowId": str}, total=False
)

ClientCountOpenWorkflowExecutionsResponseTypeDef = TypedDict(
    "ClientCountOpenWorkflowExecutionsResponseTypeDef",
    {"count": int, "truncated": bool},
    total=False,
)

_RequiredClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef = TypedDict(
    "_RequiredClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef", {"oldestDate": datetime}
)
_OptionalClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef = TypedDict(
    "_OptionalClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef",
    {"latestDate": datetime},
    total=False,
)


class ClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef(
    _RequiredClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef,
    _OptionalClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef,
):
    pass


ClientCountOpenWorkflowExecutionsTagFilterTypeDef = TypedDict(
    "ClientCountOpenWorkflowExecutionsTagFilterTypeDef", {"tag": str}, total=False
)

ClientCountOpenWorkflowExecutionsTypeFilterTypeDef = TypedDict(
    "ClientCountOpenWorkflowExecutionsTypeFilterTypeDef", {"name": str, "version": str}, total=False
)

ClientCountPendingActivityTasksResponseTypeDef = TypedDict(
    "ClientCountPendingActivityTasksResponseTypeDef", {"count": int, "truncated": bool}, total=False
)

ClientCountPendingActivityTasksTaskListTypeDef = TypedDict(
    "ClientCountPendingActivityTasksTaskListTypeDef", {"name": str}
)

ClientCountPendingDecisionTasksResponseTypeDef = TypedDict(
    "ClientCountPendingDecisionTasksResponseTypeDef", {"count": int, "truncated": bool}, total=False
)

ClientCountPendingDecisionTasksTaskListTypeDef = TypedDict(
    "ClientCountPendingDecisionTasksTaskListTypeDef", {"name": str}
)

_RequiredClientDeprecateActivityTypeActivityTypeTypeDef = TypedDict(
    "_RequiredClientDeprecateActivityTypeActivityTypeTypeDef", {"name": str}
)
_OptionalClientDeprecateActivityTypeActivityTypeTypeDef = TypedDict(
    "_OptionalClientDeprecateActivityTypeActivityTypeTypeDef", {"version": str}, total=False
)


class ClientDeprecateActivityTypeActivityTypeTypeDef(
    _RequiredClientDeprecateActivityTypeActivityTypeTypeDef,
    _OptionalClientDeprecateActivityTypeActivityTypeTypeDef,
):
    pass


_RequiredClientDeprecateWorkflowTypeWorkflowTypeTypeDef = TypedDict(
    "_RequiredClientDeprecateWorkflowTypeWorkflowTypeTypeDef", {"name": str}
)
_OptionalClientDeprecateWorkflowTypeWorkflowTypeTypeDef = TypedDict(
    "_OptionalClientDeprecateWorkflowTypeWorkflowTypeTypeDef", {"version": str}, total=False
)


class ClientDeprecateWorkflowTypeWorkflowTypeTypeDef(
    _RequiredClientDeprecateWorkflowTypeWorkflowTypeTypeDef,
    _OptionalClientDeprecateWorkflowTypeWorkflowTypeTypeDef,
):
    pass


_RequiredClientDescribeActivityTypeActivityTypeTypeDef = TypedDict(
    "_RequiredClientDescribeActivityTypeActivityTypeTypeDef", {"name": str}
)
_OptionalClientDescribeActivityTypeActivityTypeTypeDef = TypedDict(
    "_OptionalClientDescribeActivityTypeActivityTypeTypeDef", {"version": str}, total=False
)


class ClientDescribeActivityTypeActivityTypeTypeDef(
    _RequiredClientDescribeActivityTypeActivityTypeTypeDef,
    _OptionalClientDescribeActivityTypeActivityTypeTypeDef,
):
    pass


ClientDescribeActivityTypeResponseconfigurationdefaultTaskListTypeDef = TypedDict(
    "ClientDescribeActivityTypeResponseconfigurationdefaultTaskListTypeDef",
    {"name": str},
    total=False,
)

ClientDescribeActivityTypeResponseconfigurationTypeDef = TypedDict(
    "ClientDescribeActivityTypeResponseconfigurationTypeDef",
    {
        "defaultTaskStartToCloseTimeout": str,
        "defaultTaskHeartbeatTimeout": str,
        "defaultTaskList": ClientDescribeActivityTypeResponseconfigurationdefaultTaskListTypeDef,
        "defaultTaskPriority": str,
        "defaultTaskScheduleToStartTimeout": str,
        "defaultTaskScheduleToCloseTimeout": str,
    },
    total=False,
)

ClientDescribeActivityTypeResponsetypeInfoactivityTypeTypeDef = TypedDict(
    "ClientDescribeActivityTypeResponsetypeInfoactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientDescribeActivityTypeResponsetypeInfoTypeDef = TypedDict(
    "ClientDescribeActivityTypeResponsetypeInfoTypeDef",
    {
        "activityType": ClientDescribeActivityTypeResponsetypeInfoactivityTypeTypeDef,
        "status": Literal["REGISTERED", "DEPRECATED"],
        "description": str,
        "creationDate": datetime,
        "deprecationDate": datetime,
    },
    total=False,
)

ClientDescribeActivityTypeResponseTypeDef = TypedDict(
    "ClientDescribeActivityTypeResponseTypeDef",
    {
        "typeInfo": ClientDescribeActivityTypeResponsetypeInfoTypeDef,
        "configuration": ClientDescribeActivityTypeResponseconfigurationTypeDef,
    },
    total=False,
)

ClientDescribeDomainResponseconfigurationTypeDef = TypedDict(
    "ClientDescribeDomainResponseconfigurationTypeDef",
    {"workflowExecutionRetentionPeriodInDays": str},
    total=False,
)

ClientDescribeDomainResponsedomainInfoTypeDef = TypedDict(
    "ClientDescribeDomainResponsedomainInfoTypeDef",
    {"name": str, "status": Literal["REGISTERED", "DEPRECATED"], "description": str, "arn": str},
    total=False,
)

ClientDescribeDomainResponseTypeDef = TypedDict(
    "ClientDescribeDomainResponseTypeDef",
    {
        "domainInfo": ClientDescribeDomainResponsedomainInfoTypeDef,
        "configuration": ClientDescribeDomainResponseconfigurationTypeDef,
    },
    total=False,
)

_RequiredClientDescribeWorkflowExecutionExecutionTypeDef = TypedDict(
    "_RequiredClientDescribeWorkflowExecutionExecutionTypeDef", {"workflowId": str}
)
_OptionalClientDescribeWorkflowExecutionExecutionTypeDef = TypedDict(
    "_OptionalClientDescribeWorkflowExecutionExecutionTypeDef", {"runId": str}, total=False
)


class ClientDescribeWorkflowExecutionExecutionTypeDef(
    _RequiredClientDescribeWorkflowExecutionExecutionTypeDef,
    _OptionalClientDescribeWorkflowExecutionExecutionTypeDef,
):
    pass


ClientDescribeWorkflowExecutionResponseexecutionConfigurationtaskListTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseexecutionConfigurationtaskListTypeDef",
    {"name": str},
    total=False,
)

ClientDescribeWorkflowExecutionResponseexecutionConfigurationTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseexecutionConfigurationTypeDef",
    {
        "taskStartToCloseTimeout": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientDescribeWorkflowExecutionResponseexecutionConfigurationtaskListTypeDef,
        "taskPriority": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "lambdaRole": str,
    },
    total=False,
)

ClientDescribeWorkflowExecutionResponseexecutionInfoexecutionTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseexecutionInfoexecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientDescribeWorkflowExecutionResponseexecutionInfoparentTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseexecutionInfoparentTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientDescribeWorkflowExecutionResponseexecutionInfoworkflowTypeTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseexecutionInfoworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientDescribeWorkflowExecutionResponseexecutionInfoTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseexecutionInfoTypeDef",
    {
        "execution": ClientDescribeWorkflowExecutionResponseexecutionInfoexecutionTypeDef,
        "workflowType": ClientDescribeWorkflowExecutionResponseexecutionInfoworkflowTypeTypeDef,
        "startTimestamp": datetime,
        "closeTimestamp": datetime,
        "executionStatus": Literal["OPEN", "CLOSED"],
        "closeStatus": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ],
        "parent": ClientDescribeWorkflowExecutionResponseexecutionInfoparentTypeDef,
        "tagList": List[str],
        "cancelRequested": bool,
    },
    total=False,
)

ClientDescribeWorkflowExecutionResponseopenCountsTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseopenCountsTypeDef",
    {
        "openActivityTasks": int,
        "openDecisionTasks": int,
        "openTimers": int,
        "openChildWorkflowExecutions": int,
        "openLambdaFunctions": int,
    },
    total=False,
)

ClientDescribeWorkflowExecutionResponseTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseTypeDef",
    {
        "executionInfo": ClientDescribeWorkflowExecutionResponseexecutionInfoTypeDef,
        "executionConfiguration": ClientDescribeWorkflowExecutionResponseexecutionConfigurationTypeDef,
        "openCounts": ClientDescribeWorkflowExecutionResponseopenCountsTypeDef,
        "latestActivityTaskTimestamp": datetime,
        "latestExecutionContext": str,
    },
    total=False,
)

ClientDescribeWorkflowTypeResponseconfigurationdefaultTaskListTypeDef = TypedDict(
    "ClientDescribeWorkflowTypeResponseconfigurationdefaultTaskListTypeDef",
    {"name": str},
    total=False,
)

ClientDescribeWorkflowTypeResponseconfigurationTypeDef = TypedDict(
    "ClientDescribeWorkflowTypeResponseconfigurationTypeDef",
    {
        "defaultTaskStartToCloseTimeout": str,
        "defaultExecutionStartToCloseTimeout": str,
        "defaultTaskList": ClientDescribeWorkflowTypeResponseconfigurationdefaultTaskListTypeDef,
        "defaultTaskPriority": str,
        "defaultChildPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "defaultLambdaRole": str,
    },
    total=False,
)

ClientDescribeWorkflowTypeResponsetypeInfoworkflowTypeTypeDef = TypedDict(
    "ClientDescribeWorkflowTypeResponsetypeInfoworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientDescribeWorkflowTypeResponsetypeInfoTypeDef = TypedDict(
    "ClientDescribeWorkflowTypeResponsetypeInfoTypeDef",
    {
        "workflowType": ClientDescribeWorkflowTypeResponsetypeInfoworkflowTypeTypeDef,
        "status": Literal["REGISTERED", "DEPRECATED"],
        "description": str,
        "creationDate": datetime,
        "deprecationDate": datetime,
    },
    total=False,
)

ClientDescribeWorkflowTypeResponseTypeDef = TypedDict(
    "ClientDescribeWorkflowTypeResponseTypeDef",
    {
        "typeInfo": ClientDescribeWorkflowTypeResponsetypeInfoTypeDef,
        "configuration": ClientDescribeWorkflowTypeResponseconfigurationTypeDef,
    },
    total=False,
)

_RequiredClientDescribeWorkflowTypeWorkflowTypeTypeDef = TypedDict(
    "_RequiredClientDescribeWorkflowTypeWorkflowTypeTypeDef", {"name": str}
)
_OptionalClientDescribeWorkflowTypeWorkflowTypeTypeDef = TypedDict(
    "_OptionalClientDescribeWorkflowTypeWorkflowTypeTypeDef", {"version": str}, total=False
)


class ClientDescribeWorkflowTypeWorkflowTypeTypeDef(
    _RequiredClientDescribeWorkflowTypeWorkflowTypeTypeDef,
    _OptionalClientDescribeWorkflowTypeWorkflowTypeTypeDef,
):
    pass


_RequiredClientGetWorkflowExecutionHistoryExecutionTypeDef = TypedDict(
    "_RequiredClientGetWorkflowExecutionHistoryExecutionTypeDef", {"workflowId": str}
)
_OptionalClientGetWorkflowExecutionHistoryExecutionTypeDef = TypedDict(
    "_OptionalClientGetWorkflowExecutionHistoryExecutionTypeDef", {"runId": str}, total=False
)


class ClientGetWorkflowExecutionHistoryExecutionTypeDef(
    _RequiredClientGetWorkflowExecutionHistoryExecutionTypeDef,
    _OptionalClientGetWorkflowExecutionHistoryExecutionTypeDef,
):
    pass


ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef",
    {"decisionTaskCompletedEventId": int, "activityId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCanceledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCanceledEventAttributesTypeDef",
    {
        "details": str,
        "scheduledEventId": int,
        "startedEventId": int,
        "latestCancelRequestedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCompletedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCompletedEventAttributesTypeDef",
    {"result": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskFailedEventAttributesTypeDef",
    {"reason": str, "details": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesTypeDef",
    {
        "activityType": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef,
        "activityId": str,
        "input": str,
        "control": str,
        "scheduleToStartTimeout": str,
        "scheduleToCloseTimeout": str,
        "startToCloseTimeout": str,
        "taskList": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef,
        "taskPriority": str,
        "decisionTaskCompletedEventId": int,
        "heartbeatTimeout": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskStartedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskStartedEventAttributesTypeDef",
    {"identity": str, "scheduledEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskTimedOutEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskTimedOutEventAttributesTypeDef",
    {
        "timeoutType": Literal[
            "START_TO_CLOSE", "SCHEDULE_TO_START", "SCHEDULE_TO_CLOSE", "HEARTBEAT"
        ],
        "scheduledEventId": int,
        "startedEventId": int,
        "details": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventscancelTimerFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventscancelTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal["TIMER_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef,
        "details": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef,
        "result": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef,
        "reason": str,
        "details": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef,
        "timeoutType": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal[
            "UNHANDLED_DECISION",
            "WORKFLOW_TYPE_DEPRECATED",
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskCompletedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskCompletedEventAttributesTypeDef",
    {"executionContext": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributesTypeDef",
    {
        "taskList": ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef,
        "taskPriority": str,
        "startToCloseTimeout": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskStartedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskStartedEventAttributesTypeDef",
    {"identity": str, "scheduledEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskTimedOutEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskTimedOutEventAttributesTypeDef",
    {"timeoutType": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionCompletedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionCompletedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "result": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "reason": str, "details": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionScheduledEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "control": str,
        "input": str,
        "startToCloseTimeout": str,
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionStartedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionStartedEventAttributesTypeDef",
    {"scheduledEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionTimedOutEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionTimedOutEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "timeoutType": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsmarkerRecordedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsmarkerRecordedEventAttributesTypeDef",
    {"markerName": str, "details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsrecordMarkerFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsrecordMarkerFailedEventAttributesTypeDef",
    {"markerName": str, "cause": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef",
    {
        "activityId": str,
        "cause": Literal["ACTIVITY_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"workflowId": str, "runId": str, "decisionTaskCompletedEventId": int, "control": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef",
    {
        "activityType": ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef,
        "activityId": str,
        "cause": Literal[
            "ACTIVITY_TYPE_DEPRECATED",
            "ACTIVITY_TYPE_DOES_NOT_EXIST",
            "ACTIVITY_ID_ALREADY_IN_USE",
            "OPEN_ACTIVITIES_LIMIT_EXCEEDED",
            "ACTIVITY_CREATION_RATE_EXCEEDED",
            "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED",
            "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "cause": Literal[
            "ID_ALREADY_IN_USE",
            "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED",
            "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED",
            "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "signalName": str,
        "input": str,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef,
        "cause": Literal[
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "WORKFLOW_TYPE_DEPRECATED",
            "OPEN_CHILDREN_LIMIT_EXCEEDED",
            "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
            "CHILD_CREATION_RATE_EXCEEDED",
            "WORKFLOW_ALREADY_RUNNING",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "workflowId": str,
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef,
        "control": str,
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef,
        "taskPriority": str,
        "decisionTaskCompletedEventId": int,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskStartToCloseTimeout": str,
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "cause": str, "message": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartTimerFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal[
            "TIMER_ID_ALREADY_IN_USE",
            "OPEN_TIMERS_LIMIT_EXCEEDED",
            "TIMER_CREATION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventstimerCanceledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventstimerCanceledEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventstimerFiredEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventstimerFiredEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventstimerStartedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventstimerStartedEventAttributesTypeDef",
    {
        "timerId": str,
        "control": str,
        "startToFireTimeout": str,
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "externalWorkflowExecution": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
        "cause": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCanceledEventAttributesTypeDef",
    {"details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCompletedEventAttributesTypeDef",
    {"result": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "input": str,
        "decisionTaskCompletedEventId": int,
        "newExecutionRunId": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "tagList": List[str],
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef,
        "lambdaRole": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionFailedEventAttributesTypeDef",
    {"reason": str, "details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesTypeDef",
    {
        "signalName": str,
        "input": str,
        "externalWorkflowExecution": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskList": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef,
        "taskPriority": str,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef,
        "tagList": List[str],
        "continuedExecutionRunId": str,
        "parentWorkflowExecution": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef,
        "parentInitiatedEventId": int,
        "lambdaRole": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "reason": str,
        "details": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "cause": Literal["CHILD_POLICY_APPLIED", "EVENT_LIMIT_EXCEEDED", "OPERATOR_INITIATED"],
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef",
    {"timeoutType": str, "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"]},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsTypeDef",
    {
        "eventTimestamp": datetime,
        "eventType": Literal[
            "WorkflowExecutionStarted",
            "WorkflowExecutionCancelRequested",
            "WorkflowExecutionCompleted",
            "CompleteWorkflowExecutionFailed",
            "WorkflowExecutionFailed",
            "FailWorkflowExecutionFailed",
            "WorkflowExecutionTimedOut",
            "WorkflowExecutionCanceled",
            "CancelWorkflowExecutionFailed",
            "WorkflowExecutionContinuedAsNew",
            "ContinueAsNewWorkflowExecutionFailed",
            "WorkflowExecutionTerminated",
            "DecisionTaskScheduled",
            "DecisionTaskStarted",
            "DecisionTaskCompleted",
            "DecisionTaskTimedOut",
            "ActivityTaskScheduled",
            "ScheduleActivityTaskFailed",
            "ActivityTaskStarted",
            "ActivityTaskCompleted",
            "ActivityTaskFailed",
            "ActivityTaskTimedOut",
            "ActivityTaskCanceled",
            "ActivityTaskCancelRequested",
            "RequestCancelActivityTaskFailed",
            "WorkflowExecutionSignaled",
            "MarkerRecorded",
            "RecordMarkerFailed",
            "TimerStarted",
            "StartTimerFailed",
            "TimerFired",
            "TimerCanceled",
            "CancelTimerFailed",
            "StartChildWorkflowExecutionInitiated",
            "StartChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionStarted",
            "ChildWorkflowExecutionCompleted",
            "ChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionTimedOut",
            "ChildWorkflowExecutionCanceled",
            "ChildWorkflowExecutionTerminated",
            "SignalExternalWorkflowExecutionInitiated",
            "SignalExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionSignaled",
            "RequestCancelExternalWorkflowExecutionInitiated",
            "RequestCancelExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionCancelRequested",
            "LambdaFunctionScheduled",
            "LambdaFunctionStarted",
            "LambdaFunctionCompleted",
            "LambdaFunctionFailed",
            "LambdaFunctionTimedOut",
            "ScheduleLambdaFunctionFailed",
            "StartLambdaFunctionFailed",
        ],
        "eventId": int,
        "workflowExecutionStartedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesTypeDef,
        "workflowExecutionCompletedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCompletedEventAttributesTypeDef,
        "completeWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionFailedEventAttributesTypeDef,
        "failWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTimedOutEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef,
        "workflowExecutionCanceledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCanceledEventAttributesTypeDef,
        "cancelWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionContinuedAsNewEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef,
        "continueAsNewWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTerminatedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef,
        "workflowExecutionCancelRequestedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef,
        "decisionTaskScheduledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributesTypeDef,
        "decisionTaskStartedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskStartedEventAttributesTypeDef,
        "decisionTaskCompletedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskCompletedEventAttributesTypeDef,
        "decisionTaskTimedOutEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskTimedOutEventAttributesTypeDef,
        "activityTaskScheduledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesTypeDef,
        "activityTaskStartedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskStartedEventAttributesTypeDef,
        "activityTaskCompletedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCompletedEventAttributesTypeDef,
        "activityTaskFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskFailedEventAttributesTypeDef,
        "activityTaskTimedOutEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskTimedOutEventAttributesTypeDef,
        "activityTaskCanceledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCanceledEventAttributesTypeDef,
        "activityTaskCancelRequestedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef,
        "workflowExecutionSignaledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesTypeDef,
        "markerRecordedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsmarkerRecordedEventAttributesTypeDef,
        "recordMarkerFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsrecordMarkerFailedEventAttributesTypeDef,
        "timerStartedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventstimerStartedEventAttributesTypeDef,
        "timerFiredEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventstimerFiredEventAttributesTypeDef,
        "timerCanceledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventstimerCanceledEventAttributesTypeDef,
        "startChildWorkflowExecutionInitiatedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef,
        "childWorkflowExecutionStartedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef,
        "childWorkflowExecutionCompletedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef,
        "childWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef,
        "childWorkflowExecutionTimedOutEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef,
        "childWorkflowExecutionCanceledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef,
        "childWorkflowExecutionTerminatedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef,
        "signalExternalWorkflowExecutionInitiatedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "externalWorkflowExecutionSignaledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef,
        "signalExternalWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "externalWorkflowExecutionCancelRequestedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionInitiatedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "scheduleActivityTaskFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef,
        "requestCancelActivityTaskFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef,
        "startTimerFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsstartTimerFailedEventAttributesTypeDef,
        "cancelTimerFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventscancelTimerFailedEventAttributesTypeDef,
        "startChildWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef,
        "lambdaFunctionScheduledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionScheduledEventAttributesTypeDef,
        "lambdaFunctionStartedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionStartedEventAttributesTypeDef,
        "lambdaFunctionCompletedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionCompletedEventAttributesTypeDef,
        "lambdaFunctionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionFailedEventAttributesTypeDef,
        "lambdaFunctionTimedOutEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionTimedOutEventAttributesTypeDef,
        "scheduleLambdaFunctionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef,
        "startLambdaFunctionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseTypeDef",
    {"events": List[ClientGetWorkflowExecutionHistoryResponseeventsTypeDef], "nextPageToken": str},
    total=False,
)

ClientListActivityTypesResponsetypeInfosactivityTypeTypeDef = TypedDict(
    "ClientListActivityTypesResponsetypeInfosactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientListActivityTypesResponsetypeInfosTypeDef = TypedDict(
    "ClientListActivityTypesResponsetypeInfosTypeDef",
    {
        "activityType": ClientListActivityTypesResponsetypeInfosactivityTypeTypeDef,
        "status": Literal["REGISTERED", "DEPRECATED"],
        "description": str,
        "creationDate": datetime,
        "deprecationDate": datetime,
    },
    total=False,
)

ClientListActivityTypesResponseTypeDef = TypedDict(
    "ClientListActivityTypesResponseTypeDef",
    {"typeInfos": List[ClientListActivityTypesResponsetypeInfosTypeDef], "nextPageToken": str},
    total=False,
)

ClientListClosedWorkflowExecutionsCloseStatusFilterTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsCloseStatusFilterTypeDef",
    {
        "status": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ]
    },
    total=False,
)

ClientListClosedWorkflowExecutionsCloseTimeFilterTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsCloseTimeFilterTypeDef",
    {"oldestDate": datetime, "latestDate": datetime},
    total=False,
)

ClientListClosedWorkflowExecutionsExecutionFilterTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsExecutionFilterTypeDef", {"workflowId": str}, total=False
)

ClientListClosedWorkflowExecutionsResponseexecutionInfosexecutionTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsResponseexecutionInfosexecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientListClosedWorkflowExecutionsResponseexecutionInfosparentTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsResponseexecutionInfosparentTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientListClosedWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientListClosedWorkflowExecutionsResponseexecutionInfosTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsResponseexecutionInfosTypeDef",
    {
        "execution": ClientListClosedWorkflowExecutionsResponseexecutionInfosexecutionTypeDef,
        "workflowType": ClientListClosedWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef,
        "startTimestamp": datetime,
        "closeTimestamp": datetime,
        "executionStatus": Literal["OPEN", "CLOSED"],
        "closeStatus": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ],
        "parent": ClientListClosedWorkflowExecutionsResponseexecutionInfosparentTypeDef,
        "tagList": List[str],
        "cancelRequested": bool,
    },
    total=False,
)

ClientListClosedWorkflowExecutionsResponseTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsResponseTypeDef",
    {
        "executionInfos": List[ClientListClosedWorkflowExecutionsResponseexecutionInfosTypeDef],
        "nextPageToken": str,
    },
    total=False,
)

ClientListClosedWorkflowExecutionsStartTimeFilterTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsStartTimeFilterTypeDef",
    {"oldestDate": datetime, "latestDate": datetime},
    total=False,
)

ClientListClosedWorkflowExecutionsTagFilterTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsTagFilterTypeDef", {"tag": str}, total=False
)

ClientListClosedWorkflowExecutionsTypeFilterTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsTypeFilterTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientListDomainsResponsedomainInfosTypeDef = TypedDict(
    "ClientListDomainsResponsedomainInfosTypeDef",
    {"name": str, "status": Literal["REGISTERED", "DEPRECATED"], "description": str, "arn": str},
    total=False,
)

ClientListDomainsResponseTypeDef = TypedDict(
    "ClientListDomainsResponseTypeDef",
    {"domainInfos": List[ClientListDomainsResponsedomainInfosTypeDef], "nextPageToken": str},
    total=False,
)

ClientListOpenWorkflowExecutionsExecutionFilterTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsExecutionFilterTypeDef", {"workflowId": str}, total=False
)

ClientListOpenWorkflowExecutionsResponseexecutionInfosexecutionTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsResponseexecutionInfosexecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientListOpenWorkflowExecutionsResponseexecutionInfosparentTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsResponseexecutionInfosparentTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientListOpenWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientListOpenWorkflowExecutionsResponseexecutionInfosTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsResponseexecutionInfosTypeDef",
    {
        "execution": ClientListOpenWorkflowExecutionsResponseexecutionInfosexecutionTypeDef,
        "workflowType": ClientListOpenWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef,
        "startTimestamp": datetime,
        "closeTimestamp": datetime,
        "executionStatus": Literal["OPEN", "CLOSED"],
        "closeStatus": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ],
        "parent": ClientListOpenWorkflowExecutionsResponseexecutionInfosparentTypeDef,
        "tagList": List[str],
        "cancelRequested": bool,
    },
    total=False,
)

ClientListOpenWorkflowExecutionsResponseTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsResponseTypeDef",
    {
        "executionInfos": List[ClientListOpenWorkflowExecutionsResponseexecutionInfosTypeDef],
        "nextPageToken": str,
    },
    total=False,
)

_RequiredClientListOpenWorkflowExecutionsStartTimeFilterTypeDef = TypedDict(
    "_RequiredClientListOpenWorkflowExecutionsStartTimeFilterTypeDef", {"oldestDate": datetime}
)
_OptionalClientListOpenWorkflowExecutionsStartTimeFilterTypeDef = TypedDict(
    "_OptionalClientListOpenWorkflowExecutionsStartTimeFilterTypeDef",
    {"latestDate": datetime},
    total=False,
)


class ClientListOpenWorkflowExecutionsStartTimeFilterTypeDef(
    _RequiredClientListOpenWorkflowExecutionsStartTimeFilterTypeDef,
    _OptionalClientListOpenWorkflowExecutionsStartTimeFilterTypeDef,
):
    pass


ClientListOpenWorkflowExecutionsTagFilterTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsTagFilterTypeDef", {"tag": str}, total=False
)

ClientListOpenWorkflowExecutionsTypeFilterTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsTypeFilterTypeDef", {"name": str, "version": str}, total=False
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)

ClientListWorkflowTypesResponsetypeInfosworkflowTypeTypeDef = TypedDict(
    "ClientListWorkflowTypesResponsetypeInfosworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientListWorkflowTypesResponsetypeInfosTypeDef = TypedDict(
    "ClientListWorkflowTypesResponsetypeInfosTypeDef",
    {
        "workflowType": ClientListWorkflowTypesResponsetypeInfosworkflowTypeTypeDef,
        "status": Literal["REGISTERED", "DEPRECATED"],
        "description": str,
        "creationDate": datetime,
        "deprecationDate": datetime,
    },
    total=False,
)

ClientListWorkflowTypesResponseTypeDef = TypedDict(
    "ClientListWorkflowTypesResponseTypeDef",
    {"typeInfos": List[ClientListWorkflowTypesResponsetypeInfosTypeDef], "nextPageToken": str},
    total=False,
)

ClientPollForActivityTaskResponseactivityTypeTypeDef = TypedDict(
    "ClientPollForActivityTaskResponseactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForActivityTaskResponseworkflowExecutionTypeDef = TypedDict(
    "ClientPollForActivityTaskResponseworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForActivityTaskResponseTypeDef = TypedDict(
    "ClientPollForActivityTaskResponseTypeDef",
    {
        "taskToken": str,
        "activityId": str,
        "startedEventId": int,
        "workflowExecution": ClientPollForActivityTaskResponseworkflowExecutionTypeDef,
        "activityType": ClientPollForActivityTaskResponseactivityTypeTypeDef,
        "input": str,
    },
    total=False,
)

ClientPollForActivityTaskTaskListTypeDef = TypedDict(
    "ClientPollForActivityTaskTaskListTypeDef", {"name": str}
)

ClientPollForDecisionTaskResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef",
    {"decisionTaskCompletedEventId": int, "activityId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskCanceledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskCanceledEventAttributesTypeDef",
    {
        "details": str,
        "scheduledEventId": int,
        "startedEventId": int,
        "latestCancelRequestedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskCompletedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskCompletedEventAttributesTypeDef",
    {"result": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskFailedEventAttributesTypeDef",
    {"reason": str, "details": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesTypeDef",
    {
        "activityType": ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef,
        "activityId": str,
        "input": str,
        "control": str,
        "scheduleToStartTimeout": str,
        "scheduleToCloseTimeout": str,
        "startToCloseTimeout": str,
        "taskList": ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef,
        "taskPriority": str,
        "decisionTaskCompletedEventId": int,
        "heartbeatTimeout": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskStartedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskStartedEventAttributesTypeDef",
    {"identity": str, "scheduledEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskTimedOutEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskTimedOutEventAttributesTypeDef",
    {
        "timeoutType": Literal[
            "START_TO_CLOSE", "SCHEDULE_TO_START", "SCHEDULE_TO_CLOSE", "HEARTBEAT"
        ],
        "scheduledEventId": int,
        "startedEventId": int,
        "details": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventscancelTimerFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventscancelTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal["TIMER_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef,
        "details": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef,
        "result": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef,
        "reason": str,
        "details": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef,
        "timeoutType": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal[
            "UNHANDLED_DECISION",
            "WORKFLOW_TYPE_DEPRECATED",
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsdecisionTaskCompletedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsdecisionTaskCompletedEventAttributesTypeDef",
    {"executionContext": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributesTypeDef",
    {
        "taskList": ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef,
        "taskPriority": str,
        "startToCloseTimeout": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsdecisionTaskStartedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsdecisionTaskStartedEventAttributesTypeDef",
    {"identity": str, "scheduledEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsdecisionTaskTimedOutEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsdecisionTaskTimedOutEventAttributesTypeDef",
    {"timeoutType": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventslambdaFunctionCompletedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventslambdaFunctionCompletedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "result": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventslambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventslambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "reason": str, "details": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventslambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventslambdaFunctionScheduledEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "control": str,
        "input": str,
        "startToCloseTimeout": str,
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventslambdaFunctionStartedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventslambdaFunctionStartedEventAttributesTypeDef",
    {"scheduledEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventslambdaFunctionTimedOutEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventslambdaFunctionTimedOutEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "timeoutType": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsmarkerRecordedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsmarkerRecordedEventAttributesTypeDef",
    {"markerName": str, "details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsrecordMarkerFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsrecordMarkerFailedEventAttributesTypeDef",
    {"markerName": str, "cause": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef",
    {
        "activityId": str,
        "cause": Literal["ACTIVITY_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"workflowId": str, "runId": str, "decisionTaskCompletedEventId": int, "control": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef",
    {
        "activityType": ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef,
        "activityId": str,
        "cause": Literal[
            "ACTIVITY_TYPE_DEPRECATED",
            "ACTIVITY_TYPE_DOES_NOT_EXIST",
            "ACTIVITY_ID_ALREADY_IN_USE",
            "OPEN_ACTIVITIES_LIMIT_EXCEEDED",
            "ACTIVITY_CREATION_RATE_EXCEEDED",
            "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED",
            "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "cause": Literal[
            "ID_ALREADY_IN_USE",
            "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED",
            "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED",
            "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "signalName": str,
        "input": str,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowType": ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef,
        "cause": Literal[
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "WORKFLOW_TYPE_DEPRECATED",
            "OPEN_CHILDREN_LIMIT_EXCEEDED",
            "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
            "CHILD_CREATION_RATE_EXCEEDED",
            "WORKFLOW_ALREADY_RUNNING",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "workflowId": str,
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "workflowType": ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef,
        "control": str,
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef,
        "taskPriority": str,
        "decisionTaskCompletedEventId": int,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskStartToCloseTimeout": str,
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "cause": str, "message": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartTimerFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal[
            "TIMER_ID_ALREADY_IN_USE",
            "OPEN_TIMERS_LIMIT_EXCEEDED",
            "TIMER_CREATION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventstimerCanceledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventstimerCanceledEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventstimerFiredEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventstimerFiredEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventstimerStartedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventstimerStartedEventAttributesTypeDef",
    {
        "timerId": str,
        "control": str,
        "startToFireTimeout": str,
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "externalWorkflowExecution": ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
        "cause": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionCanceledEventAttributesTypeDef",
    {"details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionCompletedEventAttributesTypeDef",
    {"result": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "input": str,
        "decisionTaskCompletedEventId": int,
        "newExecutionRunId": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "tagList": List[str],
        "workflowType": ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef,
        "lambdaRole": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionFailedEventAttributesTypeDef",
    {"reason": str, "details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesTypeDef",
    {
        "signalName": str,
        "input": str,
        "externalWorkflowExecution": ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskList": ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef,
        "taskPriority": str,
        "workflowType": ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef,
        "tagList": List[str],
        "continuedExecutionRunId": str,
        "parentWorkflowExecution": ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef,
        "parentInitiatedEventId": int,
        "lambdaRole": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "reason": str,
        "details": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "cause": Literal["CHILD_POLICY_APPLIED", "EVENT_LIMIT_EXCEEDED", "OPERATOR_INITIATED"],
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef",
    {"timeoutType": str, "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"]},
    total=False,
)

ClientPollForDecisionTaskResponseeventsTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsTypeDef",
    {
        "eventTimestamp": datetime,
        "eventType": Literal[
            "WorkflowExecutionStarted",
            "WorkflowExecutionCancelRequested",
            "WorkflowExecutionCompleted",
            "CompleteWorkflowExecutionFailed",
            "WorkflowExecutionFailed",
            "FailWorkflowExecutionFailed",
            "WorkflowExecutionTimedOut",
            "WorkflowExecutionCanceled",
            "CancelWorkflowExecutionFailed",
            "WorkflowExecutionContinuedAsNew",
            "ContinueAsNewWorkflowExecutionFailed",
            "WorkflowExecutionTerminated",
            "DecisionTaskScheduled",
            "DecisionTaskStarted",
            "DecisionTaskCompleted",
            "DecisionTaskTimedOut",
            "ActivityTaskScheduled",
            "ScheduleActivityTaskFailed",
            "ActivityTaskStarted",
            "ActivityTaskCompleted",
            "ActivityTaskFailed",
            "ActivityTaskTimedOut",
            "ActivityTaskCanceled",
            "ActivityTaskCancelRequested",
            "RequestCancelActivityTaskFailed",
            "WorkflowExecutionSignaled",
            "MarkerRecorded",
            "RecordMarkerFailed",
            "TimerStarted",
            "StartTimerFailed",
            "TimerFired",
            "TimerCanceled",
            "CancelTimerFailed",
            "StartChildWorkflowExecutionInitiated",
            "StartChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionStarted",
            "ChildWorkflowExecutionCompleted",
            "ChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionTimedOut",
            "ChildWorkflowExecutionCanceled",
            "ChildWorkflowExecutionTerminated",
            "SignalExternalWorkflowExecutionInitiated",
            "SignalExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionSignaled",
            "RequestCancelExternalWorkflowExecutionInitiated",
            "RequestCancelExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionCancelRequested",
            "LambdaFunctionScheduled",
            "LambdaFunctionStarted",
            "LambdaFunctionCompleted",
            "LambdaFunctionFailed",
            "LambdaFunctionTimedOut",
            "ScheduleLambdaFunctionFailed",
            "StartLambdaFunctionFailed",
        ],
        "eventId": int,
        "workflowExecutionStartedEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesTypeDef,
        "workflowExecutionCompletedEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionCompletedEventAttributesTypeDef,
        "completeWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionFailedEventAttributesTypeDef,
        "failWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTimedOutEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef,
        "workflowExecutionCanceledEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionCanceledEventAttributesTypeDef,
        "cancelWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionContinuedAsNewEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef,
        "continueAsNewWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTerminatedEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef,
        "workflowExecutionCancelRequestedEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef,
        "decisionTaskScheduledEventAttributes": ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributesTypeDef,
        "decisionTaskStartedEventAttributes": ClientPollForDecisionTaskResponseeventsdecisionTaskStartedEventAttributesTypeDef,
        "decisionTaskCompletedEventAttributes": ClientPollForDecisionTaskResponseeventsdecisionTaskCompletedEventAttributesTypeDef,
        "decisionTaskTimedOutEventAttributes": ClientPollForDecisionTaskResponseeventsdecisionTaskTimedOutEventAttributesTypeDef,
        "activityTaskScheduledEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesTypeDef,
        "activityTaskStartedEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskStartedEventAttributesTypeDef,
        "activityTaskCompletedEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskCompletedEventAttributesTypeDef,
        "activityTaskFailedEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskFailedEventAttributesTypeDef,
        "activityTaskTimedOutEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskTimedOutEventAttributesTypeDef,
        "activityTaskCanceledEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskCanceledEventAttributesTypeDef,
        "activityTaskCancelRequestedEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef,
        "workflowExecutionSignaledEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesTypeDef,
        "markerRecordedEventAttributes": ClientPollForDecisionTaskResponseeventsmarkerRecordedEventAttributesTypeDef,
        "recordMarkerFailedEventAttributes": ClientPollForDecisionTaskResponseeventsrecordMarkerFailedEventAttributesTypeDef,
        "timerStartedEventAttributes": ClientPollForDecisionTaskResponseeventstimerStartedEventAttributesTypeDef,
        "timerFiredEventAttributes": ClientPollForDecisionTaskResponseeventstimerFiredEventAttributesTypeDef,
        "timerCanceledEventAttributes": ClientPollForDecisionTaskResponseeventstimerCanceledEventAttributesTypeDef,
        "startChildWorkflowExecutionInitiatedEventAttributes": ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef,
        "childWorkflowExecutionStartedEventAttributes": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef,
        "childWorkflowExecutionCompletedEventAttributes": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef,
        "childWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef,
        "childWorkflowExecutionTimedOutEventAttributes": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef,
        "childWorkflowExecutionCanceledEventAttributes": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef,
        "childWorkflowExecutionTerminatedEventAttributes": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef,
        "signalExternalWorkflowExecutionInitiatedEventAttributes": ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "externalWorkflowExecutionSignaledEventAttributes": ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef,
        "signalExternalWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "externalWorkflowExecutionCancelRequestedEventAttributes": ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionInitiatedEventAttributes": ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "scheduleActivityTaskFailedEventAttributes": ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef,
        "requestCancelActivityTaskFailedEventAttributes": ClientPollForDecisionTaskResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef,
        "startTimerFailedEventAttributes": ClientPollForDecisionTaskResponseeventsstartTimerFailedEventAttributesTypeDef,
        "cancelTimerFailedEventAttributes": ClientPollForDecisionTaskResponseeventscancelTimerFailedEventAttributesTypeDef,
        "startChildWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef,
        "lambdaFunctionScheduledEventAttributes": ClientPollForDecisionTaskResponseeventslambdaFunctionScheduledEventAttributesTypeDef,
        "lambdaFunctionStartedEventAttributes": ClientPollForDecisionTaskResponseeventslambdaFunctionStartedEventAttributesTypeDef,
        "lambdaFunctionCompletedEventAttributes": ClientPollForDecisionTaskResponseeventslambdaFunctionCompletedEventAttributesTypeDef,
        "lambdaFunctionFailedEventAttributes": ClientPollForDecisionTaskResponseeventslambdaFunctionFailedEventAttributesTypeDef,
        "lambdaFunctionTimedOutEventAttributes": ClientPollForDecisionTaskResponseeventslambdaFunctionTimedOutEventAttributesTypeDef,
        "scheduleLambdaFunctionFailedEventAttributes": ClientPollForDecisionTaskResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef,
        "startLambdaFunctionFailedEventAttributes": ClientPollForDecisionTaskResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef,
    },
    total=False,
)

ClientPollForDecisionTaskResponseworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseTypeDef",
    {
        "taskToken": str,
        "startedEventId": int,
        "workflowExecution": ClientPollForDecisionTaskResponseworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseworkflowTypeTypeDef,
        "events": List[ClientPollForDecisionTaskResponseeventsTypeDef],
        "nextPageToken": str,
        "previousStartedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskTaskListTypeDef = TypedDict(
    "ClientPollForDecisionTaskTaskListTypeDef", {"name": str}
)

ClientRecordActivityTaskHeartbeatResponseTypeDef = TypedDict(
    "ClientRecordActivityTaskHeartbeatResponseTypeDef", {"cancelRequested": bool}, total=False
)

ClientRegisterActivityTypeDefaultTaskListTypeDef = TypedDict(
    "ClientRegisterActivityTypeDefaultTaskListTypeDef", {"name": str}
)

_RequiredClientRegisterDomainTagsTypeDef = TypedDict(
    "_RequiredClientRegisterDomainTagsTypeDef", {"key": str}
)
_OptionalClientRegisterDomainTagsTypeDef = TypedDict(
    "_OptionalClientRegisterDomainTagsTypeDef", {"value": str}, total=False
)


class ClientRegisterDomainTagsTypeDef(
    _RequiredClientRegisterDomainTagsTypeDef, _OptionalClientRegisterDomainTagsTypeDef
):
    pass


ClientRegisterWorkflowTypeDefaultTaskListTypeDef = TypedDict(
    "ClientRegisterWorkflowTypeDefaultTaskListTypeDef", {"name": str}
)

ClientRespondDecisionTaskCompletedDecisionscancelTimerDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionscancelTimerDecisionAttributesTypeDef",
    {"timerId": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionscancelWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionscancelWorkflowExecutionDecisionAttributesTypeDef",
    {"details": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionscompleteWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionscompleteWorkflowExecutionDecisionAttributesTypeDef",
    {"result": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributestaskListTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributestaskListTypeDef,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "tagList": List[str],
        "workflowTypeVersion": str,
        "lambdaRole": str,
    },
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsfailWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsfailWorkflowExecutionDecisionAttributesTypeDef",
    {"reason": str, "details": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsrecordMarkerDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsrecordMarkerDecisionAttributesTypeDef",
    {"markerName": str, "details": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsrequestCancelActivityTaskDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsrequestCancelActivityTaskDecisionAttributesTypeDef",
    {"activityId": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsrequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsrequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef",
    {"workflowId": str, "runId": str, "control": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesactivityTypeTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributestaskListTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesTypeDef",
    {
        "activityType": ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesactivityTypeTypeDef,
        "activityId": str,
        "control": str,
        "input": str,
        "scheduleToCloseTimeout": str,
        "taskList": ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributestaskListTypeDef,
        "taskPriority": str,
        "scheduleToStartTimeout": str,
        "startToCloseTimeout": str,
        "heartbeatTimeout": str,
    },
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsscheduleLambdaFunctionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsscheduleLambdaFunctionDecisionAttributesTypeDef",
    {"id": str, "name": str, "control": str, "input": str, "startToCloseTimeout": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionssignalExternalWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionssignalExternalWorkflowExecutionDecisionAttributesTypeDef",
    {"workflowId": str, "runId": str, "signalName": str, "input": str, "control": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributestaskListTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesworkflowTypeTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesTypeDef",
    {
        "workflowType": ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesworkflowTypeTypeDef,
        "workflowId": str,
        "control": str,
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributestaskListTypeDef,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsstartTimerDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsstartTimerDecisionAttributesTypeDef",
    {"timerId": str, "control": str, "startToFireTimeout": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsTypeDef",
    {
        "decisionType": Literal[
            "ScheduleActivityTask",
            "RequestCancelActivityTask",
            "CompleteWorkflowExecution",
            "FailWorkflowExecution",
            "CancelWorkflowExecution",
            "ContinueAsNewWorkflowExecution",
            "RecordMarker",
            "StartTimer",
            "CancelTimer",
            "SignalExternalWorkflowExecution",
            "RequestCancelExternalWorkflowExecution",
            "StartChildWorkflowExecution",
            "ScheduleLambdaFunction",
        ],
        "scheduleActivityTaskDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesTypeDef,
        "requestCancelActivityTaskDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsrequestCancelActivityTaskDecisionAttributesTypeDef,
        "completeWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionscompleteWorkflowExecutionDecisionAttributesTypeDef,
        "failWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsfailWorkflowExecutionDecisionAttributesTypeDef,
        "cancelWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionscancelWorkflowExecutionDecisionAttributesTypeDef,
        "continueAsNewWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributesTypeDef,
        "recordMarkerDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsrecordMarkerDecisionAttributesTypeDef,
        "startTimerDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsstartTimerDecisionAttributesTypeDef,
        "cancelTimerDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionscancelTimerDecisionAttributesTypeDef,
        "signalExternalWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionssignalExternalWorkflowExecutionDecisionAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsrequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef,
        "startChildWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesTypeDef,
        "scheduleLambdaFunctionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsscheduleLambdaFunctionDecisionAttributesTypeDef,
    },
    total=False,
)

ClientStartWorkflowExecutionResponseTypeDef = TypedDict(
    "ClientStartWorkflowExecutionResponseTypeDef", {"runId": str}, total=False
)

ClientStartWorkflowExecutionTaskListTypeDef = TypedDict(
    "ClientStartWorkflowExecutionTaskListTypeDef", {"name": str}, total=False
)

_RequiredClientStartWorkflowExecutionWorkflowTypeTypeDef = TypedDict(
    "_RequiredClientStartWorkflowExecutionWorkflowTypeTypeDef", {"name": str}
)
_OptionalClientStartWorkflowExecutionWorkflowTypeTypeDef = TypedDict(
    "_OptionalClientStartWorkflowExecutionWorkflowTypeTypeDef", {"version": str}, total=False
)


class ClientStartWorkflowExecutionWorkflowTypeTypeDef(
    _RequiredClientStartWorkflowExecutionWorkflowTypeTypeDef,
    _OptionalClientStartWorkflowExecutionWorkflowTypeTypeDef,
):
    pass


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


_RequiredClientUndeprecateActivityTypeActivityTypeTypeDef = TypedDict(
    "_RequiredClientUndeprecateActivityTypeActivityTypeTypeDef", {"name": str}
)
_OptionalClientUndeprecateActivityTypeActivityTypeTypeDef = TypedDict(
    "_OptionalClientUndeprecateActivityTypeActivityTypeTypeDef", {"version": str}, total=False
)


class ClientUndeprecateActivityTypeActivityTypeTypeDef(
    _RequiredClientUndeprecateActivityTypeActivityTypeTypeDef,
    _OptionalClientUndeprecateActivityTypeActivityTypeTypeDef,
):
    pass


_RequiredClientUndeprecateWorkflowTypeWorkflowTypeTypeDef = TypedDict(
    "_RequiredClientUndeprecateWorkflowTypeWorkflowTypeTypeDef", {"name": str}
)
_OptionalClientUndeprecateWorkflowTypeWorkflowTypeTypeDef = TypedDict(
    "_OptionalClientUndeprecateWorkflowTypeWorkflowTypeTypeDef", {"version": str}, total=False
)


class ClientUndeprecateWorkflowTypeWorkflowTypeTypeDef(
    _RequiredClientUndeprecateWorkflowTypeWorkflowTypeTypeDef,
    _OptionalClientUndeprecateWorkflowTypeWorkflowTypeTypeDef,
):
    pass


_RequiredGetWorkflowExecutionHistoryPaginateExecutionTypeDef = TypedDict(
    "_RequiredGetWorkflowExecutionHistoryPaginateExecutionTypeDef", {"workflowId": str}
)
_OptionalGetWorkflowExecutionHistoryPaginateExecutionTypeDef = TypedDict(
    "_OptionalGetWorkflowExecutionHistoryPaginateExecutionTypeDef", {"runId": str}, total=False
)


class GetWorkflowExecutionHistoryPaginateExecutionTypeDef(
    _RequiredGetWorkflowExecutionHistoryPaginateExecutionTypeDef,
    _OptionalGetWorkflowExecutionHistoryPaginateExecutionTypeDef,
):
    pass


GetWorkflowExecutionHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef",
    {"decisionTaskCompletedEventId": int, "activityId": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskCanceledEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskCanceledEventAttributesTypeDef",
    {
        "details": str,
        "scheduledEventId": int,
        "startedEventId": int,
        "latestCancelRequestedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskCompletedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskCompletedEventAttributesTypeDef",
    {"result": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskFailedEventAttributesTypeDef",
    {"reason": str, "details": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskScheduledEventAttributesTypeDef",
    {
        "activityType": GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef,
        "activityId": str,
        "input": str,
        "control": str,
        "scheduleToStartTimeout": str,
        "scheduleToCloseTimeout": str,
        "startToCloseTimeout": str,
        "taskList": GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef,
        "taskPriority": str,
        "decisionTaskCompletedEventId": int,
        "heartbeatTimeout": str,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskStartedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskStartedEventAttributesTypeDef",
    {"identity": str, "scheduledEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskTimedOutEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskTimedOutEventAttributesTypeDef",
    {
        "timeoutType": Literal[
            "START_TO_CLOSE", "SCHEDULE_TO_START", "SCHEDULE_TO_CLOSE", "HEARTBEAT"
        ],
        "scheduledEventId": int,
        "startedEventId": int,
        "details": str,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventscancelTimerFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventscancelTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal["TIMER_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef",
    {
        "workflowExecution": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef,
        "workflowType": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef,
        "details": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef",
    {
        "workflowExecution": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef,
        "workflowType": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef,
        "result": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowExecution": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef,
        "workflowType": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef,
        "reason": str,
        "details": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "workflowExecution": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef,
        "workflowType": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "workflowExecution": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef,
        "workflowType": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef",
    {
        "workflowExecution": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef,
        "workflowType": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef,
        "timeoutType": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal[
            "UNHANDLED_DECISION",
            "WORKFLOW_TYPE_DEPRECATED",
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskCompletedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskCompletedEventAttributesTypeDef",
    {"executionContext": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskScheduledEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskScheduledEventAttributesTypeDef",
    {
        "taskList": GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef,
        "taskPriority": str,
        "startToCloseTimeout": str,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskStartedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskStartedEventAttributesTypeDef",
    {"identity": str, "scheduledEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskTimedOutEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskTimedOutEventAttributesTypeDef",
    {"timeoutType": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "workflowExecution": GetWorkflowExecutionHistoryPaginateResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef",
    {
        "workflowExecution": GetWorkflowExecutionHistoryPaginateResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionCompletedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionCompletedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "result": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "reason": str, "details": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "control": str,
        "input": str,
        "startToCloseTimeout": str,
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionStartedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionStartedEventAttributesTypeDef",
    {"scheduledEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "timeoutType": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsmarkerRecordedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsmarkerRecordedEventAttributesTypeDef",
    {"markerName": str, "details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsrecordMarkerFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsrecordMarkerFailedEventAttributesTypeDef",
    {"markerName": str, "cause": str, "decisionTaskCompletedEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef",
    {
        "activityId": str,
        "cause": Literal["ACTIVITY_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"workflowId": str, "runId": str, "decisionTaskCompletedEventId": int, "control": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef",
    {
        "activityType": GetWorkflowExecutionHistoryPaginateResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef,
        "activityId": str,
        "cause": Literal[
            "ACTIVITY_TYPE_DEPRECATED",
            "ACTIVITY_TYPE_DOES_NOT_EXIST",
            "ACTIVITY_ID_ALREADY_IN_USE",
            "OPEN_ACTIVITIES_LIMIT_EXCEEDED",
            "ACTIVITY_CREATION_RATE_EXCEEDED",
            "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED",
            "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "cause": Literal[
            "ID_ALREADY_IN_USE",
            "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED",
            "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED",
            "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "signalName": str,
        "input": str,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowType": GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef,
        "cause": Literal[
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "WORKFLOW_TYPE_DEPRECATED",
            "OPEN_CHILDREN_LIMIT_EXCEEDED",
            "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
            "CHILD_CREATION_RATE_EXCEEDED",
            "WORKFLOW_ALREADY_RUNNING",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "workflowId": str,
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "workflowType": GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef,
        "control": str,
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef,
        "taskPriority": str,
        "decisionTaskCompletedEventId": int,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskStartToCloseTimeout": str,
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "cause": str, "message": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsstartTimerFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsstartTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal[
            "TIMER_ID_ALREADY_IN_USE",
            "OPEN_TIMERS_LIMIT_EXCEEDED",
            "TIMER_CREATION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventstimerCanceledEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventstimerCanceledEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int, "decisionTaskCompletedEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventstimerFiredEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventstimerFiredEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventstimerStartedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventstimerStartedEventAttributesTypeDef",
    {
        "timerId": str,
        "control": str,
        "startToFireTimeout": str,
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "externalWorkflowExecution": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
        "cause": str,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionCanceledEventAttributesTypeDef",
    {"details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionCompletedEventAttributesTypeDef",
    {"result": str, "decisionTaskCompletedEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "input": str,
        "decisionTaskCompletedEventId": int,
        "newExecutionRunId": str,
        "executionStartToCloseTimeout": str,
        "taskList": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "tagList": List[str],
        "workflowType": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef,
        "lambdaRole": str,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionFailedEventAttributesTypeDef",
    {"reason": str, "details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionSignaledEventAttributesTypeDef",
    {
        "signalName": str,
        "input": str,
        "externalWorkflowExecution": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionStartedEventAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskList": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef,
        "taskPriority": str,
        "workflowType": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef,
        "tagList": List[str],
        "continuedExecutionRunId": str,
        "parentWorkflowExecution": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef,
        "parentInitiatedEventId": int,
        "lambdaRole": str,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "reason": str,
        "details": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "cause": Literal["CHILD_POLICY_APPLIED", "EVENT_LIMIT_EXCEEDED", "OPERATOR_INITIATED"],
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef",
    {"timeoutType": str, "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"]},
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseeventsTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseeventsTypeDef",
    {
        "eventTimestamp": datetime,
        "eventType": Literal[
            "WorkflowExecutionStarted",
            "WorkflowExecutionCancelRequested",
            "WorkflowExecutionCompleted",
            "CompleteWorkflowExecutionFailed",
            "WorkflowExecutionFailed",
            "FailWorkflowExecutionFailed",
            "WorkflowExecutionTimedOut",
            "WorkflowExecutionCanceled",
            "CancelWorkflowExecutionFailed",
            "WorkflowExecutionContinuedAsNew",
            "ContinueAsNewWorkflowExecutionFailed",
            "WorkflowExecutionTerminated",
            "DecisionTaskScheduled",
            "DecisionTaskStarted",
            "DecisionTaskCompleted",
            "DecisionTaskTimedOut",
            "ActivityTaskScheduled",
            "ScheduleActivityTaskFailed",
            "ActivityTaskStarted",
            "ActivityTaskCompleted",
            "ActivityTaskFailed",
            "ActivityTaskTimedOut",
            "ActivityTaskCanceled",
            "ActivityTaskCancelRequested",
            "RequestCancelActivityTaskFailed",
            "WorkflowExecutionSignaled",
            "MarkerRecorded",
            "RecordMarkerFailed",
            "TimerStarted",
            "StartTimerFailed",
            "TimerFired",
            "TimerCanceled",
            "CancelTimerFailed",
            "StartChildWorkflowExecutionInitiated",
            "StartChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionStarted",
            "ChildWorkflowExecutionCompleted",
            "ChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionTimedOut",
            "ChildWorkflowExecutionCanceled",
            "ChildWorkflowExecutionTerminated",
            "SignalExternalWorkflowExecutionInitiated",
            "SignalExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionSignaled",
            "RequestCancelExternalWorkflowExecutionInitiated",
            "RequestCancelExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionCancelRequested",
            "LambdaFunctionScheduled",
            "LambdaFunctionStarted",
            "LambdaFunctionCompleted",
            "LambdaFunctionFailed",
            "LambdaFunctionTimedOut",
            "ScheduleLambdaFunctionFailed",
            "StartLambdaFunctionFailed",
        ],
        "eventId": int,
        "workflowExecutionStartedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionStartedEventAttributesTypeDef,
        "workflowExecutionCompletedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionCompletedEventAttributesTypeDef,
        "completeWorkflowExecutionFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionFailedEventAttributesTypeDef,
        "failWorkflowExecutionFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTimedOutEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef,
        "workflowExecutionCanceledEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionCanceledEventAttributesTypeDef,
        "cancelWorkflowExecutionFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionContinuedAsNewEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef,
        "continueAsNewWorkflowExecutionFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTerminatedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef,
        "workflowExecutionCancelRequestedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef,
        "decisionTaskScheduledEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskScheduledEventAttributesTypeDef,
        "decisionTaskStartedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskStartedEventAttributesTypeDef,
        "decisionTaskCompletedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskCompletedEventAttributesTypeDef,
        "decisionTaskTimedOutEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsdecisionTaskTimedOutEventAttributesTypeDef,
        "activityTaskScheduledEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskScheduledEventAttributesTypeDef,
        "activityTaskStartedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskStartedEventAttributesTypeDef,
        "activityTaskCompletedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskCompletedEventAttributesTypeDef,
        "activityTaskFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskFailedEventAttributesTypeDef,
        "activityTaskTimedOutEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskTimedOutEventAttributesTypeDef,
        "activityTaskCanceledEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskCanceledEventAttributesTypeDef,
        "activityTaskCancelRequestedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef,
        "workflowExecutionSignaledEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsworkflowExecutionSignaledEventAttributesTypeDef,
        "markerRecordedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsmarkerRecordedEventAttributesTypeDef,
        "recordMarkerFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsrecordMarkerFailedEventAttributesTypeDef,
        "timerStartedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventstimerStartedEventAttributesTypeDef,
        "timerFiredEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventstimerFiredEventAttributesTypeDef,
        "timerCanceledEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventstimerCanceledEventAttributesTypeDef,
        "startChildWorkflowExecutionInitiatedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef,
        "childWorkflowExecutionStartedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef,
        "childWorkflowExecutionCompletedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef,
        "childWorkflowExecutionFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef,
        "childWorkflowExecutionTimedOutEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef,
        "childWorkflowExecutionCanceledEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef,
        "childWorkflowExecutionTerminatedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef,
        "signalExternalWorkflowExecutionInitiatedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "externalWorkflowExecutionSignaledEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef,
        "signalExternalWorkflowExecutionFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "externalWorkflowExecutionCancelRequestedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionInitiatedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "scheduleActivityTaskFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef,
        "requestCancelActivityTaskFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef,
        "startTimerFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsstartTimerFailedEventAttributesTypeDef,
        "cancelTimerFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventscancelTimerFailedEventAttributesTypeDef,
        "startChildWorkflowExecutionFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef,
        "lambdaFunctionScheduledEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventAttributesTypeDef,
        "lambdaFunctionStartedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionStartedEventAttributesTypeDef,
        "lambdaFunctionCompletedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionCompletedEventAttributesTypeDef,
        "lambdaFunctionFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventAttributesTypeDef,
        "lambdaFunctionTimedOutEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventAttributesTypeDef,
        "scheduleLambdaFunctionFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef,
        "startLambdaFunctionFailedEventAttributes": GetWorkflowExecutionHistoryPaginateResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef,
    },
    total=False,
)

GetWorkflowExecutionHistoryPaginateResponseTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryPaginateResponseTypeDef",
    {"events": List[GetWorkflowExecutionHistoryPaginateResponseeventsTypeDef], "NextToken": str},
    total=False,
)

ListActivityTypesPaginatePaginationConfigTypeDef = TypedDict(
    "ListActivityTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListActivityTypesPaginateResponsetypeInfosactivityTypeTypeDef = TypedDict(
    "ListActivityTypesPaginateResponsetypeInfosactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ListActivityTypesPaginateResponsetypeInfosTypeDef = TypedDict(
    "ListActivityTypesPaginateResponsetypeInfosTypeDef",
    {
        "activityType": ListActivityTypesPaginateResponsetypeInfosactivityTypeTypeDef,
        "status": Literal["REGISTERED", "DEPRECATED"],
        "description": str,
        "creationDate": datetime,
        "deprecationDate": datetime,
    },
    total=False,
)

ListActivityTypesPaginateResponseTypeDef = TypedDict(
    "ListActivityTypesPaginateResponseTypeDef",
    {"typeInfos": List[ListActivityTypesPaginateResponsetypeInfosTypeDef], "NextToken": str},
    total=False,
)

ListClosedWorkflowExecutionsPaginateCloseStatusFilterTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsPaginateCloseStatusFilterTypeDef",
    {
        "status": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ]
    },
    total=False,
)

ListClosedWorkflowExecutionsPaginateCloseTimeFilterTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsPaginateCloseTimeFilterTypeDef",
    {"oldestDate": datetime, "latestDate": datetime},
    total=False,
)

ListClosedWorkflowExecutionsPaginateExecutionFilterTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsPaginateExecutionFilterTypeDef", {"workflowId": str}, total=False
)

ListClosedWorkflowExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListClosedWorkflowExecutionsPaginateResponseexecutionInfosexecutionTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsPaginateResponseexecutionInfosexecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ListClosedWorkflowExecutionsPaginateResponseexecutionInfosparentTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsPaginateResponseexecutionInfosparentTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ListClosedWorkflowExecutionsPaginateResponseexecutionInfosworkflowTypeTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsPaginateResponseexecutionInfosworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ListClosedWorkflowExecutionsPaginateResponseexecutionInfosTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsPaginateResponseexecutionInfosTypeDef",
    {
        "execution": ListClosedWorkflowExecutionsPaginateResponseexecutionInfosexecutionTypeDef,
        "workflowType": ListClosedWorkflowExecutionsPaginateResponseexecutionInfosworkflowTypeTypeDef,
        "startTimestamp": datetime,
        "closeTimestamp": datetime,
        "executionStatus": Literal["OPEN", "CLOSED"],
        "closeStatus": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ],
        "parent": ListClosedWorkflowExecutionsPaginateResponseexecutionInfosparentTypeDef,
        "tagList": List[str],
        "cancelRequested": bool,
    },
    total=False,
)

ListClosedWorkflowExecutionsPaginateResponseTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsPaginateResponseTypeDef",
    {
        "executionInfos": List[ListClosedWorkflowExecutionsPaginateResponseexecutionInfosTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListClosedWorkflowExecutionsPaginateStartTimeFilterTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsPaginateStartTimeFilterTypeDef",
    {"oldestDate": datetime, "latestDate": datetime},
    total=False,
)

ListClosedWorkflowExecutionsPaginateTagFilterTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsPaginateTagFilterTypeDef", {"tag": str}, total=False
)

ListClosedWorkflowExecutionsPaginateTypeFilterTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsPaginateTypeFilterTypeDef",
    {"name": str, "version": str},
    total=False,
)

ListDomainsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDomainsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDomainsPaginateResponsedomainInfosTypeDef = TypedDict(
    "ListDomainsPaginateResponsedomainInfosTypeDef",
    {"name": str, "status": Literal["REGISTERED", "DEPRECATED"], "description": str, "arn": str},
    total=False,
)

ListDomainsPaginateResponseTypeDef = TypedDict(
    "ListDomainsPaginateResponseTypeDef",
    {"domainInfos": List[ListDomainsPaginateResponsedomainInfosTypeDef], "NextToken": str},
    total=False,
)

ListOpenWorkflowExecutionsPaginateExecutionFilterTypeDef = TypedDict(
    "ListOpenWorkflowExecutionsPaginateExecutionFilterTypeDef", {"workflowId": str}, total=False
)

ListOpenWorkflowExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListOpenWorkflowExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListOpenWorkflowExecutionsPaginateResponseexecutionInfosexecutionTypeDef = TypedDict(
    "ListOpenWorkflowExecutionsPaginateResponseexecutionInfosexecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ListOpenWorkflowExecutionsPaginateResponseexecutionInfosparentTypeDef = TypedDict(
    "ListOpenWorkflowExecutionsPaginateResponseexecutionInfosparentTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ListOpenWorkflowExecutionsPaginateResponseexecutionInfosworkflowTypeTypeDef = TypedDict(
    "ListOpenWorkflowExecutionsPaginateResponseexecutionInfosworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ListOpenWorkflowExecutionsPaginateResponseexecutionInfosTypeDef = TypedDict(
    "ListOpenWorkflowExecutionsPaginateResponseexecutionInfosTypeDef",
    {
        "execution": ListOpenWorkflowExecutionsPaginateResponseexecutionInfosexecutionTypeDef,
        "workflowType": ListOpenWorkflowExecutionsPaginateResponseexecutionInfosworkflowTypeTypeDef,
        "startTimestamp": datetime,
        "closeTimestamp": datetime,
        "executionStatus": Literal["OPEN", "CLOSED"],
        "closeStatus": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ],
        "parent": ListOpenWorkflowExecutionsPaginateResponseexecutionInfosparentTypeDef,
        "tagList": List[str],
        "cancelRequested": bool,
    },
    total=False,
)

ListOpenWorkflowExecutionsPaginateResponseTypeDef = TypedDict(
    "ListOpenWorkflowExecutionsPaginateResponseTypeDef",
    {
        "executionInfos": List[ListOpenWorkflowExecutionsPaginateResponseexecutionInfosTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredListOpenWorkflowExecutionsPaginateStartTimeFilterTypeDef = TypedDict(
    "_RequiredListOpenWorkflowExecutionsPaginateStartTimeFilterTypeDef", {"oldestDate": datetime}
)
_OptionalListOpenWorkflowExecutionsPaginateStartTimeFilterTypeDef = TypedDict(
    "_OptionalListOpenWorkflowExecutionsPaginateStartTimeFilterTypeDef",
    {"latestDate": datetime},
    total=False,
)


class ListOpenWorkflowExecutionsPaginateStartTimeFilterTypeDef(
    _RequiredListOpenWorkflowExecutionsPaginateStartTimeFilterTypeDef,
    _OptionalListOpenWorkflowExecutionsPaginateStartTimeFilterTypeDef,
):
    pass


ListOpenWorkflowExecutionsPaginateTagFilterTypeDef = TypedDict(
    "ListOpenWorkflowExecutionsPaginateTagFilterTypeDef", {"tag": str}, total=False
)

ListOpenWorkflowExecutionsPaginateTypeFilterTypeDef = TypedDict(
    "ListOpenWorkflowExecutionsPaginateTypeFilterTypeDef",
    {"name": str, "version": str},
    total=False,
)

ListWorkflowTypesPaginatePaginationConfigTypeDef = TypedDict(
    "ListWorkflowTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListWorkflowTypesPaginateResponsetypeInfosworkflowTypeTypeDef = TypedDict(
    "ListWorkflowTypesPaginateResponsetypeInfosworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ListWorkflowTypesPaginateResponsetypeInfosTypeDef = TypedDict(
    "ListWorkflowTypesPaginateResponsetypeInfosTypeDef",
    {
        "workflowType": ListWorkflowTypesPaginateResponsetypeInfosworkflowTypeTypeDef,
        "status": Literal["REGISTERED", "DEPRECATED"],
        "description": str,
        "creationDate": datetime,
        "deprecationDate": datetime,
    },
    total=False,
)

ListWorkflowTypesPaginateResponseTypeDef = TypedDict(
    "ListWorkflowTypesPaginateResponseTypeDef",
    {"typeInfos": List[ListWorkflowTypesPaginateResponsetypeInfosTypeDef], "NextToken": str},
    total=False,
)

PollForDecisionTaskPaginatePaginationConfigTypeDef = TypedDict(
    "PollForDecisionTaskPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef",
    {"decisionTaskCompletedEventId": int, "activityId": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsactivityTaskCanceledEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsactivityTaskCanceledEventAttributesTypeDef",
    {
        "details": str,
        "scheduledEventId": int,
        "startedEventId": int,
        "latestCancelRequestedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsactivityTaskCompletedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsactivityTaskCompletedEventAttributesTypeDef",
    {"result": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsactivityTaskFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsactivityTaskFailedEventAttributesTypeDef",
    {"reason": str, "details": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsactivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsactivityTaskScheduledEventAttributesTypeDef",
    {
        "activityType": PollForDecisionTaskPaginateResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef,
        "activityId": str,
        "input": str,
        "control": str,
        "scheduleToStartTimeout": str,
        "scheduleToCloseTimeout": str,
        "startToCloseTimeout": str,
        "taskList": PollForDecisionTaskPaginateResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef,
        "taskPriority": str,
        "decisionTaskCompletedEventId": int,
        "heartbeatTimeout": str,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsactivityTaskStartedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsactivityTaskStartedEventAttributesTypeDef",
    {"identity": str, "scheduledEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsactivityTaskTimedOutEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsactivityTaskTimedOutEventAttributesTypeDef",
    {
        "timeoutType": Literal[
            "START_TO_CLOSE", "SCHEDULE_TO_START", "SCHEDULE_TO_CLOSE", "HEARTBEAT"
        ],
        "scheduledEventId": int,
        "startedEventId": int,
        "details": str,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventscancelTimerFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventscancelTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal["TIMER_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef",
    {
        "workflowExecution": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef,
        "workflowType": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef,
        "details": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef",
    {
        "workflowExecution": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef,
        "workflowType": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef,
        "result": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowExecution": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef,
        "workflowType": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef,
        "reason": str,
        "details": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "workflowExecution": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef,
        "workflowType": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "workflowExecution": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef,
        "workflowType": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef",
    {
        "workflowExecution": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef,
        "workflowType": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef,
        "timeoutType": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal[
            "UNHANDLED_DECISION",
            "WORKFLOW_TYPE_DEPRECATED",
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsdecisionTaskCompletedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsdecisionTaskCompletedEventAttributesTypeDef",
    {"executionContext": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsdecisionTaskScheduledEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsdecisionTaskScheduledEventAttributesTypeDef",
    {
        "taskList": PollForDecisionTaskPaginateResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef,
        "taskPriority": str,
        "startToCloseTimeout": str,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsdecisionTaskStartedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsdecisionTaskStartedEventAttributesTypeDef",
    {"identity": str, "scheduledEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsdecisionTaskTimedOutEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsdecisionTaskTimedOutEventAttributesTypeDef",
    {"timeoutType": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "workflowExecution": PollForDecisionTaskPaginateResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef",
    {
        "workflowExecution": PollForDecisionTaskPaginateResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventslambdaFunctionCompletedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventslambdaFunctionCompletedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "result": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventslambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventslambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "reason": str, "details": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventslambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventslambdaFunctionScheduledEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "control": str,
        "input": str,
        "startToCloseTimeout": str,
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventslambdaFunctionStartedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventslambdaFunctionStartedEventAttributesTypeDef",
    {"scheduledEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventslambdaFunctionTimedOutEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventslambdaFunctionTimedOutEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "timeoutType": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsmarkerRecordedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsmarkerRecordedEventAttributesTypeDef",
    {"markerName": str, "details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsrecordMarkerFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsrecordMarkerFailedEventAttributesTypeDef",
    {"markerName": str, "cause": str, "decisionTaskCompletedEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef",
    {
        "activityId": str,
        "cause": Literal["ACTIVITY_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"workflowId": str, "runId": str, "decisionTaskCompletedEventId": int, "control": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef",
    {
        "activityType": PollForDecisionTaskPaginateResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef,
        "activityId": str,
        "cause": Literal[
            "ACTIVITY_TYPE_DEPRECATED",
            "ACTIVITY_TYPE_DOES_NOT_EXIST",
            "ACTIVITY_ID_ALREADY_IN_USE",
            "OPEN_ACTIVITIES_LIMIT_EXCEEDED",
            "ACTIVITY_CREATION_RATE_EXCEEDED",
            "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED",
            "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "cause": Literal[
            "ID_ALREADY_IN_USE",
            "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED",
            "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED",
            "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "signalName": str,
        "input": str,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowType": PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef,
        "cause": Literal[
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "WORKFLOW_TYPE_DEPRECATED",
            "OPEN_CHILDREN_LIMIT_EXCEEDED",
            "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
            "CHILD_CREATION_RATE_EXCEEDED",
            "WORKFLOW_ALREADY_RUNNING",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "workflowId": str,
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "workflowType": PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef,
        "control": str,
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef,
        "taskPriority": str,
        "decisionTaskCompletedEventId": int,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskStartToCloseTimeout": str,
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "cause": str, "message": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsstartTimerFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsstartTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal[
            "TIMER_ID_ALREADY_IN_USE",
            "OPEN_TIMERS_LIMIT_EXCEEDED",
            "TIMER_CREATION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventstimerCanceledEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventstimerCanceledEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int, "decisionTaskCompletedEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventstimerFiredEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventstimerFiredEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventstimerStartedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventstimerStartedEventAttributesTypeDef",
    {
        "timerId": str,
        "control": str,
        "startToFireTimeout": str,
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "externalWorkflowExecution": PollForDecisionTaskPaginateResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
        "cause": str,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionCanceledEventAttributesTypeDef",
    {"details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionCompletedEventAttributesTypeDef",
    {"result": str, "decisionTaskCompletedEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "input": str,
        "decisionTaskCompletedEventId": int,
        "newExecutionRunId": str,
        "executionStartToCloseTimeout": str,
        "taskList": PollForDecisionTaskPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "tagList": List[str],
        "workflowType": PollForDecisionTaskPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef,
        "lambdaRole": str,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionFailedEventAttributesTypeDef",
    {"reason": str, "details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionSignaledEventAttributesTypeDef",
    {
        "signalName": str,
        "input": str,
        "externalWorkflowExecution": PollForDecisionTaskPaginateResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionStartedEventAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskList": PollForDecisionTaskPaginateResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef,
        "taskPriority": str,
        "workflowType": PollForDecisionTaskPaginateResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef,
        "tagList": List[str],
        "continuedExecutionRunId": str,
        "parentWorkflowExecution": PollForDecisionTaskPaginateResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef,
        "parentInitiatedEventId": int,
        "lambdaRole": str,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "reason": str,
        "details": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "cause": Literal["CHILD_POLICY_APPLIED", "EVENT_LIMIT_EXCEEDED", "OPERATOR_INITIATED"],
    },
    total=False,
)

PollForDecisionTaskPaginateResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef",
    {"timeoutType": str, "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"]},
    total=False,
)

PollForDecisionTaskPaginateResponseeventsTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseeventsTypeDef",
    {
        "eventTimestamp": datetime,
        "eventType": Literal[
            "WorkflowExecutionStarted",
            "WorkflowExecutionCancelRequested",
            "WorkflowExecutionCompleted",
            "CompleteWorkflowExecutionFailed",
            "WorkflowExecutionFailed",
            "FailWorkflowExecutionFailed",
            "WorkflowExecutionTimedOut",
            "WorkflowExecutionCanceled",
            "CancelWorkflowExecutionFailed",
            "WorkflowExecutionContinuedAsNew",
            "ContinueAsNewWorkflowExecutionFailed",
            "WorkflowExecutionTerminated",
            "DecisionTaskScheduled",
            "DecisionTaskStarted",
            "DecisionTaskCompleted",
            "DecisionTaskTimedOut",
            "ActivityTaskScheduled",
            "ScheduleActivityTaskFailed",
            "ActivityTaskStarted",
            "ActivityTaskCompleted",
            "ActivityTaskFailed",
            "ActivityTaskTimedOut",
            "ActivityTaskCanceled",
            "ActivityTaskCancelRequested",
            "RequestCancelActivityTaskFailed",
            "WorkflowExecutionSignaled",
            "MarkerRecorded",
            "RecordMarkerFailed",
            "TimerStarted",
            "StartTimerFailed",
            "TimerFired",
            "TimerCanceled",
            "CancelTimerFailed",
            "StartChildWorkflowExecutionInitiated",
            "StartChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionStarted",
            "ChildWorkflowExecutionCompleted",
            "ChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionTimedOut",
            "ChildWorkflowExecutionCanceled",
            "ChildWorkflowExecutionTerminated",
            "SignalExternalWorkflowExecutionInitiated",
            "SignalExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionSignaled",
            "RequestCancelExternalWorkflowExecutionInitiated",
            "RequestCancelExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionCancelRequested",
            "LambdaFunctionScheduled",
            "LambdaFunctionStarted",
            "LambdaFunctionCompleted",
            "LambdaFunctionFailed",
            "LambdaFunctionTimedOut",
            "ScheduleLambdaFunctionFailed",
            "StartLambdaFunctionFailed",
        ],
        "eventId": int,
        "workflowExecutionStartedEventAttributes": PollForDecisionTaskPaginateResponseeventsworkflowExecutionStartedEventAttributesTypeDef,
        "workflowExecutionCompletedEventAttributes": PollForDecisionTaskPaginateResponseeventsworkflowExecutionCompletedEventAttributesTypeDef,
        "completeWorkflowExecutionFailedEventAttributes": PollForDecisionTaskPaginateResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionFailedEventAttributes": PollForDecisionTaskPaginateResponseeventsworkflowExecutionFailedEventAttributesTypeDef,
        "failWorkflowExecutionFailedEventAttributes": PollForDecisionTaskPaginateResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTimedOutEventAttributes": PollForDecisionTaskPaginateResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef,
        "workflowExecutionCanceledEventAttributes": PollForDecisionTaskPaginateResponseeventsworkflowExecutionCanceledEventAttributesTypeDef,
        "cancelWorkflowExecutionFailedEventAttributes": PollForDecisionTaskPaginateResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionContinuedAsNewEventAttributes": PollForDecisionTaskPaginateResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef,
        "continueAsNewWorkflowExecutionFailedEventAttributes": PollForDecisionTaskPaginateResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTerminatedEventAttributes": PollForDecisionTaskPaginateResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef,
        "workflowExecutionCancelRequestedEventAttributes": PollForDecisionTaskPaginateResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef,
        "decisionTaskScheduledEventAttributes": PollForDecisionTaskPaginateResponseeventsdecisionTaskScheduledEventAttributesTypeDef,
        "decisionTaskStartedEventAttributes": PollForDecisionTaskPaginateResponseeventsdecisionTaskStartedEventAttributesTypeDef,
        "decisionTaskCompletedEventAttributes": PollForDecisionTaskPaginateResponseeventsdecisionTaskCompletedEventAttributesTypeDef,
        "decisionTaskTimedOutEventAttributes": PollForDecisionTaskPaginateResponseeventsdecisionTaskTimedOutEventAttributesTypeDef,
        "activityTaskScheduledEventAttributes": PollForDecisionTaskPaginateResponseeventsactivityTaskScheduledEventAttributesTypeDef,
        "activityTaskStartedEventAttributes": PollForDecisionTaskPaginateResponseeventsactivityTaskStartedEventAttributesTypeDef,
        "activityTaskCompletedEventAttributes": PollForDecisionTaskPaginateResponseeventsactivityTaskCompletedEventAttributesTypeDef,
        "activityTaskFailedEventAttributes": PollForDecisionTaskPaginateResponseeventsactivityTaskFailedEventAttributesTypeDef,
        "activityTaskTimedOutEventAttributes": PollForDecisionTaskPaginateResponseeventsactivityTaskTimedOutEventAttributesTypeDef,
        "activityTaskCanceledEventAttributes": PollForDecisionTaskPaginateResponseeventsactivityTaskCanceledEventAttributesTypeDef,
        "activityTaskCancelRequestedEventAttributes": PollForDecisionTaskPaginateResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef,
        "workflowExecutionSignaledEventAttributes": PollForDecisionTaskPaginateResponseeventsworkflowExecutionSignaledEventAttributesTypeDef,
        "markerRecordedEventAttributes": PollForDecisionTaskPaginateResponseeventsmarkerRecordedEventAttributesTypeDef,
        "recordMarkerFailedEventAttributes": PollForDecisionTaskPaginateResponseeventsrecordMarkerFailedEventAttributesTypeDef,
        "timerStartedEventAttributes": PollForDecisionTaskPaginateResponseeventstimerStartedEventAttributesTypeDef,
        "timerFiredEventAttributes": PollForDecisionTaskPaginateResponseeventstimerFiredEventAttributesTypeDef,
        "timerCanceledEventAttributes": PollForDecisionTaskPaginateResponseeventstimerCanceledEventAttributesTypeDef,
        "startChildWorkflowExecutionInitiatedEventAttributes": PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef,
        "childWorkflowExecutionStartedEventAttributes": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef,
        "childWorkflowExecutionCompletedEventAttributes": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef,
        "childWorkflowExecutionFailedEventAttributes": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef,
        "childWorkflowExecutionTimedOutEventAttributes": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef,
        "childWorkflowExecutionCanceledEventAttributes": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef,
        "childWorkflowExecutionTerminatedEventAttributes": PollForDecisionTaskPaginateResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef,
        "signalExternalWorkflowExecutionInitiatedEventAttributes": PollForDecisionTaskPaginateResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "externalWorkflowExecutionSignaledEventAttributes": PollForDecisionTaskPaginateResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef,
        "signalExternalWorkflowExecutionFailedEventAttributes": PollForDecisionTaskPaginateResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "externalWorkflowExecutionCancelRequestedEventAttributes": PollForDecisionTaskPaginateResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionInitiatedEventAttributes": PollForDecisionTaskPaginateResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionFailedEventAttributes": PollForDecisionTaskPaginateResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "scheduleActivityTaskFailedEventAttributes": PollForDecisionTaskPaginateResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef,
        "requestCancelActivityTaskFailedEventAttributes": PollForDecisionTaskPaginateResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef,
        "startTimerFailedEventAttributes": PollForDecisionTaskPaginateResponseeventsstartTimerFailedEventAttributesTypeDef,
        "cancelTimerFailedEventAttributes": PollForDecisionTaskPaginateResponseeventscancelTimerFailedEventAttributesTypeDef,
        "startChildWorkflowExecutionFailedEventAttributes": PollForDecisionTaskPaginateResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef,
        "lambdaFunctionScheduledEventAttributes": PollForDecisionTaskPaginateResponseeventslambdaFunctionScheduledEventAttributesTypeDef,
        "lambdaFunctionStartedEventAttributes": PollForDecisionTaskPaginateResponseeventslambdaFunctionStartedEventAttributesTypeDef,
        "lambdaFunctionCompletedEventAttributes": PollForDecisionTaskPaginateResponseeventslambdaFunctionCompletedEventAttributesTypeDef,
        "lambdaFunctionFailedEventAttributes": PollForDecisionTaskPaginateResponseeventslambdaFunctionFailedEventAttributesTypeDef,
        "lambdaFunctionTimedOutEventAttributes": PollForDecisionTaskPaginateResponseeventslambdaFunctionTimedOutEventAttributesTypeDef,
        "scheduleLambdaFunctionFailedEventAttributes": PollForDecisionTaskPaginateResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef,
        "startLambdaFunctionFailedEventAttributes": PollForDecisionTaskPaginateResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef,
    },
    total=False,
)

PollForDecisionTaskPaginateResponseworkflowExecutionTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

PollForDecisionTaskPaginateResponseworkflowTypeTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

PollForDecisionTaskPaginateResponseTypeDef = TypedDict(
    "PollForDecisionTaskPaginateResponseTypeDef",
    {
        "taskToken": str,
        "startedEventId": int,
        "workflowExecution": PollForDecisionTaskPaginateResponseworkflowExecutionTypeDef,
        "workflowType": PollForDecisionTaskPaginateResponseworkflowTypeTypeDef,
        "events": List[PollForDecisionTaskPaginateResponseeventsTypeDef],
        "previousStartedEventId": int,
        "NextToken": str,
    },
    total=False,
)

PollForDecisionTaskPaginateTaskListTypeDef = TypedDict(
    "PollForDecisionTaskPaginateTaskListTypeDef", {"name": str}
)
