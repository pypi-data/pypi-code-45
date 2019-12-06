"Main interface for machinelearning service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


BatchPredictionAvailableWaitWaiterConfigTypeDef = TypedDict(
    "BatchPredictionAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)

ClientAddTagsResponseTypeDef = TypedDict(
    "ClientAddTagsResponseTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"],
    },
    total=False,
)

ClientAddTagsTagsTypeDef = TypedDict(
    "ClientAddTagsTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateBatchPredictionResponseTypeDef = TypedDict(
    "ClientCreateBatchPredictionResponseTypeDef", {"BatchPredictionId": str}, total=False
)

ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef = TypedDict(
    "ClientCreateDataSourceFromRdsRDSDataDatabaseCredentialsTypeDef",
    {"Username": str, "Password": str},
    total=False,
)

ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef = TypedDict(
    "ClientCreateDataSourceFromRdsRDSDataDatabaseInformationTypeDef",
    {"InstanceIdentifier": str, "DatabaseName": str},
    total=False,
)

ClientCreateDataSourceFromRdsRDSDataTypeDef = TypedDict(
    "ClientCreateDataSourceFromRdsRDSDataTypeDef",
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

ClientCreateDataSourceFromRdsResponseTypeDef = TypedDict(
    "ClientCreateDataSourceFromRdsResponseTypeDef", {"DataSourceId": str}, total=False
)

ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef = TypedDict(
    "ClientCreateDataSourceFromRedshiftDataSpecDatabaseCredentialsTypeDef",
    {"Username": str, "Password": str},
    total=False,
)

ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef = TypedDict(
    "ClientCreateDataSourceFromRedshiftDataSpecDatabaseInformationTypeDef",
    {"DatabaseName": str, "ClusterIdentifier": str},
    total=False,
)

ClientCreateDataSourceFromRedshiftDataSpecTypeDef = TypedDict(
    "ClientCreateDataSourceFromRedshiftDataSpecTypeDef",
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

ClientCreateDataSourceFromRedshiftResponseTypeDef = TypedDict(
    "ClientCreateDataSourceFromRedshiftResponseTypeDef", {"DataSourceId": str}, total=False
)

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
    pass


ClientCreateDataSourceFromS3ResponseTypeDef = TypedDict(
    "ClientCreateDataSourceFromS3ResponseTypeDef", {"DataSourceId": str}, total=False
)

ClientCreateEvaluationResponseTypeDef = TypedDict(
    "ClientCreateEvaluationResponseTypeDef", {"EvaluationId": str}, total=False
)

ClientCreateMlModelResponseTypeDef = TypedDict(
    "ClientCreateMlModelResponseTypeDef", {"MLModelId": str}, total=False
)

ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef = TypedDict(
    "ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": Literal["NONE", "READY", "UPDATING", "FAILED"],
    },
    total=False,
)

ClientCreateRealtimeEndpointResponseTypeDef = TypedDict(
    "ClientCreateRealtimeEndpointResponseTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": ClientCreateRealtimeEndpointResponseRealtimeEndpointInfoTypeDef,
    },
    total=False,
)

ClientDeleteBatchPredictionResponseTypeDef = TypedDict(
    "ClientDeleteBatchPredictionResponseTypeDef", {"BatchPredictionId": str}, total=False
)

ClientDeleteDataSourceResponseTypeDef = TypedDict(
    "ClientDeleteDataSourceResponseTypeDef", {"DataSourceId": str}, total=False
)

ClientDeleteEvaluationResponseTypeDef = TypedDict(
    "ClientDeleteEvaluationResponseTypeDef", {"EvaluationId": str}, total=False
)

ClientDeleteMlModelResponseTypeDef = TypedDict(
    "ClientDeleteMlModelResponseTypeDef", {"MLModelId": str}, total=False
)

ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef = TypedDict(
    "ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": Literal["NONE", "READY", "UPDATING", "FAILED"],
    },
    total=False,
)

ClientDeleteRealtimeEndpointResponseTypeDef = TypedDict(
    "ClientDeleteRealtimeEndpointResponseTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": ClientDeleteRealtimeEndpointResponseRealtimeEndpointInfoTypeDef,
    },
    total=False,
)

ClientDeleteTagsResponseTypeDef = TypedDict(
    "ClientDeleteTagsResponseTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"],
    },
    total=False,
)

ClientDescribeBatchPredictionsResponseResultsTypeDef = TypedDict(
    "ClientDescribeBatchPredictionsResponseResultsTypeDef",
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

ClientDescribeBatchPredictionsResponseTypeDef = TypedDict(
    "ClientDescribeBatchPredictionsResponseTypeDef",
    {"Results": List[ClientDescribeBatchPredictionsResponseResultsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef = TypedDict(
    "ClientDescribeDataSourcesResponseResultsRDSMetadataDatabaseTypeDef",
    {"InstanceIdentifier": str, "DatabaseName": str},
    total=False,
)

ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef = TypedDict(
    "ClientDescribeDataSourcesResponseResultsRDSMetadataTypeDef",
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

ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef = TypedDict(
    "ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef",
    {"DatabaseName": str, "ClusterIdentifier": str},
    total=False,
)

ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef = TypedDict(
    "ClientDescribeDataSourcesResponseResultsRedshiftMetadataTypeDef",
    {
        "RedshiftDatabase": ClientDescribeDataSourcesResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
    },
    total=False,
)

ClientDescribeDataSourcesResponseResultsTypeDef = TypedDict(
    "ClientDescribeDataSourcesResponseResultsTypeDef",
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

ClientDescribeDataSourcesResponseTypeDef = TypedDict(
    "ClientDescribeDataSourcesResponseTypeDef",
    {"Results": List[ClientDescribeDataSourcesResponseResultsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef = TypedDict(
    "ClientDescribeEvaluationsResponseResultsPerformanceMetricsTypeDef",
    {"Properties": Dict[str, str]},
    total=False,
)

ClientDescribeEvaluationsResponseResultsTypeDef = TypedDict(
    "ClientDescribeEvaluationsResponseResultsTypeDef",
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

ClientDescribeEvaluationsResponseTypeDef = TypedDict(
    "ClientDescribeEvaluationsResponseTypeDef",
    {"Results": List[ClientDescribeEvaluationsResponseResultsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef = TypedDict(
    "ClientDescribeMlModelsResponseResultsEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": Literal["NONE", "READY", "UPDATING", "FAILED"],
    },
    total=False,
)

ClientDescribeMlModelsResponseResultsTypeDef = TypedDict(
    "ClientDescribeMlModelsResponseResultsTypeDef",
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

ClientDescribeMlModelsResponseTypeDef = TypedDict(
    "ClientDescribeMlModelsResponseTypeDef",
    {"Results": List[ClientDescribeMlModelsResponseResultsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeTagsResponseTagsTypeDef = TypedDict(
    "ClientDescribeTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeTagsResponseTypeDef = TypedDict(
    "ClientDescribeTagsResponseTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"],
        "Tags": List[ClientDescribeTagsResponseTagsTypeDef],
    },
    total=False,
)

ClientGetBatchPredictionResponseTypeDef = TypedDict(
    "ClientGetBatchPredictionResponseTypeDef",
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

ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef = TypedDict(
    "ClientGetDataSourceResponseRDSMetadataDatabaseTypeDef",
    {"InstanceIdentifier": str, "DatabaseName": str},
    total=False,
)

ClientGetDataSourceResponseRDSMetadataTypeDef = TypedDict(
    "ClientGetDataSourceResponseRDSMetadataTypeDef",
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

ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef = TypedDict(
    "ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef",
    {"DatabaseName": str, "ClusterIdentifier": str},
    total=False,
)

ClientGetDataSourceResponseRedshiftMetadataTypeDef = TypedDict(
    "ClientGetDataSourceResponseRedshiftMetadataTypeDef",
    {
        "RedshiftDatabase": ClientGetDataSourceResponseRedshiftMetadataRedshiftDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
    },
    total=False,
)

ClientGetDataSourceResponseTypeDef = TypedDict(
    "ClientGetDataSourceResponseTypeDef",
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

ClientGetEvaluationResponsePerformanceMetricsTypeDef = TypedDict(
    "ClientGetEvaluationResponsePerformanceMetricsTypeDef",
    {"Properties": Dict[str, str]},
    total=False,
)

ClientGetEvaluationResponseTypeDef = TypedDict(
    "ClientGetEvaluationResponseTypeDef",
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

ClientGetMlModelResponseEndpointInfoTypeDef = TypedDict(
    "ClientGetMlModelResponseEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": Literal["NONE", "READY", "UPDATING", "FAILED"],
    },
    total=False,
)

ClientGetMlModelResponseTypeDef = TypedDict(
    "ClientGetMlModelResponseTypeDef",
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

ClientPredictResponsePredictionTypeDef = TypedDict(
    "ClientPredictResponsePredictionTypeDef",
    {
        "predictedLabel": str,
        "predictedValue": Any,
        "predictedScores": Dict[str, Any],
        "details": Dict[str, str],
    },
    total=False,
)

ClientPredictResponseTypeDef = TypedDict(
    "ClientPredictResponseTypeDef",
    {"Prediction": ClientPredictResponsePredictionTypeDef},
    total=False,
)

ClientUpdateBatchPredictionResponseTypeDef = TypedDict(
    "ClientUpdateBatchPredictionResponseTypeDef", {"BatchPredictionId": str}, total=False
)

ClientUpdateDataSourceResponseTypeDef = TypedDict(
    "ClientUpdateDataSourceResponseTypeDef", {"DataSourceId": str}, total=False
)

ClientUpdateEvaluationResponseTypeDef = TypedDict(
    "ClientUpdateEvaluationResponseTypeDef", {"EvaluationId": str}, total=False
)

ClientUpdateMlModelResponseTypeDef = TypedDict(
    "ClientUpdateMlModelResponseTypeDef", {"MLModelId": str}, total=False
)

DataSourceAvailableWaitWaiterConfigTypeDef = TypedDict(
    "DataSourceAvailableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

DescribeBatchPredictionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeBatchPredictionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeBatchPredictionsPaginateResponseResultsTypeDef = TypedDict(
    "DescribeBatchPredictionsPaginateResponseResultsTypeDef",
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

DescribeBatchPredictionsPaginateResponseTypeDef = TypedDict(
    "DescribeBatchPredictionsPaginateResponseTypeDef",
    {"Results": List[DescribeBatchPredictionsPaginateResponseResultsTypeDef]},
    total=False,
)

DescribeDataSourcesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeDataSourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef = TypedDict(
    "DescribeDataSourcesPaginateResponseResultsRDSMetadataDatabaseTypeDef",
    {"InstanceIdentifier": str, "DatabaseName": str},
    total=False,
)

DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef = TypedDict(
    "DescribeDataSourcesPaginateResponseResultsRDSMetadataTypeDef",
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

DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef = TypedDict(
    "DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef",
    {"DatabaseName": str, "ClusterIdentifier": str},
    total=False,
)

DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef = TypedDict(
    "DescribeDataSourcesPaginateResponseResultsRedshiftMetadataTypeDef",
    {
        "RedshiftDatabase": DescribeDataSourcesPaginateResponseResultsRedshiftMetadataRedshiftDatabaseTypeDef,
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
    },
    total=False,
)

DescribeDataSourcesPaginateResponseResultsTypeDef = TypedDict(
    "DescribeDataSourcesPaginateResponseResultsTypeDef",
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

DescribeDataSourcesPaginateResponseTypeDef = TypedDict(
    "DescribeDataSourcesPaginateResponseTypeDef",
    {"Results": List[DescribeDataSourcesPaginateResponseResultsTypeDef]},
    total=False,
)

DescribeEvaluationsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeEvaluationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef = TypedDict(
    "DescribeEvaluationsPaginateResponseResultsPerformanceMetricsTypeDef",
    {"Properties": Dict[str, str]},
    total=False,
)

DescribeEvaluationsPaginateResponseResultsTypeDef = TypedDict(
    "DescribeEvaluationsPaginateResponseResultsTypeDef",
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

DescribeEvaluationsPaginateResponseTypeDef = TypedDict(
    "DescribeEvaluationsPaginateResponseTypeDef",
    {"Results": List[DescribeEvaluationsPaginateResponseResultsTypeDef]},
    total=False,
)

DescribeMLModelsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeMLModelsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef = TypedDict(
    "DescribeMLModelsPaginateResponseResultsEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": Literal["NONE", "READY", "UPDATING", "FAILED"],
    },
    total=False,
)

DescribeMLModelsPaginateResponseResultsTypeDef = TypedDict(
    "DescribeMLModelsPaginateResponseResultsTypeDef",
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

DescribeMLModelsPaginateResponseTypeDef = TypedDict(
    "DescribeMLModelsPaginateResponseTypeDef",
    {"Results": List[DescribeMLModelsPaginateResponseResultsTypeDef]},
    total=False,
)

EvaluationAvailableWaitWaiterConfigTypeDef = TypedDict(
    "EvaluationAvailableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

MlModelAvailableWaitWaiterConfigTypeDef = TypedDict(
    "MlModelAvailableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
