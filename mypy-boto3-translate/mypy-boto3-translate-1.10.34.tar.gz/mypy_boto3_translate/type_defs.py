"Main interface for translate service type defs"
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


ClientGetTerminologyResponseTerminologyDataLocationTypeDef = TypedDict(
    "ClientGetTerminologyResponseTerminologyDataLocationTypeDef",
    {"RepositoryType": str, "Location": str},
    total=False,
)

ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef = TypedDict(
    "ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)

ClientGetTerminologyResponseTerminologyPropertiesTypeDef = TypedDict(
    "ClientGetTerminologyResponseTerminologyPropertiesTypeDef",
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

ClientGetTerminologyResponseTypeDef = TypedDict(
    "ClientGetTerminologyResponseTypeDef",
    {
        "TerminologyProperties": ClientGetTerminologyResponseTerminologyPropertiesTypeDef,
        "TerminologyDataLocation": ClientGetTerminologyResponseTerminologyDataLocationTypeDef,
    },
    total=False,
)

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
    pass


ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef = TypedDict(
    "ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)

ClientImportTerminologyResponseTerminologyPropertiesTypeDef = TypedDict(
    "ClientImportTerminologyResponseTerminologyPropertiesTypeDef",
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

ClientImportTerminologyResponseTypeDef = TypedDict(
    "ClientImportTerminologyResponseTypeDef",
    {"TerminologyProperties": ClientImportTerminologyResponseTerminologyPropertiesTypeDef},
    total=False,
)

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
    pass


ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef = TypedDict(
    "ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)

ClientListTerminologiesResponseTerminologyPropertiesListTypeDef = TypedDict(
    "ClientListTerminologiesResponseTerminologyPropertiesListTypeDef",
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

ClientListTerminologiesResponseTypeDef = TypedDict(
    "ClientListTerminologiesResponseTypeDef",
    {
        "TerminologyPropertiesList": List[
            ClientListTerminologiesResponseTerminologyPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef = TypedDict(
    "ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef",
    {"SourceText": str, "TargetText": str},
    total=False,
)

ClientTranslateTextResponseAppliedTerminologiesTypeDef = TypedDict(
    "ClientTranslateTextResponseAppliedTerminologiesTypeDef",
    {"Name": str, "Terms": List[ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef]},
    total=False,
)

ClientTranslateTextResponseTypeDef = TypedDict(
    "ClientTranslateTextResponseTypeDef",
    {
        "TranslatedText": str,
        "SourceLanguageCode": str,
        "TargetLanguageCode": str,
        "AppliedTerminologies": List[ClientTranslateTextResponseAppliedTerminologiesTypeDef],
    },
    total=False,
)

ListTerminologiesPaginatePaginationConfigTypeDef = TypedDict(
    "ListTerminologiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef = TypedDict(
    "ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)

ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef = TypedDict(
    "ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef",
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

ListTerminologiesPaginateResponseTypeDef = TypedDict(
    "ListTerminologiesPaginateResponseTypeDef",
    {
        "TerminologyPropertiesList": List[
            ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef
        ]
    },
    total=False,
)
