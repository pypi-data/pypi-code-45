"Main interface for rds-data service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_rds_data.client as client_scope
from mypy_boto3_rds_data.type_defs import (
    ClientBatchExecuteStatementParameterSetsTypeDef,
    ClientBatchExecuteStatementResponseTypeDef,
    ClientBeginTransactionResponseTypeDef,
    ClientCommitTransactionResponseTypeDef,
    ClientExecuteSqlResponseTypeDef,
    ClientExecuteStatementParametersTypeDef,
    ClientExecuteStatementResponseTypeDef,
    ClientExecuteStatementResultSetOptionsTypeDef,
    ClientRollbackTransactionResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    """
    [RDSDataService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds-data.html#RDSDataService.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_execute_statement(
        self,
        resourceArn: str,
        secretArn: str,
        sql: str,
        database: str = None,
        parameterSets: List[List[ClientBatchExecuteStatementParameterSetsTypeDef]] = None,
        schema: str = None,
        transactionId: str = None,
    ) -> ClientBatchExecuteStatementResponseTypeDef:
        """
        [Client.batch_execute_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds-data.html#RDSDataService.Client.batch_execute_statement)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def begin_transaction(
        self, resourceArn: str, secretArn: str, database: str = None, schema: str = None
    ) -> ClientBeginTransactionResponseTypeDef:
        """
        [Client.begin_transaction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds-data.html#RDSDataService.Client.begin_transaction)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds-data.html#RDSDataService.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def commit_transaction(
        self, resourceArn: str, secretArn: str, transactionId: str
    ) -> ClientCommitTransactionResponseTypeDef:
        """
        [Client.commit_transaction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds-data.html#RDSDataService.Client.commit_transaction)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def execute_sql(
        self,
        awsSecretStoreArn: str,
        dbClusterOrInstanceArn: str,
        sqlStatements: str,
        database: str = None,
        schema: str = None,
    ) -> ClientExecuteSqlResponseTypeDef:
        """
        [Client.execute_sql documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds-data.html#RDSDataService.Client.execute_sql)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def execute_statement(
        self,
        resourceArn: str,
        secretArn: str,
        sql: str,
        continueAfterTimeout: bool = None,
        database: str = None,
        includeResultMetadata: bool = None,
        parameters: List[ClientExecuteStatementParametersTypeDef] = None,
        resultSetOptions: ClientExecuteStatementResultSetOptionsTypeDef = None,
        schema: str = None,
        transactionId: str = None,
    ) -> ClientExecuteStatementResponseTypeDef:
        """
        [Client.execute_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds-data.html#RDSDataService.Client.execute_statement)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds-data.html#RDSDataService.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def rollback_transaction(
        self, resourceArn: str, secretArn: str, transactionId: str
    ) -> ClientRollbackTransactionResponseTypeDef:
        """
        [Client.rollback_transaction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds-data.html#RDSDataService.Client.rollback_transaction)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableError: Boto3ClientError
    StatementTimeoutException: Boto3ClientError
