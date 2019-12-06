"Main interface for forecast service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


_RequiredClientCreateDatasetEncryptionConfigTypeDef = TypedDict(
    "_RequiredClientCreateDatasetEncryptionConfigTypeDef", {"RoleArn": str}
)
_OptionalClientCreateDatasetEncryptionConfigTypeDef = TypedDict(
    "_OptionalClientCreateDatasetEncryptionConfigTypeDef", {"KMSKeyArn": str}, total=False
)


class ClientCreateDatasetEncryptionConfigTypeDef(
    _RequiredClientCreateDatasetEncryptionConfigTypeDef,
    _OptionalClientCreateDatasetEncryptionConfigTypeDef,
):
    pass


ClientCreateDatasetGroupResponseTypeDef = TypedDict(
    "ClientCreateDatasetGroupResponseTypeDef", {"DatasetGroupArn": str}, total=False
)

_RequiredClientCreateDatasetImportJobDataSourceS3ConfigTypeDef = TypedDict(
    "_RequiredClientCreateDatasetImportJobDataSourceS3ConfigTypeDef", {"Path": str}
)
_OptionalClientCreateDatasetImportJobDataSourceS3ConfigTypeDef = TypedDict(
    "_OptionalClientCreateDatasetImportJobDataSourceS3ConfigTypeDef",
    {"RoleArn": str, "KMSKeyArn": str},
    total=False,
)


class ClientCreateDatasetImportJobDataSourceS3ConfigTypeDef(
    _RequiredClientCreateDatasetImportJobDataSourceS3ConfigTypeDef,
    _OptionalClientCreateDatasetImportJobDataSourceS3ConfigTypeDef,
):
    pass


ClientCreateDatasetImportJobDataSourceTypeDef = TypedDict(
    "ClientCreateDatasetImportJobDataSourceTypeDef",
    {"S3Config": ClientCreateDatasetImportJobDataSourceS3ConfigTypeDef},
)

ClientCreateDatasetImportJobResponseTypeDef = TypedDict(
    "ClientCreateDatasetImportJobResponseTypeDef", {"DatasetImportJobArn": str}, total=False
)

ClientCreateDatasetResponseTypeDef = TypedDict(
    "ClientCreateDatasetResponseTypeDef", {"DatasetArn": str}, total=False
)

ClientCreateDatasetSchemaAttributesTypeDef = TypedDict(
    "ClientCreateDatasetSchemaAttributesTypeDef",
    {"AttributeName": str, "AttributeType": Literal["string", "integer", "float", "timestamp"]},
    total=False,
)

ClientCreateDatasetSchemaTypeDef = TypedDict(
    "ClientCreateDatasetSchemaTypeDef",
    {"Attributes": List[ClientCreateDatasetSchemaAttributesTypeDef]},
    total=False,
)

_RequiredClientCreateForecastExportJobDestinationS3ConfigTypeDef = TypedDict(
    "_RequiredClientCreateForecastExportJobDestinationS3ConfigTypeDef", {"Path": str}
)
_OptionalClientCreateForecastExportJobDestinationS3ConfigTypeDef = TypedDict(
    "_OptionalClientCreateForecastExportJobDestinationS3ConfigTypeDef",
    {"RoleArn": str, "KMSKeyArn": str},
    total=False,
)


class ClientCreateForecastExportJobDestinationS3ConfigTypeDef(
    _RequiredClientCreateForecastExportJobDestinationS3ConfigTypeDef,
    _OptionalClientCreateForecastExportJobDestinationS3ConfigTypeDef,
):
    pass


ClientCreateForecastExportJobDestinationTypeDef = TypedDict(
    "ClientCreateForecastExportJobDestinationTypeDef",
    {"S3Config": ClientCreateForecastExportJobDestinationS3ConfigTypeDef},
)

ClientCreateForecastExportJobResponseTypeDef = TypedDict(
    "ClientCreateForecastExportJobResponseTypeDef", {"ForecastExportJobArn": str}, total=False
)

ClientCreateForecastResponseTypeDef = TypedDict(
    "ClientCreateForecastResponseTypeDef", {"ForecastArn": str}, total=False
)

_RequiredClientCreatePredictorEncryptionConfigTypeDef = TypedDict(
    "_RequiredClientCreatePredictorEncryptionConfigTypeDef", {"RoleArn": str}
)
_OptionalClientCreatePredictorEncryptionConfigTypeDef = TypedDict(
    "_OptionalClientCreatePredictorEncryptionConfigTypeDef", {"KMSKeyArn": str}, total=False
)


class ClientCreatePredictorEncryptionConfigTypeDef(
    _RequiredClientCreatePredictorEncryptionConfigTypeDef,
    _OptionalClientCreatePredictorEncryptionConfigTypeDef,
):
    pass


ClientCreatePredictorEvaluationParametersTypeDef = TypedDict(
    "ClientCreatePredictorEvaluationParametersTypeDef",
    {"NumberOfBacktestWindows": int, "BackTestWindowOffset": int},
    total=False,
)

ClientCreatePredictorFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef = TypedDict(
    "ClientCreatePredictorFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef",
    {"FeaturizationMethodName": str, "FeaturizationMethodParameters": Dict[str, str]},
    total=False,
)

ClientCreatePredictorFeaturizationConfigFeaturizationsTypeDef = TypedDict(
    "ClientCreatePredictorFeaturizationConfigFeaturizationsTypeDef",
    {
        "AttributeName": str,
        "FeaturizationPipeline": List[
            ClientCreatePredictorFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef
        ],
    },
    total=False,
)

_RequiredClientCreatePredictorFeaturizationConfigTypeDef = TypedDict(
    "_RequiredClientCreatePredictorFeaturizationConfigTypeDef", {"ForecastFrequency": str}
)
_OptionalClientCreatePredictorFeaturizationConfigTypeDef = TypedDict(
    "_OptionalClientCreatePredictorFeaturizationConfigTypeDef",
    {
        "ForecastDimensions": List[str],
        "Featurizations": List[ClientCreatePredictorFeaturizationConfigFeaturizationsTypeDef],
    },
    total=False,
)


class ClientCreatePredictorFeaturizationConfigTypeDef(
    _RequiredClientCreatePredictorFeaturizationConfigTypeDef,
    _OptionalClientCreatePredictorFeaturizationConfigTypeDef,
):
    pass


_RequiredClientCreatePredictorHPOConfigParameterRangesCategoricalParameterRangesTypeDef = TypedDict(
    "_RequiredClientCreatePredictorHPOConfigParameterRangesCategoricalParameterRangesTypeDef",
    {"Name": str},
)
_OptionalClientCreatePredictorHPOConfigParameterRangesCategoricalParameterRangesTypeDef = TypedDict(
    "_OptionalClientCreatePredictorHPOConfigParameterRangesCategoricalParameterRangesTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreatePredictorHPOConfigParameterRangesCategoricalParameterRangesTypeDef(
    _RequiredClientCreatePredictorHPOConfigParameterRangesCategoricalParameterRangesTypeDef,
    _OptionalClientCreatePredictorHPOConfigParameterRangesCategoricalParameterRangesTypeDef,
):
    pass


ClientCreatePredictorHPOConfigParameterRangesContinuousParameterRangesTypeDef = TypedDict(
    "ClientCreatePredictorHPOConfigParameterRangesContinuousParameterRangesTypeDef",
    {
        "Name": str,
        "MaxValue": float,
        "MinValue": float,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientCreatePredictorHPOConfigParameterRangesIntegerParameterRangesTypeDef = TypedDict(
    "ClientCreatePredictorHPOConfigParameterRangesIntegerParameterRangesTypeDef",
    {
        "Name": str,
        "MaxValue": int,
        "MinValue": int,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientCreatePredictorHPOConfigParameterRangesTypeDef = TypedDict(
    "ClientCreatePredictorHPOConfigParameterRangesTypeDef",
    {
        "CategoricalParameterRanges": List[
            ClientCreatePredictorHPOConfigParameterRangesCategoricalParameterRangesTypeDef
        ],
        "ContinuousParameterRanges": List[
            ClientCreatePredictorHPOConfigParameterRangesContinuousParameterRangesTypeDef
        ],
        "IntegerParameterRanges": List[
            ClientCreatePredictorHPOConfigParameterRangesIntegerParameterRangesTypeDef
        ],
    },
    total=False,
)

ClientCreatePredictorHPOConfigTypeDef = TypedDict(
    "ClientCreatePredictorHPOConfigTypeDef",
    {"ParameterRanges": ClientCreatePredictorHPOConfigParameterRangesTypeDef},
    total=False,
)

ClientCreatePredictorInputDataConfigSupplementaryFeaturesTypeDef = TypedDict(
    "ClientCreatePredictorInputDataConfigSupplementaryFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

_RequiredClientCreatePredictorInputDataConfigTypeDef = TypedDict(
    "_RequiredClientCreatePredictorInputDataConfigTypeDef", {"DatasetGroupArn": str}
)
_OptionalClientCreatePredictorInputDataConfigTypeDef = TypedDict(
    "_OptionalClientCreatePredictorInputDataConfigTypeDef",
    {
        "SupplementaryFeatures": List[
            ClientCreatePredictorInputDataConfigSupplementaryFeaturesTypeDef
        ]
    },
    total=False,
)


class ClientCreatePredictorInputDataConfigTypeDef(
    _RequiredClientCreatePredictorInputDataConfigTypeDef,
    _OptionalClientCreatePredictorInputDataConfigTypeDef,
):
    pass


ClientCreatePredictorResponseTypeDef = TypedDict(
    "ClientCreatePredictorResponseTypeDef", {"PredictorArn": str}, total=False
)

ClientDescribeDatasetGroupResponseTypeDef = TypedDict(
    "ClientDescribeDatasetGroupResponseTypeDef",
    {
        "DatasetGroupName": str,
        "DatasetGroupArn": str,
        "DatasetArns": List[str],
        "Domain": Literal[
            "RETAIL",
            "CUSTOM",
            "INVENTORY_PLANNING",
            "EC2_CAPACITY",
            "WORK_FORCE",
            "WEB_TRAFFIC",
            "METRICS",
        ],
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ClientDescribeDatasetImportJobResponseDataSourceS3ConfigTypeDef = TypedDict(
    "ClientDescribeDatasetImportJobResponseDataSourceS3ConfigTypeDef",
    {"Path": str, "RoleArn": str, "KMSKeyArn": str},
    total=False,
)

ClientDescribeDatasetImportJobResponseDataSourceTypeDef = TypedDict(
    "ClientDescribeDatasetImportJobResponseDataSourceTypeDef",
    {"S3Config": ClientDescribeDatasetImportJobResponseDataSourceS3ConfigTypeDef},
    total=False,
)

ClientDescribeDatasetImportJobResponseFieldStatisticsTypeDef = TypedDict(
    "ClientDescribeDatasetImportJobResponseFieldStatisticsTypeDef",
    {
        "Count": int,
        "CountDistinct": int,
        "CountNull": int,
        "CountNan": int,
        "Min": str,
        "Max": str,
        "Avg": float,
        "Stddev": float,
    },
    total=False,
)

ClientDescribeDatasetImportJobResponseTypeDef = TypedDict(
    "ClientDescribeDatasetImportJobResponseTypeDef",
    {
        "DatasetImportJobName": str,
        "DatasetImportJobArn": str,
        "DatasetArn": str,
        "TimestampFormat": str,
        "DataSource": ClientDescribeDatasetImportJobResponseDataSourceTypeDef,
        "FieldStatistics": Dict[str, ClientDescribeDatasetImportJobResponseFieldStatisticsTypeDef],
        "DataSize": float,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ClientDescribeDatasetResponseEncryptionConfigTypeDef = TypedDict(
    "ClientDescribeDatasetResponseEncryptionConfigTypeDef",
    {"RoleArn": str, "KMSKeyArn": str},
    total=False,
)

ClientDescribeDatasetResponseSchemaAttributesTypeDef = TypedDict(
    "ClientDescribeDatasetResponseSchemaAttributesTypeDef",
    {"AttributeName": str, "AttributeType": Literal["string", "integer", "float", "timestamp"]},
    total=False,
)

ClientDescribeDatasetResponseSchemaTypeDef = TypedDict(
    "ClientDescribeDatasetResponseSchemaTypeDef",
    {"Attributes": List[ClientDescribeDatasetResponseSchemaAttributesTypeDef]},
    total=False,
)

ClientDescribeDatasetResponseTypeDef = TypedDict(
    "ClientDescribeDatasetResponseTypeDef",
    {
        "DatasetArn": str,
        "DatasetName": str,
        "Domain": Literal[
            "RETAIL",
            "CUSTOM",
            "INVENTORY_PLANNING",
            "EC2_CAPACITY",
            "WORK_FORCE",
            "WEB_TRAFFIC",
            "METRICS",
        ],
        "DatasetType": Literal["TARGET_TIME_SERIES", "RELATED_TIME_SERIES", "ITEM_METADATA"],
        "DataFrequency": str,
        "Schema": ClientDescribeDatasetResponseSchemaTypeDef,
        "EncryptionConfig": ClientDescribeDatasetResponseEncryptionConfigTypeDef,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ClientDescribeForecastExportJobResponseDestinationS3ConfigTypeDef = TypedDict(
    "ClientDescribeForecastExportJobResponseDestinationS3ConfigTypeDef",
    {"Path": str, "RoleArn": str, "KMSKeyArn": str},
    total=False,
)

ClientDescribeForecastExportJobResponseDestinationTypeDef = TypedDict(
    "ClientDescribeForecastExportJobResponseDestinationTypeDef",
    {"S3Config": ClientDescribeForecastExportJobResponseDestinationS3ConfigTypeDef},
    total=False,
)

ClientDescribeForecastExportJobResponseTypeDef = TypedDict(
    "ClientDescribeForecastExportJobResponseTypeDef",
    {
        "ForecastExportJobArn": str,
        "ForecastExportJobName": str,
        "ForecastArn": str,
        "Destination": ClientDescribeForecastExportJobResponseDestinationTypeDef,
        "Message": str,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ClientDescribeForecastResponseTypeDef = TypedDict(
    "ClientDescribeForecastResponseTypeDef",
    {
        "ForecastArn": str,
        "ForecastName": str,
        "ForecastTypes": List[str],
        "PredictorArn": str,
        "DatasetGroupArn": str,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ClientDescribePredictorResponseEncryptionConfigTypeDef = TypedDict(
    "ClientDescribePredictorResponseEncryptionConfigTypeDef",
    {"RoleArn": str, "KMSKeyArn": str},
    total=False,
)

ClientDescribePredictorResponseEvaluationParametersTypeDef = TypedDict(
    "ClientDescribePredictorResponseEvaluationParametersTypeDef",
    {"NumberOfBacktestWindows": int, "BackTestWindowOffset": int},
    total=False,
)

ClientDescribePredictorResponseFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef = TypedDict(
    "ClientDescribePredictorResponseFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef",
    {"FeaturizationMethodName": str, "FeaturizationMethodParameters": Dict[str, str]},
    total=False,
)

ClientDescribePredictorResponseFeaturizationConfigFeaturizationsTypeDef = TypedDict(
    "ClientDescribePredictorResponseFeaturizationConfigFeaturizationsTypeDef",
    {
        "AttributeName": str,
        "FeaturizationPipeline": List[
            ClientDescribePredictorResponseFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef
        ],
    },
    total=False,
)

ClientDescribePredictorResponseFeaturizationConfigTypeDef = TypedDict(
    "ClientDescribePredictorResponseFeaturizationConfigTypeDef",
    {
        "ForecastFrequency": str,
        "ForecastDimensions": List[str],
        "Featurizations": List[
            ClientDescribePredictorResponseFeaturizationConfigFeaturizationsTypeDef
        ],
    },
    total=False,
)

ClientDescribePredictorResponseHPOConfigParameterRangesCategoricalParameterRangesTypeDef = TypedDict(
    "ClientDescribePredictorResponseHPOConfigParameterRangesCategoricalParameterRangesTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientDescribePredictorResponseHPOConfigParameterRangesContinuousParameterRangesTypeDef = TypedDict(
    "ClientDescribePredictorResponseHPOConfigParameterRangesContinuousParameterRangesTypeDef",
    {
        "Name": str,
        "MaxValue": float,
        "MinValue": float,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientDescribePredictorResponseHPOConfigParameterRangesIntegerParameterRangesTypeDef = TypedDict(
    "ClientDescribePredictorResponseHPOConfigParameterRangesIntegerParameterRangesTypeDef",
    {
        "Name": str,
        "MaxValue": int,
        "MinValue": int,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientDescribePredictorResponseHPOConfigParameterRangesTypeDef = TypedDict(
    "ClientDescribePredictorResponseHPOConfigParameterRangesTypeDef",
    {
        "CategoricalParameterRanges": List[
            ClientDescribePredictorResponseHPOConfigParameterRangesCategoricalParameterRangesTypeDef
        ],
        "ContinuousParameterRanges": List[
            ClientDescribePredictorResponseHPOConfigParameterRangesContinuousParameterRangesTypeDef
        ],
        "IntegerParameterRanges": List[
            ClientDescribePredictorResponseHPOConfigParameterRangesIntegerParameterRangesTypeDef
        ],
    },
    total=False,
)

ClientDescribePredictorResponseHPOConfigTypeDef = TypedDict(
    "ClientDescribePredictorResponseHPOConfigTypeDef",
    {"ParameterRanges": ClientDescribePredictorResponseHPOConfigParameterRangesTypeDef},
    total=False,
)

ClientDescribePredictorResponseInputDataConfigSupplementaryFeaturesTypeDef = TypedDict(
    "ClientDescribePredictorResponseInputDataConfigSupplementaryFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribePredictorResponseInputDataConfigTypeDef = TypedDict(
    "ClientDescribePredictorResponseInputDataConfigTypeDef",
    {
        "DatasetGroupArn": str,
        "SupplementaryFeatures": List[
            ClientDescribePredictorResponseInputDataConfigSupplementaryFeaturesTypeDef
        ],
    },
    total=False,
)

ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTestWindowsTypeDef = TypedDict(
    "ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTestWindowsTypeDef",
    {"TestWindowStart": datetime, "TestWindowEnd": datetime, "Status": str, "Message": str},
    total=False,
)

ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTypeDef = TypedDict(
    "ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTypeDef",
    {
        "AlgorithmArn": str,
        "TestWindows": List[
            ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTestWindowsTypeDef
        ],
    },
    total=False,
)

ClientDescribePredictorResponsePredictorExecutionDetailsTypeDef = TypedDict(
    "ClientDescribePredictorResponsePredictorExecutionDetailsTypeDef",
    {
        "PredictorExecutions": List[
            ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTypeDef
        ]
    },
    total=False,
)

ClientDescribePredictorResponseTypeDef = TypedDict(
    "ClientDescribePredictorResponseTypeDef",
    {
        "PredictorArn": str,
        "PredictorName": str,
        "AlgorithmArn": str,
        "ForecastHorizon": int,
        "PerformAutoML": bool,
        "PerformHPO": bool,
        "TrainingParameters": Dict[str, str],
        "EvaluationParameters": ClientDescribePredictorResponseEvaluationParametersTypeDef,
        "HPOConfig": ClientDescribePredictorResponseHPOConfigTypeDef,
        "InputDataConfig": ClientDescribePredictorResponseInputDataConfigTypeDef,
        "FeaturizationConfig": ClientDescribePredictorResponseFeaturizationConfigTypeDef,
        "EncryptionConfig": ClientDescribePredictorResponseEncryptionConfigTypeDef,
        "PredictorExecutionDetails": ClientDescribePredictorResponsePredictorExecutionDetailsTypeDef,
        "DatasetImportJobArns": List[str],
        "AutoMLAlgorithmArns": List[str],
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsWeightedQuantileLossesTypeDef = TypedDict(
    "ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsWeightedQuantileLossesTypeDef",
    {"Quantile": float, "LossValue": float},
    total=False,
)

ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsTypeDef = TypedDict(
    "ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsTypeDef",
    {
        "RMSE": float,
        "WeightedQuantileLosses": List[
            ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsWeightedQuantileLossesTypeDef
        ],
    },
    total=False,
)

ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsTypeDef = TypedDict(
    "ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsTypeDef",
    {
        "TestWindowStart": datetime,
        "TestWindowEnd": datetime,
        "ItemCount": int,
        "EvaluationType": Literal["SUMMARY", "COMPUTED"],
        "Metrics": ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsTypeDef,
    },
    total=False,
)

ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTypeDef = TypedDict(
    "ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTypeDef",
    {
        "AlgorithmArn": str,
        "TestWindows": List[
            ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsTypeDef
        ],
    },
    total=False,
)

ClientGetAccuracyMetricsResponseTypeDef = TypedDict(
    "ClientGetAccuracyMetricsResponseTypeDef",
    {
        "PredictorEvaluationResults": List[
            ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTypeDef
        ]
    },
    total=False,
)

ClientListDatasetGroupsResponseDatasetGroupsTypeDef = TypedDict(
    "ClientListDatasetGroupsResponseDatasetGroupsTypeDef",
    {
        "DatasetGroupArn": str,
        "DatasetGroupName": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ClientListDatasetGroupsResponseTypeDef = TypedDict(
    "ClientListDatasetGroupsResponseTypeDef",
    {"DatasetGroups": List[ClientListDatasetGroupsResponseDatasetGroupsTypeDef], "NextToken": str},
    total=False,
)

ClientListDatasetImportJobsFiltersTypeDef = TypedDict(
    "ClientListDatasetImportJobsFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)

ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceS3ConfigTypeDef = TypedDict(
    "ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceS3ConfigTypeDef",
    {"Path": str, "RoleArn": str, "KMSKeyArn": str},
    total=False,
)

ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceTypeDef = TypedDict(
    "ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceTypeDef",
    {"S3Config": ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceS3ConfigTypeDef},
    total=False,
)

ClientListDatasetImportJobsResponseDatasetImportJobsTypeDef = TypedDict(
    "ClientListDatasetImportJobsResponseDatasetImportJobsTypeDef",
    {
        "DatasetImportJobArn": str,
        "DatasetImportJobName": str,
        "DataSource": ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceTypeDef,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ClientListDatasetImportJobsResponseTypeDef = TypedDict(
    "ClientListDatasetImportJobsResponseTypeDef",
    {
        "DatasetImportJobs": List[ClientListDatasetImportJobsResponseDatasetImportJobsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListDatasetsResponseDatasetsTypeDef = TypedDict(
    "ClientListDatasetsResponseDatasetsTypeDef",
    {
        "DatasetArn": str,
        "DatasetName": str,
        "DatasetType": Literal["TARGET_TIME_SERIES", "RELATED_TIME_SERIES", "ITEM_METADATA"],
        "Domain": Literal[
            "RETAIL",
            "CUSTOM",
            "INVENTORY_PLANNING",
            "EC2_CAPACITY",
            "WORK_FORCE",
            "WEB_TRAFFIC",
            "METRICS",
        ],
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ClientListDatasetsResponseTypeDef = TypedDict(
    "ClientListDatasetsResponseTypeDef",
    {"Datasets": List[ClientListDatasetsResponseDatasetsTypeDef], "NextToken": str},
    total=False,
)

ClientListForecastExportJobsFiltersTypeDef = TypedDict(
    "ClientListForecastExportJobsFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)

ClientListForecastExportJobsResponseForecastExportJobsDestinationS3ConfigTypeDef = TypedDict(
    "ClientListForecastExportJobsResponseForecastExportJobsDestinationS3ConfigTypeDef",
    {"Path": str, "RoleArn": str, "KMSKeyArn": str},
    total=False,
)

ClientListForecastExportJobsResponseForecastExportJobsDestinationTypeDef = TypedDict(
    "ClientListForecastExportJobsResponseForecastExportJobsDestinationTypeDef",
    {"S3Config": ClientListForecastExportJobsResponseForecastExportJobsDestinationS3ConfigTypeDef},
    total=False,
)

ClientListForecastExportJobsResponseForecastExportJobsTypeDef = TypedDict(
    "ClientListForecastExportJobsResponseForecastExportJobsTypeDef",
    {
        "ForecastExportJobArn": str,
        "ForecastExportJobName": str,
        "Destination": ClientListForecastExportJobsResponseForecastExportJobsDestinationTypeDef,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ClientListForecastExportJobsResponseTypeDef = TypedDict(
    "ClientListForecastExportJobsResponseTypeDef",
    {
        "ForecastExportJobs": List[ClientListForecastExportJobsResponseForecastExportJobsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListForecastsFiltersTypeDef = TypedDict(
    "ClientListForecastsFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)

ClientListForecastsResponseForecastsTypeDef = TypedDict(
    "ClientListForecastsResponseForecastsTypeDef",
    {
        "ForecastArn": str,
        "ForecastName": str,
        "PredictorArn": str,
        "DatasetGroupArn": str,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ClientListForecastsResponseTypeDef = TypedDict(
    "ClientListForecastsResponseTypeDef",
    {"Forecasts": List[ClientListForecastsResponseForecastsTypeDef], "NextToken": str},
    total=False,
)

ClientListPredictorsFiltersTypeDef = TypedDict(
    "ClientListPredictorsFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)

ClientListPredictorsResponsePredictorsTypeDef = TypedDict(
    "ClientListPredictorsResponsePredictorsTypeDef",
    {
        "PredictorArn": str,
        "PredictorName": str,
        "DatasetGroupArn": str,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ClientListPredictorsResponseTypeDef = TypedDict(
    "ClientListPredictorsResponseTypeDef",
    {"Predictors": List[ClientListPredictorsResponsePredictorsTypeDef], "NextToken": str},
    total=False,
)

ListDatasetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDatasetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDatasetGroupsPaginateResponseDatasetGroupsTypeDef = TypedDict(
    "ListDatasetGroupsPaginateResponseDatasetGroupsTypeDef",
    {
        "DatasetGroupArn": str,
        "DatasetGroupName": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ListDatasetGroupsPaginateResponseTypeDef = TypedDict(
    "ListDatasetGroupsPaginateResponseTypeDef",
    {"DatasetGroups": List[ListDatasetGroupsPaginateResponseDatasetGroupsTypeDef]},
    total=False,
)

ListDatasetImportJobsPaginateFiltersTypeDef = TypedDict(
    "ListDatasetImportJobsPaginateFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)

ListDatasetImportJobsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDatasetImportJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceS3ConfigTypeDef = TypedDict(
    "ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceS3ConfigTypeDef",
    {"Path": str, "RoleArn": str, "KMSKeyArn": str},
    total=False,
)

ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceTypeDef = TypedDict(
    "ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceTypeDef",
    {"S3Config": ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceS3ConfigTypeDef},
    total=False,
)

ListDatasetImportJobsPaginateResponseDatasetImportJobsTypeDef = TypedDict(
    "ListDatasetImportJobsPaginateResponseDatasetImportJobsTypeDef",
    {
        "DatasetImportJobArn": str,
        "DatasetImportJobName": str,
        "DataSource": ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceTypeDef,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ListDatasetImportJobsPaginateResponseTypeDef = TypedDict(
    "ListDatasetImportJobsPaginateResponseTypeDef",
    {"DatasetImportJobs": List[ListDatasetImportJobsPaginateResponseDatasetImportJobsTypeDef]},
    total=False,
)

ListDatasetsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDatasetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDatasetsPaginateResponseDatasetsTypeDef = TypedDict(
    "ListDatasetsPaginateResponseDatasetsTypeDef",
    {
        "DatasetArn": str,
        "DatasetName": str,
        "DatasetType": Literal["TARGET_TIME_SERIES", "RELATED_TIME_SERIES", "ITEM_METADATA"],
        "Domain": Literal[
            "RETAIL",
            "CUSTOM",
            "INVENTORY_PLANNING",
            "EC2_CAPACITY",
            "WORK_FORCE",
            "WEB_TRAFFIC",
            "METRICS",
        ],
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ListDatasetsPaginateResponseTypeDef = TypedDict(
    "ListDatasetsPaginateResponseTypeDef",
    {"Datasets": List[ListDatasetsPaginateResponseDatasetsTypeDef]},
    total=False,
)

ListForecastExportJobsPaginateFiltersTypeDef = TypedDict(
    "ListForecastExportJobsPaginateFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)

ListForecastExportJobsPaginatePaginationConfigTypeDef = TypedDict(
    "ListForecastExportJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListForecastExportJobsPaginateResponseForecastExportJobsDestinationS3ConfigTypeDef = TypedDict(
    "ListForecastExportJobsPaginateResponseForecastExportJobsDestinationS3ConfigTypeDef",
    {"Path": str, "RoleArn": str, "KMSKeyArn": str},
    total=False,
)

ListForecastExportJobsPaginateResponseForecastExportJobsDestinationTypeDef = TypedDict(
    "ListForecastExportJobsPaginateResponseForecastExportJobsDestinationTypeDef",
    {
        "S3Config": ListForecastExportJobsPaginateResponseForecastExportJobsDestinationS3ConfigTypeDef
    },
    total=False,
)

ListForecastExportJobsPaginateResponseForecastExportJobsTypeDef = TypedDict(
    "ListForecastExportJobsPaginateResponseForecastExportJobsTypeDef",
    {
        "ForecastExportJobArn": str,
        "ForecastExportJobName": str,
        "Destination": ListForecastExportJobsPaginateResponseForecastExportJobsDestinationTypeDef,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ListForecastExportJobsPaginateResponseTypeDef = TypedDict(
    "ListForecastExportJobsPaginateResponseTypeDef",
    {"ForecastExportJobs": List[ListForecastExportJobsPaginateResponseForecastExportJobsTypeDef]},
    total=False,
)

ListForecastsPaginateFiltersTypeDef = TypedDict(
    "ListForecastsPaginateFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)

ListForecastsPaginatePaginationConfigTypeDef = TypedDict(
    "ListForecastsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListForecastsPaginateResponseForecastsTypeDef = TypedDict(
    "ListForecastsPaginateResponseForecastsTypeDef",
    {
        "ForecastArn": str,
        "ForecastName": str,
        "PredictorArn": str,
        "DatasetGroupArn": str,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ListForecastsPaginateResponseTypeDef = TypedDict(
    "ListForecastsPaginateResponseTypeDef",
    {"Forecasts": List[ListForecastsPaginateResponseForecastsTypeDef]},
    total=False,
)

ListPredictorsPaginateFiltersTypeDef = TypedDict(
    "ListPredictorsPaginateFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)

ListPredictorsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPredictorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPredictorsPaginateResponsePredictorsTypeDef = TypedDict(
    "ListPredictorsPaginateResponsePredictorsTypeDef",
    {
        "PredictorArn": str,
        "PredictorName": str,
        "DatasetGroupArn": str,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ListPredictorsPaginateResponseTypeDef = TypedDict(
    "ListPredictorsPaginateResponseTypeDef",
    {"Predictors": List[ListPredictorsPaginateResponsePredictorsTypeDef]},
    total=False,
)
