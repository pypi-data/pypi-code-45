"Main interface for personalize service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef",
    "ClientCreateBatchInferenceJobJobInputTypeDef",
    "ClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef",
    "ClientCreateBatchInferenceJobJobOutputTypeDef",
    "ClientCreateBatchInferenceJobResponseTypeDef",
    "ClientCreateCampaignResponseTypeDef",
    "ClientCreateDatasetGroupResponseTypeDef",
    "ClientCreateDatasetImportJobDataSourceTypeDef",
    "ClientCreateDatasetImportJobResponseTypeDef",
    "ClientCreateDatasetResponseTypeDef",
    "ClientCreateEventTrackerResponseTypeDef",
    "ClientCreateSchemaResponseTypeDef",
    "ClientCreateSolutionResponseTypeDef",
    "ClientCreateSolutionSolutionConfigautoMLConfigTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfighpoObjectiveTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfighpoResourceConfigTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfigTypeDef",
    "ClientCreateSolutionSolutionConfigTypeDef",
    "ClientCreateSolutionVersionResponseTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmTypeDef",
    "ClientDescribeAlgorithmResponseTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef",
    "ClientDescribeBatchInferenceJobResponseTypeDef",
    "ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef",
    "ClientDescribeCampaignResponsecampaignTypeDef",
    "ClientDescribeCampaignResponseTypeDef",
    "ClientDescribeDatasetGroupResponsedatasetGroupTypeDef",
    "ClientDescribeDatasetGroupResponseTypeDef",
    "ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef",
    "ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef",
    "ClientDescribeDatasetImportJobResponseTypeDef",
    "ClientDescribeDatasetResponsedatasetTypeDef",
    "ClientDescribeDatasetResponseTypeDef",
    "ClientDescribeEventTrackerResponseeventTrackerTypeDef",
    "ClientDescribeEventTrackerResponseTypeDef",
    "ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef",
    "ClientDescribeFeatureTransformationResponseTypeDef",
    "ClientDescribeRecipeResponserecipeTypeDef",
    "ClientDescribeRecipeResponseTypeDef",
    "ClientDescribeSchemaResponseschemaTypeDef",
    "ClientDescribeSchemaResponseTypeDef",
    "ClientDescribeSolutionResponsesolutionautoMLResultTypeDef",
    "ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef",
    "ClientDescribeSolutionResponsesolutionTypeDef",
    "ClientDescribeSolutionResponseTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionTypeDef",
    "ClientDescribeSolutionVersionResponseTypeDef",
    "ClientGetSolutionMetricsResponseTypeDef",
    "ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef",
    "ClientListBatchInferenceJobsResponseTypeDef",
    "ClientListCampaignsResponsecampaignsTypeDef",
    "ClientListCampaignsResponseTypeDef",
    "ClientListDatasetGroupsResponsedatasetGroupsTypeDef",
    "ClientListDatasetGroupsResponseTypeDef",
    "ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef",
    "ClientListDatasetImportJobsResponseTypeDef",
    "ClientListDatasetsResponsedatasetsTypeDef",
    "ClientListDatasetsResponseTypeDef",
    "ClientListEventTrackersResponseeventTrackersTypeDef",
    "ClientListEventTrackersResponseTypeDef",
    "ClientListRecipesResponserecipesTypeDef",
    "ClientListRecipesResponseTypeDef",
    "ClientListSchemasResponseschemasTypeDef",
    "ClientListSchemasResponseTypeDef",
    "ClientListSolutionVersionsResponsesolutionVersionsTypeDef",
    "ClientListSolutionVersionsResponseTypeDef",
    "ClientListSolutionsResponsesolutionsTypeDef",
    "ClientListSolutionsResponseTypeDef",
    "ClientUpdateCampaignResponseTypeDef",
    "ListBatchInferenceJobsPaginatePaginationConfigTypeDef",
    "ListBatchInferenceJobsPaginateResponsebatchInferenceJobsTypeDef",
    "ListBatchInferenceJobsPaginateResponseTypeDef",
    "ListCampaignsPaginatePaginationConfigTypeDef",
    "ListCampaignsPaginateResponsecampaignsTypeDef",
    "ListCampaignsPaginateResponseTypeDef",
    "ListDatasetGroupsPaginatePaginationConfigTypeDef",
    "ListDatasetGroupsPaginateResponsedatasetGroupsTypeDef",
    "ListDatasetGroupsPaginateResponseTypeDef",
    "ListDatasetImportJobsPaginatePaginationConfigTypeDef",
    "ListDatasetImportJobsPaginateResponsedatasetImportJobsTypeDef",
    "ListDatasetImportJobsPaginateResponseTypeDef",
    "ListDatasetsPaginatePaginationConfigTypeDef",
    "ListDatasetsPaginateResponsedatasetsTypeDef",
    "ListDatasetsPaginateResponseTypeDef",
    "ListEventTrackersPaginatePaginationConfigTypeDef",
    "ListEventTrackersPaginateResponseeventTrackersTypeDef",
    "ListEventTrackersPaginateResponseTypeDef",
    "ListRecipesPaginatePaginationConfigTypeDef",
    "ListRecipesPaginateResponserecipesTypeDef",
    "ListRecipesPaginateResponseTypeDef",
    "ListSchemasPaginatePaginationConfigTypeDef",
    "ListSchemasPaginateResponseschemasTypeDef",
    "ListSchemasPaginateResponseTypeDef",
    "ListSolutionVersionsPaginatePaginationConfigTypeDef",
    "ListSolutionVersionsPaginateResponsesolutionVersionsTypeDef",
    "ListSolutionVersionsPaginateResponseTypeDef",
    "ListSolutionsPaginatePaginationConfigTypeDef",
    "ListSolutionsPaginateResponsesolutionsTypeDef",
    "ListSolutionsPaginateResponseTypeDef",
)


_RequiredClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef = TypedDict(
    "_RequiredClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef", {"path": str}
)
_OptionalClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef = TypedDict(
    "_OptionalClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef",
    {"kmsKeyArn": str},
    total=False,
)


class ClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef(
    _RequiredClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef,
    _OptionalClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef,
):
    """
    - **s3DataSource** *(dict) --***[REQUIRED]**

      The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket must be
      in the same region as the API endpoint you are calling.
      - **path** *(string) --***[REQUIRED]**

        The file path of the Amazon S3 bucket.
    """


_ClientCreateBatchInferenceJobJobInputTypeDef = TypedDict(
    "_ClientCreateBatchInferenceJobJobInputTypeDef",
    {"s3DataSource": ClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef},
)


class ClientCreateBatchInferenceJobJobInputTypeDef(_ClientCreateBatchInferenceJobJobInputTypeDef):
    """
    The Amazon S3 path that leads to the input file to base your recommendations on. The input
    material must be in JSON format.
    - **s3DataSource** *(dict) --***[REQUIRED]**

      The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket must be
      in the same region as the API endpoint you are calling.
      - **path** *(string) --***[REQUIRED]**

        The file path of the Amazon S3 bucket.
    """


_RequiredClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef = TypedDict(
    "_RequiredClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef", {"path": str}
)
_OptionalClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef = TypedDict(
    "_OptionalClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef",
    {"kmsKeyArn": str},
    total=False,
)


class ClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef(
    _RequiredClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef,
    _OptionalClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef,
):
    """
    - **s3DataDestination** *(dict) --***[REQUIRED]**

      Information on the Amazon S3 bucket in which the batch inference job's output is stored.
      - **path** *(string) --***[REQUIRED]**

        The file path of the Amazon S3 bucket.
    """


_ClientCreateBatchInferenceJobJobOutputTypeDef = TypedDict(
    "_ClientCreateBatchInferenceJobJobOutputTypeDef",
    {"s3DataDestination": ClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef},
)


class ClientCreateBatchInferenceJobJobOutputTypeDef(_ClientCreateBatchInferenceJobJobOutputTypeDef):
    """
    The path to the Amazon S3 bucket where the job's output will be stored.
    - **s3DataDestination** *(dict) --***[REQUIRED]**

      Information on the Amazon S3 bucket in which the batch inference job's output is stored.
      - **path** *(string) --***[REQUIRED]**

        The file path of the Amazon S3 bucket.
    """


_ClientCreateBatchInferenceJobResponseTypeDef = TypedDict(
    "_ClientCreateBatchInferenceJobResponseTypeDef", {"batchInferenceJobArn": str}, total=False
)


class ClientCreateBatchInferenceJobResponseTypeDef(_ClientCreateBatchInferenceJobResponseTypeDef):
    """
    - *(dict) --*

      - **batchInferenceJobArn** *(string) --*

        The ARN of the batch inference job.
    """


_ClientCreateCampaignResponseTypeDef = TypedDict(
    "_ClientCreateCampaignResponseTypeDef", {"campaignArn": str}, total=False
)


class ClientCreateCampaignResponseTypeDef(_ClientCreateCampaignResponseTypeDef):
    """
    - *(dict) --*

      - **campaignArn** *(string) --*

        The Amazon Resource Name (ARN) of the campaign.
    """


_ClientCreateDatasetGroupResponseTypeDef = TypedDict(
    "_ClientCreateDatasetGroupResponseTypeDef", {"datasetGroupArn": str}, total=False
)


class ClientCreateDatasetGroupResponseTypeDef(_ClientCreateDatasetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **datasetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the new dataset group.
    """


_ClientCreateDatasetImportJobDataSourceTypeDef = TypedDict(
    "_ClientCreateDatasetImportJobDataSourceTypeDef", {"dataLocation": str}, total=False
)


class ClientCreateDatasetImportJobDataSourceTypeDef(_ClientCreateDatasetImportJobDataSourceTypeDef):
    """
    The Amazon S3 bucket that contains the training data to import.
    - **dataLocation** *(string) --*

      The path to the Amazon S3 bucket where the data that you want to upload to your dataset is
      stored. For example:

        ``s3://bucket-name/training-data.csv``
    """


_ClientCreateDatasetImportJobResponseTypeDef = TypedDict(
    "_ClientCreateDatasetImportJobResponseTypeDef", {"datasetImportJobArn": str}, total=False
)


class ClientCreateDatasetImportJobResponseTypeDef(_ClientCreateDatasetImportJobResponseTypeDef):
    """
    - *(dict) --*

      - **datasetImportJobArn** *(string) --*

        The ARN of the dataset import job.
    """


_ClientCreateDatasetResponseTypeDef = TypedDict(
    "_ClientCreateDatasetResponseTypeDef", {"datasetArn": str}, total=False
)


class ClientCreateDatasetResponseTypeDef(_ClientCreateDatasetResponseTypeDef):
    """
    - *(dict) --*

      - **datasetArn** *(string) --*

        The ARN of the dataset.
    """


_ClientCreateEventTrackerResponseTypeDef = TypedDict(
    "_ClientCreateEventTrackerResponseTypeDef",
    {"eventTrackerArn": str, "trackingId": str},
    total=False,
)


class ClientCreateEventTrackerResponseTypeDef(_ClientCreateEventTrackerResponseTypeDef):
    """
    - *(dict) --*

      - **eventTrackerArn** *(string) --*

        The ARN of the event tracker.
    """


_ClientCreateSchemaResponseTypeDef = TypedDict(
    "_ClientCreateSchemaResponseTypeDef", {"schemaArn": str}, total=False
)


class ClientCreateSchemaResponseTypeDef(_ClientCreateSchemaResponseTypeDef):
    """
    - *(dict) --*

      - **schemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the created schema.
    """


_ClientCreateSolutionResponseTypeDef = TypedDict(
    "_ClientCreateSolutionResponseTypeDef", {"solutionArn": str}, total=False
)


class ClientCreateSolutionResponseTypeDef(_ClientCreateSolutionResponseTypeDef):
    """
    - *(dict) --*

      - **solutionArn** *(string) --*

        The ARN of the solution.
    """


_ClientCreateSolutionSolutionConfigautoMLConfigTypeDef = TypedDict(
    "_ClientCreateSolutionSolutionConfigautoMLConfigTypeDef",
    {"metricName": str, "recipeList": List[str]},
    total=False,
)


class ClientCreateSolutionSolutionConfigautoMLConfigTypeDef(
    _ClientCreateSolutionSolutionConfigautoMLConfigTypeDef
):
    pass


_ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef = TypedDict(
    "_ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef(
    _ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
):
    pass


_ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef = TypedDict(
    "_ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    {"name": str, "minValue": float, "maxValue": float},
    total=False,
)


class ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef(
    _ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
):
    pass


_ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef = TypedDict(
    "_ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    {"name": str, "minValue": int, "maxValue": int},
    total=False,
)


class ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef(
    _ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
):
    pass


_ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef = TypedDict(
    "_ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List[
            ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
        ],
        "continuousHyperParameterRanges": List[
            ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
        ],
        "categoricalHyperParameterRanges": List[
            ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
        ],
    },
    total=False,
)


class ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef(
    _ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef
):
    pass


_ClientCreateSolutionSolutionConfighpoConfighpoObjectiveTypeDef = TypedDict(
    "_ClientCreateSolutionSolutionConfighpoConfighpoObjectiveTypeDef",
    {"type": str, "metricName": str, "metricRegex": str},
    total=False,
)


class ClientCreateSolutionSolutionConfighpoConfighpoObjectiveTypeDef(
    _ClientCreateSolutionSolutionConfighpoConfighpoObjectiveTypeDef
):
    pass


_ClientCreateSolutionSolutionConfighpoConfighpoResourceConfigTypeDef = TypedDict(
    "_ClientCreateSolutionSolutionConfighpoConfighpoResourceConfigTypeDef",
    {"maxNumberOfTrainingJobs": str, "maxParallelTrainingJobs": str},
    total=False,
)


class ClientCreateSolutionSolutionConfighpoConfighpoResourceConfigTypeDef(
    _ClientCreateSolutionSolutionConfighpoConfighpoResourceConfigTypeDef
):
    pass


_ClientCreateSolutionSolutionConfighpoConfigTypeDef = TypedDict(
    "_ClientCreateSolutionSolutionConfighpoConfigTypeDef",
    {
        "hpoObjective": ClientCreateSolutionSolutionConfighpoConfighpoObjectiveTypeDef,
        "hpoResourceConfig": ClientCreateSolutionSolutionConfighpoConfighpoResourceConfigTypeDef,
        "algorithmHyperParameterRanges": ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef,
    },
    total=False,
)


class ClientCreateSolutionSolutionConfighpoConfigTypeDef(
    _ClientCreateSolutionSolutionConfighpoConfigTypeDef
):
    pass


_ClientCreateSolutionSolutionConfigTypeDef = TypedDict(
    "_ClientCreateSolutionSolutionConfigTypeDef",
    {
        "eventValueThreshold": str,
        "hpoConfig": ClientCreateSolutionSolutionConfighpoConfigTypeDef,
        "algorithmHyperParameters": Dict[str, str],
        "featureTransformationParameters": Dict[str, str],
        "autoMLConfig": ClientCreateSolutionSolutionConfigautoMLConfigTypeDef,
    },
    total=False,
)


class ClientCreateSolutionSolutionConfigTypeDef(_ClientCreateSolutionSolutionConfigTypeDef):
    """
    The configuration to use with the solution. When ``performAutoML`` is set to true, Amazon
    Personalize only evaluates the ``autoMLConfig`` section of the solution configuration.
    - **eventValueThreshold** *(string) --*

      Only events with a value greater than or equal to this threshold are used for training a
      model.
    """


_ClientCreateSolutionVersionResponseTypeDef = TypedDict(
    "_ClientCreateSolutionVersionResponseTypeDef", {"solutionVersionArn": str}, total=False
)


class ClientCreateSolutionVersionResponseTypeDef(_ClientCreateSolutionVersionResponseTypeDef):
    """
    - *(dict) --*

      - **solutionVersionArn** *(string) --*

        The ARN of the new solution version.
    """


_ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef",
    {"name": str, "dockerURI": str},
    total=False,
)


class ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef(
    _ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef
):
    pass


_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    {"name": str, "values": List[str], "isTunable": bool},
    total=False,
)


class ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef(
    _ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef
):
    pass


_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    {"name": str, "minValue": float, "maxValue": float, "isTunable": bool},
    total=False,
)


class ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef(
    _ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef
):
    pass


_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef",
    {"name": str, "minValue": int, "maxValue": int, "isTunable": bool},
    total=False,
)


class ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef(
    _ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef
):
    pass


_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List[
            ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef
        ],
        "continuousHyperParameterRanges": List[
            ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef
        ],
        "categoricalHyperParameterRanges": List[
            ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef(
    _ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef
):
    pass


_ClientDescribeAlgorithmResponsealgorithmTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponsealgorithmTypeDef",
    {
        "name": str,
        "algorithmArn": str,
        "algorithmImage": ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef,
        "defaultHyperParameters": Dict[str, str],
        "defaultHyperParameterRanges": ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef,
        "defaultResourceConfig": Dict[str, str],
        "trainingInputMode": str,
        "roleArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeAlgorithmResponsealgorithmTypeDef(
    _ClientDescribeAlgorithmResponsealgorithmTypeDef
):
    """
    - **algorithm** *(dict) --*

      A listing of the properties of the algorithm.
      - **name** *(string) --*

        The name of the algorithm.
    """


_ClientDescribeAlgorithmResponseTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseTypeDef",
    {"algorithm": ClientDescribeAlgorithmResponsealgorithmTypeDef},
    total=False,
)


class ClientDescribeAlgorithmResponseTypeDef(_ClientDescribeAlgorithmResponseTypeDef):
    """
    - *(dict) --*

      - **algorithm** *(dict) --*

        A listing of the properties of the algorithm.
        - **name** *(string) --*

          The name of the algorithm.
    """


_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef = TypedDict(
    "_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef",
    {"path": str, "kmsKeyArn": str},
    total=False,
)


class ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef(
    _ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef
):
    pass


_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef = TypedDict(
    "_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef",
    {
        "s3DataSource": ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef
    },
    total=False,
)


class ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef(
    _ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef
):
    pass


_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef = TypedDict(
    "_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef",
    {"path": str, "kmsKeyArn": str},
    total=False,
)


class ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef(
    _ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef
):
    pass


_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef = TypedDict(
    "_ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef",
    {
        "s3DataDestination": ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef
    },
    total=False,
)


class ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef(
    _ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef
):
    pass


_ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef = TypedDict(
    "_ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef",
    {
        "jobName": str,
        "batchInferenceJobArn": str,
        "failureReason": str,
        "solutionVersionArn": str,
        "numResults": int,
        "jobInput": ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef,
        "jobOutput": ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef,
        "roleArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef(
    _ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef
):
    """
    - **batchInferenceJob** *(dict) --*

      Information on the specified batch inference job.
      - **jobName** *(string) --*

        The name of the batch inference job.
    """


_ClientDescribeBatchInferenceJobResponseTypeDef = TypedDict(
    "_ClientDescribeBatchInferenceJobResponseTypeDef",
    {"batchInferenceJob": ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef},
    total=False,
)


class ClientDescribeBatchInferenceJobResponseTypeDef(
    _ClientDescribeBatchInferenceJobResponseTypeDef
):
    """
    - *(dict) --*

      - **batchInferenceJob** *(dict) --*

        Information on the specified batch inference job.
        - **jobName** *(string) --*

          The name of the batch inference job.
    """


_ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef = TypedDict(
    "_ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef",
    {
        "solutionVersionArn": str,
        "minProvisionedTPS": int,
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef(
    _ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef
):
    pass


_ClientDescribeCampaignResponsecampaignTypeDef = TypedDict(
    "_ClientDescribeCampaignResponsecampaignTypeDef",
    {
        "name": str,
        "campaignArn": str,
        "solutionVersionArn": str,
        "minProvisionedTPS": int,
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "latestCampaignUpdate": ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef,
    },
    total=False,
)


class ClientDescribeCampaignResponsecampaignTypeDef(_ClientDescribeCampaignResponsecampaignTypeDef):
    """
    - **campaign** *(dict) --*

      The properties of the campaign.
      - **name** *(string) --*

        The name of the campaign.
    """


_ClientDescribeCampaignResponseTypeDef = TypedDict(
    "_ClientDescribeCampaignResponseTypeDef",
    {"campaign": ClientDescribeCampaignResponsecampaignTypeDef},
    total=False,
)


class ClientDescribeCampaignResponseTypeDef(_ClientDescribeCampaignResponseTypeDef):
    """
    - *(dict) --*

      - **campaign** *(dict) --*

        The properties of the campaign.
        - **name** *(string) --*

          The name of the campaign.
    """


_ClientDescribeDatasetGroupResponsedatasetGroupTypeDef = TypedDict(
    "_ClientDescribeDatasetGroupResponsedatasetGroupTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "status": str,
        "roleArn": str,
        "kmsKeyArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientDescribeDatasetGroupResponsedatasetGroupTypeDef(
    _ClientDescribeDatasetGroupResponsedatasetGroupTypeDef
):
    """
    - **datasetGroup** *(dict) --*

      A listing of the dataset group's properties.
      - **name** *(string) --*

        The name of the dataset group.
    """


_ClientDescribeDatasetGroupResponseTypeDef = TypedDict(
    "_ClientDescribeDatasetGroupResponseTypeDef",
    {"datasetGroup": ClientDescribeDatasetGroupResponsedatasetGroupTypeDef},
    total=False,
)


class ClientDescribeDatasetGroupResponseTypeDef(_ClientDescribeDatasetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **datasetGroup** *(dict) --*

        A listing of the dataset group's properties.
        - **name** *(string) --*

          The name of the dataset group.
    """


_ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef = TypedDict(
    "_ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef",
    {"dataLocation": str},
    total=False,
)


class ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef(
    _ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef
):
    pass


_ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef = TypedDict(
    "_ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef",
    {
        "jobName": str,
        "datasetImportJobArn": str,
        "datasetArn": str,
        "dataSource": ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef,
        "roleArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef(
    _ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef
):
    """
    - **datasetImportJob** *(dict) --*

      Information about the dataset import job, including the status.
      The status is one of the following values:
      * CREATE PENDING
      * CREATE IN_PROGRESS
      * ACTIVE
      * CREATE FAILED
      - **jobName** *(string) --*

        The name of the import job.
    """


_ClientDescribeDatasetImportJobResponseTypeDef = TypedDict(
    "_ClientDescribeDatasetImportJobResponseTypeDef",
    {"datasetImportJob": ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef},
    total=False,
)


class ClientDescribeDatasetImportJobResponseTypeDef(_ClientDescribeDatasetImportJobResponseTypeDef):
    """
    - *(dict) --*

      - **datasetImportJob** *(dict) --*

        Information about the dataset import job, including the status.
        The status is one of the following values:
        * CREATE PENDING
        * CREATE IN_PROGRESS
        * ACTIVE
        * CREATE FAILED
        - **jobName** *(string) --*

          The name of the import job.
    """


_ClientDescribeDatasetResponsedatasetTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetTypeDef",
    {
        "name": str,
        "datasetArn": str,
        "datasetGroupArn": str,
        "datasetType": str,
        "schemaArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeDatasetResponsedatasetTypeDef(_ClientDescribeDatasetResponsedatasetTypeDef):
    """
    - **dataset** *(dict) --*

      A listing of the dataset's properties.
      - **name** *(string) --*

        The name of the dataset.
    """


_ClientDescribeDatasetResponseTypeDef = TypedDict(
    "_ClientDescribeDatasetResponseTypeDef",
    {"dataset": ClientDescribeDatasetResponsedatasetTypeDef},
    total=False,
)


class ClientDescribeDatasetResponseTypeDef(_ClientDescribeDatasetResponseTypeDef):
    """
    - *(dict) --*

      - **dataset** *(dict) --*

        A listing of the dataset's properties.
        - **name** *(string) --*

          The name of the dataset.
    """


_ClientDescribeEventTrackerResponseeventTrackerTypeDef = TypedDict(
    "_ClientDescribeEventTrackerResponseeventTrackerTypeDef",
    {
        "name": str,
        "eventTrackerArn": str,
        "accountId": str,
        "trackingId": str,
        "datasetGroupArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeEventTrackerResponseeventTrackerTypeDef(
    _ClientDescribeEventTrackerResponseeventTrackerTypeDef
):
    """
    - **eventTracker** *(dict) --*

      An object that describes the event tracker.
      - **name** *(string) --*

        The name of the event tracker.
    """


_ClientDescribeEventTrackerResponseTypeDef = TypedDict(
    "_ClientDescribeEventTrackerResponseTypeDef",
    {"eventTracker": ClientDescribeEventTrackerResponseeventTrackerTypeDef},
    total=False,
)


class ClientDescribeEventTrackerResponseTypeDef(_ClientDescribeEventTrackerResponseTypeDef):
    """
    - *(dict) --*

      - **eventTracker** *(dict) --*

        An object that describes the event tracker.
        - **name** *(string) --*

          The name of the event tracker.
    """


_ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef = TypedDict(
    "_ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef",
    {
        "name": str,
        "featureTransformationArn": str,
        "defaultParameters": Dict[str, str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef(
    _ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef
):
    """
    - **featureTransformation** *(dict) --*

      A listing of the FeatureTransformation properties.
      - **name** *(string) --*

        The name of the feature transformation.
    """


_ClientDescribeFeatureTransformationResponseTypeDef = TypedDict(
    "_ClientDescribeFeatureTransformationResponseTypeDef",
    {
        "featureTransformation": ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef
    },
    total=False,
)


class ClientDescribeFeatureTransformationResponseTypeDef(
    _ClientDescribeFeatureTransformationResponseTypeDef
):
    """
    - *(dict) --*

      - **featureTransformation** *(dict) --*

        A listing of the FeatureTransformation properties.
        - **name** *(string) --*

          The name of the feature transformation.
    """


_ClientDescribeRecipeResponserecipeTypeDef = TypedDict(
    "_ClientDescribeRecipeResponserecipeTypeDef",
    {
        "name": str,
        "recipeArn": str,
        "algorithmArn": str,
        "featureTransformationArn": str,
        "status": str,
        "description": str,
        "creationDateTime": datetime,
        "recipeType": str,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeRecipeResponserecipeTypeDef(_ClientDescribeRecipeResponserecipeTypeDef):
    """
    - **recipe** *(dict) --*

      An object that describes the recipe.
      - **name** *(string) --*

        The name of the recipe.
    """


_ClientDescribeRecipeResponseTypeDef = TypedDict(
    "_ClientDescribeRecipeResponseTypeDef",
    {"recipe": ClientDescribeRecipeResponserecipeTypeDef},
    total=False,
)


class ClientDescribeRecipeResponseTypeDef(_ClientDescribeRecipeResponseTypeDef):
    """
    - *(dict) --*

      - **recipe** *(dict) --*

        An object that describes the recipe.
        - **name** *(string) --*

          The name of the recipe.
    """


_ClientDescribeSchemaResponseschemaTypeDef = TypedDict(
    "_ClientDescribeSchemaResponseschemaTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "schema": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeSchemaResponseschemaTypeDef(_ClientDescribeSchemaResponseschemaTypeDef):
    """
    - **schema** *(dict) --*

      The requested schema.
      - **name** *(string) --*

        The name of the schema.
    """


_ClientDescribeSchemaResponseTypeDef = TypedDict(
    "_ClientDescribeSchemaResponseTypeDef",
    {"schema": ClientDescribeSchemaResponseschemaTypeDef},
    total=False,
)


class ClientDescribeSchemaResponseTypeDef(_ClientDescribeSchemaResponseTypeDef):
    """
    - *(dict) --*

      - **schema** *(dict) --*

        The requested schema.
        - **name** *(string) --*

          The name of the schema.
    """


_ClientDescribeSolutionResponsesolutionautoMLResultTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionautoMLResultTypeDef",
    {"bestRecipeArn": str},
    total=False,
)


class ClientDescribeSolutionResponsesolutionautoMLResultTypeDef(
    _ClientDescribeSolutionResponsesolutionautoMLResultTypeDef
):
    pass


_ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef",
    {
        "solutionVersionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef(
    _ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef
):
    pass


_ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef",
    {"metricName": str, "recipeList": List[str]},
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef
):
    pass


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
):
    pass


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    {"name": str, "minValue": float, "maxValue": float},
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
):
    pass


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    {"name": str, "minValue": int, "maxValue": int},
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
):
    pass


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List[
            ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
        ],
        "continuousHyperParameterRanges": List[
            ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
        ],
        "categoricalHyperParameterRanges": List[
            ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef
):
    pass


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef",
    {"type": str, "metricName": str, "metricRegex": str},
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef
):
    pass


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef",
    {"maxNumberOfTrainingJobs": str, "maxParallelTrainingJobs": str},
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef
):
    pass


_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef",
    {
        "hpoObjective": ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef,
        "hpoResourceConfig": ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef,
        "algorithmHyperParameterRanges": ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef,
    },
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef
):
    pass


_ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef",
    {
        "eventValueThreshold": str,
        "hpoConfig": ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef,
        "algorithmHyperParameters": Dict[str, str],
        "featureTransformationParameters": Dict[str, str],
        "autoMLConfig": ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef(
    _ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef
):
    pass


_ClientDescribeSolutionResponsesolutionTypeDef = TypedDict(
    "_ClientDescribeSolutionResponsesolutionTypeDef",
    {
        "name": str,
        "solutionArn": str,
        "performHPO": bool,
        "performAutoML": bool,
        "recipeArn": str,
        "datasetGroupArn": str,
        "eventType": str,
        "solutionConfig": ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef,
        "autoMLResult": ClientDescribeSolutionResponsesolutionautoMLResultTypeDef,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "latestSolutionVersion": ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef,
    },
    total=False,
)


class ClientDescribeSolutionResponsesolutionTypeDef(_ClientDescribeSolutionResponsesolutionTypeDef):
    """
    - **solution** *(dict) --*

      An object that describes the solution.
      - **name** *(string) --*

        The name of the solution.
    """


_ClientDescribeSolutionResponseTypeDef = TypedDict(
    "_ClientDescribeSolutionResponseTypeDef",
    {"solution": ClientDescribeSolutionResponsesolutionTypeDef},
    total=False,
)


class ClientDescribeSolutionResponseTypeDef(_ClientDescribeSolutionResponseTypeDef):
    """
    - *(dict) --*

      - **solution** *(dict) --*

        An object that describes the solution.
        - **name** *(string) --*

          The name of the solution.
    """


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef",
    {"metricName": str, "recipeList": List[str]},
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef
):
    pass


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
):
    pass


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    {"name": str, "minValue": float, "maxValue": float},
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
):
    pass


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    {"name": str, "minValue": int, "maxValue": int},
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
):
    pass


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List[
            ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
        ],
        "continuousHyperParameterRanges": List[
            ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
        ],
        "categoricalHyperParameterRanges": List[
            ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef
):
    pass


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef",
    {"type": str, "metricName": str, "metricRegex": str},
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef
):
    pass


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef",
    {"maxNumberOfTrainingJobs": str, "maxParallelTrainingJobs": str},
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef
):
    pass


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef",
    {
        "hpoObjective": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef,
        "hpoResourceConfig": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef,
        "algorithmHyperParameterRanges": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef,
    },
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef
):
    pass


_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef",
    {
        "eventValueThreshold": str,
        "hpoConfig": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef,
        "algorithmHyperParameters": Dict[str, str],
        "featureTransformationParameters": Dict[str, str],
        "autoMLConfig": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef
):
    pass


_ClientDescribeSolutionVersionResponsesolutionVersionTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponsesolutionVersionTypeDef",
    {
        "solutionVersionArn": str,
        "solutionArn": str,
        "performHPO": bool,
        "performAutoML": bool,
        "recipeArn": str,
        "eventType": str,
        "datasetGroupArn": str,
        "solutionConfig": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef,
        "trainingHours": float,
        "trainingMode": Literal["FULL", "UPDATE"],
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeSolutionVersionResponsesolutionVersionTypeDef(
    _ClientDescribeSolutionVersionResponsesolutionVersionTypeDef
):
    """
    - **solutionVersion** *(dict) --*

      The solution version.
      - **solutionVersionArn** *(string) --*

        The ARN of the solution version.
    """


_ClientDescribeSolutionVersionResponseTypeDef = TypedDict(
    "_ClientDescribeSolutionVersionResponseTypeDef",
    {"solutionVersion": ClientDescribeSolutionVersionResponsesolutionVersionTypeDef},
    total=False,
)


class ClientDescribeSolutionVersionResponseTypeDef(_ClientDescribeSolutionVersionResponseTypeDef):
    """
    - *(dict) --*

      - **solutionVersion** *(dict) --*

        The solution version.
        - **solutionVersionArn** *(string) --*

          The ARN of the solution version.
    """


_ClientGetSolutionMetricsResponseTypeDef = TypedDict(
    "_ClientGetSolutionMetricsResponseTypeDef",
    {"solutionVersionArn": str, "metrics": Dict[str, float]},
    total=False,
)


class ClientGetSolutionMetricsResponseTypeDef(_ClientGetSolutionMetricsResponseTypeDef):
    """
    - *(dict) --*

      - **solutionVersionArn** *(string) --*

        The same solution version ARN as specified in the request.
    """


_ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef = TypedDict(
    "_ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef",
    {
        "batchInferenceJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef(
    _ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef
):
    """
    - *(dict) --*

      A truncated version of the  BatchInferenceJob datatype. The  ListBatchInferenceJobs operation
      returns a list of batch inference job summaries.
      - **batchInferenceJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the batch inference job.
    """


_ClientListBatchInferenceJobsResponseTypeDef = TypedDict(
    "_ClientListBatchInferenceJobsResponseTypeDef",
    {
        "batchInferenceJobs": List[ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListBatchInferenceJobsResponseTypeDef(_ClientListBatchInferenceJobsResponseTypeDef):
    """
    - *(dict) --*

      - **batchInferenceJobs** *(list) --*

        A list containing information on each job that is returned.
        - *(dict) --*

          A truncated version of the  BatchInferenceJob datatype. The  ListBatchInferenceJobs
          operation returns a list of batch inference job summaries.
          - **batchInferenceJobArn** *(string) --*

            The Amazon Resource Name (ARN) of the batch inference job.
    """


_ClientListCampaignsResponsecampaignsTypeDef = TypedDict(
    "_ClientListCampaignsResponsecampaignsTypeDef",
    {
        "name": str,
        "campaignArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientListCampaignsResponsecampaignsTypeDef(_ClientListCampaignsResponsecampaignsTypeDef):
    """
    - *(dict) --*

      Provides a summary of the properties of a campaign. For a complete listing, call the
      DescribeCampaign API.
      - **name** *(string) --*

        The name of the campaign.
    """


_ClientListCampaignsResponseTypeDef = TypedDict(
    "_ClientListCampaignsResponseTypeDef",
    {"campaigns": List[ClientListCampaignsResponsecampaignsTypeDef], "nextToken": str},
    total=False,
)


class ClientListCampaignsResponseTypeDef(_ClientListCampaignsResponseTypeDef):
    """
    - *(dict) --*

      - **campaigns** *(list) --*

        A list of the campaigns.
        - *(dict) --*

          Provides a summary of the properties of a campaign. For a complete listing, call the
          DescribeCampaign API.
          - **name** *(string) --*

            The name of the campaign.
    """


_ClientListDatasetGroupsResponsedatasetGroupsTypeDef = TypedDict(
    "_ClientListDatasetGroupsResponsedatasetGroupsTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientListDatasetGroupsResponsedatasetGroupsTypeDef(
    _ClientListDatasetGroupsResponsedatasetGroupsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the properties of a dataset group. For a complete listing, call the
      DescribeDatasetGroup API.
      - **name** *(string) --*

        The name of the dataset group.
    """


_ClientListDatasetGroupsResponseTypeDef = TypedDict(
    "_ClientListDatasetGroupsResponseTypeDef",
    {"datasetGroups": List[ClientListDatasetGroupsResponsedatasetGroupsTypeDef], "nextToken": str},
    total=False,
)


class ClientListDatasetGroupsResponseTypeDef(_ClientListDatasetGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **datasetGroups** *(list) --*

        The list of your dataset groups.
        - *(dict) --*

          Provides a summary of the properties of a dataset group. For a complete listing, call the
          DescribeDatasetGroup API.
          - **name** *(string) --*

            The name of the dataset group.
    """


_ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef = TypedDict(
    "_ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef",
    {
        "datasetImportJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef(
    _ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the properties of a dataset import job. For a complete listing, call the
      DescribeDatasetImportJob API.
      - **datasetImportJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset import job.
    """


_ClientListDatasetImportJobsResponseTypeDef = TypedDict(
    "_ClientListDatasetImportJobsResponseTypeDef",
    {
        "datasetImportJobs": List[ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListDatasetImportJobsResponseTypeDef(_ClientListDatasetImportJobsResponseTypeDef):
    """
    - *(dict) --*

      - **datasetImportJobs** *(list) --*

        The list of dataset import jobs.
        - *(dict) --*

          Provides a summary of the properties of a dataset import job. For a complete listing, call
          the  DescribeDatasetImportJob API.
          - **datasetImportJobArn** *(string) --*

            The Amazon Resource Name (ARN) of the dataset import job.
    """


_ClientListDatasetsResponsedatasetsTypeDef = TypedDict(
    "_ClientListDatasetsResponsedatasetsTypeDef",
    {
        "name": str,
        "datasetArn": str,
        "datasetType": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientListDatasetsResponsedatasetsTypeDef(_ClientListDatasetsResponsedatasetsTypeDef):
    """
    - *(dict) --*

      Provides a summary of the properties of a dataset. For a complete listing, call the
      DescribeDataset API.
      - **name** *(string) --*

        The name of the dataset.
    """


_ClientListDatasetsResponseTypeDef = TypedDict(
    "_ClientListDatasetsResponseTypeDef",
    {"datasets": List[ClientListDatasetsResponsedatasetsTypeDef], "nextToken": str},
    total=False,
)


class ClientListDatasetsResponseTypeDef(_ClientListDatasetsResponseTypeDef):
    """
    - *(dict) --*

      - **datasets** *(list) --*

        An array of ``Dataset`` objects. Each object provides metadata information.
        - *(dict) --*

          Provides a summary of the properties of a dataset. For a complete listing, call the
          DescribeDataset API.
          - **name** *(string) --*

            The name of the dataset.
    """


_ClientListEventTrackersResponseeventTrackersTypeDef = TypedDict(
    "_ClientListEventTrackersResponseeventTrackersTypeDef",
    {
        "name": str,
        "eventTrackerArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientListEventTrackersResponseeventTrackersTypeDef(
    _ClientListEventTrackersResponseeventTrackersTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the properties of an event tracker. For a complete listing, call the
      DescribeEventTracker API.
      - **name** *(string) --*

        The name of the event tracker.
    """


_ClientListEventTrackersResponseTypeDef = TypedDict(
    "_ClientListEventTrackersResponseTypeDef",
    {"eventTrackers": List[ClientListEventTrackersResponseeventTrackersTypeDef], "nextToken": str},
    total=False,
)


class ClientListEventTrackersResponseTypeDef(_ClientListEventTrackersResponseTypeDef):
    """
    - *(dict) --*

      - **eventTrackers** *(list) --*

        A list of event trackers.
        - *(dict) --*

          Provides a summary of the properties of an event tracker. For a complete listing, call the
          DescribeEventTracker API.
          - **name** *(string) --*

            The name of the event tracker.
    """


_ClientListRecipesResponserecipesTypeDef = TypedDict(
    "_ClientListRecipesResponserecipesTypeDef",
    {
        "name": str,
        "recipeArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientListRecipesResponserecipesTypeDef(_ClientListRecipesResponserecipesTypeDef):
    """
    - *(dict) --*

      Provides a summary of the properties of a recipe. For a complete listing, call the
      DescribeRecipe API.
      - **name** *(string) --*

        The name of the recipe.
    """


_ClientListRecipesResponseTypeDef = TypedDict(
    "_ClientListRecipesResponseTypeDef",
    {"recipes": List[ClientListRecipesResponserecipesTypeDef], "nextToken": str},
    total=False,
)


class ClientListRecipesResponseTypeDef(_ClientListRecipesResponseTypeDef):
    """
    - *(dict) --*

      - **recipes** *(list) --*

        The list of available recipes.
        - *(dict) --*

          Provides a summary of the properties of a recipe. For a complete listing, call the
          DescribeRecipe API.
          - **name** *(string) --*

            The name of the recipe.
    """


_ClientListSchemasResponseschemasTypeDef = TypedDict(
    "_ClientListSchemasResponseschemasTypeDef",
    {"name": str, "schemaArn": str, "creationDateTime": datetime, "lastUpdatedDateTime": datetime},
    total=False,
)


class ClientListSchemasResponseschemasTypeDef(_ClientListSchemasResponseschemasTypeDef):
    """
    - *(dict) --*

      Provides a summary of the properties of a dataset schema. For a complete listing, call the
      DescribeSchema API.
      - **name** *(string) --*

        The name of the schema.
    """


_ClientListSchemasResponseTypeDef = TypedDict(
    "_ClientListSchemasResponseTypeDef",
    {"schemas": List[ClientListSchemasResponseschemasTypeDef], "nextToken": str},
    total=False,
)


class ClientListSchemasResponseTypeDef(_ClientListSchemasResponseTypeDef):
    """
    - *(dict) --*

      - **schemas** *(list) --*

        A list of schemas.
        - *(dict) --*

          Provides a summary of the properties of a dataset schema. For a complete listing, call the
          DescribeSchema API.
          - **name** *(string) --*

            The name of the schema.
    """


_ClientListSolutionVersionsResponsesolutionVersionsTypeDef = TypedDict(
    "_ClientListSolutionVersionsResponsesolutionVersionsTypeDef",
    {
        "solutionVersionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ClientListSolutionVersionsResponsesolutionVersionsTypeDef(
    _ClientListSolutionVersionsResponsesolutionVersionsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the properties of a solution version. For a complete listing, call the
      DescribeSolutionVersion API.
      - **solutionVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of the solution version.
    """


_ClientListSolutionVersionsResponseTypeDef = TypedDict(
    "_ClientListSolutionVersionsResponseTypeDef",
    {
        "solutionVersions": List[ClientListSolutionVersionsResponsesolutionVersionsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListSolutionVersionsResponseTypeDef(_ClientListSolutionVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **solutionVersions** *(list) --*

        A list of solution versions describing the version properties.
        - *(dict) --*

          Provides a summary of the properties of a solution version. For a complete listing, call
          the  DescribeSolutionVersion API.
          - **solutionVersionArn** *(string) --*

            The Amazon Resource Name (ARN) of the solution version.
    """


_ClientListSolutionsResponsesolutionsTypeDef = TypedDict(
    "_ClientListSolutionsResponsesolutionsTypeDef",
    {
        "name": str,
        "solutionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientListSolutionsResponsesolutionsTypeDef(_ClientListSolutionsResponsesolutionsTypeDef):
    """
    - *(dict) --*

      Provides a summary of the properties of a solution. For a complete listing, call the
      DescribeSolution API.
      - **name** *(string) --*

        The name of the solution.
    """


_ClientListSolutionsResponseTypeDef = TypedDict(
    "_ClientListSolutionsResponseTypeDef",
    {"solutions": List[ClientListSolutionsResponsesolutionsTypeDef], "nextToken": str},
    total=False,
)


class ClientListSolutionsResponseTypeDef(_ClientListSolutionsResponseTypeDef):
    """
    - *(dict) --*

      - **solutions** *(list) --*

        A list of the current solutions.
        - *(dict) --*

          Provides a summary of the properties of a solution. For a complete listing, call the
          DescribeSolution API.
          - **name** *(string) --*

            The name of the solution.
    """


_ClientUpdateCampaignResponseTypeDef = TypedDict(
    "_ClientUpdateCampaignResponseTypeDef", {"campaignArn": str}, total=False
)


class ClientUpdateCampaignResponseTypeDef(_ClientUpdateCampaignResponseTypeDef):
    """
    - *(dict) --*

      - **campaignArn** *(string) --*

        The same campaign ARN as given in the request.
    """


_ListBatchInferenceJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBatchInferenceJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBatchInferenceJobsPaginatePaginationConfigTypeDef(
    _ListBatchInferenceJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBatchInferenceJobsPaginateResponsebatchInferenceJobsTypeDef = TypedDict(
    "_ListBatchInferenceJobsPaginateResponsebatchInferenceJobsTypeDef",
    {
        "batchInferenceJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ListBatchInferenceJobsPaginateResponsebatchInferenceJobsTypeDef(
    _ListBatchInferenceJobsPaginateResponsebatchInferenceJobsTypeDef
):
    """
    - *(dict) --*

      A truncated version of the  BatchInferenceJob datatype. The  ListBatchInferenceJobs operation
      returns a list of batch inference job summaries.
      - **batchInferenceJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the batch inference job.
    """


_ListBatchInferenceJobsPaginateResponseTypeDef = TypedDict(
    "_ListBatchInferenceJobsPaginateResponseTypeDef",
    {
        "batchInferenceJobs": List[ListBatchInferenceJobsPaginateResponsebatchInferenceJobsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListBatchInferenceJobsPaginateResponseTypeDef(_ListBatchInferenceJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **batchInferenceJobs** *(list) --*

        A list containing information on each job that is returned.
        - *(dict) --*

          A truncated version of the  BatchInferenceJob datatype. The  ListBatchInferenceJobs
          operation returns a list of batch inference job summaries.
          - **batchInferenceJobArn** *(string) --*

            The Amazon Resource Name (ARN) of the batch inference job.
    """


_ListCampaignsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCampaignsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCampaignsPaginatePaginationConfigTypeDef(_ListCampaignsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCampaignsPaginateResponsecampaignsTypeDef = TypedDict(
    "_ListCampaignsPaginateResponsecampaignsTypeDef",
    {
        "name": str,
        "campaignArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ListCampaignsPaginateResponsecampaignsTypeDef(_ListCampaignsPaginateResponsecampaignsTypeDef):
    """
    - *(dict) --*

      Provides a summary of the properties of a campaign. For a complete listing, call the
      DescribeCampaign API.
      - **name** *(string) --*

        The name of the campaign.
    """


_ListCampaignsPaginateResponseTypeDef = TypedDict(
    "_ListCampaignsPaginateResponseTypeDef",
    {"campaigns": List[ListCampaignsPaginateResponsecampaignsTypeDef], "NextToken": str},
    total=False,
)


class ListCampaignsPaginateResponseTypeDef(_ListCampaignsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **campaigns** *(list) --*

        A list of the campaigns.
        - *(dict) --*

          Provides a summary of the properties of a campaign. For a complete listing, call the
          DescribeCampaign API.
          - **name** *(string) --*

            The name of the campaign.
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


_ListDatasetGroupsPaginateResponsedatasetGroupsTypeDef = TypedDict(
    "_ListDatasetGroupsPaginateResponsedatasetGroupsTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ListDatasetGroupsPaginateResponsedatasetGroupsTypeDef(
    _ListDatasetGroupsPaginateResponsedatasetGroupsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the properties of a dataset group. For a complete listing, call the
      DescribeDatasetGroup API.
      - **name** *(string) --*

        The name of the dataset group.
    """


_ListDatasetGroupsPaginateResponseTypeDef = TypedDict(
    "_ListDatasetGroupsPaginateResponseTypeDef",
    {
        "datasetGroups": List[ListDatasetGroupsPaginateResponsedatasetGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListDatasetGroupsPaginateResponseTypeDef(_ListDatasetGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **datasetGroups** *(list) --*

        The list of your dataset groups.
        - *(dict) --*

          Provides a summary of the properties of a dataset group. For a complete listing, call the
          DescribeDatasetGroup API.
          - **name** *(string) --*

            The name of the dataset group.
    """


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


_ListDatasetImportJobsPaginateResponsedatasetImportJobsTypeDef = TypedDict(
    "_ListDatasetImportJobsPaginateResponsedatasetImportJobsTypeDef",
    {
        "datasetImportJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ListDatasetImportJobsPaginateResponsedatasetImportJobsTypeDef(
    _ListDatasetImportJobsPaginateResponsedatasetImportJobsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the properties of a dataset import job. For a complete listing, call the
      DescribeDatasetImportJob API.
      - **datasetImportJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset import job.
    """


_ListDatasetImportJobsPaginateResponseTypeDef = TypedDict(
    "_ListDatasetImportJobsPaginateResponseTypeDef",
    {
        "datasetImportJobs": List[ListDatasetImportJobsPaginateResponsedatasetImportJobsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListDatasetImportJobsPaginateResponseTypeDef(_ListDatasetImportJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **datasetImportJobs** *(list) --*

        The list of dataset import jobs.
        - *(dict) --*

          Provides a summary of the properties of a dataset import job. For a complete listing, call
          the  DescribeDatasetImportJob API.
          - **datasetImportJobArn** *(string) --*

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


_ListDatasetsPaginateResponsedatasetsTypeDef = TypedDict(
    "_ListDatasetsPaginateResponsedatasetsTypeDef",
    {
        "name": str,
        "datasetArn": str,
        "datasetType": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ListDatasetsPaginateResponsedatasetsTypeDef(_ListDatasetsPaginateResponsedatasetsTypeDef):
    """
    - *(dict) --*

      Provides a summary of the properties of a dataset. For a complete listing, call the
      DescribeDataset API.
      - **name** *(string) --*

        The name of the dataset.
    """


_ListDatasetsPaginateResponseTypeDef = TypedDict(
    "_ListDatasetsPaginateResponseTypeDef",
    {"datasets": List[ListDatasetsPaginateResponsedatasetsTypeDef], "NextToken": str},
    total=False,
)


class ListDatasetsPaginateResponseTypeDef(_ListDatasetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **datasets** *(list) --*

        An array of ``Dataset`` objects. Each object provides metadata information.
        - *(dict) --*

          Provides a summary of the properties of a dataset. For a complete listing, call the
          DescribeDataset API.
          - **name** *(string) --*

            The name of the dataset.
    """


_ListEventTrackersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEventTrackersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEventTrackersPaginatePaginationConfigTypeDef(
    _ListEventTrackersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEventTrackersPaginateResponseeventTrackersTypeDef = TypedDict(
    "_ListEventTrackersPaginateResponseeventTrackersTypeDef",
    {
        "name": str,
        "eventTrackerArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ListEventTrackersPaginateResponseeventTrackersTypeDef(
    _ListEventTrackersPaginateResponseeventTrackersTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the properties of an event tracker. For a complete listing, call the
      DescribeEventTracker API.
      - **name** *(string) --*

        The name of the event tracker.
    """


_ListEventTrackersPaginateResponseTypeDef = TypedDict(
    "_ListEventTrackersPaginateResponseTypeDef",
    {
        "eventTrackers": List[ListEventTrackersPaginateResponseeventTrackersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListEventTrackersPaginateResponseTypeDef(_ListEventTrackersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **eventTrackers** *(list) --*

        A list of event trackers.
        - *(dict) --*

          Provides a summary of the properties of an event tracker. For a complete listing, call the
          DescribeEventTracker API.
          - **name** *(string) --*

            The name of the event tracker.
    """


_ListRecipesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRecipesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRecipesPaginatePaginationConfigTypeDef(_ListRecipesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRecipesPaginateResponserecipesTypeDef = TypedDict(
    "_ListRecipesPaginateResponserecipesTypeDef",
    {
        "name": str,
        "recipeArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ListRecipesPaginateResponserecipesTypeDef(_ListRecipesPaginateResponserecipesTypeDef):
    """
    - *(dict) --*

      Provides a summary of the properties of a recipe. For a complete listing, call the
      DescribeRecipe API.
      - **name** *(string) --*

        The name of the recipe.
    """


_ListRecipesPaginateResponseTypeDef = TypedDict(
    "_ListRecipesPaginateResponseTypeDef",
    {"recipes": List[ListRecipesPaginateResponserecipesTypeDef], "NextToken": str},
    total=False,
)


class ListRecipesPaginateResponseTypeDef(_ListRecipesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **recipes** *(list) --*

        The list of available recipes.
        - *(dict) --*

          Provides a summary of the properties of a recipe. For a complete listing, call the
          DescribeRecipe API.
          - **name** *(string) --*

            The name of the recipe.
    """


_ListSchemasPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSchemasPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSchemasPaginatePaginationConfigTypeDef(_ListSchemasPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSchemasPaginateResponseschemasTypeDef = TypedDict(
    "_ListSchemasPaginateResponseschemasTypeDef",
    {"name": str, "schemaArn": str, "creationDateTime": datetime, "lastUpdatedDateTime": datetime},
    total=False,
)


class ListSchemasPaginateResponseschemasTypeDef(_ListSchemasPaginateResponseschemasTypeDef):
    """
    - *(dict) --*

      Provides a summary of the properties of a dataset schema. For a complete listing, call the
      DescribeSchema API.
      - **name** *(string) --*

        The name of the schema.
    """


_ListSchemasPaginateResponseTypeDef = TypedDict(
    "_ListSchemasPaginateResponseTypeDef",
    {"schemas": List[ListSchemasPaginateResponseschemasTypeDef], "NextToken": str},
    total=False,
)


class ListSchemasPaginateResponseTypeDef(_ListSchemasPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **schemas** *(list) --*

        A list of schemas.
        - *(dict) --*

          Provides a summary of the properties of a dataset schema. For a complete listing, call the
          DescribeSchema API.
          - **name** *(string) --*

            The name of the schema.
    """


_ListSolutionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSolutionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSolutionVersionsPaginatePaginationConfigTypeDef(
    _ListSolutionVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSolutionVersionsPaginateResponsesolutionVersionsTypeDef = TypedDict(
    "_ListSolutionVersionsPaginateResponsesolutionVersionsTypeDef",
    {
        "solutionVersionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)


class ListSolutionVersionsPaginateResponsesolutionVersionsTypeDef(
    _ListSolutionVersionsPaginateResponsesolutionVersionsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of the properties of a solution version. For a complete listing, call the
      DescribeSolutionVersion API.
      - **solutionVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of the solution version.
    """


_ListSolutionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListSolutionVersionsPaginateResponseTypeDef",
    {
        "solutionVersions": List[ListSolutionVersionsPaginateResponsesolutionVersionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListSolutionVersionsPaginateResponseTypeDef(_ListSolutionVersionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **solutionVersions** *(list) --*

        A list of solution versions describing the version properties.
        - *(dict) --*

          Provides a summary of the properties of a solution version. For a complete listing, call
          the  DescribeSolutionVersion API.
          - **solutionVersionArn** *(string) --*

            The Amazon Resource Name (ARN) of the solution version.
    """


_ListSolutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSolutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSolutionsPaginatePaginationConfigTypeDef(_ListSolutionsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSolutionsPaginateResponsesolutionsTypeDef = TypedDict(
    "_ListSolutionsPaginateResponsesolutionsTypeDef",
    {
        "name": str,
        "solutionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class ListSolutionsPaginateResponsesolutionsTypeDef(_ListSolutionsPaginateResponsesolutionsTypeDef):
    """
    - *(dict) --*

      Provides a summary of the properties of a solution. For a complete listing, call the
      DescribeSolution API.
      - **name** *(string) --*

        The name of the solution.
    """


_ListSolutionsPaginateResponseTypeDef = TypedDict(
    "_ListSolutionsPaginateResponseTypeDef",
    {"solutions": List[ListSolutionsPaginateResponsesolutionsTypeDef], "NextToken": str},
    total=False,
)


class ListSolutionsPaginateResponseTypeDef(_ListSolutionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **solutions** *(list) --*

        A list of the current solutions.
        - *(dict) --*

          Provides a summary of the properties of a solution. For a complete listing, call the
          DescribeSolution API.
          - **name** *(string) --*

            The name of the solution.
    """
