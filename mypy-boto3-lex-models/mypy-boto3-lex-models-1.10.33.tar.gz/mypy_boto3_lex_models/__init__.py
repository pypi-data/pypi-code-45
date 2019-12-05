"Main interface for lex-models service"

from mypy_boto3_lex_models.client import Client
from mypy_boto3_lex_models.paginator import (
    GetBotAliasesPaginator,
    GetBotChannelAssociationsPaginator,
    GetBotVersionsPaginator,
    GetBotsPaginator,
    GetBuiltinIntentsPaginator,
    GetBuiltinSlotTypesPaginator,
    GetIntentVersionsPaginator,
    GetIntentsPaginator,
    GetSlotTypeVersionsPaginator,
    GetSlotTypesPaginator,
)


__all__ = (
    "Client",
    "GetBotAliasesPaginator",
    "GetBotChannelAssociationsPaginator",
    "GetBotVersionsPaginator",
    "GetBotsPaginator",
    "GetBuiltinIntentsPaginator",
    "GetBuiltinSlotTypesPaginator",
    "GetIntentVersionsPaginator",
    "GetIntentsPaginator",
    "GetSlotTypeVersionsPaginator",
    "GetSlotTypesPaginator",
)
