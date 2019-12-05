"Main interface for polly service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_polly.type_defs import (
    DescribeVoicesPaginatePaginationConfigTypeDef,
    DescribeVoicesPaginateResponseTypeDef,
    ListLexiconsPaginatePaginationConfigTypeDef,
    ListLexiconsPaginateResponseTypeDef,
    ListSpeechSynthesisTasksPaginatePaginationConfigTypeDef,
    ListSpeechSynthesisTasksPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DescribeVoicesPaginator", "ListLexiconsPaginator", "ListSpeechSynthesisTasksPaginator")


class DescribeVoicesPaginator(Boto3Paginator):
    """
    Paginator for `describe_voices`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        IncludeAdditionalLanguageCodes: bool = None,
        PaginationConfig: DescribeVoicesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVoicesPaginateResponseTypeDef:
        """
        [DescribeVoices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/polly.html#Polly.Paginator.DescribeVoices.paginate)
        """


class ListLexiconsPaginator(Boto3Paginator):
    """
    Paginator for `list_lexicons`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListLexiconsPaginatePaginationConfigTypeDef = None
    ) -> ListLexiconsPaginateResponseTypeDef:
        """
        [ListLexicons.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/polly.html#Polly.Paginator.ListLexicons.paginate)
        """


class ListSpeechSynthesisTasksPaginator(Boto3Paginator):
    """
    Paginator for `list_speech_synthesis_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Status: Literal["scheduled", "inProgress", "completed", "failed"] = None,
        PaginationConfig: ListSpeechSynthesisTasksPaginatePaginationConfigTypeDef = None,
    ) -> ListSpeechSynthesisTasksPaginateResponseTypeDef:
        """
        [ListSpeechSynthesisTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/polly.html#Polly.Paginator.ListSpeechSynthesisTasks.paginate)
        """
