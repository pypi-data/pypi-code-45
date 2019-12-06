"Main interface for transcribe service type defs"
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


ClientCreateVocabularyResponseTypeDef = TypedDict(
    "ClientCreateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef = TypedDict(
    "ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    {"MediaFileUri": str},
    total=False,
)

ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef = TypedDict(
    "ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
    },
    total=False,
)

ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef = TypedDict(
    "ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    {"TranscriptFileUri": str},
    total=False,
)

ClientGetTranscriptionJobResponseTranscriptionJobTypeDef = TypedDict(
    "ClientGetTranscriptionJobResponseTranscriptionJobTypeDef",
    {
        "TranscriptionJobName": str,
        "TranscriptionJobStatus": Literal["IN_PROGRESS", "FAILED", "COMPLETED"],
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "MediaSampleRateHertz": int,
        "MediaFormat": Literal["mp3", "mp4", "wav", "flac"],
        "Media": ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef,
        "Transcript": ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef,
    },
    total=False,
)

ClientGetTranscriptionJobResponseTypeDef = TypedDict(
    "ClientGetTranscriptionJobResponseTypeDef",
    {"TranscriptionJob": ClientGetTranscriptionJobResponseTranscriptionJobTypeDef},
    total=False,
)

ClientGetVocabularyResponseTypeDef = TypedDict(
    "ClientGetVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
    },
    total=False,
)

ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef = TypedDict(
    "ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef",
    {
        "TranscriptionJobName": str,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "TranscriptionJobStatus": Literal["IN_PROGRESS", "FAILED", "COMPLETED"],
        "FailureReason": str,
        "OutputLocationType": Literal["CUSTOMER_BUCKET", "SERVICE_BUCKET"],
    },
    total=False,
)

ClientListTranscriptionJobsResponseTypeDef = TypedDict(
    "ClientListTranscriptionJobsResponseTypeDef",
    {
        "Status": Literal["IN_PROGRESS", "FAILED", "COMPLETED"],
        "NextToken": str,
        "TranscriptionJobSummaries": List[
            ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef
        ],
    },
    total=False,
)

ClientListVocabulariesResponseVocabulariesTypeDef = TypedDict(
    "ClientListVocabulariesResponseVocabulariesTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "LastModifiedTime": datetime,
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
    },
    total=False,
)

ClientListVocabulariesResponseTypeDef = TypedDict(
    "ClientListVocabulariesResponseTypeDef",
    {
        "Status": Literal["IN_PROGRESS", "FAILED", "COMPLETED"],
        "NextToken": str,
        "Vocabularies": List[ClientListVocabulariesResponseVocabulariesTypeDef],
    },
    total=False,
)

ClientStartTranscriptionJobMediaTypeDef = TypedDict(
    "ClientStartTranscriptionJobMediaTypeDef", {"MediaFileUri": str}, total=False
)

ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef = TypedDict(
    "ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    {"MediaFileUri": str},
    total=False,
)

ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef = TypedDict(
    "ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
    },
    total=False,
)

ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef = TypedDict(
    "ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    {"TranscriptFileUri": str},
    total=False,
)

ClientStartTranscriptionJobResponseTranscriptionJobTypeDef = TypedDict(
    "ClientStartTranscriptionJobResponseTranscriptionJobTypeDef",
    {
        "TranscriptionJobName": str,
        "TranscriptionJobStatus": Literal["IN_PROGRESS", "FAILED", "COMPLETED"],
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "MediaSampleRateHertz": int,
        "MediaFormat": Literal["mp3", "mp4", "wav", "flac"],
        "Media": ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef,
        "Transcript": ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef,
    },
    total=False,
)

ClientStartTranscriptionJobResponseTypeDef = TypedDict(
    "ClientStartTranscriptionJobResponseTypeDef",
    {"TranscriptionJob": ClientStartTranscriptionJobResponseTranscriptionJobTypeDef},
    total=False,
)

ClientStartTranscriptionJobSettingsTypeDef = TypedDict(
    "ClientStartTranscriptionJobSettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
    },
    total=False,
)

ClientUpdateVocabularyResponseTypeDef = TypedDict(
    "ClientUpdateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "LastModifiedTime": datetime,
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
    },
    total=False,
)
