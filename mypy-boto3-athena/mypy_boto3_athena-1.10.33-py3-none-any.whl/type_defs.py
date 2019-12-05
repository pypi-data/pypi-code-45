"Main interface for athena service type defs"
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


ClientBatchGetNamedQueryResponseNamedQueriesTypeDef = TypedDict(
    "ClientBatchGetNamedQueryResponseNamedQueriesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Database": str,
        "QueryString": str,
        "NamedQueryId": str,
        "WorkGroup": str,
    },
    total=False,
)

ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef = TypedDict(
    "ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef",
    {"NamedQueryId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchGetNamedQueryResponseTypeDef = TypedDict(
    "ClientBatchGetNamedQueryResponseTypeDef",
    {
        "NamedQueries": List[ClientBatchGetNamedQueryResponseNamedQueriesTypeDef],
        "UnprocessedNamedQueryIds": List[
            ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef
        ],
    },
    total=False,
)

ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef = TypedDict(
    "ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef",
    {"Database": str},
    total=False,
)

ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": Literal["SSE_S3", "SSE_KMS", "CSE_KMS"], "KmsKey": str},
    total=False,
)

ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef = TypedDict(
    "ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)

ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef = TypedDict(
    "ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef",
    {
        "EngineExecutionTimeInMillis": int,
        "DataScannedInBytes": int,
        "DataManifestLocation": str,
        "TotalExecutionTimeInMillis": int,
        "QueryQueueTimeInMillis": int,
        "QueryPlanningTimeInMillis": int,
        "ServiceProcessingTimeInMillis": int,
    },
    total=False,
)

ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef = TypedDict(
    "ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef",
    {
        "State": Literal["QUEUED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"],
        "StateChangeReason": str,
        "SubmissionDateTime": datetime,
        "CompletionDateTime": datetime,
    },
    total=False,
)

ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef = TypedDict(
    "ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef",
    {
        "QueryExecutionId": str,
        "Query": str,
        "StatementType": Literal["DDL", "DML", "UTILITY"],
        "ResultConfiguration": ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef,
        "QueryExecutionContext": ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef,
        "Status": ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef,
        "Statistics": ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef,
        "WorkGroup": str,
    },
    total=False,
)

ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef = TypedDict(
    "ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef",
    {"QueryExecutionId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchGetQueryExecutionResponseTypeDef = TypedDict(
    "ClientBatchGetQueryExecutionResponseTypeDef",
    {
        "QueryExecutions": List[ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef],
        "UnprocessedQueryExecutionIds": List[
            ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef
        ],
    },
    total=False,
)

ClientCreateNamedQueryResponseTypeDef = TypedDict(
    "ClientCreateNamedQueryResponseTypeDef", {"NamedQueryId": str}, total=False
)

ClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": Literal["SSE_S3", "SSE_KMS", "CSE_KMS"], "KmsKey": str},
    total=False,
)

ClientCreateWorkGroupConfigurationResultConfigurationTypeDef = TypedDict(
    "ClientCreateWorkGroupConfigurationResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)

ClientCreateWorkGroupConfigurationTypeDef = TypedDict(
    "ClientCreateWorkGroupConfigurationTypeDef",
    {
        "ResultConfiguration": ClientCreateWorkGroupConfigurationResultConfigurationTypeDef,
        "EnforceWorkGroupConfiguration": bool,
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RequesterPaysEnabled": bool,
    },
    total=False,
)

ClientCreateWorkGroupTagsTypeDef = TypedDict(
    "ClientCreateWorkGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetNamedQueryResponseNamedQueryTypeDef = TypedDict(
    "ClientGetNamedQueryResponseNamedQueryTypeDef",
    {
        "Name": str,
        "Description": str,
        "Database": str,
        "QueryString": str,
        "NamedQueryId": str,
        "WorkGroup": str,
    },
    total=False,
)

ClientGetNamedQueryResponseTypeDef = TypedDict(
    "ClientGetNamedQueryResponseTypeDef",
    {"NamedQuery": ClientGetNamedQueryResponseNamedQueryTypeDef},
    total=False,
)

ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef = TypedDict(
    "ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef",
    {"Database": str},
    total=False,
)

ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": Literal["SSE_S3", "SSE_KMS", "CSE_KMS"], "KmsKey": str},
    total=False,
)

ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef = TypedDict(
    "ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)

ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef = TypedDict(
    "ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef",
    {
        "EngineExecutionTimeInMillis": int,
        "DataScannedInBytes": int,
        "DataManifestLocation": str,
        "TotalExecutionTimeInMillis": int,
        "QueryQueueTimeInMillis": int,
        "QueryPlanningTimeInMillis": int,
        "ServiceProcessingTimeInMillis": int,
    },
    total=False,
)

ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef = TypedDict(
    "ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef",
    {
        "State": Literal["QUEUED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"],
        "StateChangeReason": str,
        "SubmissionDateTime": datetime,
        "CompletionDateTime": datetime,
    },
    total=False,
)

ClientGetQueryExecutionResponseQueryExecutionTypeDef = TypedDict(
    "ClientGetQueryExecutionResponseQueryExecutionTypeDef",
    {
        "QueryExecutionId": str,
        "Query": str,
        "StatementType": Literal["DDL", "DML", "UTILITY"],
        "ResultConfiguration": ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef,
        "QueryExecutionContext": ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef,
        "Status": ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef,
        "Statistics": ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef,
        "WorkGroup": str,
    },
    total=False,
)

ClientGetQueryExecutionResponseTypeDef = TypedDict(
    "ClientGetQueryExecutionResponseTypeDef",
    {"QueryExecution": ClientGetQueryExecutionResponseQueryExecutionTypeDef},
    total=False,
)

ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef = TypedDict(
    "ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef",
    {
        "CatalogName": str,
        "SchemaName": str,
        "TableName": str,
        "Name": str,
        "Label": str,
        "Type": str,
        "Precision": int,
        "Scale": int,
        "Nullable": Literal["NOT_NULL", "NULLABLE", "UNKNOWN"],
        "CaseSensitive": bool,
    },
    total=False,
)

ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef = TypedDict(
    "ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef",
    {"ColumnInfo": List[ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef]},
    total=False,
)

ClientGetQueryResultsResponseResultSetRowsDataTypeDef = TypedDict(
    "ClientGetQueryResultsResponseResultSetRowsDataTypeDef", {"VarCharValue": str}, total=False
)

ClientGetQueryResultsResponseResultSetRowsTypeDef = TypedDict(
    "ClientGetQueryResultsResponseResultSetRowsTypeDef",
    {"Data": List[ClientGetQueryResultsResponseResultSetRowsDataTypeDef]},
    total=False,
)

ClientGetQueryResultsResponseResultSetTypeDef = TypedDict(
    "ClientGetQueryResultsResponseResultSetTypeDef",
    {
        "Rows": List[ClientGetQueryResultsResponseResultSetRowsTypeDef],
        "ResultSetMetadata": ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef,
    },
    total=False,
)

ClientGetQueryResultsResponseTypeDef = TypedDict(
    "ClientGetQueryResultsResponseTypeDef",
    {
        "UpdateCount": int,
        "ResultSet": ClientGetQueryResultsResponseResultSetTypeDef,
        "NextToken": str,
    },
    total=False,
)

ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": Literal["SSE_S3", "SSE_KMS", "CSE_KMS"], "KmsKey": str},
    total=False,
)

ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef = TypedDict(
    "ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)

ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef = TypedDict(
    "ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef",
    {
        "ResultConfiguration": ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef,
        "EnforceWorkGroupConfiguration": bool,
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RequesterPaysEnabled": bool,
    },
    total=False,
)

ClientGetWorkGroupResponseWorkGroupTypeDef = TypedDict(
    "ClientGetWorkGroupResponseWorkGroupTypeDef",
    {
        "Name": str,
        "State": Literal["ENABLED", "DISABLED"],
        "Configuration": ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef,
        "Description": str,
        "CreationTime": datetime,
    },
    total=False,
)

ClientGetWorkGroupResponseTypeDef = TypedDict(
    "ClientGetWorkGroupResponseTypeDef",
    {"WorkGroup": ClientGetWorkGroupResponseWorkGroupTypeDef},
    total=False,
)

ClientListNamedQueriesResponseTypeDef = TypedDict(
    "ClientListNamedQueriesResponseTypeDef",
    {"NamedQueryIds": List[str], "NextToken": str},
    total=False,
)

ClientListQueryExecutionsResponseTypeDef = TypedDict(
    "ClientListQueryExecutionsResponseTypeDef",
    {"QueryExecutionIds": List[str], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientListWorkGroupsResponseWorkGroupsTypeDef = TypedDict(
    "ClientListWorkGroupsResponseWorkGroupsTypeDef",
    {
        "Name": str,
        "State": Literal["ENABLED", "DISABLED"],
        "Description": str,
        "CreationTime": datetime,
    },
    total=False,
)

ClientListWorkGroupsResponseTypeDef = TypedDict(
    "ClientListWorkGroupsResponseTypeDef",
    {"WorkGroups": List[ClientListWorkGroupsResponseWorkGroupsTypeDef], "NextToken": str},
    total=False,
)

ClientStartQueryExecutionQueryExecutionContextTypeDef = TypedDict(
    "ClientStartQueryExecutionQueryExecutionContextTypeDef", {"Database": str}, total=False
)

ClientStartQueryExecutionResponseTypeDef = TypedDict(
    "ClientStartQueryExecutionResponseTypeDef", {"QueryExecutionId": str}, total=False
)

ClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": Literal["SSE_S3", "SSE_KMS", "CSE_KMS"], "KmsKey": str},
    total=False,
)

ClientStartQueryExecutionResultConfigurationTypeDef = TypedDict(
    "ClientStartQueryExecutionResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef = TypedDict(
    "ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef",
    {"EncryptionOption": Literal["SSE_S3", "SSE_KMS", "CSE_KMS"], "KmsKey": str},
    total=False,
)

ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef = TypedDict(
    "ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef",
    {
        "OutputLocation": str,
        "RemoveOutputLocation": bool,
        "EncryptionConfiguration": ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef,
        "RemoveEncryptionConfiguration": bool,
    },
    total=False,
)

ClientUpdateWorkGroupConfigurationUpdatesTypeDef = TypedDict(
    "ClientUpdateWorkGroupConfigurationUpdatesTypeDef",
    {
        "EnforceWorkGroupConfiguration": bool,
        "ResultConfigurationUpdates": ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef,
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RemoveBytesScannedCutoffPerQuery": bool,
        "RequesterPaysEnabled": bool,
    },
    total=False,
)

GetQueryResultsPaginatePaginationConfigTypeDef = TypedDict(
    "GetQueryResultsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef = TypedDict(
    "GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef",
    {
        "CatalogName": str,
        "SchemaName": str,
        "TableName": str,
        "Name": str,
        "Label": str,
        "Type": str,
        "Precision": int,
        "Scale": int,
        "Nullable": Literal["NOT_NULL", "NULLABLE", "UNKNOWN"],
        "CaseSensitive": bool,
    },
    total=False,
)

GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef = TypedDict(
    "GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef",
    {
        "ColumnInfo": List[
            GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef
        ]
    },
    total=False,
)

GetQueryResultsPaginateResponseResultSetRowsDataTypeDef = TypedDict(
    "GetQueryResultsPaginateResponseResultSetRowsDataTypeDef", {"VarCharValue": str}, total=False
)

GetQueryResultsPaginateResponseResultSetRowsTypeDef = TypedDict(
    "GetQueryResultsPaginateResponseResultSetRowsTypeDef",
    {"Data": List[GetQueryResultsPaginateResponseResultSetRowsDataTypeDef]},
    total=False,
)

GetQueryResultsPaginateResponseResultSetTypeDef = TypedDict(
    "GetQueryResultsPaginateResponseResultSetTypeDef",
    {
        "Rows": List[GetQueryResultsPaginateResponseResultSetRowsTypeDef],
        "ResultSetMetadata": GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef,
    },
    total=False,
)

GetQueryResultsPaginateResponseTypeDef = TypedDict(
    "GetQueryResultsPaginateResponseTypeDef",
    {"UpdateCount": int, "ResultSet": GetQueryResultsPaginateResponseResultSetTypeDef},
    total=False,
)

ListNamedQueriesPaginatePaginationConfigTypeDef = TypedDict(
    "ListNamedQueriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListNamedQueriesPaginateResponseTypeDef = TypedDict(
    "ListNamedQueriesPaginateResponseTypeDef", {"NamedQueryIds": List[str]}, total=False
)

ListQueryExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListQueryExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListQueryExecutionsPaginateResponseTypeDef = TypedDict(
    "ListQueryExecutionsPaginateResponseTypeDef", {"QueryExecutionIds": List[str]}, total=False
)
