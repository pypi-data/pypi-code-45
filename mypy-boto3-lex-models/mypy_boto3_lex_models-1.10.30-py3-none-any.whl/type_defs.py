"Main interface for lex-models service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateBotVersionResponseabortStatementmessagesTypeDef",
    "ClientCreateBotVersionResponseabortStatementTypeDef",
    "ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef",
    "ClientCreateBotVersionResponseclarificationPromptTypeDef",
    "ClientCreateBotVersionResponseintentsTypeDef",
    "ClientCreateBotVersionResponseTypeDef",
    "ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef",
    "ClientCreateIntentVersionResponseconclusionStatementTypeDef",
    "ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef",
    "ClientCreateIntentVersionResponseconfirmationPromptTypeDef",
    "ClientCreateIntentVersionResponsedialogCodeHookTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptTypeDef",
    "ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef",
    "ClientCreateIntentVersionResponsefulfillmentActivityTypeDef",
    "ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef",
    "ClientCreateIntentVersionResponserejectionStatementTypeDef",
    "ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef",
    "ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef",
    "ClientCreateIntentVersionResponseslotsTypeDef",
    "ClientCreateIntentVersionResponseTypeDef",
    "ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef",
    "ClientCreateSlotTypeVersionResponseTypeDef",
    "ClientGetBotAliasResponseTypeDef",
    "ClientGetBotAliasesResponseBotAliasesTypeDef",
    "ClientGetBotAliasesResponseTypeDef",
    "ClientGetBotChannelAssociationResponseTypeDef",
    "ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef",
    "ClientGetBotChannelAssociationsResponseTypeDef",
    "ClientGetBotResponseabortStatementmessagesTypeDef",
    "ClientGetBotResponseabortStatementTypeDef",
    "ClientGetBotResponseclarificationPromptmessagesTypeDef",
    "ClientGetBotResponseclarificationPromptTypeDef",
    "ClientGetBotResponseintentsTypeDef",
    "ClientGetBotResponseTypeDef",
    "ClientGetBotVersionsResponsebotsTypeDef",
    "ClientGetBotVersionsResponseTypeDef",
    "ClientGetBotsResponsebotsTypeDef",
    "ClientGetBotsResponseTypeDef",
    "ClientGetBuiltinIntentResponseslotsTypeDef",
    "ClientGetBuiltinIntentResponseTypeDef",
    "ClientGetBuiltinIntentsResponseintentsTypeDef",
    "ClientGetBuiltinIntentsResponseTypeDef",
    "ClientGetBuiltinSlotTypesResponseslotTypesTypeDef",
    "ClientGetBuiltinSlotTypesResponseTypeDef",
    "ClientGetExportResponseTypeDef",
    "ClientGetImportResponseTypeDef",
    "ClientGetIntentResponseconclusionStatementmessagesTypeDef",
    "ClientGetIntentResponseconclusionStatementTypeDef",
    "ClientGetIntentResponseconfirmationPromptmessagesTypeDef",
    "ClientGetIntentResponseconfirmationPromptTypeDef",
    "ClientGetIntentResponsedialogCodeHookTypeDef",
    "ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef",
    "ClientGetIntentResponsefollowUpPromptpromptTypeDef",
    "ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    "ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef",
    "ClientGetIntentResponsefollowUpPromptTypeDef",
    "ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef",
    "ClientGetIntentResponsefulfillmentActivityTypeDef",
    "ClientGetIntentResponserejectionStatementmessagesTypeDef",
    "ClientGetIntentResponserejectionStatementTypeDef",
    "ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef",
    "ClientGetIntentResponseslotsvalueElicitationPromptTypeDef",
    "ClientGetIntentResponseslotsTypeDef",
    "ClientGetIntentResponseTypeDef",
    "ClientGetIntentVersionsResponseintentsTypeDef",
    "ClientGetIntentVersionsResponseTypeDef",
    "ClientGetIntentsResponseintentsTypeDef",
    "ClientGetIntentsResponseTypeDef",
    "ClientGetSlotTypeResponseenumerationValuesTypeDef",
    "ClientGetSlotTypeResponseTypeDef",
    "ClientGetSlotTypeVersionsResponseslotTypesTypeDef",
    "ClientGetSlotTypeVersionsResponseTypeDef",
    "ClientGetSlotTypesResponseslotTypesTypeDef",
    "ClientGetSlotTypesResponseTypeDef",
    "ClientGetUtterancesViewResponseutterancesutterancesTypeDef",
    "ClientGetUtterancesViewResponseutterancesTypeDef",
    "ClientGetUtterancesViewResponseTypeDef",
    "ClientPutBotAbortStatementmessagesTypeDef",
    "ClientPutBotAbortStatementTypeDef",
    "ClientPutBotAliasResponseTypeDef",
    "ClientPutBotClarificationPromptmessagesTypeDef",
    "ClientPutBotClarificationPromptTypeDef",
    "ClientPutBotIntentsTypeDef",
    "ClientPutBotResponseabortStatementmessagesTypeDef",
    "ClientPutBotResponseabortStatementTypeDef",
    "ClientPutBotResponseclarificationPromptmessagesTypeDef",
    "ClientPutBotResponseclarificationPromptTypeDef",
    "ClientPutBotResponseintentsTypeDef",
    "ClientPutBotResponseTypeDef",
    "ClientPutIntentConclusionStatementmessagesTypeDef",
    "ClientPutIntentConclusionStatementTypeDef",
    "ClientPutIntentConfirmationPromptmessagesTypeDef",
    "ClientPutIntentConfirmationPromptTypeDef",
    "ClientPutIntentDialogCodeHookTypeDef",
    "ClientPutIntentFollowUpPromptpromptmessagesTypeDef",
    "ClientPutIntentFollowUpPromptpromptTypeDef",
    "ClientPutIntentFollowUpPromptrejectionStatementmessagesTypeDef",
    "ClientPutIntentFollowUpPromptrejectionStatementTypeDef",
    "ClientPutIntentFollowUpPromptTypeDef",
    "ClientPutIntentFulfillmentActivitycodeHookTypeDef",
    "ClientPutIntentFulfillmentActivityTypeDef",
    "ClientPutIntentRejectionStatementmessagesTypeDef",
    "ClientPutIntentRejectionStatementTypeDef",
    "ClientPutIntentResponseconclusionStatementmessagesTypeDef",
    "ClientPutIntentResponseconclusionStatementTypeDef",
    "ClientPutIntentResponseconfirmationPromptmessagesTypeDef",
    "ClientPutIntentResponseconfirmationPromptTypeDef",
    "ClientPutIntentResponsedialogCodeHookTypeDef",
    "ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef",
    "ClientPutIntentResponsefollowUpPromptpromptTypeDef",
    "ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    "ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef",
    "ClientPutIntentResponsefollowUpPromptTypeDef",
    "ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef",
    "ClientPutIntentResponsefulfillmentActivityTypeDef",
    "ClientPutIntentResponserejectionStatementmessagesTypeDef",
    "ClientPutIntentResponserejectionStatementTypeDef",
    "ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef",
    "ClientPutIntentResponseslotsvalueElicitationPromptTypeDef",
    "ClientPutIntentResponseslotsTypeDef",
    "ClientPutIntentResponseTypeDef",
    "ClientPutIntentSlotsvalueElicitationPromptmessagesTypeDef",
    "ClientPutIntentSlotsvalueElicitationPromptTypeDef",
    "ClientPutIntentSlotsTypeDef",
    "ClientPutSlotTypeEnumerationValuesTypeDef",
    "ClientPutSlotTypeResponseenumerationValuesTypeDef",
    "ClientPutSlotTypeResponseTypeDef",
    "ClientStartImportResponseTypeDef",
    "GetBotAliasesPaginatePaginationConfigTypeDef",
    "GetBotAliasesPaginateResponseBotAliasesTypeDef",
    "GetBotAliasesPaginateResponseTypeDef",
    "GetBotChannelAssociationsPaginatePaginationConfigTypeDef",
    "GetBotChannelAssociationsPaginateResponsebotChannelAssociationsTypeDef",
    "GetBotChannelAssociationsPaginateResponseTypeDef",
    "GetBotVersionsPaginatePaginationConfigTypeDef",
    "GetBotVersionsPaginateResponsebotsTypeDef",
    "GetBotVersionsPaginateResponseTypeDef",
    "GetBotsPaginatePaginationConfigTypeDef",
    "GetBotsPaginateResponsebotsTypeDef",
    "GetBotsPaginateResponseTypeDef",
    "GetBuiltinIntentsPaginatePaginationConfigTypeDef",
    "GetBuiltinIntentsPaginateResponseintentsTypeDef",
    "GetBuiltinIntentsPaginateResponseTypeDef",
    "GetBuiltinSlotTypesPaginatePaginationConfigTypeDef",
    "GetBuiltinSlotTypesPaginateResponseslotTypesTypeDef",
    "GetBuiltinSlotTypesPaginateResponseTypeDef",
    "GetIntentVersionsPaginatePaginationConfigTypeDef",
    "GetIntentVersionsPaginateResponseintentsTypeDef",
    "GetIntentVersionsPaginateResponseTypeDef",
    "GetIntentsPaginatePaginationConfigTypeDef",
    "GetIntentsPaginateResponseintentsTypeDef",
    "GetIntentsPaginateResponseTypeDef",
    "GetSlotTypeVersionsPaginatePaginationConfigTypeDef",
    "GetSlotTypeVersionsPaginateResponseslotTypesTypeDef",
    "GetSlotTypeVersionsPaginateResponseTypeDef",
    "GetSlotTypesPaginatePaginationConfigTypeDef",
    "GetSlotTypesPaginateResponseslotTypesTypeDef",
    "GetSlotTypesPaginateResponseTypeDef",
)


_ClientCreateBotVersionResponseabortStatementmessagesTypeDef = TypedDict(
    "_ClientCreateBotVersionResponseabortStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientCreateBotVersionResponseabortStatementmessagesTypeDef(
    _ClientCreateBotVersionResponseabortStatementmessagesTypeDef
):
    pass


_ClientCreateBotVersionResponseabortStatementTypeDef = TypedDict(
    "_ClientCreateBotVersionResponseabortStatementTypeDef",
    {
        "messages": List[ClientCreateBotVersionResponseabortStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientCreateBotVersionResponseabortStatementTypeDef(
    _ClientCreateBotVersionResponseabortStatementTypeDef
):
    pass


_ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef = TypedDict(
    "_ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef(
    _ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef
):
    pass


_ClientCreateBotVersionResponseclarificationPromptTypeDef = TypedDict(
    "_ClientCreateBotVersionResponseclarificationPromptTypeDef",
    {
        "messages": List[ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientCreateBotVersionResponseclarificationPromptTypeDef(
    _ClientCreateBotVersionResponseclarificationPromptTypeDef
):
    pass


_ClientCreateBotVersionResponseintentsTypeDef = TypedDict(
    "_ClientCreateBotVersionResponseintentsTypeDef",
    {"intentName": str, "intentVersion": str},
    total=False,
)


class ClientCreateBotVersionResponseintentsTypeDef(_ClientCreateBotVersionResponseintentsTypeDef):
    pass


_ClientCreateBotVersionResponseTypeDef = TypedDict(
    "_ClientCreateBotVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[ClientCreateBotVersionResponseintentsTypeDef],
        "clarificationPrompt": ClientCreateBotVersionResponseclarificationPromptTypeDef,
        "abortStatement": ClientCreateBotVersionResponseabortStatementTypeDef,
        "status": Literal["BUILDING", "READY", "READY_BASIC_TESTING", "FAILED", "NOT_BUILT"],
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": Literal["en-US", "en-GB", "de-DE"],
        "childDirected": bool,
        "detectSentiment": bool,
    },
    total=False,
)


class ClientCreateBotVersionResponseTypeDef(_ClientCreateBotVersionResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the bot.
    """


_ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef(
    _ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef
):
    pass


_ClientCreateIntentVersionResponseconclusionStatementTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseconclusionStatementTypeDef",
    {
        "messages": List[ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponseconclusionStatementTypeDef(
    _ClientCreateIntentVersionResponseconclusionStatementTypeDef
):
    pass


_ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef(
    _ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef
):
    pass


_ClientCreateIntentVersionResponseconfirmationPromptTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseconfirmationPromptTypeDef",
    {
        "messages": List[ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponseconfirmationPromptTypeDef(
    _ClientCreateIntentVersionResponseconfirmationPromptTypeDef
):
    pass


_ClientCreateIntentVersionResponsedialogCodeHookTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsedialogCodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)


class ClientCreateIntentVersionResponsedialogCodeHookTypeDef(
    _ClientCreateIntentVersionResponsedialogCodeHookTypeDef
):
    pass


_ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef(
    _ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef
):
    pass


_ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef",
    {
        "messages": List[ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef(
    _ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef
):
    pass


_ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef(
    _ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef
):
    pass


_ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef",
    {
        "messages": List[
            ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef
        ],
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef(
    _ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef
):
    pass


_ClientCreateIntentVersionResponsefollowUpPromptTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefollowUpPromptTypeDef",
    {
        "prompt": ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef,
        "rejectionStatement": ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef,
    },
    total=False,
)


class ClientCreateIntentVersionResponsefollowUpPromptTypeDef(
    _ClientCreateIntentVersionResponsefollowUpPromptTypeDef
):
    pass


_ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)


class ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef(
    _ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef
):
    pass


_ClientCreateIntentVersionResponsefulfillmentActivityTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefulfillmentActivityTypeDef",
    {
        "type": Literal["ReturnIntent", "CodeHook"],
        "codeHook": ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef,
    },
    total=False,
)


class ClientCreateIntentVersionResponsefulfillmentActivityTypeDef(
    _ClientCreateIntentVersionResponsefulfillmentActivityTypeDef
):
    pass


_ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef(
    _ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef
):
    pass


_ClientCreateIntentVersionResponserejectionStatementTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponserejectionStatementTypeDef",
    {
        "messages": List[ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponserejectionStatementTypeDef(
    _ClientCreateIntentVersionResponserejectionStatementTypeDef
):
    pass


_ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef(
    _ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef
):
    pass


_ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef",
    {
        "messages": List[
            ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef
        ],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef(
    _ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef
):
    pass


_ClientCreateIntentVersionResponseslotsTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseslotsTypeDef",
    {
        "name": str,
        "description": str,
        "slotConstraint": Literal["Required", "Optional"],
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef,
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponseslotsTypeDef(_ClientCreateIntentVersionResponseslotsTypeDef):
    pass


_ClientCreateIntentVersionResponseTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[ClientCreateIntentVersionResponseslotsTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": ClientCreateIntentVersionResponseconfirmationPromptTypeDef,
        "rejectionStatement": ClientCreateIntentVersionResponserejectionStatementTypeDef,
        "followUpPrompt": ClientCreateIntentVersionResponsefollowUpPromptTypeDef,
        "conclusionStatement": ClientCreateIntentVersionResponseconclusionStatementTypeDef,
        "dialogCodeHook": ClientCreateIntentVersionResponsedialogCodeHookTypeDef,
        "fulfillmentActivity": ClientCreateIntentVersionResponsefulfillmentActivityTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponseTypeDef(_ClientCreateIntentVersionResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the intent.
    """


_ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef = TypedDict(
    "_ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef",
    {"value": str, "synonyms": List[str]},
    total=False,
)


class ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef(
    _ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef
):
    pass


_ClientCreateSlotTypeVersionResponseTypeDef = TypedDict(
    "_ClientCreateSlotTypeVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"],
    },
    total=False,
)


class ClientCreateSlotTypeVersionResponseTypeDef(_ClientCreateSlotTypeVersionResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the slot type.
    """


_ClientGetBotAliasResponseTypeDef = TypedDict(
    "_ClientGetBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
    },
    total=False,
)


class ClientGetBotAliasResponseTypeDef(_ClientGetBotAliasResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the bot alias.
    """


_ClientGetBotAliasesResponseBotAliasesTypeDef = TypedDict(
    "_ClientGetBotAliasesResponseBotAliasesTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
    },
    total=False,
)


class ClientGetBotAliasesResponseBotAliasesTypeDef(_ClientGetBotAliasesResponseBotAliasesTypeDef):
    """
    - *(dict) --*

      Provides information about a bot alias.
      - **name** *(string) --*

        The name of the bot alias.
    """


_ClientGetBotAliasesResponseTypeDef = TypedDict(
    "_ClientGetBotAliasesResponseTypeDef",
    {"BotAliases": List[ClientGetBotAliasesResponseBotAliasesTypeDef], "nextToken": str},
    total=False,
)


class ClientGetBotAliasesResponseTypeDef(_ClientGetBotAliasesResponseTypeDef):
    """
    - *(dict) --*

      - **BotAliases** *(list) --*

        An array of ``BotAliasMetadata`` objects, each describing a bot alias.
        - *(dict) --*

          Provides information about a bot alias.
          - **name** *(string) --*

            The name of the bot alias.
    """


_ClientGetBotChannelAssociationResponseTypeDef = TypedDict(
    "_ClientGetBotChannelAssociationResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": Literal["Facebook", "Slack", "Twilio-Sms", "Kik"],
        "botConfiguration": Dict[str, str],
        "status": Literal["IN_PROGRESS", "CREATED", "FAILED"],
        "failureReason": str,
    },
    total=False,
)


class ClientGetBotChannelAssociationResponseTypeDef(_ClientGetBotChannelAssociationResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the association between the bot and the channel.
    """


_ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef = TypedDict(
    "_ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": Literal["Facebook", "Slack", "Twilio-Sms", "Kik"],
        "botConfiguration": Dict[str, str],
        "status": Literal["IN_PROGRESS", "CREATED", "FAILED"],
        "failureReason": str,
    },
    total=False,
)


class ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef(
    _ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef
):
    """
    - *(dict) --*

      Represents an association between an Amazon Lex bot and an external messaging platform.
      - **name** *(string) --*

        The name of the association between the bot and the channel.
    """


_ClientGetBotChannelAssociationsResponseTypeDef = TypedDict(
    "_ClientGetBotChannelAssociationsResponseTypeDef",
    {
        "botChannelAssociations": List[
            ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetBotChannelAssociationsResponseTypeDef(
    _ClientGetBotChannelAssociationsResponseTypeDef
):
    """
    - *(dict) --*

      - **botChannelAssociations** *(list) --*

        An array of objects, one for each association, that provides information about the Amazon
        Lex bot and its association with the channel.
        - *(dict) --*

          Represents an association between an Amazon Lex bot and an external messaging platform.
          - **name** *(string) --*

            The name of the association between the bot and the channel.
    """


_ClientGetBotResponseabortStatementmessagesTypeDef = TypedDict(
    "_ClientGetBotResponseabortStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientGetBotResponseabortStatementmessagesTypeDef(
    _ClientGetBotResponseabortStatementmessagesTypeDef
):
    pass


_ClientGetBotResponseabortStatementTypeDef = TypedDict(
    "_ClientGetBotResponseabortStatementTypeDef",
    {"messages": List[ClientGetBotResponseabortStatementmessagesTypeDef], "responseCard": str},
    total=False,
)


class ClientGetBotResponseabortStatementTypeDef(_ClientGetBotResponseabortStatementTypeDef):
    pass


_ClientGetBotResponseclarificationPromptmessagesTypeDef = TypedDict(
    "_ClientGetBotResponseclarificationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientGetBotResponseclarificationPromptmessagesTypeDef(
    _ClientGetBotResponseclarificationPromptmessagesTypeDef
):
    pass


_ClientGetBotResponseclarificationPromptTypeDef = TypedDict(
    "_ClientGetBotResponseclarificationPromptTypeDef",
    {
        "messages": List[ClientGetBotResponseclarificationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientGetBotResponseclarificationPromptTypeDef(
    _ClientGetBotResponseclarificationPromptTypeDef
):
    pass


_ClientGetBotResponseintentsTypeDef = TypedDict(
    "_ClientGetBotResponseintentsTypeDef", {"intentName": str, "intentVersion": str}, total=False
)


class ClientGetBotResponseintentsTypeDef(_ClientGetBotResponseintentsTypeDef):
    pass


_ClientGetBotResponseTypeDef = TypedDict(
    "_ClientGetBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[ClientGetBotResponseintentsTypeDef],
        "clarificationPrompt": ClientGetBotResponseclarificationPromptTypeDef,
        "abortStatement": ClientGetBotResponseabortStatementTypeDef,
        "status": Literal["BUILDING", "READY", "READY_BASIC_TESTING", "FAILED", "NOT_BUILT"],
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": Literal["en-US", "en-GB", "de-DE"],
        "childDirected": bool,
        "detectSentiment": bool,
    },
    total=False,
)


class ClientGetBotResponseTypeDef(_ClientGetBotResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the bot.
    """


_ClientGetBotVersionsResponsebotsTypeDef = TypedDict(
    "_ClientGetBotVersionsResponsebotsTypeDef",
    {
        "name": str,
        "description": str,
        "status": Literal["BUILDING", "READY", "READY_BASIC_TESTING", "FAILED", "NOT_BUILT"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class ClientGetBotVersionsResponsebotsTypeDef(_ClientGetBotVersionsResponsebotsTypeDef):
    """
    - *(dict) --*

      Provides information about a bot. .
      - **name** *(string) --*

        The name of the bot.
    """


_ClientGetBotVersionsResponseTypeDef = TypedDict(
    "_ClientGetBotVersionsResponseTypeDef",
    {"bots": List[ClientGetBotVersionsResponsebotsTypeDef], "nextToken": str},
    total=False,
)


class ClientGetBotVersionsResponseTypeDef(_ClientGetBotVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **bots** *(list) --*

        An array of ``BotMetadata`` objects, one for each numbered version of the bot plus one for
        the ``$LATEST`` version.
        - *(dict) --*

          Provides information about a bot. .
          - **name** *(string) --*

            The name of the bot.
    """


_ClientGetBotsResponsebotsTypeDef = TypedDict(
    "_ClientGetBotsResponsebotsTypeDef",
    {
        "name": str,
        "description": str,
        "status": Literal["BUILDING", "READY", "READY_BASIC_TESTING", "FAILED", "NOT_BUILT"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class ClientGetBotsResponsebotsTypeDef(_ClientGetBotsResponsebotsTypeDef):
    """
    - *(dict) --*

      Provides information about a bot. .
      - **name** *(string) --*

        The name of the bot.
    """


_ClientGetBotsResponseTypeDef = TypedDict(
    "_ClientGetBotsResponseTypeDef",
    {"bots": List[ClientGetBotsResponsebotsTypeDef], "nextToken": str},
    total=False,
)


class ClientGetBotsResponseTypeDef(_ClientGetBotsResponseTypeDef):
    """
    - *(dict) --*

      - **bots** *(list) --*

        An array of ``botMetadata`` objects, with one entry for each bot.
        - *(dict) --*

          Provides information about a bot. .
          - **name** *(string) --*

            The name of the bot.
    """


_ClientGetBuiltinIntentResponseslotsTypeDef = TypedDict(
    "_ClientGetBuiltinIntentResponseslotsTypeDef", {"name": str}, total=False
)


class ClientGetBuiltinIntentResponseslotsTypeDef(_ClientGetBuiltinIntentResponseslotsTypeDef):
    pass


_ClientGetBuiltinIntentResponseTypeDef = TypedDict(
    "_ClientGetBuiltinIntentResponseTypeDef",
    {
        "signature": str,
        "supportedLocales": List[Literal["en-US", "en-GB", "de-DE"]],
        "slots": List[ClientGetBuiltinIntentResponseslotsTypeDef],
    },
    total=False,
)


class ClientGetBuiltinIntentResponseTypeDef(_ClientGetBuiltinIntentResponseTypeDef):
    """
    - *(dict) --*

      - **signature** *(string) --*

        The unique identifier for a built-in intent.
    """


_ClientGetBuiltinIntentsResponseintentsTypeDef = TypedDict(
    "_ClientGetBuiltinIntentsResponseintentsTypeDef",
    {"signature": str, "supportedLocales": List[Literal["en-US", "en-GB", "de-DE"]]},
    total=False,
)


class ClientGetBuiltinIntentsResponseintentsTypeDef(_ClientGetBuiltinIntentsResponseintentsTypeDef):
    """
    - *(dict) --*

      Provides metadata for a built-in intent.
      - **signature** *(string) --*

        A unique identifier for the built-in intent. To find the signature for an intent, see
        `Standard Built-in Intents
        <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__
        in the *Alexa Skills Kit* .
    """


_ClientGetBuiltinIntentsResponseTypeDef = TypedDict(
    "_ClientGetBuiltinIntentsResponseTypeDef",
    {"intents": List[ClientGetBuiltinIntentsResponseintentsTypeDef], "nextToken": str},
    total=False,
)


class ClientGetBuiltinIntentsResponseTypeDef(_ClientGetBuiltinIntentsResponseTypeDef):
    """
    - *(dict) --*

      - **intents** *(list) --*

        An array of ``builtinIntentMetadata`` objects, one for each intent in the response.
        - *(dict) --*

          Provides metadata for a built-in intent.
          - **signature** *(string) --*

            A unique identifier for the built-in intent. To find the signature for an intent, see
            `Standard Built-in Intents
            <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__
            in the *Alexa Skills Kit* .
    """


_ClientGetBuiltinSlotTypesResponseslotTypesTypeDef = TypedDict(
    "_ClientGetBuiltinSlotTypesResponseslotTypesTypeDef",
    {"signature": str, "supportedLocales": List[Literal["en-US", "en-GB", "de-DE"]]},
    total=False,
)


class ClientGetBuiltinSlotTypesResponseslotTypesTypeDef(
    _ClientGetBuiltinSlotTypesResponseslotTypesTypeDef
):
    """
    - *(dict) --*

      Provides information about a built in slot type.
      - **signature** *(string) --*

        A unique identifier for the built-in slot type. To find the signature for a slot type, see
        `Slot Type Reference
        <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference>`__
        in the *Alexa Skills Kit* .
    """


_ClientGetBuiltinSlotTypesResponseTypeDef = TypedDict(
    "_ClientGetBuiltinSlotTypesResponseTypeDef",
    {"slotTypes": List[ClientGetBuiltinSlotTypesResponseslotTypesTypeDef], "nextToken": str},
    total=False,
)


class ClientGetBuiltinSlotTypesResponseTypeDef(_ClientGetBuiltinSlotTypesResponseTypeDef):
    """
    - *(dict) --*

      - **slotTypes** *(list) --*

        An array of ``BuiltInSlotTypeMetadata`` objects, one entry for each slot type returned.
        - *(dict) --*

          Provides information about a built in slot type.
          - **signature** *(string) --*

            A unique identifier for the built-in slot type. To find the signature for a slot type,
            see `Slot Type Reference
            <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference>`__
            in the *Alexa Skills Kit* .
    """


_ClientGetExportResponseTypeDef = TypedDict(
    "_ClientGetExportResponseTypeDef",
    {
        "name": str,
        "version": str,
        "resourceType": Literal["BOT", "INTENT", "SLOT_TYPE"],
        "exportType": Literal["ALEXA_SKILLS_KIT", "LEX"],
        "exportStatus": Literal["IN_PROGRESS", "READY", "FAILED"],
        "failureReason": str,
        "url": str,
    },
    total=False,
)


class ClientGetExportResponseTypeDef(_ClientGetExportResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the bot being exported.
    """


_ClientGetImportResponseTypeDef = TypedDict(
    "_ClientGetImportResponseTypeDef",
    {
        "name": str,
        "resourceType": Literal["BOT", "INTENT", "SLOT_TYPE"],
        "mergeStrategy": Literal["OVERWRITE_LATEST", "FAIL_ON_CONFLICT"],
        "importId": str,
        "importStatus": Literal["IN_PROGRESS", "COMPLETE", "FAILED"],
        "failureReason": List[str],
        "createdDate": datetime,
    },
    total=False,
)


class ClientGetImportResponseTypeDef(_ClientGetImportResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name given to the import job.
    """


_ClientGetIntentResponseconclusionStatementmessagesTypeDef = TypedDict(
    "_ClientGetIntentResponseconclusionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientGetIntentResponseconclusionStatementmessagesTypeDef(
    _ClientGetIntentResponseconclusionStatementmessagesTypeDef
):
    pass


_ClientGetIntentResponseconclusionStatementTypeDef = TypedDict(
    "_ClientGetIntentResponseconclusionStatementTypeDef",
    {
        "messages": List[ClientGetIntentResponseconclusionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponseconclusionStatementTypeDef(
    _ClientGetIntentResponseconclusionStatementTypeDef
):
    pass


_ClientGetIntentResponseconfirmationPromptmessagesTypeDef = TypedDict(
    "_ClientGetIntentResponseconfirmationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientGetIntentResponseconfirmationPromptmessagesTypeDef(
    _ClientGetIntentResponseconfirmationPromptmessagesTypeDef
):
    pass


_ClientGetIntentResponseconfirmationPromptTypeDef = TypedDict(
    "_ClientGetIntentResponseconfirmationPromptTypeDef",
    {
        "messages": List[ClientGetIntentResponseconfirmationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponseconfirmationPromptTypeDef(
    _ClientGetIntentResponseconfirmationPromptTypeDef
):
    pass


_ClientGetIntentResponsedialogCodeHookTypeDef = TypedDict(
    "_ClientGetIntentResponsedialogCodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)


class ClientGetIntentResponsedialogCodeHookTypeDef(_ClientGetIntentResponsedialogCodeHookTypeDef):
    pass


_ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef = TypedDict(
    "_ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef(
    _ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef
):
    pass


_ClientGetIntentResponsefollowUpPromptpromptTypeDef = TypedDict(
    "_ClientGetIntentResponsefollowUpPromptpromptTypeDef",
    {
        "messages": List[ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponsefollowUpPromptpromptTypeDef(
    _ClientGetIntentResponsefollowUpPromptpromptTypeDef
):
    pass


_ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef = TypedDict(
    "_ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef(
    _ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef
):
    pass


_ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef = TypedDict(
    "_ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef",
    {
        "messages": List[ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef(
    _ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef
):
    pass


_ClientGetIntentResponsefollowUpPromptTypeDef = TypedDict(
    "_ClientGetIntentResponsefollowUpPromptTypeDef",
    {
        "prompt": ClientGetIntentResponsefollowUpPromptpromptTypeDef,
        "rejectionStatement": ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef,
    },
    total=False,
)


class ClientGetIntentResponsefollowUpPromptTypeDef(_ClientGetIntentResponsefollowUpPromptTypeDef):
    pass


_ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef = TypedDict(
    "_ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)


class ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef(
    _ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef
):
    pass


_ClientGetIntentResponsefulfillmentActivityTypeDef = TypedDict(
    "_ClientGetIntentResponsefulfillmentActivityTypeDef",
    {
        "type": Literal["ReturnIntent", "CodeHook"],
        "codeHook": ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef,
    },
    total=False,
)


class ClientGetIntentResponsefulfillmentActivityTypeDef(
    _ClientGetIntentResponsefulfillmentActivityTypeDef
):
    pass


_ClientGetIntentResponserejectionStatementmessagesTypeDef = TypedDict(
    "_ClientGetIntentResponserejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientGetIntentResponserejectionStatementmessagesTypeDef(
    _ClientGetIntentResponserejectionStatementmessagesTypeDef
):
    pass


_ClientGetIntentResponserejectionStatementTypeDef = TypedDict(
    "_ClientGetIntentResponserejectionStatementTypeDef",
    {
        "messages": List[ClientGetIntentResponserejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponserejectionStatementTypeDef(
    _ClientGetIntentResponserejectionStatementTypeDef
):
    pass


_ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef = TypedDict(
    "_ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef(
    _ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef
):
    pass


_ClientGetIntentResponseslotsvalueElicitationPromptTypeDef = TypedDict(
    "_ClientGetIntentResponseslotsvalueElicitationPromptTypeDef",
    {
        "messages": List[ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponseslotsvalueElicitationPromptTypeDef(
    _ClientGetIntentResponseslotsvalueElicitationPromptTypeDef
):
    pass


_ClientGetIntentResponseslotsTypeDef = TypedDict(
    "_ClientGetIntentResponseslotsTypeDef",
    {
        "name": str,
        "description": str,
        "slotConstraint": Literal["Required", "Optional"],
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": ClientGetIntentResponseslotsvalueElicitationPromptTypeDef,
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponseslotsTypeDef(_ClientGetIntentResponseslotsTypeDef):
    pass


_ClientGetIntentResponseTypeDef = TypedDict(
    "_ClientGetIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[ClientGetIntentResponseslotsTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": ClientGetIntentResponseconfirmationPromptTypeDef,
        "rejectionStatement": ClientGetIntentResponserejectionStatementTypeDef,
        "followUpPrompt": ClientGetIntentResponsefollowUpPromptTypeDef,
        "conclusionStatement": ClientGetIntentResponseconclusionStatementTypeDef,
        "dialogCodeHook": ClientGetIntentResponsedialogCodeHookTypeDef,
        "fulfillmentActivity": ClientGetIntentResponsefulfillmentActivityTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
    },
    total=False,
)


class ClientGetIntentResponseTypeDef(_ClientGetIntentResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the intent.
    """


_ClientGetIntentVersionsResponseintentsTypeDef = TypedDict(
    "_ClientGetIntentVersionsResponseintentsTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class ClientGetIntentVersionsResponseintentsTypeDef(_ClientGetIntentVersionsResponseintentsTypeDef):
    """
    - *(dict) --*

      Provides information about an intent.
      - **name** *(string) --*

        The name of the intent.
    """


_ClientGetIntentVersionsResponseTypeDef = TypedDict(
    "_ClientGetIntentVersionsResponseTypeDef",
    {"intents": List[ClientGetIntentVersionsResponseintentsTypeDef], "nextToken": str},
    total=False,
)


class ClientGetIntentVersionsResponseTypeDef(_ClientGetIntentVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **intents** *(list) --*

        An array of ``IntentMetadata`` objects, one for each numbered version of the intent plus one
        for the ``$LATEST`` version.
        - *(dict) --*

          Provides information about an intent.
          - **name** *(string) --*

            The name of the intent.
    """


_ClientGetIntentsResponseintentsTypeDef = TypedDict(
    "_ClientGetIntentsResponseintentsTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class ClientGetIntentsResponseintentsTypeDef(_ClientGetIntentsResponseintentsTypeDef):
    """
    - *(dict) --*

      Provides information about an intent.
      - **name** *(string) --*

        The name of the intent.
    """


_ClientGetIntentsResponseTypeDef = TypedDict(
    "_ClientGetIntentsResponseTypeDef",
    {"intents": List[ClientGetIntentsResponseintentsTypeDef], "nextToken": str},
    total=False,
)


class ClientGetIntentsResponseTypeDef(_ClientGetIntentsResponseTypeDef):
    """
    - *(dict) --*

      - **intents** *(list) --*

        An array of ``Intent`` objects. For more information, see  PutBot .
        - *(dict) --*

          Provides information about an intent.
          - **name** *(string) --*

            The name of the intent.
    """


_ClientGetSlotTypeResponseenumerationValuesTypeDef = TypedDict(
    "_ClientGetSlotTypeResponseenumerationValuesTypeDef",
    {"value": str, "synonyms": List[str]},
    total=False,
)


class ClientGetSlotTypeResponseenumerationValuesTypeDef(
    _ClientGetSlotTypeResponseenumerationValuesTypeDef
):
    pass


_ClientGetSlotTypeResponseTypeDef = TypedDict(
    "_ClientGetSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[ClientGetSlotTypeResponseenumerationValuesTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"],
    },
    total=False,
)


class ClientGetSlotTypeResponseTypeDef(_ClientGetSlotTypeResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the slot type.
    """


_ClientGetSlotTypeVersionsResponseslotTypesTypeDef = TypedDict(
    "_ClientGetSlotTypeVersionsResponseslotTypesTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class ClientGetSlotTypeVersionsResponseslotTypesTypeDef(
    _ClientGetSlotTypeVersionsResponseslotTypesTypeDef
):
    """
    - *(dict) --*

      Provides information about a slot type..
      - **name** *(string) --*

        The name of the slot type.
    """


_ClientGetSlotTypeVersionsResponseTypeDef = TypedDict(
    "_ClientGetSlotTypeVersionsResponseTypeDef",
    {"slotTypes": List[ClientGetSlotTypeVersionsResponseslotTypesTypeDef], "nextToken": str},
    total=False,
)


class ClientGetSlotTypeVersionsResponseTypeDef(_ClientGetSlotTypeVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **slotTypes** *(list) --*

        An array of ``SlotTypeMetadata`` objects, one for each numbered version of the slot type
        plus one for the ``$LATEST`` version.
        - *(dict) --*

          Provides information about a slot type..
          - **name** *(string) --*

            The name of the slot type.
    """


_ClientGetSlotTypesResponseslotTypesTypeDef = TypedDict(
    "_ClientGetSlotTypesResponseslotTypesTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class ClientGetSlotTypesResponseslotTypesTypeDef(_ClientGetSlotTypesResponseslotTypesTypeDef):
    """
    - *(dict) --*

      Provides information about a slot type..
      - **name** *(string) --*

        The name of the slot type.
    """


_ClientGetSlotTypesResponseTypeDef = TypedDict(
    "_ClientGetSlotTypesResponseTypeDef",
    {"slotTypes": List[ClientGetSlotTypesResponseslotTypesTypeDef], "nextToken": str},
    total=False,
)


class ClientGetSlotTypesResponseTypeDef(_ClientGetSlotTypesResponseTypeDef):
    """
    - *(dict) --*

      - **slotTypes** *(list) --*

        An array of objects, one for each slot type, that provides information such as the name of
        the slot type, the version, and a description.
        - *(dict) --*

          Provides information about a slot type..
          - **name** *(string) --*

            The name of the slot type.
    """


_ClientGetUtterancesViewResponseutterancesutterancesTypeDef = TypedDict(
    "_ClientGetUtterancesViewResponseutterancesutterancesTypeDef",
    {
        "utteranceString": str,
        "count": int,
        "distinctUsers": int,
        "firstUtteredDate": datetime,
        "lastUtteredDate": datetime,
    },
    total=False,
)


class ClientGetUtterancesViewResponseutterancesutterancesTypeDef(
    _ClientGetUtterancesViewResponseutterancesutterancesTypeDef
):
    pass


_ClientGetUtterancesViewResponseutterancesTypeDef = TypedDict(
    "_ClientGetUtterancesViewResponseutterancesTypeDef",
    {
        "botVersion": str,
        "utterances": List[ClientGetUtterancesViewResponseutterancesutterancesTypeDef],
    },
    total=False,
)


class ClientGetUtterancesViewResponseutterancesTypeDef(
    _ClientGetUtterancesViewResponseutterancesTypeDef
):
    pass


_ClientGetUtterancesViewResponseTypeDef = TypedDict(
    "_ClientGetUtterancesViewResponseTypeDef",
    {"botName": str, "utterances": List[ClientGetUtterancesViewResponseutterancesTypeDef]},
    total=False,
)


class ClientGetUtterancesViewResponseTypeDef(_ClientGetUtterancesViewResponseTypeDef):
    """
    - *(dict) --*

      - **botName** *(string) --*

        The name of the bot for which utterance information was returned.
    """


_RequiredClientPutBotAbortStatementmessagesTypeDef = TypedDict(
    "_RequiredClientPutBotAbortStatementmessagesTypeDef",
    {"contentType": Literal["PlainText", "SSML", "CustomPayload"]},
)
_OptionalClientPutBotAbortStatementmessagesTypeDef = TypedDict(
    "_OptionalClientPutBotAbortStatementmessagesTypeDef",
    {"content": str, "groupNumber": int},
    total=False,
)


class ClientPutBotAbortStatementmessagesTypeDef(
    _RequiredClientPutBotAbortStatementmessagesTypeDef,
    _OptionalClientPutBotAbortStatementmessagesTypeDef,
):
    """
    - *(dict) --*

      The message object that provides the message text and its type.
      - **contentType** *(string) --***[REQUIRED]**

        The content type of the message string.
    """


_RequiredClientPutBotAbortStatementTypeDef = TypedDict(
    "_RequiredClientPutBotAbortStatementTypeDef",
    {"messages": List[ClientPutBotAbortStatementmessagesTypeDef]},
)
_OptionalClientPutBotAbortStatementTypeDef = TypedDict(
    "_OptionalClientPutBotAbortStatementTypeDef", {"responseCard": str}, total=False
)


class ClientPutBotAbortStatementTypeDef(
    _RequiredClientPutBotAbortStatementTypeDef, _OptionalClientPutBotAbortStatementTypeDef
):
    """
    When Amazon Lex can't understand the user's input in context, it tries to elicit the information
    a few times. After that, Amazon Lex sends the message defined in ``abortStatement`` to the user,
    and then aborts the conversation. To set the number of retries, use the
    ``valueElicitationPrompt`` field for the slot type.
    For example, in a pizza ordering bot, Amazon Lex might ask a user "What type of crust would you
    like?" If the user's response is not one of the expected responses (for example, "thin crust,
    "deep dish," etc.), Amazon Lex tries to elicit a correct response a few more times.
    For example, in a pizza ordering application, ``OrderPizza`` might be one of the intents. This
    intent might require the ``CrustType`` slot. You specify the ``valueElicitationPrompt`` field
    when you create the ``CrustType`` slot.
    If you have defined a fallback intent the abort statement will not be sent to the user, the
    fallback intent is used instead. For more information, see `AMAZON.FallbackIntent
    <https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-fallback.html>`__ .
    - **messages** *(list) --***[REQUIRED]**

      A collection of message objects.
      - *(dict) --*

        The message object that provides the message text and its type.
        - **contentType** *(string) --***[REQUIRED]**

          The content type of the message string.
    """


_ClientPutBotAliasResponseTypeDef = TypedDict(
    "_ClientPutBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
    },
    total=False,
)


class ClientPutBotAliasResponseTypeDef(_ClientPutBotAliasResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the alias.
    """


_RequiredClientPutBotClarificationPromptmessagesTypeDef = TypedDict(
    "_RequiredClientPutBotClarificationPromptmessagesTypeDef",
    {"contentType": Literal["PlainText", "SSML", "CustomPayload"]},
)
_OptionalClientPutBotClarificationPromptmessagesTypeDef = TypedDict(
    "_OptionalClientPutBotClarificationPromptmessagesTypeDef",
    {"content": str, "groupNumber": int},
    total=False,
)


class ClientPutBotClarificationPromptmessagesTypeDef(
    _RequiredClientPutBotClarificationPromptmessagesTypeDef,
    _OptionalClientPutBotClarificationPromptmessagesTypeDef,
):
    """
    - *(dict) --*

      The message object that provides the message text and its type.
      - **contentType** *(string) --***[REQUIRED]**

        The content type of the message string.
    """


_RequiredClientPutBotClarificationPromptTypeDef = TypedDict(
    "_RequiredClientPutBotClarificationPromptTypeDef",
    {"messages": List[ClientPutBotClarificationPromptmessagesTypeDef]},
)
_OptionalClientPutBotClarificationPromptTypeDef = TypedDict(
    "_OptionalClientPutBotClarificationPromptTypeDef",
    {"maxAttempts": int, "responseCard": str},
    total=False,
)


class ClientPutBotClarificationPromptTypeDef(
    _RequiredClientPutBotClarificationPromptTypeDef, _OptionalClientPutBotClarificationPromptTypeDef
):
    """
    When Amazon Lex doesn't understand the user's intent, it uses this message to get clarification.
    To specify how many times Amazon Lex should repeat the clarification prompt, use the
    ``maxAttempts`` field. If Amazon Lex still doesn't understand, it sends the message in the
    ``abortStatement`` field.
    When you create a clarification prompt, make sure that it suggests the correct response from the
    user. for example, for a bot that orders pizza and drinks, you might create this clarification
    prompt: "What would you like to do? You can say 'Order a pizza' or 'Order a drink.'"
    If you have defined a fallback intent, it will be invoked if the clarification prompt is
    repeated the number of times defined in the ``maxAttempts`` field. For more information, see
    `AMAZON.FallbackIntent
    <https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-fallback.html>`__ .
    If you don't define a clarification prompt, at runtime Amazon Lex will return a 400 Bad Request
    exception in three cases:
    * Follow-up prompt - When the user responds to a follow-up prompt but does not provide an
    intent. For example, in response to a follow-up prompt that says "Would you like anything else
    today?" the user says "Yes." Amazon Lex will return a 400 Bad Request exception because it does
    not have a clarification prompt to send to the user to get an intent.
    * Lambda function - When using a Lambda function, you return an ``ElicitIntent`` dialog type.
    Since Amazon Lex does not have a clarification prompt to get an intent from the user, it returns
    a 400 Bad Request exception.
    * PutSession operation - When using the ``PutSession`` operation, you send an ``ElicitIntent``
    dialog type. Since Amazon Lex does not have a clarification prompt to get an intent from the
    user, it returns a 400 Bad Request exception.
    - **messages** *(list) --***[REQUIRED]**

      An array of objects, each of which provides a message string and its type. You can specify the
      message string in plain text or in Speech Synthesis Markup Language (SSML).
      - *(dict) --*

        The message object that provides the message text and its type.
        - **contentType** *(string) --***[REQUIRED]**

          The content type of the message string.
    """


_RequiredClientPutBotIntentsTypeDef = TypedDict(
    "_RequiredClientPutBotIntentsTypeDef", {"intentName": str}
)
_OptionalClientPutBotIntentsTypeDef = TypedDict(
    "_OptionalClientPutBotIntentsTypeDef", {"intentVersion": str}, total=False
)


class ClientPutBotIntentsTypeDef(
    _RequiredClientPutBotIntentsTypeDef, _OptionalClientPutBotIntentsTypeDef
):
    """
    - *(dict) --*

      Identifies the specific version of an intent.
      - **intentName** *(string) --***[REQUIRED]**

        The name of the intent.
    """


_ClientPutBotResponseabortStatementmessagesTypeDef = TypedDict(
    "_ClientPutBotResponseabortStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientPutBotResponseabortStatementmessagesTypeDef(
    _ClientPutBotResponseabortStatementmessagesTypeDef
):
    pass


_ClientPutBotResponseabortStatementTypeDef = TypedDict(
    "_ClientPutBotResponseabortStatementTypeDef",
    {"messages": List[ClientPutBotResponseabortStatementmessagesTypeDef], "responseCard": str},
    total=False,
)


class ClientPutBotResponseabortStatementTypeDef(_ClientPutBotResponseabortStatementTypeDef):
    pass


_ClientPutBotResponseclarificationPromptmessagesTypeDef = TypedDict(
    "_ClientPutBotResponseclarificationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientPutBotResponseclarificationPromptmessagesTypeDef(
    _ClientPutBotResponseclarificationPromptmessagesTypeDef
):
    pass


_ClientPutBotResponseclarificationPromptTypeDef = TypedDict(
    "_ClientPutBotResponseclarificationPromptTypeDef",
    {
        "messages": List[ClientPutBotResponseclarificationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientPutBotResponseclarificationPromptTypeDef(
    _ClientPutBotResponseclarificationPromptTypeDef
):
    pass


_ClientPutBotResponseintentsTypeDef = TypedDict(
    "_ClientPutBotResponseintentsTypeDef", {"intentName": str, "intentVersion": str}, total=False
)


class ClientPutBotResponseintentsTypeDef(_ClientPutBotResponseintentsTypeDef):
    pass


_ClientPutBotResponseTypeDef = TypedDict(
    "_ClientPutBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[ClientPutBotResponseintentsTypeDef],
        "clarificationPrompt": ClientPutBotResponseclarificationPromptTypeDef,
        "abortStatement": ClientPutBotResponseabortStatementTypeDef,
        "status": Literal["BUILDING", "READY", "READY_BASIC_TESTING", "FAILED", "NOT_BUILT"],
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": Literal["en-US", "en-GB", "de-DE"],
        "childDirected": bool,
        "createVersion": bool,
        "detectSentiment": bool,
    },
    total=False,
)


class ClientPutBotResponseTypeDef(_ClientPutBotResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the bot.
    """


_ClientPutIntentConclusionStatementmessagesTypeDef = TypedDict(
    "_ClientPutIntentConclusionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientPutIntentConclusionStatementmessagesTypeDef(
    _ClientPutIntentConclusionStatementmessagesTypeDef
):
    pass


_ClientPutIntentConclusionStatementTypeDef = TypedDict(
    "_ClientPutIntentConclusionStatementTypeDef",
    {"messages": List[ClientPutIntentConclusionStatementmessagesTypeDef], "responseCard": str},
    total=False,
)


class ClientPutIntentConclusionStatementTypeDef(_ClientPutIntentConclusionStatementTypeDef):
    """
    The statement that you want Amazon Lex to convey to the user after the intent is successfully
    fulfilled by the Lambda function.
    This element is relevant only if you provide a Lambda function in the ``fulfillmentActivity`` .
    If you return the intent to the client application, you can't specify this element.
    .. note::

      The ``followUpPrompt`` and ``conclusionStatement`` are mutually exclusive. You can specify
      only one.
    """


_ClientPutIntentConfirmationPromptmessagesTypeDef = TypedDict(
    "_ClientPutIntentConfirmationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientPutIntentConfirmationPromptmessagesTypeDef(
    _ClientPutIntentConfirmationPromptmessagesTypeDef
):
    pass


_ClientPutIntentConfirmationPromptTypeDef = TypedDict(
    "_ClientPutIntentConfirmationPromptTypeDef",
    {
        "messages": List[ClientPutIntentConfirmationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentConfirmationPromptTypeDef(_ClientPutIntentConfirmationPromptTypeDef):
    """
    Prompts the user to confirm the intent. This question should have a yes or no answer.
    Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for
    fulfillment. For example, with the ``OrderPizza`` intent, you might want to confirm that the
    order is correct before placing it. For other intents, such as intents that simply respond to
    user questions, you might not need to ask the user for confirmation before providing the
    information.
    .. note::

      You you must provide both the ``rejectionStatement`` and the ``confirmationPrompt`` , or
      neither.
    """


_RequiredClientPutIntentDialogCodeHookTypeDef = TypedDict(
    "_RequiredClientPutIntentDialogCodeHookTypeDef", {"uri": str}
)
_OptionalClientPutIntentDialogCodeHookTypeDef = TypedDict(
    "_OptionalClientPutIntentDialogCodeHookTypeDef", {"messageVersion": str}, total=False
)


class ClientPutIntentDialogCodeHookTypeDef(
    _RequiredClientPutIntentDialogCodeHookTypeDef, _OptionalClientPutIntentDialogCodeHookTypeDef
):
    """
    Specifies a Lambda function to invoke for each user input. You can invoke this Lambda function
    to personalize user interaction.
    For example, suppose your bot determines that the user is John. Your Lambda function might
    retrieve John's information from a backend database and prepopulate some of the values. For
    example, if you find that John is gluten intolerant, you might set the corresponding intent
    slot, ``GlutenIntolerant`` , to true. You might find John's phone number and set the
    corresponding session attribute.
    - **uri** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) of the Lambda function.
    """


_RequiredClientPutIntentFollowUpPromptpromptmessagesTypeDef = TypedDict(
    "_RequiredClientPutIntentFollowUpPromptpromptmessagesTypeDef",
    {"contentType": Literal["PlainText", "SSML", "CustomPayload"]},
)
_OptionalClientPutIntentFollowUpPromptpromptmessagesTypeDef = TypedDict(
    "_OptionalClientPutIntentFollowUpPromptpromptmessagesTypeDef",
    {"content": str, "groupNumber": int},
    total=False,
)


class ClientPutIntentFollowUpPromptpromptmessagesTypeDef(
    _RequiredClientPutIntentFollowUpPromptpromptmessagesTypeDef,
    _OptionalClientPutIntentFollowUpPromptpromptmessagesTypeDef,
):
    """
    - *(dict) --*

      The message object that provides the message text and its type.
      - **contentType** *(string) --***[REQUIRED]**

        The content type of the message string.
    """


_RequiredClientPutIntentFollowUpPromptpromptTypeDef = TypedDict(
    "_RequiredClientPutIntentFollowUpPromptpromptTypeDef",
    {"messages": List[ClientPutIntentFollowUpPromptpromptmessagesTypeDef]},
)
_OptionalClientPutIntentFollowUpPromptpromptTypeDef = TypedDict(
    "_OptionalClientPutIntentFollowUpPromptpromptTypeDef",
    {"maxAttempts": int, "responseCard": str},
    total=False,
)


class ClientPutIntentFollowUpPromptpromptTypeDef(
    _RequiredClientPutIntentFollowUpPromptpromptTypeDef,
    _OptionalClientPutIntentFollowUpPromptpromptTypeDef,
):
    """
    - **prompt** *(dict) --***[REQUIRED]**

      Prompts for information from the user.
      - **messages** *(list) --***[REQUIRED]**

        An array of objects, each of which provides a message string and its type. You can specify
        the message string in plain text or in Speech Synthesis Markup Language (SSML).
        - *(dict) --*

          The message object that provides the message text and its type.
          - **contentType** *(string) --***[REQUIRED]**

            The content type of the message string.
    """


_ClientPutIntentFollowUpPromptrejectionStatementmessagesTypeDef = TypedDict(
    "_ClientPutIntentFollowUpPromptrejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientPutIntentFollowUpPromptrejectionStatementmessagesTypeDef(
    _ClientPutIntentFollowUpPromptrejectionStatementmessagesTypeDef
):
    pass


_ClientPutIntentFollowUpPromptrejectionStatementTypeDef = TypedDict(
    "_ClientPutIntentFollowUpPromptrejectionStatementTypeDef",
    {
        "messages": List[ClientPutIntentFollowUpPromptrejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentFollowUpPromptrejectionStatementTypeDef(
    _ClientPutIntentFollowUpPromptrejectionStatementTypeDef
):
    pass


_RequiredClientPutIntentFollowUpPromptTypeDef = TypedDict(
    "_RequiredClientPutIntentFollowUpPromptTypeDef",
    {"prompt": ClientPutIntentFollowUpPromptpromptTypeDef},
)
_OptionalClientPutIntentFollowUpPromptTypeDef = TypedDict(
    "_OptionalClientPutIntentFollowUpPromptTypeDef",
    {"rejectionStatement": ClientPutIntentFollowUpPromptrejectionStatementTypeDef},
    total=False,
)


class ClientPutIntentFollowUpPromptTypeDef(
    _RequiredClientPutIntentFollowUpPromptTypeDef, _OptionalClientPutIntentFollowUpPromptTypeDef
):
    """
    Amazon Lex uses this prompt to solicit additional activity after fulfilling an intent. For
    example, after the ``OrderPizza`` intent is fulfilled, you might prompt the user to order a
    drink.
    The action that Amazon Lex takes depends on the user's response, as follows:
    * If the user says "Yes" it responds with the clarification prompt that is configured for the
    bot.
    * if the user says "Yes" and continues with an utterance that triggers an intent it starts a
    conversation for the intent.
    * If the user says "No" it responds with the rejection statement configured for the the
    follow-up prompt.
    * If it doesn't recognize the utterance it repeats the follow-up prompt again.
    The ``followUpPrompt`` field and the ``conclusionStatement`` field are mutually exclusive. You
    can specify only one.
    - **prompt** *(dict) --***[REQUIRED]**

      Prompts for information from the user.
      - **messages** *(list) --***[REQUIRED]**

        An array of objects, each of which provides a message string and its type. You can specify
        the message string in plain text or in Speech Synthesis Markup Language (SSML).
        - *(dict) --*

          The message object that provides the message text and its type.
          - **contentType** *(string) --***[REQUIRED]**

            The content type of the message string.
    """


_ClientPutIntentFulfillmentActivitycodeHookTypeDef = TypedDict(
    "_ClientPutIntentFulfillmentActivitycodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)


class ClientPutIntentFulfillmentActivitycodeHookTypeDef(
    _ClientPutIntentFulfillmentActivitycodeHookTypeDef
):
    pass


_RequiredClientPutIntentFulfillmentActivityTypeDef = TypedDict(
    "_RequiredClientPutIntentFulfillmentActivityTypeDef",
    {"type": Literal["ReturnIntent", "CodeHook"]},
)
_OptionalClientPutIntentFulfillmentActivityTypeDef = TypedDict(
    "_OptionalClientPutIntentFulfillmentActivityTypeDef",
    {"codeHook": ClientPutIntentFulfillmentActivitycodeHookTypeDef},
    total=False,
)


class ClientPutIntentFulfillmentActivityTypeDef(
    _RequiredClientPutIntentFulfillmentActivityTypeDef,
    _OptionalClientPutIntentFulfillmentActivityTypeDef,
):
    """
    Required. Describes how the intent is fulfilled. For example, after a user provides all of the
    information for a pizza order, ``fulfillmentActivity`` defines how the bot places an order with
    a local pizza store.
    You might configure Amazon Lex to return all of the intent information to the client
    application, or direct it to invoke a Lambda function that can process the intent (for example,
    place an order with a pizzeria).
    - **type** *(string) --***[REQUIRED]**

      How the intent should be fulfilled, either by running a Lambda function or by returning the
      slot data to the client application.
    """


_ClientPutIntentRejectionStatementmessagesTypeDef = TypedDict(
    "_ClientPutIntentRejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientPutIntentRejectionStatementmessagesTypeDef(
    _ClientPutIntentRejectionStatementmessagesTypeDef
):
    pass


_ClientPutIntentRejectionStatementTypeDef = TypedDict(
    "_ClientPutIntentRejectionStatementTypeDef",
    {"messages": List[ClientPutIntentRejectionStatementmessagesTypeDef], "responseCard": str},
    total=False,
)


class ClientPutIntentRejectionStatementTypeDef(_ClientPutIntentRejectionStatementTypeDef):
    """
    When the user answers "no" to the question defined in ``confirmationPrompt`` , Amazon Lex
    responds with this statement to acknowledge that the intent was canceled.
    .. note::

      You must provide both the ``rejectionStatement`` and the ``confirmationPrompt`` , or neither.
    """


_ClientPutIntentResponseconclusionStatementmessagesTypeDef = TypedDict(
    "_ClientPutIntentResponseconclusionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientPutIntentResponseconclusionStatementmessagesTypeDef(
    _ClientPutIntentResponseconclusionStatementmessagesTypeDef
):
    pass


_ClientPutIntentResponseconclusionStatementTypeDef = TypedDict(
    "_ClientPutIntentResponseconclusionStatementTypeDef",
    {
        "messages": List[ClientPutIntentResponseconclusionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponseconclusionStatementTypeDef(
    _ClientPutIntentResponseconclusionStatementTypeDef
):
    pass


_ClientPutIntentResponseconfirmationPromptmessagesTypeDef = TypedDict(
    "_ClientPutIntentResponseconfirmationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientPutIntentResponseconfirmationPromptmessagesTypeDef(
    _ClientPutIntentResponseconfirmationPromptmessagesTypeDef
):
    pass


_ClientPutIntentResponseconfirmationPromptTypeDef = TypedDict(
    "_ClientPutIntentResponseconfirmationPromptTypeDef",
    {
        "messages": List[ClientPutIntentResponseconfirmationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponseconfirmationPromptTypeDef(
    _ClientPutIntentResponseconfirmationPromptTypeDef
):
    pass


_ClientPutIntentResponsedialogCodeHookTypeDef = TypedDict(
    "_ClientPutIntentResponsedialogCodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)


class ClientPutIntentResponsedialogCodeHookTypeDef(_ClientPutIntentResponsedialogCodeHookTypeDef):
    pass


_ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef = TypedDict(
    "_ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef(
    _ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef
):
    pass


_ClientPutIntentResponsefollowUpPromptpromptTypeDef = TypedDict(
    "_ClientPutIntentResponsefollowUpPromptpromptTypeDef",
    {
        "messages": List[ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponsefollowUpPromptpromptTypeDef(
    _ClientPutIntentResponsefollowUpPromptpromptTypeDef
):
    pass


_ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef = TypedDict(
    "_ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef(
    _ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef
):
    pass


_ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef = TypedDict(
    "_ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef",
    {
        "messages": List[ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef(
    _ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef
):
    pass


_ClientPutIntentResponsefollowUpPromptTypeDef = TypedDict(
    "_ClientPutIntentResponsefollowUpPromptTypeDef",
    {
        "prompt": ClientPutIntentResponsefollowUpPromptpromptTypeDef,
        "rejectionStatement": ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef,
    },
    total=False,
)


class ClientPutIntentResponsefollowUpPromptTypeDef(_ClientPutIntentResponsefollowUpPromptTypeDef):
    pass


_ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef = TypedDict(
    "_ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)


class ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef(
    _ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef
):
    pass


_ClientPutIntentResponsefulfillmentActivityTypeDef = TypedDict(
    "_ClientPutIntentResponsefulfillmentActivityTypeDef",
    {
        "type": Literal["ReturnIntent", "CodeHook"],
        "codeHook": ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef,
    },
    total=False,
)


class ClientPutIntentResponsefulfillmentActivityTypeDef(
    _ClientPutIntentResponsefulfillmentActivityTypeDef
):
    pass


_ClientPutIntentResponserejectionStatementmessagesTypeDef = TypedDict(
    "_ClientPutIntentResponserejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientPutIntentResponserejectionStatementmessagesTypeDef(
    _ClientPutIntentResponserejectionStatementmessagesTypeDef
):
    pass


_ClientPutIntentResponserejectionStatementTypeDef = TypedDict(
    "_ClientPutIntentResponserejectionStatementTypeDef",
    {
        "messages": List[ClientPutIntentResponserejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponserejectionStatementTypeDef(
    _ClientPutIntentResponserejectionStatementTypeDef
):
    pass


_ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef = TypedDict(
    "_ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef(
    _ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef
):
    pass


_ClientPutIntentResponseslotsvalueElicitationPromptTypeDef = TypedDict(
    "_ClientPutIntentResponseslotsvalueElicitationPromptTypeDef",
    {
        "messages": List[ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponseslotsvalueElicitationPromptTypeDef(
    _ClientPutIntentResponseslotsvalueElicitationPromptTypeDef
):
    pass


_ClientPutIntentResponseslotsTypeDef = TypedDict(
    "_ClientPutIntentResponseslotsTypeDef",
    {
        "name": str,
        "description": str,
        "slotConstraint": Literal["Required", "Optional"],
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": ClientPutIntentResponseslotsvalueElicitationPromptTypeDef,
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponseslotsTypeDef(_ClientPutIntentResponseslotsTypeDef):
    pass


_ClientPutIntentResponseTypeDef = TypedDict(
    "_ClientPutIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[ClientPutIntentResponseslotsTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": ClientPutIntentResponseconfirmationPromptTypeDef,
        "rejectionStatement": ClientPutIntentResponserejectionStatementTypeDef,
        "followUpPrompt": ClientPutIntentResponsefollowUpPromptTypeDef,
        "conclusionStatement": ClientPutIntentResponseconclusionStatementTypeDef,
        "dialogCodeHook": ClientPutIntentResponsedialogCodeHookTypeDef,
        "fulfillmentActivity": ClientPutIntentResponsefulfillmentActivityTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "createVersion": bool,
    },
    total=False,
)


class ClientPutIntentResponseTypeDef(_ClientPutIntentResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the intent.
    """


_ClientPutIntentSlotsvalueElicitationPromptmessagesTypeDef = TypedDict(
    "_ClientPutIntentSlotsvalueElicitationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)


class ClientPutIntentSlotsvalueElicitationPromptmessagesTypeDef(
    _ClientPutIntentSlotsvalueElicitationPromptmessagesTypeDef
):
    pass


_ClientPutIntentSlotsvalueElicitationPromptTypeDef = TypedDict(
    "_ClientPutIntentSlotsvalueElicitationPromptTypeDef",
    {
        "messages": List[ClientPutIntentSlotsvalueElicitationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentSlotsvalueElicitationPromptTypeDef(
    _ClientPutIntentSlotsvalueElicitationPromptTypeDef
):
    pass


_RequiredClientPutIntentSlotsTypeDef = TypedDict(
    "_RequiredClientPutIntentSlotsTypeDef", {"name": str}
)
_OptionalClientPutIntentSlotsTypeDef = TypedDict(
    "_OptionalClientPutIntentSlotsTypeDef",
    {
        "description": str,
        "slotConstraint": Literal["Required", "Optional"],
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": ClientPutIntentSlotsvalueElicitationPromptTypeDef,
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentSlotsTypeDef(
    _RequiredClientPutIntentSlotsTypeDef, _OptionalClientPutIntentSlotsTypeDef
):
    """
    - *(dict) --*

      Identifies the version of a specific slot.
      - **name** *(string) --***[REQUIRED]**

        The name of the slot.
    """


_RequiredClientPutSlotTypeEnumerationValuesTypeDef = TypedDict(
    "_RequiredClientPutSlotTypeEnumerationValuesTypeDef", {"value": str}
)
_OptionalClientPutSlotTypeEnumerationValuesTypeDef = TypedDict(
    "_OptionalClientPutSlotTypeEnumerationValuesTypeDef", {"synonyms": List[str]}, total=False
)


class ClientPutSlotTypeEnumerationValuesTypeDef(
    _RequiredClientPutSlotTypeEnumerationValuesTypeDef,
    _OptionalClientPutSlotTypeEnumerationValuesTypeDef,
):
    """
    - *(dict) --*

      Each slot type can have a set of values. Each enumeration value represents a value the slot
      type can take.
      For example, a pizza ordering bot could have a slot type that specifies the type of crust that
      the pizza should have. The slot type could include the values
      * thick
      * thin
      * stuffed
      - **value** *(string) --***[REQUIRED]**

        The value of the slot type.
    """


_ClientPutSlotTypeResponseenumerationValuesTypeDef = TypedDict(
    "_ClientPutSlotTypeResponseenumerationValuesTypeDef",
    {"value": str, "synonyms": List[str]},
    total=False,
)


class ClientPutSlotTypeResponseenumerationValuesTypeDef(
    _ClientPutSlotTypeResponseenumerationValuesTypeDef
):
    pass


_ClientPutSlotTypeResponseTypeDef = TypedDict(
    "_ClientPutSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[ClientPutSlotTypeResponseenumerationValuesTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"],
        "createVersion": bool,
    },
    total=False,
)


class ClientPutSlotTypeResponseTypeDef(_ClientPutSlotTypeResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the slot type.
    """


_ClientStartImportResponseTypeDef = TypedDict(
    "_ClientStartImportResponseTypeDef",
    {
        "name": str,
        "resourceType": Literal["BOT", "INTENT", "SLOT_TYPE"],
        "mergeStrategy": Literal["OVERWRITE_LATEST", "FAIL_ON_CONFLICT"],
        "importId": str,
        "importStatus": Literal["IN_PROGRESS", "COMPLETE", "FAILED"],
        "createdDate": datetime,
    },
    total=False,
)


class ClientStartImportResponseTypeDef(_ClientStartImportResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name given to the import job.
    """


_GetBotAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBotAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBotAliasesPaginatePaginationConfigTypeDef(_GetBotAliasesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetBotAliasesPaginateResponseBotAliasesTypeDef = TypedDict(
    "_GetBotAliasesPaginateResponseBotAliasesTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
    },
    total=False,
)


class GetBotAliasesPaginateResponseBotAliasesTypeDef(
    _GetBotAliasesPaginateResponseBotAliasesTypeDef
):
    """
    - *(dict) --*

      Provides information about a bot alias.
      - **name** *(string) --*

        The name of the bot alias.
    """


_GetBotAliasesPaginateResponseTypeDef = TypedDict(
    "_GetBotAliasesPaginateResponseTypeDef",
    {"BotAliases": List[GetBotAliasesPaginateResponseBotAliasesTypeDef], "NextToken": str},
    total=False,
)


class GetBotAliasesPaginateResponseTypeDef(_GetBotAliasesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **BotAliases** *(list) --*

        An array of ``BotAliasMetadata`` objects, each describing a bot alias.
        - *(dict) --*

          Provides information about a bot alias.
          - **name** *(string) --*

            The name of the bot alias.
    """


_GetBotChannelAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBotChannelAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBotChannelAssociationsPaginatePaginationConfigTypeDef(
    _GetBotChannelAssociationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetBotChannelAssociationsPaginateResponsebotChannelAssociationsTypeDef = TypedDict(
    "_GetBotChannelAssociationsPaginateResponsebotChannelAssociationsTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": Literal["Facebook", "Slack", "Twilio-Sms", "Kik"],
        "botConfiguration": Dict[str, str],
        "status": Literal["IN_PROGRESS", "CREATED", "FAILED"],
        "failureReason": str,
    },
    total=False,
)


class GetBotChannelAssociationsPaginateResponsebotChannelAssociationsTypeDef(
    _GetBotChannelAssociationsPaginateResponsebotChannelAssociationsTypeDef
):
    """
    - *(dict) --*

      Represents an association between an Amazon Lex bot and an external messaging platform.
      - **name** *(string) --*

        The name of the association between the bot and the channel.
    """


_GetBotChannelAssociationsPaginateResponseTypeDef = TypedDict(
    "_GetBotChannelAssociationsPaginateResponseTypeDef",
    {
        "botChannelAssociations": List[
            GetBotChannelAssociationsPaginateResponsebotChannelAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetBotChannelAssociationsPaginateResponseTypeDef(
    _GetBotChannelAssociationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **botChannelAssociations** *(list) --*

        An array of objects, one for each association, that provides information about the Amazon
        Lex bot and its association with the channel.
        - *(dict) --*

          Represents an association between an Amazon Lex bot and an external messaging platform.
          - **name** *(string) --*

            The name of the association between the bot and the channel.
    """


_GetBotVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBotVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBotVersionsPaginatePaginationConfigTypeDef(_GetBotVersionsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetBotVersionsPaginateResponsebotsTypeDef = TypedDict(
    "_GetBotVersionsPaginateResponsebotsTypeDef",
    {
        "name": str,
        "description": str,
        "status": Literal["BUILDING", "READY", "READY_BASIC_TESTING", "FAILED", "NOT_BUILT"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class GetBotVersionsPaginateResponsebotsTypeDef(_GetBotVersionsPaginateResponsebotsTypeDef):
    """
    - *(dict) --*

      Provides information about a bot. .
      - **name** *(string) --*

        The name of the bot.
    """


_GetBotVersionsPaginateResponseTypeDef = TypedDict(
    "_GetBotVersionsPaginateResponseTypeDef",
    {"bots": List[GetBotVersionsPaginateResponsebotsTypeDef], "NextToken": str},
    total=False,
)


class GetBotVersionsPaginateResponseTypeDef(_GetBotVersionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **bots** *(list) --*

        An array of ``BotMetadata`` objects, one for each numbered version of the bot plus one for
        the ``$LATEST`` version.
        - *(dict) --*

          Provides information about a bot. .
          - **name** *(string) --*

            The name of the bot.
    """


_GetBotsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBotsPaginatePaginationConfigTypeDef(_GetBotsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetBotsPaginateResponsebotsTypeDef = TypedDict(
    "_GetBotsPaginateResponsebotsTypeDef",
    {
        "name": str,
        "description": str,
        "status": Literal["BUILDING", "READY", "READY_BASIC_TESTING", "FAILED", "NOT_BUILT"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class GetBotsPaginateResponsebotsTypeDef(_GetBotsPaginateResponsebotsTypeDef):
    """
    - *(dict) --*

      Provides information about a bot. .
      - **name** *(string) --*

        The name of the bot.
    """


_GetBotsPaginateResponseTypeDef = TypedDict(
    "_GetBotsPaginateResponseTypeDef",
    {"bots": List[GetBotsPaginateResponsebotsTypeDef], "NextToken": str},
    total=False,
)


class GetBotsPaginateResponseTypeDef(_GetBotsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **bots** *(list) --*

        An array of ``botMetadata`` objects, with one entry for each bot.
        - *(dict) --*

          Provides information about a bot. .
          - **name** *(string) --*

            The name of the bot.
    """


_GetBuiltinIntentsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBuiltinIntentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBuiltinIntentsPaginatePaginationConfigTypeDef(
    _GetBuiltinIntentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetBuiltinIntentsPaginateResponseintentsTypeDef = TypedDict(
    "_GetBuiltinIntentsPaginateResponseintentsTypeDef",
    {"signature": str, "supportedLocales": List[Literal["en-US", "en-GB", "de-DE"]]},
    total=False,
)


class GetBuiltinIntentsPaginateResponseintentsTypeDef(
    _GetBuiltinIntentsPaginateResponseintentsTypeDef
):
    """
    - *(dict) --*

      Provides metadata for a built-in intent.
      - **signature** *(string) --*

        A unique identifier for the built-in intent. To find the signature for an intent, see
        `Standard Built-in Intents
        <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__
        in the *Alexa Skills Kit* .
    """


_GetBuiltinIntentsPaginateResponseTypeDef = TypedDict(
    "_GetBuiltinIntentsPaginateResponseTypeDef",
    {"intents": List[GetBuiltinIntentsPaginateResponseintentsTypeDef], "NextToken": str},
    total=False,
)


class GetBuiltinIntentsPaginateResponseTypeDef(_GetBuiltinIntentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **intents** *(list) --*

        An array of ``builtinIntentMetadata`` objects, one for each intent in the response.
        - *(dict) --*

          Provides metadata for a built-in intent.
          - **signature** *(string) --*

            A unique identifier for the built-in intent. To find the signature for an intent, see
            `Standard Built-in Intents
            <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__
            in the *Alexa Skills Kit* .
    """


_GetBuiltinSlotTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBuiltinSlotTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBuiltinSlotTypesPaginatePaginationConfigTypeDef(
    _GetBuiltinSlotTypesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetBuiltinSlotTypesPaginateResponseslotTypesTypeDef = TypedDict(
    "_GetBuiltinSlotTypesPaginateResponseslotTypesTypeDef",
    {"signature": str, "supportedLocales": List[Literal["en-US", "en-GB", "de-DE"]]},
    total=False,
)


class GetBuiltinSlotTypesPaginateResponseslotTypesTypeDef(
    _GetBuiltinSlotTypesPaginateResponseslotTypesTypeDef
):
    """
    - *(dict) --*

      Provides information about a built in slot type.
      - **signature** *(string) --*

        A unique identifier for the built-in slot type. To find the signature for a slot type, see
        `Slot Type Reference
        <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference>`__
        in the *Alexa Skills Kit* .
    """


_GetBuiltinSlotTypesPaginateResponseTypeDef = TypedDict(
    "_GetBuiltinSlotTypesPaginateResponseTypeDef",
    {"slotTypes": List[GetBuiltinSlotTypesPaginateResponseslotTypesTypeDef], "NextToken": str},
    total=False,
)


class GetBuiltinSlotTypesPaginateResponseTypeDef(_GetBuiltinSlotTypesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **slotTypes** *(list) --*

        An array of ``BuiltInSlotTypeMetadata`` objects, one entry for each slot type returned.
        - *(dict) --*

          Provides information about a built in slot type.
          - **signature** *(string) --*

            A unique identifier for the built-in slot type. To find the signature for a slot type,
            see `Slot Type Reference
            <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference>`__
            in the *Alexa Skills Kit* .
    """


_GetIntentVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetIntentVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetIntentVersionsPaginatePaginationConfigTypeDef(
    _GetIntentVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetIntentVersionsPaginateResponseintentsTypeDef = TypedDict(
    "_GetIntentVersionsPaginateResponseintentsTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class GetIntentVersionsPaginateResponseintentsTypeDef(
    _GetIntentVersionsPaginateResponseintentsTypeDef
):
    """
    - *(dict) --*

      Provides information about an intent.
      - **name** *(string) --*

        The name of the intent.
    """


_GetIntentVersionsPaginateResponseTypeDef = TypedDict(
    "_GetIntentVersionsPaginateResponseTypeDef",
    {"intents": List[GetIntentVersionsPaginateResponseintentsTypeDef], "NextToken": str},
    total=False,
)


class GetIntentVersionsPaginateResponseTypeDef(_GetIntentVersionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **intents** *(list) --*

        An array of ``IntentMetadata`` objects, one for each numbered version of the intent plus one
        for the ``$LATEST`` version.
        - *(dict) --*

          Provides information about an intent.
          - **name** *(string) --*

            The name of the intent.
    """


_GetIntentsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetIntentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetIntentsPaginatePaginationConfigTypeDef(_GetIntentsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetIntentsPaginateResponseintentsTypeDef = TypedDict(
    "_GetIntentsPaginateResponseintentsTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class GetIntentsPaginateResponseintentsTypeDef(_GetIntentsPaginateResponseintentsTypeDef):
    """
    - *(dict) --*

      Provides information about an intent.
      - **name** *(string) --*

        The name of the intent.
    """


_GetIntentsPaginateResponseTypeDef = TypedDict(
    "_GetIntentsPaginateResponseTypeDef",
    {"intents": List[GetIntentsPaginateResponseintentsTypeDef], "NextToken": str},
    total=False,
)


class GetIntentsPaginateResponseTypeDef(_GetIntentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **intents** *(list) --*

        An array of ``Intent`` objects. For more information, see  PutBot .
        - *(dict) --*

          Provides information about an intent.
          - **name** *(string) --*

            The name of the intent.
    """


_GetSlotTypeVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetSlotTypeVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetSlotTypeVersionsPaginatePaginationConfigTypeDef(
    _GetSlotTypeVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetSlotTypeVersionsPaginateResponseslotTypesTypeDef = TypedDict(
    "_GetSlotTypeVersionsPaginateResponseslotTypesTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class GetSlotTypeVersionsPaginateResponseslotTypesTypeDef(
    _GetSlotTypeVersionsPaginateResponseslotTypesTypeDef
):
    """
    - *(dict) --*

      Provides information about a slot type..
      - **name** *(string) --*

        The name of the slot type.
    """


_GetSlotTypeVersionsPaginateResponseTypeDef = TypedDict(
    "_GetSlotTypeVersionsPaginateResponseTypeDef",
    {"slotTypes": List[GetSlotTypeVersionsPaginateResponseslotTypesTypeDef], "NextToken": str},
    total=False,
)


class GetSlotTypeVersionsPaginateResponseTypeDef(_GetSlotTypeVersionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **slotTypes** *(list) --*

        An array of ``SlotTypeMetadata`` objects, one for each numbered version of the slot type
        plus one for the ``$LATEST`` version.
        - *(dict) --*

          Provides information about a slot type..
          - **name** *(string) --*

            The name of the slot type.
    """


_GetSlotTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetSlotTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetSlotTypesPaginatePaginationConfigTypeDef(_GetSlotTypesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetSlotTypesPaginateResponseslotTypesTypeDef = TypedDict(
    "_GetSlotTypesPaginateResponseslotTypesTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class GetSlotTypesPaginateResponseslotTypesTypeDef(_GetSlotTypesPaginateResponseslotTypesTypeDef):
    """
    - *(dict) --*

      Provides information about a slot type..
      - **name** *(string) --*

        The name of the slot type.
    """


_GetSlotTypesPaginateResponseTypeDef = TypedDict(
    "_GetSlotTypesPaginateResponseTypeDef",
    {"slotTypes": List[GetSlotTypesPaginateResponseslotTypesTypeDef], "NextToken": str},
    total=False,
)


class GetSlotTypesPaginateResponseTypeDef(_GetSlotTypesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **slotTypes** *(list) --*

        An array of objects, one for each slot type, that provides information such as the name of
        the slot type, the version, and a description.
        - *(dict) --*

          Provides information about a slot type..
          - **name** *(string) --*

            The name of the slot type.
    """
