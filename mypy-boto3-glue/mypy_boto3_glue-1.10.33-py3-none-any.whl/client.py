"Main interface for glue service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_glue.client as client_scope

# pylint: disable=import-self
import mypy_boto3_glue.paginator as paginator_scope
from mypy_boto3_glue.type_defs import (
    ClientBatchCreatePartitionPartitionInputListTypeDef,
    ClientBatchCreatePartitionResponseTypeDef,
    ClientBatchDeleteConnectionResponseTypeDef,
    ClientBatchDeletePartitionPartitionsToDeleteTypeDef,
    ClientBatchDeletePartitionResponseTypeDef,
    ClientBatchDeleteTableResponseTypeDef,
    ClientBatchDeleteTableVersionResponseTypeDef,
    ClientBatchGetCrawlersResponseTypeDef,
    ClientBatchGetDevEndpointsResponseTypeDef,
    ClientBatchGetJobsResponseTypeDef,
    ClientBatchGetPartitionPartitionsToGetTypeDef,
    ClientBatchGetPartitionResponseTypeDef,
    ClientBatchGetTriggersResponseTypeDef,
    ClientBatchGetWorkflowsResponseTypeDef,
    ClientBatchStopJobRunResponseTypeDef,
    ClientCancelMlTaskRunResponseTypeDef,
    ClientCreateClassifierCsvClassifierTypeDef,
    ClientCreateClassifierGrokClassifierTypeDef,
    ClientCreateClassifierJsonClassifierTypeDef,
    ClientCreateClassifierXMLClassifierTypeDef,
    ClientCreateConnectionConnectionInputTypeDef,
    ClientCreateCrawlerSchemaChangePolicyTypeDef,
    ClientCreateCrawlerTargetsTypeDef,
    ClientCreateDatabaseDatabaseInputTypeDef,
    ClientCreateDevEndpointResponseTypeDef,
    ClientCreateJobCommandTypeDef,
    ClientCreateJobConnectionsTypeDef,
    ClientCreateJobExecutionPropertyTypeDef,
    ClientCreateJobNotificationPropertyTypeDef,
    ClientCreateJobResponseTypeDef,
    ClientCreateMlTransformInputRecordTablesTypeDef,
    ClientCreateMlTransformParametersTypeDef,
    ClientCreateMlTransformResponseTypeDef,
    ClientCreatePartitionPartitionInputTypeDef,
    ClientCreateScriptDagEdgesTypeDef,
    ClientCreateScriptDagNodesTypeDef,
    ClientCreateScriptResponseTypeDef,
    ClientCreateSecurityConfigurationEncryptionConfigurationTypeDef,
    ClientCreateSecurityConfigurationResponseTypeDef,
    ClientCreateTableTableInputTypeDef,
    ClientCreateTriggerActionsTypeDef,
    ClientCreateTriggerPredicateTypeDef,
    ClientCreateTriggerResponseTypeDef,
    ClientCreateUserDefinedFunctionFunctionInputTypeDef,
    ClientCreateWorkflowResponseTypeDef,
    ClientDeleteJobResponseTypeDef,
    ClientDeleteMlTransformResponseTypeDef,
    ClientDeleteTriggerResponseTypeDef,
    ClientDeleteWorkflowResponseTypeDef,
    ClientGetCatalogImportStatusResponseTypeDef,
    ClientGetClassifierResponseTypeDef,
    ClientGetClassifiersResponseTypeDef,
    ClientGetConnectionResponseTypeDef,
    ClientGetConnectionsFilterTypeDef,
    ClientGetConnectionsResponseTypeDef,
    ClientGetCrawlerMetricsResponseTypeDef,
    ClientGetCrawlerResponseTypeDef,
    ClientGetCrawlersResponseTypeDef,
    ClientGetDataCatalogEncryptionSettingsResponseTypeDef,
    ClientGetDatabaseResponseTypeDef,
    ClientGetDatabasesResponseTypeDef,
    ClientGetDataflowGraphResponseTypeDef,
    ClientGetDevEndpointResponseTypeDef,
    ClientGetDevEndpointsResponseTypeDef,
    ClientGetJobBookmarkResponseTypeDef,
    ClientGetJobResponseTypeDef,
    ClientGetJobRunResponseTypeDef,
    ClientGetJobRunsResponseTypeDef,
    ClientGetJobsResponseTypeDef,
    ClientGetMappingLocationTypeDef,
    ClientGetMappingResponseTypeDef,
    ClientGetMappingSinksTypeDef,
    ClientGetMappingSourceTypeDef,
    ClientGetMlTaskRunResponseTypeDef,
    ClientGetMlTaskRunsFilterTypeDef,
    ClientGetMlTaskRunsResponseTypeDef,
    ClientGetMlTaskRunsSortTypeDef,
    ClientGetMlTransformResponseTypeDef,
    ClientGetMlTransformsFilterTypeDef,
    ClientGetMlTransformsResponseTypeDef,
    ClientGetMlTransformsSortTypeDef,
    ClientGetPartitionResponseTypeDef,
    ClientGetPartitionsResponseTypeDef,
    ClientGetPartitionsSegmentTypeDef,
    ClientGetPlanLocationTypeDef,
    ClientGetPlanMappingTypeDef,
    ClientGetPlanResponseTypeDef,
    ClientGetPlanSinksTypeDef,
    ClientGetPlanSourceTypeDef,
    ClientGetResourcePolicyResponseTypeDef,
    ClientGetSecurityConfigurationResponseTypeDef,
    ClientGetSecurityConfigurationsResponseTypeDef,
    ClientGetTableResponseTypeDef,
    ClientGetTableVersionResponseTypeDef,
    ClientGetTableVersionsResponseTypeDef,
    ClientGetTablesResponseTypeDef,
    ClientGetTagsResponseTypeDef,
    ClientGetTriggerResponseTypeDef,
    ClientGetTriggersResponseTypeDef,
    ClientGetUserDefinedFunctionResponseTypeDef,
    ClientGetUserDefinedFunctionsResponseTypeDef,
    ClientGetWorkflowResponseTypeDef,
    ClientGetWorkflowRunPropertiesResponseTypeDef,
    ClientGetWorkflowRunResponseTypeDef,
    ClientGetWorkflowRunsResponseTypeDef,
    ClientListCrawlersResponseTypeDef,
    ClientListDevEndpointsResponseTypeDef,
    ClientListJobsResponseTypeDef,
    ClientListTriggersResponseTypeDef,
    ClientListWorkflowsResponseTypeDef,
    ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsTypeDef,
    ClientPutResourcePolicyResponseTypeDef,
    ClientResetJobBookmarkResponseTypeDef,
    ClientSearchTablesFiltersTypeDef,
    ClientSearchTablesResponseTypeDef,
    ClientSearchTablesSortCriteriaTypeDef,
    ClientStartExportLabelsTaskRunResponseTypeDef,
    ClientStartImportLabelsTaskRunResponseTypeDef,
    ClientStartJobRunNotificationPropertyTypeDef,
    ClientStartJobRunResponseTypeDef,
    ClientStartMlEvaluationTaskRunResponseTypeDef,
    ClientStartMlLabelingSetGenerationTaskRunResponseTypeDef,
    ClientStartTriggerResponseTypeDef,
    ClientStartWorkflowRunResponseTypeDef,
    ClientStopTriggerResponseTypeDef,
    ClientUpdateClassifierCsvClassifierTypeDef,
    ClientUpdateClassifierGrokClassifierTypeDef,
    ClientUpdateClassifierJsonClassifierTypeDef,
    ClientUpdateClassifierXMLClassifierTypeDef,
    ClientUpdateConnectionConnectionInputTypeDef,
    ClientUpdateCrawlerSchemaChangePolicyTypeDef,
    ClientUpdateCrawlerTargetsTypeDef,
    ClientUpdateDatabaseDatabaseInputTypeDef,
    ClientUpdateDevEndpointCustomLibrariesTypeDef,
    ClientUpdateJobJobUpdateTypeDef,
    ClientUpdateJobResponseTypeDef,
    ClientUpdateMlTransformParametersTypeDef,
    ClientUpdateMlTransformResponseTypeDef,
    ClientUpdatePartitionPartitionInputTypeDef,
    ClientUpdateTableTableInputTypeDef,
    ClientUpdateTriggerResponseTypeDef,
    ClientUpdateTriggerTriggerUpdateTypeDef,
    ClientUpdateUserDefinedFunctionFunctionInputTypeDef,
    ClientUpdateWorkflowResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [Glue.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_create_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionInputList: List[ClientBatchCreatePartitionPartitionInputListTypeDef],
        CatalogId: str = None,
    ) -> ClientBatchCreatePartitionResponseTypeDef:
        """
        [Client.batch_create_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.batch_create_partition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_connection(
        self, ConnectionNameList: List[str], CatalogId: str = None
    ) -> ClientBatchDeleteConnectionResponseTypeDef:
        """
        [Client.batch_delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.batch_delete_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionsToDelete: List[ClientBatchDeletePartitionPartitionsToDeleteTypeDef],
        CatalogId: str = None,
    ) -> ClientBatchDeletePartitionResponseTypeDef:
        """
        [Client.batch_delete_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.batch_delete_partition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_table(
        self, DatabaseName: str, TablesToDelete: List[str], CatalogId: str = None
    ) -> ClientBatchDeleteTableResponseTypeDef:
        """
        [Client.batch_delete_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.batch_delete_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_table_version(
        self, DatabaseName: str, TableName: str, VersionIds: List[str], CatalogId: str = None
    ) -> ClientBatchDeleteTableVersionResponseTypeDef:
        """
        [Client.batch_delete_table_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.batch_delete_table_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_crawlers(self, CrawlerNames: List[str]) -> ClientBatchGetCrawlersResponseTypeDef:
        """
        [Client.batch_get_crawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.batch_get_crawlers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_dev_endpoints(
        self, DevEndpointNames: List[str]
    ) -> ClientBatchGetDevEndpointsResponseTypeDef:
        """
        [Client.batch_get_dev_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.batch_get_dev_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_jobs(self, JobNames: List[str]) -> ClientBatchGetJobsResponseTypeDef:
        """
        [Client.batch_get_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.batch_get_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionsToGet: List[ClientBatchGetPartitionPartitionsToGetTypeDef],
        CatalogId: str = None,
    ) -> ClientBatchGetPartitionResponseTypeDef:
        """
        [Client.batch_get_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.batch_get_partition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_triggers(self, TriggerNames: List[str]) -> ClientBatchGetTriggersResponseTypeDef:
        """
        [Client.batch_get_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.batch_get_triggers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_workflows(
        self, Names: List[str], IncludeGraph: bool = None
    ) -> ClientBatchGetWorkflowsResponseTypeDef:
        """
        [Client.batch_get_workflows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.batch_get_workflows)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_stop_job_run(
        self, JobName: str, JobRunIds: List[str]
    ) -> ClientBatchStopJobRunResponseTypeDef:
        """
        [Client.batch_stop_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.batch_stop_job_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_ml_task_run(
        self, TransformId: str, TaskRunId: str
    ) -> ClientCancelMlTaskRunResponseTypeDef:
        """
        [Client.cancel_ml_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.cancel_ml_task_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_classifier(
        self,
        GrokClassifier: ClientCreateClassifierGrokClassifierTypeDef = None,
        XMLClassifier: ClientCreateClassifierXMLClassifierTypeDef = None,
        JsonClassifier: ClientCreateClassifierJsonClassifierTypeDef = None,
        CsvClassifier: ClientCreateClassifierCsvClassifierTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_classifier)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_connection(
        self, ConnectionInput: ClientCreateConnectionConnectionInputTypeDef, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.create_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_crawler(
        self,
        Name: str,
        Role: str,
        Targets: ClientCreateCrawlerTargetsTypeDef,
        DatabaseName: str = None,
        Description: str = None,
        Schedule: str = None,
        Classifiers: List[str] = None,
        TablePrefix: str = None,
        SchemaChangePolicy: ClientCreateCrawlerSchemaChangePolicyTypeDef = None,
        Configuration: str = None,
        CrawlerSecurityConfiguration: str = None,
        Tags: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_crawler)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_database(
        self, DatabaseInput: ClientCreateDatabaseDatabaseInputTypeDef, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.create_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_database)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dev_endpoint(
        self,
        EndpointName: str,
        RoleArn: str,
        SecurityGroupIds: List[str] = None,
        SubnetId: str = None,
        PublicKey: str = None,
        PublicKeys: List[str] = None,
        NumberOfNodes: int = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
        GlueVersion: str = None,
        NumberOfWorkers: int = None,
        ExtraPythonLibsS3Path: str = None,
        ExtraJarsS3Path: str = None,
        SecurityConfiguration: str = None,
        Tags: Dict[str, str] = None,
        Arguments: Dict[str, str] = None,
    ) -> ClientCreateDevEndpointResponseTypeDef:
        """
        [Client.create_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_dev_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_job(
        self,
        Name: str,
        Role: str,
        Command: ClientCreateJobCommandTypeDef,
        Description: str = None,
        LogUri: str = None,
        ExecutionProperty: ClientCreateJobExecutionPropertyTypeDef = None,
        DefaultArguments: Dict[str, str] = None,
        Connections: ClientCreateJobConnectionsTypeDef = None,
        MaxRetries: int = None,
        AllocatedCapacity: int = None,
        Timeout: int = None,
        MaxCapacity: float = None,
        SecurityConfiguration: str = None,
        Tags: Dict[str, str] = None,
        NotificationProperty: ClientCreateJobNotificationPropertyTypeDef = None,
        GlueVersion: str = None,
        NumberOfWorkers: int = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
    ) -> ClientCreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_ml_transform(
        self,
        Name: str,
        InputRecordTables: List[ClientCreateMlTransformInputRecordTablesTypeDef],
        Parameters: ClientCreateMlTransformParametersTypeDef,
        Role: str,
        Description: str = None,
        GlueVersion: str = None,
        MaxCapacity: float = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
        NumberOfWorkers: int = None,
        Timeout: int = None,
        MaxRetries: int = None,
    ) -> ClientCreateMlTransformResponseTypeDef:
        """
        [Client.create_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_ml_transform)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionInput: ClientCreatePartitionPartitionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_partition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_script(
        self,
        DagNodes: List[ClientCreateScriptDagNodesTypeDef] = None,
        DagEdges: List[ClientCreateScriptDagEdgesTypeDef] = None,
        Language: Literal["PYTHON", "SCALA"] = None,
    ) -> ClientCreateScriptResponseTypeDef:
        """
        [Client.create_script documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_script)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_security_configuration(
        self,
        Name: str,
        EncryptionConfiguration: ClientCreateSecurityConfigurationEncryptionConfigurationTypeDef,
    ) -> ClientCreateSecurityConfigurationResponseTypeDef:
        """
        [Client.create_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_security_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_table(
        self,
        DatabaseName: str,
        TableInput: ClientCreateTableTableInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_trigger(
        self,
        Name: str,
        Type: Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        Actions: List[ClientCreateTriggerActionsTypeDef],
        WorkflowName: str = None,
        Schedule: str = None,
        Predicate: ClientCreateTriggerPredicateTypeDef = None,
        Description: str = None,
        StartOnCreation: bool = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateTriggerResponseTypeDef:
        """
        [Client.create_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_trigger)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user_defined_function(
        self,
        DatabaseName: str,
        FunctionInput: ClientCreateUserDefinedFunctionFunctionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_user_defined_function)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_workflow(
        self,
        Name: str,
        Description: str = None,
        DefaultRunProperties: Dict[str, str] = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateWorkflowResponseTypeDef:
        """
        [Client.create_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.create_workflow)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_classifier(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_classifier)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_connection(self, ConnectionName: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_crawler(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_crawler)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_database(self, Name: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_database)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dev_endpoint(self, EndpointName: str) -> Dict[str, Any]:
        """
        [Client.delete_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_dev_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_job(self, JobName: str) -> ClientDeleteJobResponseTypeDef:
        """
        [Client.delete_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_ml_transform(self, TransformId: str) -> ClientDeleteMlTransformResponseTypeDef:
        """
        [Client.delete_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_ml_transform)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_partition(
        self, DatabaseName: str, TableName: str, PartitionValues: List[str], CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_partition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resource_policy(self, PolicyHashCondition: str = None) -> Dict[str, Any]:
        """
        [Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_resource_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_security_configuration(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_security_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_table(self, DatabaseName: str, Name: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_table_version(
        self, DatabaseName: str, TableName: str, VersionId: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_table_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_table_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_trigger(self, Name: str) -> ClientDeleteTriggerResponseTypeDef:
        """
        [Client.delete_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_trigger)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user_defined_function(
        self, DatabaseName: str, FunctionName: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_user_defined_function)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_workflow(self, Name: str) -> ClientDeleteWorkflowResponseTypeDef:
        """
        [Client.delete_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.delete_workflow)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_catalog_import_status(
        self, CatalogId: str = None
    ) -> ClientGetCatalogImportStatusResponseTypeDef:
        """
        [Client.get_catalog_import_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_catalog_import_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_classifier(self, Name: str) -> ClientGetClassifierResponseTypeDef:
        """
        [Client.get_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_classifier)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_classifiers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetClassifiersResponseTypeDef:
        """
        [Client.get_classifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_classifiers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connection(
        self, Name: str, CatalogId: str = None, HidePassword: bool = None
    ) -> ClientGetConnectionResponseTypeDef:
        """
        [Client.get_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connections(
        self,
        CatalogId: str = None,
        Filter: ClientGetConnectionsFilterTypeDef = None,
        HidePassword: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetConnectionsResponseTypeDef:
        """
        [Client.get_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_connections)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_crawler(self, Name: str) -> ClientGetCrawlerResponseTypeDef:
        """
        [Client.get_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_crawler)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_crawler_metrics(
        self, CrawlerNameList: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetCrawlerMetricsResponseTypeDef:
        """
        [Client.get_crawler_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_crawler_metrics)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_crawlers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetCrawlersResponseTypeDef:
        """
        [Client.get_crawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_crawlers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_data_catalog_encryption_settings(
        self, CatalogId: str = None
    ) -> ClientGetDataCatalogEncryptionSettingsResponseTypeDef:
        """
        [Client.get_data_catalog_encryption_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_data_catalog_encryption_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_database(self, Name: str, CatalogId: str = None) -> ClientGetDatabaseResponseTypeDef:
        """
        [Client.get_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_database)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_databases(
        self, CatalogId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetDatabasesResponseTypeDef:
        """
        [Client.get_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_databases)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dataflow_graph(self, PythonScript: str = None) -> ClientGetDataflowGraphResponseTypeDef:
        """
        [Client.get_dataflow_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_dataflow_graph)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dev_endpoint(self, EndpointName: str) -> ClientGetDevEndpointResponseTypeDef:
        """
        [Client.get_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_dev_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dev_endpoints(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetDevEndpointsResponseTypeDef:
        """
        [Client.get_dev_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_dev_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job(self, JobName: str) -> ClientGetJobResponseTypeDef:
        """
        [Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job_bookmark(
        self, JobName: str, RunId: str = None
    ) -> ClientGetJobBookmarkResponseTypeDef:
        """
        [Client.get_job_bookmark documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_job_bookmark)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job_run(
        self, JobName: str, RunId: str, PredecessorsIncluded: bool = None
    ) -> ClientGetJobRunResponseTypeDef:
        """
        [Client.get_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_job_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job_runs(
        self, JobName: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetJobRunsResponseTypeDef:
        """
        [Client.get_job_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_job_runs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_jobs(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetJobsResponseTypeDef:
        """
        [Client.get_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_mapping(
        self,
        Source: ClientGetMappingSourceTypeDef,
        Sinks: List[ClientGetMappingSinksTypeDef] = None,
        Location: ClientGetMappingLocationTypeDef = None,
    ) -> ClientGetMappingResponseTypeDef:
        """
        [Client.get_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_mapping)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ml_task_run(
        self, TransformId: str, TaskRunId: str
    ) -> ClientGetMlTaskRunResponseTypeDef:
        """
        [Client.get_ml_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_ml_task_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ml_task_runs(
        self,
        TransformId: str,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: ClientGetMlTaskRunsFilterTypeDef = None,
        Sort: ClientGetMlTaskRunsSortTypeDef = None,
    ) -> ClientGetMlTaskRunsResponseTypeDef:
        """
        [Client.get_ml_task_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_ml_task_runs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ml_transform(self, TransformId: str) -> ClientGetMlTransformResponseTypeDef:
        """
        [Client.get_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_ml_transform)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ml_transforms(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: ClientGetMlTransformsFilterTypeDef = None,
        Sort: ClientGetMlTransformsSortTypeDef = None,
    ) -> ClientGetMlTransformsResponseTypeDef:
        """
        [Client.get_ml_transforms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_ml_transforms)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_partition(
        self, DatabaseName: str, TableName: str, PartitionValues: List[str], CatalogId: str = None
    ) -> ClientGetPartitionResponseTypeDef:
        """
        [Client.get_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_partition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_partitions(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        Expression: str = None,
        NextToken: str = None,
        Segment: ClientGetPartitionsSegmentTypeDef = None,
        MaxResults: int = None,
    ) -> ClientGetPartitionsResponseTypeDef:
        """
        [Client.get_partitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_partitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_plan(
        self,
        Mapping: List[ClientGetPlanMappingTypeDef],
        Source: ClientGetPlanSourceTypeDef,
        Sinks: List[ClientGetPlanSinksTypeDef] = None,
        Location: ClientGetPlanLocationTypeDef = None,
        Language: Literal["PYTHON", "SCALA"] = None,
    ) -> ClientGetPlanResponseTypeDef:
        """
        [Client.get_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_plan)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_policy(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetResourcePolicyResponseTypeDef:
        """
        [Client.get_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_resource_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_security_configuration(
        self, Name: str
    ) -> ClientGetSecurityConfigurationResponseTypeDef:
        """
        [Client.get_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_security_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_security_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetSecurityConfigurationsResponseTypeDef:
        """
        [Client.get_security_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_security_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_table(
        self, DatabaseName: str, Name: str, CatalogId: str = None
    ) -> ClientGetTableResponseTypeDef:
        """
        [Client.get_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_table_version(
        self, DatabaseName: str, TableName: str, CatalogId: str = None, VersionId: str = None
    ) -> ClientGetTableVersionResponseTypeDef:
        """
        [Client.get_table_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_table_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_table_versions(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetTableVersionsResponseTypeDef:
        """
        [Client.get_table_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_table_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_tables(
        self,
        DatabaseName: str,
        CatalogId: str = None,
        Expression: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetTablesResponseTypeDef:
        """
        [Client.get_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_tables)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_tags(self, ResourceArn: str) -> ClientGetTagsResponseTypeDef:
        """
        [Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_trigger(self, Name: str) -> ClientGetTriggerResponseTypeDef:
        """
        [Client.get_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_trigger)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_triggers(
        self, NextToken: str = None, DependentJobName: str = None, MaxResults: int = None
    ) -> ClientGetTriggersResponseTypeDef:
        """
        [Client.get_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_triggers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_user_defined_function(
        self, DatabaseName: str, FunctionName: str, CatalogId: str = None
    ) -> ClientGetUserDefinedFunctionResponseTypeDef:
        """
        [Client.get_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_user_defined_function)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_user_defined_functions(
        self,
        DatabaseName: str,
        Pattern: str,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetUserDefinedFunctionsResponseTypeDef:
        """
        [Client.get_user_defined_functions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_user_defined_functions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_workflow(
        self, Name: str, IncludeGraph: bool = None
    ) -> ClientGetWorkflowResponseTypeDef:
        """
        [Client.get_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_workflow)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_workflow_run(
        self, Name: str, RunId: str, IncludeGraph: bool = None
    ) -> ClientGetWorkflowRunResponseTypeDef:
        """
        [Client.get_workflow_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_workflow_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_workflow_run_properties(
        self, Name: str, RunId: str
    ) -> ClientGetWorkflowRunPropertiesResponseTypeDef:
        """
        [Client.get_workflow_run_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_workflow_run_properties)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_workflow_runs(
        self, Name: str, IncludeGraph: bool = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetWorkflowRunsResponseTypeDef:
        """
        [Client.get_workflow_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.get_workflow_runs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_catalog_to_glue(self, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Client.import_catalog_to_glue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.import_catalog_to_glue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_crawlers(
        self, MaxResults: int = None, NextToken: str = None, Tags: Dict[str, str] = None
    ) -> ClientListCrawlersResponseTypeDef:
        """
        [Client.list_crawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.list_crawlers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dev_endpoints(
        self, NextToken: str = None, MaxResults: int = None, Tags: Dict[str, str] = None
    ) -> ClientListDevEndpointsResponseTypeDef:
        """
        [Client.list_dev_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.list_dev_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs(
        self, NextToken: str = None, MaxResults: int = None, Tags: Dict[str, str] = None
    ) -> ClientListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.list_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_triggers(
        self,
        NextToken: str = None,
        DependentJobName: str = None,
        MaxResults: int = None,
        Tags: Dict[str, str] = None,
    ) -> ClientListTriggersResponseTypeDef:
        """
        [Client.list_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.list_triggers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_workflows(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListWorkflowsResponseTypeDef:
        """
        [Client.list_workflows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.list_workflows)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_data_catalog_encryption_settings(
        self,
        DataCatalogEncryptionSettings: ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_data_catalog_encryption_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.put_data_catalog_encryption_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_resource_policy(
        self,
        PolicyInJson: str,
        PolicyHashCondition: str = None,
        PolicyExistsCondition: Literal["MUST_EXIST", "NOT_EXIST", "NONE"] = None,
    ) -> ClientPutResourcePolicyResponseTypeDef:
        """
        [Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.put_resource_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_workflow_run_properties(
        self, Name: str, RunId: str, RunProperties: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        [Client.put_workflow_run_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.put_workflow_run_properties)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_job_bookmark(
        self, JobName: str, RunId: str = None
    ) -> ClientResetJobBookmarkResponseTypeDef:
        """
        [Client.reset_job_bookmark documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.reset_job_bookmark)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_tables(
        self,
        CatalogId: str = None,
        NextToken: str = None,
        Filters: List[ClientSearchTablesFiltersTypeDef] = None,
        SearchText: str = None,
        SortCriteria: List[ClientSearchTablesSortCriteriaTypeDef] = None,
        MaxResults: int = None,
    ) -> ClientSearchTablesResponseTypeDef:
        """
        [Client.search_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.search_tables)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_crawler(self, Name: str) -> Dict[str, Any]:
        """
        [Client.start_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.start_crawler)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_crawler_schedule(self, CrawlerName: str) -> Dict[str, Any]:
        """
        [Client.start_crawler_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.start_crawler_schedule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_export_labels_task_run(
        self, TransformId: str, OutputS3Path: str
    ) -> ClientStartExportLabelsTaskRunResponseTypeDef:
        """
        [Client.start_export_labels_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.start_export_labels_task_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_import_labels_task_run(
        self, TransformId: str, InputS3Path: str, ReplaceAllLabels: bool = None
    ) -> ClientStartImportLabelsTaskRunResponseTypeDef:
        """
        [Client.start_import_labels_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.start_import_labels_task_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_job_run(
        self,
        JobName: str,
        JobRunId: str = None,
        Arguments: Dict[str, str] = None,
        AllocatedCapacity: int = None,
        Timeout: int = None,
        MaxCapacity: float = None,
        SecurityConfiguration: str = None,
        NotificationProperty: ClientStartJobRunNotificationPropertyTypeDef = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
        NumberOfWorkers: int = None,
    ) -> ClientStartJobRunResponseTypeDef:
        """
        [Client.start_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.start_job_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_ml_evaluation_task_run(
        self, TransformId: str
    ) -> ClientStartMlEvaluationTaskRunResponseTypeDef:
        """
        [Client.start_ml_evaluation_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.start_ml_evaluation_task_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_ml_labeling_set_generation_task_run(
        self, TransformId: str, OutputS3Path: str
    ) -> ClientStartMlLabelingSetGenerationTaskRunResponseTypeDef:
        """
        [Client.start_ml_labeling_set_generation_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.start_ml_labeling_set_generation_task_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_trigger(self, Name: str) -> ClientStartTriggerResponseTypeDef:
        """
        [Client.start_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.start_trigger)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_workflow_run(self, Name: str) -> ClientStartWorkflowRunResponseTypeDef:
        """
        [Client.start_workflow_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.start_workflow_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_crawler(self, Name: str) -> Dict[str, Any]:
        """
        [Client.stop_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.stop_crawler)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_crawler_schedule(self, CrawlerName: str) -> Dict[str, Any]:
        """
        [Client.stop_crawler_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.stop_crawler_schedule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_trigger(self, Name: str) -> ClientStopTriggerResponseTypeDef:
        """
        [Client.stop_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.stop_trigger)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, TagsToAdd: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagsToRemove: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_classifier(
        self,
        GrokClassifier: ClientUpdateClassifierGrokClassifierTypeDef = None,
        XMLClassifier: ClientUpdateClassifierXMLClassifierTypeDef = None,
        JsonClassifier: ClientUpdateClassifierJsonClassifierTypeDef = None,
        CsvClassifier: ClientUpdateClassifierCsvClassifierTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.update_classifier)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_connection(
        self,
        Name: str,
        ConnectionInput: ClientUpdateConnectionConnectionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.update_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_crawler(
        self,
        Name: str,
        Role: str = None,
        DatabaseName: str = None,
        Description: str = None,
        Targets: ClientUpdateCrawlerTargetsTypeDef = None,
        Schedule: str = None,
        Classifiers: List[str] = None,
        TablePrefix: str = None,
        SchemaChangePolicy: ClientUpdateCrawlerSchemaChangePolicyTypeDef = None,
        Configuration: str = None,
        CrawlerSecurityConfiguration: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.update_crawler)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_crawler_schedule(self, CrawlerName: str, Schedule: str = None) -> Dict[str, Any]:
        """
        [Client.update_crawler_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.update_crawler_schedule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_database(
        self,
        Name: str,
        DatabaseInput: ClientUpdateDatabaseDatabaseInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.update_database)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_dev_endpoint(
        self,
        EndpointName: str,
        PublicKey: str = None,
        AddPublicKeys: List[str] = None,
        DeletePublicKeys: List[str] = None,
        CustomLibraries: ClientUpdateDevEndpointCustomLibrariesTypeDef = None,
        UpdateEtlLibraries: bool = None,
        DeleteArguments: List[str] = None,
        AddArguments: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.update_dev_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_job(
        self, JobName: str, JobUpdate: ClientUpdateJobJobUpdateTypeDef
    ) -> ClientUpdateJobResponseTypeDef:
        """
        [Client.update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.update_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_ml_transform(
        self,
        TransformId: str,
        Name: str = None,
        Description: str = None,
        Parameters: ClientUpdateMlTransformParametersTypeDef = None,
        Role: str = None,
        GlueVersion: str = None,
        MaxCapacity: float = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
        NumberOfWorkers: int = None,
        Timeout: int = None,
        MaxRetries: int = None,
    ) -> ClientUpdateMlTransformResponseTypeDef:
        """
        [Client.update_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.update_ml_transform)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValueList: List[str],
        PartitionInput: ClientUpdatePartitionPartitionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.update_partition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_table(
        self,
        DatabaseName: str,
        TableInput: ClientUpdateTableTableInputTypeDef,
        CatalogId: str = None,
        SkipArchive: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.update_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_trigger(
        self, Name: str, TriggerUpdate: ClientUpdateTriggerTriggerUpdateTypeDef
    ) -> ClientUpdateTriggerResponseTypeDef:
        """
        [Client.update_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.update_trigger)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user_defined_function(
        self,
        DatabaseName: str,
        FunctionName: str,
        FunctionInput: ClientUpdateUserDefinedFunctionFunctionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.update_user_defined_function)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_workflow(
        self, Name: str, Description: str = None, DefaultRunProperties: Dict[str, str] = None
    ) -> ClientUpdateWorkflowResponseTypeDef:
        """
        [Client.update_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Client.update_workflow)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_classifiers"]
    ) -> paginator_scope.GetClassifiersPaginator:
        """
        [Paginator.GetClassifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetClassifiers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_connections"]
    ) -> paginator_scope.GetConnectionsPaginator:
        """
        [Paginator.GetConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetConnections)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_crawler_metrics"]
    ) -> paginator_scope.GetCrawlerMetricsPaginator:
        """
        [Paginator.GetCrawlerMetrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetCrawlerMetrics)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_crawlers"]
    ) -> paginator_scope.GetCrawlersPaginator:
        """
        [Paginator.GetCrawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetCrawlers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_databases"]
    ) -> paginator_scope.GetDatabasesPaginator:
        """
        [Paginator.GetDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetDatabases)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_dev_endpoints"]
    ) -> paginator_scope.GetDevEndpointsPaginator:
        """
        [Paginator.GetDevEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetDevEndpoints)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_job_runs"]
    ) -> paginator_scope.GetJobRunsPaginator:
        """
        [Paginator.GetJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetJobRuns)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_jobs"]
    ) -> paginator_scope.GetJobsPaginator:
        """
        [Paginator.GetJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_partitions"]
    ) -> paginator_scope.GetPartitionsPaginator:
        """
        [Paginator.GetPartitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetPartitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_security_configurations"]
    ) -> paginator_scope.GetSecurityConfigurationsPaginator:
        """
        [Paginator.GetSecurityConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetSecurityConfigurations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_table_versions"]
    ) -> paginator_scope.GetTableVersionsPaginator:
        """
        [Paginator.GetTableVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetTableVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_tables"]
    ) -> paginator_scope.GetTablesPaginator:
        """
        [Paginator.GetTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetTables)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_triggers"]
    ) -> paginator_scope.GetTriggersPaginator:
        """
        [Paginator.GetTriggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetTriggers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_user_defined_functions"]
    ) -> paginator_scope.GetUserDefinedFunctionsPaginator:
        """
        [Paginator.GetUserDefinedFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetUserDefinedFunctions)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AlreadyExistsException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    ConcurrentRunsExceededException: Boto3ClientError
    ConditionCheckFailureException: Boto3ClientError
    CrawlerNotRunningException: Boto3ClientError
    CrawlerRunningException: Boto3ClientError
    CrawlerStoppingException: Boto3ClientError
    EntityNotFoundException: Boto3ClientError
    GlueEncryptionException: Boto3ClientError
    IdempotentParameterMismatchException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    MLTransformNotReadyException: Boto3ClientError
    NoScheduleException: Boto3ClientError
    OperationTimeoutException: Boto3ClientError
    ResourceNumberLimitExceededException: Boto3ClientError
    SchedulerNotRunningException: Boto3ClientError
    SchedulerRunningException: Boto3ClientError
    SchedulerTransitioningException: Boto3ClientError
    ValidationException: Boto3ClientError
    VersionMismatchException: Boto3ClientError
