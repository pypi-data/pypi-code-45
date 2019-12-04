"Main interface for stepfunctions service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateActivityResponseTypeDef",
    "ClientCreateActivityTagsTypeDef",
    "ClientCreateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    "ClientCreateStateMachineLoggingConfigurationdestinationsTypeDef",
    "ClientCreateStateMachineLoggingConfigurationTypeDef",
    "ClientCreateStateMachineResponseTypeDef",
    "ClientCreateStateMachineTagsTypeDef",
    "ClientDescribeActivityResponseTypeDef",
    "ClientDescribeExecutionResponseTypeDef",
    "ClientDescribeStateMachineForExecutionResponseTypeDef",
    "ClientDescribeStateMachineResponseloggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    "ClientDescribeStateMachineResponseloggingConfigurationdestinationsTypeDef",
    "ClientDescribeStateMachineResponseloggingConfigurationTypeDef",
    "ClientDescribeStateMachineResponseTypeDef",
    "ClientGetActivityTaskResponseTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsTypeDef",
    "ClientGetExecutionHistoryResponseTypeDef",
    "ClientListActivitiesResponseactivitiesTypeDef",
    "ClientListActivitiesResponseTypeDef",
    "ClientListExecutionsResponseexecutionsTypeDef",
    "ClientListExecutionsResponseTypeDef",
    "ClientListStateMachinesResponsestateMachinesTypeDef",
    "ClientListStateMachinesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientStartExecutionResponseTypeDef",
    "ClientStopExecutionResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    "ClientUpdateStateMachineLoggingConfigurationdestinationsTypeDef",
    "ClientUpdateStateMachineLoggingConfigurationTypeDef",
    "ClientUpdateStateMachineResponseTypeDef",
    "GetExecutionHistoryPaginatePaginationConfigTypeDef",
    "GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsTypeDef",
    "GetExecutionHistoryPaginateResponseTypeDef",
    "ListActivitiesPaginatePaginationConfigTypeDef",
    "ListActivitiesPaginateResponseactivitiesTypeDef",
    "ListActivitiesPaginateResponseTypeDef",
    "ListExecutionsPaginatePaginationConfigTypeDef",
    "ListExecutionsPaginateResponseexecutionsTypeDef",
    "ListExecutionsPaginateResponseTypeDef",
    "ListStateMachinesPaginatePaginationConfigTypeDef",
    "ListStateMachinesPaginateResponsestateMachinesTypeDef",
    "ListStateMachinesPaginateResponseTypeDef",
)


_ClientCreateActivityResponseTypeDef = TypedDict(
    "_ClientCreateActivityResponseTypeDef",
    {"activityArn": str, "creationDate": datetime},
    total=False,
)


class ClientCreateActivityResponseTypeDef(_ClientCreateActivityResponseTypeDef):
    """
    - *(dict) --*

      - **activityArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the created activity.
    """


_ClientCreateActivityTagsTypeDef = TypedDict(
    "_ClientCreateActivityTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateActivityTagsTypeDef(_ClientCreateActivityTagsTypeDef):
    """
    - *(dict) --*

      Tags are key-value pairs that can be associated with Step Functions state machines and
      activities.
      An array of key-value pairs. For more information, see `Using Cost Allocation Tags
      <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the
      *AWS Billing and Cost Management User Guide* , and `Controlling Access Using IAM Tags
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html>`__ .
      Tags may only contain Unicode letters, digits, white space, or these symbols: ``_ . : / =
           + -
      @`` .
      - **key** *(string) --*

        The key of a tag.
    """


_ClientCreateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef = TypedDict(
    "_ClientCreateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    {"logGroupArn": str},
    total=False,
)


class ClientCreateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef(
    _ClientCreateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef
):
    pass


_ClientCreateStateMachineLoggingConfigurationdestinationsTypeDef = TypedDict(
    "_ClientCreateStateMachineLoggingConfigurationdestinationsTypeDef",
    {
        "cloudWatchLogsLogGroup": ClientCreateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef
    },
    total=False,
)


class ClientCreateStateMachineLoggingConfigurationdestinationsTypeDef(
    _ClientCreateStateMachineLoggingConfigurationdestinationsTypeDef
):
    pass


_ClientCreateStateMachineLoggingConfigurationTypeDef = TypedDict(
    "_ClientCreateStateMachineLoggingConfigurationTypeDef",
    {
        "level": Literal["ALL", "ERROR", "FATAL", "OFF"],
        "includeExecutionData": bool,
        "destinations": List[ClientCreateStateMachineLoggingConfigurationdestinationsTypeDef],
    },
    total=False,
)


class ClientCreateStateMachineLoggingConfigurationTypeDef(
    _ClientCreateStateMachineLoggingConfigurationTypeDef
):
    """
    Defines what execution history events are logged and where they are logged.
    - **level** *(string) --*

      Defines which category of execution history events are logged.
    """


_ClientCreateStateMachineResponseTypeDef = TypedDict(
    "_ClientCreateStateMachineResponseTypeDef",
    {"stateMachineArn": str, "creationDate": datetime},
    total=False,
)


class ClientCreateStateMachineResponseTypeDef(_ClientCreateStateMachineResponseTypeDef):
    """
    - *(dict) --*

      - **stateMachineArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the created state machine.
    """


_ClientCreateStateMachineTagsTypeDef = TypedDict(
    "_ClientCreateStateMachineTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateStateMachineTagsTypeDef(_ClientCreateStateMachineTagsTypeDef):
    """
    - *(dict) --*

      Tags are key-value pairs that can be associated with Step Functions state machines and
      activities.
      An array of key-value pairs. For more information, see `Using Cost Allocation Tags
      <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the
      *AWS Billing and Cost Management User Guide* , and `Controlling Access Using IAM Tags
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html>`__ .
      Tags may only contain Unicode letters, digits, white space, or these symbols: ``_ . : / =
           + -
      @`` .
      - **key** *(string) --*

        The key of a tag.
    """


_ClientDescribeActivityResponseTypeDef = TypedDict(
    "_ClientDescribeActivityResponseTypeDef",
    {"activityArn": str, "name": str, "creationDate": datetime},
    total=False,
)


class ClientDescribeActivityResponseTypeDef(_ClientDescribeActivityResponseTypeDef):
    """
    - *(dict) --*

      - **activityArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the activity.
    """


_ClientDescribeExecutionResponseTypeDef = TypedDict(
    "_ClientDescribeExecutionResponseTypeDef",
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


class ClientDescribeExecutionResponseTypeDef(_ClientDescribeExecutionResponseTypeDef):
    """
    - *(dict) --*

      - **executionArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the execution.
    """


_ClientDescribeStateMachineForExecutionResponseTypeDef = TypedDict(
    "_ClientDescribeStateMachineForExecutionResponseTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "definition": str,
        "roleArn": str,
        "updateDate": datetime,
    },
    total=False,
)


class ClientDescribeStateMachineForExecutionResponseTypeDef(
    _ClientDescribeStateMachineForExecutionResponseTypeDef
):
    """
    - *(dict) --*

      - **stateMachineArn** *(string) --*

        The Amazon Resource Name (ARN) of the state machine associated with the execution.
    """


_ClientDescribeStateMachineResponseloggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef = TypedDict(
    "_ClientDescribeStateMachineResponseloggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    {"logGroupArn": str},
    total=False,
)


class ClientDescribeStateMachineResponseloggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef(
    _ClientDescribeStateMachineResponseloggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef
):
    pass


_ClientDescribeStateMachineResponseloggingConfigurationdestinationsTypeDef = TypedDict(
    "_ClientDescribeStateMachineResponseloggingConfigurationdestinationsTypeDef",
    {
        "cloudWatchLogsLogGroup": ClientDescribeStateMachineResponseloggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef
    },
    total=False,
)


class ClientDescribeStateMachineResponseloggingConfigurationdestinationsTypeDef(
    _ClientDescribeStateMachineResponseloggingConfigurationdestinationsTypeDef
):
    pass


_ClientDescribeStateMachineResponseloggingConfigurationTypeDef = TypedDict(
    "_ClientDescribeStateMachineResponseloggingConfigurationTypeDef",
    {
        "level": Literal["ALL", "ERROR", "FATAL", "OFF"],
        "includeExecutionData": bool,
        "destinations": List[
            ClientDescribeStateMachineResponseloggingConfigurationdestinationsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeStateMachineResponseloggingConfigurationTypeDef(
    _ClientDescribeStateMachineResponseloggingConfigurationTypeDef
):
    pass


_ClientDescribeStateMachineResponseTypeDef = TypedDict(
    "_ClientDescribeStateMachineResponseTypeDef",
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


class ClientDescribeStateMachineResponseTypeDef(_ClientDescribeStateMachineResponseTypeDef):
    """
    - *(dict) --*

      - **stateMachineArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the state machine.
    """


_ClientGetActivityTaskResponseTypeDef = TypedDict(
    "_ClientGetActivityTaskResponseTypeDef", {"taskToken": str, "input": str}, total=False
)


class ClientGetActivityTaskResponseTypeDef(_ClientGetActivityTaskResponseTypeDef):
    """
    - *(dict) --*

      - **taskToken** *(string) --*

        A token that identifies the scheduled task. This token must be copied and included in
        subsequent calls to  SendTaskHeartbeat ,  SendTaskSuccess or  SendTaskFailure in order to
        report the progress or completion of the task.
    """


_ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int, "heartbeatInSeconds": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef",
    {"workerName": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef",
    {"input": str, "roleArn": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef",
    {"length": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef",
    {"name": str, "input": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef",
    {"name": str, "output": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "region": str,
        "parameters": str,
        "timeoutInSeconds": int,
    },
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef",
    {"resourceType": str, "resource": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef
):
    pass


_ClientGetExecutionHistoryResponseeventsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsTypeDef",
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


class ClientGetExecutionHistoryResponseeventsTypeDef(
    _ClientGetExecutionHistoryResponseeventsTypeDef
):
    """
    - *(dict) --*

      Contains details about the events of an execution.
      - **timestamp** *(datetime) --*

        The date and time the event occurred.
    """


_ClientGetExecutionHistoryResponseTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseTypeDef",
    {"events": List[ClientGetExecutionHistoryResponseeventsTypeDef], "nextToken": str},
    total=False,
)


class ClientGetExecutionHistoryResponseTypeDef(_ClientGetExecutionHistoryResponseTypeDef):
    """
    - *(dict) --*

      - **events** *(list) --*

        The list of events that occurred in the execution.
        - *(dict) --*

          Contains details about the events of an execution.
          - **timestamp** *(datetime) --*

            The date and time the event occurred.
    """


_ClientListActivitiesResponseactivitiesTypeDef = TypedDict(
    "_ClientListActivitiesResponseactivitiesTypeDef",
    {"activityArn": str, "name": str, "creationDate": datetime},
    total=False,
)


class ClientListActivitiesResponseactivitiesTypeDef(_ClientListActivitiesResponseactivitiesTypeDef):
    """
    - *(dict) --*

      Contains details about an activity.
      - **activityArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the activity.
    """


_ClientListActivitiesResponseTypeDef = TypedDict(
    "_ClientListActivitiesResponseTypeDef",
    {"activities": List[ClientListActivitiesResponseactivitiesTypeDef], "nextToken": str},
    total=False,
)


class ClientListActivitiesResponseTypeDef(_ClientListActivitiesResponseTypeDef):
    """
    - *(dict) --*

      - **activities** *(list) --*

        The list of activities.
        - *(dict) --*

          Contains details about an activity.
          - **activityArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the activity.
    """


_ClientListExecutionsResponseexecutionsTypeDef = TypedDict(
    "_ClientListExecutionsResponseexecutionsTypeDef",
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


class ClientListExecutionsResponseexecutionsTypeDef(_ClientListExecutionsResponseexecutionsTypeDef):
    """
    - *(dict) --*

      Contains details about an execution.
      - **executionArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the execution.
    """


_ClientListExecutionsResponseTypeDef = TypedDict(
    "_ClientListExecutionsResponseTypeDef",
    {"executions": List[ClientListExecutionsResponseexecutionsTypeDef], "nextToken": str},
    total=False,
)


class ClientListExecutionsResponseTypeDef(_ClientListExecutionsResponseTypeDef):
    """
    - *(dict) --*

      - **executions** *(list) --*

        The list of matching executions.
        - *(dict) --*

          Contains details about an execution.
          - **executionArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the execution.
    """


_ClientListStateMachinesResponsestateMachinesTypeDef = TypedDict(
    "_ClientListStateMachinesResponsestateMachinesTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "type": Literal["STANDARD", "EXPRESS"],
        "creationDate": datetime,
    },
    total=False,
)


class ClientListStateMachinesResponsestateMachinesTypeDef(
    _ClientListStateMachinesResponsestateMachinesTypeDef
):
    """
    - *(dict) --*

      Contains details about the state machine.
      - **stateMachineArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the state machine.
    """


_ClientListStateMachinesResponseTypeDef = TypedDict(
    "_ClientListStateMachinesResponseTypeDef",
    {"stateMachines": List[ClientListStateMachinesResponsestateMachinesTypeDef], "nextToken": str},
    total=False,
)


class ClientListStateMachinesResponseTypeDef(_ClientListStateMachinesResponseTypeDef):
    """
    - *(dict) --*

      - **stateMachines** *(list) --*

        - *(dict) --*

          Contains details about the state machine.
          - **stateMachineArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the state machine.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientListTagsForResourceResponsetagsTypeDef(_ClientListTagsForResourceResponsetagsTypeDef):
    """
    - *(dict) --*

      Tags are key-value pairs that can be associated with Step Functions state machines and
      activities.
      An array of key-value pairs. For more information, see `Using Cost Allocation Tags
      <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the
      *AWS Billing and Cost Management User Guide* , and `Controlling Access Using IAM Tags
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html>`__ .
      Tags may only contain Unicode letters, digits, white space, or these symbols: ``_ . : / =
           + -
      @`` .
      - **key** *(string) --*

        The key of a tag.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        An array of tags associated with the resource.
        - *(dict) --*

          Tags are key-value pairs that can be associated with Step Functions state machines and
          activities.
          An array of key-value pairs. For more information, see `Using Cost Allocation Tags
          <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in
          the *AWS Billing and Cost Management User Guide* , and `Controlling Access Using IAM Tags
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html>`__ .
          Tags may only contain Unicode letters, digits, white space, or these symbols: ``_ . : / =
          + - @`` .
          - **key** *(string) --*

            The key of a tag.
    """


_ClientStartExecutionResponseTypeDef = TypedDict(
    "_ClientStartExecutionResponseTypeDef",
    {"executionArn": str, "startDate": datetime},
    total=False,
)


class ClientStartExecutionResponseTypeDef(_ClientStartExecutionResponseTypeDef):
    """
    - *(dict) --*

      - **executionArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the execution.
    """


_ClientStopExecutionResponseTypeDef = TypedDict(
    "_ClientStopExecutionResponseTypeDef", {"stopDate": datetime}, total=False
)


class ClientStopExecutionResponseTypeDef(_ClientStopExecutionResponseTypeDef):
    """
    - *(dict) --*

      - **stopDate** *(datetime) --*

        The date the execution is stopped.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      Tags are key-value pairs that can be associated with Step Functions state machines and
      activities.
      An array of key-value pairs. For more information, see `Using Cost Allocation Tags
      <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the
      *AWS Billing and Cost Management User Guide* , and `Controlling Access Using IAM Tags
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html>`__ .
      Tags may only contain Unicode letters, digits, white space, or these symbols: ``_ . : / =
           + -
      @`` .
      - **key** *(string) --*

        The key of a tag.
    """


_ClientUpdateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef = TypedDict(
    "_ClientUpdateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    {"logGroupArn": str},
    total=False,
)


class ClientUpdateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef(
    _ClientUpdateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef
):
    pass


_ClientUpdateStateMachineLoggingConfigurationdestinationsTypeDef = TypedDict(
    "_ClientUpdateStateMachineLoggingConfigurationdestinationsTypeDef",
    {
        "cloudWatchLogsLogGroup": ClientUpdateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef
    },
    total=False,
)


class ClientUpdateStateMachineLoggingConfigurationdestinationsTypeDef(
    _ClientUpdateStateMachineLoggingConfigurationdestinationsTypeDef
):
    pass


_ClientUpdateStateMachineLoggingConfigurationTypeDef = TypedDict(
    "_ClientUpdateStateMachineLoggingConfigurationTypeDef",
    {
        "level": Literal["ALL", "ERROR", "FATAL", "OFF"],
        "includeExecutionData": bool,
        "destinations": List[ClientUpdateStateMachineLoggingConfigurationdestinationsTypeDef],
    },
    total=False,
)


class ClientUpdateStateMachineLoggingConfigurationTypeDef(
    _ClientUpdateStateMachineLoggingConfigurationTypeDef
):
    """
    - **level** *(string) --*

      Defines which category of execution history events are logged.
    """


_ClientUpdateStateMachineResponseTypeDef = TypedDict(
    "_ClientUpdateStateMachineResponseTypeDef", {"updateDate": datetime}, total=False
)


class ClientUpdateStateMachineResponseTypeDef(_ClientUpdateStateMachineResponseTypeDef):
    """
    - *(dict) --*

      - **updateDate** *(datetime) --*

        The date and time the state machine was updated.
    """


_GetExecutionHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_GetExecutionHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetExecutionHistoryPaginatePaginationConfigTypeDef(
    _GetExecutionHistoryPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int, "heartbeatInSeconds": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef",
    {"workerName": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef",
    {"input": str, "roleArn": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef",
    {"length": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef",
    {"name": str, "input": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef",
    {"name": str, "output": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "region": str,
        "parameters": str,
        "timeoutInSeconds": int,
    },
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef",
    {"resourceType": str, "resource": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef
):
    pass


_GetExecutionHistoryPaginateResponseeventsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsTypeDef",
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


class GetExecutionHistoryPaginateResponseeventsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsTypeDef
):
    """
    - *(dict) --*

      Contains details about the events of an execution.
      - **timestamp** *(datetime) --*

        The date and time the event occurred.
    """


_GetExecutionHistoryPaginateResponseTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseTypeDef",
    {"events": List[GetExecutionHistoryPaginateResponseeventsTypeDef], "NextToken": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseTypeDef(_GetExecutionHistoryPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **events** *(list) --*

        The list of events that occurred in the execution.
        - *(dict) --*

          Contains details about the events of an execution.
          - **timestamp** *(datetime) --*

            The date and time the event occurred.
    """


_ListActivitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListActivitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListActivitiesPaginatePaginationConfigTypeDef(_ListActivitiesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListActivitiesPaginateResponseactivitiesTypeDef = TypedDict(
    "_ListActivitiesPaginateResponseactivitiesTypeDef",
    {"activityArn": str, "name": str, "creationDate": datetime},
    total=False,
)


class ListActivitiesPaginateResponseactivitiesTypeDef(
    _ListActivitiesPaginateResponseactivitiesTypeDef
):
    """
    - *(dict) --*

      Contains details about an activity.
      - **activityArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the activity.
    """


_ListActivitiesPaginateResponseTypeDef = TypedDict(
    "_ListActivitiesPaginateResponseTypeDef",
    {"activities": List[ListActivitiesPaginateResponseactivitiesTypeDef], "NextToken": str},
    total=False,
)


class ListActivitiesPaginateResponseTypeDef(_ListActivitiesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **activities** *(list) --*

        The list of activities.
        - *(dict) --*

          Contains details about an activity.
          - **activityArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the activity.
    """


_ListExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListExecutionsPaginatePaginationConfigTypeDef(_ListExecutionsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListExecutionsPaginateResponseexecutionsTypeDef = TypedDict(
    "_ListExecutionsPaginateResponseexecutionsTypeDef",
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


class ListExecutionsPaginateResponseexecutionsTypeDef(
    _ListExecutionsPaginateResponseexecutionsTypeDef
):
    """
    - *(dict) --*

      Contains details about an execution.
      - **executionArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the execution.
    """


_ListExecutionsPaginateResponseTypeDef = TypedDict(
    "_ListExecutionsPaginateResponseTypeDef",
    {"executions": List[ListExecutionsPaginateResponseexecutionsTypeDef], "NextToken": str},
    total=False,
)


class ListExecutionsPaginateResponseTypeDef(_ListExecutionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **executions** *(list) --*

        The list of matching executions.
        - *(dict) --*

          Contains details about an execution.
          - **executionArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the execution.
    """


_ListStateMachinesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStateMachinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStateMachinesPaginatePaginationConfigTypeDef(
    _ListStateMachinesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListStateMachinesPaginateResponsestateMachinesTypeDef = TypedDict(
    "_ListStateMachinesPaginateResponsestateMachinesTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "type": Literal["STANDARD", "EXPRESS"],
        "creationDate": datetime,
    },
    total=False,
)


class ListStateMachinesPaginateResponsestateMachinesTypeDef(
    _ListStateMachinesPaginateResponsestateMachinesTypeDef
):
    """
    - *(dict) --*

      Contains details about the state machine.
      - **stateMachineArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the state machine.
    """


_ListStateMachinesPaginateResponseTypeDef = TypedDict(
    "_ListStateMachinesPaginateResponseTypeDef",
    {
        "stateMachines": List[ListStateMachinesPaginateResponsestateMachinesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListStateMachinesPaginateResponseTypeDef(_ListStateMachinesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **stateMachines** *(list) --*

        - *(dict) --*

          Contains details about the state machine.
          - **stateMachineArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the state machine.
    """
