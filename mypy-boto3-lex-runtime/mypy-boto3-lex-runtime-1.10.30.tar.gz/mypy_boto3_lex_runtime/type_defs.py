"Main interface for lex-runtime service type defs"
from __future__ import annotations

from typing import Any, Dict, List, Union
from botocore.response import StreamingBody
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientDeleteSessionResponseTypeDef",
    "ClientGetSessionResponsedialogActionTypeDef",
    "ClientGetSessionResponserecentIntentSummaryViewTypeDef",
    "ClientGetSessionResponseTypeDef",
    "ClientPostContentResponseTypeDef",
    "ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef",
    "ClientPostTextResponseresponseCardgenericAttachmentsTypeDef",
    "ClientPostTextResponseresponseCardTypeDef",
    "ClientPostTextResponsesentimentResponseTypeDef",
    "ClientPostTextResponseTypeDef",
    "ClientPutSessionDialogActionTypeDef",
    "ClientPutSessionRecentIntentSummaryViewTypeDef",
    "ClientPutSessionResponseTypeDef",
)


_ClientDeleteSessionResponseTypeDef = TypedDict(
    "_ClientDeleteSessionResponseTypeDef",
    {"botName": str, "botAlias": str, "userId": str, "sessionId": str},
    total=False,
)


class ClientDeleteSessionResponseTypeDef(_ClientDeleteSessionResponseTypeDef):
    """
    - *(dict) --*

      - **botName** *(string) --*

        The name of the bot associated with the session data.
    """


_ClientGetSessionResponsedialogActionTypeDef = TypedDict(
    "_ClientGetSessionResponsedialogActionTypeDef",
    {
        "type": Literal["ElicitIntent", "ConfirmIntent", "ElicitSlot", "Close", "Delegate"],
        "intentName": str,
        "slots": Dict[str, str],
        "slotToElicit": str,
        "fulfillmentState": Literal["Fulfilled", "Failed", "ReadyForFulfillment"],
        "message": str,
        "messageFormat": Literal["PlainText", "CustomPayload", "SSML", "Composite"],
    },
    total=False,
)


class ClientGetSessionResponsedialogActionTypeDef(_ClientGetSessionResponsedialogActionTypeDef):
    pass


_ClientGetSessionResponserecentIntentSummaryViewTypeDef = TypedDict(
    "_ClientGetSessionResponserecentIntentSummaryViewTypeDef",
    {
        "intentName": str,
        "checkpointLabel": str,
        "slots": Dict[str, str],
        "confirmationStatus": Literal["None", "Confirmed", "Denied"],
        "dialogActionType": Literal[
            "ElicitIntent", "ConfirmIntent", "ElicitSlot", "Close", "Delegate"
        ],
        "fulfillmentState": Literal["Fulfilled", "Failed", "ReadyForFulfillment"],
        "slotToElicit": str,
    },
    total=False,
)


class ClientGetSessionResponserecentIntentSummaryViewTypeDef(
    _ClientGetSessionResponserecentIntentSummaryViewTypeDef
):
    """
    - *(dict) --*

      Provides information about the state of an intent. You can use this information to get the
      current state of an intent so that you can process the intent, or so that you can return the
      intent to its previous state.
      - **intentName** *(string) --*

        The name of the intent.
    """


_ClientGetSessionResponseTypeDef = TypedDict(
    "_ClientGetSessionResponseTypeDef",
    {
        "recentIntentSummaryView": List[ClientGetSessionResponserecentIntentSummaryViewTypeDef],
        "sessionAttributes": Dict[str, str],
        "sessionId": str,
        "dialogAction": ClientGetSessionResponsedialogActionTypeDef,
    },
    total=False,
)


class ClientGetSessionResponseTypeDef(_ClientGetSessionResponseTypeDef):
    """
    - *(dict) --*

      - **recentIntentSummaryView** *(list) --*

        An array of information about the intents used in the session. The array can contain a
        maximum of three summaries. If more than three intents are used in the session, the
        ``recentIntentSummaryView`` operation contains information about the last three intents
        used.
        If you set the ``checkpointLabelFilter`` parameter in the request, the array contains only
        the intents with the specified label.
        - *(dict) --*

          Provides information about the state of an intent. You can use this information to get the
          current state of an intent so that you can process the intent, or so that you can return
          the intent to its previous state.
          - **intentName** *(string) --*

            The name of the intent.
    """


_ClientPostContentResponseTypeDef = TypedDict(
    "_ClientPostContentResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "slots": Union[Dict[str, Any], List[Any], int, float, str, bool, None],
        "sessionAttributes": Union[Dict[str, Any], List[Any], int, float, str, bool, None],
        "sentimentResponse": str,
        "message": str,
        "messageFormat": Literal["PlainText", "CustomPayload", "SSML", "Composite"],
        "dialogState": Literal[
            "ElicitIntent",
            "ConfirmIntent",
            "ElicitSlot",
            "Fulfilled",
            "ReadyForFulfillment",
            "Failed",
        ],
        "slotToElicit": str,
        "inputTranscript": str,
        "audioStream": StreamingBody,
        "sessionId": str,
    },
    total=False,
)


class ClientPostContentResponseTypeDef(_ClientPostContentResponseTypeDef):
    """
    - *(dict) --*

      - **contentType** *(string) --*

        Content type as specified in the ``Accept`` HTTP header in the request.
    """


_ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef = TypedDict(
    "_ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef",
    {"text": str, "value": str},
    total=False,
)


class ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef(
    _ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef
):
    pass


_ClientPostTextResponseresponseCardgenericAttachmentsTypeDef = TypedDict(
    "_ClientPostTextResponseresponseCardgenericAttachmentsTypeDef",
    {
        "title": str,
        "subTitle": str,
        "attachmentLinkUrl": str,
        "imageUrl": str,
        "buttons": List[ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef],
    },
    total=False,
)


class ClientPostTextResponseresponseCardgenericAttachmentsTypeDef(
    _ClientPostTextResponseresponseCardgenericAttachmentsTypeDef
):
    pass


_ClientPostTextResponseresponseCardTypeDef = TypedDict(
    "_ClientPostTextResponseresponseCardTypeDef",
    {
        "version": str,
        "contentType": str,
        "genericAttachments": List[ClientPostTextResponseresponseCardgenericAttachmentsTypeDef],
    },
    total=False,
)


class ClientPostTextResponseresponseCardTypeDef(_ClientPostTextResponseresponseCardTypeDef):
    pass


_ClientPostTextResponsesentimentResponseTypeDef = TypedDict(
    "_ClientPostTextResponsesentimentResponseTypeDef",
    {"sentimentLabel": str, "sentimentScore": str},
    total=False,
)


class ClientPostTextResponsesentimentResponseTypeDef(
    _ClientPostTextResponsesentimentResponseTypeDef
):
    pass


_ClientPostTextResponseTypeDef = TypedDict(
    "_ClientPostTextResponseTypeDef",
    {
        "intentName": str,
        "slots": Dict[str, str],
        "sessionAttributes": Dict[str, str],
        "message": str,
        "sentimentResponse": ClientPostTextResponsesentimentResponseTypeDef,
        "messageFormat": Literal["PlainText", "CustomPayload", "SSML", "Composite"],
        "dialogState": Literal[
            "ElicitIntent",
            "ConfirmIntent",
            "ElicitSlot",
            "Fulfilled",
            "ReadyForFulfillment",
            "Failed",
        ],
        "slotToElicit": str,
        "responseCard": ClientPostTextResponseresponseCardTypeDef,
        "sessionId": str,
    },
    total=False,
)


class ClientPostTextResponseTypeDef(_ClientPostTextResponseTypeDef):
    """
    - *(dict) --*

      - **intentName** *(string) --*

        The current user intent that Amazon Lex is aware of.
    """


_RequiredClientPutSessionDialogActionTypeDef = TypedDict(
    "_RequiredClientPutSessionDialogActionTypeDef",
    {"type": Literal["ElicitIntent", "ConfirmIntent", "ElicitSlot", "Close", "Delegate"]},
)
_OptionalClientPutSessionDialogActionTypeDef = TypedDict(
    "_OptionalClientPutSessionDialogActionTypeDef",
    {
        "intentName": str,
        "slots": Dict[str, str],
        "slotToElicit": str,
        "fulfillmentState": Literal["Fulfilled", "Failed", "ReadyForFulfillment"],
        "message": str,
        "messageFormat": Literal["PlainText", "CustomPayload", "SSML", "Composite"],
    },
    total=False,
)


class ClientPutSessionDialogActionTypeDef(
    _RequiredClientPutSessionDialogActionTypeDef, _OptionalClientPutSessionDialogActionTypeDef
):
    """
    Sets the next action that the bot should take to fulfill the conversation.
    - **type** *(string) --***[REQUIRED]**

      The next action that the bot should take in its interaction with the user. The possible values
      are:
      * ``ConfirmIntent`` - The next action is asking the user if the intent is complete and ready
      to be fulfilled. This is a yes/no question such as "Place the order?"
      * ``Close`` - Indicates that the there will not be a response from the user. For example, the
      statement "Your order has been placed" does not require a response.
      * ``Delegate`` - The next action is determined by Amazon Lex.
      * ``ElicitIntent`` - The next action is to determine the intent that the user wants to
      fulfill.
      * ``ElicitSlot`` - The next action is to elicit a slot value from the user.
    """


_ClientPutSessionRecentIntentSummaryViewTypeDef = TypedDict(
    "_ClientPutSessionRecentIntentSummaryViewTypeDef",
    {
        "intentName": str,
        "checkpointLabel": str,
        "slots": Dict[str, str],
        "confirmationStatus": Literal["None", "Confirmed", "Denied"],
        "dialogActionType": Literal[
            "ElicitIntent", "ConfirmIntent", "ElicitSlot", "Close", "Delegate"
        ],
        "fulfillmentState": Literal["Fulfilled", "Failed", "ReadyForFulfillment"],
        "slotToElicit": str,
    },
    total=False,
)


class ClientPutSessionRecentIntentSummaryViewTypeDef(
    _ClientPutSessionRecentIntentSummaryViewTypeDef
):
    """
    - *(dict) --*

      Provides information about the state of an intent. You can use this information to get the
      current state of an intent so that you can process the intent, or so that you can return the
      intent to its previous state.
      - **intentName** *(string) --*

        The name of the intent.
    """


_ClientPutSessionResponseTypeDef = TypedDict(
    "_ClientPutSessionResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "slots": Union[Dict[str, Any], List[Any], int, float, str, bool, None],
        "sessionAttributes": Union[Dict[str, Any], List[Any], int, float, str, bool, None],
        "message": str,
        "messageFormat": Literal["PlainText", "CustomPayload", "SSML", "Composite"],
        "dialogState": Literal[
            "ElicitIntent",
            "ConfirmIntent",
            "ElicitSlot",
            "Fulfilled",
            "ReadyForFulfillment",
            "Failed",
        ],
        "slotToElicit": str,
        "audioStream": StreamingBody,
        "sessionId": str,
    },
    total=False,
)


class ClientPutSessionResponseTypeDef(_ClientPutSessionResponseTypeDef):
    """
    - *(dict) --*

      - **contentType** *(string) --*

        Content type as specified in the ``Accept`` HTTP header in the request.
    """
