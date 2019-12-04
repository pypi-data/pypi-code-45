"Main interface for machinelearning service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "BatchPredictionAvailableWaitWaiterConfigTypeDef",
    "ClientAddTagsResponseTypeDef",
    "ClientAddTagsTagsTypeDef",
    "ClientCreateBatchPredictionResponseTypeDef",
    "ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef",
    "ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef",
    "ClientCreateDataSourceFromRdsRDSDataTypeDef",
    "ClientCreateDataSourceFromRdsResponseTypeDef",
    "ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef",
    "ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef",
    "ClientCreateDataSourceFromRedshiftDataSpecTypeDef",
    "ClientCreateDataSourceFromRedshiftResponseTypeDef",
    "ClientCreateDataSourceFromS3DataSpecTypeDef",
    "ClientCreateDataSourceFromS3ResponseTypeDef",
    "ClientCreateEvaluationResponseTypeDef",
    "ClientCreateMlModelResponseTypeDef",
    "ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef",
    "ClientCreateRealtimeEndpointResponseTypeDef",
    "ClientDeleteBatchPredictionResponseTypeDef",
    "ClientDeleteDataSourceResponseTypeDef",
    "ClientDeleteEvaluationResponseTypeDef",
    "ClientDeleteMlModelResponseTypeDef",
    "ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef",
    "ClientDeleteRealtimeEndpointResponseTypeDef",
    "ClientDeleteTagsResponseTypeDef",
    "ClientDescribeBatchPredictionsResponseResultsTypeDef",
    "ClientDescribeBatchPredictionsResponseTypeDef",
    "ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef",
    "ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef",
    "ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef",
    "ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef",
    "ClientDescribeDataSourcesResponseResultsTypeDef",
    "ClientDescribeDataSourcesResponseTypeDef",
    "ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef",
    "ClientDescribeEvaluationsResponseResultsTypeDef",
    "ClientDescribeEvaluationsResponseTypeDef",
    "ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef",
    "ClientDescribeMlModelsResponseResultsTypeDef",
    "ClientDescribeMlModelsResponseTypeDef",
    "ClientDescribeTagsResponseTagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientGetBatchPredictionResponseTypeDef",
    "ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef",
    "ClientGetDataSourceResponseRDSMetadataTypeDef",
    "ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef",
    "ClientGetDataSourceResponseRedshiftMetadataTypeDef",
    "ClientGetDataSourceResponseTypeDef",
    "ClientGetEvaluationResponsePerformanceMetricsTypeDef",
    "ClientGetEvaluationResponseTypeDef",
    "ClientGetMlModelResponseEndpointInfoTypeDef",
    "ClientGetMlModelResponseTypeDef",
    "ClientPredictResponsePredictionTypeDef",
    "ClientPredictResponseTypeDef",
    "ClientUpdateBatchPredictionResponseTypeDef",
    "ClientUpdateDataSourceResponseTypeDef",
    "ClientUpdateEvaluationResponseTypeDef",
    "ClientUpdateMlModelResponseTypeDef",
    "DataSourceAvailableWaitWaiterConfigTypeDef",
    "DescribeBatchPredictionsPaginatePaginationConfigTypeDef",
    "DescribeBatchPredictionsPaginateResponseResultsTypeDef",
    "DescribeBatchPredictionsPaginateResponseTypeDef",
    "DescribeDataSourcesPaginatePaginationConfigTypeDef",
    "DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef",
    "DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef",
    "DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef",
    "DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef",
    "DescribeDataSourcesPaginateResponseResultsTypeDef",
    "DescribeDataSourcesPaginateResponseTypeDef",
    "DescribeEvaluationsPaginatePaginationConfigTypeDef",
    "DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef",
    "DescribeEvaluationsPaginateResponseResultsTypeDef",
    "DescribeEvaluationsPaginateResponseTypeDef",
    "DescribeMLModelsPaginatePaginationConfigTypeDef",
    "DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef",
    "DescribeMLModelsPaginateResponseResultsTypeDef",
    "DescribeMLModelsPaginateResponseTypeDef",
    "EvaluationAvailableWaitWaiterConfigTypeDef",
    "MlModelAvailableWaitWaiterConfigTypeDef",
)


_BatchPredictionAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_BatchPredictionAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class BatchPredictionAvailableWaitWaiterConfigTypeDef(
    _BatchPredictionAvailableWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_ClientAddTagsResponseTypeDef = TypedDict(
    "_ClientAddTagsResponseTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"],
    },
    total=False,
)


class ClientAddTagsResponseTypeDef(_ClientAddTagsResponseTypeDef):
    """
    - *(dict) --*

      Amazon ML returns the following elements.
      - **ResourceId** *(string) --*

        The ID of the ML object that was tagged.
    """


_ClientAddTagsTagsTypeDef = TypedDict(
    "_ClientAddTagsTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsTagsTypeDef(_ClientAddTagsTagsTypeDef):
    """
    - *(dict) --*

      A custom key-value pair associated with an ML object, such as an ML model.
      - **Key** *(string) --*

        A unique identifier for the tag. Valid characters include Unicode letters, digits, white
        space, _, ., /, =, +, -, %, and @.
    """


_ClientCreateBatchPredictionResponseTypeDef = TypedDict(
    "_ClientCreateBatchPredictionResponseTypeDef", {"BatchPredictionId": str}, total=False
)


class ClientCreateBatchPredictionResponseTypeDef(_ClientCreateBatchPredictionResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``CreateBatchPrediction`` operation, and is an acknowledgement that
      Amazon ML received the request.
      The ``CreateBatchPrediction`` operation is asynchronous. You can poll for status updates by
      using the ``>GetBatchPrediction`` operation and checking the ``Status`` parameter of the
      result.
      - **BatchPredictionId** *(string) --*

        A user-supplied ID that uniquely identifies the ``BatchPrediction`` . This value is
        identical to the value of the ``BatchPredictionId`` in the request.
    """


_ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef",
    {"Username": str, "Password": str},
    total=False,
)


class ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef(
    _ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef
):
    pass


_ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef",
    {"InstanceIdentifier": str, "DatabaseName": str},
    total=False,
)


class ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef(
    _ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef
):
    pass


_ClientCreateDataSourceFromRdsRDSDataTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRdsRDSDataTypeDef",
    {
        "DatabaseInformation": ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef,
        "SelectSqlQuery": str,
        "DatabaseCredentials": ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef,
        "S3StagingLocation": str,
        "DataRearrangement": str,
        "DataSchema": str,
        "DataSchemaUri": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "SubnetId": str,
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class ClientCreateDataSourceFromRdsRDSDataTypeDef(_ClientCreateDataSourceFromRdsRDSDataTypeDef):
    """
    The data specification of an Amazon RDS ``DataSource`` :
    * DatabaseInformation -

      * ``DatabaseName`` - The name of the Amazon RDS database.
      * ``InstanceIdentifier`` - A unique identifier for the Amazon RDS database instance.
    """


_ClientCreateDataSourceFromRdsResponseTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRdsResponseTypeDef", {"DataSourceId": str}, total=False
)


class ClientCreateDataSourceFromRdsResponseTypeDef(_ClientCreateDataSourceFromRdsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``CreateDataSourceFromRDS`` operation, and is an acknowledgement
      that Amazon ML received the request.
      The ``CreateDataSourceFromRDS`` > operation is asynchronous. You can poll for updates by using
      the ``GetBatchPrediction`` operation and checking the ``Status`` parameter. You can inspect
      the ``Message`` when ``Status`` shows up as ``FAILED`` . You can also check the progress of
      the copy operation by going to the ``DataPipeline`` console and looking up the pipeline using
      the ``pipelineId`` from the describe call.
      - **DataSourceId** *(string) --*

        A user-supplied ID that uniquely identifies the datasource. This value should be identical
        to the value of the ``DataSourceID`` in the request.
    """


_ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef",
    {"Username": str, "Password": str},
    total=False,
)


class ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef(
    _ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef
):
    pass


_ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef",
    {"DatabaseName": str, "ClusterIdentifier": str},
    total=False,
)


class ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef(
    _ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef
):
    pass


_ClientCreateDataSourceFromRedshiftDataSpecTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRedshiftDataSpecTypeDef",
    {
        "DatabaseInformation": ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef,
        "SelectSqlQuery": str,
        "DatabaseCredentials": ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef,
        "S3StagingLocation": str,
        "DataRearrangement": str,
        "DataSchema": str,
        "DataSchemaUri": str,
    },
    total=False,
)


class ClientCreateDataSourceFromRedshiftDataSpecTypeDef(
    _ClientCreateDataSourceFromRedshiftDataSpecTypeDef
):
    """
    The data specification of an Amazon Redshift ``DataSource`` :
    * DatabaseInformation -

      * ``DatabaseName`` - The name of the Amazon Redshift database.
      * ``ClusterIdentifier`` - The unique ID for the Amazon Redshift cluster.
    """


_ClientCreateDataSourceFromRedshiftResponseTypeDef = TypedDict(
    "_ClientCreateDataSourceFromRedshiftResponseTypeDef", {"DataSourceId": str}, total=False
)


class ClientCreateDataSourceFromRedshiftResponseTypeDef(
    _ClientCreateDataSourceFromRedshiftResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``CreateDataSourceFromRedshift`` operation, and is an
      acknowledgement that Amazon ML received the request.
      The ``CreateDataSourceFromRedshift`` operation is asynchronous. You can poll for updates by
      using the ``GetBatchPrediction`` operation and checking the ``Status`` parameter.
      - **DataSourceId** *(string) --*

        A user-supplied ID that uniquely identifies the datasource. This value should be identical
        to the value of the ``DataSourceID`` in the request.
    """


_RequiredClientCreateDataSourceFromS3DataSpecTypeDef = TypedDict(
    "_RequiredClientCreateDataSourceFromS3DataSpecTypeDef", {"DataLocationS3": str}
)
_OptionalClientCreateDataSourceFromS3DataSpecTypeDef = TypedDict(
    "_OptionalClientCreateDataSourceFromS3DataSpecTypeDef",
    {"DataRearrangement": str, "DataSchema": str, "DataSchemaLocationS3": str},
    total=False,
)


class ClientCreateDataSourceFromS3DataSpecTypeDef(
    _RequiredClientCreateDataSourceFromS3DataSpecTypeDef,
    _OptionalClientCreateDataSourceFromS3DataSpecTypeDef,
):
    """
    The data specification of a ``DataSource`` :
    * DataLocationS3 - The Amazon S3 location of the observation data.
    * DataSchemaLocationS3 - The Amazon S3 location of the ``DataSchema`` .
    * DataSchema - A JSON string representing the schema. This is not required if ``DataSchemaUri``
    is specified.
    * DataRearrangement - A JSON string that represents the splitting and rearrangement requirements
    for the ``Datasource`` .  Sample -
    ``"{\\"splitting\\":{\\"percentBegin\\":10,\\"percentEnd\\":60}}"``
    - **DataLocationS3** *(string) --***[REQUIRED]**

      The location of the data file(s) used by a ``DataSource`` . The URI specifies a data file or
      an Amazon Simple Storage Service (Amazon S3) directory or bucket containing data files.
    """


_ClientCreateDataSourceFromS3ResponseTypeDef = TypedDict(
    "_ClientCreateDataSourceFromS3ResponseTypeDef", {"DataSourceId": str}, total=False
)


class ClientCreateDataSourceFromS3ResponseTypeDef(_ClientCreateDataSourceFromS3ResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``CreateDataSourceFromS3`` operation, and is an acknowledgement
      that Amazon ML received the request.
      The ``CreateDataSourceFromS3`` operation is asynchronous. You can poll for updates by using
      the ``GetBatchPrediction`` operation and checking the ``Status`` parameter.
      - **DataSourceId** *(string) --*

        A user-supplied ID that uniquely identifies the ``DataSource`` . This value should be
        identical to the value of the ``DataSourceID`` in the request.
    """


_ClientCreateEvaluationResponseTypeDef = TypedDict(
    "_ClientCreateEvaluationResponseTypeDef", {"EvaluationId": str}, total=False
)


class ClientCreateEvaluationResponseTypeDef(_ClientCreateEvaluationResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``CreateEvaluation`` operation, and is an acknowledgement that
      Amazon ML received the request.
      ``CreateEvaluation`` operation is asynchronous. You can poll for status updates by using the
      ``GetEvcaluation`` operation and checking the ``Status`` parameter.
      - **EvaluationId** *(string) --*

        The user-supplied ID that uniquely identifies the ``Evaluation`` . This value should be
        identical to the value of the ``EvaluationId`` in the request.
    """


_ClientCreateMlModelResponseTypeDef = TypedDict(
    "_ClientCreateMlModelResponseTypeDef", {"MLModelId": str}, total=False
)


class ClientCreateMlModelResponseTypeDef(_ClientCreateMlModelResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``CreateMLModel`` operation, and is an acknowledgement that Amazon
      ML received the request.
      The ``CreateMLModel`` operation is asynchronous. You can poll for status updates by using the
      ``GetMLModel`` operation and checking the ``Status`` parameter.
      - **MLModelId** *(string) --*

        A user-supplied ID that uniquely identifies the ``MLModel`` . This value should be identical
        to the value of the ``MLModelId`` in the request.
    """


_ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef = TypedDict(
    "_ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": Literal["NONE", "READY", "UPDATING", "FAILED"],
    },
    total=False,
)


class ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef(
    _ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef
):
    pass


_ClientCreateRealtimeEndpointResponseTypeDef = TypedDict(
    "_ClientCreateRealtimeEndpointResponseTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef,
    },
    total=False,
)


class ClientCreateRealtimeEndpointResponseTypeDef(_ClientCreateRealtimeEndpointResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of an ``CreateRealtimeEndpoint`` operation.
      The result contains the ``MLModelId`` and the endpoint information for the ``MLModel`` .
      .. note::

        The endpoint information includes the URI of the ``MLModel`` ; that is, the location to send
        online prediction requests for the specified ``MLModel`` .
    """


_ClientDeleteBatchPredictionResponseTypeDef = TypedDict(
    "_ClientDeleteBatchPredictionResponseTypeDef", {"BatchPredictionId": str}, total=False
)


class ClientDeleteBatchPredictionResponseTypeDef(_ClientDeleteBatchPredictionResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DeleteBatchPrediction`` operation.
      You can use the ``GetBatchPrediction`` operation and check the value of the ``Status``
      parameter to see whether a ``BatchPrediction`` is marked as ``DELETED`` .
      - **BatchPredictionId** *(string) --*

        A user-supplied ID that uniquely identifies the ``BatchPrediction`` . This value should be
        identical to the value of the ``BatchPredictionID`` in the request.
    """


_ClientDeleteDataSourceResponseTypeDef = TypedDict(
    "_ClientDeleteDataSourceResponseTypeDef", {"DataSourceId": str}, total=False
)


class ClientDeleteDataSourceResponseTypeDef(_ClientDeleteDataSourceResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DeleteDataSource`` operation.
      - **DataSourceId** *(string) --*

        A user-supplied ID that uniquely identifies the ``DataSource`` . This value should be
        identical to the value of the ``DataSourceID`` in the request.
    """


_ClientDeleteEvaluationResponseTypeDef = TypedDict(
    "_ClientDeleteEvaluationResponseTypeDef", {"EvaluationId": str}, total=False
)


class ClientDeleteEvaluationResponseTypeDef(_ClientDeleteEvaluationResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DeleteEvaluation`` operation. The output indicates that Amazon
      Machine Learning (Amazon ML) received the request.
      You can use the ``GetEvaluation`` operation and check the value of the ``Status`` parameter to
      see whether an ``Evaluation`` is marked as ``DELETED`` .
      - **EvaluationId** *(string) --*

        A user-supplied ID that uniquely identifies the ``Evaluation`` . This value should be
        identical to the value of the ``EvaluationId`` in the request.
    """


_ClientDeleteMlModelResponseTypeDef = TypedDict(
    "_ClientDeleteMlModelResponseTypeDef", {"MLModelId": str}, total=False
)


class ClientDeleteMlModelResponseTypeDef(_ClientDeleteMlModelResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DeleteMLModel`` operation.
      You can use the ``GetMLModel`` operation and check the value of the ``Status`` parameter to
      see whether an ``MLModel`` is marked as ``DELETED`` .
      - **MLModelId** *(string) --*

        A user-supplied ID that uniquely identifies the ``MLModel`` . This value should be identical
        to the value of the ``MLModelID`` in the request.
    """


_ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef = TypedDict(
    "_ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": Literal["NONE", "READY", "UPDATING", "FAILED"],
    },
    total=False,
)


class ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef(
    _ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef
):
    pass


_ClientDeleteRealtimeEndpointResponseTypeDef = TypedDict(
    "_ClientDeleteRealtimeEndpointResponseTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef,
    },
    total=False,
)


class ClientDeleteRealtimeEndpointResponseTypeDef(_ClientDeleteRealtimeEndpointResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of an ``DeleteRealtimeEndpoint`` operation.
      The result contains the ``MLModelId`` and the endpoint information for the ``MLModel`` .
      - **MLModelId** *(string) --*

        A user-supplied ID that uniquely identifies the ``MLModel`` . This value should be identical
        to the value of the ``MLModelId`` in the request.
    """


_ClientDeleteTagsResponseTypeDef = TypedDict(
    "_ClientDeleteTagsResponseTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"],
    },
    total=False,
)


class ClientDeleteTagsResponseTypeDef(_ClientDeleteTagsResponseTypeDef):
    """
    - *(dict) --*

      Amazon ML returns the following elements.
      - **ResourceId** *(string) --*

        The ID of the ML object from which tags were deleted.
    """


_ClientDescribeBatchPredictionsResponseResultsTypeDef = TypedDict(
    "_ClientDescribeBatchPredictionsResponseResultsTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "OutputUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "TotalRecordCount": int,
        "InvalidRecordCount": int,
    },
    total=False,
)


class ClientDescribeBatchPredictionsResponseResultsTypeDef(
    _ClientDescribeBatchPredictionsResponseResultsTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``GetBatchPrediction`` operation.
      The content consists of the detailed metadata, the status, and the data file information of a
      ``Batch Prediction`` .
      - **BatchPredictionId** *(string) --*

        The ID assigned to the ``BatchPrediction`` at creation. This value should be identical to
        the value of the ``BatchPredictionID`` in the request.
    """


_ClientDescribeBatchPredictionsResponseTypeDef = TypedDict(
    "_ClientDescribeBatchPredictionsResponseTypeDef",
    {"Results": List[ClientDescribeBatchPredictionsResponseResultsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeBatchPredictionsResponseTypeDef(_ClientDescribeBatchPredictionsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DescribeBatchPredictions`` operation. The content is essentially
      a list of ``BatchPrediction`` s.
      - **Results** *(list) --*

        A list of ``BatchPrediction`` objects that meet the search criteria.
        - *(dict) --*

          Represents the output of a ``GetBatchPrediction`` operation.
          The content consists of the detailed metadata, the status, and the data file information
          of a ``Batch Prediction`` .
          - **BatchPredictionId** *(string) --*

            The ID assigned to the ``BatchPrediction`` at creation. This value should be identical
            to the value of the ``BatchPredictionID`` in the request.
    """


_ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef = TypedDict(
    "_ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef",
    {"InstanceIdentifier": str, "DatabaseName": str},
    total=False,
)


class ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef(
    _ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef
):
    pass


_ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef = TypedDict(
    "_ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef",
    {
        "Database": ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "DataPipelineId": str,
    },
    total=False,
)


class ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef(
    _ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef
):
    pass


_ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef = TypedDict(
    "_ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef",
    {"DatabaseName": str, "ClusterIdentifier": str},
    total=False,
)


class ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef(
    _ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef
):
    pass


_ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef = TypedDict(
    "_ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef",
    {
        "RedshiftDatabase": ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
    },
    total=False,
)


class ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef(
    _ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef
):
    pass


_ClientDescribeDataSourcesResponseResultsTypeDef = TypedDict(
    "_ClientDescribeDataSourcesResponseResultsTypeDef",
    {
        "DataSourceId": str,
        "DataLocationS3": str,
        "DataRearrangement": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "DataSizeInBytes": int,
        "NumberOfFiles": int,
        "Name": str,
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "Message": str,
        "RedshiftMetadata": ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef,
        "RDSMetadata": ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef,
        "RoleARN": str,
        "ComputeStatistics": bool,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class ClientDescribeDataSourcesResponseResultsTypeDef(
    _ClientDescribeDataSourcesResponseResultsTypeDef
):
    """
    - *(dict) --*

      Represents the output of the ``GetDataSource`` operation.
      The content consists of the detailed metadata and data file information and the current status
      of the ``DataSource`` .
      - **DataSourceId** *(string) --*

        The ID that is assigned to the ``DataSource`` during creation.
    """


_ClientDescribeDataSourcesResponseTypeDef = TypedDict(
    "_ClientDescribeDataSourcesResponseTypeDef",
    {"Results": List[ClientDescribeDataSourcesResponseResultsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeDataSourcesResponseTypeDef(_ClientDescribeDataSourcesResponseTypeDef):
    """
    - *(dict) --*

      Represents the query results from a  DescribeDataSources operation. The content is essentially
      a list of ``DataSource`` .
      - **Results** *(list) --*

        A list of ``DataSource`` that meet the search criteria.
        - *(dict) --*

          Represents the output of the ``GetDataSource`` operation.
          The content consists of the detailed metadata and data file information and the current
          status of the ``DataSource`` .
          - **DataSourceId** *(string) --*

            The ID that is assigned to the ``DataSource`` during creation.
    """


_ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef = TypedDict(
    "_ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef",
    {"Properties": Dict[str, str]},
    total=False,
)


class ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef(
    _ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef
):
    pass


_ClientDescribeEvaluationsResponseResultsTypeDef = TypedDict(
    "_ClientDescribeEvaluationsResponseResultsTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "PerformanceMetrics": ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class ClientDescribeEvaluationsResponseResultsTypeDef(
    _ClientDescribeEvaluationsResponseResultsTypeDef
):
    """
    - *(dict) --*

      Represents the output of ``GetEvaluation`` operation.
      The content consists of the detailed metadata and data file information and the current status
      of the ``Evaluation`` .
      - **EvaluationId** *(string) --*

        The ID that is assigned to the ``Evaluation`` at creation.
    """


_ClientDescribeEvaluationsResponseTypeDef = TypedDict(
    "_ClientDescribeEvaluationsResponseTypeDef",
    {"Results": List[ClientDescribeEvaluationsResponseResultsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeEvaluationsResponseTypeDef(_ClientDescribeEvaluationsResponseTypeDef):
    """
    - *(dict) --*

      Represents the query results from a ``DescribeEvaluations`` operation. The content is
      essentially a list of ``Evaluation`` .
      - **Results** *(list) --*

        A list of ``Evaluation`` that meet the search criteria.
        - *(dict) --*

          Represents the output of ``GetEvaluation`` operation.
          The content consists of the detailed metadata and data file information and the current
          status of the ``Evaluation`` .
          - **EvaluationId** *(string) --*

            The ID that is assigned to the ``Evaluation`` at creation.
    """


_ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef = TypedDict(
    "_ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": Literal["NONE", "READY", "UPDATING", "FAILED"],
    },
    total=False,
)


class ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef(
    _ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef
):
    pass


_ClientDescribeMlModelsResponseResultsTypeDef = TypedDict(
    "_ClientDescribeMlModelsResponseResultsTypeDef",
    {
        "MLModelId": str,
        "TrainingDataSourceId": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "SizeInBytes": int,
        "EndpointInfo": ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef,
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "Algorithm": str,
        "MLModelType": Literal["REGRESSION", "BINARY", "MULTICLASS"],
        "ScoreThreshold": Any,
        "ScoreThresholdLastUpdatedAt": datetime,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class ClientDescribeMlModelsResponseResultsTypeDef(_ClientDescribeMlModelsResponseResultsTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``GetMLModel`` operation.
      The content consists of the detailed metadata and the current status of the ``MLModel`` .
      - **MLModelId** *(string) --*

        The ID assigned to the ``MLModel`` at creation.
    """


_ClientDescribeMlModelsResponseTypeDef = TypedDict(
    "_ClientDescribeMlModelsResponseTypeDef",
    {"Results": List[ClientDescribeMlModelsResponseResultsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeMlModelsResponseTypeDef(_ClientDescribeMlModelsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DescribeMLModels`` operation. The content is essentially a list
      of ``MLModel`` .
      - **Results** *(list) --*

        A list of ``MLModel`` that meet the search criteria.
        - *(dict) --*

          Represents the output of a ``GetMLModel`` operation.
          The content consists of the detailed metadata and the current status of the ``MLModel`` .
          - **MLModelId** *(string) --*

            The ID assigned to the ``MLModel`` at creation.
    """


_ClientDescribeTagsResponseTagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeTagsResponseTagsTypeDef(_ClientDescribeTagsResponseTagsTypeDef):
    pass


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"],
        "Tags": List[ClientDescribeTagsResponseTagsTypeDef],
    },
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    - *(dict) --*

      Amazon ML returns the following elements.
      - **ResourceId** *(string) --*

        The ID of the tagged ML object.
    """


_ClientGetBatchPredictionResponseTypeDef = TypedDict(
    "_ClientGetBatchPredictionResponseTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "OutputUri": str,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "TotalRecordCount": int,
        "InvalidRecordCount": int,
    },
    total=False,
)


class ClientGetBatchPredictionResponseTypeDef(_ClientGetBatchPredictionResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``GetBatchPrediction`` operation and describes a
      ``BatchPrediction`` .
      - **BatchPredictionId** *(string) --*

        An ID assigned to the ``BatchPrediction`` at creation. This value should be identical to the
        value of the ``BatchPredictionID`` in the request.
    """


_ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef = TypedDict(
    "_ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef",
    {"InstanceIdentifier": str, "DatabaseName": str},
    total=False,
)


class ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef(
    _ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef
):
    pass


_ClientGetDataSourceResponseRDSMetadataTypeDef = TypedDict(
    "_ClientGetDataSourceResponseRDSMetadataTypeDef",
    {
        "Database": ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "DataPipelineId": str,
    },
    total=False,
)


class ClientGetDataSourceResponseRDSMetadataTypeDef(_ClientGetDataSourceResponseRDSMetadataTypeDef):
    pass


_ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef = TypedDict(
    "_ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef",
    {"DatabaseName": str, "ClusterIdentifier": str},
    total=False,
)


class ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef(
    _ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef
):
    pass


_ClientGetDataSourceResponseRedshiftMetadataTypeDef = TypedDict(
    "_ClientGetDataSourceResponseRedshiftMetadataTypeDef",
    {
        "RedshiftDatabase": ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
    },
    total=False,
)


class ClientGetDataSourceResponseRedshiftMetadataTypeDef(
    _ClientGetDataSourceResponseRedshiftMetadataTypeDef
):
    pass


_ClientGetDataSourceResponseTypeDef = TypedDict(
    "_ClientGetDataSourceResponseTypeDef",
    {
        "DataSourceId": str,
        "DataLocationS3": str,
        "DataRearrangement": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "DataSizeInBytes": int,
        "NumberOfFiles": int,
        "Name": str,
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "LogUri": str,
        "Message": str,
        "RedshiftMetadata": ClientGetDataSourceResponseRedshiftMetadataTypeDef,
        "RDSMetadata": ClientGetDataSourceResponseRDSMetadataTypeDef,
        "RoleARN": str,
        "ComputeStatistics": bool,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "DataSourceSchema": str,
    },
    total=False,
)


class ClientGetDataSourceResponseTypeDef(_ClientGetDataSourceResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``GetDataSource`` operation and describes a ``DataSource`` .
      - **DataSourceId** *(string) --*

        The ID assigned to the ``DataSource`` at creation. This value should be identical to the
        value of the ``DataSourceId`` in the request.
    """


_ClientGetEvaluationResponsePerformanceMetricsTypeDef = TypedDict(
    "_ClientGetEvaluationResponsePerformanceMetricsTypeDef",
    {"Properties": Dict[str, str]},
    total=False,
)


class ClientGetEvaluationResponsePerformanceMetricsTypeDef(
    _ClientGetEvaluationResponsePerformanceMetricsTypeDef
):
    pass


_ClientGetEvaluationResponseTypeDef = TypedDict(
    "_ClientGetEvaluationResponseTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "PerformanceMetrics": ClientGetEvaluationResponsePerformanceMetricsTypeDef,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class ClientGetEvaluationResponseTypeDef(_ClientGetEvaluationResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``GetEvaluation`` operation and describes an ``Evaluation`` .
      - **EvaluationId** *(string) --*

        The evaluation ID which is same as the ``EvaluationId`` in the request.
    """


_ClientGetMlModelResponseEndpointInfoTypeDef = TypedDict(
    "_ClientGetMlModelResponseEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": Literal["NONE", "READY", "UPDATING", "FAILED"],
    },
    total=False,
)


class ClientGetMlModelResponseEndpointInfoTypeDef(_ClientGetMlModelResponseEndpointInfoTypeDef):
    pass


_ClientGetMlModelResponseTypeDef = TypedDict(
    "_ClientGetMlModelResponseTypeDef",
    {
        "MLModelId": str,
        "TrainingDataSourceId": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "SizeInBytes": int,
        "EndpointInfo": ClientGetMlModelResponseEndpointInfoTypeDef,
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "MLModelType": Literal["REGRESSION", "BINARY", "MULTICLASS"],
        "ScoreThreshold": Any,
        "ScoreThresholdLastUpdatedAt": datetime,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "Recipe": str,
        "Schema": str,
    },
    total=False,
)


class ClientGetMlModelResponseTypeDef(_ClientGetMlModelResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``GetMLModel`` operation, and provides detailed information about a
      ``MLModel`` .
      - **MLModelId** *(string) --*

        The MLModel ID,which is same as the ``MLModelId`` in the request.
    """


_ClientPredictResponsePredictionTypeDef = TypedDict(
    "_ClientPredictResponsePredictionTypeDef",
    {
        "predictedLabel": str,
        "predictedValue": Any,
        "predictedScores": Dict[str, Any],
        "details": Dict[str, str],
    },
    total=False,
)


class ClientPredictResponsePredictionTypeDef(_ClientPredictResponsePredictionTypeDef):
    """
    - **Prediction** *(dict) --*

      The output from a ``Predict`` operation:
      * ``Details`` - Contains the following attributes: ``DetailsAttributes.PREDICTIVE_MODEL_TYPE -
      REGRESSION | BINARY | MULTICLASS``  ``DetailsAttributes.ALGORITHM - SGD``
      * ``PredictedLabel`` - Present for either a ``BINARY`` or ``MULTICLASS``  ``MLModel`` request.
      * ``PredictedScores`` - Contains the raw classification score corresponding to each label.
      * ``PredictedValue`` - Present for a ``REGRESSION``  ``MLModel`` request.
      - **predictedLabel** *(string) --*

        The prediction label for either a ``BINARY`` or ``MULTICLASS``  ``MLModel`` .
    """


_ClientPredictResponseTypeDef = TypedDict(
    "_ClientPredictResponseTypeDef",
    {"Prediction": ClientPredictResponsePredictionTypeDef},
    total=False,
)


class ClientPredictResponseTypeDef(_ClientPredictResponseTypeDef):
    """
    - *(dict) --*

      - **Prediction** *(dict) --*

        The output from a ``Predict`` operation:
        * ``Details`` - Contains the following attributes: ``DetailsAttributes.PREDICTIVE_MODEL_TYPE
        - REGRESSION | BINARY | MULTICLASS``  ``DetailsAttributes.ALGORITHM - SGD``
        * ``PredictedLabel`` - Present for either a ``BINARY`` or ``MULTICLASS``  ``MLModel``
        request.
        * ``PredictedScores`` - Contains the raw classification score corresponding to each label.
        * ``PredictedValue`` - Present for a ``REGRESSION``  ``MLModel`` request.
        - **predictedLabel** *(string) --*

          The prediction label for either a ``BINARY`` or ``MULTICLASS``  ``MLModel`` .
    """


_ClientUpdateBatchPredictionResponseTypeDef = TypedDict(
    "_ClientUpdateBatchPredictionResponseTypeDef", {"BatchPredictionId": str}, total=False
)


class ClientUpdateBatchPredictionResponseTypeDef(_ClientUpdateBatchPredictionResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of an ``UpdateBatchPrediction`` operation.
      You can see the updated content by using the ``GetBatchPrediction`` operation.
      - **BatchPredictionId** *(string) --*

        The ID assigned to the ``BatchPrediction`` during creation. This value should be identical
        to the value of the ``BatchPredictionId`` in the request.
    """


_ClientUpdateDataSourceResponseTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponseTypeDef", {"DataSourceId": str}, total=False
)


class ClientUpdateDataSourceResponseTypeDef(_ClientUpdateDataSourceResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of an ``UpdateDataSource`` operation.
      You can see the updated content by using the ``GetBatchPrediction`` operation.
      - **DataSourceId** *(string) --*

        The ID assigned to the ``DataSource`` during creation. This value should be identical to the
        value of the ``DataSourceID`` in the request.
    """


_ClientUpdateEvaluationResponseTypeDef = TypedDict(
    "_ClientUpdateEvaluationResponseTypeDef", {"EvaluationId": str}, total=False
)


class ClientUpdateEvaluationResponseTypeDef(_ClientUpdateEvaluationResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of an ``UpdateEvaluation`` operation.
      You can see the updated content by using the ``GetEvaluation`` operation.
      - **EvaluationId** *(string) --*

        The ID assigned to the ``Evaluation`` during creation. This value should be identical to the
        value of the ``Evaluation`` in the request.
    """


_ClientUpdateMlModelResponseTypeDef = TypedDict(
    "_ClientUpdateMlModelResponseTypeDef", {"MLModelId": str}, total=False
)


class ClientUpdateMlModelResponseTypeDef(_ClientUpdateMlModelResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of an ``UpdateMLModel`` operation.
      You can see the updated content by using the ``GetMLModel`` operation.
      - **MLModelId** *(string) --*

        The ID assigned to the ``MLModel`` during creation. This value should be identical to the
        value of the ``MLModelID`` in the request.
    """


_DataSourceAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_DataSourceAvailableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class DataSourceAvailableWaitWaiterConfigTypeDef(_DataSourceAvailableWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_DescribeBatchPredictionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeBatchPredictionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeBatchPredictionsPaginatePaginationConfigTypeDef(
    _DescribeBatchPredictionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeBatchPredictionsPaginateResponseResultsTypeDef = TypedDict(
    "_DescribeBatchPredictionsPaginateResponseResultsTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "OutputUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "TotalRecordCount": int,
        "InvalidRecordCount": int,
    },
    total=False,
)


class DescribeBatchPredictionsPaginateResponseResultsTypeDef(
    _DescribeBatchPredictionsPaginateResponseResultsTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``GetBatchPrediction`` operation.
      The content consists of the detailed metadata, the status, and the data file information of a
      ``Batch Prediction`` .
      - **BatchPredictionId** *(string) --*

        The ID assigned to the ``BatchPrediction`` at creation. This value should be identical to
        the value of the ``BatchPredictionID`` in the request.
    """


_DescribeBatchPredictionsPaginateResponseTypeDef = TypedDict(
    "_DescribeBatchPredictionsPaginateResponseTypeDef",
    {"Results": List[DescribeBatchPredictionsPaginateResponseResultsTypeDef]},
    total=False,
)


class DescribeBatchPredictionsPaginateResponseTypeDef(
    _DescribeBatchPredictionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``DescribeBatchPredictions`` operation. The content is essentially
      a list of ``BatchPrediction`` s.
      - **Results** *(list) --*

        A list of ``BatchPrediction`` objects that meet the search criteria.
        - *(dict) --*

          Represents the output of a ``GetBatchPrediction`` operation.
          The content consists of the detailed metadata, the status, and the data file information
          of a ``Batch Prediction`` .
          - **BatchPredictionId** *(string) --*

            The ID assigned to the ``BatchPrediction`` at creation. This value should be identical
            to the value of the ``BatchPredictionID`` in the request.
    """


_DescribeDataSourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDataSourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDataSourcesPaginatePaginationConfigTypeDef(
    _DescribeDataSourcesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef = TypedDict(
    "_DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef",
    {"InstanceIdentifier": str, "DatabaseName": str},
    total=False,
)


class DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef(
    _DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef
):
    pass


_DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef = TypedDict(
    "_DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef",
    {
        "Database": DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "DataPipelineId": str,
    },
    total=False,
)


class DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef(
    _DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef
):
    pass


_DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef = TypedDict(
    "_DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef",
    {"DatabaseName": str, "ClusterIdentifier": str},
    total=False,
)


class DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef(
    _DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef
):
    pass


_DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef = TypedDict(
    "_DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef",
    {
        "RedshiftDatabase": DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
    },
    total=False,
)


class DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef(
    _DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef
):
    pass


_DescribeDataSourcesPaginateResponseResultsTypeDef = TypedDict(
    "_DescribeDataSourcesPaginateResponseResultsTypeDef",
    {
        "DataSourceId": str,
        "DataLocationS3": str,
        "DataRearrangement": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "DataSizeInBytes": int,
        "NumberOfFiles": int,
        "Name": str,
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "Message": str,
        "RedshiftMetadata": DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef,
        "RDSMetadata": DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef,
        "RoleARN": str,
        "ComputeStatistics": bool,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class DescribeDataSourcesPaginateResponseResultsTypeDef(
    _DescribeDataSourcesPaginateResponseResultsTypeDef
):
    """
    - *(dict) --*

      Represents the output of the ``GetDataSource`` operation.
      The content consists of the detailed metadata and data file information and the current status
      of the ``DataSource`` .
      - **DataSourceId** *(string) --*

        The ID that is assigned to the ``DataSource`` during creation.
    """


_DescribeDataSourcesPaginateResponseTypeDef = TypedDict(
    "_DescribeDataSourcesPaginateResponseTypeDef",
    {"Results": List[DescribeDataSourcesPaginateResponseResultsTypeDef]},
    total=False,
)


class DescribeDataSourcesPaginateResponseTypeDef(_DescribeDataSourcesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the query results from a  DescribeDataSources operation. The content is essentially
      a list of ``DataSource`` .
      - **Results** *(list) --*

        A list of ``DataSource`` that meet the search criteria.
        - *(dict) --*

          Represents the output of the ``GetDataSource`` operation.
          The content consists of the detailed metadata and data file information and the current
          status of the ``DataSource`` .
          - **DataSourceId** *(string) --*

            The ID that is assigned to the ``DataSource`` during creation.
    """


_DescribeEvaluationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEvaluationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEvaluationsPaginatePaginationConfigTypeDef(
    _DescribeEvaluationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef = TypedDict(
    "_DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef",
    {"Properties": Dict[str, str]},
    total=False,
)


class DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef(
    _DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef
):
    pass


_DescribeEvaluationsPaginateResponseResultsTypeDef = TypedDict(
    "_DescribeEvaluationsPaginateResponseResultsTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "PerformanceMetrics": DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class DescribeEvaluationsPaginateResponseResultsTypeDef(
    _DescribeEvaluationsPaginateResponseResultsTypeDef
):
    """
    - *(dict) --*

      Represents the output of ``GetEvaluation`` operation.
      The content consists of the detailed metadata and data file information and the current status
      of the ``Evaluation`` .
      - **EvaluationId** *(string) --*

        The ID that is assigned to the ``Evaluation`` at creation.
    """


_DescribeEvaluationsPaginateResponseTypeDef = TypedDict(
    "_DescribeEvaluationsPaginateResponseTypeDef",
    {"Results": List[DescribeEvaluationsPaginateResponseResultsTypeDef]},
    total=False,
)


class DescribeEvaluationsPaginateResponseTypeDef(_DescribeEvaluationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the query results from a ``DescribeEvaluations`` operation. The content is
      essentially a list of ``Evaluation`` .
      - **Results** *(list) --*

        A list of ``Evaluation`` that meet the search criteria.
        - *(dict) --*

          Represents the output of ``GetEvaluation`` operation.
          The content consists of the detailed metadata and data file information and the current
          status of the ``Evaluation`` .
          - **EvaluationId** *(string) --*

            The ID that is assigned to the ``Evaluation`` at creation.
    """


_DescribeMLModelsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMLModelsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMLModelsPaginatePaginationConfigTypeDef(
    _DescribeMLModelsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef = TypedDict(
    "_DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": Literal["NONE", "READY", "UPDATING", "FAILED"],
    },
    total=False,
)


class DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef(
    _DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef
):
    pass


_DescribeMLModelsPaginateResponseResultsTypeDef = TypedDict(
    "_DescribeMLModelsPaginateResponseResultsTypeDef",
    {
        "MLModelId": str,
        "TrainingDataSourceId": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "SizeInBytes": int,
        "EndpointInfo": DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef,
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "Algorithm": str,
        "MLModelType": Literal["REGRESSION", "BINARY", "MULTICLASS"],
        "ScoreThreshold": Any,
        "ScoreThresholdLastUpdatedAt": datetime,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)


class DescribeMLModelsPaginateResponseResultsTypeDef(
    _DescribeMLModelsPaginateResponseResultsTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``GetMLModel`` operation.
      The content consists of the detailed metadata and the current status of the ``MLModel`` .
      - **MLModelId** *(string) --*

        The ID assigned to the ``MLModel`` at creation.
    """


_DescribeMLModelsPaginateResponseTypeDef = TypedDict(
    "_DescribeMLModelsPaginateResponseTypeDef",
    {"Results": List[DescribeMLModelsPaginateResponseResultsTypeDef]},
    total=False,
)


class DescribeMLModelsPaginateResponseTypeDef(_DescribeMLModelsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DescribeMLModels`` operation. The content is essentially a list
      of ``MLModel`` .
      - **Results** *(list) --*

        A list of ``MLModel`` that meet the search criteria.
        - *(dict) --*

          Represents the output of a ``GetMLModel`` operation.
          The content consists of the detailed metadata and the current status of the ``MLModel`` .
          - **MLModelId** *(string) --*

            The ID assigned to the ``MLModel`` at creation.
    """


_EvaluationAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_EvaluationAvailableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class EvaluationAvailableWaitWaiterConfigTypeDef(_EvaluationAvailableWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_MlModelAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_MlModelAvailableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class MlModelAvailableWaitWaiterConfigTypeDef(_MlModelAvailableWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """
