"Main interface for cloudsearch service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBuildSuggestersResponseTypeDef",
    "ClientCreateDomainResponseDomainStatusDocServiceTypeDef",
    "ClientCreateDomainResponseDomainStatusLimitsTypeDef",
    "ClientCreateDomainResponseDomainStatusSearchServiceTypeDef",
    "ClientCreateDomainResponseDomainStatusTypeDef",
    "ClientCreateDomainResponseTypeDef",
    "ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef",
    "ClientDefineAnalysisSchemeAnalysisSchemeTypeDef",
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef",
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef",
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef",
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef",
    "ClientDefineAnalysisSchemeResponseTypeDef",
    "ClientDefineExpressionExpressionTypeDef",
    "ClientDefineExpressionResponseExpressionOptionsTypeDef",
    "ClientDefineExpressionResponseExpressionStatusTypeDef",
    "ClientDefineExpressionResponseExpressionTypeDef",
    "ClientDefineExpressionResponseTypeDef",
    "ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldDateOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldIntOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldTextOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldStatusTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldTypeDef",
    "ClientDefineIndexFieldResponseTypeDef",
    "ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef",
    "ClientDefineSuggesterResponseSuggesterOptionsTypeDef",
    "ClientDefineSuggesterResponseSuggesterStatusTypeDef",
    "ClientDefineSuggesterResponseSuggesterTypeDef",
    "ClientDefineSuggesterResponseTypeDef",
    "ClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef",
    "ClientDefineSuggesterSuggesterTypeDef",
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef",
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef",
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef",
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef",
    "ClientDeleteAnalysisSchemeResponseTypeDef",
    "ClientDeleteDomainResponseDomainStatusDocServiceTypeDef",
    "ClientDeleteDomainResponseDomainStatusLimitsTypeDef",
    "ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef",
    "ClientDeleteDomainResponseDomainStatusTypeDef",
    "ClientDeleteDomainResponseTypeDef",
    "ClientDeleteExpressionResponseExpressionOptionsTypeDef",
    "ClientDeleteExpressionResponseExpressionStatusTypeDef",
    "ClientDeleteExpressionResponseExpressionTypeDef",
    "ClientDeleteExpressionResponseTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldTypeDef",
    "ClientDeleteIndexFieldResponseTypeDef",
    "ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef",
    "ClientDeleteSuggesterResponseSuggesterOptionsTypeDef",
    "ClientDeleteSuggesterResponseSuggesterStatusTypeDef",
    "ClientDeleteSuggesterResponseSuggesterTypeDef",
    "ClientDeleteSuggesterResponseTypeDef",
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef",
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef",
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef",
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef",
    "ClientDescribeAnalysisSchemesResponseTypeDef",
    "ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef",
    "ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef",
    "ClientDescribeAvailabilityOptionsResponseTypeDef",
    "ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef",
    "ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef",
    "ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef",
    "ClientDescribeDomainEndpointOptionsResponseTypeDef",
    "ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef",
    "ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef",
    "ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef",
    "ClientDescribeDomainsResponseDomainStatusListTypeDef",
    "ClientDescribeDomainsResponseTypeDef",
    "ClientDescribeExpressionsResponseExpressionsOptionsTypeDef",
    "ClientDescribeExpressionsResponseExpressionsStatusTypeDef",
    "ClientDescribeExpressionsResponseExpressionsTypeDef",
    "ClientDescribeExpressionsResponseTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsTypeDef",
    "ClientDescribeIndexFieldsResponseTypeDef",
    "ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef",
    "ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef",
    "ClientDescribeScalingParametersResponseScalingParametersTypeDef",
    "ClientDescribeScalingParametersResponseTypeDef",
    "ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef",
    "ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef",
    "ClientDescribeServiceAccessPoliciesResponseTypeDef",
    "ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef",
    "ClientDescribeSuggestersResponseSuggestersOptionsTypeDef",
    "ClientDescribeSuggestersResponseSuggestersStatusTypeDef",
    "ClientDescribeSuggestersResponseSuggestersTypeDef",
    "ClientDescribeSuggestersResponseTypeDef",
    "ClientIndexDocumentsResponseTypeDef",
    "ClientListDomainNamesResponseTypeDef",
    "ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef",
    "ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef",
    "ClientUpdateAvailabilityOptionsResponseTypeDef",
    "ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef",
    "ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef",
    "ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef",
    "ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef",
    "ClientUpdateDomainEndpointOptionsResponseTypeDef",
    "ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef",
    "ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef",
    "ClientUpdateScalingParametersResponseScalingParametersTypeDef",
    "ClientUpdateScalingParametersResponseTypeDef",
    "ClientUpdateScalingParametersScalingParametersTypeDef",
    "ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef",
    "ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef",
    "ClientUpdateServiceAccessPoliciesResponseTypeDef",
)


_ClientBuildSuggestersResponseTypeDef = TypedDict(
    "_ClientBuildSuggestersResponseTypeDef", {"FieldNames": List[str]}, total=False
)


class ClientBuildSuggestersResponseTypeDef(_ClientBuildSuggestersResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``BuildSuggester`` request. Contains a list of the fields used for
      suggestions.
      - **FieldNames** *(list) --*

        A list of field names.
        - *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
          ends with a wildcard. Any document fields that don't map to a regular index field but do
          match a dynamic field's pattern are configured with the dynamic field's indexing options.
          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.
          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .
    """


_ClientCreateDomainResponseDomainStatusDocServiceTypeDef = TypedDict(
    "_ClientCreateDomainResponseDomainStatusDocServiceTypeDef", {"Endpoint": str}, total=False
)


class ClientCreateDomainResponseDomainStatusDocServiceTypeDef(
    _ClientCreateDomainResponseDomainStatusDocServiceTypeDef
):
    pass


_ClientCreateDomainResponseDomainStatusLimitsTypeDef = TypedDict(
    "_ClientCreateDomainResponseDomainStatusLimitsTypeDef",
    {"MaximumReplicationCount": int, "MaximumPartitionCount": int},
    total=False,
)


class ClientCreateDomainResponseDomainStatusLimitsTypeDef(
    _ClientCreateDomainResponseDomainStatusLimitsTypeDef
):
    pass


_ClientCreateDomainResponseDomainStatusSearchServiceTypeDef = TypedDict(
    "_ClientCreateDomainResponseDomainStatusSearchServiceTypeDef", {"Endpoint": str}, total=False
)


class ClientCreateDomainResponseDomainStatusSearchServiceTypeDef(
    _ClientCreateDomainResponseDomainStatusSearchServiceTypeDef
):
    pass


_ClientCreateDomainResponseDomainStatusTypeDef = TypedDict(
    "_ClientCreateDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "DocService": ClientCreateDomainResponseDomainStatusDocServiceTypeDef,
        "SearchService": ClientCreateDomainResponseDomainStatusSearchServiceTypeDef,
        "RequiresIndexDocuments": bool,
        "Processing": bool,
        "SearchInstanceType": str,
        "SearchPartitionCount": int,
        "SearchInstanceCount": int,
        "Limits": ClientCreateDomainResponseDomainStatusLimitsTypeDef,
    },
    total=False,
)


class ClientCreateDomainResponseDomainStatusTypeDef(_ClientCreateDomainResponseDomainStatusTypeDef):
    """
    - **DomainStatus** *(dict) --*

      The current status of the search domain.
      - **DomainId** *(string) --*

        An internally generated unique identifier for a domain.
    """


_ClientCreateDomainResponseTypeDef = TypedDict(
    "_ClientCreateDomainResponseTypeDef",
    {"DomainStatus": ClientCreateDomainResponseDomainStatusTypeDef},
    total=False,
)


class ClientCreateDomainResponseTypeDef(_ClientCreateDomainResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``CreateDomainRequest`` . Contains the status of a newly created domain.
      - **DomainStatus** *(dict) --*

        The current status of the search domain.
        - **DomainId** *(string) --*

          An internally generated unique identifier for a domain.
    """


_ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef = TypedDict(
    "_ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": Literal["none", "minimal", "light", "full"],
    },
    total=False,
)


class ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef(
    _ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef
):
    pass


_RequiredClientDefineAnalysisSchemeAnalysisSchemeTypeDef = TypedDict(
    "_RequiredClientDefineAnalysisSchemeAnalysisSchemeTypeDef", {"AnalysisSchemeName": str}
)
_OptionalClientDefineAnalysisSchemeAnalysisSchemeTypeDef = TypedDict(
    "_OptionalClientDefineAnalysisSchemeAnalysisSchemeTypeDef",
    {
        "AnalysisSchemeLanguage": Literal[
            "ar",
            "bg",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "eu",
            "fa",
            "fi",
            "fr",
            "ga",
            "gl",
            "he",
            "hi",
            "hu",
            "hy",
            "id",
            "it",
            "ja",
            "ko",
            "lv",
            "mul",
            "nl",
            "no",
            "pt",
            "ro",
            "ru",
            "sv",
            "th",
            "tr",
            "zh-Hans",
            "zh-Hant",
        ],
        "AnalysisOptions": ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef,
    },
    total=False,
)


class ClientDefineAnalysisSchemeAnalysisSchemeTypeDef(
    _RequiredClientDefineAnalysisSchemeAnalysisSchemeTypeDef,
    _OptionalClientDefineAnalysisSchemeAnalysisSchemeTypeDef,
):
    """
    Configuration information for an analysis scheme. Each analysis scheme has a unique name and
    specifies the language of the text to be processed. The following options can be configured for
    an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
    ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .
    - **AnalysisSchemeName** *(string) --***[REQUIRED]**

      Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9,
      and _ (underscore).
    """


_ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef = TypedDict(
    "_ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": Literal["none", "minimal", "light", "full"],
    },
    total=False,
)


class ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef(
    _ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef
):
    pass


_ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef = TypedDict(
    "_ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": Literal[
            "ar",
            "bg",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "eu",
            "fa",
            "fi",
            "fr",
            "ga",
            "gl",
            "he",
            "hi",
            "hu",
            "hy",
            "id",
            "it",
            "ja",
            "ko",
            "lv",
            "mul",
            "nl",
            "no",
            "pt",
            "ro",
            "ru",
            "sv",
            "th",
            "tr",
            "zh-Hans",
            "zh-Hant",
        ],
        "AnalysisOptions": ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef,
    },
    total=False,
)


class ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef(
    _ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      Configuration information for an analysis scheme. Each analysis scheme has a unique name and
      specifies the language of the text to be processed. The following options can be configured
      for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
      ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .
      - **AnalysisSchemeName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).
    """


_ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef = TypedDict(
    "_ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef(
    _ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef
):
    pass


_ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef = TypedDict(
    "_ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef",
    {
        "Options": ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef,
        "Status": ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef,
    },
    total=False,
)


class ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef(
    _ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef
):
    """
    - **AnalysisScheme** *(dict) --*

      The status and configuration of an ``AnalysisScheme`` .
      - **Options** *(dict) --*

        Configuration information for an analysis scheme. Each analysis scheme has a unique name and
        specifies the language of the text to be processed. The following options can be configured
        for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
        ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .
        - **AnalysisSchemeName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).
    """


_ClientDefineAnalysisSchemeResponseTypeDef = TypedDict(
    "_ClientDefineAnalysisSchemeResponseTypeDef",
    {"AnalysisScheme": ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef},
    total=False,
)


class ClientDefineAnalysisSchemeResponseTypeDef(_ClientDefineAnalysisSchemeResponseTypeDef):
    """
    - *(dict) --*

      The result of a `` DefineAnalysisScheme`` request. Contains the status of the newly-configured
      analysis scheme.
      - **AnalysisScheme** *(dict) --*

        The status and configuration of an ``AnalysisScheme`` .
        - **Options** *(dict) --*

          Configuration information for an analysis scheme. Each analysis scheme has a unique name
          and specifies the language of the text to be processed. The following options can be
          configured for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
          ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .
          - **AnalysisSchemeName** *(string) --*

            Names must begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore).
    """


_RequiredClientDefineExpressionExpressionTypeDef = TypedDict(
    "_RequiredClientDefineExpressionExpressionTypeDef", {"ExpressionName": str}
)
_OptionalClientDefineExpressionExpressionTypeDef = TypedDict(
    "_OptionalClientDefineExpressionExpressionTypeDef", {"ExpressionValue": str}, total=False
)


class ClientDefineExpressionExpressionTypeDef(
    _RequiredClientDefineExpressionExpressionTypeDef,
    _OptionalClientDefineExpressionExpressionTypeDef,
):
    """
    A named expression that can be evaluated at search time. Can be used to sort the search results,
    define other expressions, or return computed information in the search results.
    - **ExpressionName** *(string) --***[REQUIRED]**

      Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9,
      and _ (underscore).
    """


_ClientDefineExpressionResponseExpressionOptionsTypeDef = TypedDict(
    "_ClientDefineExpressionResponseExpressionOptionsTypeDef",
    {"ExpressionName": str, "ExpressionValue": str},
    total=False,
)


class ClientDefineExpressionResponseExpressionOptionsTypeDef(
    _ClientDefineExpressionResponseExpressionOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      The expression that is evaluated for sorting while processing a search request.
      - **ExpressionName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).
    """


_ClientDefineExpressionResponseExpressionStatusTypeDef = TypedDict(
    "_ClientDefineExpressionResponseExpressionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDefineExpressionResponseExpressionStatusTypeDef(
    _ClientDefineExpressionResponseExpressionStatusTypeDef
):
    pass


_ClientDefineExpressionResponseExpressionTypeDef = TypedDict(
    "_ClientDefineExpressionResponseExpressionTypeDef",
    {
        "Options": ClientDefineExpressionResponseExpressionOptionsTypeDef,
        "Status": ClientDefineExpressionResponseExpressionStatusTypeDef,
    },
    total=False,
)


class ClientDefineExpressionResponseExpressionTypeDef(
    _ClientDefineExpressionResponseExpressionTypeDef
):
    """
    - **Expression** *(dict) --*

      The value of an ``Expression`` and its current status.
      - **Options** *(dict) --*

        The expression that is evaluated for sorting while processing a search request.
        - **ExpressionName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).
    """


_ClientDefineExpressionResponseTypeDef = TypedDict(
    "_ClientDefineExpressionResponseTypeDef",
    {"Expression": ClientDefineExpressionResponseExpressionTypeDef},
    total=False,
)


class ClientDefineExpressionResponseTypeDef(_ClientDefineExpressionResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``DefineExpression`` request. Contains the status of the newly-configured
      expression.
      - **Expression** *(dict) --*

        The value of an ``Expression`` and its current status.
        - **Options** *(dict) --*

          The expression that is evaluated for sorting while processing a search request.
          - **ExpressionName** *(string) --*

            Names must begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore).
    """


_ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef
):
    pass


_ClientDefineIndexFieldIndexFieldDateOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldDateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldDateOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldDateOptionsTypeDef
):
    pass


_ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef
):
    pass


_ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef
):
    pass


_ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef
):
    pass


_ClientDefineIndexFieldIndexFieldIntOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldIntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldIntOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldIntOptionsTypeDef
):
    pass


_ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef
):
    pass


_ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef
):
    pass


_ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef
):
    pass


_ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef
):
    pass


_ClientDefineIndexFieldIndexFieldTextOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldIndexFieldTextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldTextOptionsTypeDef(
    _ClientDefineIndexFieldIndexFieldTextOptionsTypeDef
):
    pass


_RequiredClientDefineIndexFieldIndexFieldTypeDef = TypedDict(
    "_RequiredClientDefineIndexFieldIndexFieldTypeDef", {"IndexFieldName": str}
)
_OptionalClientDefineIndexFieldIndexFieldTypeDef = TypedDict(
    "_OptionalClientDefineIndexFieldIndexFieldTypeDef",
    {
        "IndexFieldType": Literal[
            "int",
            "double",
            "literal",
            "text",
            "date",
            "latlon",
            "int-array",
            "double-array",
            "literal-array",
            "text-array",
            "date-array",
        ],
        "IntOptions": ClientDefineIndexFieldIndexFieldIntOptionsTypeDef,
        "DoubleOptions": ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef,
        "LiteralOptions": ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef,
        "TextOptions": ClientDefineIndexFieldIndexFieldTextOptionsTypeDef,
        "DateOptions": ClientDefineIndexFieldIndexFieldDateOptionsTypeDef,
        "LatLonOptions": ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef,
        "IntArrayOptions": ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef,
        "DoubleArrayOptions": ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef,
        "LiteralArrayOptions": ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef,
        "TextArrayOptions": ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef,
        "DateArrayOptions": ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldTypeDef(
    _RequiredClientDefineIndexFieldIndexFieldTypeDef,
    _OptionalClientDefineIndexFieldIndexFieldTypeDef,
):
    """
    The index field and field options you want to configure.
    - **IndexFieldName** *(string) --***[REQUIRED]**

      A string that represents the name of an index field. CloudSearch supports regular index fields
      as well as dynamic fields. A dynamic field's name defines a pattern that begins or ends with a
      wildcard. Any document fields that don't map to a regular index field but do match a dynamic
      field's pattern are configured with the dynamic field's indexing options.
      Regular field names begin with a letter and can contain the following characters: a-z
      (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
      (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards,
      and wildcards embedded within a string are not supported.
      The name ``score`` is reserved and cannot be used as a field name. To reference a document's
      ID, you can use the name ``_id`` .
    """


_ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef
):
    pass


_ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef
):
    pass


_ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef
):
    pass


_ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef
):
    pass


_ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef
):
    pass


_ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef
):
    pass


_ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef
):
    pass


_ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef
):
    pass


_ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef
):
    pass


_ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef
):
    pass


_ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef
):
    pass


_ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": Literal[
            "int",
            "double",
            "literal",
            "text",
            "date",
            "latlon",
            "int-array",
            "double-array",
            "literal-array",
            "text-array",
            "date-array",
        ],
        "IntOptions": ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef,
        "DoubleOptions": ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef,
        "LiteralOptions": ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef,
        "TextOptions": ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef,
        "DateOptions": ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef,
        "LatLonOptions": ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef,
        "IntArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef,
        "DoubleArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef,
        "LiteralArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef,
        "TextArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef,
        "DateArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      Configuration information for a field in the index, including its name, type, and options. The
      supported options depend on the `` IndexFieldType`` .
      - **IndexFieldName** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
        ends with a wildcard. Any document fields that don't map to a regular index field but do
        match a dynamic field's pattern are configured with the dynamic field's indexing options.
        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
        (*). The wildcard can also be the only character in a dynamic field name. Multiple
        wildcards, and wildcards embedded within a string are not supported.
        The name ``score`` is reserved and cannot be used as a field name. To reference a document's
        ID, you can use the name ``_id`` .
    """


_ClientDefineIndexFieldResponseIndexFieldStatusTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldStatusTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldStatusTypeDef
):
    pass


_ClientDefineIndexFieldResponseIndexFieldTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseIndexFieldTypeDef",
    {
        "Options": ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef,
        "Status": ClientDefineIndexFieldResponseIndexFieldStatusTypeDef,
    },
    total=False,
)


class ClientDefineIndexFieldResponseIndexFieldTypeDef(
    _ClientDefineIndexFieldResponseIndexFieldTypeDef
):
    """
    - **IndexField** *(dict) --*

      The value of an ``IndexField`` and its current status.
      - **Options** *(dict) --*

        Configuration information for a field in the index, including its name, type, and options.
        The supported options depend on the `` IndexFieldType`` .
        - **IndexFieldName** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
          ends with a wildcard. Any document fields that don't map to a regular index field but do
          match a dynamic field's pattern are configured with the dynamic field's indexing options.
          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.
          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .
    """


_ClientDefineIndexFieldResponseTypeDef = TypedDict(
    "_ClientDefineIndexFieldResponseTypeDef",
    {"IndexField": ClientDefineIndexFieldResponseIndexFieldTypeDef},
    total=False,
)


class ClientDefineIndexFieldResponseTypeDef(_ClientDefineIndexFieldResponseTypeDef):
    """
    - *(dict) --*

      The result of a `` DefineIndexField`` request. Contains the status of the newly-configured
      index field.
      - **IndexField** *(dict) --*

        The value of an ``IndexField`` and its current status.
        - **Options** *(dict) --*

          Configuration information for a field in the index, including its name, type, and options.
          The supported options depend on the `` IndexFieldType`` .
          - **IndexFieldName** *(string) --*

            A string that represents the name of an index field. CloudSearch supports regular index
            fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
            or ends with a wildcard. Any document fields that don't map to a regular index field but
            do match a dynamic field's pattern are configured with the dynamic field's indexing
            options.
            Regular field names begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
            wildcard (*). The wildcard can also be the only character in a dynamic field name.
            Multiple wildcards, and wildcards embedded within a string are not supported.
            The name ``score`` is reserved and cannot be used as a field name. To reference a
            document's ID, you can use the name ``_id`` .
    """


_ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef = TypedDict(
    "_ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef",
    {"SourceField": str, "FuzzyMatching": Literal["none", "low", "high"], "SortExpression": str},
    total=False,
)


class ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef(
    _ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef
):
    pass


_ClientDefineSuggesterResponseSuggesterOptionsTypeDef = TypedDict(
    "_ClientDefineSuggesterResponseSuggesterOptionsTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef,
    },
    total=False,
)


class ClientDefineSuggesterResponseSuggesterOptionsTypeDef(
    _ClientDefineSuggesterResponseSuggesterOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      Configuration information for a search suggester. Each suggester has a unique name and
      specifies the text field you want to use for suggestions. The following options can be
      configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .
      - **SuggesterName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).
    """


_ClientDefineSuggesterResponseSuggesterStatusTypeDef = TypedDict(
    "_ClientDefineSuggesterResponseSuggesterStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDefineSuggesterResponseSuggesterStatusTypeDef(
    _ClientDefineSuggesterResponseSuggesterStatusTypeDef
):
    pass


_ClientDefineSuggesterResponseSuggesterTypeDef = TypedDict(
    "_ClientDefineSuggesterResponseSuggesterTypeDef",
    {
        "Options": ClientDefineSuggesterResponseSuggesterOptionsTypeDef,
        "Status": ClientDefineSuggesterResponseSuggesterStatusTypeDef,
    },
    total=False,
)


class ClientDefineSuggesterResponseSuggesterTypeDef(_ClientDefineSuggesterResponseSuggesterTypeDef):
    """
    - **Suggester** *(dict) --*

      The value of a ``Suggester`` and its current status.
      - **Options** *(dict) --*

        Configuration information for a search suggester. Each suggester has a unique name and
        specifies the text field you want to use for suggestions. The following options can be
        configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .
        - **SuggesterName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).
    """


_ClientDefineSuggesterResponseTypeDef = TypedDict(
    "_ClientDefineSuggesterResponseTypeDef",
    {"Suggester": ClientDefineSuggesterResponseSuggesterTypeDef},
    total=False,
)


class ClientDefineSuggesterResponseTypeDef(_ClientDefineSuggesterResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``DefineSuggester`` request. Contains the status of the newly-configured
      suggester.
      - **Suggester** *(dict) --*

        The value of a ``Suggester`` and its current status.
        - **Options** *(dict) --*

          Configuration information for a search suggester. Each suggester has a unique name and
          specifies the text field you want to use for suggestions. The following options can be
          configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .
          - **SuggesterName** *(string) --*

            Names must begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore).
    """


_ClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef = TypedDict(
    "_ClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef",
    {"SourceField": str, "FuzzyMatching": Literal["none", "low", "high"], "SortExpression": str},
    total=False,
)


class ClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef(
    _ClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef
):
    pass


_RequiredClientDefineSuggesterSuggesterTypeDef = TypedDict(
    "_RequiredClientDefineSuggesterSuggesterTypeDef", {"SuggesterName": str}
)
_OptionalClientDefineSuggesterSuggesterTypeDef = TypedDict(
    "_OptionalClientDefineSuggesterSuggesterTypeDef",
    {"DocumentSuggesterOptions": ClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef},
    total=False,
)


class ClientDefineSuggesterSuggesterTypeDef(
    _RequiredClientDefineSuggesterSuggesterTypeDef, _OptionalClientDefineSuggesterSuggesterTypeDef
):
    """
    Configuration information for a search suggester. Each suggester has a unique name and specifies
    the text field you want to use for suggestions. The following options can be configured for a
    suggester: ``FuzzyMatching`` , ``SortExpression`` .
    - **SuggesterName** *(string) --***[REQUIRED]**

      Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9,
      and _ (underscore).
    """


_ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef = TypedDict(
    "_ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": Literal["none", "minimal", "light", "full"],
    },
    total=False,
)


class ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef(
    _ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef
):
    pass


_ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef = TypedDict(
    "_ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": Literal[
            "ar",
            "bg",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "eu",
            "fa",
            "fi",
            "fr",
            "ga",
            "gl",
            "he",
            "hi",
            "hu",
            "hy",
            "id",
            "it",
            "ja",
            "ko",
            "lv",
            "mul",
            "nl",
            "no",
            "pt",
            "ro",
            "ru",
            "sv",
            "th",
            "tr",
            "zh-Hans",
            "zh-Hant",
        ],
        "AnalysisOptions": ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef,
    },
    total=False,
)


class ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef(
    _ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      Configuration information for an analysis scheme. Each analysis scheme has a unique name and
      specifies the language of the text to be processed. The following options can be configured
      for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
      ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .
      - **AnalysisSchemeName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).
    """


_ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef = TypedDict(
    "_ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef(
    _ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef
):
    pass


_ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef = TypedDict(
    "_ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef",
    {
        "Options": ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef,
        "Status": ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef,
    },
    total=False,
)


class ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef(
    _ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef
):
    """
    - **AnalysisScheme** *(dict) --*

      The status of the analysis scheme being deleted.
      - **Options** *(dict) --*

        Configuration information for an analysis scheme. Each analysis scheme has a unique name and
        specifies the language of the text to be processed. The following options can be configured
        for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
        ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .
        - **AnalysisSchemeName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).
    """


_ClientDeleteAnalysisSchemeResponseTypeDef = TypedDict(
    "_ClientDeleteAnalysisSchemeResponseTypeDef",
    {"AnalysisScheme": ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef},
    total=False,
)


class ClientDeleteAnalysisSchemeResponseTypeDef(_ClientDeleteAnalysisSchemeResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``DeleteAnalysisScheme`` request. Contains the status of the deleted analysis
      scheme.
      - **AnalysisScheme** *(dict) --*

        The status of the analysis scheme being deleted.
        - **Options** *(dict) --*

          Configuration information for an analysis scheme. Each analysis scheme has a unique name
          and specifies the language of the text to be processed. The following options can be
          configured for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
          ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .
          - **AnalysisSchemeName** *(string) --*

            Names must begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore).
    """


_ClientDeleteDomainResponseDomainStatusDocServiceTypeDef = TypedDict(
    "_ClientDeleteDomainResponseDomainStatusDocServiceTypeDef", {"Endpoint": str}, total=False
)


class ClientDeleteDomainResponseDomainStatusDocServiceTypeDef(
    _ClientDeleteDomainResponseDomainStatusDocServiceTypeDef
):
    pass


_ClientDeleteDomainResponseDomainStatusLimitsTypeDef = TypedDict(
    "_ClientDeleteDomainResponseDomainStatusLimitsTypeDef",
    {"MaximumReplicationCount": int, "MaximumPartitionCount": int},
    total=False,
)


class ClientDeleteDomainResponseDomainStatusLimitsTypeDef(
    _ClientDeleteDomainResponseDomainStatusLimitsTypeDef
):
    pass


_ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef = TypedDict(
    "_ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef", {"Endpoint": str}, total=False
)


class ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef(
    _ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef
):
    pass


_ClientDeleteDomainResponseDomainStatusTypeDef = TypedDict(
    "_ClientDeleteDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "DocService": ClientDeleteDomainResponseDomainStatusDocServiceTypeDef,
        "SearchService": ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef,
        "RequiresIndexDocuments": bool,
        "Processing": bool,
        "SearchInstanceType": str,
        "SearchPartitionCount": int,
        "SearchInstanceCount": int,
        "Limits": ClientDeleteDomainResponseDomainStatusLimitsTypeDef,
    },
    total=False,
)


class ClientDeleteDomainResponseDomainStatusTypeDef(_ClientDeleteDomainResponseDomainStatusTypeDef):
    """
    - **DomainStatus** *(dict) --*

      The current status of the search domain.
      - **DomainId** *(string) --*

        An internally generated unique identifier for a domain.
    """


_ClientDeleteDomainResponseTypeDef = TypedDict(
    "_ClientDeleteDomainResponseTypeDef",
    {"DomainStatus": ClientDeleteDomainResponseDomainStatusTypeDef},
    total=False,
)


class ClientDeleteDomainResponseTypeDef(_ClientDeleteDomainResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``DeleteDomain`` request. Contains the status of a newly deleted domain, or no
      status if the domain has already been completely deleted.
      - **DomainStatus** *(dict) --*

        The current status of the search domain.
        - **DomainId** *(string) --*

          An internally generated unique identifier for a domain.
    """


_ClientDeleteExpressionResponseExpressionOptionsTypeDef = TypedDict(
    "_ClientDeleteExpressionResponseExpressionOptionsTypeDef",
    {"ExpressionName": str, "ExpressionValue": str},
    total=False,
)


class ClientDeleteExpressionResponseExpressionOptionsTypeDef(
    _ClientDeleteExpressionResponseExpressionOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      The expression that is evaluated for sorting while processing a search request.
      - **ExpressionName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).
    """


_ClientDeleteExpressionResponseExpressionStatusTypeDef = TypedDict(
    "_ClientDeleteExpressionResponseExpressionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDeleteExpressionResponseExpressionStatusTypeDef(
    _ClientDeleteExpressionResponseExpressionStatusTypeDef
):
    pass


_ClientDeleteExpressionResponseExpressionTypeDef = TypedDict(
    "_ClientDeleteExpressionResponseExpressionTypeDef",
    {
        "Options": ClientDeleteExpressionResponseExpressionOptionsTypeDef,
        "Status": ClientDeleteExpressionResponseExpressionStatusTypeDef,
    },
    total=False,
)


class ClientDeleteExpressionResponseExpressionTypeDef(
    _ClientDeleteExpressionResponseExpressionTypeDef
):
    """
    - **Expression** *(dict) --*

      The status of the expression being deleted.
      - **Options** *(dict) --*

        The expression that is evaluated for sorting while processing a search request.
        - **ExpressionName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).
    """


_ClientDeleteExpressionResponseTypeDef = TypedDict(
    "_ClientDeleteExpressionResponseTypeDef",
    {"Expression": ClientDeleteExpressionResponseExpressionTypeDef},
    total=False,
)


class ClientDeleteExpressionResponseTypeDef(_ClientDeleteExpressionResponseTypeDef):
    """
    - *(dict) --*

      The result of a `` DeleteExpression`` request. Specifies the expression being deleted.
      - **Expression** *(dict) --*

        The status of the expression being deleted.
        - **Options** *(dict) --*

          The expression that is evaluated for sorting while processing a search request.
          - **ExpressionName** *(string) --*

            Names must begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore).
    """


_ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef
):
    pass


_ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef
):
    pass


_ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef
):
    pass


_ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef
):
    pass


_ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef
):
    pass


_ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef
):
    pass


_ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef
):
    pass


_ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef
):
    pass


_ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef
):
    pass


_ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef
):
    pass


_ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef
):
    pass


_ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": Literal[
            "int",
            "double",
            "literal",
            "text",
            "date",
            "latlon",
            "int-array",
            "double-array",
            "literal-array",
            "text-array",
            "date-array",
        ],
        "IntOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef,
        "DoubleOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef,
        "LiteralOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef,
        "TextOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef,
        "DateOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef,
        "LatLonOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef,
        "IntArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef,
        "DoubleArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef,
        "LiteralArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef,
        "TextArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef,
        "DateArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      Configuration information for a field in the index, including its name, type, and options. The
      supported options depend on the `` IndexFieldType`` .
      - **IndexFieldName** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
        ends with a wildcard. Any document fields that don't map to a regular index field but do
        match a dynamic field's pattern are configured with the dynamic field's indexing options.
        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
        (*). The wildcard can also be the only character in a dynamic field name. Multiple
        wildcards, and wildcards embedded within a string are not supported.
        The name ``score`` is reserved and cannot be used as a field name. To reference a document's
        ID, you can use the name ``_id`` .
    """


_ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef
):
    pass


_ClientDeleteIndexFieldResponseIndexFieldTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseIndexFieldTypeDef",
    {
        "Options": ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef,
        "Status": ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef,
    },
    total=False,
)


class ClientDeleteIndexFieldResponseIndexFieldTypeDef(
    _ClientDeleteIndexFieldResponseIndexFieldTypeDef
):
    """
    - **IndexField** *(dict) --*

      The status of the index field being deleted.
      - **Options** *(dict) --*

        Configuration information for a field in the index, including its name, type, and options.
        The supported options depend on the `` IndexFieldType`` .
        - **IndexFieldName** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
          ends with a wildcard. Any document fields that don't map to a regular index field but do
          match a dynamic field's pattern are configured with the dynamic field's indexing options.
          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.
          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .
    """


_ClientDeleteIndexFieldResponseTypeDef = TypedDict(
    "_ClientDeleteIndexFieldResponseTypeDef",
    {"IndexField": ClientDeleteIndexFieldResponseIndexFieldTypeDef},
    total=False,
)


class ClientDeleteIndexFieldResponseTypeDef(_ClientDeleteIndexFieldResponseTypeDef):
    """
    - *(dict) --*

      The result of a `` DeleteIndexField`` request.
      - **IndexField** *(dict) --*

        The status of the index field being deleted.
        - **Options** *(dict) --*

          Configuration information for a field in the index, including its name, type, and options.
          The supported options depend on the `` IndexFieldType`` .
          - **IndexFieldName** *(string) --*

            A string that represents the name of an index field. CloudSearch supports regular index
            fields as well as dynamic fields. A dynamic field's name defines a pattern that begins
            or ends with a wildcard. Any document fields that don't map to a regular index field but
            do match a dynamic field's pattern are configured with the dynamic field's indexing
            options.
            Regular field names begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
            wildcard (*). The wildcard can also be the only character in a dynamic field name.
            Multiple wildcards, and wildcards embedded within a string are not supported.
            The name ``score`` is reserved and cannot be used as a field name. To reference a
            document's ID, you can use the name ``_id`` .
    """


_ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef = TypedDict(
    "_ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef",
    {"SourceField": str, "FuzzyMatching": Literal["none", "low", "high"], "SortExpression": str},
    total=False,
)


class ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef(
    _ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef
):
    pass


_ClientDeleteSuggesterResponseSuggesterOptionsTypeDef = TypedDict(
    "_ClientDeleteSuggesterResponseSuggesterOptionsTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef,
    },
    total=False,
)


class ClientDeleteSuggesterResponseSuggesterOptionsTypeDef(
    _ClientDeleteSuggesterResponseSuggesterOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      Configuration information for a search suggester. Each suggester has a unique name and
      specifies the text field you want to use for suggestions. The following options can be
      configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .
      - **SuggesterName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).
    """


_ClientDeleteSuggesterResponseSuggesterStatusTypeDef = TypedDict(
    "_ClientDeleteSuggesterResponseSuggesterStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDeleteSuggesterResponseSuggesterStatusTypeDef(
    _ClientDeleteSuggesterResponseSuggesterStatusTypeDef
):
    pass


_ClientDeleteSuggesterResponseSuggesterTypeDef = TypedDict(
    "_ClientDeleteSuggesterResponseSuggesterTypeDef",
    {
        "Options": ClientDeleteSuggesterResponseSuggesterOptionsTypeDef,
        "Status": ClientDeleteSuggesterResponseSuggesterStatusTypeDef,
    },
    total=False,
)


class ClientDeleteSuggesterResponseSuggesterTypeDef(_ClientDeleteSuggesterResponseSuggesterTypeDef):
    """
    - **Suggester** *(dict) --*

      The status of the suggester being deleted.
      - **Options** *(dict) --*

        Configuration information for a search suggester. Each suggester has a unique name and
        specifies the text field you want to use for suggestions. The following options can be
        configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .
        - **SuggesterName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).
    """


_ClientDeleteSuggesterResponseTypeDef = TypedDict(
    "_ClientDeleteSuggesterResponseTypeDef",
    {"Suggester": ClientDeleteSuggesterResponseSuggesterTypeDef},
    total=False,
)


class ClientDeleteSuggesterResponseTypeDef(_ClientDeleteSuggesterResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``DeleteSuggester`` request. Contains the status of the deleted suggester.
      - **Suggester** *(dict) --*

        The status of the suggester being deleted.
        - **Options** *(dict) --*

          Configuration information for a search suggester. Each suggester has a unique name and
          specifies the text field you want to use for suggestions. The following options can be
          configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .
          - **SuggesterName** *(string) --*

            Names must begin with a letter and can contain the following characters: a-z
            (lowercase), 0-9, and _ (underscore).
    """


_ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef = TypedDict(
    "_ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": Literal["none", "minimal", "light", "full"],
    },
    total=False,
)


class ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef(
    _ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef
):
    pass


_ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef = TypedDict(
    "_ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": Literal[
            "ar",
            "bg",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "eu",
            "fa",
            "fi",
            "fr",
            "ga",
            "gl",
            "he",
            "hi",
            "hu",
            "hy",
            "id",
            "it",
            "ja",
            "ko",
            "lv",
            "mul",
            "nl",
            "no",
            "pt",
            "ro",
            "ru",
            "sv",
            "th",
            "tr",
            "zh-Hans",
            "zh-Hant",
        ],
        "AnalysisOptions": ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef(
    _ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      Configuration information for an analysis scheme. Each analysis scheme has a unique name and
      specifies the language of the text to be processed. The following options can be configured
      for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
      ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .
      - **AnalysisSchemeName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).
    """


_ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef = TypedDict(
    "_ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef(
    _ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef
):
    pass


_ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef = TypedDict(
    "_ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef",
    {
        "Options": ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef,
        "Status": ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef,
    },
    total=False,
)


class ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef(
    _ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef
):
    """
    - *(dict) --*

      The status and configuration of an ``AnalysisScheme`` .
      - **Options** *(dict) --*

        Configuration information for an analysis scheme. Each analysis scheme has a unique name and
        specifies the language of the text to be processed. The following options can be configured
        for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary`` ,
        ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .
        - **AnalysisSchemeName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).
    """


_ClientDescribeAnalysisSchemesResponseTypeDef = TypedDict(
    "_ClientDescribeAnalysisSchemesResponseTypeDef",
    {"AnalysisSchemes": List[ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef]},
    total=False,
)


class ClientDescribeAnalysisSchemesResponseTypeDef(_ClientDescribeAnalysisSchemesResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``DescribeAnalysisSchemes`` request. Contains the analysis schemes configured
      for the domain specified in the request.
      - **AnalysisSchemes** *(list) --*

        The analysis scheme descriptions.
        - *(dict) --*

          The status and configuration of an ``AnalysisScheme`` .
          - **Options** *(dict) --*

            Configuration information for an analysis scheme. Each analysis scheme has a unique name
            and specifies the language of the text to be processed. The following options can be
            configured for an analysis scheme: ``Synonyms`` , ``Stopwords`` , ``StemmingDictionary``
            , ``JapaneseTokenizationDictionary`` and ``AlgorithmicStemming`` .
            - **AnalysisSchemeName** *(string) --*

              Names must begin with a letter and can contain the following characters: a-z
              (lowercase), 0-9, and _ (underscore).
    """


_ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef(
    _ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef
):
    pass


_ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef = TypedDict(
    "_ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef",
    {
        "Options": bool,
        "Status": ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef(
    _ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef
):
    """
    - **AvailabilityOptions** *(dict) --*

      The availability options configured for the domain. Indicates whether Multi-AZ is enabled for
      the domain.
      - **Options** *(boolean) --*

        The availability options configured for the domain.
    """


_ClientDescribeAvailabilityOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeAvailabilityOptionsResponseTypeDef",
    {"AvailabilityOptions": ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef},
    total=False,
)


class ClientDescribeAvailabilityOptionsResponseTypeDef(
    _ClientDescribeAvailabilityOptionsResponseTypeDef
):
    """
    - *(dict) --*

      The result of a ``DescribeAvailabilityOptions`` request. Indicates whether or not the Multi-AZ
      option is enabled for the domain specified in the request.
      - **AvailabilityOptions** *(dict) --*

        The availability options configured for the domain. Indicates whether Multi-AZ is enabled
        for the domain.
        - **Options** *(boolean) --*

          The availability options configured for the domain.
    """


_ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)


class ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef(
    _ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      The domain endpoint options configured for the domain.
      - **EnforceHTTPS** *(boolean) --*

        Whether the domain is HTTPS only enabled.
    """


_ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef(
    _ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef
):
    pass


_ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef",
    {
        "Options": ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef,
        "Status": ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef(
    _ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef
):
    """
    - **DomainEndpointOptions** *(dict) --*

      The status and configuration of a search domain's endpoint options.
      - **Options** *(dict) --*

        The domain endpoint options configured for the domain.
        - **EnforceHTTPS** *(boolean) --*

          Whether the domain is HTTPS only enabled.
    """


_ClientDescribeDomainEndpointOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef
    },
    total=False,
)


class ClientDescribeDomainEndpointOptionsResponseTypeDef(
    _ClientDescribeDomainEndpointOptionsResponseTypeDef
):
    """
    - *(dict) --*

      The result of a ``DescribeDomainEndpointOptions`` request. Contains the status and
      configuration of a search domain's endpoint options.
      - **DomainEndpointOptions** *(dict) --*

        The status and configuration of a search domain's endpoint options.
        - **Options** *(dict) --*

          The domain endpoint options configured for the domain.
          - **EnforceHTTPS** *(boolean) --*

            Whether the domain is HTTPS only enabled.
    """


_ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef = TypedDict(
    "_ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef",
    {"Endpoint": str},
    total=False,
)


class ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef(
    _ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef
):
    pass


_ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef = TypedDict(
    "_ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef",
    {"MaximumReplicationCount": int, "MaximumPartitionCount": int},
    total=False,
)


class ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef(
    _ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef
):
    pass


_ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef = TypedDict(
    "_ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef",
    {"Endpoint": str},
    total=False,
)


class ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef(
    _ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef
):
    pass


_ClientDescribeDomainsResponseDomainStatusListTypeDef = TypedDict(
    "_ClientDescribeDomainsResponseDomainStatusListTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "DocService": ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef,
        "SearchService": ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef,
        "RequiresIndexDocuments": bool,
        "Processing": bool,
        "SearchInstanceType": str,
        "SearchPartitionCount": int,
        "SearchInstanceCount": int,
        "Limits": ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef,
    },
    total=False,
)


class ClientDescribeDomainsResponseDomainStatusListTypeDef(
    _ClientDescribeDomainsResponseDomainStatusListTypeDef
):
    """
    - *(dict) --*

      The current status of the search domain.
      - **DomainId** *(string) --*

        An internally generated unique identifier for a domain.
    """


_ClientDescribeDomainsResponseTypeDef = TypedDict(
    "_ClientDescribeDomainsResponseTypeDef",
    {"DomainStatusList": List[ClientDescribeDomainsResponseDomainStatusListTypeDef]},
    total=False,
)


class ClientDescribeDomainsResponseTypeDef(_ClientDescribeDomainsResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``DescribeDomains`` request. Contains the status of the domains specified in
      the request or all domains owned by the account.
      - **DomainStatusList** *(list) --*

        A list that contains the status of each requested domain.
        - *(dict) --*

          The current status of the search domain.
          - **DomainId** *(string) --*

            An internally generated unique identifier for a domain.
    """


_ClientDescribeExpressionsResponseExpressionsOptionsTypeDef = TypedDict(
    "_ClientDescribeExpressionsResponseExpressionsOptionsTypeDef",
    {"ExpressionName": str, "ExpressionValue": str},
    total=False,
)


class ClientDescribeExpressionsResponseExpressionsOptionsTypeDef(
    _ClientDescribeExpressionsResponseExpressionsOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      The expression that is evaluated for sorting while processing a search request.
      - **ExpressionName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).
    """


_ClientDescribeExpressionsResponseExpressionsStatusTypeDef = TypedDict(
    "_ClientDescribeExpressionsResponseExpressionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeExpressionsResponseExpressionsStatusTypeDef(
    _ClientDescribeExpressionsResponseExpressionsStatusTypeDef
):
    pass


_ClientDescribeExpressionsResponseExpressionsTypeDef = TypedDict(
    "_ClientDescribeExpressionsResponseExpressionsTypeDef",
    {
        "Options": ClientDescribeExpressionsResponseExpressionsOptionsTypeDef,
        "Status": ClientDescribeExpressionsResponseExpressionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeExpressionsResponseExpressionsTypeDef(
    _ClientDescribeExpressionsResponseExpressionsTypeDef
):
    """
    - *(dict) --*

      The value of an ``Expression`` and its current status.
      - **Options** *(dict) --*

        The expression that is evaluated for sorting while processing a search request.
        - **ExpressionName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).
    """


_ClientDescribeExpressionsResponseTypeDef = TypedDict(
    "_ClientDescribeExpressionsResponseTypeDef",
    {"Expressions": List[ClientDescribeExpressionsResponseExpressionsTypeDef]},
    total=False,
)


class ClientDescribeExpressionsResponseTypeDef(_ClientDescribeExpressionsResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``DescribeExpressions`` request. Contains the expressions configured for the
      domain specified in the request.
      - **Expressions** *(list) --*

        The expressions configured for the domain.
        - *(dict) --*

          The value of an ``Expression`` and its current status.
          - **Options** *(dict) --*

            The expression that is evaluated for sorting while processing a search request.
            - **ExpressionName** *(string) --*

              Names must begin with a letter and can contain the following characters: a-z
              (lowercase), 0-9, and _ (underscore).
    """


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef
):
    pass


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef
):
    pass


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef
):
    pass


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef
):
    pass


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef
):
    pass


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef
):
    pass


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef
):
    pass


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef
):
    pass


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef
):
    pass


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef
):
    pass


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef
):
    pass


_ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": Literal[
            "int",
            "double",
            "literal",
            "text",
            "date",
            "latlon",
            "int-array",
            "double-array",
            "literal-array",
            "text-array",
            "date-array",
        ],
        "IntOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef,
        "DoubleOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef,
        "LiteralOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef,
        "TextOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef,
        "DateOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef,
        "LatLonOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef,
        "IntArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef,
        "DoubleArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef,
        "LiteralArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef,
        "TextArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef,
        "DateArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      Configuration information for a field in the index, including its name, type, and options. The
      supported options depend on the `` IndexFieldType`` .
      - **IndexFieldName** *(string) --*

        A string that represents the name of an index field. CloudSearch supports regular index
        fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
        ends with a wildcard. Any document fields that don't map to a regular index field but do
        match a dynamic field's pattern are configured with the dynamic field's indexing options.
        Regular field names begin with a letter and can contain the following characters: a-z
        (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard
        (*). The wildcard can also be the only character in a dynamic field name. Multiple
        wildcards, and wildcards embedded within a string are not supported.
        The name ``score`` is reserved and cannot be used as a field name. To reference a document's
        ID, you can use the name ``_id`` .
    """


_ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef
):
    pass


_ClientDescribeIndexFieldsResponseIndexFieldsTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseIndexFieldsTypeDef",
    {
        "Options": ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef,
        "Status": ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeIndexFieldsResponseIndexFieldsTypeDef(
    _ClientDescribeIndexFieldsResponseIndexFieldsTypeDef
):
    """
    - *(dict) --*

      The value of an ``IndexField`` and its current status.
      - **Options** *(dict) --*

        Configuration information for a field in the index, including its name, type, and options.
        The supported options depend on the `` IndexFieldType`` .
        - **IndexFieldName** *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
          ends with a wildcard. Any document fields that don't map to a regular index field but do
          match a dynamic field's pattern are configured with the dynamic field's indexing options.
          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.
          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .
    """


_ClientDescribeIndexFieldsResponseTypeDef = TypedDict(
    "_ClientDescribeIndexFieldsResponseTypeDef",
    {"IndexFields": List[ClientDescribeIndexFieldsResponseIndexFieldsTypeDef]},
    total=False,
)


class ClientDescribeIndexFieldsResponseTypeDef(_ClientDescribeIndexFieldsResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``DescribeIndexFields`` request. Contains the index fields configured for the
      domain specified in the request.
      - **IndexFields** *(list) --*

        The index fields configured for the domain.
        - *(dict) --*

          The value of an ``IndexField`` and its current status.
          - **Options** *(dict) --*

            Configuration information for a field in the index, including its name, type, and
            options. The supported options depend on the `` IndexFieldType`` .
            - **IndexFieldName** *(string) --*

              A string that represents the name of an index field. CloudSearch supports regular
              index fields as well as dynamic fields. A dynamic field's name defines a pattern that
              begins or ends with a wildcard. Any document fields that don't map to a regular index
              field but do match a dynamic field's pattern are configured with the dynamic field's
              indexing options.
              Regular field names begin with a letter and can contain the following characters: a-z
              (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
              wildcard (*). The wildcard can also be the only character in a dynamic field name.
              Multiple wildcards, and wildcards embedded within a string are not supported.
              The name ``score`` is reserved and cannot be used as a field name. To reference a
              document's ID, you can use the name ``_id`` .
    """


_ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef = TypedDict(
    "_ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef",
    {
        "DesiredInstanceType": Literal[
            "search.m1.small",
            "search.m1.large",
            "search.m2.xlarge",
            "search.m2.2xlarge",
            "search.m3.medium",
            "search.m3.large",
            "search.m3.xlarge",
            "search.m3.2xlarge",
        ],
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)


class ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef(
    _ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      The desired instance type and desired number of replicas of each index partition.
      - **DesiredInstanceType** *(string) --*

        The instance type that you want to preconfigure for your domain. For example,
        ``search.m1.small`` .
    """


_ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef = TypedDict(
    "_ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef(
    _ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef
):
    pass


_ClientDescribeScalingParametersResponseScalingParametersTypeDef = TypedDict(
    "_ClientDescribeScalingParametersResponseScalingParametersTypeDef",
    {
        "Options": ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef,
        "Status": ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef,
    },
    total=False,
)


class ClientDescribeScalingParametersResponseScalingParametersTypeDef(
    _ClientDescribeScalingParametersResponseScalingParametersTypeDef
):
    """
    - **ScalingParameters** *(dict) --*

      The status and configuration of a search domain's scaling parameters.
      - **Options** *(dict) --*

        The desired instance type and desired number of replicas of each index partition.
        - **DesiredInstanceType** *(string) --*

          The instance type that you want to preconfigure for your domain. For example,
          ``search.m1.small`` .
    """


_ClientDescribeScalingParametersResponseTypeDef = TypedDict(
    "_ClientDescribeScalingParametersResponseTypeDef",
    {"ScalingParameters": ClientDescribeScalingParametersResponseScalingParametersTypeDef},
    total=False,
)


class ClientDescribeScalingParametersResponseTypeDef(
    _ClientDescribeScalingParametersResponseTypeDef
):
    """
    - *(dict) --*

      The result of a ``DescribeScalingParameters`` request. Contains the scaling parameters
      configured for the domain specified in the request.
      - **ScalingParameters** *(dict) --*

        The status and configuration of a search domain's scaling parameters.
        - **Options** *(dict) --*

          The desired instance type and desired number of replicas of each index partition.
          - **DesiredInstanceType** *(string) --*

            The instance type that you want to preconfigure for your domain. For example,
            ``search.m1.small`` .
    """


_ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef = TypedDict(
    "_ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef(
    _ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef
):
    pass


_ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef = TypedDict(
    "_ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef",
    {
        "Options": str,
        "Status": ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef,
    },
    total=False,
)


class ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef(
    _ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef
):
    """
    - **AccessPolicies** *(dict) --*

      The access rules configured for the domain specified in the request.
      - **Options** *(string) --*

        Access rules for a domain's document or search service endpoints. For more information, see
        `Configuring Access for a Search Domain
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html>`__ in
        the *Amazon CloudSearch Developer Guide* . The maximum size of a policy document is 100 KB.
    """


_ClientDescribeServiceAccessPoliciesResponseTypeDef = TypedDict(
    "_ClientDescribeServiceAccessPoliciesResponseTypeDef",
    {"AccessPolicies": ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef},
    total=False,
)


class ClientDescribeServiceAccessPoliciesResponseTypeDef(
    _ClientDescribeServiceAccessPoliciesResponseTypeDef
):
    """
    - *(dict) --*

      The result of a ``DescribeServiceAccessPolicies`` request.
      - **AccessPolicies** *(dict) --*

        The access rules configured for the domain specified in the request.
        - **Options** *(string) --*

          Access rules for a domain's document or search service endpoints. For more information,
          see `Configuring Access for a Search Domain
          <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html>`__
          in the *Amazon CloudSearch Developer Guide* . The maximum size of a policy document is 100
          KB.
    """


_ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef = TypedDict(
    "_ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef",
    {"SourceField": str, "FuzzyMatching": Literal["none", "low", "high"], "SortExpression": str},
    total=False,
)


class ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef(
    _ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef
):
    pass


_ClientDescribeSuggestersResponseSuggestersOptionsTypeDef = TypedDict(
    "_ClientDescribeSuggestersResponseSuggestersOptionsTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeSuggestersResponseSuggestersOptionsTypeDef(
    _ClientDescribeSuggestersResponseSuggestersOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      Configuration information for a search suggester. Each suggester has a unique name and
      specifies the text field you want to use for suggestions. The following options can be
      configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .
      - **SuggesterName** *(string) --*

        Names must begin with a letter and can contain the following characters: a-z (lowercase),
        0-9, and _ (underscore).
    """


_ClientDescribeSuggestersResponseSuggestersStatusTypeDef = TypedDict(
    "_ClientDescribeSuggestersResponseSuggestersStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeSuggestersResponseSuggestersStatusTypeDef(
    _ClientDescribeSuggestersResponseSuggestersStatusTypeDef
):
    pass


_ClientDescribeSuggestersResponseSuggestersTypeDef = TypedDict(
    "_ClientDescribeSuggestersResponseSuggestersTypeDef",
    {
        "Options": ClientDescribeSuggestersResponseSuggestersOptionsTypeDef,
        "Status": ClientDescribeSuggestersResponseSuggestersStatusTypeDef,
    },
    total=False,
)


class ClientDescribeSuggestersResponseSuggestersTypeDef(
    _ClientDescribeSuggestersResponseSuggestersTypeDef
):
    """
    - *(dict) --*

      The value of a ``Suggester`` and its current status.
      - **Options** *(dict) --*

        Configuration information for a search suggester. Each suggester has a unique name and
        specifies the text field you want to use for suggestions. The following options can be
        configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .
        - **SuggesterName** *(string) --*

          Names must begin with a letter and can contain the following characters: a-z (lowercase),
          0-9, and _ (underscore).
    """


_ClientDescribeSuggestersResponseTypeDef = TypedDict(
    "_ClientDescribeSuggestersResponseTypeDef",
    {"Suggesters": List[ClientDescribeSuggestersResponseSuggestersTypeDef]},
    total=False,
)


class ClientDescribeSuggestersResponseTypeDef(_ClientDescribeSuggestersResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``DescribeSuggesters`` request.
      - **Suggesters** *(list) --*

        The suggesters configured for the domain specified in the request.
        - *(dict) --*

          The value of a ``Suggester`` and its current status.
          - **Options** *(dict) --*

            Configuration information for a search suggester. Each suggester has a unique name and
            specifies the text field you want to use for suggestions. The following options can be
            configured for a suggester: ``FuzzyMatching`` , ``SortExpression`` .
            - **SuggesterName** *(string) --*

              Names must begin with a letter and can contain the following characters: a-z
              (lowercase), 0-9, and _ (underscore).
    """


_ClientIndexDocumentsResponseTypeDef = TypedDict(
    "_ClientIndexDocumentsResponseTypeDef", {"FieldNames": List[str]}, total=False
)


class ClientIndexDocumentsResponseTypeDef(_ClientIndexDocumentsResponseTypeDef):
    """
    - *(dict) --*

      The result of an ``IndexDocuments`` request. Contains the status of the indexing operation,
      including the fields being indexed.
      - **FieldNames** *(list) --*

        The names of the fields that are currently being indexed.
        - *(string) --*

          A string that represents the name of an index field. CloudSearch supports regular index
          fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or
          ends with a wildcard. Any document fields that don't map to a regular index field but do
          match a dynamic field's pattern are configured with the dynamic field's indexing options.
          Regular field names begin with a letter and can contain the following characters: a-z
          (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a
          wildcard (*). The wildcard can also be the only character in a dynamic field name.
          Multiple wildcards, and wildcards embedded within a string are not supported.
          The name ``score`` is reserved and cannot be used as a field name. To reference a
          document's ID, you can use the name ``_id`` .
    """


_ClientListDomainNamesResponseTypeDef = TypedDict(
    "_ClientListDomainNamesResponseTypeDef", {"DomainNames": Dict[str, str]}, total=False
)


class ClientListDomainNamesResponseTypeDef(_ClientListDomainNamesResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``ListDomainNames`` request. Contains a list of the domains owned by an
      account.
      - **DomainNames** *(dict) --*

        The names of the search domains owned by an account.
        - *(string) --*

          A string that represents the name of a domain. Domain names are unique across the domains
          owned by an account within an AWS region. Domain names start with a letter or number and
          can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
          - *(string) --*

            The Amazon CloudSearch API version for a domain: 2011-02-01 or 2013-01-01.
    """


_ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef(
    _ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef
):
    pass


_ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef = TypedDict(
    "_ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef",
    {
        "Options": bool,
        "Status": ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef(
    _ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef
):
    """
    - **AvailabilityOptions** *(dict) --*

      The newly-configured availability options. Indicates whether Multi-AZ is enabled for the
      domain.
      - **Options** *(boolean) --*

        The availability options configured for the domain.
    """


_ClientUpdateAvailabilityOptionsResponseTypeDef = TypedDict(
    "_ClientUpdateAvailabilityOptionsResponseTypeDef",
    {"AvailabilityOptions": ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef},
    total=False,
)


class ClientUpdateAvailabilityOptionsResponseTypeDef(
    _ClientUpdateAvailabilityOptionsResponseTypeDef
):
    """
    - *(dict) --*

      The result of a ``UpdateAvailabilityOptions`` request. Contains the status of the domain's
      availability options.
      - **AvailabilityOptions** *(dict) --*

        The newly-configured availability options. Indicates whether Multi-AZ is enabled for the
        domain.
        - **Options** *(boolean) --*

          The availability options configured for the domain.
    """


_ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)


class ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef(
    _ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef
):
    """
    Whether to require that all requests to the domain arrive over HTTPS. We recommend
    Policy-Min-TLS-1-2-2019-07 for TLSSecurityPolicy. For compatibility with older clients, the
    default is Policy-Min-TLS-1-0-2019-07.
    - **EnforceHTTPS** *(boolean) --*

      Whether the domain is HTTPS only enabled.
    """


_ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)


class ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef(
    _ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      The domain endpoint options configured for the domain.
      - **EnforceHTTPS** *(boolean) --*

        Whether the domain is HTTPS only enabled.
    """


_ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef(
    _ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef
):
    pass


_ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef",
    {
        "Options": ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef,
        "Status": ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef(
    _ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef
):
    """
    - **DomainEndpointOptions** *(dict) --*

      The newly-configured domain endpoint options.
      - **Options** *(dict) --*

        The domain endpoint options configured for the domain.
        - **EnforceHTTPS** *(boolean) --*

          Whether the domain is HTTPS only enabled.
    """


_ClientUpdateDomainEndpointOptionsResponseTypeDef = TypedDict(
    "_ClientUpdateDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef
    },
    total=False,
)


class ClientUpdateDomainEndpointOptionsResponseTypeDef(
    _ClientUpdateDomainEndpointOptionsResponseTypeDef
):
    """
    - *(dict) --*

      The result of a ``UpdateDomainEndpointOptions`` request. Contains the configuration and status
      of the domain's endpoint options.
      - **DomainEndpointOptions** *(dict) --*

        The newly-configured domain endpoint options.
        - **Options** *(dict) --*

          The domain endpoint options configured for the domain.
          - **EnforceHTTPS** *(boolean) --*

            Whether the domain is HTTPS only enabled.
    """


_ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef = TypedDict(
    "_ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef",
    {
        "DesiredInstanceType": Literal[
            "search.m1.small",
            "search.m1.large",
            "search.m2.xlarge",
            "search.m2.2xlarge",
            "search.m3.medium",
            "search.m3.large",
            "search.m3.xlarge",
            "search.m3.2xlarge",
        ],
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)


class ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef(
    _ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef
):
    """
    - **Options** *(dict) --*

      The desired instance type and desired number of replicas of each index partition.
      - **DesiredInstanceType** *(string) --*

        The instance type that you want to preconfigure for your domain. For example,
        ``search.m1.small`` .
    """


_ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef = TypedDict(
    "_ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef(
    _ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef
):
    pass


_ClientUpdateScalingParametersResponseScalingParametersTypeDef = TypedDict(
    "_ClientUpdateScalingParametersResponseScalingParametersTypeDef",
    {
        "Options": ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef,
        "Status": ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef,
    },
    total=False,
)


class ClientUpdateScalingParametersResponseScalingParametersTypeDef(
    _ClientUpdateScalingParametersResponseScalingParametersTypeDef
):
    """
    - **ScalingParameters** *(dict) --*

      The status and configuration of a search domain's scaling parameters.
      - **Options** *(dict) --*

        The desired instance type and desired number of replicas of each index partition.
        - **DesiredInstanceType** *(string) --*

          The instance type that you want to preconfigure for your domain. For example,
          ``search.m1.small`` .
    """


_ClientUpdateScalingParametersResponseTypeDef = TypedDict(
    "_ClientUpdateScalingParametersResponseTypeDef",
    {"ScalingParameters": ClientUpdateScalingParametersResponseScalingParametersTypeDef},
    total=False,
)


class ClientUpdateScalingParametersResponseTypeDef(_ClientUpdateScalingParametersResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``UpdateScalingParameters`` request. Contains the status of the
      newly-configured scaling parameters.
      - **ScalingParameters** *(dict) --*

        The status and configuration of a search domain's scaling parameters.
        - **Options** *(dict) --*

          The desired instance type and desired number of replicas of each index partition.
          - **DesiredInstanceType** *(string) --*

            The instance type that you want to preconfigure for your domain. For example,
            ``search.m1.small`` .
    """


_ClientUpdateScalingParametersScalingParametersTypeDef = TypedDict(
    "_ClientUpdateScalingParametersScalingParametersTypeDef",
    {
        "DesiredInstanceType": Literal[
            "search.m1.small",
            "search.m1.large",
            "search.m2.xlarge",
            "search.m2.2xlarge",
            "search.m3.medium",
            "search.m3.large",
            "search.m3.xlarge",
            "search.m3.2xlarge",
        ],
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)


class ClientUpdateScalingParametersScalingParametersTypeDef(
    _ClientUpdateScalingParametersScalingParametersTypeDef
):
    """
    The desired instance type and desired number of replicas of each index partition.
    - **DesiredInstanceType** *(string) --*

      The instance type that you want to preconfigure for your domain. For example,
      ``search.m1.small`` .
    """


_ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef = TypedDict(
    "_ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef(
    _ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef
):
    pass


_ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef = TypedDict(
    "_ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef",
    {
        "Options": str,
        "Status": ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef,
    },
    total=False,
)


class ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef(
    _ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef
):
    """
    - **AccessPolicies** *(dict) --*

      The access rules configured for the domain.
      - **Options** *(string) --*

        Access rules for a domain's document or search service endpoints. For more information, see
        `Configuring Access for a Search Domain
        <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html>`__ in
        the *Amazon CloudSearch Developer Guide* . The maximum size of a policy document is 100 KB.
    """


_ClientUpdateServiceAccessPoliciesResponseTypeDef = TypedDict(
    "_ClientUpdateServiceAccessPoliciesResponseTypeDef",
    {"AccessPolicies": ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef},
    total=False,
)


class ClientUpdateServiceAccessPoliciesResponseTypeDef(
    _ClientUpdateServiceAccessPoliciesResponseTypeDef
):
    """
    - *(dict) --*

      The result of an ``UpdateServiceAccessPolicies`` request. Contains the new access policies.
      - **AccessPolicies** *(dict) --*

        The access rules configured for the domain.
        - **Options** *(string) --*

          Access rules for a domain's document or search service endpoints. For more information,
          see `Configuring Access for a Search Domain
          <http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html>`__
          in the *Amazon CloudSearch Developer Guide* . The maximum size of a policy document is 100
          KB.
    """
