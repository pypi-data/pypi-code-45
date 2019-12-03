"Main interface for translate service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientGetTerminologyResponseTerminologyDataLocationTypeDef",
    "ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    "ClientGetTerminologyResponseTerminologyPropertiesTypeDef",
    "ClientGetTerminologyResponseTypeDef",
    "ClientImportTerminologyEncryptionKeyTypeDef",
    "ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    "ClientImportTerminologyResponseTerminologyPropertiesTypeDef",
    "ClientImportTerminologyResponseTypeDef",
    "ClientImportTerminologyTerminologyDataTypeDef",
    "ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef",
    "ClientListTerminologiesResponseTerminologyPropertiesListTypeDef",
    "ClientListTerminologiesResponseTypeDef",
    "ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef",
    "ClientTranslateTextResponseAppliedTerminologiesTypeDef",
    "ClientTranslateTextResponseTypeDef",
    "ListTerminologiesPaginatePaginationConfigTypeDef",
    "ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef",
    "ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef",
    "ListTerminologiesPaginateResponseTypeDef",
)


_ClientGetTerminologyResponseTerminologyDataLocationTypeDef = TypedDict(
    "_ClientGetTerminologyResponseTerminologyDataLocationTypeDef",
    {"RepositoryType": str, "Location": str},
    total=False,
)


class ClientGetTerminologyResponseTerminologyDataLocationTypeDef(
    _ClientGetTerminologyResponseTerminologyDataLocationTypeDef
):
    pass


_ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef = TypedDict(
    "_ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)


class ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef(
    _ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef
):
    pass


_ClientGetTerminologyResponseTerminologyPropertiesTypeDef = TypedDict(
    "_ClientGetTerminologyResponseTerminologyPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef,
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)


class ClientGetTerminologyResponseTerminologyPropertiesTypeDef(
    _ClientGetTerminologyResponseTerminologyPropertiesTypeDef
):
    """
    - **TerminologyProperties** *(dict) --*

      The properties of the custom terminology being retrieved.
      - **Name** *(string) --*

        The name of the custom terminology.
    """


_ClientGetTerminologyResponseTypeDef = TypedDict(
    "_ClientGetTerminologyResponseTypeDef",
    {
        "TerminologyProperties": ClientGetTerminologyResponseTerminologyPropertiesTypeDef,
        "TerminologyDataLocation": ClientGetTerminologyResponseTerminologyDataLocationTypeDef,
    },
    total=False,
)


class ClientGetTerminologyResponseTypeDef(_ClientGetTerminologyResponseTypeDef):
    """
    - *(dict) --*

      - **TerminologyProperties** *(dict) --*

        The properties of the custom terminology being retrieved.
        - **Name** *(string) --*

          The name of the custom terminology.
    """


_RequiredClientImportTerminologyEncryptionKeyTypeDef = TypedDict(
    "_RequiredClientImportTerminologyEncryptionKeyTypeDef", {"Type": str}
)
_OptionalClientImportTerminologyEncryptionKeyTypeDef = TypedDict(
    "_OptionalClientImportTerminologyEncryptionKeyTypeDef", {"Id": str}, total=False
)


class ClientImportTerminologyEncryptionKeyTypeDef(
    _RequiredClientImportTerminologyEncryptionKeyTypeDef,
    _OptionalClientImportTerminologyEncryptionKeyTypeDef,
):
    """
    The encryption key for the custom terminology being imported.
    - **Type** *(string) --***[REQUIRED]**

      The type of encryption key used by Amazon Translate to encrypt custom terminologies.
    """


_ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef = TypedDict(
    "_ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)


class ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef(
    _ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef
):
    pass


_ClientImportTerminologyResponseTerminologyPropertiesTypeDef = TypedDict(
    "_ClientImportTerminologyResponseTerminologyPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef,
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)


class ClientImportTerminologyResponseTerminologyPropertiesTypeDef(
    _ClientImportTerminologyResponseTerminologyPropertiesTypeDef
):
    """
    - **TerminologyProperties** *(dict) --*

      The properties of the custom terminology being imported.
      - **Name** *(string) --*

        The name of the custom terminology.
    """


_ClientImportTerminologyResponseTypeDef = TypedDict(
    "_ClientImportTerminologyResponseTypeDef",
    {"TerminologyProperties": ClientImportTerminologyResponseTerminologyPropertiesTypeDef},
    total=False,
)


class ClientImportTerminologyResponseTypeDef(_ClientImportTerminologyResponseTypeDef):
    """
    - *(dict) --*

      - **TerminologyProperties** *(dict) --*

        The properties of the custom terminology being imported.
        - **Name** *(string) --*

          The name of the custom terminology.
    """


_RequiredClientImportTerminologyTerminologyDataTypeDef = TypedDict(
    "_RequiredClientImportTerminologyTerminologyDataTypeDef", {"File": bytes}
)
_OptionalClientImportTerminologyTerminologyDataTypeDef = TypedDict(
    "_OptionalClientImportTerminologyTerminologyDataTypeDef",
    {"Format": Literal["CSV", "TMX"]},
    total=False,
)


class ClientImportTerminologyTerminologyDataTypeDef(
    _RequiredClientImportTerminologyTerminologyDataTypeDef,
    _OptionalClientImportTerminologyTerminologyDataTypeDef,
):
    """
    The terminology data for the custom terminology being imported.
    - **File** *(bytes) --***[REQUIRED]**

      The file containing the custom terminology data.
    """


_ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef = TypedDict(
    "_ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)


class ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef(
    _ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef
):
    pass


_ClientListTerminologiesResponseTerminologyPropertiesListTypeDef = TypedDict(
    "_ClientListTerminologiesResponseTerminologyPropertiesListTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef,
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)


class ClientListTerminologiesResponseTerminologyPropertiesListTypeDef(
    _ClientListTerminologiesResponseTerminologyPropertiesListTypeDef
):
    """
    - *(dict) --*

      The properties of the custom terminology.
      - **Name** *(string) --*

        The name of the custom terminology.
    """


_ClientListTerminologiesResponseTypeDef = TypedDict(
    "_ClientListTerminologiesResponseTypeDef",
    {
        "TerminologyPropertiesList": List[
            ClientListTerminologiesResponseTerminologyPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListTerminologiesResponseTypeDef(_ClientListTerminologiesResponseTypeDef):
    """
    - *(dict) --*

      - **TerminologyPropertiesList** *(list) --*

        The properties list of the custom terminologies returned on the list request.
        - *(dict) --*

          The properties of the custom terminology.
          - **Name** *(string) --*

            The name of the custom terminology.
    """


_ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef = TypedDict(
    "_ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef",
    {"SourceText": str, "TargetText": str},
    total=False,
)


class ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef(
    _ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef
):
    pass


_ClientTranslateTextResponseAppliedTerminologiesTypeDef = TypedDict(
    "_ClientTranslateTextResponseAppliedTerminologiesTypeDef",
    {"Name": str, "Terms": List[ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef]},
    total=False,
)


class ClientTranslateTextResponseAppliedTerminologiesTypeDef(
    _ClientTranslateTextResponseAppliedTerminologiesTypeDef
):
    pass


_ClientTranslateTextResponseTypeDef = TypedDict(
    "_ClientTranslateTextResponseTypeDef",
    {
        "TranslatedText": str,
        "SourceLanguageCode": str,
        "TargetLanguageCode": str,
        "AppliedTerminologies": List[ClientTranslateTextResponseAppliedTerminologiesTypeDef],
    },
    total=False,
)


class ClientTranslateTextResponseTypeDef(_ClientTranslateTextResponseTypeDef):
    """
    - *(dict) --*

      - **TranslatedText** *(string) --*

        The the translated text. The maximum length of this text is 5kb.
    """


_ListTerminologiesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTerminologiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTerminologiesPaginatePaginationConfigTypeDef(
    _ListTerminologiesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef = TypedDict(
    "_ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)


class ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef(
    _ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef
):
    pass


_ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef = TypedDict(
    "_ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef,
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)


class ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef(
    _ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef
):
    """
    - *(dict) --*

      The properties of the custom terminology.
      - **Name** *(string) --*

        The name of the custom terminology.
    """


_ListTerminologiesPaginateResponseTypeDef = TypedDict(
    "_ListTerminologiesPaginateResponseTypeDef",
    {
        "TerminologyPropertiesList": List[
            ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListTerminologiesPaginateResponseTypeDef(_ListTerminologiesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TerminologyPropertiesList** *(list) --*

        The properties list of the custom terminologies returned on the list request.
        - *(dict) --*

          The properties of the custom terminology.
          - **Name** *(string) --*

            The name of the custom terminology.
    """
