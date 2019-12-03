"Main interface for transcribe service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateVocabularyResponseTypeDef",
    "ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    "ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
    "ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    "ClientGetTranscriptionJobResponseTranscriptionJobTypeDef",
    "ClientGetTranscriptionJobResponseTypeDef",
    "ClientGetVocabularyResponseTypeDef",
    "ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef",
    "ClientListTranscriptionJobsResponseTypeDef",
    "ClientListVocabulariesResponseVocabulariesTypeDef",
    "ClientListVocabulariesResponseTypeDef",
    "ClientStartTranscriptionJobMediaTypeDef",
    "ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    "ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
    "ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    "ClientStartTranscriptionJobResponseTranscriptionJobTypeDef",
    "ClientStartTranscriptionJobResponseTypeDef",
    "ClientStartTranscriptionJobSettingsTypeDef",
    "ClientUpdateVocabularyResponseTypeDef",
)


_ClientCreateVocabularyResponseTypeDef = TypedDict(
    "_ClientCreateVocabularyResponseTypeDef",
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


class ClientCreateVocabularyResponseTypeDef(_ClientCreateVocabularyResponseTypeDef):
    """
    - *(dict) --*

      - **VocabularyName** *(string) --*

        The name of the vocabulary.
    """


_ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef = TypedDict(
    "_ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    {"MediaFileUri": str},
    total=False,
)


class ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef(
    _ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef
):
    pass


_ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef = TypedDict(
    "_ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
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


class ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef(
    _ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef
):
    pass


_ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef = TypedDict(
    "_ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    {"TranscriptFileUri": str},
    total=False,
)


class ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef(
    _ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef
):
    pass


_ClientGetTranscriptionJobResponseTranscriptionJobTypeDef = TypedDict(
    "_ClientGetTranscriptionJobResponseTranscriptionJobTypeDef",
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


class ClientGetTranscriptionJobResponseTranscriptionJobTypeDef(
    _ClientGetTranscriptionJobResponseTranscriptionJobTypeDef
):
    """
    - **TranscriptionJob** *(dict) --*

      An object that contains the results of the transcription job.
      - **TranscriptionJobName** *(string) --*

        The name of the transcription job.
    """


_ClientGetTranscriptionJobResponseTypeDef = TypedDict(
    "_ClientGetTranscriptionJobResponseTypeDef",
    {"TranscriptionJob": ClientGetTranscriptionJobResponseTranscriptionJobTypeDef},
    total=False,
)


class ClientGetTranscriptionJobResponseTypeDef(_ClientGetTranscriptionJobResponseTypeDef):
    """
    - *(dict) --*

      - **TranscriptionJob** *(dict) --*

        An object that contains the results of the transcription job.
        - **TranscriptionJobName** *(string) --*

          The name of the transcription job.
    """


_ClientGetVocabularyResponseTypeDef = TypedDict(
    "_ClientGetVocabularyResponseTypeDef",
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


class ClientGetVocabularyResponseTypeDef(_ClientGetVocabularyResponseTypeDef):
    """
    - *(dict) --*

      - **VocabularyName** *(string) --*

        The name of the vocabulary to return.
    """


_ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef = TypedDict(
    "_ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef",
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


class ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef(
    _ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef
):
    pass


_ClientListTranscriptionJobsResponseTypeDef = TypedDict(
    "_ClientListTranscriptionJobsResponseTypeDef",
    {
        "Status": Literal["IN_PROGRESS", "FAILED", "COMPLETED"],
        "NextToken": str,
        "TranscriptionJobSummaries": List[
            ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef
        ],
    },
    total=False,
)


class ClientListTranscriptionJobsResponseTypeDef(_ClientListTranscriptionJobsResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(string) --*

        The requested status of the jobs returned.
    """


_ClientListVocabulariesResponseVocabulariesTypeDef = TypedDict(
    "_ClientListVocabulariesResponseVocabulariesTypeDef",
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


class ClientListVocabulariesResponseVocabulariesTypeDef(
    _ClientListVocabulariesResponseVocabulariesTypeDef
):
    pass


_ClientListVocabulariesResponseTypeDef = TypedDict(
    "_ClientListVocabulariesResponseTypeDef",
    {
        "Status": Literal["IN_PROGRESS", "FAILED", "COMPLETED"],
        "NextToken": str,
        "Vocabularies": List[ClientListVocabulariesResponseVocabulariesTypeDef],
    },
    total=False,
)


class ClientListVocabulariesResponseTypeDef(_ClientListVocabulariesResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(string) --*

        The requested vocabulary state.
    """


_ClientStartTranscriptionJobMediaTypeDef = TypedDict(
    "_ClientStartTranscriptionJobMediaTypeDef", {"MediaFileUri": str}, total=False
)


class ClientStartTranscriptionJobMediaTypeDef(_ClientStartTranscriptionJobMediaTypeDef):
    """
    An object that describes the input media for a transcription job.
    - **MediaFileUri** *(string) --*

      The S3 location of the input media file. The URI must be in the same region as the API
      endpoint that you are calling. The general form is:

        ``https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``
    """


_ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef = TypedDict(
    "_ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    {"MediaFileUri": str},
    total=False,
)


class ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef(
    _ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef
):
    pass


_ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef = TypedDict(
    "_ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
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


class ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef(
    _ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef
):
    pass


_ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef = TypedDict(
    "_ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    {"TranscriptFileUri": str},
    total=False,
)


class ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef(
    _ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef
):
    pass


_ClientStartTranscriptionJobResponseTranscriptionJobTypeDef = TypedDict(
    "_ClientStartTranscriptionJobResponseTranscriptionJobTypeDef",
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


class ClientStartTranscriptionJobResponseTranscriptionJobTypeDef(
    _ClientStartTranscriptionJobResponseTranscriptionJobTypeDef
):
    """
    - **TranscriptionJob** *(dict) --*

      An object containing details of the asynchronous transcription job.
      - **TranscriptionJobName** *(string) --*

        The name of the transcription job.
    """


_ClientStartTranscriptionJobResponseTypeDef = TypedDict(
    "_ClientStartTranscriptionJobResponseTypeDef",
    {"TranscriptionJob": ClientStartTranscriptionJobResponseTranscriptionJobTypeDef},
    total=False,
)


class ClientStartTranscriptionJobResponseTypeDef(_ClientStartTranscriptionJobResponseTypeDef):
    """
    - *(dict) --*

      - **TranscriptionJob** *(dict) --*

        An object containing details of the asynchronous transcription job.
        - **TranscriptionJobName** *(string) --*

          The name of the transcription job.
    """


_ClientStartTranscriptionJobSettingsTypeDef = TypedDict(
    "_ClientStartTranscriptionJobSettingsTypeDef",
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


class ClientStartTranscriptionJobSettingsTypeDef(_ClientStartTranscriptionJobSettingsTypeDef):
    """
    A ``Settings`` object that provides optional settings for a transcription job.
    - **VocabularyName** *(string) --*

      The name of a vocabulary to use when processing the transcription job.
    """


_ClientUpdateVocabularyResponseTypeDef = TypedDict(
    "_ClientUpdateVocabularyResponseTypeDef",
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


class ClientUpdateVocabularyResponseTypeDef(_ClientUpdateVocabularyResponseTypeDef):
    """
    - *(dict) --*

      - **VocabularyName** *(string) --*

        The name of the vocabulary that was updated.
    """
