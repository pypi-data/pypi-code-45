"Main interface for iotevents service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExitTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionTypeDef",
    "ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef",
    "ClientCreateDetectorModelResponseTypeDef",
    "ClientCreateDetectorModelTagsTypeDef",
    "ClientCreateInputInputDefinitionattributesTypeDef",
    "ClientCreateInputInputDefinitionTypeDef",
    "ClientCreateInputResponseinputConfigurationTypeDef",
    "ClientCreateInputResponseTypeDef",
    "ClientCreateInputTagsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModelTypeDef",
    "ClientDescribeDetectorModelResponseTypeDef",
    "ClientDescribeInputResponseinputinputConfigurationTypeDef",
    "ClientDescribeInputResponseinputinputDefinitionattributesTypeDef",
    "ClientDescribeInputResponseinputinputDefinitionTypeDef",
    "ClientDescribeInputResponseinputTypeDef",
    "ClientDescribeInputResponseTypeDef",
    "ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef",
    "ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef",
    "ClientDescribeLoggingOptionsResponseTypeDef",
    "ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef",
    "ClientListDetectorModelVersionsResponseTypeDef",
    "ClientListDetectorModelsResponsedetectorModelSummariesTypeDef",
    "ClientListDetectorModelsResponseTypeDef",
    "ClientListInputsResponseinputSummariesTypeDef",
    "ClientListInputsResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutLoggingOptionsLoggingOptionsdetectorDebugOptionsTypeDef",
    "ClientPutLoggingOptionsLoggingOptionsTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExitTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionTypeDef",
    "ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef",
    "ClientUpdateDetectorModelResponseTypeDef",
    "ClientUpdateInputInputDefinitionattributesTypeDef",
    "ClientUpdateInputInputDefinitionTypeDef",
    "ClientUpdateInputResponseinputConfigurationTypeDef",
    "ClientUpdateInputResponseTypeDef",
)


_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    {
        "setVariable": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef,
        "sns": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef,
        "iotTopicPublish": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef,
        "clearTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef,
        "resetTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef,
        "lambda": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef,
        "iotEvents": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef,
        "sqs": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef,
        "firehose": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef",
    {"events": List[ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef]},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    {
        "setVariable": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef,
        "sns": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef,
        "iotTopicPublish": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef,
        "clearTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef,
        "resetTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef,
        "lambda": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef,
        "iotEvents": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef,
        "sqs": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef,
        "firehose": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonExitTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonExitTypeDef",
    {"events": List[ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef]},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonExitTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonExitTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    {
        "setVariable": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef,
        "sns": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef,
        "iotTopicPublish": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef,
        "clearTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef,
        "resetTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef,
        "lambda": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef,
        "iotEvents": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef,
        "sqs": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef,
        "firehose": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    {
        "setVariable": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef,
        "sns": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef,
        "iotTopicPublish": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef,
        "clearTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef,
        "resetTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef,
        "lambda": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef,
        "iotEvents": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef,
        "sqs": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef,
        "firehose": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
        ],
        "nextState": str,
    },
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef
):
    pass


_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputTypeDef = TypedDict(
    "_ClientCreateDetectorModelDetectorModelDefinitionstatesonInputTypeDef",
    {
        "events": List[ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef],
        "transitionEvents": List[
            ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesonInputTypeDef(
    _ClientCreateDetectorModelDetectorModelDefinitionstatesonInputTypeDef
):
    pass


_RequiredClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef", {"stateName": str}
)
_OptionalClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef",
    {
        "onInput": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputTypeDef,
        "onEnter": ClientCreateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef,
        "onExit": ClientCreateDetectorModelDetectorModelDefinitionstatesonExitTypeDef,
    },
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef(
    _RequiredClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef,
    _OptionalClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef,
):
    """
    - *(dict) --*

      Information that defines a state of a detector.
      - **stateName** *(string) --***[REQUIRED]**

        The name of the state.
    """


_RequiredClientCreateDetectorModelDetectorModelDefinitionTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModelDetectorModelDefinitionTypeDef",
    {"states": List[ClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef]},
)
_OptionalClientCreateDetectorModelDetectorModelDefinitionTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModelDetectorModelDefinitionTypeDef",
    {"initialStateName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionTypeDef(
    _RequiredClientCreateDetectorModelDetectorModelDefinitionTypeDef,
    _OptionalClientCreateDetectorModelDetectorModelDefinitionTypeDef,
):
    """
    Information that defines how the detectors operate.
    - **states** *(list) --***[REQUIRED]**

      Information about the states of the detector.
      - *(dict) --*

        Information that defines a state of a detector.
        - **stateName** *(string) --***[REQUIRED]**

          The name of the state.
    """


_ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef = TypedDict(
    "_ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelDescription": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal[
            "ACTIVE", "ACTIVATING", "INACTIVE", "DEPRECATED", "DRAFT", "PAUSED", "FAILED"
        ],
        "key": str,
        "evaluationMethod": Literal["BATCH", "SERIAL"],
    },
    total=False,
)


class ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef(
    _ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef
):
    """
    - **detectorModelConfiguration** *(dict) --*

      Information about how the detector model is configured.
      - **detectorModelName** *(string) --*

        The name of the detector model.
    """


_ClientCreateDetectorModelResponseTypeDef = TypedDict(
    "_ClientCreateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef
    },
    total=False,
)


class ClientCreateDetectorModelResponseTypeDef(_ClientCreateDetectorModelResponseTypeDef):
    """
    - *(dict) --*

      - **detectorModelConfiguration** *(dict) --*

        Information about how the detector model is configured.
        - **detectorModelName** *(string) --*

          The name of the detector model.
    """


_RequiredClientCreateDetectorModelTagsTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModelTagsTypeDef", {"key": str}
)
_OptionalClientCreateDetectorModelTagsTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModelTagsTypeDef", {"value": str}, total=False
)


class ClientCreateDetectorModelTagsTypeDef(
    _RequiredClientCreateDetectorModelTagsTypeDef, _OptionalClientCreateDetectorModelTagsTypeDef
):
    """
    - *(dict) --*

      Metadata that can be used to manage the resource.
      - **key** *(string) --***[REQUIRED]**

        The tag's key.
    """


_ClientCreateInputInputDefinitionattributesTypeDef = TypedDict(
    "_ClientCreateInputInputDefinitionattributesTypeDef", {"jsonPath": str}
)


class ClientCreateInputInputDefinitionattributesTypeDef(
    _ClientCreateInputInputDefinitionattributesTypeDef
):
    """
    - *(dict) --*

      The attributes from the JSON payload that are made available by the input. Inputs are derived
      from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
      contains a JSON payload, and those attributes (and their paired values) specified here are
      available for use in the ``condition`` expressions used by detectors.
      - **jsonPath** *(string) --***[REQUIRED]**

        An expression that specifies an attribute-value pair in a JSON structure. Use this to
        specify an attribute from the JSON payload that is made available by the input. Inputs are
        derived from messages sent to the AWS IoT Events system (``BatchPutMessage`` ). Each such
        message contains a JSON payload, and the attribute (and its paired value) specified here are
        available for use in the ``"condition"`` expressions used by detectors.
        Syntax: ``<field-name>.<field-name>...``
    """


_ClientCreateInputInputDefinitionTypeDef = TypedDict(
    "_ClientCreateInputInputDefinitionTypeDef",
    {"attributes": List[ClientCreateInputInputDefinitionattributesTypeDef]},
)


class ClientCreateInputInputDefinitionTypeDef(_ClientCreateInputInputDefinitionTypeDef):
    """
    The definition of the input.
    - **attributes** *(list) --***[REQUIRED]**

      The attributes from the JSON payload that are made available by the input. Inputs are derived
      from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
      contains a JSON payload, and those attributes (and their paired values) specified here are
      available for use in the ``"condition"`` expressions used by detectors that monitor this
      input.
      - *(dict) --*

        The attributes from the JSON payload that are made available by the input. Inputs are
        derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each
        such message contains a JSON payload, and those attributes (and their paired values)
        specified here are available for use in the ``condition`` expressions used by detectors.
        - **jsonPath** *(string) --***[REQUIRED]**

          An expression that specifies an attribute-value pair in a JSON structure. Use this to
          specify an attribute from the JSON payload that is made available by the input. Inputs are
          derived from messages sent to the AWS IoT Events system (``BatchPutMessage`` ). Each such
          message contains a JSON payload, and the attribute (and its paired value) specified here
          are available for use in the ``"condition"`` expressions used by detectors.
          Syntax: ``<field-name>.<field-name>...``
    """


_ClientCreateInputResponseinputConfigurationTypeDef = TypedDict(
    "_ClientCreateInputResponseinputConfigurationTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING"],
    },
    total=False,
)


class ClientCreateInputResponseinputConfigurationTypeDef(
    _ClientCreateInputResponseinputConfigurationTypeDef
):
    """
    - **inputConfiguration** *(dict) --*

      Information about the configuration of the input.
      - **inputName** *(string) --*

        The name of the input.
    """


_ClientCreateInputResponseTypeDef = TypedDict(
    "_ClientCreateInputResponseTypeDef",
    {"inputConfiguration": ClientCreateInputResponseinputConfigurationTypeDef},
    total=False,
)


class ClientCreateInputResponseTypeDef(_ClientCreateInputResponseTypeDef):
    """
    - *(dict) --*

      - **inputConfiguration** *(dict) --*

        Information about the configuration of the input.
        - **inputName** *(string) --*

          The name of the input.
    """


_RequiredClientCreateInputTagsTypeDef = TypedDict(
    "_RequiredClientCreateInputTagsTypeDef", {"key": str}
)
_OptionalClientCreateInputTagsTypeDef = TypedDict(
    "_OptionalClientCreateInputTagsTypeDef", {"value": str}, total=False
)


class ClientCreateInputTagsTypeDef(
    _RequiredClientCreateInputTagsTypeDef, _OptionalClientCreateInputTagsTypeDef
):
    """
    - *(dict) --*

      Metadata that can be used to manage the resource.
      - **key** *(string) --***[REQUIRED]**

        The tag's key.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelDescription": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal[
            "ACTIVE", "ACTIVATING", "INACTIVE", "DEPRECATED", "DRAFT", "PAUSED", "FAILED"
        ],
        "key": str,
        "evaluationMethod": Literal["BATCH", "SERIAL"],
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    {
        "setVariable": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef,
        "sns": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef,
        "iotTopicPublish": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef,
        "clearTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef,
        "resetTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef,
        "lambda": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef,
        "iotEvents": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef,
        "sqs": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef,
        "firehose": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef",
    {
        "events": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    {
        "setVariable": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef,
        "sns": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef,
        "iotTopicPublish": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef,
        "clearTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef,
        "resetTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef,
        "lambda": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef,
        "iotEvents": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef,
        "sqs": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef,
        "firehose": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef",
    {
        "events": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    {
        "setVariable": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef,
        "sns": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef,
        "iotTopicPublish": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef,
        "clearTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef,
        "resetTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef,
        "lambda": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef,
        "iotEvents": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef,
        "sqs": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef,
        "firehose": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    {
        "setVariable": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef,
        "sns": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef,
        "iotTopicPublish": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef,
        "clearTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef,
        "resetTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef,
        "lambda": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef,
        "iotEvents": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef,
        "sqs": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef,
        "firehose": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
        ],
        "nextState": str,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef",
    {
        "events": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef
        ],
        "transitionEvents": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef
):
    pass


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef",
    {
        "stateName": str,
        "onInput": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef,
        "onEnter": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef,
        "onExit": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef
):
    """
    - *(dict) --*

      Information that defines a state of a detector.
      - **stateName** *(string) --*

        The name of the state.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef",
    {
        "states": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef
        ],
        "initialStateName": str,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef
):
    """
    - **detectorModelDefinition** *(dict) --*

      Information that defines how a detector operates.
      - **states** *(list) --*

        Information about the states of the detector.
        - *(dict) --*

          Information that defines a state of a detector.
          - **stateName** *(string) --*

            The name of the state.
    """


_ClientDescribeDetectorModelResponsedetectorModelTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModelTypeDef",
    {
        "detectorModelDefinition": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef,
        "detectorModelConfiguration": ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModelTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModelTypeDef
):
    """
    - **detectorModel** *(dict) --*

      Information about the detector model.
      - **detectorModelDefinition** *(dict) --*

        Information that defines how a detector operates.
        - **states** *(list) --*

          Information about the states of the detector.
          - *(dict) --*

            Information that defines a state of a detector.
            - **stateName** *(string) --*

              The name of the state.
    """


_ClientDescribeDetectorModelResponseTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponseTypeDef",
    {"detectorModel": ClientDescribeDetectorModelResponsedetectorModelTypeDef},
    total=False,
)


class ClientDescribeDetectorModelResponseTypeDef(_ClientDescribeDetectorModelResponseTypeDef):
    """
    - *(dict) --*

      - **detectorModel** *(dict) --*

        Information about the detector model.
        - **detectorModelDefinition** *(dict) --*

          Information that defines how a detector operates.
          - **states** *(list) --*

            Information about the states of the detector.
            - *(dict) --*

              Information that defines a state of a detector.
              - **stateName** *(string) --*

                The name of the state.
    """


_ClientDescribeInputResponseinputinputConfigurationTypeDef = TypedDict(
    "_ClientDescribeInputResponseinputinputConfigurationTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING"],
    },
    total=False,
)


class ClientDescribeInputResponseinputinputConfigurationTypeDef(
    _ClientDescribeInputResponseinputinputConfigurationTypeDef
):
    """
    - **inputConfiguration** *(dict) --*

      Information about the configuration of an input.
      - **inputName** *(string) --*

        The name of the input.
    """


_ClientDescribeInputResponseinputinputDefinitionattributesTypeDef = TypedDict(
    "_ClientDescribeInputResponseinputinputDefinitionattributesTypeDef",
    {"jsonPath": str},
    total=False,
)


class ClientDescribeInputResponseinputinputDefinitionattributesTypeDef(
    _ClientDescribeInputResponseinputinputDefinitionattributesTypeDef
):
    pass


_ClientDescribeInputResponseinputinputDefinitionTypeDef = TypedDict(
    "_ClientDescribeInputResponseinputinputDefinitionTypeDef",
    {"attributes": List[ClientDescribeInputResponseinputinputDefinitionattributesTypeDef]},
    total=False,
)


class ClientDescribeInputResponseinputinputDefinitionTypeDef(
    _ClientDescribeInputResponseinputinputDefinitionTypeDef
):
    pass


_ClientDescribeInputResponseinputTypeDef = TypedDict(
    "_ClientDescribeInputResponseinputTypeDef",
    {
        "inputConfiguration": ClientDescribeInputResponseinputinputConfigurationTypeDef,
        "inputDefinition": ClientDescribeInputResponseinputinputDefinitionTypeDef,
    },
    total=False,
)


class ClientDescribeInputResponseinputTypeDef(_ClientDescribeInputResponseinputTypeDef):
    """
    - **input** *(dict) --*

      Information about the input.
      - **inputConfiguration** *(dict) --*

        Information about the configuration of an input.
        - **inputName** *(string) --*

          The name of the input.
    """


_ClientDescribeInputResponseTypeDef = TypedDict(
    "_ClientDescribeInputResponseTypeDef",
    {"input": ClientDescribeInputResponseinputTypeDef},
    total=False,
)


class ClientDescribeInputResponseTypeDef(_ClientDescribeInputResponseTypeDef):
    """
    - *(dict) --*

      - **input** *(dict) --*

        Information about the input.
        - **inputConfiguration** *(dict) --*

          Information about the configuration of an input.
          - **inputName** *(string) --*

            The name of the input.
    """


_ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef = TypedDict(
    "_ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef",
    {"detectorModelName": str, "keyValue": str},
    total=False,
)


class ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef(
    _ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef
):
    pass


_ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef = TypedDict(
    "_ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef",
    {
        "roleArn": str,
        "level": Literal["ERROR", "INFO", "DEBUG"],
        "enabled": bool,
        "detectorDebugOptions": List[
            ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef(
    _ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef
):
    """
    - **loggingOptions** *(dict) --*

      The current settings of the AWS IoT Events logging options.
      - **roleArn** *(string) --*

        The ARN of the role that grants permission to AWS IoT Events to perform logging.
    """


_ClientDescribeLoggingOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeLoggingOptionsResponseTypeDef",
    {"loggingOptions": ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef},
    total=False,
)


class ClientDescribeLoggingOptionsResponseTypeDef(_ClientDescribeLoggingOptionsResponseTypeDef):
    """
    - *(dict) --*

      - **loggingOptions** *(dict) --*

        The current settings of the AWS IoT Events logging options.
        - **roleArn** *(string) --*

          The ARN of the role that grants permission to AWS IoT Events to perform logging.
    """


_ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef = TypedDict(
    "_ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal[
            "ACTIVE", "ACTIVATING", "INACTIVE", "DEPRECATED", "DRAFT", "PAUSED", "FAILED"
        ],
        "evaluationMethod": Literal["BATCH", "SERIAL"],
    },
    total=False,
)


class ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef(
    _ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef
):
    """
    - *(dict) --*

      Information about the detector model version.
      - **detectorModelName** *(string) --*

        The name of the detector model.
    """


_ClientListDetectorModelVersionsResponseTypeDef = TypedDict(
    "_ClientListDetectorModelVersionsResponseTypeDef",
    {
        "detectorModelVersionSummaries": List[
            ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListDetectorModelVersionsResponseTypeDef(
    _ClientListDetectorModelVersionsResponseTypeDef
):
    """
    - *(dict) --*

      - **detectorModelVersionSummaries** *(list) --*

        Summary information about the detector model versions.
        - *(dict) --*

          Information about the detector model version.
          - **detectorModelName** *(string) --*

            The name of the detector model.
    """


_ClientListDetectorModelsResponsedetectorModelSummariesTypeDef = TypedDict(
    "_ClientListDetectorModelsResponsedetectorModelSummariesTypeDef",
    {"detectorModelName": str, "detectorModelDescription": str, "creationTime": datetime},
    total=False,
)


class ClientListDetectorModelsResponsedetectorModelSummariesTypeDef(
    _ClientListDetectorModelsResponsedetectorModelSummariesTypeDef
):
    """
    - *(dict) --*

      Information about the detector model.
      - **detectorModelName** *(string) --*

        The name of the detector model.
    """


_ClientListDetectorModelsResponseTypeDef = TypedDict(
    "_ClientListDetectorModelsResponseTypeDef",
    {
        "detectorModelSummaries": List[
            ClientListDetectorModelsResponsedetectorModelSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListDetectorModelsResponseTypeDef(_ClientListDetectorModelsResponseTypeDef):
    """
    - *(dict) --*

      - **detectorModelSummaries** *(list) --*

        Summary information about the detector models.
        - *(dict) --*

          Information about the detector model.
          - **detectorModelName** *(string) --*

            The name of the detector model.
    """


_ClientListInputsResponseinputSummariesTypeDef = TypedDict(
    "_ClientListInputsResponseinputSummariesTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING"],
    },
    total=False,
)


class ClientListInputsResponseinputSummariesTypeDef(_ClientListInputsResponseinputSummariesTypeDef):
    """
    - *(dict) --*

      Information about the input.
      - **inputName** *(string) --*

        The name of the input.
    """


_ClientListInputsResponseTypeDef = TypedDict(
    "_ClientListInputsResponseTypeDef",
    {"inputSummaries": List[ClientListInputsResponseinputSummariesTypeDef], "nextToken": str},
    total=False,
)


class ClientListInputsResponseTypeDef(_ClientListInputsResponseTypeDef):
    """
    - *(dict) --*

      - **inputSummaries** *(list) --*

        Summary information about the inputs.
        - *(dict) --*

          Information about the input.
          - **inputName** *(string) --*

            The name of the input.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientListTagsForResourceResponsetagsTypeDef(_ClientListTagsForResourceResponsetagsTypeDef):
    """
    - *(dict) --*

      Metadata that can be used to manage the resource.
      - **key** *(string) --*

        The tag's key.
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

        The list of tags assigned to the resource.
        - *(dict) --*

          Metadata that can be used to manage the resource.
          - **key** *(string) --*

            The tag's key.
    """


_ClientPutLoggingOptionsLoggingOptionsdetectorDebugOptionsTypeDef = TypedDict(
    "_ClientPutLoggingOptionsLoggingOptionsdetectorDebugOptionsTypeDef",
    {"detectorModelName": str, "keyValue": str},
    total=False,
)


class ClientPutLoggingOptionsLoggingOptionsdetectorDebugOptionsTypeDef(
    _ClientPutLoggingOptionsLoggingOptionsdetectorDebugOptionsTypeDef
):
    pass


_RequiredClientPutLoggingOptionsLoggingOptionsTypeDef = TypedDict(
    "_RequiredClientPutLoggingOptionsLoggingOptionsTypeDef", {"roleArn": str}
)
_OptionalClientPutLoggingOptionsLoggingOptionsTypeDef = TypedDict(
    "_OptionalClientPutLoggingOptionsLoggingOptionsTypeDef",
    {
        "level": Literal["ERROR", "INFO", "DEBUG"],
        "enabled": bool,
        "detectorDebugOptions": List[
            ClientPutLoggingOptionsLoggingOptionsdetectorDebugOptionsTypeDef
        ],
    },
    total=False,
)


class ClientPutLoggingOptionsLoggingOptionsTypeDef(
    _RequiredClientPutLoggingOptionsLoggingOptionsTypeDef,
    _OptionalClientPutLoggingOptionsLoggingOptionsTypeDef,
):
    """
    The new values of the AWS IoT Events logging options.
    - **roleArn** *(string) --***[REQUIRED]**

      The ARN of the role that grants permission to AWS IoT Events to perform logging.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      Metadata that can be used to manage the resource.
      - **key** *(string) --***[REQUIRED]**

        The tag's key.
    """


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    {
        "setVariable": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef,
        "sns": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef,
        "iotTopicPublish": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef,
        "clearTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef,
        "resetTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef,
        "lambda": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef,
        "iotEvents": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef,
        "sqs": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef,
        "firehose": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef",
    {"events": List[ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef]},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    {
        "setVariable": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef,
        "sns": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef,
        "iotTopicPublish": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef,
        "clearTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef,
        "resetTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef,
        "lambda": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef,
        "iotEvents": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef,
        "sqs": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef,
        "firehose": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExitTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonExitTypeDef",
    {"events": List[ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef]},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonExitTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonExitTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    {
        "setVariable": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef,
        "sns": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef,
        "iotTopicPublish": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef,
        "clearTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef,
        "resetTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef,
        "lambda": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef,
        "iotEvents": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef,
        "sqs": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef,
        "firehose": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    {
        "setVariable": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef,
        "sns": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef,
        "iotTopicPublish": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef,
        "clearTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef,
        "resetTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef,
        "lambda": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef,
        "iotEvents": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef,
        "sqs": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef,
        "firehose": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
        ],
        "nextState": str,
    },
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef
):
    pass


_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputTypeDef = TypedDict(
    "_ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputTypeDef",
    {
        "events": List[ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef],
        "transitionEvents": List[
            ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputTypeDef(
    _ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputTypeDef
):
    pass


_RequiredClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef", {"stateName": str}
)
_OptionalClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef",
    {
        "onInput": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputTypeDef,
        "onEnter": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef,
        "onExit": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExitTypeDef,
    },
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef(
    _RequiredClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef,
    _OptionalClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef,
):
    """
    - *(dict) --*

      Information that defines a state of a detector.
      - **stateName** *(string) --***[REQUIRED]**

        The name of the state.
    """


_RequiredClientUpdateDetectorModelDetectorModelDefinitionTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModelDetectorModelDefinitionTypeDef",
    {"states": List[ClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef]},
)
_OptionalClientUpdateDetectorModelDetectorModelDefinitionTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModelDetectorModelDefinitionTypeDef",
    {"initialStateName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionTypeDef(
    _RequiredClientUpdateDetectorModelDetectorModelDefinitionTypeDef,
    _OptionalClientUpdateDetectorModelDetectorModelDefinitionTypeDef,
):
    """
    Information that defines how a detector operates.
    - **states** *(list) --***[REQUIRED]**

      Information about the states of the detector.
      - *(dict) --*

        Information that defines a state of a detector.
        - **stateName** *(string) --***[REQUIRED]**

          The name of the state.
    """


_ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef = TypedDict(
    "_ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelDescription": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal[
            "ACTIVE", "ACTIVATING", "INACTIVE", "DEPRECATED", "DRAFT", "PAUSED", "FAILED"
        ],
        "key": str,
        "evaluationMethod": Literal["BATCH", "SERIAL"],
    },
    total=False,
)


class ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef(
    _ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef
):
    """
    - **detectorModelConfiguration** *(dict) --*

      Information about how the detector model is configured.
      - **detectorModelName** *(string) --*

        The name of the detector model.
    """


_ClientUpdateDetectorModelResponseTypeDef = TypedDict(
    "_ClientUpdateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef
    },
    total=False,
)


class ClientUpdateDetectorModelResponseTypeDef(_ClientUpdateDetectorModelResponseTypeDef):
    """
    - *(dict) --*

      - **detectorModelConfiguration** *(dict) --*

        Information about how the detector model is configured.
        - **detectorModelName** *(string) --*

          The name of the detector model.
    """


_ClientUpdateInputInputDefinitionattributesTypeDef = TypedDict(
    "_ClientUpdateInputInputDefinitionattributesTypeDef", {"jsonPath": str}
)


class ClientUpdateInputInputDefinitionattributesTypeDef(
    _ClientUpdateInputInputDefinitionattributesTypeDef
):
    """
    - *(dict) --*

      The attributes from the JSON payload that are made available by the input. Inputs are derived
      from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
      contains a JSON payload, and those attributes (and their paired values) specified here are
      available for use in the ``condition`` expressions used by detectors.
      - **jsonPath** *(string) --***[REQUIRED]**

        An expression that specifies an attribute-value pair in a JSON structure. Use this to
        specify an attribute from the JSON payload that is made available by the input. Inputs are
        derived from messages sent to the AWS IoT Events system (``BatchPutMessage`` ). Each such
        message contains a JSON payload, and the attribute (and its paired value) specified here are
        available for use in the ``"condition"`` expressions used by detectors.
        Syntax: ``<field-name>.<field-name>...``
    """


_ClientUpdateInputInputDefinitionTypeDef = TypedDict(
    "_ClientUpdateInputInputDefinitionTypeDef",
    {"attributes": List[ClientUpdateInputInputDefinitionattributesTypeDef]},
)


class ClientUpdateInputInputDefinitionTypeDef(_ClientUpdateInputInputDefinitionTypeDef):
    """
    The definition of the input.
    - **attributes** *(list) --***[REQUIRED]**

      The attributes from the JSON payload that are made available by the input. Inputs are derived
      from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
      contains a JSON payload, and those attributes (and their paired values) specified here are
      available for use in the ``"condition"`` expressions used by detectors that monitor this
      input.
      - *(dict) --*

        The attributes from the JSON payload that are made available by the input. Inputs are
        derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each
        such message contains a JSON payload, and those attributes (and their paired values)
        specified here are available for use in the ``condition`` expressions used by detectors.
        - **jsonPath** *(string) --***[REQUIRED]**

          An expression that specifies an attribute-value pair in a JSON structure. Use this to
          specify an attribute from the JSON payload that is made available by the input. Inputs are
          derived from messages sent to the AWS IoT Events system (``BatchPutMessage`` ). Each such
          message contains a JSON payload, and the attribute (and its paired value) specified here
          are available for use in the ``"condition"`` expressions used by detectors.
          Syntax: ``<field-name>.<field-name>...``
    """


_ClientUpdateInputResponseinputConfigurationTypeDef = TypedDict(
    "_ClientUpdateInputResponseinputConfigurationTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING"],
    },
    total=False,
)


class ClientUpdateInputResponseinputConfigurationTypeDef(
    _ClientUpdateInputResponseinputConfigurationTypeDef
):
    """
    - **inputConfiguration** *(dict) --*

      Information about the configuration of the input.
      - **inputName** *(string) --*

        The name of the input.
    """


_ClientUpdateInputResponseTypeDef = TypedDict(
    "_ClientUpdateInputResponseTypeDef",
    {"inputConfiguration": ClientUpdateInputResponseinputConfigurationTypeDef},
    total=False,
)


class ClientUpdateInputResponseTypeDef(_ClientUpdateInputResponseTypeDef):
    """
    - *(dict) --*

      - **inputConfiguration** *(dict) --*

        Information about the configuration of the input.
        - **inputName** *(string) --*

          The name of the input.
    """
