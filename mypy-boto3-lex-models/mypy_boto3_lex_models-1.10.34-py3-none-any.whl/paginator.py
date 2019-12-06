"Main interface for lex-models service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_lex_models.type_defs import (
    GetBotAliasesPaginatePaginationConfigTypeDef,
    GetBotAliasesPaginateResponseTypeDef,
    GetBotChannelAssociationsPaginatePaginationConfigTypeDef,
    GetBotChannelAssociationsPaginateResponseTypeDef,
    GetBotVersionsPaginatePaginationConfigTypeDef,
    GetBotVersionsPaginateResponseTypeDef,
    GetBotsPaginatePaginationConfigTypeDef,
    GetBotsPaginateResponseTypeDef,
    GetBuiltinIntentsPaginatePaginationConfigTypeDef,
    GetBuiltinIntentsPaginateResponseTypeDef,
    GetBuiltinSlotTypesPaginatePaginationConfigTypeDef,
    GetBuiltinSlotTypesPaginateResponseTypeDef,
    GetIntentVersionsPaginatePaginationConfigTypeDef,
    GetIntentVersionsPaginateResponseTypeDef,
    GetIntentsPaginatePaginationConfigTypeDef,
    GetIntentsPaginateResponseTypeDef,
    GetSlotTypeVersionsPaginatePaginationConfigTypeDef,
    GetSlotTypeVersionsPaginateResponseTypeDef,
    GetSlotTypesPaginatePaginationConfigTypeDef,
    GetSlotTypesPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
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


class GetBotAliasesPaginator(Boto3Paginator):
    """
    Paginator for `get_bot_aliases`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        botName: str,
        nameContains: str = None,
        PaginationConfig: GetBotAliasesPaginatePaginationConfigTypeDef = None,
    ) -> GetBotAliasesPaginateResponseTypeDef:
        """
        [GetBotAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases.paginate)
        """


class GetBotChannelAssociationsPaginator(Boto3Paginator):
    """
    Paginator for `get_bot_channel_associations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        botName: str,
        botAlias: str,
        nameContains: str = None,
        PaginationConfig: GetBotChannelAssociationsPaginatePaginationConfigTypeDef = None,
    ) -> GetBotChannelAssociationsPaginateResponseTypeDef:
        """
        [GetBotChannelAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations.paginate)
        """


class GetBotVersionsPaginator(Boto3Paginator):
    """
    Paginator for `get_bot_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, name: str, PaginationConfig: GetBotVersionsPaginatePaginationConfigTypeDef = None
    ) -> GetBotVersionsPaginateResponseTypeDef:
        """
        [GetBotVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions.paginate)
        """


class GetBotsPaginator(Boto3Paginator):
    """
    Paginator for `get_bots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        nameContains: str = None,
        PaginationConfig: GetBotsPaginatePaginationConfigTypeDef = None,
    ) -> GetBotsPaginateResponseTypeDef:
        """
        [GetBots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots.paginate)
        """


class GetBuiltinIntentsPaginator(Boto3Paginator):
    """
    Paginator for `get_builtin_intents`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        locale: Literal["en-US", "en-GB", "de-DE"] = None,
        signatureContains: str = None,
        PaginationConfig: GetBuiltinIntentsPaginatePaginationConfigTypeDef = None,
    ) -> GetBuiltinIntentsPaginateResponseTypeDef:
        """
        [GetBuiltinIntents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents.paginate)
        """


class GetBuiltinSlotTypesPaginator(Boto3Paginator):
    """
    Paginator for `get_builtin_slot_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        locale: Literal["en-US", "en-GB", "de-DE"] = None,
        signatureContains: str = None,
        PaginationConfig: GetBuiltinSlotTypesPaginatePaginationConfigTypeDef = None,
    ) -> GetBuiltinSlotTypesPaginateResponseTypeDef:
        """
        [GetBuiltinSlotTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes.paginate)
        """


class GetIntentVersionsPaginator(Boto3Paginator):
    """
    Paginator for `get_intent_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, name: str, PaginationConfig: GetIntentVersionsPaginatePaginationConfigTypeDef = None
    ) -> GetIntentVersionsPaginateResponseTypeDef:
        """
        [GetIntentVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions.paginate)
        """


class GetIntentsPaginator(Boto3Paginator):
    """
    Paginator for `get_intents`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        nameContains: str = None,
        PaginationConfig: GetIntentsPaginatePaginationConfigTypeDef = None,
    ) -> GetIntentsPaginateResponseTypeDef:
        """
        [GetIntents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents.paginate)
        """


class GetSlotTypeVersionsPaginator(Boto3Paginator):
    """
    Paginator for `get_slot_type_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, name: str, PaginationConfig: GetSlotTypeVersionsPaginatePaginationConfigTypeDef = None
    ) -> GetSlotTypeVersionsPaginateResponseTypeDef:
        """
        [GetSlotTypeVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions.paginate)
        """


class GetSlotTypesPaginator(Boto3Paginator):
    """
    Paginator for `get_slot_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        nameContains: str = None,
        PaginationConfig: GetSlotTypesPaginatePaginationConfigTypeDef = None,
    ) -> GetSlotTypesPaginateResponseTypeDef:
        """
        [GetSlotTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes.paginate)
        """
