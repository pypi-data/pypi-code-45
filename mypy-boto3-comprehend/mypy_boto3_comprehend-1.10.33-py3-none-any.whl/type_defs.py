"Main interface for comprehend service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientBatchDetectDominantLanguageResponseErrorListTypeDef = TypedDict(
    "ClientBatchDetectDominantLanguageResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef = TypedDict(
    "ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef",
    {"LanguageCode": str, "Score": Any},
    total=False,
)

ClientBatchDetectDominantLanguageResponseResultListTypeDef = TypedDict(
    "ClientBatchDetectDominantLanguageResponseResultListTypeDef",
    {
        "Index": int,
        "Languages": List[ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef],
    },
    total=False,
)

ClientBatchDetectDominantLanguageResponseTypeDef = TypedDict(
    "ClientBatchDetectDominantLanguageResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectDominantLanguageResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectDominantLanguageResponseErrorListTypeDef],
    },
    total=False,
)

ClientBatchDetectEntitiesResponseErrorListTypeDef = TypedDict(
    "ClientBatchDetectEntitiesResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef = TypedDict(
    "ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef",
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

ClientBatchDetectEntitiesResponseResultListTypeDef = TypedDict(
    "ClientBatchDetectEntitiesResponseResultListTypeDef",
    {"Index": int, "Entities": List[ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef]},
    total=False,
)

ClientBatchDetectEntitiesResponseTypeDef = TypedDict(
    "ClientBatchDetectEntitiesResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectEntitiesResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectEntitiesResponseErrorListTypeDef],
    },
    total=False,
)

ClientBatchDetectKeyPhrasesResponseErrorListTypeDef = TypedDict(
    "ClientBatchDetectKeyPhrasesResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef = TypedDict(
    "ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef",
    {"Score": Any, "Text": str, "BeginOffset": int, "EndOffset": int},
    total=False,
)

ClientBatchDetectKeyPhrasesResponseResultListTypeDef = TypedDict(
    "ClientBatchDetectKeyPhrasesResponseResultListTypeDef",
    {
        "Index": int,
        "KeyPhrases": List[ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef],
    },
    total=False,
)

ClientBatchDetectKeyPhrasesResponseTypeDef = TypedDict(
    "ClientBatchDetectKeyPhrasesResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectKeyPhrasesResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectKeyPhrasesResponseErrorListTypeDef],
    },
    total=False,
)

ClientBatchDetectSentimentResponseErrorListTypeDef = TypedDict(
    "ClientBatchDetectSentimentResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef = TypedDict(
    "ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef",
    {"Positive": Any, "Negative": Any, "Neutral": Any, "Mixed": Any},
    total=False,
)

ClientBatchDetectSentimentResponseResultListTypeDef = TypedDict(
    "ClientBatchDetectSentimentResponseResultListTypeDef",
    {
        "Index": int,
        "Sentiment": Literal["POSITIVE", "NEGATIVE", "NEUTRAL", "MIXED"],
        "SentimentScore": ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef,
    },
    total=False,
)

ClientBatchDetectSentimentResponseTypeDef = TypedDict(
    "ClientBatchDetectSentimentResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectSentimentResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectSentimentResponseErrorListTypeDef],
    },
    total=False,
)

ClientBatchDetectSyntaxResponseErrorListTypeDef = TypedDict(
    "ClientBatchDetectSyntaxResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef = TypedDict(
    "ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef",
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

ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef = TypedDict(
    "ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef",
    {
        "TokenId": int,
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
        "PartOfSpeech": ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef,
    },
    total=False,
)

ClientBatchDetectSyntaxResponseResultListTypeDef = TypedDict(
    "ClientBatchDetectSyntaxResponseResultListTypeDef",
    {
        "Index": int,
        "SyntaxTokens": List[ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef],
    },
    total=False,
)

ClientBatchDetectSyntaxResponseTypeDef = TypedDict(
    "ClientBatchDetectSyntaxResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectSyntaxResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectSyntaxResponseErrorListTypeDef],
    },
    total=False,
)

ClientClassifyDocumentResponseClassesTypeDef = TypedDict(
    "ClientClassifyDocumentResponseClassesTypeDef", {"Name": str, "Score": Any}, total=False
)

ClientClassifyDocumentResponseTypeDef = TypedDict(
    "ClientClassifyDocumentResponseTypeDef",
    {"Classes": List[ClientClassifyDocumentResponseClassesTypeDef]},
    total=False,
)

ClientCreateDocumentClassifierInputDataConfigTypeDef = TypedDict(
    "ClientCreateDocumentClassifierInputDataConfigTypeDef", {"S3Uri": str}
)

ClientCreateDocumentClassifierOutputDataConfigTypeDef = TypedDict(
    "ClientCreateDocumentClassifierOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientCreateDocumentClassifierResponseTypeDef = TypedDict(
    "ClientCreateDocumentClassifierResponseTypeDef", {"DocumentClassifierArn": str}, total=False
)

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
    pass


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
    pass


ClientCreateEndpointResponseTypeDef = TypedDict(
    "ClientCreateEndpointResponseTypeDef", {"EndpointArn": str}, total=False
)

_RequiredClientCreateEndpointTagsTypeDef = TypedDict(
    "_RequiredClientCreateEndpointTagsTypeDef", {"Key": str}
)
_OptionalClientCreateEndpointTagsTypeDef = TypedDict(
    "_OptionalClientCreateEndpointTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateEndpointTagsTypeDef(
    _RequiredClientCreateEndpointTagsTypeDef, _OptionalClientCreateEndpointTagsTypeDef
):
    pass


ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef = TypedDict(
    "ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef", {"S3Uri": str}, total=False
)

ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef = TypedDict(
    "ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef", {"S3Uri": str}, total=False
)

ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef = TypedDict(
    "ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef", {"S3Uri": str}, total=False
)

ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef = TypedDict(
    "ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef", {"Type": str}
)

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
    pass


ClientCreateEntityRecognizerResponseTypeDef = TypedDict(
    "ClientCreateEntityRecognizerResponseTypeDef", {"EntityRecognizerArn": str}, total=False
)

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
    pass


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
    pass


ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef = TypedDict(
    "ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef = TypedDict(
    "ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef = TypedDict(
    "ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef",
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

ClientDescribeDocumentClassificationJobResponseTypeDef = TypedDict(
    "ClientDescribeDocumentClassificationJobResponseTypeDef",
    {
        "DocumentClassificationJobProperties": ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef
    },
    total=False,
)

ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef = TypedDict(
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef",
    {"Accuracy": float, "Precision": float, "Recall": float, "F1Score": float},
    total=False,
)

ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef = TypedDict(
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef",
    {
        "NumberOfLabels": int,
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef,
    },
    total=False,
)

ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef = TypedDict(
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef = TypedDict(
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef = TypedDict(
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef",
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

ClientDescribeDocumentClassifierResponseTypeDef = TypedDict(
    "ClientDescribeDocumentClassifierResponseTypeDef",
    {
        "DocumentClassifierProperties": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef
    },
    total=False,
)

ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef = TypedDict(
    "ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef",
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

ClientDescribeDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "ClientDescribeDominantLanguageDetectionJobResponseTypeDef",
    {
        "DominantLanguageDetectionJobProperties": ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef
    },
    total=False,
)

ClientDescribeEndpointResponseEndpointPropertiesTypeDef = TypedDict(
    "ClientDescribeEndpointResponseEndpointPropertiesTypeDef",
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

ClientDescribeEndpointResponseTypeDef = TypedDict(
    "ClientDescribeEndpointResponseTypeDef",
    {"EndpointProperties": ClientDescribeEndpointResponseEndpointPropertiesTypeDef},
    total=False,
)

ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef = TypedDict(
    "ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef",
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

ClientDescribeEntitiesDetectionJobResponseTypeDef = TypedDict(
    "ClientDescribeEntitiesDetectionJobResponseTypeDef",
    {
        "EntitiesDetectionJobProperties": ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef
    },
    total=False,
)

ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef = TypedDict(
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef = TypedDict(
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef = TypedDict(
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef = TypedDict(
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef",
    {"Type": str},
    total=False,
)

ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef = TypedDict(
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef",
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

ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef = TypedDict(
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)

ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef = TypedDict(
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef",
    {
        "Type": str,
        "EvaluationMetrics": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef,
        "NumberOfTrainMentions": int,
    },
    total=False,
)

ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef = TypedDict(
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)

ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef = TypedDict(
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef",
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

ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef = TypedDict(
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef = TypedDict(
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef",
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

ClientDescribeEntityRecognizerResponseTypeDef = TypedDict(
    "ClientDescribeEntityRecognizerResponseTypeDef",
    {
        "EntityRecognizerProperties": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef
    },
    total=False,
)

ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef = TypedDict(
    "ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef",
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

ClientDescribeKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "ClientDescribeKeyPhrasesDetectionJobResponseTypeDef",
    {
        "KeyPhrasesDetectionJobProperties": ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef
    },
    total=False,
)

ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef = TypedDict(
    "ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef",
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

ClientDescribeSentimentDetectionJobResponseTypeDef = TypedDict(
    "ClientDescribeSentimentDetectionJobResponseTypeDef",
    {
        "SentimentDetectionJobProperties": ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef
    },
    total=False,
)

ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef = TypedDict(
    "ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef",
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

ClientDescribeTopicsDetectionJobResponseTypeDef = TypedDict(
    "ClientDescribeTopicsDetectionJobResponseTypeDef",
    {
        "TopicsDetectionJobProperties": ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef
    },
    total=False,
)

ClientDetectDominantLanguageResponseLanguagesTypeDef = TypedDict(
    "ClientDetectDominantLanguageResponseLanguagesTypeDef",
    {"LanguageCode": str, "Score": Any},
    total=False,
)

ClientDetectDominantLanguageResponseTypeDef = TypedDict(
    "ClientDetectDominantLanguageResponseTypeDef",
    {"Languages": List[ClientDetectDominantLanguageResponseLanguagesTypeDef]},
    total=False,
)

ClientDetectEntitiesResponseEntitiesTypeDef = TypedDict(
    "ClientDetectEntitiesResponseEntitiesTypeDef",
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

ClientDetectEntitiesResponseTypeDef = TypedDict(
    "ClientDetectEntitiesResponseTypeDef",
    {"Entities": List[ClientDetectEntitiesResponseEntitiesTypeDef]},
    total=False,
)

ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef = TypedDict(
    "ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef",
    {"Score": float, "Text": str, "BeginOffset": int, "EndOffset": int},
    total=False,
)

ClientDetectKeyPhrasesResponseTypeDef = TypedDict(
    "ClientDetectKeyPhrasesResponseTypeDef",
    {"KeyPhrases": List[ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef]},
    total=False,
)

ClientDetectSentimentResponseSentimentScoreTypeDef = TypedDict(
    "ClientDetectSentimentResponseSentimentScoreTypeDef",
    {"Positive": Any, "Negative": Any, "Neutral": Any, "Mixed": Any},
    total=False,
)

ClientDetectSentimentResponseTypeDef = TypedDict(
    "ClientDetectSentimentResponseTypeDef",
    {
        "Sentiment": Literal["POSITIVE", "NEGATIVE", "NEUTRAL", "MIXED"],
        "SentimentScore": ClientDetectSentimentResponseSentimentScoreTypeDef,
    },
    total=False,
)

ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef = TypedDict(
    "ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef",
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

ClientDetectSyntaxResponseSyntaxTokensTypeDef = TypedDict(
    "ClientDetectSyntaxResponseSyntaxTokensTypeDef",
    {
        "TokenId": int,
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
        "PartOfSpeech": ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef,
    },
    total=False,
)

ClientDetectSyntaxResponseTypeDef = TypedDict(
    "ClientDetectSyntaxResponseTypeDef",
    {"SyntaxTokens": List[ClientDetectSyntaxResponseSyntaxTokensTypeDef]},
    total=False,
)

ClientListDocumentClassificationJobsFilterTypeDef = TypedDict(
    "ClientListDocumentClassificationJobsFilterTypeDef",
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

ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef = TypedDict(
    "ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef = TypedDict(
    "ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef",
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

ClientListDocumentClassificationJobsResponseTypeDef = TypedDict(
    "ClientListDocumentClassificationJobsResponseTypeDef",
    {
        "DocumentClassificationJobPropertiesList": List[
            ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListDocumentClassifiersFilterTypeDef = TypedDict(
    "ClientListDocumentClassifiersFilterTypeDef",
    {
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef = TypedDict(
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef",
    {"Accuracy": float, "Precision": float, "Recall": float, "F1Score": float},
    total=False,
)

ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef = TypedDict(
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef",
    {
        "NumberOfLabels": int,
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef,
    },
    total=False,
)

ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef = TypedDict(
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef = TypedDict(
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef = TypedDict(
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef",
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

ClientListDocumentClassifiersResponseTypeDef = TypedDict(
    "ClientListDocumentClassifiersResponseTypeDef",
    {
        "DocumentClassifierPropertiesList": List[
            ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListDominantLanguageDetectionJobsFilterTypeDef = TypedDict(
    "ClientListDominantLanguageDetectionJobsFilterTypeDef",
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

ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef = TypedDict(
    "ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef",
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

ClientListDominantLanguageDetectionJobsResponseTypeDef = TypedDict(
    "ClientListDominantLanguageDetectionJobsResponseTypeDef",
    {
        "DominantLanguageDetectionJobPropertiesList": List[
            ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListEndpointsFilterTypeDef = TypedDict(
    "ClientListEndpointsFilterTypeDef",
    {
        "ModelArn": str,
        "Status": Literal["CREATING", "DELETING", "FAILED", "IN_SERVICE", "UPDATING"],
        "CreationTimeBefore": datetime,
        "CreationTimeAfter": datetime,
    },
    total=False,
)

ClientListEndpointsResponseEndpointPropertiesListTypeDef = TypedDict(
    "ClientListEndpointsResponseEndpointPropertiesListTypeDef",
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

ClientListEndpointsResponseTypeDef = TypedDict(
    "ClientListEndpointsResponseTypeDef",
    {
        "EndpointPropertiesList": List[ClientListEndpointsResponseEndpointPropertiesListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListEntitiesDetectionJobsFilterTypeDef = TypedDict(
    "ClientListEntitiesDetectionJobsFilterTypeDef",
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

ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef = TypedDict(
    "ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef",
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

ClientListEntitiesDetectionJobsResponseTypeDef = TypedDict(
    "ClientListEntitiesDetectionJobsResponseTypeDef",
    {
        "EntitiesDetectionJobPropertiesList": List[
            ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListEntityRecognizersFilterTypeDef = TypedDict(
    "ClientListEntityRecognizersFilterTypeDef",
    {
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef = TypedDict(
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef = TypedDict(
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef = TypedDict(
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef = TypedDict(
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef",
    {"Type": str},
    total=False,
)

ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef = TypedDict(
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef",
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

ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef = TypedDict(
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)

ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef = TypedDict(
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef",
    {
        "Type": str,
        "EvaluationMetrics": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef,
        "NumberOfTrainMentions": int,
    },
    total=False,
)

ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef = TypedDict(
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)

ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef = TypedDict(
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef",
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

ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef = TypedDict(
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef = TypedDict(
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef",
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

ClientListEntityRecognizersResponseTypeDef = TypedDict(
    "ClientListEntityRecognizersResponseTypeDef",
    {
        "EntityRecognizerPropertiesList": List[
            ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListKeyPhrasesDetectionJobsFilterTypeDef = TypedDict(
    "ClientListKeyPhrasesDetectionJobsFilterTypeDef",
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

ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef = TypedDict(
    "ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef",
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

ClientListKeyPhrasesDetectionJobsResponseTypeDef = TypedDict(
    "ClientListKeyPhrasesDetectionJobsResponseTypeDef",
    {
        "KeyPhrasesDetectionJobPropertiesList": List[
            ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListSentimentDetectionJobsFilterTypeDef = TypedDict(
    "ClientListSentimentDetectionJobsFilterTypeDef",
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

ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef = TypedDict(
    "ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef",
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

ClientListSentimentDetectionJobsResponseTypeDef = TypedDict(
    "ClientListSentimentDetectionJobsResponseTypeDef",
    {
        "SentimentDetectionJobPropertiesList": List[
            ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"ResourceArn": str, "Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

ClientListTopicsDetectionJobsFilterTypeDef = TypedDict(
    "ClientListTopicsDetectionJobsFilterTypeDef",
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

ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef = TypedDict(
    "ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef",
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

ClientListTopicsDetectionJobsResponseTypeDef = TypedDict(
    "ClientListTopicsDetectionJobsResponseTypeDef",
    {
        "TopicsDetectionJobPropertiesList": List[
            ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

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
    pass


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
    pass


ClientStartDocumentClassificationJobResponseTypeDef = TypedDict(
    "ClientStartDocumentClassificationJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)

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
    pass


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
    pass


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
    pass


ClientStartDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "ClientStartDominantLanguageDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)

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
    pass


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
    pass


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
    pass


ClientStartEntitiesDetectionJobResponseTypeDef = TypedDict(
    "ClientStartEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)

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
    pass


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
    pass


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
    pass


ClientStartKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "ClientStartKeyPhrasesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)

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
    pass


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
    pass


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
    pass


ClientStartSentimentDetectionJobResponseTypeDef = TypedDict(
    "ClientStartSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)

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
    pass


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
    pass


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
    pass


ClientStartTopicsDetectionJobResponseTypeDef = TypedDict(
    "ClientStartTopicsDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)

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
    pass


ClientStopDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "ClientStopDominantLanguageDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)

ClientStopEntitiesDetectionJobResponseTypeDef = TypedDict(
    "ClientStopEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)

ClientStopKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "ClientStopKeyPhrasesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)

ClientStopSentimentDetectionJobResponseTypeDef = TypedDict(
    "ClientStopSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED", "STOP_REQUESTED", "STOPPED"
        ],
    },
    total=False,
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ListDocumentClassificationJobsPaginateFilterTypeDef = TypedDict(
    "ListDocumentClassificationJobsPaginateFilterTypeDef",
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

ListDocumentClassificationJobsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDocumentClassificationJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef = TypedDict(
    "ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef = TypedDict(
    "ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef",
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

ListDocumentClassificationJobsPaginateResponseTypeDef = TypedDict(
    "ListDocumentClassificationJobsPaginateResponseTypeDef",
    {
        "DocumentClassificationJobPropertiesList": List[
            ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef
        ]
    },
    total=False,
)

ListDocumentClassifiersPaginateFilterTypeDef = TypedDict(
    "ListDocumentClassifiersPaginateFilterTypeDef",
    {
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

ListDocumentClassifiersPaginatePaginationConfigTypeDef = TypedDict(
    "ListDocumentClassifiersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef = TypedDict(
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef",
    {"Accuracy": float, "Precision": float, "Recall": float, "F1Score": float},
    total=False,
)

ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef = TypedDict(
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef",
    {
        "NumberOfLabels": int,
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef,
    },
    total=False,
)

ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef = TypedDict(
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str},
    total=False,
)

ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef = TypedDict(
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef = TypedDict(
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef",
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

ListDocumentClassifiersPaginateResponseTypeDef = TypedDict(
    "ListDocumentClassifiersPaginateResponseTypeDef",
    {
        "DocumentClassifierPropertiesList": List[
            ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef
        ]
    },
    total=False,
)

ListDominantLanguageDetectionJobsPaginateFilterTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsPaginateFilterTypeDef",
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

ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef",
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

ListDominantLanguageDetectionJobsPaginateResponseTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsPaginateResponseTypeDef",
    {
        "DominantLanguageDetectionJobPropertiesList": List[
            ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)

ListEntitiesDetectionJobsPaginateFilterTypeDef = TypedDict(
    "ListEntitiesDetectionJobsPaginateFilterTypeDef",
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

ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef = TypedDict(
    "ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef",
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

ListEntitiesDetectionJobsPaginateResponseTypeDef = TypedDict(
    "ListEntitiesDetectionJobsPaginateResponseTypeDef",
    {
        "EntitiesDetectionJobPropertiesList": List[
            ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)

ListEntityRecognizersPaginateFilterTypeDef = TypedDict(
    "ListEntityRecognizersPaginateFilterTypeDef",
    {
        "Status": Literal[
            "SUBMITTED", "TRAINING", "DELETING", "STOP_REQUESTED", "STOPPED", "IN_ERROR", "TRAINED"
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

ListEntityRecognizersPaginatePaginationConfigTypeDef = TypedDict(
    "ListEntityRecognizersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef = TypedDict(
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef",
    {"S3Uri": str},
    total=False,
)

ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef = TypedDict(
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef",
    {"S3Uri": str},
    total=False,
)

ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef = TypedDict(
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef",
    {"S3Uri": str},
    total=False,
)

ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef = TypedDict(
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef",
    {"Type": str},
    total=False,
)

ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef = TypedDict(
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef",
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

ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef = TypedDict(
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)

ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef = TypedDict(
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef",
    {
        "Type": str,
        "EvaluationMetrics": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef,
        "NumberOfTrainMentions": int,
    },
    total=False,
)

ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef = TypedDict(
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)

ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef = TypedDict(
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef",
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

ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef = TypedDict(
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef = TypedDict(
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef",
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

ListEntityRecognizersPaginateResponseTypeDef = TypedDict(
    "ListEntityRecognizersPaginateResponseTypeDef",
    {
        "EntityRecognizerPropertiesList": List[
            ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef
        ]
    },
    total=False,
)

ListKeyPhrasesDetectionJobsPaginateFilterTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsPaginateFilterTypeDef",
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

ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef",
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

ListKeyPhrasesDetectionJobsPaginateResponseTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsPaginateResponseTypeDef",
    {
        "KeyPhrasesDetectionJobPropertiesList": List[
            ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)

ListSentimentDetectionJobsPaginateFilterTypeDef = TypedDict(
    "ListSentimentDetectionJobsPaginateFilterTypeDef",
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

ListSentimentDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "ListSentimentDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef = TypedDict(
    "ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef",
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

ListSentimentDetectionJobsPaginateResponseTypeDef = TypedDict(
    "ListSentimentDetectionJobsPaginateResponseTypeDef",
    {
        "SentimentDetectionJobPropertiesList": List[
            ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)

ListTopicsDetectionJobsPaginateFilterTypeDef = TypedDict(
    "ListTopicsDetectionJobsPaginateFilterTypeDef",
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

ListTopicsDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "ListTopicsDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]},
    total=False,
)

ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)

ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef = TypedDict(
    "ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef",
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

ListTopicsDetectionJobsPaginateResponseTypeDef = TypedDict(
    "ListTopicsDetectionJobsPaginateResponseTypeDef",
    {
        "TopicsDetectionJobPropertiesList": List[
            ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)
