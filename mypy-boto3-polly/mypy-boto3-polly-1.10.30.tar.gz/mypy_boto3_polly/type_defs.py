"Main interface for polly service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.response import StreamingBody
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientDescribeVoicesResponseVoicesTypeDef",
    "ClientDescribeVoicesResponseTypeDef",
    "ClientGetLexiconResponseLexiconAttributesTypeDef",
    "ClientGetLexiconResponseLexiconTypeDef",
    "ClientGetLexiconResponseTypeDef",
    "ClientGetSpeechSynthesisTaskResponseSynthesisTaskTypeDef",
    "ClientGetSpeechSynthesisTaskResponseTypeDef",
    "ClientListLexiconsResponseLexiconsAttributesTypeDef",
    "ClientListLexiconsResponseLexiconsTypeDef",
    "ClientListLexiconsResponseTypeDef",
    "ClientListSpeechSynthesisTasksResponseSynthesisTasksTypeDef",
    "ClientListSpeechSynthesisTasksResponseTypeDef",
    "ClientStartSpeechSynthesisTaskResponseSynthesisTaskTypeDef",
    "ClientStartSpeechSynthesisTaskResponseTypeDef",
    "ClientSynthesizeSpeechResponseTypeDef",
    "DescribeVoicesPaginatePaginationConfigTypeDef",
    "DescribeVoicesPaginateResponseVoicesTypeDef",
    "DescribeVoicesPaginateResponseTypeDef",
    "ListLexiconsPaginatePaginationConfigTypeDef",
    "ListLexiconsPaginateResponseLexiconsAttributesTypeDef",
    "ListLexiconsPaginateResponseLexiconsTypeDef",
    "ListLexiconsPaginateResponseTypeDef",
    "ListSpeechSynthesisTasksPaginatePaginationConfigTypeDef",
    "ListSpeechSynthesisTasksPaginateResponseSynthesisTasksTypeDef",
    "ListSpeechSynthesisTasksPaginateResponseTypeDef",
)


_ClientDescribeVoicesResponseVoicesTypeDef = TypedDict(
    "_ClientDescribeVoicesResponseVoicesTypeDef",
    {
        "Gender": Literal["Female", "Male"],
        "Id": Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        "LanguageCode": Literal[
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
        ],
        "LanguageName": str,
        "Name": str,
        "AdditionalLanguageCodes": List[
            Literal[
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
            ]
        ],
        "SupportedEngines": List[Literal["standard", "neural"]],
    },
    total=False,
)


class ClientDescribeVoicesResponseVoicesTypeDef(_ClientDescribeVoicesResponseVoicesTypeDef):
    """
    - *(dict) --*

      Description of the voice.
      - **Gender** *(string) --*

        Gender of the voice.
    """


_ClientDescribeVoicesResponseTypeDef = TypedDict(
    "_ClientDescribeVoicesResponseTypeDef",
    {"Voices": List[ClientDescribeVoicesResponseVoicesTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeVoicesResponseTypeDef(_ClientDescribeVoicesResponseTypeDef):
    """
    - *(dict) --*

      - **Voices** *(list) --*

        A list of voices with their properties.
        - *(dict) --*

          Description of the voice.
          - **Gender** *(string) --*

            Gender of the voice.
    """


_ClientGetLexiconResponseLexiconAttributesTypeDef = TypedDict(
    "_ClientGetLexiconResponseLexiconAttributesTypeDef",
    {
        "Alphabet": str,
        "LanguageCode": Literal[
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
        ],
        "LastModified": datetime,
        "LexiconArn": str,
        "LexemesCount": int,
        "Size": int,
    },
    total=False,
)


class ClientGetLexiconResponseLexiconAttributesTypeDef(
    _ClientGetLexiconResponseLexiconAttributesTypeDef
):
    pass


_ClientGetLexiconResponseLexiconTypeDef = TypedDict(
    "_ClientGetLexiconResponseLexiconTypeDef", {"Content": str, "Name": str}, total=False
)


class ClientGetLexiconResponseLexiconTypeDef(_ClientGetLexiconResponseLexiconTypeDef):
    """
    - **Lexicon** *(dict) --*

      Lexicon object that provides name and the string content of the lexicon.
      - **Content** *(string) --*

        Lexicon content in string format. The content of a lexicon must be in PLS format.
    """


_ClientGetLexiconResponseTypeDef = TypedDict(
    "_ClientGetLexiconResponseTypeDef",
    {
        "Lexicon": ClientGetLexiconResponseLexiconTypeDef,
        "LexiconAttributes": ClientGetLexiconResponseLexiconAttributesTypeDef,
    },
    total=False,
)


class ClientGetLexiconResponseTypeDef(_ClientGetLexiconResponseTypeDef):
    """
    - *(dict) --*

      - **Lexicon** *(dict) --*

        Lexicon object that provides name and the string content of the lexicon.
        - **Content** *(string) --*

          Lexicon content in string format. The content of a lexicon must be in PLS format.
    """


_ClientGetSpeechSynthesisTaskResponseSynthesisTaskTypeDef = TypedDict(
    "_ClientGetSpeechSynthesisTaskResponseSynthesisTaskTypeDef",
    {
        "Engine": Literal["standard", "neural"],
        "TaskId": str,
        "TaskStatus": Literal["scheduled", "inProgress", "completed", "failed"],
        "TaskStatusReason": str,
        "OutputUri": str,
        "CreationTime": datetime,
        "RequestCharacters": int,
        "SnsTopicArn": str,
        "LexiconNames": List[str],
        "OutputFormat": Literal["json", "mp3", "ogg_vorbis", "pcm"],
        "SampleRate": str,
        "SpeechMarkTypes": List[Literal["sentence", "ssml", "viseme", "word"]],
        "TextType": Literal["ssml", "text"],
        "VoiceId": Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        "LanguageCode": Literal[
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
        ],
    },
    total=False,
)


class ClientGetSpeechSynthesisTaskResponseSynthesisTaskTypeDef(
    _ClientGetSpeechSynthesisTaskResponseSynthesisTaskTypeDef
):
    """
    - **SynthesisTask** *(dict) --*

      SynthesisTask object that provides information from the requested task, including output
      format, creation time, task status, and so on.
      - **Engine** *(string) --*

        Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when processing
        input text for speech synthesis. Using a voice that is not supported for the engine selected
        will result in an error.
    """


_ClientGetSpeechSynthesisTaskResponseTypeDef = TypedDict(
    "_ClientGetSpeechSynthesisTaskResponseTypeDef",
    {"SynthesisTask": ClientGetSpeechSynthesisTaskResponseSynthesisTaskTypeDef},
    total=False,
)


class ClientGetSpeechSynthesisTaskResponseTypeDef(_ClientGetSpeechSynthesisTaskResponseTypeDef):
    """
    - *(dict) --*

      - **SynthesisTask** *(dict) --*

        SynthesisTask object that provides information from the requested task, including output
        format, creation time, task status, and so on.
        - **Engine** *(string) --*

          Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when processing
          input text for speech synthesis. Using a voice that is not supported for the engine
          selected will result in an error.
    """


_ClientListLexiconsResponseLexiconsAttributesTypeDef = TypedDict(
    "_ClientListLexiconsResponseLexiconsAttributesTypeDef",
    {
        "Alphabet": str,
        "LanguageCode": Literal[
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
        ],
        "LastModified": datetime,
        "LexiconArn": str,
        "LexemesCount": int,
        "Size": int,
    },
    total=False,
)


class ClientListLexiconsResponseLexiconsAttributesTypeDef(
    _ClientListLexiconsResponseLexiconsAttributesTypeDef
):
    pass


_ClientListLexiconsResponseLexiconsTypeDef = TypedDict(
    "_ClientListLexiconsResponseLexiconsTypeDef",
    {"Name": str, "Attributes": ClientListLexiconsResponseLexiconsAttributesTypeDef},
    total=False,
)


class ClientListLexiconsResponseLexiconsTypeDef(_ClientListLexiconsResponseLexiconsTypeDef):
    """
    - *(dict) --*

      Describes the content of the lexicon.
      - **Name** *(string) --*

        Name of the lexicon.
    """


_ClientListLexiconsResponseTypeDef = TypedDict(
    "_ClientListLexiconsResponseTypeDef",
    {"Lexicons": List[ClientListLexiconsResponseLexiconsTypeDef], "NextToken": str},
    total=False,
)


class ClientListLexiconsResponseTypeDef(_ClientListLexiconsResponseTypeDef):
    """
    - *(dict) --*

      - **Lexicons** *(list) --*

        A list of lexicon names and attributes.
        - *(dict) --*

          Describes the content of the lexicon.
          - **Name** *(string) --*

            Name of the lexicon.
    """


_ClientListSpeechSynthesisTasksResponseSynthesisTasksTypeDef = TypedDict(
    "_ClientListSpeechSynthesisTasksResponseSynthesisTasksTypeDef",
    {
        "Engine": Literal["standard", "neural"],
        "TaskId": str,
        "TaskStatus": Literal["scheduled", "inProgress", "completed", "failed"],
        "TaskStatusReason": str,
        "OutputUri": str,
        "CreationTime": datetime,
        "RequestCharacters": int,
        "SnsTopicArn": str,
        "LexiconNames": List[str],
        "OutputFormat": Literal["json", "mp3", "ogg_vorbis", "pcm"],
        "SampleRate": str,
        "SpeechMarkTypes": List[Literal["sentence", "ssml", "viseme", "word"]],
        "TextType": Literal["ssml", "text"],
        "VoiceId": Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        "LanguageCode": Literal[
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
        ],
    },
    total=False,
)


class ClientListSpeechSynthesisTasksResponseSynthesisTasksTypeDef(
    _ClientListSpeechSynthesisTasksResponseSynthesisTasksTypeDef
):
    pass


_ClientListSpeechSynthesisTasksResponseTypeDef = TypedDict(
    "_ClientListSpeechSynthesisTasksResponseTypeDef",
    {
        "NextToken": str,
        "SynthesisTasks": List[ClientListSpeechSynthesisTasksResponseSynthesisTasksTypeDef],
    },
    total=False,
)


class ClientListSpeechSynthesisTasksResponseTypeDef(_ClientListSpeechSynthesisTasksResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        An opaque pagination token returned from the previous List operation in this request. If
        present, this indicates where to continue the listing.
    """


_ClientStartSpeechSynthesisTaskResponseSynthesisTaskTypeDef = TypedDict(
    "_ClientStartSpeechSynthesisTaskResponseSynthesisTaskTypeDef",
    {
        "Engine": Literal["standard", "neural"],
        "TaskId": str,
        "TaskStatus": Literal["scheduled", "inProgress", "completed", "failed"],
        "TaskStatusReason": str,
        "OutputUri": str,
        "CreationTime": datetime,
        "RequestCharacters": int,
        "SnsTopicArn": str,
        "LexiconNames": List[str],
        "OutputFormat": Literal["json", "mp3", "ogg_vorbis", "pcm"],
        "SampleRate": str,
        "SpeechMarkTypes": List[Literal["sentence", "ssml", "viseme", "word"]],
        "TextType": Literal["ssml", "text"],
        "VoiceId": Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        "LanguageCode": Literal[
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
        ],
    },
    total=False,
)


class ClientStartSpeechSynthesisTaskResponseSynthesisTaskTypeDef(
    _ClientStartSpeechSynthesisTaskResponseSynthesisTaskTypeDef
):
    """
    - **SynthesisTask** *(dict) --*

      SynthesisTask object that provides information and attributes about a newly submitted speech
      synthesis task.
      - **Engine** *(string) --*

        Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when processing
        input text for speech synthesis. Using a voice that is not supported for the engine selected
        will result in an error.
    """


_ClientStartSpeechSynthesisTaskResponseTypeDef = TypedDict(
    "_ClientStartSpeechSynthesisTaskResponseTypeDef",
    {"SynthesisTask": ClientStartSpeechSynthesisTaskResponseSynthesisTaskTypeDef},
    total=False,
)


class ClientStartSpeechSynthesisTaskResponseTypeDef(_ClientStartSpeechSynthesisTaskResponseTypeDef):
    """
    - *(dict) --*

      - **SynthesisTask** *(dict) --*

        SynthesisTask object that provides information and attributes about a newly submitted speech
        synthesis task.
        - **Engine** *(string) --*

          Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when processing
          input text for speech synthesis. Using a voice that is not supported for the engine
          selected will result in an error.
    """


_ClientSynthesizeSpeechResponseTypeDef = TypedDict(
    "_ClientSynthesizeSpeechResponseTypeDef",
    {"AudioStream": StreamingBody, "ContentType": str, "RequestCharacters": int},
    total=False,
)


class ClientSynthesizeSpeechResponseTypeDef(_ClientSynthesizeSpeechResponseTypeDef):
    """
    - *(dict) --*

      - **AudioStream** (:class:`.StreamingBody`) --

        Stream containing the synthesized speech.
    """


_DescribeVoicesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeVoicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeVoicesPaginatePaginationConfigTypeDef(_DescribeVoicesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeVoicesPaginateResponseVoicesTypeDef = TypedDict(
    "_DescribeVoicesPaginateResponseVoicesTypeDef",
    {
        "Gender": Literal["Female", "Male"],
        "Id": Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        "LanguageCode": Literal[
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
        ],
        "LanguageName": str,
        "Name": str,
        "AdditionalLanguageCodes": List[
            Literal[
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
            ]
        ],
        "SupportedEngines": List[Literal["standard", "neural"]],
    },
    total=False,
)


class DescribeVoicesPaginateResponseVoicesTypeDef(_DescribeVoicesPaginateResponseVoicesTypeDef):
    """
    - *(dict) --*

      Description of the voice.
      - **Gender** *(string) --*

        Gender of the voice.
    """


_DescribeVoicesPaginateResponseTypeDef = TypedDict(
    "_DescribeVoicesPaginateResponseTypeDef",
    {"Voices": List[DescribeVoicesPaginateResponseVoicesTypeDef]},
    total=False,
)


class DescribeVoicesPaginateResponseTypeDef(_DescribeVoicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Voices** *(list) --*

        A list of voices with their properties.
        - *(dict) --*

          Description of the voice.
          - **Gender** *(string) --*

            Gender of the voice.
    """


_ListLexiconsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLexiconsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListLexiconsPaginatePaginationConfigTypeDef(_ListLexiconsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListLexiconsPaginateResponseLexiconsAttributesTypeDef = TypedDict(
    "_ListLexiconsPaginateResponseLexiconsAttributesTypeDef",
    {
        "Alphabet": str,
        "LanguageCode": Literal[
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
        ],
        "LastModified": datetime,
        "LexiconArn": str,
        "LexemesCount": int,
        "Size": int,
    },
    total=False,
)


class ListLexiconsPaginateResponseLexiconsAttributesTypeDef(
    _ListLexiconsPaginateResponseLexiconsAttributesTypeDef
):
    pass


_ListLexiconsPaginateResponseLexiconsTypeDef = TypedDict(
    "_ListLexiconsPaginateResponseLexiconsTypeDef",
    {"Name": str, "Attributes": ListLexiconsPaginateResponseLexiconsAttributesTypeDef},
    total=False,
)


class ListLexiconsPaginateResponseLexiconsTypeDef(_ListLexiconsPaginateResponseLexiconsTypeDef):
    """
    - *(dict) --*

      Describes the content of the lexicon.
      - **Name** *(string) --*

        Name of the lexicon.
    """


_ListLexiconsPaginateResponseTypeDef = TypedDict(
    "_ListLexiconsPaginateResponseTypeDef",
    {"Lexicons": List[ListLexiconsPaginateResponseLexiconsTypeDef]},
    total=False,
)


class ListLexiconsPaginateResponseTypeDef(_ListLexiconsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Lexicons** *(list) --*

        A list of lexicon names and attributes.
        - *(dict) --*

          Describes the content of the lexicon.
          - **Name** *(string) --*

            Name of the lexicon.
    """


_ListSpeechSynthesisTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSpeechSynthesisTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSpeechSynthesisTasksPaginatePaginationConfigTypeDef(
    _ListSpeechSynthesisTasksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSpeechSynthesisTasksPaginateResponseSynthesisTasksTypeDef = TypedDict(
    "_ListSpeechSynthesisTasksPaginateResponseSynthesisTasksTypeDef",
    {
        "Engine": Literal["standard", "neural"],
        "TaskId": str,
        "TaskStatus": Literal["scheduled", "inProgress", "completed", "failed"],
        "TaskStatusReason": str,
        "OutputUri": str,
        "CreationTime": datetime,
        "RequestCharacters": int,
        "SnsTopicArn": str,
        "LexiconNames": List[str],
        "OutputFormat": Literal["json", "mp3", "ogg_vorbis", "pcm"],
        "SampleRate": str,
        "SpeechMarkTypes": List[Literal["sentence", "ssml", "viseme", "word"]],
        "TextType": Literal["ssml", "text"],
        "VoiceId": Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        "LanguageCode": Literal[
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
        ],
    },
    total=False,
)


class ListSpeechSynthesisTasksPaginateResponseSynthesisTasksTypeDef(
    _ListSpeechSynthesisTasksPaginateResponseSynthesisTasksTypeDef
):
    """
    - *(dict) --*

      SynthesisTask object that provides information about a speech synthesis task.
      - **Engine** *(string) --*

        Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when processing
        input text for speech synthesis. Using a voice that is not supported for the engine selected
        will result in an error.
    """


_ListSpeechSynthesisTasksPaginateResponseTypeDef = TypedDict(
    "_ListSpeechSynthesisTasksPaginateResponseTypeDef",
    {"SynthesisTasks": List[ListSpeechSynthesisTasksPaginateResponseSynthesisTasksTypeDef]},
    total=False,
)


class ListSpeechSynthesisTasksPaginateResponseTypeDef(
    _ListSpeechSynthesisTasksPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **SynthesisTasks** *(list) --*

        List of SynthesisTask objects that provides information from the specified task in the list
        request, including output format, creation time, task status, and so on.
        - *(dict) --*

          SynthesisTask object that provides information about a speech synthesis task.
          - **Engine** *(string) --*

            Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when
            processing input text for speech synthesis. Using a voice that is not supported for the
            engine selected will result in an error.
    """
