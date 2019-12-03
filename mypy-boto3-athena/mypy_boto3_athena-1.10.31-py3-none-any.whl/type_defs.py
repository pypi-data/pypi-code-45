"Main interface for athena service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchGetNamedQueryResponseNamedQueriesTypeDef",
    "ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef",
    "ClientBatchGetNamedQueryResponseTypeDef",
    "ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef",
    "ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef",
    "ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef",
    "ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef",
    "ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef",
    "ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef",
    "ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef",
    "ClientBatchGetQueryExecutionResponseTypeDef",
    "ClientCreateNamedQueryResponseTypeDef",
    "ClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateWorkGroupConfigurationResultConfigurationTypeDef",
    "ClientCreateWorkGroupConfigurationTypeDef",
    "ClientCreateWorkGroupTagsTypeDef",
    "ClientGetNamedQueryResponseNamedQueryTypeDef",
    "ClientGetNamedQueryResponseTypeDef",
    "ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef",
    "ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef",
    "ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef",
    "ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef",
    "ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef",
    "ClientGetQueryExecutionResponseQueryExecutionTypeDef",
    "ClientGetQueryExecutionResponseTypeDef",
    "ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef",
    "ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef",
    "ClientGetQueryResultsResponseResultSetRowsDataTypeDef",
    "ClientGetQueryResultsResponseResultSetRowsTypeDef",
    "ClientGetQueryResultsResponseResultSetTypeDef",
    "ClientGetQueryResultsResponseTypeDef",
    "ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef",
    "ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef",
    "ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef",
    "ClientGetWorkGroupResponseWorkGroupTypeDef",
    "ClientGetWorkGroupResponseTypeDef",
    "ClientListNamedQueriesResponseTypeDef",
    "ClientListQueryExecutionsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListWorkGroupsResponseWorkGroupsTypeDef",
    "ClientListWorkGroupsResponseTypeDef",
    "ClientStartQueryExecutionQueryExecutionContextTypeDef",
    "ClientStartQueryExecutionResponseTypeDef",
    "ClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef",
    "ClientStartQueryExecutionResultConfigurationTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef",
    "ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef",
    "ClientUpdateWorkGroupConfigurationUpdatesTypeDef",
    "GetQueryResultsPaginatePaginationConfigTypeDef",
    "GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef",
    "GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef",
    "GetQueryResultsPaginateResponseResultSetRowsDataTypeDef",
    "GetQueryResultsPaginateResponseResultSetRowsTypeDef",
    "GetQueryResultsPaginateResponseResultSetTypeDef",
    "GetQueryResultsPaginateResponseTypeDef",
    "ListNamedQueriesPaginatePaginationConfigTypeDef",
    "ListNamedQueriesPaginateResponseTypeDef",
    "ListQueryExecutionsPaginatePaginationConfigTypeDef",
    "ListQueryExecutionsPaginateResponseTypeDef",
)


_ClientBatchGetNamedQueryResponseNamedQueriesTypeDef = TypedDict(
    "_ClientBatchGetNamedQueryResponseNamedQueriesTypeDef",
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


class ClientBatchGetNamedQueryResponseNamedQueriesTypeDef(
    _ClientBatchGetNamedQueryResponseNamedQueriesTypeDef
):
    """
    - *(dict) --*

      A query, where ``QueryString`` is the list of SQL query statements that comprise the query.
      - **Name** *(string) --*

        The query name.
    """


_ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef = TypedDict(
    "_ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef",
    {"NamedQueryId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef(
    _ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef
):
    pass


_ClientBatchGetNamedQueryResponseTypeDef = TypedDict(
    "_ClientBatchGetNamedQueryResponseTypeDef",
    {
        "NamedQueries": List[ClientBatchGetNamedQueryResponseNamedQueriesTypeDef],
        "UnprocessedNamedQueryIds": List[
            ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetNamedQueryResponseTypeDef(_ClientBatchGetNamedQueryResponseTypeDef):
    """
    - *(dict) --*

      - **NamedQueries** *(list) --*

        Information about the named query IDs submitted.
        - *(dict) --*

          A query, where ``QueryString`` is the list of SQL query statements that comprise the
          query.
          - **Name** *(string) --*

            The query name.
    """


_ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef",
    {"Database": str},
    total=False,
)


class ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef(
    _ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef
):
    pass


_ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": Literal["SSE_S3", "SSE_KMS", "CSE_KMS"], "KmsKey": str},
    total=False,
)


class ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef(
    _ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef
):
    pass


_ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef(
    _ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef
):
    pass


_ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef",
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


class ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef(
    _ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef
):
    pass


_ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef",
    {
        "State": Literal["QUEUED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"],
        "StateChangeReason": str,
        "SubmissionDateTime": datetime,
        "CompletionDateTime": datetime,
    },
    total=False,
)


class ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef(
    _ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef
):
    pass


_ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef",
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


class ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef(
    _ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef
):
    """
    - *(dict) --*

      Information about a single instance of a query execution.
      - **QueryExecutionId** *(string) --*

        The unique identifier for each query execution.
    """


_ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef",
    {"QueryExecutionId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef(
    _ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef
):
    pass


_ClientBatchGetQueryExecutionResponseTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseTypeDef",
    {
        "QueryExecutions": List[ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef],
        "UnprocessedQueryExecutionIds": List[
            ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetQueryExecutionResponseTypeDef(_ClientBatchGetQueryExecutionResponseTypeDef):
    """
    - *(dict) --*

      - **QueryExecutions** *(list) --*

        Information about a query execution.
        - *(dict) --*

          Information about a single instance of a query execution.
          - **QueryExecutionId** *(string) --*

            The unique identifier for each query execution.
    """


_ClientCreateNamedQueryResponseTypeDef = TypedDict(
    "_ClientCreateNamedQueryResponseTypeDef", {"NamedQueryId": str}, total=False
)


class ClientCreateNamedQueryResponseTypeDef(_ClientCreateNamedQueryResponseTypeDef):
    """
    - *(dict) --*

      - **NamedQueryId** *(string) --*

        The unique ID of the query.
    """


_ClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": Literal["SSE_S3", "SSE_KMS", "CSE_KMS"], "KmsKey": str},
    total=False,
)


class ClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef(
    _ClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef
):
    pass


_ClientCreateWorkGroupConfigurationResultConfigurationTypeDef = TypedDict(
    "_ClientCreateWorkGroupConfigurationResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateWorkGroupConfigurationResultConfigurationTypeDef(
    _ClientCreateWorkGroupConfigurationResultConfigurationTypeDef
):
    """
    - **ResultConfiguration** *(dict) --*

      The configuration for the workgroup, which includes the location in Amazon S3 where query
      results are stored and the encryption option, if any, used for query results. To run the
      query, you must specify the query results location using one of the ways: either in the
      workgroup using this setting, or for individual queries (client-side), using
      ResultConfiguration$OutputLocation . If none of them is set, Athena issues an error that no
      output location is provided. For more information, see `Query Results
      <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ .
      - **OutputLocation** *(string) --*

        The location in Amazon S3 where your query results are stored, such as
        ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
        location using one of the ways: either for individual queries using either this setting
        (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is set,
        Athena issues an error that no output location is provided. For more information, see `Query
        Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If workgroup
        settings override client-side settings, then the query uses the settings specified for the
        workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .
    """


_ClientCreateWorkGroupConfigurationTypeDef = TypedDict(
    "_ClientCreateWorkGroupConfigurationTypeDef",
    {
        "ResultConfiguration": ClientCreateWorkGroupConfigurationResultConfigurationTypeDef,
        "EnforceWorkGroupConfiguration": bool,
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RequesterPaysEnabled": bool,
    },
    total=False,
)


class ClientCreateWorkGroupConfigurationTypeDef(_ClientCreateWorkGroupConfigurationTypeDef):
    """
    The configuration for the workgroup, which includes the location in Amazon S3 where query
    results are stored, the encryption configuration, if any, used for encrypting query results,
    whether the Amazon CloudWatch Metrics are enabled for the workgroup, the limit for the amount of
    bytes scanned (cutoff) per query, if it is specified, and whether workgroup's settings
    (specified with EnforceWorkGroupConfiguration) in the WorkGroupConfiguration override
    client-side settings. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .
    - **ResultConfiguration** *(dict) --*

      The configuration for the workgroup, which includes the location in Amazon S3 where query
      results are stored and the encryption option, if any, used for query results. To run the
      query, you must specify the query results location using one of the ways: either in the
      workgroup using this setting, or for individual queries (client-side), using
      ResultConfiguration$OutputLocation . If none of them is set, Athena issues an error that no
      output location is provided. For more information, see `Query Results
      <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ .
      - **OutputLocation** *(string) --*

        The location in Amazon S3 where your query results are stored, such as
        ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
        location using one of the ways: either for individual queries using either this setting
        (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is set,
        Athena issues an error that no output location is provided. For more information, see `Query
        Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If workgroup
        settings override client-side settings, then the query uses the settings specified for the
        workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .
    """


_ClientCreateWorkGroupTagsTypeDef = TypedDict(
    "_ClientCreateWorkGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateWorkGroupTagsTypeDef(_ClientCreateWorkGroupTagsTypeDef):
    """
    - *(dict) --*

      A tag that you can add to a resource. A tag is a label that you assign to an AWS Athena
      resource (a workgroup). Each tag consists of a key and an optional value, both of which you
      define. Tags enable you to categorize workgroups in Athena, for example, by purpose, owner, or
      environment. Use a consistent set of tag keys to make it easier to search and filter
      workgroups in your account. The maximum tag key length is 128 Unicode characters in UTF-8. The
      maximum tag value length is 256 Unicode characters in UTF-8. You can use letters and numbers
      representable in UTF-8, and the following characters: + - =
           . _ : / @. Tag keys and values are
      case-sensitive. Tag keys must be unique per resource.
      - **Key** *(string) --*

        A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use
        letters and numbers representable in UTF-8, and the following characters: + - =
             . _ : / @.
        Tag keys are case-sensitive and must be unique per resource.
    """


_ClientGetNamedQueryResponseNamedQueryTypeDef = TypedDict(
    "_ClientGetNamedQueryResponseNamedQueryTypeDef",
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


class ClientGetNamedQueryResponseNamedQueryTypeDef(_ClientGetNamedQueryResponseNamedQueryTypeDef):
    """
    - **NamedQuery** *(dict) --*

      Information about the query.
      - **Name** *(string) --*

        The query name.
    """


_ClientGetNamedQueryResponseTypeDef = TypedDict(
    "_ClientGetNamedQueryResponseTypeDef",
    {"NamedQuery": ClientGetNamedQueryResponseNamedQueryTypeDef},
    total=False,
)


class ClientGetNamedQueryResponseTypeDef(_ClientGetNamedQueryResponseTypeDef):
    """
    - *(dict) --*

      - **NamedQuery** *(dict) --*

        Information about the query.
        - **Name** *(string) --*

          The query name.
    """


_ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef",
    {"Database": str},
    total=False,
)


class ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef(
    _ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef
):
    pass


_ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": Literal["SSE_S3", "SSE_KMS", "CSE_KMS"], "KmsKey": str},
    total=False,
)


class ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef(
    _ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef
):
    pass


_ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef(
    _ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef
):
    pass


_ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef",
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


class ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef(
    _ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef
):
    pass


_ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef",
    {
        "State": Literal["QUEUED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"],
        "StateChangeReason": str,
        "SubmissionDateTime": datetime,
        "CompletionDateTime": datetime,
    },
    total=False,
)


class ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef(
    _ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef
):
    pass


_ClientGetQueryExecutionResponseQueryExecutionTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseQueryExecutionTypeDef",
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


class ClientGetQueryExecutionResponseQueryExecutionTypeDef(
    _ClientGetQueryExecutionResponseQueryExecutionTypeDef
):
    """
    - **QueryExecution** *(dict) --*

      Information about the query execution.
      - **QueryExecutionId** *(string) --*

        The unique identifier for each query execution.
    """


_ClientGetQueryExecutionResponseTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseTypeDef",
    {"QueryExecution": ClientGetQueryExecutionResponseQueryExecutionTypeDef},
    total=False,
)


class ClientGetQueryExecutionResponseTypeDef(_ClientGetQueryExecutionResponseTypeDef):
    """
    - *(dict) --*

      - **QueryExecution** *(dict) --*

        Information about the query execution.
        - **QueryExecutionId** *(string) --*

          The unique identifier for each query execution.
    """


_ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef",
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


class ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef(
    _ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef
):
    pass


_ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef",
    {"ColumnInfo": List[ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef]},
    total=False,
)


class ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef(
    _ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef
):
    pass


_ClientGetQueryResultsResponseResultSetRowsDataTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseResultSetRowsDataTypeDef", {"VarCharValue": str}, total=False
)


class ClientGetQueryResultsResponseResultSetRowsDataTypeDef(
    _ClientGetQueryResultsResponseResultSetRowsDataTypeDef
):
    pass


_ClientGetQueryResultsResponseResultSetRowsTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseResultSetRowsTypeDef",
    {"Data": List[ClientGetQueryResultsResponseResultSetRowsDataTypeDef]},
    total=False,
)


class ClientGetQueryResultsResponseResultSetRowsTypeDef(
    _ClientGetQueryResultsResponseResultSetRowsTypeDef
):
    pass


_ClientGetQueryResultsResponseResultSetTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseResultSetTypeDef",
    {
        "Rows": List[ClientGetQueryResultsResponseResultSetRowsTypeDef],
        "ResultSetMetadata": ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef,
    },
    total=False,
)


class ClientGetQueryResultsResponseResultSetTypeDef(_ClientGetQueryResultsResponseResultSetTypeDef):
    pass


_ClientGetQueryResultsResponseTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseTypeDef",
    {
        "UpdateCount": int,
        "ResultSet": ClientGetQueryResultsResponseResultSetTypeDef,
        "NextToken": str,
    },
    total=False,
)


class ClientGetQueryResultsResponseTypeDef(_ClientGetQueryResultsResponseTypeDef):
    """
    - *(dict) --*

      - **UpdateCount** *(integer) --*

        The number of rows inserted with a CREATE TABLE AS SELECT statement.
    """


_ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": Literal["SSE_S3", "SSE_KMS", "CSE_KMS"], "KmsKey": str},
    total=False,
)


class ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef(
    _ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef
):
    pass


_ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef = TypedDict(
    "_ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef(
    _ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef
):
    pass


_ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef = TypedDict(
    "_ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef",
    {
        "ResultConfiguration": ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef,
        "EnforceWorkGroupConfiguration": bool,
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RequesterPaysEnabled": bool,
    },
    total=False,
)


class ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef(
    _ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef
):
    pass


_ClientGetWorkGroupResponseWorkGroupTypeDef = TypedDict(
    "_ClientGetWorkGroupResponseWorkGroupTypeDef",
    {
        "Name": str,
        "State": Literal["ENABLED", "DISABLED"],
        "Configuration": ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef,
        "Description": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientGetWorkGroupResponseWorkGroupTypeDef(_ClientGetWorkGroupResponseWorkGroupTypeDef):
    """
    - **WorkGroup** *(dict) --*

      Information about the workgroup.
      - **Name** *(string) --*

        The workgroup name.
    """


_ClientGetWorkGroupResponseTypeDef = TypedDict(
    "_ClientGetWorkGroupResponseTypeDef",
    {"WorkGroup": ClientGetWorkGroupResponseWorkGroupTypeDef},
    total=False,
)


class ClientGetWorkGroupResponseTypeDef(_ClientGetWorkGroupResponseTypeDef):
    """
    - *(dict) --*

      - **WorkGroup** *(dict) --*

        Information about the workgroup.
        - **Name** *(string) --*

          The workgroup name.
    """


_ClientListNamedQueriesResponseTypeDef = TypedDict(
    "_ClientListNamedQueriesResponseTypeDef",
    {"NamedQueryIds": List[str], "NextToken": str},
    total=False,
)


class ClientListNamedQueriesResponseTypeDef(_ClientListNamedQueriesResponseTypeDef):
    """
    - *(dict) --*

      - **NamedQueryIds** *(list) --*

        The list of unique query IDs.
        - *(string) --*
    """


_ClientListQueryExecutionsResponseTypeDef = TypedDict(
    "_ClientListQueryExecutionsResponseTypeDef",
    {"QueryExecutionIds": List[str], "NextToken": str},
    total=False,
)


class ClientListQueryExecutionsResponseTypeDef(_ClientListQueryExecutionsResponseTypeDef):
    """
    - *(dict) --*

      - **QueryExecutionIds** *(list) --*

        The unique IDs of each query execution as an array of strings.
        - *(string) --*
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      A tag that you can add to a resource. A tag is a label that you assign to an AWS Athena
      resource (a workgroup). Each tag consists of a key and an optional value, both of which you
      define. Tags enable you to categorize workgroups in Athena, for example, by purpose, owner, or
      environment. Use a consistent set of tag keys to make it easier to search and filter
      workgroups in your account. The maximum tag key length is 128 Unicode characters in UTF-8. The
      maximum tag value length is 256 Unicode characters in UTF-8. You can use letters and numbers
      representable in UTF-8, and the following characters: + - =
           . _ : / @. Tag keys and values are
      case-sensitive. Tag keys must be unique per resource.
      - **Key** *(string) --*

        A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use
        letters and numbers representable in UTF-8, and the following characters: + - =
             . _ : / @.
        Tag keys are case-sensitive and must be unique per resource.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The list of tags associated with this workgroup.
        - *(dict) --*

          A tag that you can add to a resource. A tag is a label that you assign to an AWS Athena
          resource (a workgroup). Each tag consists of a key and an optional value, both of which
          you define. Tags enable you to categorize workgroups in Athena, for example, by purpose,
          owner, or environment. Use a consistent set of tag keys to make it easier to search and
          filter workgroups in your account. The maximum tag key length is 128 Unicode characters in
          UTF-8. The maximum tag value length is 256 Unicode characters in UTF-8. You can use
          letters and numbers representable in UTF-8, and the following characters: + - =
               . _ : / @.
          Tag keys and values are case-sensitive. Tag keys must be unique per resource.
          - **Key** *(string) --*

            A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use
            letters and numbers representable in UTF-8, and the following characters: + - =
                 . _ : /
            @. Tag keys are case-sensitive and must be unique per resource.
    """


_ClientListWorkGroupsResponseWorkGroupsTypeDef = TypedDict(
    "_ClientListWorkGroupsResponseWorkGroupsTypeDef",
    {
        "Name": str,
        "State": Literal["ENABLED", "DISABLED"],
        "Description": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientListWorkGroupsResponseWorkGroupsTypeDef(_ClientListWorkGroupsResponseWorkGroupsTypeDef):
    """
    - *(dict) --*

      The summary information for the workgroup, which includes its name, state, description, and
      the date and time it was created.
      - **Name** *(string) --*

        The name of the workgroup.
    """


_ClientListWorkGroupsResponseTypeDef = TypedDict(
    "_ClientListWorkGroupsResponseTypeDef",
    {"WorkGroups": List[ClientListWorkGroupsResponseWorkGroupsTypeDef], "NextToken": str},
    total=False,
)


class ClientListWorkGroupsResponseTypeDef(_ClientListWorkGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **WorkGroups** *(list) --*

        The list of workgroups, including their names, descriptions, creation times, and states.
        - *(dict) --*

          The summary information for the workgroup, which includes its name, state, description,
          and the date and time it was created.
          - **Name** *(string) --*

            The name of the workgroup.
    """


_ClientStartQueryExecutionQueryExecutionContextTypeDef = TypedDict(
    "_ClientStartQueryExecutionQueryExecutionContextTypeDef", {"Database": str}, total=False
)


class ClientStartQueryExecutionQueryExecutionContextTypeDef(
    _ClientStartQueryExecutionQueryExecutionContextTypeDef
):
    """
    The database within which the query executes.
    - **Database** *(string) --*

      The name of the database.
    """


_ClientStartQueryExecutionResponseTypeDef = TypedDict(
    "_ClientStartQueryExecutionResponseTypeDef", {"QueryExecutionId": str}, total=False
)


class ClientStartQueryExecutionResponseTypeDef(_ClientStartQueryExecutionResponseTypeDef):
    """
    - *(dict) --*

      - **QueryExecutionId** *(string) --*

        The unique ID of the query that ran as a result of this request.
    """


_ClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": Literal["SSE_S3", "SSE_KMS", "CSE_KMS"], "KmsKey": str},
    total=False,
)


class ClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef(
    _ClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef
):
    pass


_ClientStartQueryExecutionResultConfigurationTypeDef = TypedDict(
    "_ClientStartQueryExecutionResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientStartQueryExecutionResultConfigurationTypeDef(
    _ClientStartQueryExecutionResultConfigurationTypeDef
):
    """
    Specifies information about where and how to save the results of the query execution. If the
    query runs in a workgroup, then workgroup's settings may override query settings. This affects
    the query results location. The workgroup settings override is specified in
    EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See
    WorkGroupConfiguration$EnforceWorkGroupConfiguration .
    - **OutputLocation** *(string) --*

      The location in Amazon S3 where your query results are stored, such as
      ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results location
      using one of the ways: either for individual queries using either this setting (client-side),
      or in the workgroup, using  WorkGroupConfiguration . If none of them is set, Athena issues an
      error that no output location is provided. For more information, see `Query Results
      <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If workgroup settings
      override client-side settings, then the query uses the settings specified for the workgroup.
      See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      A tag that you can add to a resource. A tag is a label that you assign to an AWS Athena
      resource (a workgroup). Each tag consists of a key and an optional value, both of which you
      define. Tags enable you to categorize workgroups in Athena, for example, by purpose, owner, or
      environment. Use a consistent set of tag keys to make it easier to search and filter
      workgroups in your account. The maximum tag key length is 128 Unicode characters in UTF-8. The
      maximum tag value length is 256 Unicode characters in UTF-8. You can use letters and numbers
      representable in UTF-8, and the following characters: + - =
           . _ : / @. Tag keys and values are
      case-sensitive. Tag keys must be unique per resource.
      - **Key** *(string) --*

        A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use
        letters and numbers representable in UTF-8, and the following characters: + - =
             . _ : / @.
        Tag keys are case-sensitive and must be unique per resource.
    """


_ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef = TypedDict(
    "_ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef",
    {"EncryptionOption": Literal["SSE_S3", "SSE_KMS", "CSE_KMS"], "KmsKey": str},
    total=False,
)


class ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef(
    _ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef
):
    pass


_ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef = TypedDict(
    "_ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef",
    {
        "OutputLocation": str,
        "RemoveOutputLocation": bool,
        "EncryptionConfiguration": ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef,
        "RemoveEncryptionConfiguration": bool,
    },
    total=False,
)


class ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef(
    _ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef
):
    pass


_ClientUpdateWorkGroupConfigurationUpdatesTypeDef = TypedDict(
    "_ClientUpdateWorkGroupConfigurationUpdatesTypeDef",
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


class ClientUpdateWorkGroupConfigurationUpdatesTypeDef(
    _ClientUpdateWorkGroupConfigurationUpdatesTypeDef
):
    """
    The workgroup configuration that will be updated for the given workgroup.
    - **EnforceWorkGroupConfiguration** *(boolean) --*

      If set to "true", the settings for the workgroup override client-side settings. If set to
      "false" client-side settings are used. For more information, see `Workgroup Settings Override
      Client-Side Settings
      <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .
    """


_GetQueryResultsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetQueryResultsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetQueryResultsPaginatePaginationConfigTypeDef(
    _GetQueryResultsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef = TypedDict(
    "_GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef",
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


class GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef(
    _GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef
):
    pass


_GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef = TypedDict(
    "_GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef",
    {
        "ColumnInfo": List[
            GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef
        ]
    },
    total=False,
)


class GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef(
    _GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef
):
    pass


_GetQueryResultsPaginateResponseResultSetRowsDataTypeDef = TypedDict(
    "_GetQueryResultsPaginateResponseResultSetRowsDataTypeDef", {"VarCharValue": str}, total=False
)


class GetQueryResultsPaginateResponseResultSetRowsDataTypeDef(
    _GetQueryResultsPaginateResponseResultSetRowsDataTypeDef
):
    pass


_GetQueryResultsPaginateResponseResultSetRowsTypeDef = TypedDict(
    "_GetQueryResultsPaginateResponseResultSetRowsTypeDef",
    {"Data": List[GetQueryResultsPaginateResponseResultSetRowsDataTypeDef]},
    total=False,
)


class GetQueryResultsPaginateResponseResultSetRowsTypeDef(
    _GetQueryResultsPaginateResponseResultSetRowsTypeDef
):
    pass


_GetQueryResultsPaginateResponseResultSetTypeDef = TypedDict(
    "_GetQueryResultsPaginateResponseResultSetTypeDef",
    {
        "Rows": List[GetQueryResultsPaginateResponseResultSetRowsTypeDef],
        "ResultSetMetadata": GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef,
    },
    total=False,
)


class GetQueryResultsPaginateResponseResultSetTypeDef(
    _GetQueryResultsPaginateResponseResultSetTypeDef
):
    pass


_GetQueryResultsPaginateResponseTypeDef = TypedDict(
    "_GetQueryResultsPaginateResponseTypeDef",
    {"UpdateCount": int, "ResultSet": GetQueryResultsPaginateResponseResultSetTypeDef},
    total=False,
)


class GetQueryResultsPaginateResponseTypeDef(_GetQueryResultsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **UpdateCount** *(integer) --*

        The number of rows inserted with a CREATE TABLE AS SELECT statement.
    """


_ListNamedQueriesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListNamedQueriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListNamedQueriesPaginatePaginationConfigTypeDef(
    _ListNamedQueriesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListNamedQueriesPaginateResponseTypeDef = TypedDict(
    "_ListNamedQueriesPaginateResponseTypeDef", {"NamedQueryIds": List[str]}, total=False
)


class ListNamedQueriesPaginateResponseTypeDef(_ListNamedQueriesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **NamedQueryIds** *(list) --*

        The list of unique query IDs.
        - *(string) --*
    """


_ListQueryExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListQueryExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListQueryExecutionsPaginatePaginationConfigTypeDef(
    _ListQueryExecutionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListQueryExecutionsPaginateResponseTypeDef = TypedDict(
    "_ListQueryExecutionsPaginateResponseTypeDef", {"QueryExecutionIds": List[str]}, total=False
)


class ListQueryExecutionsPaginateResponseTypeDef(_ListQueryExecutionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **QueryExecutionIds** *(list) --*

        The unique IDs of each query execution as an array of strings.
        - *(string) --*
    """
