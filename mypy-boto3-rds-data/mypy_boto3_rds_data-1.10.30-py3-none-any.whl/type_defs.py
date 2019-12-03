"Main interface for rds-data service type defs"
from __future__ import annotations

from typing import Any, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchExecuteStatementParameterSetsvaluearrayValueTypeDef",
    "ClientBatchExecuteStatementParameterSetsvalueTypeDef",
    "ClientBatchExecuteStatementParameterSetsTypeDef",
    "ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef",
    "ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef",
    "ClientBatchExecuteStatementResponseupdateResultsTypeDef",
    "ClientBatchExecuteStatementResponseTypeDef",
    "ClientBeginTransactionResponseTypeDef",
    "ClientCommitTransactionResponseTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsTypeDef",
    "ClientExecuteSqlResponseTypeDef",
    "ClientExecuteStatementParametersvaluearrayValueTypeDef",
    "ClientExecuteStatementParametersvalueTypeDef",
    "ClientExecuteStatementParametersTypeDef",
    "ClientExecuteStatementResponsecolumnMetadataTypeDef",
    "ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef",
    "ClientExecuteStatementResponsegeneratedFieldsTypeDef",
    "ClientExecuteStatementResponserecordsarrayValueTypeDef",
    "ClientExecuteStatementResponserecordsTypeDef",
    "ClientExecuteStatementResponseTypeDef",
    "ClientExecuteStatementResultSetOptionsTypeDef",
    "ClientRollbackTransactionResponseTypeDef",
)


_ClientBatchExecuteStatementParameterSetsvaluearrayValueTypeDef = TypedDict(
    "_ClientBatchExecuteStatementParameterSetsvaluearrayValueTypeDef",
    {
        "arrayValues": List[Any],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)


class ClientBatchExecuteStatementParameterSetsvaluearrayValueTypeDef(
    _ClientBatchExecuteStatementParameterSetsvaluearrayValueTypeDef
):
    pass


_ClientBatchExecuteStatementParameterSetsvalueTypeDef = TypedDict(
    "_ClientBatchExecuteStatementParameterSetsvalueTypeDef",
    {
        "arrayValue": ClientBatchExecuteStatementParameterSetsvaluearrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)


class ClientBatchExecuteStatementParameterSetsvalueTypeDef(
    _ClientBatchExecuteStatementParameterSetsvalueTypeDef
):
    pass


_ClientBatchExecuteStatementParameterSetsTypeDef = TypedDict(
    "_ClientBatchExecuteStatementParameterSetsTypeDef",
    {
        "name": str,
        "typeHint": Literal["DATE", "DECIMAL", "TIME", "TIMESTAMP"],
        "value": ClientBatchExecuteStatementParameterSetsvalueTypeDef,
    },
    total=False,
)


class ClientBatchExecuteStatementParameterSetsTypeDef(
    _ClientBatchExecuteStatementParameterSetsTypeDef
):
    """
    - *(dict) --*

      A parameter used in a SQL statement.
      - **name** *(string) --*

        The name of the parameter.
    """


_ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef = TypedDict(
    "_ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef",
    {
        "arrayValues": List[Any],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)


class ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef(
    _ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef
):
    """
    - **arrayValue** *(dict) --*

      An array of values.
      - **arrayValues** *(list) --*

        An array of arrays.
        - *(dict) --*

          Contains an array.
    """


_ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef = TypedDict(
    "_ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef",
    {
        "arrayValue": ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)


class ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef(
    _ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef
):
    """
    - *(dict) --*

      Contains a value.
      - **arrayValue** *(dict) --*

        An array of values.
        - **arrayValues** *(list) --*

          An array of arrays.
          - *(dict) --*

            Contains an array.
    """


_ClientBatchExecuteStatementResponseupdateResultsTypeDef = TypedDict(
    "_ClientBatchExecuteStatementResponseupdateResultsTypeDef",
    {
        "generatedFields": List[
            ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef
        ]
    },
    total=False,
)


class ClientBatchExecuteStatementResponseupdateResultsTypeDef(
    _ClientBatchExecuteStatementResponseupdateResultsTypeDef
):
    """
    - *(dict) --*

      The response elements represent the results of an update.
      - **generatedFields** *(list) --*

        Values for fields generated during the request.
        - *(dict) --*

          Contains a value.
          - **arrayValue** *(dict) --*

            An array of values.
            - **arrayValues** *(list) --*

              An array of arrays.
              - *(dict) --*

                Contains an array.
    """


_ClientBatchExecuteStatementResponseTypeDef = TypedDict(
    "_ClientBatchExecuteStatementResponseTypeDef",
    {"updateResults": List[ClientBatchExecuteStatementResponseupdateResultsTypeDef]},
    total=False,
)


class ClientBatchExecuteStatementResponseTypeDef(_ClientBatchExecuteStatementResponseTypeDef):
    """
    - *(dict) --*

      The response elements represent the output of a SQL statement over an array of data.
      - **updateResults** *(list) --*

        The execution results of each batch entry.
        - *(dict) --*

          The response elements represent the results of an update.
          - **generatedFields** *(list) --*

            Values for fields generated during the request.
            - *(dict) --*

              Contains a value.
              - **arrayValue** *(dict) --*

                An array of values.
                - **arrayValues** *(list) --*

                  An array of arrays.
                  - *(dict) --*

                    Contains an array.
    """


_ClientBeginTransactionResponseTypeDef = TypedDict(
    "_ClientBeginTransactionResponseTypeDef", {"transactionId": str}, total=False
)


class ClientBeginTransactionResponseTypeDef(_ClientBeginTransactionResponseTypeDef):
    """
    - *(dict) --*

      The response elements represent the output of a request to start a SQL transaction.
      - **transactionId** *(string) --*

        The transaction ID of the transaction started by the call.
    """


_ClientCommitTransactionResponseTypeDef = TypedDict(
    "_ClientCommitTransactionResponseTypeDef", {"transactionStatus": str}, total=False
)


class ClientCommitTransactionResponseTypeDef(_ClientCommitTransactionResponseTypeDef):
    """
    - *(dict) --*

      The response elements represent the output of a commit transaction request.
      - **transactionStatus** *(string) --*

        The status of the commit operation.
    """


_ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef",
    {"attributes": List[Any]},
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef
):
    pass


_ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef",
    {
        "arrayValues": List[Any],
        "bigIntValue": int,
        "bitValue": bool,
        "blobValue": bytes,
        "doubleValue": float,
        "intValue": int,
        "isNull": bool,
        "realValue": Any,
        "stringValue": str,
        "structValue": ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef,
    },
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef
):
    pass


_ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef",
    {"values": List[ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef]},
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef
):
    pass


_ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef",
    {
        "arrayBaseColumnType": int,
        "isAutoIncrement": bool,
        "isCaseSensitive": bool,
        "isCurrency": bool,
        "isSigned": bool,
        "label": str,
        "name": str,
        "nullable": int,
        "precision": int,
        "scale": int,
        "schemaName": str,
        "tableName": str,
        "type": int,
        "typeName": str,
    },
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef
):
    pass


_ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef",
    {
        "columnCount": int,
        "columnMetadata": List[
            ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef
        ],
    },
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef
):
    pass


_ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef",
    {
        "records": List[ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef],
        "resultSetMetadata": ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef,
    },
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef
):
    pass


_ClientExecuteSqlResponsesqlStatementResultsTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsTypeDef",
    {
        "numberOfRecordsUpdated": int,
        "resultFrame": ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef,
    },
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsTypeDef
):
    """
    - *(dict) --*

      The result of a SQL statement.

        ``<important> <p>This data type is deprecated.</p> </important>``
    """


_ClientExecuteSqlResponseTypeDef = TypedDict(
    "_ClientExecuteSqlResponseTypeDef",
    {"sqlStatementResults": List[ClientExecuteSqlResponsesqlStatementResultsTypeDef]},
    total=False,
)


class ClientExecuteSqlResponseTypeDef(_ClientExecuteSqlResponseTypeDef):
    """
    - *(dict) --*

      The response elements represent the output of a request to run one or more SQL statements.
      - **sqlStatementResults** *(list) --*

        The results of the SQL statement or statements.
        - *(dict) --*

          The result of a SQL statement.

            ``<important> <p>This data type is deprecated.</p> </important>``
    """


_ClientExecuteStatementParametersvaluearrayValueTypeDef = TypedDict(
    "_ClientExecuteStatementParametersvaluearrayValueTypeDef",
    {
        "arrayValues": List[Any],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)


class ClientExecuteStatementParametersvaluearrayValueTypeDef(
    _ClientExecuteStatementParametersvaluearrayValueTypeDef
):
    pass


_ClientExecuteStatementParametersvalueTypeDef = TypedDict(
    "_ClientExecuteStatementParametersvalueTypeDef",
    {
        "arrayValue": ClientExecuteStatementParametersvaluearrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)


class ClientExecuteStatementParametersvalueTypeDef(_ClientExecuteStatementParametersvalueTypeDef):
    pass


_ClientExecuteStatementParametersTypeDef = TypedDict(
    "_ClientExecuteStatementParametersTypeDef",
    {
        "name": str,
        "typeHint": Literal["DATE", "DECIMAL", "TIME", "TIMESTAMP"],
        "value": ClientExecuteStatementParametersvalueTypeDef,
    },
    total=False,
)


class ClientExecuteStatementParametersTypeDef(_ClientExecuteStatementParametersTypeDef):
    """
    - *(dict) --*

      A parameter used in a SQL statement.
      - **name** *(string) --*

        The name of the parameter.
    """


_ClientExecuteStatementResponsecolumnMetadataTypeDef = TypedDict(
    "_ClientExecuteStatementResponsecolumnMetadataTypeDef",
    {
        "arrayBaseColumnType": int,
        "isAutoIncrement": bool,
        "isCaseSensitive": bool,
        "isCurrency": bool,
        "isSigned": bool,
        "label": str,
        "name": str,
        "nullable": int,
        "precision": int,
        "scale": int,
        "schemaName": str,
        "tableName": str,
        "type": int,
        "typeName": str,
    },
    total=False,
)


class ClientExecuteStatementResponsecolumnMetadataTypeDef(
    _ClientExecuteStatementResponsecolumnMetadataTypeDef
):
    """
    - *(dict) --*

      Contains the metadata for a column.
      - **arrayBaseColumnType** *(integer) --*

        The type of the column.
    """


_ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef = TypedDict(
    "_ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef",
    {
        "arrayValues": List[Any],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)


class ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef(
    _ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef
):
    pass


_ClientExecuteStatementResponsegeneratedFieldsTypeDef = TypedDict(
    "_ClientExecuteStatementResponsegeneratedFieldsTypeDef",
    {
        "arrayValue": ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)


class ClientExecuteStatementResponsegeneratedFieldsTypeDef(
    _ClientExecuteStatementResponsegeneratedFieldsTypeDef
):
    pass


_ClientExecuteStatementResponserecordsarrayValueTypeDef = TypedDict(
    "_ClientExecuteStatementResponserecordsarrayValueTypeDef",
    {
        "arrayValues": List[Any],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)


class ClientExecuteStatementResponserecordsarrayValueTypeDef(
    _ClientExecuteStatementResponserecordsarrayValueTypeDef
):
    pass


_ClientExecuteStatementResponserecordsTypeDef = TypedDict(
    "_ClientExecuteStatementResponserecordsTypeDef",
    {
        "arrayValue": ClientExecuteStatementResponserecordsarrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)


class ClientExecuteStatementResponserecordsTypeDef(_ClientExecuteStatementResponserecordsTypeDef):
    pass


_ClientExecuteStatementResponseTypeDef = TypedDict(
    "_ClientExecuteStatementResponseTypeDef",
    {
        "columnMetadata": List[ClientExecuteStatementResponsecolumnMetadataTypeDef],
        "generatedFields": List[ClientExecuteStatementResponsegeneratedFieldsTypeDef],
        "numberOfRecordsUpdated": int,
        "records": List[List[ClientExecuteStatementResponserecordsTypeDef]],
    },
    total=False,
)


class ClientExecuteStatementResponseTypeDef(_ClientExecuteStatementResponseTypeDef):
    """
    - *(dict) --*

      The response elements represent the output of a request to run a SQL statement against a
      database.
      - **columnMetadata** *(list) --*

        Metadata for the columns included in the results.
        - *(dict) --*

          Contains the metadata for a column.
          - **arrayBaseColumnType** *(integer) --*

            The type of the column.
    """


_ClientExecuteStatementResultSetOptionsTypeDef = TypedDict(
    "_ClientExecuteStatementResultSetOptionsTypeDef",
    {"decimalReturnType": Literal["DOUBLE_OR_LONG", "STRING"]},
    total=False,
)


class ClientExecuteStatementResultSetOptionsTypeDef(_ClientExecuteStatementResultSetOptionsTypeDef):
    """
    Options that control how the result set is returned.
    - **decimalReturnType** *(string) --*

      A value that indicates how a field of ``DECIMAL`` type is represented in the response. The
      value of ``STRING`` , the default, specifies that it is converted to a String value. The value
      of ``DOUBLE_OR_LONG`` specifies that it is converted to a Long value if its scale is 0, or to
      a Double value otherwise.
      .. warning::

        Conversion to Double or Long can result in roundoff errors due to precision loss. We
        recommend converting to String, especially when working with currency values.
    """


_ClientRollbackTransactionResponseTypeDef = TypedDict(
    "_ClientRollbackTransactionResponseTypeDef", {"transactionStatus": str}, total=False
)


class ClientRollbackTransactionResponseTypeDef(_ClientRollbackTransactionResponseTypeDef):
    """
    - *(dict) --*

      The response elements represent the output of a request to perform a rollback of a
      transaction.
      - **transactionStatus** *(string) --*

        The status of the rollback operation.
    """
