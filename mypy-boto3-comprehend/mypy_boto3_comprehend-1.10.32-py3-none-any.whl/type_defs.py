"Main interface for comprehend service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchDetectDominantLanguageResponseErrorListTypeDef",
    "ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef",
    "ClientBatchDetectDominantLanguageResponseResultListTypeDef",
    "ClientBatchDetectDominantLanguageResponseTypeDef",
    "ClientBatchDetectEntitiesResponseErrorListTypeDef",
    "ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef",
    "ClientBatchDetectEntitiesResponseResultListTypeDef",
    "ClientBatchDetectEntitiesResponseTypeDef",
    "ClientBatchDetectKeyPhrasesResponseErrorListTypeDef",
    "ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef",
    "ClientBatchDetectKeyPhrasesResponseResultListTypeDef",
    "ClientBatchDetectKeyPhrasesResponseTypeDef",
    "ClientBatchDetectSentimentResponseErrorListTypeDef",
    "ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef",
    "ClientBatchDetectSentimentResponseResultListTypeDef",
    "ClientBatchDetectSentimentResponseTypeDef",
    "ClientBatchDetectSyntaxResponseErrorListTypeDef",
    "ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef",
    "ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef",
    "ClientBatchDetectSyntaxResponseResultListTypeDef",
    "ClientBatchDetectSyntaxResponseTypeDef",
    "ClientClassifyDocumentResponseClassesTypeDef",
    "ClientClassifyDocumentResponseTypeDef",
    "ClientCreateDocumentClassifierInputDataConfigTypeDef",
    "ClientCreateDocumentClassifierOutputDataConfigTypeDef",
    "ClientCreateDocumentClassifierResponseTypeDef",
    "ClientCreateDocumentClassifierTagsTypeDef",
    "ClientCreateDocumentClassifierVpcConfigTypeDef",
    "ClientCreateEndpointResponseTypeDef",
    "ClientCreateEndpointTagsTypeDef",
    "ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef",
    "ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef",
    "ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef",
    "ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef",
    "ClientCreateEntityRecognizerInputDataConfigTypeDef",
    "ClientCreateEntityRecognizerResponseTypeDef",
    "ClientCreateEntityRecognizerTagsTypeDef",
    "ClientCreateEntityRecognizerVpcConfigTypeDef",
    "ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef",
    "ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef",
    "ClientDescribeDocumentClassificationJobResponseTypeDef",
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef",
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef",
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef",
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef",
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef",
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef",
    "ClientDescribeDocumentClassifierResponseTypeDef",
    "ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef",
    "ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef",
    "ClientDescribeDominantLanguageDetectionJobResponseTypeDef",
    "ClientDescribeEndpointResponseEndpointPropertiesTypeDef",
    "ClientDescribeEndpointResponseTypeDef",
    "ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef",
    "ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef",
    "ClientDescribeEntitiesDetectionJobResponseTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef",
    "ClientDescribeEntityRecognizerResponseTypeDef",
    "ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef",
    "ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef",
    "ClientDescribeKeyPhrasesDetectionJobResponseTypeDef",
    "ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef",
    "ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef",
    "ClientDescribeSentimentDetectionJobResponseTypeDef",
    "ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef",
    "ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef",
    "ClientDescribeTopicsDetectionJobResponseTypeDef",
    "ClientDetectDominantLanguageResponseLanguagesTypeDef",
    "ClientDetectDominantLanguageResponseTypeDef",
    "ClientDetectEntitiesResponseEntitiesTypeDef",
    "ClientDetectEntitiesResponseTypeDef",
    "ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef",
    "ClientDetectKeyPhrasesResponseTypeDef",
    "ClientDetectSentimentResponseSentimentScoreTypeDef",
    "ClientDetectSentimentResponseTypeDef",
    "ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef",
    "ClientDetectSyntaxResponseSyntaxTokensTypeDef",
    "ClientDetectSyntaxResponseTypeDef",
    "ClientListDocumentClassificationJobsFilterTypeDef",
    "ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef",
    "ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef",
    "ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef",
    "ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef",
    "ClientListDocumentClassificationJobsResponseTypeDef",
    "ClientListDocumentClassifiersFilterTypeDef",
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef",
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef",
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef",
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef",
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef",
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef",
    "ClientListDocumentClassifiersResponseTypeDef",
    "ClientListDominantLanguageDetectionJobsFilterTypeDef",
    "ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef",
    "ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef",
    "ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef",
    "ClientListDominantLanguageDetectionJobsResponseTypeDef",
    "ClientListEndpointsFilterTypeDef",
    "ClientListEndpointsResponseEndpointPropertiesListTypeDef",
    "ClientListEndpointsResponseTypeDef",
    "ClientListEntitiesDetectionJobsFilterTypeDef",
    "ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef",
    "ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef",
    "ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef",
    "ClientListEntitiesDetectionJobsResponseTypeDef",
    "ClientListEntityRecognizersFilterTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef",
    "ClientListEntityRecognizersResponseTypeDef",
    "ClientListKeyPhrasesDetectionJobsFilterTypeDef",
    "ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef",
    "ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef",
    "ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef",
    "ClientListKeyPhrasesDetectionJobsResponseTypeDef",
    "ClientListSentimentDetectionJobsFilterTypeDef",
    "ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef",
    "ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef",
    "ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef",
    "ClientListSentimentDetectionJobsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTopicsDetectionJobsFilterTypeDef",
    "ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef",
    "ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef",
    "ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef",
    "ClientListTopicsDetectionJobsResponseTypeDef",
    "ClientStartDocumentClassificationJobInputDataConfigTypeDef",
    "ClientStartDocumentClassificationJobOutputDataConfigTypeDef",
    "ClientStartDocumentClassificationJobResponseTypeDef",
    "ClientStartDocumentClassificationJobVpcConfigTypeDef",
    "ClientStartDominantLanguageDetectionJobInputDataConfigTypeDef",
    "ClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef",
    "ClientStartDominantLanguageDetectionJobResponseTypeDef",
    "ClientStartDominantLanguageDetectionJobVpcConfigTypeDef",
    "ClientStartEntitiesDetectionJobInputDataConfigTypeDef",
    "ClientStartEntitiesDetectionJobOutputDataConfigTypeDef",
    "ClientStartEntitiesDetectionJobResponseTypeDef",
    "ClientStartEntitiesDetectionJobVpcConfigTypeDef",
    "ClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef",
    "ClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef",
    "ClientStartKeyPhrasesDetectionJobResponseTypeDef",
    "ClientStartKeyPhrasesDetectionJobVpcConfigTypeDef",
    "ClientStartSentimentDetectionJobInputDataConfigTypeDef",
    "ClientStartSentimentDetectionJobOutputDataConfigTypeDef",
    "ClientStartSentimentDetectionJobResponseTypeDef",
    "ClientStartSentimentDetectionJobVpcConfigTypeDef",
    "ClientStartTopicsDetectionJobInputDataConfigTypeDef",
    "ClientStartTopicsDetectionJobOutputDataConfigTypeDef",
    "ClientStartTopicsDetectionJobResponseTypeDef",
    "ClientStartTopicsDetectionJobVpcConfigTypeDef",
    "ClientStopDominantLanguageDetectionJobResponseTypeDef",
    "ClientStopEntitiesDetectionJobResponseTypeDef",
    "ClientStopKeyPhrasesDetectionJobResponseTypeDef",
    "ClientStopSentimentDetectionJobResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ListDocumentClassificationJobsPaginateFilterTypeDef",
    "ListDocumentClassificationJobsPaginatePaginationConfigTypeDef",
    "ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef",
    "ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef",
    "ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef",
    "ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef",
    "ListDocumentClassificationJobsPaginateResponseTypeDef",
    "ListDocumentClassifiersPaginateFilterTypeDef",
    "ListDocumentClassifiersPaginatePaginationConfigTypeDef",
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef",
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef",
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef",
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef",
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef",
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef",
    "ListDocumentClassifiersPaginateResponseTypeDef",
    "ListDominantLanguageDetectionJobsPaginateFilterTypeDef",
    "ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef",
    "ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef",
    "ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef",
    "ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef",
    "ListDominantLanguageDetectionJobsPaginateResponseTypeDef",
    "ListEntitiesDetectionJobsPaginateFilterTypeDef",
    "ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef",
    "ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef",
    "ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef",
    "ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef",
    "ListEntitiesDetectionJobsPaginateResponseTypeDef",
    "ListEntityRecognizersPaginateFilterTypeDef",
    "ListEntityRecognizersPaginatePaginationConfigTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef",
    "ListEntityRecognizersPaginateResponseTypeDef",
    "ListKeyPhrasesDetectionJobsPaginateFilterTypeDef",
    "ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef",
    "ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef",
    "ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef",
    "ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef",
    "ListKeyPhrasesDetectionJobsPaginateResponseTypeDef",
    "ListSentimentDetectionJobsPaginateFilterTypeDef",
    "ListSentimentDetectionJobsPaginatePaginationConfigTypeDef",
    "ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef",
    "ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef",
    "ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef",
    "ListSentimentDetectionJobsPaginateResponseTypeDef",
    "ListTopicsDetectionJobsPaginateFilterTypeDef",
    "ListTopicsDetectionJobsPaginatePaginationConfigTypeDef",
    "ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef",
    "ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef",
    "ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef",
    "ListTopicsDetectionJobsPaginateResponseTypeDef",
)


_ClientBatchDetectDominantLanguageResponseErrorListTypeDef = TypedDict(
    "_ClientBatchDetectDominantLanguageResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDetectDominantLanguageResponseErrorListTypeDef(
    _ClientBatchDetectDominantLanguageResponseErrorListTypeDef
):
    pass


_ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef = TypedDict(
    "_ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef",
    {"LanguageCode": str, "Score": Any},
    total=False,
)


class ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef(
    _ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef
):
    pass


_ClientBatchDetectDominantLanguageResponseResultListTypeDef = TypedDict(
    "_ClientBatchDetectDominantLanguageResponseResultListTypeDef",
    {
        "Index": int,
        "Languages": List[ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef],
    },
    total=False,
)


class ClientBatchDetectDominantLanguageResponseResultListTypeDef(
    _ClientBatchDetectDominantLanguageResponseResultListTypeDef
):
    """
    - *(dict) --*

      The result of calling the operation. The operation returns one object for each document that
      is successfully processed by the operation.
      - **Index** *(integer) --*

        The zero-based index of the document in the input list.
    """


_ClientBatchDetectDominantLanguageResponseTypeDef = TypedDict(
    "_ClientBatchDetectDominantLanguageResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectDominantLanguageResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectDominantLanguageResponseErrorListTypeDef],
    },
    total=False,
)


class ClientBatchDetectDominantLanguageResponseTypeDef(
    _ClientBatchDetectDominantLanguageResponseTypeDef
):
    """
    - *(dict) --*

      - **ResultList** *(list) --*

        A list of objects containing the results of the operation. The results are sorted in
        ascending order by the ``Index`` field and match the order of the documents in the input
        list. If all of the documents contain an error, the ``ResultList`` is empty.
        - *(dict) --*

          The result of calling the operation. The operation returns one object for each document
          that is successfully processed by the operation.
          - **Index** *(integer) --*

            The zero-based index of the document in the input list.
    """


_ClientBatchDetectEntitiesResponseErrorListTypeDef = TypedDict(
    "_ClientBatchDetectEntitiesResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDetectEntitiesResponseErrorListTypeDef(
    _ClientBatchDetectEntitiesResponseErrorListTypeDef
):
    pass


_ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef = TypedDict(
    "_ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef",
    {
        "Score": Any,
        "Type": Literal[
            "PERSON",
            "LOCATION",
            "ORGANIZATION",
            "COMMERCIAL_ITEM",
            "EVENT",
            "DATE",
            "QUANTITY",
            "TITLE",
            "OTHER",
        ],
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
    },
    total=False,
)


class ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef(
    _ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef
):
    pass


_ClientBatchDetectEntitiesResponseResultListTypeDef = TypedDict(
    "_ClientBatchDetectEntitiesResponseResultListTypeDef",
    {"Index": int, "Entities": List[ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef]},
    total=False,
)


class ClientBatchDetectEntitiesResponseResultListTypeDef(
    _ClientBatchDetectEntitiesResponseResultListTypeDef
):
    """
    - *(dict) --*

      The result of calling the operation. The operation returns one object for each document that
      is successfully processed by the operation.
      - **Index** *(integer) --*

        The zero-based index of the document in the input list.
    """


_ClientBatchDetectEntitiesResponseTypeDef = TypedDict(
    "_ClientBatchDetectEntitiesResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectEntitiesResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectEntitiesResponseErrorListTypeDef],
    },
    total=False,
)


class ClientBatchDetectEntitiesResponseTypeDef(_ClientBatchDetectEntitiesResponseTypeDef):
    """
    - *(dict) --*

      - **ResultList** *(list) --*

        A list of objects containing the results of the operation. The results are sorted in
        ascending order by the ``Index`` field and match the order of the documents in the input
        list. If all of the documents contain an error, the ``ResultList`` is empty.
        - *(dict) --*

          The result of calling the operation. The operation returns one object for each document
          that is successfully processed by the operation.
          - **Index** *(integer) --*

            The zero-based index of the document in the input list.
    """


_ClientBatchDetectKeyPhrasesResponseErrorListTypeDef = TypedDict(
    "_ClientBatchDetectKeyPhrasesResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDetectKeyPhrasesResponseErrorListTypeDef(
    _ClientBatchDetectKeyPhrasesResponseErrorListTypeDef
):
    pass


_ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef = TypedDict(
    "_ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef",
    {"Score": Any, "Text": str, "BeginOffset": int, "EndOffset": int},
    total=False,
)


class ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef(
    _ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef
):
    pass


_ClientBatchDetectKeyPhrasesResponseResultListTypeDef = TypedDict(
    "_ClientBatchDetectKeyPhrasesResponseResultListTypeDef",
    {
        "Index": int,
        "KeyPhrases": List[ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef],
    },
    total=False,
)


class ClientBatchDetectKeyPhrasesResponseResultListTypeDef(
    _ClientBatchDetectKeyPhrasesResponseResultListTypeDef
):
    """
    - *(dict) --*

      The result of calling the operation. The operation returns one object for each document that
      is successfully processed by the operation.
      - **Index** *(integer) --*

        The zero-based index of the document in the input list.
    """


_ClientBatchDetectKeyPhrasesResponseTypeDef = TypedDict(
    "_ClientBatchDetectKeyPhrasesResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectKeyPhrasesResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectKeyPhrasesResponseErrorListTypeDef],
    },
    total=False,
)


class ClientBatchDetectKeyPhrasesResponseTypeDef(_ClientBatchDetectKeyPhrasesResponseTypeDef):
    """
    - *(dict) --*

      - **ResultList** *(list) --*

        A list of objects containing the results of the operation. The results are sorted in
        ascending order by the ``Index`` field and match the order of the documents in the input
        list. If all of the documents contain an error, the ``ResultList`` is empty.
        - *(dict) --*

          The result of calling the operation. The operation returns one object for each document
          that is successfully processed by the operation.
          - **Index** *(integer) --*

            The zero-based index of the document in the input list.
    """


_ClientBatchDetectSentimentResponseErrorListTypeDef = TypedDict(
    "_ClientBatchDetectSentimentResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDetectSentimentResponseErrorListTypeDef(
    _ClientBatchDetectSentimentResponseErrorListTypeDef
):
    pass


_ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef = TypedDict(
    "_ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef",
    {"Positive": Any, "Negative": Any, "Neutral": Any, "Mixed": Any},
    total=False,
)


class ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef(
    _ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef
):
    pass


_ClientBatchDetectSentimentResponseResultListTypeDef = TypedDict(
    "_ClientBatchDetectSentimentResponseResultListTypeDef",
    {
        "Index": int,
        "Sentiment": Literal["POSITIVE", "NEGATIVE", "NEUTRAL", "MIXED"],
        "SentimentScore": ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef,
    },
    total=False,
)


class ClientBatchDetectSentimentResponseResultListTypeDef(
    _ClientBatchDetectSentimentResponseResultListTypeDef
):
    """
    - *(dict) --*

      The result of calling the operation. The operation returns one object for each document that
      is successfully processed by the operation.
      - **Index** *(integer) --*

        The zero-based index of the document in the input list.
    """


_ClientBatchDetectSentimentResponseTypeDef = TypedDict(
    "_ClientBatchDetectSentimentResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectSentimentResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectSentimentResponseErrorListTypeDef],
    },
    total=False,
)


class ClientBatchDetectSentimentResponseTypeDef(_ClientBatchDetectSentimentResponseTypeDef):
    """
    - *(dict) --*

      - **ResultList** *(list) --*

        A list of objects containing the results of the operation. The results are sorted in
        ascending order by the ``Index`` field and match the order of the documents in the input
        list. If all of the documents contain an error, the ``ResultList`` is empty.
        - *(dict) --*

          The result of calling the operation. The operation returns one object for each document
          that is successfully processed by the operation.
          - **Index** *(integer) --*

            The zero-based index of the document in the input list.
    """


_ClientBatchDetectSyntaxResponseErrorListTypeDef = TypedDict(
    "_ClientBatchDetectSyntaxResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDetectSyntaxResponseErrorListTypeDef(
    _ClientBatchDetectSyntaxResponseErrorListTypeDef
):
    pass


_ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef = TypedDict(
    "_ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef",
    {
        "Tag": Literal[
            "ADJ",
            "ADP",
            "ADV",
            "AUX",
            "CONJ",
            "CCONJ",
            "DET",
            "INTJ",
            "NOUN",
            "NUM",
            "O",
            "PART",
            "PRON",
            "PROPN",
            "PUNCT",
            "SCONJ",
            "SYM",
            "VERB",
        ],
        "Score": Any,
    },
    total=False,
)


class ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef(
    _ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef
):
    pass


_ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef = TypedDict(
    "_ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef",
    {
        "TokenId": int,
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
        "PartOfSpeech": ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef,
    },
    total=False,
)


class ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef(
    _ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef
):
    pass


_ClientBatchDetectSyntaxResponseResultListTypeDef = TypedDict(
    "_ClientBatchDetectSyntaxResponseResultListTypeDef",
    {
        "Index": int,
        "SyntaxTokens": List[ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef],
    },
    total=False,
)


class ClientBatchDetectSyntaxResponseResultListTypeDef(
    _ClientBatchDetectSyntaxResponseResultListTypeDef
):
    """
    - *(dict) --*

      The result of calling the operation. The operation returns one object that is successfully
      processed by the operation.
      - **Index** *(integer) --*

        The zero-based index of the document in the input list.
    """


_ClientBatchDetectSyntaxResponseTypeDef = TypedDict(
    "_ClientBatchDetectSyntaxResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectSyntaxResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectSyntaxResponseErrorListTypeDef],
    },
    total=False,
)


class ClientBatchDetectSyntaxResponseTypeDef(_ClientBatchDetectSyntaxResponseTypeDef):
    """
    - *(dict) --*

      - **ResultList** *(list) --*

        A list of objects containing the results of the operation. The results are sorted in
        ascending order by the ``Index`` field and match the order of the documents in the input
        list. If all of the documents contain an error, the ``ResultList`` is empty.
        - *(dict) --*

          The result of calling the operation. The operation returns one object that is successfully
          processed by the operation.
          - **Index** *(integer) --*

            The zero-based index of the document in the input list.
    """


_ClientClassifyDocumentResponseClassesTypeDef = TypedDict(
    "_ClientClassifyDocumentResponseClassesTypeDef", {"Name": str, "Score": Any}, total=False
)


class ClientClassifyDocumentResponseClassesTypeDef(_ClientClassifyDocumentResponseClassesTypeDef):
    """
    - *(dict) --*

      Specifies the class that categorizes the document being analyzed
      - **Name** *(string) --*

        The name of the class.
    """


_ClientClassifyDocumentResponseTypeDef = TypedDict(
    "_ClientClassifyDocumentResponseTypeDef",
    {"Classes": List[ClientClassifyDocumentResponseClassesTypeDef]},
    total=False,
)


class ClientClassifyDocumentResponseTypeDef(_ClientClassifyDocumentResponseTypeDef):
    """
    - *(dict) --*

      - **Classes** *(list) --*

        The classes used by the document being analyzed. These are used for multi-class trained
        models. Individual classes are mutually exclusive and each document is expected to have only
        a single class assigned to it. For example, an animal can be a dog or a cat, but not both at
        the same time.
        - *(dict) --*

          Specifies the class that categorizes the document being analyzed
          - **Name** *(string) --*

            The name of the class.
    """


_ClientCreateDocumentClassifierInputDataConfigTypeDef = TypedDict(
    "_ClientCreateDocumentClassifierInputDataConfigTypeDef", {"S3Uri": str}
)


class ClientCreateDocumentClassifierInputDataConfigTypeDef(
    _ClientCreateDocumentClassifierInputDataConfigTypeDef
):
    """
    Specifies the format and location of the input data for the job.
    - **S3Uri** *(string) --***[REQUIRED]**

      The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can provide the
      prefix for a collection of input files.
      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix,
      Amazon Comprehend uses all of them as input.
    """


_ClientCreateDocumentClassifierOutputDataConfigTypeDef = TypedDict(
    "_ClientCreateDocumentClassifierOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientCreateDocumentClassifierOutputDataConfigTypeDef(
    _ClientCreateDocumentClassifierOutputDataConfigTypeDef
):
    """
    Enables the addition of output results configuration parameters for custom classifier jobs.
    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object while creating a custom classifier, you specify
      the Amazon S3 location where you want to write the confusion matrix. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the prefix for
      the actual location of this output file.
      When the custom classifier job is finished, the service creates the output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the confusion matrix.
    """


_ClientCreateDocumentClassifierResponseTypeDef = TypedDict(
    "_ClientCreateDocumentClassifierResponseTypeDef", {"DocumentClassifierArn": str}, total=False
)


class ClientCreateDocumentClassifierResponseTypeDef(_ClientCreateDocumentClassifierResponseTypeDef):
    """
    - *(dict) --*

      - **DocumentClassifierArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the document classifier.
    """


_RequiredClientCreateDocumentClassifierTagsTypeDef = TypedDict(
    "_RequiredClientCreateDocumentClassifierTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDocumentClassifierTagsTypeDef = TypedDict(
    "_OptionalClientCreateDocumentClassifierTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDocumentClassifierTagsTypeDef(
    _RequiredClientCreateDocumentClassifierTagsTypeDef,
    _OptionalClientCreateDocumentClassifierTagsTypeDef,
):
    """
    - *(dict) --*

      A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example,
      a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource to indicate
      its use by a particular department.
      - **Key** *(string) --***[REQUIRED]**

        The initial part of a key-value pair that forms a tag associated with a given resource. For
        instance, if you want to show which resources are used by which departments, you might use
        “Department” as the key portion of the pair, with multiple possible values such as “sales,”
        “legal,” and “administration.”
    """


_RequiredClientCreateDocumentClassifierVpcConfigTypeDef = TypedDict(
    "_RequiredClientCreateDocumentClassifierVpcConfigTypeDef", {"SecurityGroupIds": List[str]}
)
_OptionalClientCreateDocumentClassifierVpcConfigTypeDef = TypedDict(
    "_OptionalClientCreateDocumentClassifierVpcConfigTypeDef", {"Subnets": List[str]}, total=False
)


class ClientCreateDocumentClassifierVpcConfigTypeDef(
    _RequiredClientCreateDocumentClassifierVpcConfigTypeDef,
    _OptionalClientCreateDocumentClassifierVpcConfigTypeDef,
):
    """
    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your custom classifier. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .
    - **SecurityGroupIds** *(list) --***[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .
      - *(string) --*
    """


_ClientCreateEndpointResponseTypeDef = TypedDict(
    "_ClientCreateEndpointResponseTypeDef", {"EndpointArn": str}, total=False
)


class ClientCreateEndpointResponseTypeDef(_ClientCreateEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointArn** *(string) --*

        The Amazon Resource Number (ARN) of the endpoint being created.
    """


_RequiredClientCreateEndpointTagsTypeDef = TypedDict(
    "_RequiredClientCreateEndpointTagsTypeDef", {"Key": str}
)
_OptionalClientCreateEndpointTagsTypeDef = TypedDict(
    "_OptionalClientCreateEndpointTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateEndpointTagsTypeDef(
    _RequiredClientCreateEndpointTagsTypeDef, _OptionalClientCreateEndpointTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example,
      a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource to indicate
      its use by a particular department.
      - **Key** *(string) --***[REQUIRED]**

        The initial part of a key-value pair that forms a tag associated with a given resource. For
        instance, if you want to show which resources are used by which departments, you might use
        “Department” as the key portion of the pair, with multiple possible values such as “sales,”
        “legal,” and “administration.”
    """


_ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef = TypedDict(
    "_ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef", {"S3Uri": str}, total=False
)


class ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef(
    _ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef
):
    pass


_ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef = TypedDict(
    "_ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef", {"S3Uri": str}, total=False
)


class ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef(
    _ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef
):
    pass


_ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef = TypedDict(
    "_ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef", {"S3Uri": str}, total=False
)


class ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef(
    _ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef
):
    pass


_ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef = TypedDict(
    "_ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef", {"Type": str}
)


class ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef(
    _ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef
):
    """
    - *(dict) --*

      Information about an individual item on a list of entity types.
      - **Type** *(string) --***[REQUIRED]**

        Entity type of an item on an entity type list.
    """


_RequiredClientCreateEntityRecognizerInputDataConfigTypeDef = TypedDict(
    "_RequiredClientCreateEntityRecognizerInputDataConfigTypeDef",
    {"EntityTypes": List[ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef]},
)
_OptionalClientCreateEntityRecognizerInputDataConfigTypeDef = TypedDict(
    "_OptionalClientCreateEntityRecognizerInputDataConfigTypeDef",
    {
        "Documents": ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef,
        "Annotations": ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef,
        "EntityList": ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef,
    },
    total=False,
)


class ClientCreateEntityRecognizerInputDataConfigTypeDef(
    _RequiredClientCreateEntityRecognizerInputDataConfigTypeDef,
    _OptionalClientCreateEntityRecognizerInputDataConfigTypeDef,
):
    """
    Specifies the format and location of the input data. The S3 bucket containing the input data
    must be located in the same region as the entity recognizer being created.
    - **EntityTypes** *(list) --***[REQUIRED]**

      The entity types in the input data for an entity recognizer. A maximum of 12 entity types can
      be used at one time to train an entity recognizer.
      - *(dict) --*

        Information about an individual item on a list of entity types.
        - **Type** *(string) --***[REQUIRED]**

          Entity type of an item on an entity type list.
    """


_ClientCreateEntityRecognizerResponseTypeDef = TypedDict(
    "_ClientCreateEntityRecognizerResponseTypeDef", {"EntityRecognizerArn": str}, total=False
)


class ClientCreateEntityRecognizerResponseTypeDef(_ClientCreateEntityRecognizerResponseTypeDef):
    """
    - *(dict) --*

      - **EntityRecognizerArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the entity recognizer.
    """


_RequiredClientCreateEntityRecognizerTagsTypeDef = TypedDict(
    "_RequiredClientCreateEntityRecognizerTagsTypeDef", {"Key": str}
)
_OptionalClientCreateEntityRecognizerTagsTypeDef = TypedDict(
    "_OptionalClientCreateEntityRecognizerTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateEntityRecognizerTagsTypeDef(
    _RequiredClientCreateEntityRecognizerTagsTypeDef,
    _OptionalClientCreateEntityRecognizerTagsTypeDef,
):
    """
    - *(dict) --*

      A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example,
      a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource to indicate
      its use by a particular department.
      - **Key** *(string) --***[REQUIRED]**

        The initial part of a key-value pair that forms a tag associated with a given resource. For
        instance, if you want to show which resources are used by which departments, you might use
        “Department” as the key portion of the pair, with multiple possible values such as “sales,”
        “legal,” and “administration.”
    """


_RequiredClientCreateEntityRecognizerVpcConfigTypeDef = TypedDict(
    "_RequiredClientCreateEntityRecognizerVpcConfigTypeDef", {"SecurityGroupIds": List[str]}
)
_OptionalClientCreateEntityRecognizerVpcConfigTypeDef = TypedDict(
    "_OptionalClientCreateEntityRecognizerVpcConfigTypeDef", {"Subnets": List[str]}, total=False
)


class ClientCreateEntityRecognizerVpcConfigTypeDef(
    _RequiredClientCreateEntityRecognizerVpcConfigTypeDef,
    _OptionalClientCreateEntityRecognizerVpcConfigTypeDef,
):
    """
    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your custom entity recognizer. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .
    - **SecurityGroupIds** *(list) --***[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .
      - *(string) --*
    """


_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef
):
    pass


_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef
):
    pass


_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef(
    _ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef
):
    pass


_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "DocumentClassifierArn": str,
        "InputDataConfig": ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef(
    _ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef
):
    """
    - **DocumentClassificationJobProperties** *(dict) --*

      An object that describes the properties associated with the document classification job.
      - **JobId** *(string) --*

        The identifier assigned to the document classification job.
    """


_ClientDescribeDocumentClassificationJobResponseTypeDef = TypedDict(
    "_ClientDescribeDocumentClassificationJobResponseTypeDef",
    {
        "DocumentClassificationJobProperties": ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeDocumentClassificationJobResponseTypeDef(
    _ClientDescribeDocumentClassificationJobResponseTypeDef
):
    """
    - *(dict) --*

      - **DocumentClassificationJobProperties** *(dict) --*

        An object that describes the properties associated with the document classification job.
        - **JobId** *(string) --*

          The identifier assigned to the document classification job.
    """


_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef",
    {"Accuracy": float, "Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef(
    _ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef
):
    pass


_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef",
    {
        "NumberOfLabels": int,
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef,
    },
    total=False,
)


class ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef(
    _ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef
):
    pass


_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef(
    _ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef
):
    pass


_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef(
    _ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef
):
    pass


_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef(
    _ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef
):
    pass


_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef",
    {
        "DocumentClassifierArn": str,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef,
        "ClassifierMetadata": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef(
    _ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef
):
    """
    - **DocumentClassifierProperties** *(dict) --*

      An object that contains the properties associated with a document classifier.
      - **DocumentClassifierArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the document classifier.
    """


_ClientDescribeDocumentClassifierResponseTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseTypeDef",
    {
        "DocumentClassifierProperties": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeDocumentClassifierResponseTypeDef(
    _ClientDescribeDocumentClassifierResponseTypeDef
):
    """
    - *(dict) --*

      - **DocumentClassifierProperties** *(dict) --*

        An object that contains the properties associated with a document classifier.
        - **DocumentClassifierArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the document classifier.
    """


_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef
):
    pass


_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef
):
    pass


_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef(
    _ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef
):
    pass


_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef(
    _ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef
):
    """
    - **DominantLanguageDetectionJobProperties** *(dict) --*

      An object that contains the properties associated with a dominant language detection job.
      - **JobId** *(string) --*

        The identifier assigned to the dominant language detection job.
    """


_ClientDescribeDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "_ClientDescribeDominantLanguageDetectionJobResponseTypeDef",
    {
        "DominantLanguageDetectionJobProperties": ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeDominantLanguageDetectionJobResponseTypeDef(
    _ClientDescribeDominantLanguageDetectionJobResponseTypeDef
):
    """
    - *(dict) --*

      - **DominantLanguageDetectionJobProperties** *(dict) --*

        An object that contains the properties associated with a dominant language detection job.
        - **JobId** *(string) --*

          The identifier assigned to the dominant language detection job.
    """


_ClientDescribeEndpointResponseEndpointPropertiesTypeDef = TypedDict(
    "_ClientDescribeEndpointResponseEndpointPropertiesTypeDef",
    {
        "EndpointArn": str,
        "Status": Literal["CREATING", "DELETING", "FAILED", "IN_SERVICE", "UPDATING"],
        "Message": str,
        "ModelArn": str,
        "DesiredInferenceUnits": int,
        "CurrentInferenceUnits": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ClientDescribeEndpointResponseEndpointPropertiesTypeDef(
    _ClientDescribeEndpointResponseEndpointPropertiesTypeDef
):
    """
    - **EndpointProperties** *(dict) --*

      Describes information associated with the specific endpoint.
      - **EndpointArn** *(string) --*

        The Amazon Resource Number (ARN) of the endpoint.
    """


_ClientDescribeEndpointResponseTypeDef = TypedDict(
    "_ClientDescribeEndpointResponseTypeDef",
    {"EndpointProperties": ClientDescribeEndpointResponseEndpointPropertiesTypeDef},
    total=False,
)


class ClientDescribeEndpointResponseTypeDef(_ClientDescribeEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointProperties** *(dict) --*

        Describes information associated with the specific endpoint.
        - **EndpointArn** *(string) --*

          The Amazon Resource Number (ARN) of the endpoint.
    """


_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef
):
    pass


_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef
):
    pass


_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef(
    _ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef
):
    pass


_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "EntityRecognizerArn": str,
        "InputDataConfig": ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef(
    _ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef
):
    """
    - **EntitiesDetectionJobProperties** *(dict) --*

      An object that contains the properties associated with an entities detection job.
      - **JobId** *(string) --*

        The identifier assigned to the entities detection job.
    """


_ClientDescribeEntitiesDetectionJobResponseTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionJobResponseTypeDef",
    {
        "EntitiesDetectionJobProperties": ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeEntitiesDetectionJobResponseTypeDef(
    _ClientDescribeEntitiesDetectionJobResponseTypeDef
):
    """
    - *(dict) --*

      - **EntitiesDetectionJobProperties** *(dict) --*

        An object that contains the properties associated with an entities detection job.
        - **JobId** *(string) --*

          The identifier assigned to the entities detection job.
    """


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef
):
    pass


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef
):
    pass


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef
):
    pass


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef",
    {"Type": str},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef
):
    pass


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef",
    {
        "EntityTypes": List[
            ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef
        ],
        "Documents": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef,
        "Annotations": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef,
        "EntityList": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef,
    },
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef
):
    pass


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef
):
    pass


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef",
    {
        "Type": str,
        "EvaluationMetrics": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef,
        "NumberOfTrainMentions": int,
    },
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef
):
    pass


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef
):
    pass


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef",
    {
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef,
        "EntityTypes": List[
            ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef
):
    pass


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef
):
    pass


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef",
    {
        "EntityRecognizerArn": str,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef,
        "RecognizerMetadata": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef
):
    """
    - **EntityRecognizerProperties** *(dict) --*

      Describes information associated with an entity recognizer.
      - **EntityRecognizerArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the entity recognizer.
    """


_ClientDescribeEntityRecognizerResponseTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseTypeDef",
    {
        "EntityRecognizerProperties": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeEntityRecognizerResponseTypeDef(_ClientDescribeEntityRecognizerResponseTypeDef):
    """
    - *(dict) --*

      - **EntityRecognizerProperties** *(dict) --*

        Describes information associated with an entity recognizer.
        - **EntityRecognizerArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the entity recognizer.
    """


_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef
):
    pass


_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef
):
    pass


_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef(
    _ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef
):
    pass


_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef(
    _ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef
):
    """
    - **KeyPhrasesDetectionJobProperties** *(dict) --*

      An object that contains the properties associated with a key phrases detection job.
      - **JobId** *(string) --*

        The identifier assigned to the key phrases detection job.
    """


_ClientDescribeKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "_ClientDescribeKeyPhrasesDetectionJobResponseTypeDef",
    {
        "KeyPhrasesDetectionJobProperties": ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeKeyPhrasesDetectionJobResponseTypeDef(
    _ClientDescribeKeyPhrasesDetectionJobResponseTypeDef
):
    """
    - *(dict) --*

      - **KeyPhrasesDetectionJobProperties** *(dict) --*

        An object that contains the properties associated with a key phrases detection job.
        - **JobId** *(string) --*

          The identifier assigned to the key phrases detection job.
    """


_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef
):
    pass


_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef
):
    pass


_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef(
    _ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef
):
    pass


_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef(
    _ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef
):
    """
    - **SentimentDetectionJobProperties** *(dict) --*

      An object that contains the properties associated with a sentiment detection job.
      - **JobId** *(string) --*

        The identifier assigned to the sentiment detection job.
    """


_ClientDescribeSentimentDetectionJobResponseTypeDef = TypedDict(
    "_ClientDescribeSentimentDetectionJobResponseTypeDef",
    {
        "SentimentDetectionJobProperties": ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeSentimentDetectionJobResponseTypeDef(
    _ClientDescribeSentimentDetectionJobResponseTypeDef
):
    """
    - *(dict) --*

      - **SentimentDetectionJobProperties** *(dict) --*

        An object that contains the properties associated with a sentiment detection job.
        - **JobId** *(string) --*

          The identifier assigned to the sentiment detection job.
    """


_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef
):
    pass


_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef
):
    pass


_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef(
    _ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef
):
    pass


_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef,
        "NumberOfTopics": int,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef(
    _ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef
):
    """
    - **TopicsDetectionJobProperties** *(dict) --*

      The list of properties for the requested job.
      - **JobId** *(string) --*

        The identifier assigned to the topic detection job.
    """


_ClientDescribeTopicsDetectionJobResponseTypeDef = TypedDict(
    "_ClientDescribeTopicsDetectionJobResponseTypeDef",
    {
        "TopicsDetectionJobProperties": ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeTopicsDetectionJobResponseTypeDef(
    _ClientDescribeTopicsDetectionJobResponseTypeDef
):
    """
    - *(dict) --*

      - **TopicsDetectionJobProperties** *(dict) --*

        The list of properties for the requested job.
        - **JobId** *(string) --*

          The identifier assigned to the topic detection job.
    """


_ClientDetectDominantLanguageResponseLanguagesTypeDef = TypedDict(
    "_ClientDetectDominantLanguageResponseLanguagesTypeDef",
    {"LanguageCode": str, "Score": Any},
    total=False,
)


class ClientDetectDominantLanguageResponseLanguagesTypeDef(
    _ClientDetectDominantLanguageResponseLanguagesTypeDef
):
    """
    - *(dict) --*

      Returns the code for the dominant language in the input text and the level of confidence that
      Amazon Comprehend has in the accuracy of the detection.
      - **LanguageCode** *(string) --*

        The RFC 5646 language code for the dominant language. For more information about RFC 5646,
        see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on the *IETF
        Tools* web site.
    """


_ClientDetectDominantLanguageResponseTypeDef = TypedDict(
    "_ClientDetectDominantLanguageResponseTypeDef",
    {"Languages": List[ClientDetectDominantLanguageResponseLanguagesTypeDef]},
    total=False,
)


class ClientDetectDominantLanguageResponseTypeDef(_ClientDetectDominantLanguageResponseTypeDef):
    """
    - *(dict) --*

      - **Languages** *(list) --*

        The languages that Amazon Comprehend detected in the input text. For each language, the
        response returns the RFC 5646 language code and the level of confidence that Amazon
        Comprehend has in the accuracy of its inference. For more information about RFC 5646, see
        `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on the *IETF Tools*
        web site.
        - *(dict) --*

          Returns the code for the dominant language in the input text and the level of confidence
          that Amazon Comprehend has in the accuracy of the detection.
          - **LanguageCode** *(string) --*

            The RFC 5646 language code for the dominant language. For more information about RFC
            5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on
            the *IETF Tools* web site.
    """


_ClientDetectEntitiesResponseEntitiesTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseEntitiesTypeDef",
    {
        "Score": float,
        "Type": Literal[
            "PERSON",
            "LOCATION",
            "ORGANIZATION",
            "COMMERCIAL_ITEM",
            "EVENT",
            "DATE",
            "QUANTITY",
            "TITLE",
            "OTHER",
        ],
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
    },
    total=False,
)


class ClientDetectEntitiesResponseEntitiesTypeDef(_ClientDetectEntitiesResponseEntitiesTypeDef):
    """
    - *(dict) --*

      Provides information about an entity.
      - **Score** *(float) --*

        The level of confidence that Amazon Comprehend has in the accuracy of the detection.
    """


_ClientDetectEntitiesResponseTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseTypeDef",
    {"Entities": List[ClientDetectEntitiesResponseEntitiesTypeDef]},
    total=False,
)


class ClientDetectEntitiesResponseTypeDef(_ClientDetectEntitiesResponseTypeDef):
    """
    - *(dict) --*

      - **Entities** *(list) --*

        A collection of entities identified in the input text. For each entity, the response
        provides the entity text, entity type, where the entity text begins and ends, and the level
        of confidence that Amazon Comprehend has in the detection. For a list of entity types, see
        how-entities .
        - *(dict) --*

          Provides information about an entity.
          - **Score** *(float) --*

            The level of confidence that Amazon Comprehend has in the accuracy of the detection.
    """


_ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef = TypedDict(
    "_ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef",
    {"Score": float, "Text": str, "BeginOffset": int, "EndOffset": int},
    total=False,
)


class ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef(
    _ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef
):
    """
    - *(dict) --*

      Describes a key noun phrase.
      - **Score** *(float) --*

        The level of confidence that Amazon Comprehend has in the accuracy of the detection.
    """


_ClientDetectKeyPhrasesResponseTypeDef = TypedDict(
    "_ClientDetectKeyPhrasesResponseTypeDef",
    {"KeyPhrases": List[ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef]},
    total=False,
)


class ClientDetectKeyPhrasesResponseTypeDef(_ClientDetectKeyPhrasesResponseTypeDef):
    """
    - *(dict) --*

      - **KeyPhrases** *(list) --*

        A collection of key phrases that Amazon Comprehend identified in the input text. For each
        key phrase, the response provides the text of the key phrase, where the key phrase begins
        and ends, and the level of confidence that Amazon Comprehend has in the accuracy of the
        detection.
        - *(dict) --*

          Describes a key noun phrase.
          - **Score** *(float) --*

            The level of confidence that Amazon Comprehend has in the accuracy of the detection.
    """


_ClientDetectSentimentResponseSentimentScoreTypeDef = TypedDict(
    "_ClientDetectSentimentResponseSentimentScoreTypeDef",
    {"Positive": Any, "Negative": Any, "Neutral": Any, "Mixed": Any},
    total=False,
)


class ClientDetectSentimentResponseSentimentScoreTypeDef(
    _ClientDetectSentimentResponseSentimentScoreTypeDef
):
    pass


_ClientDetectSentimentResponseTypeDef = TypedDict(
    "_ClientDetectSentimentResponseTypeDef",
    {
        "Sentiment": Literal["POSITIVE", "NEGATIVE", "NEUTRAL", "MIXED"],
        "SentimentScore": ClientDetectSentimentResponseSentimentScoreTypeDef,
    },
    total=False,
)


class ClientDetectSentimentResponseTypeDef(_ClientDetectSentimentResponseTypeDef):
    """
    - *(dict) --*

      - **Sentiment** *(string) --*

        The inferred sentiment that Amazon Comprehend has the highest level of confidence in.
    """


_ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef = TypedDict(
    "_ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef",
    {
        "Tag": Literal[
            "ADJ",
            "ADP",
            "ADV",
            "AUX",
            "CONJ",
            "CCONJ",
            "DET",
            "INTJ",
            "NOUN",
            "NUM",
            "O",
            "PART",
            "PRON",
            "PROPN",
            "PUNCT",
            "SCONJ",
            "SYM",
            "VERB",
        ],
        "Score": Any,
    },
    total=False,
)


class ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef(
    _ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef
):
    pass


_ClientDetectSyntaxResponseSyntaxTokensTypeDef = TypedDict(
    "_ClientDetectSyntaxResponseSyntaxTokensTypeDef",
    {
        "TokenId": int,
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
        "PartOfSpeech": ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef,
    },
    total=False,
)


class ClientDetectSyntaxResponseSyntaxTokensTypeDef(_ClientDetectSyntaxResponseSyntaxTokensTypeDef):
    """
    - *(dict) --*

      Represents a work in the input text that was recognized and assigned a part of speech. There
      is one syntax token record for each word in the source text.
      - **TokenId** *(integer) --*

        A unique identifier for a token.
    """


_ClientDetectSyntaxResponseTypeDef = TypedDict(
    "_ClientDetectSyntaxResponseTypeDef",
    {"SyntaxTokens": List[ClientDetectSyntaxResponseSyntaxTokensTypeDef]},
    total=False,
)


class ClientDetectSyntaxResponseTypeDef(_ClientDetectSyntaxResponseTypeDef):
    """
    - *(dict) --*

      - **SyntaxTokens** *(list) --*

        A collection of syntax tokens describing the text. For each token, the response provides the
        text, the token type, where the text begins and ends, and the level of confidence that
        Amazon Comprehend has that the token is correct. For a list of token types, see  how-syntax
        .
        - *(dict) --*

          Represents a work in the input text that was recognized and assigned a part of speech.
          There is one syntax token record for each word in the source text.
          - **TokenId** *(integer) --*

            A unique identifier for a token.
    """


_ClientListDocumentClassificationJobsFilterTypeDef = TypedDict(
    "_ClientListDocumentClassificationJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListDocumentClassificationJobsFilterTypeDef(
    _ClientListDocumentClassificationJobsFilterTypeDef
):
    """
    Filters the jobs that are returned. You can filter jobs on their names, status, or the date and
    time that they were submitted. You can only set one filter at a time.
    - **JobName** *(string) --*

      Filters on the name of the job.
    """


_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef(
    _ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef
):
    pass


_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef(
    _ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef(
    _ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef
):
    pass


_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef = TypedDict(
    "_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "DocumentClassifierArn": str,
        "InputDataConfig": ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef(
    _ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a document classification job.
      - **JobId** *(string) --*

        The identifier assigned to the document classification job.
    """


_ClientListDocumentClassificationJobsResponseTypeDef = TypedDict(
    "_ClientListDocumentClassificationJobsResponseTypeDef",
    {
        "DocumentClassificationJobPropertiesList": List[
            ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListDocumentClassificationJobsResponseTypeDef(
    _ClientListDocumentClassificationJobsResponseTypeDef
):
    """
    - *(dict) --*

      - **DocumentClassificationJobPropertiesList** *(list) --*

        A list containing the properties of each job returned.
        - *(dict) --*

          Provides information about a document classification job.
          - **JobId** *(string) --*

            The identifier assigned to the document classification job.
    """


_ClientListDocumentClassifiersFilterTypeDef = TypedDict(
    "_ClientListDocumentClassifiersFilterTypeDef",
    {
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListDocumentClassifiersFilterTypeDef(_ClientListDocumentClassifiersFilterTypeDef):
    """
    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.
    - **Status** *(string) --*

      Filters the list of classifiers based on status.
    """


_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef",
    {"Accuracy": float, "Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef(
    _ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef
):
    pass


_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef",
    {
        "NumberOfLabels": int,
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef,
    },
    total=False,
)


class ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef(
    _ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef
):
    pass


_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef(
    _ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef
):
    pass


_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef(
    _ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef
):
    pass


_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef(
    _ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef
):
    pass


_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef",
    {
        "DocumentClassifierArn": str,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef,
        "ClassifierMetadata": ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef(
    _ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a document classifier.
      - **DocumentClassifierArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the document classifier.
    """


_ClientListDocumentClassifiersResponseTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseTypeDef",
    {
        "DocumentClassifierPropertiesList": List[
            ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListDocumentClassifiersResponseTypeDef(_ClientListDocumentClassifiersResponseTypeDef):
    """
    - *(dict) --*

      - **DocumentClassifierPropertiesList** *(list) --*

        A list containing the properties of each job returned.
        - *(dict) --*

          Provides information about a document classifier.
          - **DocumentClassifierArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the document classifier.
    """


_ClientListDominantLanguageDetectionJobsFilterTypeDef = TypedDict(
    "_ClientListDominantLanguageDetectionJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListDominantLanguageDetectionJobsFilterTypeDef(
    _ClientListDominantLanguageDetectionJobsFilterTypeDef
):
    """
    Filters that jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.
    - **JobName** *(string) --*

      Filters on the name of the job.
    """


_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef(
    _ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef
):
    pass


_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef(
    _ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef
):
    pass


_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef = TypedDict(
    "_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef(
    _ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a dominant language detection job.
      - **JobId** *(string) --*

        The identifier assigned to the dominant language detection job.
    """


_ClientListDominantLanguageDetectionJobsResponseTypeDef = TypedDict(
    "_ClientListDominantLanguageDetectionJobsResponseTypeDef",
    {
        "DominantLanguageDetectionJobPropertiesList": List[
            ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListDominantLanguageDetectionJobsResponseTypeDef(
    _ClientListDominantLanguageDetectionJobsResponseTypeDef
):
    """
    - *(dict) --*

      - **DominantLanguageDetectionJobPropertiesList** *(list) --*

        A list containing the properties of each job that is returned.
        - *(dict) --*

          Provides information about a dominant language detection job.
          - **JobId** *(string) --*

            The identifier assigned to the dominant language detection job.
    """


_ClientListEndpointsFilterTypeDef = TypedDict(
    "_ClientListEndpointsFilterTypeDef",
    {
        "ModelArn": str,
        "Status": Literal["CREATING", "DELETING", "FAILED", "IN_SERVICE", "UPDATING"],
        "CreationTimeBefore": datetime,
        "CreationTimeAfter": datetime,
    },
    total=False,
)


class ClientListEndpointsFilterTypeDef(_ClientListEndpointsFilterTypeDef):
    """
    Filters the endpoints that are returned. You can filter endpoints on their name, model, status,
    or the date and time that they were created. You can only set one filter at a time.
    - **ModelArn** *(string) --*

      The Amazon Resource Number (ARN) of the model to which the endpoint is attached.
    """


_ClientListEndpointsResponseEndpointPropertiesListTypeDef = TypedDict(
    "_ClientListEndpointsResponseEndpointPropertiesListTypeDef",
    {
        "EndpointArn": str,
        "Status": Literal["CREATING", "DELETING", "FAILED", "IN_SERVICE", "UPDATING"],
        "Message": str,
        "ModelArn": str,
        "DesiredInferenceUnits": int,
        "CurrentInferenceUnits": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ClientListEndpointsResponseEndpointPropertiesListTypeDef(
    _ClientListEndpointsResponseEndpointPropertiesListTypeDef
):
    """
    - *(dict) --*

      Specifies information about the specified endpoint.
      - **EndpointArn** *(string) --*

        The Amazon Resource Number (ARN) of the endpoint.
    """


_ClientListEndpointsResponseTypeDef = TypedDict(
    "_ClientListEndpointsResponseTypeDef",
    {
        "EndpointPropertiesList": List[ClientListEndpointsResponseEndpointPropertiesListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListEndpointsResponseTypeDef(_ClientListEndpointsResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointPropertiesList** *(list) --*

        Displays a list of endpoint properties being retrieved by the service in response to the
        request.
        - *(dict) --*

          Specifies information about the specified endpoint.
          - **EndpointArn** *(string) --*

            The Amazon Resource Number (ARN) of the endpoint.
    """


_ClientListEntitiesDetectionJobsFilterTypeDef = TypedDict(
    "_ClientListEntitiesDetectionJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListEntitiesDetectionJobsFilterTypeDef(_ClientListEntitiesDetectionJobsFilterTypeDef):
    """
    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.
    - **JobName** *(string) --*

      Filters on the name of the job.
    """


_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef(
    _ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef
):
    pass


_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef(
    _ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef
):
    pass


_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef = TypedDict(
    "_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "EntityRecognizerArn": str,
        "InputDataConfig": ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef(
    _ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about an entities detection job.
      - **JobId** *(string) --*

        The identifier assigned to the entities detection job.
    """


_ClientListEntitiesDetectionJobsResponseTypeDef = TypedDict(
    "_ClientListEntitiesDetectionJobsResponseTypeDef",
    {
        "EntitiesDetectionJobPropertiesList": List[
            ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListEntitiesDetectionJobsResponseTypeDef(
    _ClientListEntitiesDetectionJobsResponseTypeDef
):
    """
    - *(dict) --*

      - **EntitiesDetectionJobPropertiesList** *(list) --*

        A list containing the properties of each job that is returned.
        - *(dict) --*

          Provides information about an entities detection job.
          - **JobId** *(string) --*

            The identifier assigned to the entities detection job.
    """


_ClientListEntityRecognizersFilterTypeDef = TypedDict(
    "_ClientListEntityRecognizersFilterTypeDef",
    {
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListEntityRecognizersFilterTypeDef(_ClientListEntityRecognizersFilterTypeDef):
    """
    Filters the list of entities returned. You can filter on ``Status`` , ``SubmitTimeBefore`` , or
    ``SubmitTimeAfter`` . You can only set one filter at a time.
    - **Status** *(string) --*

      The status of an entity recognizer.
    """


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef
):
    pass


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef
):
    pass


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef
):
    pass


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef",
    {"Type": str},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef
):
    pass


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef",
    {
        "EntityTypes": List[
            ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef
        ],
        "Documents": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef,
        "Annotations": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef,
        "EntityList": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef,
    },
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef
):
    pass


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef
):
    pass


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef",
    {
        "Type": str,
        "EvaluationMetrics": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef,
        "NumberOfTrainMentions": int,
    },
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef
):
    pass


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef
):
    pass


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef",
    {
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef,
        "EntityTypes": List[
            ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef
        ],
    },
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef
):
    pass


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef
):
    pass


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef",
    {
        "EntityRecognizerArn": str,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef,
        "RecognizerMetadata": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef
):
    """
    - *(dict) --*

      Describes information about an entity recognizer.
      - **EntityRecognizerArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the entity recognizer.
    """


_ClientListEntityRecognizersResponseTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseTypeDef",
    {
        "EntityRecognizerPropertiesList": List[
            ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListEntityRecognizersResponseTypeDef(_ClientListEntityRecognizersResponseTypeDef):
    """
    - *(dict) --*

      - **EntityRecognizerPropertiesList** *(list) --*

        The list of properties of an entity recognizer.
        - *(dict) --*

          Describes information about an entity recognizer.
          - **EntityRecognizerArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the entity recognizer.
    """


_ClientListKeyPhrasesDetectionJobsFilterTypeDef = TypedDict(
    "_ClientListKeyPhrasesDetectionJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListKeyPhrasesDetectionJobsFilterTypeDef(
    _ClientListKeyPhrasesDetectionJobsFilterTypeDef
):
    """
    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.
    - **JobName** *(string) --*

      Filters on the name of the job.
    """


_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef(
    _ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef
):
    pass


_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef(
    _ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef
):
    pass


_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef = TypedDict(
    "_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef(
    _ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a key phrases detection job.
      - **JobId** *(string) --*

        The identifier assigned to the key phrases detection job.
    """


_ClientListKeyPhrasesDetectionJobsResponseTypeDef = TypedDict(
    "_ClientListKeyPhrasesDetectionJobsResponseTypeDef",
    {
        "KeyPhrasesDetectionJobPropertiesList": List[
            ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListKeyPhrasesDetectionJobsResponseTypeDef(
    _ClientListKeyPhrasesDetectionJobsResponseTypeDef
):
    """
    - *(dict) --*

      - **KeyPhrasesDetectionJobPropertiesList** *(list) --*

        A list containing the properties of each job that is returned.
        - *(dict) --*

          Provides information about a key phrases detection job.
          - **JobId** *(string) --*

            The identifier assigned to the key phrases detection job.
    """


_ClientListSentimentDetectionJobsFilterTypeDef = TypedDict(
    "_ClientListSentimentDetectionJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListSentimentDetectionJobsFilterTypeDef(_ClientListSentimentDetectionJobsFilterTypeDef):
    """
    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.
    - **JobName** *(string) --*

      Filters on the name of the job.
    """


_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef(
    _ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef
):
    pass


_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef(
    _ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef
):
    pass


_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef = TypedDict(
    "_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef(
    _ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a sentiment detection job.
      - **JobId** *(string) --*

        The identifier assigned to the sentiment detection job.
    """


_ClientListSentimentDetectionJobsResponseTypeDef = TypedDict(
    "_ClientListSentimentDetectionJobsResponseTypeDef",
    {
        "SentimentDetectionJobPropertiesList": List[
            ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListSentimentDetectionJobsResponseTypeDef(
    _ClientListSentimentDetectionJobsResponseTypeDef
):
    """
    - *(dict) --*

      - **SentimentDetectionJobPropertiesList** *(list) --*

        A list containing the properties of each job that is returned.
        - *(dict) --*

          Provides information about a sentiment detection job.
          - **JobId** *(string) --*

            The identifier assigned to the sentiment detection job.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    pass


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"ResourceArn": str, "Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the given Amazon Comprehend resource you are querying.
    """


_ClientListTopicsDetectionJobsFilterTypeDef = TypedDict(
    "_ClientListTopicsDetectionJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListTopicsDetectionJobsFilterTypeDef(_ClientListTopicsDetectionJobsFilterTypeDef):
    """
    Filters the jobs that are returned. Jobs can be filtered on their name, status, or the date and
    time that they were submitted. You can set only one filter at a time.
    - **JobName** *(string) --*
    - **JobStatus** *(string) --*

      Filters the list of topic detection jobs based on job status. Returns only jobs with the
      specified status.
    """


_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef(
    _ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef
):
    pass


_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef(
    _ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef
):
    pass


_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef = TypedDict(
    "_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef,
        "NumberOfTopics": int,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef(
    _ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a topic detection job.
      - **JobId** *(string) --*

        The identifier assigned to the topic detection job.
    """


_ClientListTopicsDetectionJobsResponseTypeDef = TypedDict(
    "_ClientListTopicsDetectionJobsResponseTypeDef",
    {
        "TopicsDetectionJobPropertiesList": List[
            ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListTopicsDetectionJobsResponseTypeDef(_ClientListTopicsDetectionJobsResponseTypeDef):
    """
    - *(dict) --*

      - **TopicsDetectionJobPropertiesList** *(list) --*

        A list containing the properties of each job that is returned.
        - *(dict) --*

          Provides information about a topic detection job.
          - **JobId** *(string) --*

            The identifier assigned to the topic detection job.
    """


_RequiredClientStartDocumentClassificationJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartDocumentClassificationJobInputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartDocumentClassificationJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartDocumentClassificationJobInputDataConfigTypeDef",
    {"InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientStartDocumentClassificationJobInputDataConfigTypeDef(
    _RequiredClientStartDocumentClassificationJobInputDataConfigTypeDef,
    _OptionalClientStartDocumentClassificationJobInputDataConfigTypeDef,
):
    """
    Specifies the format and location of the input data for the job.
    - **S3Uri** *(string) --***[REQUIRED]**

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that
      you are calling. The URI can point to a single input file or it can provide the prefix for a
      collection of data files.
      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix,
      Amazon Comprehend uses all of them as input.
    """


_RequiredClientStartDocumentClassificationJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartDocumentClassificationJobOutputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartDocumentClassificationJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartDocumentClassificationJobOutputDataConfigTypeDef",
    {"KmsKeyId": str},
    total=False,
)


class ClientStartDocumentClassificationJobOutputDataConfigTypeDef(
    _RequiredClientStartDocumentClassificationJobOutputDataConfigTypeDef,
    _OptionalClientStartDocumentClassificationJobOutputDataConfigTypeDef,
):
    """
    Specifies where to send the output files.
    - **S3Uri** *(string) --***[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output file.
      When the topic detection job is finished, the service creates an output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
    """


_ClientStartDocumentClassificationJobResponseTypeDef = TypedDict(
    "_ClientStartDocumentClassificationJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)


class ClientStartDocumentClassificationJobResponseTypeDef(
    _ClientStartDocumentClassificationJobResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier generated for the job. To get the status of the job, use this identifier with
        the operation.
    """


_RequiredClientStartDocumentClassificationJobVpcConfigTypeDef = TypedDict(
    "_RequiredClientStartDocumentClassificationJobVpcConfigTypeDef", {"SecurityGroupIds": List[str]}
)
_OptionalClientStartDocumentClassificationJobVpcConfigTypeDef = TypedDict(
    "_OptionalClientStartDocumentClassificationJobVpcConfigTypeDef",
    {"Subnets": List[str]},
    total=False,
)


class ClientStartDocumentClassificationJobVpcConfigTypeDef(
    _RequiredClientStartDocumentClassificationJobVpcConfigTypeDef,
    _OptionalClientStartDocumentClassificationJobVpcConfigTypeDef,
):
    """
    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your document classification job. For more information, see `Amazon
    VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .
    - **SecurityGroupIds** *(list) --***[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .
      - *(string) --*
    """


_RequiredClientStartDominantLanguageDetectionJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartDominantLanguageDetectionJobInputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartDominantLanguageDetectionJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartDominantLanguageDetectionJobInputDataConfigTypeDef",
    {"InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientStartDominantLanguageDetectionJobInputDataConfigTypeDef(
    _RequiredClientStartDominantLanguageDetectionJobInputDataConfigTypeDef,
    _OptionalClientStartDominantLanguageDetectionJobInputDataConfigTypeDef,
):
    """
    Specifies the format and location of the input data for the job.
    - **S3Uri** *(string) --***[REQUIRED]**

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that
      you are calling. The URI can point to a single input file or it can provide the prefix for a
      collection of data files.
      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix,
      Amazon Comprehend uses all of them as input.
    """


_RequiredClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef",
    {"KmsKeyId": str},
    total=False,
)


class ClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef(
    _RequiredClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef,
    _OptionalClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef,
):
    """
    Specifies where to send the output files.
    - **S3Uri** *(string) --***[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output file.
      When the topic detection job is finished, the service creates an output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
    """


_ClientStartDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "_ClientStartDominantLanguageDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)


class ClientStartDominantLanguageDetectionJobResponseTypeDef(
    _ClientStartDominantLanguageDetectionJobResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier generated for the job. To get the status of a job, use this identifier with
        the operation.
    """


_RequiredClientStartDominantLanguageDetectionJobVpcConfigTypeDef = TypedDict(
    "_RequiredClientStartDominantLanguageDetectionJobVpcConfigTypeDef",
    {"SecurityGroupIds": List[str]},
)
_OptionalClientStartDominantLanguageDetectionJobVpcConfigTypeDef = TypedDict(
    "_OptionalClientStartDominantLanguageDetectionJobVpcConfigTypeDef",
    {"Subnets": List[str]},
    total=False,
)


class ClientStartDominantLanguageDetectionJobVpcConfigTypeDef(
    _RequiredClientStartDominantLanguageDetectionJobVpcConfigTypeDef,
    _OptionalClientStartDominantLanguageDetectionJobVpcConfigTypeDef,
):
    """
    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your dominant language detection job. For more information, see
    `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .
    - **SecurityGroupIds** *(list) --***[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .
      - *(string) --*
    """


_RequiredClientStartEntitiesDetectionJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartEntitiesDetectionJobInputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartEntitiesDetectionJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartEntitiesDetectionJobInputDataConfigTypeDef",
    {"InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientStartEntitiesDetectionJobInputDataConfigTypeDef(
    _RequiredClientStartEntitiesDetectionJobInputDataConfigTypeDef,
    _OptionalClientStartEntitiesDetectionJobInputDataConfigTypeDef,
):
    """
    Specifies the format and location of the input data for the job.
    - **S3Uri** *(string) --***[REQUIRED]**

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that
      you are calling. The URI can point to a single input file or it can provide the prefix for a
      collection of data files.
      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix,
      Amazon Comprehend uses all of them as input.
    """


_RequiredClientStartEntitiesDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartEntitiesDetectionJobOutputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartEntitiesDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartEntitiesDetectionJobOutputDataConfigTypeDef",
    {"KmsKeyId": str},
    total=False,
)


class ClientStartEntitiesDetectionJobOutputDataConfigTypeDef(
    _RequiredClientStartEntitiesDetectionJobOutputDataConfigTypeDef,
    _OptionalClientStartEntitiesDetectionJobOutputDataConfigTypeDef,
):
    """
    Specifies where to send the output files.
    - **S3Uri** *(string) --***[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output file.
      When the topic detection job is finished, the service creates an output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
    """


_ClientStartEntitiesDetectionJobResponseTypeDef = TypedDict(
    "_ClientStartEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)


class ClientStartEntitiesDetectionJobResponseTypeDef(
    _ClientStartEntitiesDetectionJobResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier generated for the job. To get the status of job, use this identifier with the
        operation.
    """


_RequiredClientStartEntitiesDetectionJobVpcConfigTypeDef = TypedDict(
    "_RequiredClientStartEntitiesDetectionJobVpcConfigTypeDef", {"SecurityGroupIds": List[str]}
)
_OptionalClientStartEntitiesDetectionJobVpcConfigTypeDef = TypedDict(
    "_OptionalClientStartEntitiesDetectionJobVpcConfigTypeDef", {"Subnets": List[str]}, total=False
)


class ClientStartEntitiesDetectionJobVpcConfigTypeDef(
    _RequiredClientStartEntitiesDetectionJobVpcConfigTypeDef,
    _OptionalClientStartEntitiesDetectionJobVpcConfigTypeDef,
):
    """
    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your entity detection job. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .
    - **SecurityGroupIds** *(list) --***[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .
      - *(string) --*
    """


_RequiredClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef",
    {"InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef(
    _RequiredClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef,
    _OptionalClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef,
):
    """
    Specifies the format and location of the input data for the job.
    - **S3Uri** *(string) --***[REQUIRED]**

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that
      you are calling. The URI can point to a single input file or it can provide the prefix for a
      collection of data files.
      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix,
      Amazon Comprehend uses all of them as input.
    """


_RequiredClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef",
    {"KmsKeyId": str},
    total=False,
)


class ClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef(
    _RequiredClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef,
    _OptionalClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef,
):
    """
    Specifies where to send the output files.
    - **S3Uri** *(string) --***[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output file.
      When the topic detection job is finished, the service creates an output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
    """


_ClientStartKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "_ClientStartKeyPhrasesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)


class ClientStartKeyPhrasesDetectionJobResponseTypeDef(
    _ClientStartKeyPhrasesDetectionJobResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier generated for the job. To get the status of a job, use this identifier with
        the operation.
    """


_RequiredClientStartKeyPhrasesDetectionJobVpcConfigTypeDef = TypedDict(
    "_RequiredClientStartKeyPhrasesDetectionJobVpcConfigTypeDef", {"SecurityGroupIds": List[str]}
)
_OptionalClientStartKeyPhrasesDetectionJobVpcConfigTypeDef = TypedDict(
    "_OptionalClientStartKeyPhrasesDetectionJobVpcConfigTypeDef",
    {"Subnets": List[str]},
    total=False,
)


class ClientStartKeyPhrasesDetectionJobVpcConfigTypeDef(
    _RequiredClientStartKeyPhrasesDetectionJobVpcConfigTypeDef,
    _OptionalClientStartKeyPhrasesDetectionJobVpcConfigTypeDef,
):
    """
    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your key phrases detection job. For more information, see `Amazon
    VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .
    - **SecurityGroupIds** *(list) --***[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .
      - *(string) --*
    """


_RequiredClientStartSentimentDetectionJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartSentimentDetectionJobInputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartSentimentDetectionJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartSentimentDetectionJobInputDataConfigTypeDef",
    {"InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientStartSentimentDetectionJobInputDataConfigTypeDef(
    _RequiredClientStartSentimentDetectionJobInputDataConfigTypeDef,
    _OptionalClientStartSentimentDetectionJobInputDataConfigTypeDef,
):
    """
    Specifies the format and location of the input data for the job.
    - **S3Uri** *(string) --***[REQUIRED]**

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that
      you are calling. The URI can point to a single input file or it can provide the prefix for a
      collection of data files.
      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix,
      Amazon Comprehend uses all of them as input.
    """


_RequiredClientStartSentimentDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartSentimentDetectionJobOutputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartSentimentDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartSentimentDetectionJobOutputDataConfigTypeDef",
    {"KmsKeyId": str},
    total=False,
)


class ClientStartSentimentDetectionJobOutputDataConfigTypeDef(
    _RequiredClientStartSentimentDetectionJobOutputDataConfigTypeDef,
    _OptionalClientStartSentimentDetectionJobOutputDataConfigTypeDef,
):
    """
    Specifies where to send the output files.
    - **S3Uri** *(string) --***[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output file.
      When the topic detection job is finished, the service creates an output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
    """


_ClientStartSentimentDetectionJobResponseTypeDef = TypedDict(
    "_ClientStartSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)


class ClientStartSentimentDetectionJobResponseTypeDef(
    _ClientStartSentimentDetectionJobResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier generated for the job. To get the status of a job, use this identifier with
        the operation.
    """


_RequiredClientStartSentimentDetectionJobVpcConfigTypeDef = TypedDict(
    "_RequiredClientStartSentimentDetectionJobVpcConfigTypeDef", {"SecurityGroupIds": List[str]}
)
_OptionalClientStartSentimentDetectionJobVpcConfigTypeDef = TypedDict(
    "_OptionalClientStartSentimentDetectionJobVpcConfigTypeDef", {"Subnets": List[str]}, total=False
)


class ClientStartSentimentDetectionJobVpcConfigTypeDef(
    _RequiredClientStartSentimentDetectionJobVpcConfigTypeDef,
    _OptionalClientStartSentimentDetectionJobVpcConfigTypeDef,
):
    """
    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your sentiment detection job. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .
    - **SecurityGroupIds** *(list) --***[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .
      - *(string) --*
    """


_RequiredClientStartTopicsDetectionJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartTopicsDetectionJobInputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartTopicsDetectionJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartTopicsDetectionJobInputDataConfigTypeDef",
    {"InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ClientStartTopicsDetectionJobInputDataConfigTypeDef(
    _RequiredClientStartTopicsDetectionJobInputDataConfigTypeDef,
    _OptionalClientStartTopicsDetectionJobInputDataConfigTypeDef,
):
    """
    Specifies the format and location of the input data for the job.
    - **S3Uri** *(string) --***[REQUIRED]**

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that
      you are calling. The URI can point to a single input file or it can provide the prefix for a
      collection of data files.
      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix,
      Amazon Comprehend uses all of them as input.
    """


_RequiredClientStartTopicsDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartTopicsDetectionJobOutputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartTopicsDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartTopicsDetectionJobOutputDataConfigTypeDef", {"KmsKeyId": str}, total=False
)


class ClientStartTopicsDetectionJobOutputDataConfigTypeDef(
    _RequiredClientStartTopicsDetectionJobOutputDataConfigTypeDef,
    _OptionalClientStartTopicsDetectionJobOutputDataConfigTypeDef,
):
    """
    Specifies where to send the output files. The output is a compressed archive with two files,
    ``topic-terms.csv`` that lists the terms associated with each topic, and ``doc-topics.csv`` that
    lists the documents associated with each topic
    - **S3Uri** *(string) --***[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output file.
      When the topic detection job is finished, the service creates an output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
    """


_ClientStartTopicsDetectionJobResponseTypeDef = TypedDict(
    "_ClientStartTopicsDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)


class ClientStartTopicsDetectionJobResponseTypeDef(_ClientStartTopicsDetectionJobResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier generated for the job. To get the status of the job, use this identifier with
        the ``DescribeTopicDetectionJob`` operation.
    """


_RequiredClientStartTopicsDetectionJobVpcConfigTypeDef = TypedDict(
    "_RequiredClientStartTopicsDetectionJobVpcConfigTypeDef", {"SecurityGroupIds": List[str]}
)
_OptionalClientStartTopicsDetectionJobVpcConfigTypeDef = TypedDict(
    "_OptionalClientStartTopicsDetectionJobVpcConfigTypeDef", {"Subnets": List[str]}, total=False
)


class ClientStartTopicsDetectionJobVpcConfigTypeDef(
    _RequiredClientStartTopicsDetectionJobVpcConfigTypeDef,
    _OptionalClientStartTopicsDetectionJobVpcConfigTypeDef,
):
    """
    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your topic detection job. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .
    - **SecurityGroupIds** *(list) --***[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .
      - *(string) --*
    """


_ClientStopDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "_ClientStopDominantLanguageDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)


class ClientStopDominantLanguageDetectionJobResponseTypeDef(
    _ClientStopDominantLanguageDetectionJobResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier of the dominant language detection job to stop.
    """


_ClientStopEntitiesDetectionJobResponseTypeDef = TypedDict(
    "_ClientStopEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)


class ClientStopEntitiesDetectionJobResponseTypeDef(_ClientStopEntitiesDetectionJobResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier of the entities detection job to stop.
    """


_ClientStopKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "_ClientStopKeyPhrasesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)


class ClientStopKeyPhrasesDetectionJobResponseTypeDef(
    _ClientStopKeyPhrasesDetectionJobResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier of the key phrases detection job to stop.
    """


_ClientStopSentimentDetectionJobResponseTypeDef = TypedDict(
    "_ClientStopSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)


class ClientStopSentimentDetectionJobResponseTypeDef(
    _ClientStopSentimentDetectionJobResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier of the sentiment detection job to stop.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example,
      a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource to indicate
      its use by a particular department.
      - **Key** *(string) --***[REQUIRED]**

        The initial part of a key-value pair that forms a tag associated with a given resource. For
        instance, if you want to show which resources are used by which departments, you might use
        “Department” as the key portion of the pair, with multiple possible values such as “sales,”
        “legal,” and “administration.”
    """


_ListDocumentClassificationJobsPaginateFilterTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginateFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListDocumentClassificationJobsPaginateFilterTypeDef(
    _ListDocumentClassificationJobsPaginateFilterTypeDef
):
    """
    Filters the jobs that are returned. You can filter jobs on their names, status, or the date and
    time that they were submitted. You can only set one filter at a time.
    - **JobName** *(string) --*

      Filters on the name of the job.
    """


_ListDocumentClassificationJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDocumentClassificationJobsPaginatePaginationConfigTypeDef(
    _ListDocumentClassificationJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef(
    _ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef
):
    pass


_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef(
    _ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef(
    _ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef
):
    pass


_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "DocumentClassifierArn": str,
        "InputDataConfig": ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef(
    _ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a document classification job.
      - **JobId** *(string) --*

        The identifier assigned to the document classification job.
    """


_ListDocumentClassificationJobsPaginateResponseTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginateResponseTypeDef",
    {
        "DocumentClassificationJobPropertiesList": List[
            ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListDocumentClassificationJobsPaginateResponseTypeDef(
    _ListDocumentClassificationJobsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **DocumentClassificationJobPropertiesList** *(list) --*

        A list containing the properties of each job returned.
        - *(dict) --*

          Provides information about a document classification job.
          - **JobId** *(string) --*

            The identifier assigned to the document classification job.
    """


_ListDocumentClassifiersPaginateFilterTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateFilterTypeDef",
    {
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListDocumentClassifiersPaginateFilterTypeDef(_ListDocumentClassifiersPaginateFilterTypeDef):
    """
    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.
    - **Status** *(string) --*

      Filters the list of classifiers based on status.
    """


_ListDocumentClassifiersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDocumentClassifiersPaginatePaginationConfigTypeDef(
    _ListDocumentClassifiersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef",
    {"Accuracy": float, "Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef(
    _ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef
):
    pass


_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef",
    {
        "NumberOfLabels": int,
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef,
    },
    total=False,
)


class ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef(
    _ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef
):
    pass


_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str},
    total=False,
)


class ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef(
    _ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef
):
    pass


_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef(
    _ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef
):
    pass


_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef(
    _ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef
):
    pass


_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef",
    {
        "DocumentClassifierArn": str,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef,
        "ClassifierMetadata": ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef(
    _ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a document classifier.
      - **DocumentClassifierArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the document classifier.
    """


_ListDocumentClassifiersPaginateResponseTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseTypeDef",
    {
        "DocumentClassifierPropertiesList": List[
            ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListDocumentClassifiersPaginateResponseTypeDef(
    _ListDocumentClassifiersPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **DocumentClassifierPropertiesList** *(list) --*

        A list containing the properties of each job returned.
        - *(dict) --*

          Provides information about a document classifier.
          - **DocumentClassifierArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the document classifier.
    """


_ListDominantLanguageDetectionJobsPaginateFilterTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginateFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListDominantLanguageDetectionJobsPaginateFilterTypeDef(
    _ListDominantLanguageDetectionJobsPaginateFilterTypeDef
):
    """
    Filters that jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.
    - **JobName** *(string) --*

      Filters on the name of the job.
    """


_ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef(
    _ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef(
    _ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef
):
    pass


_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef(
    _ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef
):
    pass


_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef(
    _ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a dominant language detection job.
      - **JobId** *(string) --*

        The identifier assigned to the dominant language detection job.
    """


_ListDominantLanguageDetectionJobsPaginateResponseTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginateResponseTypeDef",
    {
        "DominantLanguageDetectionJobPropertiesList": List[
            ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListDominantLanguageDetectionJobsPaginateResponseTypeDef(
    _ListDominantLanguageDetectionJobsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **DominantLanguageDetectionJobPropertiesList** *(list) --*

        A list containing the properties of each job that is returned.
        - *(dict) --*

          Provides information about a dominant language detection job.
          - **JobId** *(string) --*

            The identifier assigned to the dominant language detection job.
    """


_ListEntitiesDetectionJobsPaginateFilterTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginateFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListEntitiesDetectionJobsPaginateFilterTypeDef(
    _ListEntitiesDetectionJobsPaginateFilterTypeDef
):
    """
    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.
    - **JobName** *(string) --*

      Filters on the name of the job.
    """


_ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef(
    _ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef(
    _ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef
):
    pass


_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef(
    _ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef
):
    pass


_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "EntityRecognizerArn": str,
        "InputDataConfig": ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef(
    _ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about an entities detection job.
      - **JobId** *(string) --*

        The identifier assigned to the entities detection job.
    """


_ListEntitiesDetectionJobsPaginateResponseTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginateResponseTypeDef",
    {
        "EntitiesDetectionJobPropertiesList": List[
            ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListEntitiesDetectionJobsPaginateResponseTypeDef(
    _ListEntitiesDetectionJobsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **EntitiesDetectionJobPropertiesList** *(list) --*

        A list containing the properties of each job that is returned.
        - *(dict) --*

          Provides information about an entities detection job.
          - **JobId** *(string) --*

            The identifier assigned to the entities detection job.
    """


_ListEntityRecognizersPaginateFilterTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateFilterTypeDef",
    {
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListEntityRecognizersPaginateFilterTypeDef(_ListEntityRecognizersPaginateFilterTypeDef):
    """
    Filters the list of entities returned. You can filter on ``Status`` , ``SubmitTimeBefore`` , or
    ``SubmitTimeAfter`` . You can only set one filter at a time.
    - **Status** *(string) --*

      The status of an entity recognizer.
    """


_ListEntityRecognizersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEntityRecognizersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEntityRecognizersPaginatePaginationConfigTypeDef(
    _ListEntityRecognizersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef",
    {"S3Uri": str},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef
):
    pass


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef",
    {"S3Uri": str},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef
):
    pass


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef",
    {"S3Uri": str},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef
):
    pass


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef",
    {"Type": str},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef
):
    pass


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef",
    {
        "EntityTypes": List[
            ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef
        ],
        "Documents": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef,
        "Annotations": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef,
        "EntityList": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef,
    },
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef
):
    pass


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef
):
    pass


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef",
    {
        "Type": str,
        "EvaluationMetrics": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef,
        "NumberOfTrainMentions": int,
    },
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef
):
    pass


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef
):
    pass


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef",
    {
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef,
        "EntityTypes": List[
            ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef
        ],
    },
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef
):
    pass


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef
):
    pass


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef",
    {
        "EntityRecognizerArn": str,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef,
        "RecognizerMetadata": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef
):
    """
    - *(dict) --*

      Describes information about an entity recognizer.
      - **EntityRecognizerArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the entity recognizer.
    """


_ListEntityRecognizersPaginateResponseTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseTypeDef",
    {
        "EntityRecognizerPropertiesList": List[
            ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListEntityRecognizersPaginateResponseTypeDef(_ListEntityRecognizersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **EntityRecognizerPropertiesList** *(list) --*

        The list of properties of an entity recognizer.
        - *(dict) --*

          Describes information about an entity recognizer.
          - **EntityRecognizerArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the entity recognizer.
    """


_ListKeyPhrasesDetectionJobsPaginateFilterTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginateFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginateFilterTypeDef(
    _ListKeyPhrasesDetectionJobsPaginateFilterTypeDef
):
    """
    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.
    - **JobName** *(string) --*

      Filters on the name of the job.
    """


_ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef(
    _ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef(
    _ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef
):
    pass


_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef(
    _ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef
):
    pass


_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef(
    _ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a key phrases detection job.
      - **JobId** *(string) --*

        The identifier assigned to the key phrases detection job.
    """


_ListKeyPhrasesDetectionJobsPaginateResponseTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginateResponseTypeDef",
    {
        "KeyPhrasesDetectionJobPropertiesList": List[
            ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginateResponseTypeDef(
    _ListKeyPhrasesDetectionJobsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **KeyPhrasesDetectionJobPropertiesList** *(list) --*

        A list containing the properties of each job that is returned.
        - *(dict) --*

          Provides information about a key phrases detection job.
          - **JobId** *(string) --*

            The identifier assigned to the key phrases detection job.
    """


_ListSentimentDetectionJobsPaginateFilterTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginateFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListSentimentDetectionJobsPaginateFilterTypeDef(
    _ListSentimentDetectionJobsPaginateFilterTypeDef
):
    """
    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.
    - **JobName** *(string) --*

      Filters on the name of the job.
    """


_ListSentimentDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSentimentDetectionJobsPaginatePaginationConfigTypeDef(
    _ListSentimentDetectionJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef(
    _ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef
):
    pass


_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef(
    _ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef
):
    pass


_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef(
    _ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a sentiment detection job.
      - **JobId** *(string) --*

        The identifier assigned to the sentiment detection job.
    """


_ListSentimentDetectionJobsPaginateResponseTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginateResponseTypeDef",
    {
        "SentimentDetectionJobPropertiesList": List[
            ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListSentimentDetectionJobsPaginateResponseTypeDef(
    _ListSentimentDetectionJobsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **SentimentDetectionJobPropertiesList** *(list) --*

        A list containing the properties of each job that is returned.
        - *(dict) --*

          Provides information about a sentiment detection job.
          - **JobId** *(string) --*

            The identifier assigned to the sentiment detection job.
    """


_ListTopicsDetectionJobsPaginateFilterTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginateFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListTopicsDetectionJobsPaginateFilterTypeDef(_ListTopicsDetectionJobsPaginateFilterTypeDef):
    """
    Filters the jobs that are returned. Jobs can be filtered on their name, status, or the date and
    time that they were submitted. You can set only one filter at a time.
    - **JobName** *(string) --*
    - **JobStatus** *(string) --*

      Filters the list of topic detection jobs based on job status. Returns only jobs with the
      specified status.
    """


_ListTopicsDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTopicsDetectionJobsPaginatePaginationConfigTypeDef(
    _ListTopicsDetectionJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)


class ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef(
    _ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef
):
    pass


_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef(
    _ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef
):
    pass


_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef,
        "NumberOfTopics": int,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef(
    _ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a topic detection job.
      - **JobId** *(string) --*

        The identifier assigned to the topic detection job.
    """


_ListTopicsDetectionJobsPaginateResponseTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginateResponseTypeDef",
    {
        "TopicsDetectionJobPropertiesList": List[
            ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListTopicsDetectionJobsPaginateResponseTypeDef(
    _ListTopicsDetectionJobsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **TopicsDetectionJobPropertiesList** *(list) --*

        A list containing the properties of each job that is returned.
        - *(dict) --*

          Provides information about a topic detection job.
          - **JobId** *(string) --*

            The identifier assigned to the topic detection job.
    """
