"Main interface for pinpoint-sms-voice service type defs"
from __future__ import annotations

from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchLogsDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseTypeDef",
    "ClientSendVoiceMessageContentCallInstructionsMessageTypeDef",
    "ClientSendVoiceMessageContentPlainTextMessageTypeDef",
    "ClientSendVoiceMessageContentSSMLMessageTypeDef",
    "ClientSendVoiceMessageContentTypeDef",
    "ClientSendVoiceMessageResponseTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
)


_ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef",
    {"IamRoleArn": str, "LogGroupArn": str},
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef
):
    """
    - **CloudWatchLogsDestination** *(dict) --*An object that contains information about an event
    destination that sends data to Amazon CloudWatch Logs.

      - **IamRoleArn** *(string) --*The Amazon Resource Name (ARN) of an Amazon Identity and Access
      Management (IAM) role that is able to write event data to an Amazon CloudWatch destination.
      - **LogGroupArn** *(string) --*The name of the Amazon CloudWatch Log Group that you want to
      record events in.
    """


_ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    {"DeliveryStreamArn": str, "IamRoleArn": str},
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef
):
    pass


_ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    {"TopicArn": str},
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef
):
    pass


_ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef,
        "Enabled": bool,
        "KinesisFirehoseDestination": ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "MatchingEventTypes": List[
            Literal[
                "INITIATED_CALL",
                "RINGING",
                "ANSWERED",
                "COMPLETED_CALL",
                "BUSY",
                "FAILED",
                "NO_ANSWER",
            ]
        ],
        "SnsDestination": ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef,
    },
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef
):
    """
    - **CloudWatchLogsDestination** *(dict) --*An object that contains information about an event
    destination that sends data to Amazon CloudWatch Logs.

      - **IamRoleArn** *(string) --*The Amazon Resource Name (ARN) of an Amazon Identity and Access
      Management (IAM) role that is able to write event data to an Amazon CloudWatch destination.
      - **LogGroupArn** *(string) --*The name of the Amazon CloudWatch Log Group that you want to
      record events in.
    """


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchLogsDestinationTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchLogsDestinationTypeDef",
    {"IamRoleArn": str, "LogGroupArn": str},
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchLogsDestinationTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchLogsDestinationTypeDef
):
    """
    - **CloudWatchLogsDestination** *(dict) --*An object that contains information about an event
    destination that sends data to Amazon CloudWatch Logs.

      - **IamRoleArn** *(string) --*The Amazon Resource Name (ARN) of an Amazon Identity and Access
      Management (IAM) role that is able to write event data to an Amazon CloudWatch destination.
      - **LogGroupArn** *(string) --*The name of the Amazon CloudWatch Log Group that you want to
      record events in.
    """


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    {"DeliveryStreamArn": str, "IamRoleArn": str},
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef
):
    pass


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef",
    {"TopicArn": str},
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef
):
    pass


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef",
    {
        "CloudWatchLogsDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchLogsDestinationTypeDef,
        "Enabled": bool,
        "KinesisFirehoseDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef,
        "MatchingEventTypes": List[
            Literal[
                "INITIATED_CALL",
                "RINGING",
                "ANSWERED",
                "COMPLETED_CALL",
                "BUSY",
                "FAILED",
                "NO_ANSWER",
            ]
        ],
        "Name": str,
        "SnsDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef,
    },
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef
):
    """
    - *(dict) --*An object that defines an event destination.

      - **CloudWatchLogsDestination** *(dict) --*An object that contains information about an event
      destination that sends data to Amazon CloudWatch Logs.

        - **IamRoleArn** *(string) --*The Amazon Resource Name (ARN) of an Amazon Identity and
        Access Management (IAM) role that is able to write event data to an Amazon CloudWatch
        destination.
        - **LogGroupArn** *(string) --*The name of the Amazon CloudWatch Log Group that you want to
        record events in.
    """


_ClientGetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseTypeDef",
    {
        "EventDestinations": List[
            ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef
        ]
    },
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseTypeDef
):
    """
    - *(dict) --*GetConfigurationSetEventDestinationsResponse

      - **EventDestinations** *(list) --*An array of EventDestination objects. Each EventDestination
      object includes ARNs and other information that define an event destination.

        - *(dict) --*An object that defines an event destination.

          - **CloudWatchLogsDestination** *(dict) --*An object that contains information about an
          event destination that sends data to Amazon CloudWatch Logs.

            - **IamRoleArn** *(string) --*The Amazon Resource Name (ARN) of an Amazon Identity and
            Access Management (IAM) role that is able to write event data to an Amazon CloudWatch
            destination.
            - **LogGroupArn** *(string) --*The name of the Amazon CloudWatch Log Group that you want
            to record events in.
    """


_ClientSendVoiceMessageContentCallInstructionsMessageTypeDef = TypedDict(
    "_ClientSendVoiceMessageContentCallInstructionsMessageTypeDef", {"Text": str}, total=False
)


class ClientSendVoiceMessageContentCallInstructionsMessageTypeDef(
    _ClientSendVoiceMessageContentCallInstructionsMessageTypeDef
):
    """
    - **CallInstructionsMessage** *(dict) --*An object that defines a message that contains text
    formatted using Amazon Pinpoint Voice Instructions markup.

      - **Text** *(string) --*The language to use when delivering the message. For a complete list
      of supported languages, see the Amazon Polly Developer Guide.
    """


_ClientSendVoiceMessageContentPlainTextMessageTypeDef = TypedDict(
    "_ClientSendVoiceMessageContentPlainTextMessageTypeDef",
    {"LanguageCode": str, "Text": str, "VoiceId": str},
    total=False,
)


class ClientSendVoiceMessageContentPlainTextMessageTypeDef(
    _ClientSendVoiceMessageContentPlainTextMessageTypeDef
):
    pass


_ClientSendVoiceMessageContentSSMLMessageTypeDef = TypedDict(
    "_ClientSendVoiceMessageContentSSMLMessageTypeDef",
    {"LanguageCode": str, "Text": str, "VoiceId": str},
    total=False,
)


class ClientSendVoiceMessageContentSSMLMessageTypeDef(
    _ClientSendVoiceMessageContentSSMLMessageTypeDef
):
    pass


_ClientSendVoiceMessageContentTypeDef = TypedDict(
    "_ClientSendVoiceMessageContentTypeDef",
    {
        "CallInstructionsMessage": ClientSendVoiceMessageContentCallInstructionsMessageTypeDef,
        "PlainTextMessage": ClientSendVoiceMessageContentPlainTextMessageTypeDef,
        "SSMLMessage": ClientSendVoiceMessageContentSSMLMessageTypeDef,
    },
    total=False,
)


class ClientSendVoiceMessageContentTypeDef(_ClientSendVoiceMessageContentTypeDef):
    """
    - **CallInstructionsMessage** *(dict) --*An object that defines a message that contains text
    formatted using Amazon Pinpoint Voice Instructions markup.

      - **Text** *(string) --*The language to use when delivering the message. For a complete list
      of supported languages, see the Amazon Polly Developer Guide.
    """


_ClientSendVoiceMessageResponseTypeDef = TypedDict(
    "_ClientSendVoiceMessageResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendVoiceMessageResponseTypeDef(_ClientSendVoiceMessageResponseTypeDef):
    """
    - *(dict) --*SendVoiceMessageResponse

      - **MessageId** *(string) --*A unique identifier for the voice message.
    """


_ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef",
    {"IamRoleArn": str, "LogGroupArn": str},
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef
):
    """
    - **CloudWatchLogsDestination** *(dict) --*An object that contains information about an event
    destination that sends data to Amazon CloudWatch Logs.

      - **IamRoleArn** *(string) --*The Amazon Resource Name (ARN) of an Amazon Identity and Access
      Management (IAM) role that is able to write event data to an Amazon CloudWatch destination.
      - **LogGroupArn** *(string) --*The name of the Amazon CloudWatch Log Group that you want to
      record events in.
    """


_ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    {"DeliveryStreamArn": str, "IamRoleArn": str},
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef
):
    pass


_ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    {"TopicArn": str},
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef
):
    pass


_ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef,
        "Enabled": bool,
        "KinesisFirehoseDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "MatchingEventTypes": List[
            Literal[
                "INITIATED_CALL",
                "RINGING",
                "ANSWERED",
                "COMPLETED_CALL",
                "BUSY",
                "FAILED",
                "NO_ANSWER",
            ]
        ],
        "SnsDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef,
    },
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef
):
    """
    - **CloudWatchLogsDestination** *(dict) --*An object that contains information about an event
    destination that sends data to Amazon CloudWatch Logs.

      - **IamRoleArn** *(string) --*The Amazon Resource Name (ARN) of an Amazon Identity and Access
      Management (IAM) role that is able to write event data to an Amazon CloudWatch destination.
      - **LogGroupArn** *(string) --*The name of the Amazon CloudWatch Log Group that you want to
      record events in.
    """
