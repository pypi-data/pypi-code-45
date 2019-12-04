"Main interface for forecast service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateDatasetEncryptionConfigTypeDef",
    "ClientCreateDatasetGroupResponseTypeDef",
    "ClientCreateDatasetImportJobDataSourceS3ConfigTypeDef",
    "ClientCreateDatasetImportJobDataSourceTypeDef",
    "ClientCreateDatasetImportJobResponseTypeDef",
    "ClientCreateDatasetResponseTypeDef",
    "ClientCreateDatasetSchemaAttributesTypeDef",
    "ClientCreateDatasetSchemaTypeDef",
    "ClientCreateForecastExportJobDestinationS3ConfigTypeDef",
    "ClientCreateForecastExportJobDestinationTypeDef",
    "ClientCreateForecastExportJobResponseTypeDef",
    "ClientCreateForecastResponseTypeDef",
    "ClientCreatePredictorEncryptionConfigTypeDef",
    "ClientCreatePredictorEvaluationParametersTypeDef",
    "ClientCreatePredictorFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef",
    "ClientCreatePredictorFeaturizationConfigFeaturizationsTypeDef",
    "ClientCreatePredictorFeaturizationConfigTypeDef",
    "ClientCreatePredictorHPOConfigParameterRangesCategoricalParameterRangesTypeDef",
    "ClientCreatePredictorHPOConfigParameterRangesContinuousParameterRangesTypeDef",
    "ClientCreatePredictorHPOConfigParameterRangesIntegerParameterRangesTypeDef",
    "ClientCreatePredictorHPOConfigParameterRangesTypeDef",
    "ClientCreatePredictorHPOConfigTypeDef",
    "ClientCreatePredictorInputDataConfigSupplementaryFeaturesTypeDef",
    "ClientCreatePredictorInputDataConfigTypeDef",
    "ClientCreatePredictorResponseTypeDef",
    "ClientDescribeDatasetGroupResponseTypeDef",
    "ClientDescribeDatasetImportJobResponseDataSourceS3ConfigTypeDef",
    "ClientDescribeDatasetImportJobResponseDataSourceTypeDef",
    "ClientDescribeDatasetImportJobResponseFieldStatisticsTypeDef",
    "ClientDescribeDatasetImportJobResponseTypeDef",
    "ClientDescribeDatasetResponseEncryptionConfigTypeDef",
    "ClientDescribeDatasetResponseSchemaAttributesTypeDef",
    "ClientDescribeDatasetResponseSchemaTypeDef",
    "ClientDescribeDatasetResponseTypeDef",
    "ClientDescribeForecastExportJobResponseDestinationS3ConfigTypeDef",
    "ClientDescribeForecastExportJobResponseDestinationTypeDef",
    "ClientDescribeForecastExportJobResponseTypeDef",
    "ClientDescribeForecastResponseTypeDef",
    "ClientDescribePredictorResponseEncryptionConfigTypeDef",
    "ClientDescribePredictorResponseEvaluationParametersTypeDef",
    "ClientDescribePredictorResponseFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef",
    "ClientDescribePredictorResponseFeaturizationConfigFeaturizationsTypeDef",
    "ClientDescribePredictorResponseFeaturizationConfigTypeDef",
    "ClientDescribePredictorResponseHPOConfigParameterRangesCategoricalParameterRangesTypeDef",
    "ClientDescribePredictorResponseHPOConfigParameterRangesContinuousParameterRangesTypeDef",
    "ClientDescribePredictorResponseHPOConfigParameterRangesIntegerParameterRangesTypeDef",
    "ClientDescribePredictorResponseHPOConfigParameterRangesTypeDef",
    "ClientDescribePredictorResponseHPOConfigTypeDef",
    "ClientDescribePredictorResponseInputDataConfigSupplementaryFeaturesTypeDef",
    "ClientDescribePredictorResponseInputDataConfigTypeDef",
    "ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTestWindowsTypeDef",
    "ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTypeDef",
    "ClientDescribePredictorResponsePredictorExecutionDetailsTypeDef",
    "ClientDescribePredictorResponseTypeDef",
    "ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsWeightedQuantileLossesTypeDef",
    "ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsTypeDef",
    "ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsTypeDef",
    "ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTypeDef",
    "ClientGetAccuracyMetricsResponseTypeDef",
    "ClientListDatasetGroupsResponseDatasetGroupsTypeDef",
    "ClientListDatasetGroupsResponseTypeDef",
    "ClientListDatasetImportJobsFiltersTypeDef",
    "ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceS3ConfigTypeDef",
    "ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceTypeDef",
    "ClientListDatasetImportJobsResponseDatasetImportJobsTypeDef",
    "ClientListDatasetImportJobsResponseTypeDef",
    "ClientListDatasetsResponseDatasetsTypeDef",
    "ClientListDatasetsResponseTypeDef",
    "ClientListForecastExportJobsFiltersTypeDef",
    "ClientListForecastExportJobsResponseForecastExportJobsDestinationS3ConfigTypeDef",
    "ClientListForecastExportJobsResponseForecastExportJobsDestinationTypeDef",
    "ClientListForecastExportJobsResponseForecastExportJobsTypeDef",
    "ClientListForecastExportJobsResponseTypeDef",
    "ClientListForecastsFiltersTypeDef",
    "ClientListForecastsResponseForecastsTypeDef",
    "ClientListForecastsResponseTypeDef",
    "ClientListPredictorsFiltersTypeDef",
    "ClientListPredictorsResponsePredictorsTypeDef",
    "ClientListPredictorsResponseTypeDef",
    "ListDatasetGroupsPaginatePaginationConfigTypeDef",
    "ListDatasetGroupsPaginateResponseDatasetGroupsTypeDef",
    "ListDatasetGroupsPaginateResponseTypeDef",
    "ListDatasetImportJobsPaginateFiltersTypeDef",
    "ListDatasetImportJobsPaginatePaginationConfigTypeDef",
    "ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceS3ConfigTypeDef",
    "ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceTypeDef",
    "ListDatasetImportJobsPaginateResponseDatasetImportJobsTypeDef",
    "ListDatasetImportJobsPaginateResponseTypeDef",
    "ListDatasetsPaginatePaginationConfigTypeDef",
    "ListDatasetsPaginateResponseDatasetsTypeDef",
    "ListDatasetsPaginateResponseTypeDef",
    "ListForecastExportJobsPaginateFiltersTypeDef",
    "ListForecastExportJobsPaginatePaginationConfigTypeDef",
    "ListForecastExportJobsPaginateResponseForecastExportJobsDestinationS3ConfigTypeDef",
    "ListForecastExportJobsPaginateResponseForecastExportJobsDestinationTypeDef",
    "ListForecastExportJobsPaginateResponseForecastExportJobsTypeDef",
    "ListForecastExportJobsPaginateResponseTypeDef",
    "ListForecastsPaginateFiltersTypeDef",
    "ListForecastsPaginatePaginationConfigTypeDef",
    "ListForecastsPaginateResponseForecastsTypeDef",
    "ListForecastsPaginateResponseTypeDef",
    "ListPredictorsPaginateFiltersTypeDef",
    "ListPredictorsPaginatePaginationConfigTypeDef",
    "ListPredictorsPaginateResponsePredictorsTypeDef",
    "ListPredictorsPaginateResponseTypeDef",
)


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
    """
    An AWS Key Management Service (KMS) key and the AWS Identity and Access Management (IAM) role
    that Amazon Forecast can assume to access the key.
    - **RoleArn** *(string) --***[REQUIRED]**

      The ARN of the IAM role that Amazon Forecast can assume to access the AWS KMS key.
      Passing a role across AWS accounts is not allowed. If you pass a role that isn't in your
      account, you get an ``InvalidInputException`` error.
    """


_ClientCreateDatasetGroupResponseTypeDef = TypedDict(
    "_ClientCreateDatasetGroupResponseTypeDef", {"DatasetGroupArn": str}, total=False
)


class ClientCreateDatasetGroupResponseTypeDef(_ClientCreateDatasetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **DatasetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset group.
    """


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
    """
    - **S3Config** *(dict) --***[REQUIRED]**

      The path to the training data stored in an Amazon Simple Storage Service (Amazon S3) bucket
      along with the credentials to access the data.
      - **Path** *(string) --***[REQUIRED]**

        The path to an Amazon Simple Storage Service (Amazon S3) bucket or file(s) in an Amazon S3
        bucket.
    """


_ClientCreateDatasetImportJobDataSourceTypeDef = TypedDict(
    "_ClientCreateDatasetImportJobDataSourceTypeDef",
    {"S3Config": ClientCreateDatasetImportJobDataSourceS3ConfigTypeDef},
)


class ClientCreateDatasetImportJobDataSourceTypeDef(_ClientCreateDatasetImportJobDataSourceTypeDef):
    """
    The location of the training data to import and an AWS Identity and Access Management (IAM) role
    that Amazon Forecast can assume to access the data. The training data must be stored in an
    Amazon S3 bucket.
    If encryption is used, ``DataSource`` must include an AWS Key Management Service (KMS) key and
    the IAM role must allow Amazon Forecast permission to access the key. The KMS key and IAM role
    must match those specified in the ``EncryptionConfig`` parameter of the  CreateDataset
    operation.
    - **S3Config** *(dict) --***[REQUIRED]**

      The path to the training data stored in an Amazon Simple Storage Service (Amazon S3) bucket
      along with the credentials to access the data.
      - **Path** *(string) --***[REQUIRED]**

        The path to an Amazon Simple Storage Service (Amazon S3) bucket or file(s) in an Amazon S3
        bucket.
    """


_ClientCreateDatasetImportJobResponseTypeDef = TypedDict(
    "_ClientCreateDatasetImportJobResponseTypeDef", {"DatasetImportJobArn": str}, total=False
)


class ClientCreateDatasetImportJobResponseTypeDef(_ClientCreateDatasetImportJobResponseTypeDef):
    """
    - *(dict) --*

      - **DatasetImportJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset import job.
    """


_ClientCreateDatasetResponseTypeDef = TypedDict(
    "_ClientCreateDatasetResponseTypeDef", {"DatasetArn": str}, total=False
)


class ClientCreateDatasetResponseTypeDef(_ClientCreateDatasetResponseTypeDef):
    """
    - *(dict) --*

      - **DatasetArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset.
    """


_ClientCreateDatasetSchemaAttributesTypeDef = TypedDict(
    "_ClientCreateDatasetSchemaAttributesTypeDef",
    {"AttributeName": str, "AttributeType": Literal["string", "integer", "float", "timestamp"]},
    total=False,
)


class ClientCreateDatasetSchemaAttributesTypeDef(_ClientCreateDatasetSchemaAttributesTypeDef):
    """
    - *(dict) --*

      An attribute of a schema, which defines a dataset field. A schema attribute is required for
      every field in a dataset. The  Schema object contains an array of ``SchemaAttribute`` objects.
      - **AttributeName** *(string) --*

        The name of the dataset field.
    """


_ClientCreateDatasetSchemaTypeDef = TypedDict(
    "_ClientCreateDatasetSchemaTypeDef",
    {"Attributes": List[ClientCreateDatasetSchemaAttributesTypeDef]},
    total=False,
)


class ClientCreateDatasetSchemaTypeDef(_ClientCreateDatasetSchemaTypeDef):
    """
    The schema for the dataset. The schema attributes and their order must match the fields in your
    data. The dataset ``Domain`` and ``DatasetType`` that you choose determine the minimum required
    fields in your training data. For information about the required fields for a specific dataset
    domain and type, see  howitworks-domains-ds-types .
    - **Attributes** *(list) --*

      An array of attributes specifying the name and type of each field in a dataset.
      - *(dict) --*

        An attribute of a schema, which defines a dataset field. A schema attribute is required for
        every field in a dataset. The  Schema object contains an array of ``SchemaAttribute``
        objects.
        - **AttributeName** *(string) --*

          The name of the dataset field.
    """


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
    """
    - **S3Config** *(dict) --***[REQUIRED]**

      The path to an Amazon Simple Storage Service (Amazon S3) bucket along with the credentials to
      access the bucket.
      - **Path** *(string) --***[REQUIRED]**

        The path to an Amazon Simple Storage Service (Amazon S3) bucket or file(s) in an Amazon S3
        bucket.
    """


_ClientCreateForecastExportJobDestinationTypeDef = TypedDict(
    "_ClientCreateForecastExportJobDestinationTypeDef",
    {"S3Config": ClientCreateForecastExportJobDestinationS3ConfigTypeDef},
)


class ClientCreateForecastExportJobDestinationTypeDef(
    _ClientCreateForecastExportJobDestinationTypeDef
):
    """
    The location where you want to save the forecast and an AWS Identity and Access Management (IAM)
    role that Amazon Forecast can assume to access the location. The forecast must be exported to an
    Amazon S3 bucket.
    If encryption is used, ``Destination`` must include an AWS Key Management Service (KMS) key. The
    IAM role must allow Amazon Forecast permission to access the key.
    - **S3Config** *(dict) --***[REQUIRED]**

      The path to an Amazon Simple Storage Service (Amazon S3) bucket along with the credentials to
      access the bucket.
      - **Path** *(string) --***[REQUIRED]**

        The path to an Amazon Simple Storage Service (Amazon S3) bucket or file(s) in an Amazon S3
        bucket.
    """


_ClientCreateForecastExportJobResponseTypeDef = TypedDict(
    "_ClientCreateForecastExportJobResponseTypeDef", {"ForecastExportJobArn": str}, total=False
)


class ClientCreateForecastExportJobResponseTypeDef(_ClientCreateForecastExportJobResponseTypeDef):
    """
    - *(dict) --*

      - **ForecastExportJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the export job.
    """


_ClientCreateForecastResponseTypeDef = TypedDict(
    "_ClientCreateForecastResponseTypeDef", {"ForecastArn": str}, total=False
)


class ClientCreateForecastResponseTypeDef(_ClientCreateForecastResponseTypeDef):
    """
    - *(dict) --*

      - **ForecastArn** *(string) --*

        The Amazon Resource Name (ARN) of the forecast.
    """


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
    """
    An AWS Key Management Service (KMS) key and the AWS Identity and Access Management (IAM) role
    that Amazon Forecast can assume to access the key.
    - **RoleArn** *(string) --***[REQUIRED]**

      The ARN of the IAM role that Amazon Forecast can assume to access the AWS KMS key.
      Passing a role across AWS accounts is not allowed. If you pass a role that isn't in your
      account, you get an ``InvalidInputException`` error.
    """


_ClientCreatePredictorEvaluationParametersTypeDef = TypedDict(
    "_ClientCreatePredictorEvaluationParametersTypeDef",
    {"NumberOfBacktestWindows": int, "BackTestWindowOffset": int},
    total=False,
)


class ClientCreatePredictorEvaluationParametersTypeDef(
    _ClientCreatePredictorEvaluationParametersTypeDef
):
    """
    Used to override the default evaluation parameters of the specified algorithm. Amazon Forecast
    evaluates a predictor by splitting a dataset into training data and testing data. The evaluation
    parameters define how to perform the split and the number of iterations.
    - **NumberOfBacktestWindows** *(integer) --*

      The number of times to split the input data. The default is 1. Valid values are 1 through 5.
    """


_ClientCreatePredictorFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef = TypedDict(
    "_ClientCreatePredictorFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef",
    {"FeaturizationMethodName": str, "FeaturizationMethodParameters": Dict[str, str]},
    total=False,
)


class ClientCreatePredictorFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef(
    _ClientCreatePredictorFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef
):
    pass


_ClientCreatePredictorFeaturizationConfigFeaturizationsTypeDef = TypedDict(
    "_ClientCreatePredictorFeaturizationConfigFeaturizationsTypeDef",
    {
        "AttributeName": str,
        "FeaturizationPipeline": List[
            ClientCreatePredictorFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef
        ],
    },
    total=False,
)


class ClientCreatePredictorFeaturizationConfigFeaturizationsTypeDef(
    _ClientCreatePredictorFeaturizationConfigFeaturizationsTypeDef
):
    pass


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
    """
    The featurization configuration.
    - **ForecastFrequency** *(string) --***[REQUIRED]**

      The frequency of predictions in a forecast.
      Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes),
      15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute). For example,
      "Y" indicates every year and "5min" indicates every five minutes.
      The frequency must be greater than or equal to the TARGET_TIME_SERIES dataset frequency.
      When a RELATED_TIME_SERIES dataset is provided, the frequency must be equal to the
      RELATED_TIME_SERIES dataset frequency.
    """


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
    """
    - *(dict) --*

      Specifies a categorical hyperparameter and it's range of tunable values. This object is part
      of the  ParameterRanges object.
      - **Name** *(string) --***[REQUIRED]**

        The name of the categorical hyperparameter to tune.
    """


_ClientCreatePredictorHPOConfigParameterRangesContinuousParameterRangesTypeDef = TypedDict(
    "_ClientCreatePredictorHPOConfigParameterRangesContinuousParameterRangesTypeDef",
    {
        "Name": str,
        "MaxValue": float,
        "MinValue": float,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)


class ClientCreatePredictorHPOConfigParameterRangesContinuousParameterRangesTypeDef(
    _ClientCreatePredictorHPOConfigParameterRangesContinuousParameterRangesTypeDef
):
    pass


_ClientCreatePredictorHPOConfigParameterRangesIntegerParameterRangesTypeDef = TypedDict(
    "_ClientCreatePredictorHPOConfigParameterRangesIntegerParameterRangesTypeDef",
    {
        "Name": str,
        "MaxValue": int,
        "MinValue": int,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)


class ClientCreatePredictorHPOConfigParameterRangesIntegerParameterRangesTypeDef(
    _ClientCreatePredictorHPOConfigParameterRangesIntegerParameterRangesTypeDef
):
    pass


_ClientCreatePredictorHPOConfigParameterRangesTypeDef = TypedDict(
    "_ClientCreatePredictorHPOConfigParameterRangesTypeDef",
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


class ClientCreatePredictorHPOConfigParameterRangesTypeDef(
    _ClientCreatePredictorHPOConfigParameterRangesTypeDef
):
    """
    - **ParameterRanges** *(dict) --*

      Specifies the ranges of valid values for the hyperparameters.
      - **CategoricalParameterRanges** *(list) --*

        Specifies the tunable range for each categorical hyperparameter.
        - *(dict) --*

          Specifies a categorical hyperparameter and it's range of tunable values. This object is
          part of the  ParameterRanges object.
          - **Name** *(string) --***[REQUIRED]**

            The name of the categorical hyperparameter to tune.
    """


_ClientCreatePredictorHPOConfigTypeDef = TypedDict(
    "_ClientCreatePredictorHPOConfigTypeDef",
    {"ParameterRanges": ClientCreatePredictorHPOConfigParameterRangesTypeDef},
    total=False,
)


class ClientCreatePredictorHPOConfigTypeDef(_ClientCreatePredictorHPOConfigTypeDef):
    """
    Provides hyperparameter override values for the algorithm. If you don't provide this parameter,
    Amazon Forecast uses default values. The individual algorithms specify which hyperparameters
    support hyperparameter optimization (HPO). For more information, see
    aws-forecast-choosing-recipes .
    If you included the ``HPOConfig`` object, you must set ``PerformHPO`` to true.
    - **ParameterRanges** *(dict) --*

      Specifies the ranges of valid values for the hyperparameters.
      - **CategoricalParameterRanges** *(list) --*

        Specifies the tunable range for each categorical hyperparameter.
        - *(dict) --*

          Specifies a categorical hyperparameter and it's range of tunable values. This object is
          part of the  ParameterRanges object.
          - **Name** *(string) --***[REQUIRED]**

            The name of the categorical hyperparameter to tune.
    """


_ClientCreatePredictorInputDataConfigSupplementaryFeaturesTypeDef = TypedDict(
    "_ClientCreatePredictorInputDataConfigSupplementaryFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreatePredictorInputDataConfigSupplementaryFeaturesTypeDef(
    _ClientCreatePredictorInputDataConfigSupplementaryFeaturesTypeDef
):
    pass


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
    """
    Describes the dataset group that contains the data to use to train the predictor.
    - **DatasetGroupArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) of the dataset group.
    """


_ClientCreatePredictorResponseTypeDef = TypedDict(
    "_ClientCreatePredictorResponseTypeDef", {"PredictorArn": str}, total=False
)


class ClientCreatePredictorResponseTypeDef(_ClientCreatePredictorResponseTypeDef):
    """
    - *(dict) --*

      - **PredictorArn** *(string) --*

        The Amazon Resource Name (ARN) of the predictor.
    """


_ClientDescribeDatasetGroupResponseTypeDef = TypedDict(
    "_ClientDescribeDatasetGroupResponseTypeDef",
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


class ClientDescribeDatasetGroupResponseTypeDef(_ClientDescribeDatasetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **DatasetGroupName** *(string) --*

        The name of the dataset group.
    """


_ClientDescribeDatasetImportJobResponseDataSourceS3ConfigTypeDef = TypedDict(
    "_ClientDescribeDatasetImportJobResponseDataSourceS3ConfigTypeDef",
    {"Path": str, "RoleArn": str, "KMSKeyArn": str},
    total=False,
)


class ClientDescribeDatasetImportJobResponseDataSourceS3ConfigTypeDef(
    _ClientDescribeDatasetImportJobResponseDataSourceS3ConfigTypeDef
):
    pass


_ClientDescribeDatasetImportJobResponseDataSourceTypeDef = TypedDict(
    "_ClientDescribeDatasetImportJobResponseDataSourceTypeDef",
    {"S3Config": ClientDescribeDatasetImportJobResponseDataSourceS3ConfigTypeDef},
    total=False,
)


class ClientDescribeDatasetImportJobResponseDataSourceTypeDef(
    _ClientDescribeDatasetImportJobResponseDataSourceTypeDef
):
    pass


_ClientDescribeDatasetImportJobResponseFieldStatisticsTypeDef = TypedDict(
    "_ClientDescribeDatasetImportJobResponseFieldStatisticsTypeDef",
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


class ClientDescribeDatasetImportJobResponseFieldStatisticsTypeDef(
    _ClientDescribeDatasetImportJobResponseFieldStatisticsTypeDef
):
    pass


_ClientDescribeDatasetImportJobResponseTypeDef = TypedDict(
    "_ClientDescribeDatasetImportJobResponseTypeDef",
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


class ClientDescribeDatasetImportJobResponseTypeDef(_ClientDescribeDatasetImportJobResponseTypeDef):
    """
    - *(dict) --*

      - **DatasetImportJobName** *(string) --*

        The name of the dataset import job.
    """


_ClientDescribeDatasetResponseEncryptionConfigTypeDef = TypedDict(
    "_ClientDescribeDatasetResponseEncryptionConfigTypeDef",
    {"RoleArn": str, "KMSKeyArn": str},
    total=False,
)


class ClientDescribeDatasetResponseEncryptionConfigTypeDef(
    _ClientDescribeDatasetResponseEncryptionConfigTypeDef
):
    pass


_ClientDescribeDatasetResponseSchemaAttributesTypeDef = TypedDict(
    "_ClientDescribeDatasetResponseSchemaAttributesTypeDef",
    {"AttributeName": str, "AttributeType": Literal["string", "integer", "float", "timestamp"]},
    total=False,
)


class ClientDescribeDatasetResponseSchemaAttributesTypeDef(
    _ClientDescribeDatasetResponseSchemaAttributesTypeDef
):
    pass


_ClientDescribeDatasetResponseSchemaTypeDef = TypedDict(
    "_ClientDescribeDatasetResponseSchemaTypeDef",
    {"Attributes": List[ClientDescribeDatasetResponseSchemaAttributesTypeDef]},
    total=False,
)


class ClientDescribeDatasetResponseSchemaTypeDef(_ClientDescribeDatasetResponseSchemaTypeDef):
    pass


_ClientDescribeDatasetResponseTypeDef = TypedDict(
    "_ClientDescribeDatasetResponseTypeDef",
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


class ClientDescribeDatasetResponseTypeDef(_ClientDescribeDatasetResponseTypeDef):
    """
    - *(dict) --*

      - **DatasetArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset.
    """


_ClientDescribeForecastExportJobResponseDestinationS3ConfigTypeDef = TypedDict(
    "_ClientDescribeForecastExportJobResponseDestinationS3ConfigTypeDef",
    {"Path": str, "RoleArn": str, "KMSKeyArn": str},
    total=False,
)


class ClientDescribeForecastExportJobResponseDestinationS3ConfigTypeDef(
    _ClientDescribeForecastExportJobResponseDestinationS3ConfigTypeDef
):
    pass


_ClientDescribeForecastExportJobResponseDestinationTypeDef = TypedDict(
    "_ClientDescribeForecastExportJobResponseDestinationTypeDef",
    {"S3Config": ClientDescribeForecastExportJobResponseDestinationS3ConfigTypeDef},
    total=False,
)


class ClientDescribeForecastExportJobResponseDestinationTypeDef(
    _ClientDescribeForecastExportJobResponseDestinationTypeDef
):
    pass


_ClientDescribeForecastExportJobResponseTypeDef = TypedDict(
    "_ClientDescribeForecastExportJobResponseTypeDef",
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


class ClientDescribeForecastExportJobResponseTypeDef(
    _ClientDescribeForecastExportJobResponseTypeDef
):
    """
    - *(dict) --*

      - **ForecastExportJobArn** *(string) --*

        The ARN of the forecast export job.
    """


_ClientDescribeForecastResponseTypeDef = TypedDict(
    "_ClientDescribeForecastResponseTypeDef",
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


class ClientDescribeForecastResponseTypeDef(_ClientDescribeForecastResponseTypeDef):
    """
    - *(dict) --*

      - **ForecastArn** *(string) --*

        The forecast ARN as specified in the request.
    """


_ClientDescribePredictorResponseEncryptionConfigTypeDef = TypedDict(
    "_ClientDescribePredictorResponseEncryptionConfigTypeDef",
    {"RoleArn": str, "KMSKeyArn": str},
    total=False,
)


class ClientDescribePredictorResponseEncryptionConfigTypeDef(
    _ClientDescribePredictorResponseEncryptionConfigTypeDef
):
    pass


_ClientDescribePredictorResponseEvaluationParametersTypeDef = TypedDict(
    "_ClientDescribePredictorResponseEvaluationParametersTypeDef",
    {"NumberOfBacktestWindows": int, "BackTestWindowOffset": int},
    total=False,
)


class ClientDescribePredictorResponseEvaluationParametersTypeDef(
    _ClientDescribePredictorResponseEvaluationParametersTypeDef
):
    pass


_ClientDescribePredictorResponseFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef = TypedDict(
    "_ClientDescribePredictorResponseFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef",
    {"FeaturizationMethodName": str, "FeaturizationMethodParameters": Dict[str, str]},
    total=False,
)


class ClientDescribePredictorResponseFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef(
    _ClientDescribePredictorResponseFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef
):
    pass


_ClientDescribePredictorResponseFeaturizationConfigFeaturizationsTypeDef = TypedDict(
    "_ClientDescribePredictorResponseFeaturizationConfigFeaturizationsTypeDef",
    {
        "AttributeName": str,
        "FeaturizationPipeline": List[
            ClientDescribePredictorResponseFeaturizationConfigFeaturizationsFeaturizationPipelineTypeDef
        ],
    },
    total=False,
)


class ClientDescribePredictorResponseFeaturizationConfigFeaturizationsTypeDef(
    _ClientDescribePredictorResponseFeaturizationConfigFeaturizationsTypeDef
):
    pass


_ClientDescribePredictorResponseFeaturizationConfigTypeDef = TypedDict(
    "_ClientDescribePredictorResponseFeaturizationConfigTypeDef",
    {
        "ForecastFrequency": str,
        "ForecastDimensions": List[str],
        "Featurizations": List[
            ClientDescribePredictorResponseFeaturizationConfigFeaturizationsTypeDef
        ],
    },
    total=False,
)


class ClientDescribePredictorResponseFeaturizationConfigTypeDef(
    _ClientDescribePredictorResponseFeaturizationConfigTypeDef
):
    pass


_ClientDescribePredictorResponseHPOConfigParameterRangesCategoricalParameterRangesTypeDef = TypedDict(
    "_ClientDescribePredictorResponseHPOConfigParameterRangesCategoricalParameterRangesTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribePredictorResponseHPOConfigParameterRangesCategoricalParameterRangesTypeDef(
    _ClientDescribePredictorResponseHPOConfigParameterRangesCategoricalParameterRangesTypeDef
):
    pass


_ClientDescribePredictorResponseHPOConfigParameterRangesContinuousParameterRangesTypeDef = TypedDict(
    "_ClientDescribePredictorResponseHPOConfigParameterRangesContinuousParameterRangesTypeDef",
    {
        "Name": str,
        "MaxValue": float,
        "MinValue": float,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)


class ClientDescribePredictorResponseHPOConfigParameterRangesContinuousParameterRangesTypeDef(
    _ClientDescribePredictorResponseHPOConfigParameterRangesContinuousParameterRangesTypeDef
):
    pass


_ClientDescribePredictorResponseHPOConfigParameterRangesIntegerParameterRangesTypeDef = TypedDict(
    "_ClientDescribePredictorResponseHPOConfigParameterRangesIntegerParameterRangesTypeDef",
    {
        "Name": str,
        "MaxValue": int,
        "MinValue": int,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)


class ClientDescribePredictorResponseHPOConfigParameterRangesIntegerParameterRangesTypeDef(
    _ClientDescribePredictorResponseHPOConfigParameterRangesIntegerParameterRangesTypeDef
):
    pass


_ClientDescribePredictorResponseHPOConfigParameterRangesTypeDef = TypedDict(
    "_ClientDescribePredictorResponseHPOConfigParameterRangesTypeDef",
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


class ClientDescribePredictorResponseHPOConfigParameterRangesTypeDef(
    _ClientDescribePredictorResponseHPOConfigParameterRangesTypeDef
):
    pass


_ClientDescribePredictorResponseHPOConfigTypeDef = TypedDict(
    "_ClientDescribePredictorResponseHPOConfigTypeDef",
    {"ParameterRanges": ClientDescribePredictorResponseHPOConfigParameterRangesTypeDef},
    total=False,
)


class ClientDescribePredictorResponseHPOConfigTypeDef(
    _ClientDescribePredictorResponseHPOConfigTypeDef
):
    pass


_ClientDescribePredictorResponseInputDataConfigSupplementaryFeaturesTypeDef = TypedDict(
    "_ClientDescribePredictorResponseInputDataConfigSupplementaryFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribePredictorResponseInputDataConfigSupplementaryFeaturesTypeDef(
    _ClientDescribePredictorResponseInputDataConfigSupplementaryFeaturesTypeDef
):
    pass


_ClientDescribePredictorResponseInputDataConfigTypeDef = TypedDict(
    "_ClientDescribePredictorResponseInputDataConfigTypeDef",
    {
        "DatasetGroupArn": str,
        "SupplementaryFeatures": List[
            ClientDescribePredictorResponseInputDataConfigSupplementaryFeaturesTypeDef
        ],
    },
    total=False,
)


class ClientDescribePredictorResponseInputDataConfigTypeDef(
    _ClientDescribePredictorResponseInputDataConfigTypeDef
):
    pass


_ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTestWindowsTypeDef = TypedDict(
    "_ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTestWindowsTypeDef",
    {"TestWindowStart": datetime, "TestWindowEnd": datetime, "Status": str, "Message": str},
    total=False,
)


class ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTestWindowsTypeDef(
    _ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTestWindowsTypeDef
):
    pass


_ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTypeDef = TypedDict(
    "_ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTypeDef",
    {
        "AlgorithmArn": str,
        "TestWindows": List[
            ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTestWindowsTypeDef
        ],
    },
    total=False,
)


class ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTypeDef(
    _ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTypeDef
):
    pass


_ClientDescribePredictorResponsePredictorExecutionDetailsTypeDef = TypedDict(
    "_ClientDescribePredictorResponsePredictorExecutionDetailsTypeDef",
    {
        "PredictorExecutions": List[
            ClientDescribePredictorResponsePredictorExecutionDetailsPredictorExecutionsTypeDef
        ]
    },
    total=False,
)


class ClientDescribePredictorResponsePredictorExecutionDetailsTypeDef(
    _ClientDescribePredictorResponsePredictorExecutionDetailsTypeDef
):
    pass


_ClientDescribePredictorResponseTypeDef = TypedDict(
    "_ClientDescribePredictorResponseTypeDef",
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


class ClientDescribePredictorResponseTypeDef(_ClientDescribePredictorResponseTypeDef):
    """
    - *(dict) --*

      - **PredictorArn** *(string) --*

        The ARN of the predictor.
    """


_ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsWeightedQuantileLossesTypeDef = TypedDict(
    "_ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsWeightedQuantileLossesTypeDef",
    {"Quantile": float, "LossValue": float},
    total=False,
)


class ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsWeightedQuantileLossesTypeDef(
    _ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsWeightedQuantileLossesTypeDef
):
    pass


_ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsTypeDef = TypedDict(
    "_ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsTypeDef",
    {
        "RMSE": float,
        "WeightedQuantileLosses": List[
            ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsWeightedQuantileLossesTypeDef
        ],
    },
    total=False,
)


class ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsTypeDef(
    _ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsTypeDef
):
    pass


_ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsTypeDef = TypedDict(
    "_ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsTypeDef",
    {
        "TestWindowStart": datetime,
        "TestWindowEnd": datetime,
        "ItemCount": int,
        "EvaluationType": Literal["SUMMARY", "COMPUTED"],
        "Metrics": ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsMetricsTypeDef,
    },
    total=False,
)


class ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsTypeDef(
    _ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsTypeDef
):
    pass


_ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTypeDef = TypedDict(
    "_ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTypeDef",
    {
        "AlgorithmArn": str,
        "TestWindows": List[
            ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTestWindowsTypeDef
        ],
    },
    total=False,
)


class ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTypeDef(
    _ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTypeDef
):
    """
    - *(dict) --*

      The results of evaluating an algorithm. Returned as part of the  GetAccuracyMetrics response.
      - **AlgorithmArn** *(string) --*

        The Amazon Resource Name (ARN) of the algorithm that was evaluated.
    """


_ClientGetAccuracyMetricsResponseTypeDef = TypedDict(
    "_ClientGetAccuracyMetricsResponseTypeDef",
    {
        "PredictorEvaluationResults": List[
            ClientGetAccuracyMetricsResponsePredictorEvaluationResultsTypeDef
        ]
    },
    total=False,
)


class ClientGetAccuracyMetricsResponseTypeDef(_ClientGetAccuracyMetricsResponseTypeDef):
    """
    - *(dict) --*

      - **PredictorEvaluationResults** *(list) --*

        An array of results from evaluating the predictor.
        - *(dict) --*

          The results of evaluating an algorithm. Returned as part of the  GetAccuracyMetrics
          response.
          - **AlgorithmArn** *(string) --*

            The Amazon Resource Name (ARN) of the algorithm that was evaluated.
    """


_ClientListDatasetGroupsResponseDatasetGroupsTypeDef = TypedDict(
    "_ClientListDatasetGroupsResponseDatasetGroupsTypeDef",
    {
        "DatasetGroupArn": str,
        "DatasetGroupName": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)


class ClientListDatasetGroupsResponseDatasetGroupsTypeDef(
    _ClientListDatasetGroupsResponseDatasetGroupsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the dataset group properties used in the  ListDatasetGroups operation.
      To get the complete set of properties, call the  DescribeDatasetGroup operation, and provide
      the ``DatasetGroupArn`` .
      - **DatasetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset group.
    """


_ClientListDatasetGroupsResponseTypeDef = TypedDict(
    "_ClientListDatasetGroupsResponseTypeDef",
    {"DatasetGroups": List[ClientListDatasetGroupsResponseDatasetGroupsTypeDef], "NextToken": str},
    total=False,
)


class ClientListDatasetGroupsResponseTypeDef(_ClientListDatasetGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **DatasetGroups** *(list) --*

        An array of objects that summarize each dataset group's properties.
        - *(dict) --*

          Provides a summary of the dataset group properties used in the  ListDatasetGroups
          operation. To get the complete set of properties, call the  DescribeDatasetGroup
          operation, and provide the ``DatasetGroupArn`` .
          - **DatasetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the dataset group.
    """


_ClientListDatasetImportJobsFiltersTypeDef = TypedDict(
    "_ClientListDatasetImportJobsFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)


class ClientListDatasetImportJobsFiltersTypeDef(_ClientListDatasetImportJobsFiltersTypeDef):
    pass


_ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceS3ConfigTypeDef = TypedDict(
    "_ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceS3ConfigTypeDef",
    {"Path": str, "RoleArn": str, "KMSKeyArn": str},
    total=False,
)


class ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceS3ConfigTypeDef(
    _ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceS3ConfigTypeDef
):
    pass


_ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceTypeDef = TypedDict(
    "_ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceTypeDef",
    {"S3Config": ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceS3ConfigTypeDef},
    total=False,
)


class ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceTypeDef(
    _ClientListDatasetImportJobsResponseDatasetImportJobsDataSourceTypeDef
):
    pass


_ClientListDatasetImportJobsResponseDatasetImportJobsTypeDef = TypedDict(
    "_ClientListDatasetImportJobsResponseDatasetImportJobsTypeDef",
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


class ClientListDatasetImportJobsResponseDatasetImportJobsTypeDef(
    _ClientListDatasetImportJobsResponseDatasetImportJobsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the dataset import job properties used in the  ListDatasetImportJobs
      operation. To get the complete set of properties, call the  DescribeDatasetImportJob
      operation, and provide the ``DatasetImportJobArn`` .
      - **DatasetImportJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset import job.
    """


_ClientListDatasetImportJobsResponseTypeDef = TypedDict(
    "_ClientListDatasetImportJobsResponseTypeDef",
    {
        "DatasetImportJobs": List[ClientListDatasetImportJobsResponseDatasetImportJobsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListDatasetImportJobsResponseTypeDef(_ClientListDatasetImportJobsResponseTypeDef):
    """
    - *(dict) --*

      - **DatasetImportJobs** *(list) --*

        An array of objects that summarize each dataset import job's properties.
        - *(dict) --*

          Provides a summary of the dataset import job properties used in the  ListDatasetImportJobs
          operation. To get the complete set of properties, call the  DescribeDatasetImportJob
          operation, and provide the ``DatasetImportJobArn`` .
          - **DatasetImportJobArn** *(string) --*

            The Amazon Resource Name (ARN) of the dataset import job.
    """


_ClientListDatasetsResponseDatasetsTypeDef = TypedDict(
    "_ClientListDatasetsResponseDatasetsTypeDef",
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


class ClientListDatasetsResponseDatasetsTypeDef(_ClientListDatasetsResponseDatasetsTypeDef):
    """
    - *(dict) --*

      Provides a summary of the dataset properties used in the  ListDatasets operation. To get the
      complete set of properties, call the  DescribeDataset operation, and provide the
      ``DatasetArn`` .
      - **DatasetArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset.
    """


_ClientListDatasetsResponseTypeDef = TypedDict(
    "_ClientListDatasetsResponseTypeDef",
    {"Datasets": List[ClientListDatasetsResponseDatasetsTypeDef], "NextToken": str},
    total=False,
)


class ClientListDatasetsResponseTypeDef(_ClientListDatasetsResponseTypeDef):
    """
    - *(dict) --*

      - **Datasets** *(list) --*

        An array of objects that summarize each dataset's properties.
        - *(dict) --*

          Provides a summary of the dataset properties used in the  ListDatasets operation. To get
          the complete set of properties, call the  DescribeDataset operation, and provide the
          ``DatasetArn`` .
          - **DatasetArn** *(string) --*

            The Amazon Resource Name (ARN) of the dataset.
    """


_ClientListForecastExportJobsFiltersTypeDef = TypedDict(
    "_ClientListForecastExportJobsFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)


class ClientListForecastExportJobsFiltersTypeDef(_ClientListForecastExportJobsFiltersTypeDef):
    pass


_ClientListForecastExportJobsResponseForecastExportJobsDestinationS3ConfigTypeDef = TypedDict(
    "_ClientListForecastExportJobsResponseForecastExportJobsDestinationS3ConfigTypeDef",
    {"Path": str, "RoleArn": str, "KMSKeyArn": str},
    total=False,
)


class ClientListForecastExportJobsResponseForecastExportJobsDestinationS3ConfigTypeDef(
    _ClientListForecastExportJobsResponseForecastExportJobsDestinationS3ConfigTypeDef
):
    pass


_ClientListForecastExportJobsResponseForecastExportJobsDestinationTypeDef = TypedDict(
    "_ClientListForecastExportJobsResponseForecastExportJobsDestinationTypeDef",
    {"S3Config": ClientListForecastExportJobsResponseForecastExportJobsDestinationS3ConfigTypeDef},
    total=False,
)


class ClientListForecastExportJobsResponseForecastExportJobsDestinationTypeDef(
    _ClientListForecastExportJobsResponseForecastExportJobsDestinationTypeDef
):
    pass


_ClientListForecastExportJobsResponseForecastExportJobsTypeDef = TypedDict(
    "_ClientListForecastExportJobsResponseForecastExportJobsTypeDef",
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


class ClientListForecastExportJobsResponseForecastExportJobsTypeDef(
    _ClientListForecastExportJobsResponseForecastExportJobsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the forecast export job properties used in the  ListForecastExportJobs
      operation. To get the complete set of properties, call the  DescribeForecastExportJob
      operation, and provide the listed ``ForecastExportJobArn`` .
      - **ForecastExportJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the forecast export job.
    """


_ClientListForecastExportJobsResponseTypeDef = TypedDict(
    "_ClientListForecastExportJobsResponseTypeDef",
    {
        "ForecastExportJobs": List[ClientListForecastExportJobsResponseForecastExportJobsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListForecastExportJobsResponseTypeDef(_ClientListForecastExportJobsResponseTypeDef):
    """
    - *(dict) --*

      - **ForecastExportJobs** *(list) --*

        An array of objects that summarize each export job's properties.
        - *(dict) --*

          Provides a summary of the forecast export job properties used in the
          ListForecastExportJobs operation. To get the complete set of properties, call the
          DescribeForecastExportJob operation, and provide the listed ``ForecastExportJobArn`` .
          - **ForecastExportJobArn** *(string) --*

            The Amazon Resource Name (ARN) of the forecast export job.
    """


_ClientListForecastsFiltersTypeDef = TypedDict(
    "_ClientListForecastsFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)


class ClientListForecastsFiltersTypeDef(_ClientListForecastsFiltersTypeDef):
    pass


_ClientListForecastsResponseForecastsTypeDef = TypedDict(
    "_ClientListForecastsResponseForecastsTypeDef",
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


class ClientListForecastsResponseForecastsTypeDef(_ClientListForecastsResponseForecastsTypeDef):
    """
    - *(dict) --*

      Provides a summary of the forecast properties used in the  ListForecasts operation. To get the
      complete set of properties, call the  DescribeForecast operation, and provide the
      ``ForecastArn`` that is listed in the summary.
      - **ForecastArn** *(string) --*

        The ARN of the forecast.
    """


_ClientListForecastsResponseTypeDef = TypedDict(
    "_ClientListForecastsResponseTypeDef",
    {"Forecasts": List[ClientListForecastsResponseForecastsTypeDef], "NextToken": str},
    total=False,
)


class ClientListForecastsResponseTypeDef(_ClientListForecastsResponseTypeDef):
    """
    - *(dict) --*

      - **Forecasts** *(list) --*

        An array of objects that summarize each forecast's properties.
        - *(dict) --*

          Provides a summary of the forecast properties used in the  ListForecasts operation. To get
          the complete set of properties, call the  DescribeForecast operation, and provide the
          ``ForecastArn`` that is listed in the summary.
          - **ForecastArn** *(string) --*

            The ARN of the forecast.
    """


_ClientListPredictorsFiltersTypeDef = TypedDict(
    "_ClientListPredictorsFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)


class ClientListPredictorsFiltersTypeDef(_ClientListPredictorsFiltersTypeDef):
    pass


_ClientListPredictorsResponsePredictorsTypeDef = TypedDict(
    "_ClientListPredictorsResponsePredictorsTypeDef",
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


class ClientListPredictorsResponsePredictorsTypeDef(_ClientListPredictorsResponsePredictorsTypeDef):
    """
    - *(dict) --*

      Provides a summary of the predictor properties that are used in the  ListPredictors operation.
      To get the complete set of properties, call the  DescribePredictor operation, and provide the
      listed ``PredictorArn`` .
      - **PredictorArn** *(string) --*

        The ARN of the predictor.
    """


_ClientListPredictorsResponseTypeDef = TypedDict(
    "_ClientListPredictorsResponseTypeDef",
    {"Predictors": List[ClientListPredictorsResponsePredictorsTypeDef], "NextToken": str},
    total=False,
)


class ClientListPredictorsResponseTypeDef(_ClientListPredictorsResponseTypeDef):
    """
    - *(dict) --*

      - **Predictors** *(list) --*

        An array of objects that summarize each predictor's properties.
        - *(dict) --*

          Provides a summary of the predictor properties that are used in the  ListPredictors
          operation. To get the complete set of properties, call the  DescribePredictor operation,
          and provide the listed ``PredictorArn`` .
          - **PredictorArn** *(string) --*

            The ARN of the predictor.
    """


_ListDatasetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDatasetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDatasetGroupsPaginatePaginationConfigTypeDef(
    _ListDatasetGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDatasetGroupsPaginateResponseDatasetGroupsTypeDef = TypedDict(
    "_ListDatasetGroupsPaginateResponseDatasetGroupsTypeDef",
    {
        "DatasetGroupArn": str,
        "DatasetGroupName": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)


class ListDatasetGroupsPaginateResponseDatasetGroupsTypeDef(
    _ListDatasetGroupsPaginateResponseDatasetGroupsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the dataset group properties used in the  ListDatasetGroups operation.
      To get the complete set of properties, call the  DescribeDatasetGroup operation, and provide
      the ``DatasetGroupArn`` .
      - **DatasetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset group.
    """


_ListDatasetGroupsPaginateResponseTypeDef = TypedDict(
    "_ListDatasetGroupsPaginateResponseTypeDef",
    {"DatasetGroups": List[ListDatasetGroupsPaginateResponseDatasetGroupsTypeDef]},
    total=False,
)


class ListDatasetGroupsPaginateResponseTypeDef(_ListDatasetGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **DatasetGroups** *(list) --*

        An array of objects that summarize each dataset group's properties.
        - *(dict) --*

          Provides a summary of the dataset group properties used in the  ListDatasetGroups
          operation. To get the complete set of properties, call the  DescribeDatasetGroup
          operation, and provide the ``DatasetGroupArn`` .
          - **DatasetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the dataset group.
    """


_ListDatasetImportJobsPaginateFiltersTypeDef = TypedDict(
    "_ListDatasetImportJobsPaginateFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)


class ListDatasetImportJobsPaginateFiltersTypeDef(_ListDatasetImportJobsPaginateFiltersTypeDef):
    pass


_ListDatasetImportJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDatasetImportJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDatasetImportJobsPaginatePaginationConfigTypeDef(
    _ListDatasetImportJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceS3ConfigTypeDef = TypedDict(
    "_ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceS3ConfigTypeDef",
    {"Path": str, "RoleArn": str, "KMSKeyArn": str},
    total=False,
)


class ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceS3ConfigTypeDef(
    _ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceS3ConfigTypeDef
):
    pass


_ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceTypeDef = TypedDict(
    "_ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceTypeDef",
    {"S3Config": ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceS3ConfigTypeDef},
    total=False,
)


class ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceTypeDef(
    _ListDatasetImportJobsPaginateResponseDatasetImportJobsDataSourceTypeDef
):
    pass


_ListDatasetImportJobsPaginateResponseDatasetImportJobsTypeDef = TypedDict(
    "_ListDatasetImportJobsPaginateResponseDatasetImportJobsTypeDef",
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


class ListDatasetImportJobsPaginateResponseDatasetImportJobsTypeDef(
    _ListDatasetImportJobsPaginateResponseDatasetImportJobsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the dataset import job properties used in the  ListDatasetImportJobs
      operation. To get the complete set of properties, call the  DescribeDatasetImportJob
      operation, and provide the ``DatasetImportJobArn`` .
      - **DatasetImportJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset import job.
    """


_ListDatasetImportJobsPaginateResponseTypeDef = TypedDict(
    "_ListDatasetImportJobsPaginateResponseTypeDef",
    {"DatasetImportJobs": List[ListDatasetImportJobsPaginateResponseDatasetImportJobsTypeDef]},
    total=False,
)


class ListDatasetImportJobsPaginateResponseTypeDef(_ListDatasetImportJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **DatasetImportJobs** *(list) --*

        An array of objects that summarize each dataset import job's properties.
        - *(dict) --*

          Provides a summary of the dataset import job properties used in the  ListDatasetImportJobs
          operation. To get the complete set of properties, call the  DescribeDatasetImportJob
          operation, and provide the ``DatasetImportJobArn`` .
          - **DatasetImportJobArn** *(string) --*

            The Amazon Resource Name (ARN) of the dataset import job.
    """


_ListDatasetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDatasetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDatasetsPaginatePaginationConfigTypeDef(_ListDatasetsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDatasetsPaginateResponseDatasetsTypeDef = TypedDict(
    "_ListDatasetsPaginateResponseDatasetsTypeDef",
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


class ListDatasetsPaginateResponseDatasetsTypeDef(_ListDatasetsPaginateResponseDatasetsTypeDef):
    """
    - *(dict) --*

      Provides a summary of the dataset properties used in the  ListDatasets operation. To get the
      complete set of properties, call the  DescribeDataset operation, and provide the
      ``DatasetArn`` .
      - **DatasetArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset.
    """


_ListDatasetsPaginateResponseTypeDef = TypedDict(
    "_ListDatasetsPaginateResponseTypeDef",
    {"Datasets": List[ListDatasetsPaginateResponseDatasetsTypeDef]},
    total=False,
)


class ListDatasetsPaginateResponseTypeDef(_ListDatasetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Datasets** *(list) --*

        An array of objects that summarize each dataset's properties.
        - *(dict) --*

          Provides a summary of the dataset properties used in the  ListDatasets operation. To get
          the complete set of properties, call the  DescribeDataset operation, and provide the
          ``DatasetArn`` .
          - **DatasetArn** *(string) --*

            The Amazon Resource Name (ARN) of the dataset.
    """


_ListForecastExportJobsPaginateFiltersTypeDef = TypedDict(
    "_ListForecastExportJobsPaginateFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)


class ListForecastExportJobsPaginateFiltersTypeDef(_ListForecastExportJobsPaginateFiltersTypeDef):
    pass


_ListForecastExportJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListForecastExportJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListForecastExportJobsPaginatePaginationConfigTypeDef(
    _ListForecastExportJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListForecastExportJobsPaginateResponseForecastExportJobsDestinationS3ConfigTypeDef = TypedDict(
    "_ListForecastExportJobsPaginateResponseForecastExportJobsDestinationS3ConfigTypeDef",
    {"Path": str, "RoleArn": str, "KMSKeyArn": str},
    total=False,
)


class ListForecastExportJobsPaginateResponseForecastExportJobsDestinationS3ConfigTypeDef(
    _ListForecastExportJobsPaginateResponseForecastExportJobsDestinationS3ConfigTypeDef
):
    pass


_ListForecastExportJobsPaginateResponseForecastExportJobsDestinationTypeDef = TypedDict(
    "_ListForecastExportJobsPaginateResponseForecastExportJobsDestinationTypeDef",
    {
        "S3Config": ListForecastExportJobsPaginateResponseForecastExportJobsDestinationS3ConfigTypeDef
    },
    total=False,
)


class ListForecastExportJobsPaginateResponseForecastExportJobsDestinationTypeDef(
    _ListForecastExportJobsPaginateResponseForecastExportJobsDestinationTypeDef
):
    pass


_ListForecastExportJobsPaginateResponseForecastExportJobsTypeDef = TypedDict(
    "_ListForecastExportJobsPaginateResponseForecastExportJobsTypeDef",
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


class ListForecastExportJobsPaginateResponseForecastExportJobsTypeDef(
    _ListForecastExportJobsPaginateResponseForecastExportJobsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the forecast export job properties used in the  ListForecastExportJobs
      operation. To get the complete set of properties, call the  DescribeForecastExportJob
      operation, and provide the listed ``ForecastExportJobArn`` .
      - **ForecastExportJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the forecast export job.
    """


_ListForecastExportJobsPaginateResponseTypeDef = TypedDict(
    "_ListForecastExportJobsPaginateResponseTypeDef",
    {"ForecastExportJobs": List[ListForecastExportJobsPaginateResponseForecastExportJobsTypeDef]},
    total=False,
)


class ListForecastExportJobsPaginateResponseTypeDef(_ListForecastExportJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ForecastExportJobs** *(list) --*

        An array of objects that summarize each export job's properties.
        - *(dict) --*

          Provides a summary of the forecast export job properties used in the
          ListForecastExportJobs operation. To get the complete set of properties, call the
          DescribeForecastExportJob operation, and provide the listed ``ForecastExportJobArn`` .
          - **ForecastExportJobArn** *(string) --*

            The Amazon Resource Name (ARN) of the forecast export job.
    """


_ListForecastsPaginateFiltersTypeDef = TypedDict(
    "_ListForecastsPaginateFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)


class ListForecastsPaginateFiltersTypeDef(_ListForecastsPaginateFiltersTypeDef):
    pass


_ListForecastsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListForecastsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListForecastsPaginatePaginationConfigTypeDef(_ListForecastsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListForecastsPaginateResponseForecastsTypeDef = TypedDict(
    "_ListForecastsPaginateResponseForecastsTypeDef",
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


class ListForecastsPaginateResponseForecastsTypeDef(_ListForecastsPaginateResponseForecastsTypeDef):
    """
    - *(dict) --*

      Provides a summary of the forecast properties used in the  ListForecasts operation. To get the
      complete set of properties, call the  DescribeForecast operation, and provide the
      ``ForecastArn`` that is listed in the summary.
      - **ForecastArn** *(string) --*

        The ARN of the forecast.
    """


_ListForecastsPaginateResponseTypeDef = TypedDict(
    "_ListForecastsPaginateResponseTypeDef",
    {"Forecasts": List[ListForecastsPaginateResponseForecastsTypeDef]},
    total=False,
)


class ListForecastsPaginateResponseTypeDef(_ListForecastsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Forecasts** *(list) --*

        An array of objects that summarize each forecast's properties.
        - *(dict) --*

          Provides a summary of the forecast properties used in the  ListForecasts operation. To get
          the complete set of properties, call the  DescribeForecast operation, and provide the
          ``ForecastArn`` that is listed in the summary.
          - **ForecastArn** *(string) --*

            The ARN of the forecast.
    """


_ListPredictorsPaginateFiltersTypeDef = TypedDict(
    "_ListPredictorsPaginateFiltersTypeDef",
    {"Key": str, "Value": str, "Condition": Literal["IS", "IS_NOT"]},
    total=False,
)


class ListPredictorsPaginateFiltersTypeDef(_ListPredictorsPaginateFiltersTypeDef):
    pass


_ListPredictorsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPredictorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPredictorsPaginatePaginationConfigTypeDef(_ListPredictorsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPredictorsPaginateResponsePredictorsTypeDef = TypedDict(
    "_ListPredictorsPaginateResponsePredictorsTypeDef",
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


class ListPredictorsPaginateResponsePredictorsTypeDef(
    _ListPredictorsPaginateResponsePredictorsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the predictor properties that are used in the  ListPredictors operation.
      To get the complete set of properties, call the  DescribePredictor operation, and provide the
      listed ``PredictorArn`` .
      - **PredictorArn** *(string) --*

        The ARN of the predictor.
    """


_ListPredictorsPaginateResponseTypeDef = TypedDict(
    "_ListPredictorsPaginateResponseTypeDef",
    {"Predictors": List[ListPredictorsPaginateResponsePredictorsTypeDef]},
    total=False,
)


class ListPredictorsPaginateResponseTypeDef(_ListPredictorsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Predictors** *(list) --*

        An array of objects that summarize each predictor's properties.
        - *(dict) --*

          Provides a summary of the predictor properties that are used in the  ListPredictors
          operation. To get the complete set of properties, call the  DescribePredictor operation,
          and provide the listed ``PredictorArn`` .
          - **PredictorArn** *(string) --*

            The ARN of the predictor.
    """
