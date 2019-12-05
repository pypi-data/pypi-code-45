"Main interface for polly service"

from mypy_boto3_polly.client import Client
from mypy_boto3_polly.paginator import (
    DescribeVoicesPaginator,
    ListLexiconsPaginator,
    ListSpeechSynthesisTasksPaginator,
)


__all__ = (
    "Client",
    "DescribeVoicesPaginator",
    "ListLexiconsPaginator",
    "ListSpeechSynthesisTasksPaginator",
)
