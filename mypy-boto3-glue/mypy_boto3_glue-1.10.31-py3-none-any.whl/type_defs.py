"Main interface for glue service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchCreatePartitionPartitionInputListStorageDescriptorColumnsTypeDef",
    "ClientBatchCreatePartitionPartitionInputListStorageDescriptorSerdeInfoTypeDef",
    "ClientBatchCreatePartitionPartitionInputListStorageDescriptorSkewedInfoTypeDef",
    "ClientBatchCreatePartitionPartitionInputListStorageDescriptorSortColumnsTypeDef",
    "ClientBatchCreatePartitionPartitionInputListStorageDescriptorTypeDef",
    "ClientBatchCreatePartitionPartitionInputListTypeDef",
    "ClientBatchCreatePartitionResponseErrorsErrorDetailTypeDef",
    "ClientBatchCreatePartitionResponseErrorsTypeDef",
    "ClientBatchCreatePartitionResponseTypeDef",
    "ClientBatchDeleteConnectionResponseErrorsTypeDef",
    "ClientBatchDeleteConnectionResponseTypeDef",
    "ClientBatchDeletePartitionPartitionsToDeleteTypeDef",
    "ClientBatchDeletePartitionResponseErrorsErrorDetailTypeDef",
    "ClientBatchDeletePartitionResponseErrorsTypeDef",
    "ClientBatchDeletePartitionResponseTypeDef",
    "ClientBatchDeleteTableResponseErrorsErrorDetailTypeDef",
    "ClientBatchDeleteTableResponseErrorsTypeDef",
    "ClientBatchDeleteTableResponseTypeDef",
    "ClientBatchDeleteTableVersionResponseErrorsErrorDetailTypeDef",
    "ClientBatchDeleteTableVersionResponseErrorsTypeDef",
    "ClientBatchDeleteTableVersionResponseTypeDef",
    "ClientBatchGetCrawlersResponseCrawlersLastCrawlTypeDef",
    "ClientBatchGetCrawlersResponseCrawlersScheduleTypeDef",
    "ClientBatchGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef",
    "ClientBatchGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef",
    "ClientBatchGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef",
    "ClientBatchGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef",
    "ClientBatchGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef",
    "ClientBatchGetCrawlersResponseCrawlersTargetsTypeDef",
    "ClientBatchGetCrawlersResponseCrawlersTypeDef",
    "ClientBatchGetCrawlersResponseTypeDef",
    "ClientBatchGetDevEndpointsResponseDevEndpointsTypeDef",
    "ClientBatchGetDevEndpointsResponseTypeDef",
    "ClientBatchGetJobsResponseJobsCommandTypeDef",
    "ClientBatchGetJobsResponseJobsConnectionsTypeDef",
    "ClientBatchGetJobsResponseJobsExecutionPropertyTypeDef",
    "ClientBatchGetJobsResponseJobsNotificationPropertyTypeDef",
    "ClientBatchGetJobsResponseJobsTypeDef",
    "ClientBatchGetJobsResponseTypeDef",
    "ClientBatchGetPartitionPartitionsToGetTypeDef",
    "ClientBatchGetPartitionResponsePartitionsStorageDescriptorColumnsTypeDef",
    "ClientBatchGetPartitionResponsePartitionsStorageDescriptorSerdeInfoTypeDef",
    "ClientBatchGetPartitionResponsePartitionsStorageDescriptorSkewedInfoTypeDef",
    "ClientBatchGetPartitionResponsePartitionsStorageDescriptorSortColumnsTypeDef",
    "ClientBatchGetPartitionResponsePartitionsStorageDescriptorTypeDef",
    "ClientBatchGetPartitionResponsePartitionsTypeDef",
    "ClientBatchGetPartitionResponseUnprocessedKeysTypeDef",
    "ClientBatchGetPartitionResponseTypeDef",
    "ClientBatchGetTriggersResponseTriggersActionsNotificationPropertyTypeDef",
    "ClientBatchGetTriggersResponseTriggersActionsTypeDef",
    "ClientBatchGetTriggersResponseTriggersPredicateConditionsTypeDef",
    "ClientBatchGetTriggersResponseTriggersPredicateTypeDef",
    "ClientBatchGetTriggersResponseTriggersTypeDef",
    "ClientBatchGetTriggersResponseTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphEdgesTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsCrawlsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsGraphTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphEdgesTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsCrawlsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunStatisticsTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunTypeDef",
    "ClientBatchGetWorkflowsResponseWorkflowsTypeDef",
    "ClientBatchGetWorkflowsResponseTypeDef",
    "ClientBatchStopJobRunResponseErrorsErrorDetailTypeDef",
    "ClientBatchStopJobRunResponseErrorsTypeDef",
    "ClientBatchStopJobRunResponseSuccessfulSubmissionsTypeDef",
    "ClientBatchStopJobRunResponseTypeDef",
    "ClientCancelMlTaskRunResponseTypeDef",
    "ClientCreateClassifierCsvClassifierTypeDef",
    "ClientCreateClassifierGrokClassifierTypeDef",
    "ClientCreateClassifierJsonClassifierTypeDef",
    "ClientCreateClassifierXMLClassifierTypeDef",
    "ClientCreateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef",
    "ClientCreateConnectionConnectionInputTypeDef",
    "ClientCreateCrawlerSchemaChangePolicyTypeDef",
    "ClientCreateCrawlerTargetsCatalogTargetsTypeDef",
    "ClientCreateCrawlerTargetsDynamoDBTargetsTypeDef",
    "ClientCreateCrawlerTargetsJdbcTargetsTypeDef",
    "ClientCreateCrawlerTargetsS3TargetsTypeDef",
    "ClientCreateCrawlerTargetsTypeDef",
    "ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef",
    "ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef",
    "ClientCreateDatabaseDatabaseInputTypeDef",
    "ClientCreateDevEndpointResponseTypeDef",
    "ClientCreateJobCommandTypeDef",
    "ClientCreateJobConnectionsTypeDef",
    "ClientCreateJobExecutionPropertyTypeDef",
    "ClientCreateJobNotificationPropertyTypeDef",
    "ClientCreateJobResponseTypeDef",
    "ClientCreateMlTransformInputRecordTablesTypeDef",
    "ClientCreateMlTransformParametersFindMatchesParametersTypeDef",
    "ClientCreateMlTransformParametersTypeDef",
    "ClientCreateMlTransformResponseTypeDef",
    "ClientCreatePartitionPartitionInputStorageDescriptorColumnsTypeDef",
    "ClientCreatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef",
    "ClientCreatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef",
    "ClientCreatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef",
    "ClientCreatePartitionPartitionInputStorageDescriptorTypeDef",
    "ClientCreatePartitionPartitionInputTypeDef",
    "ClientCreateScriptDagEdgesTypeDef",
    "ClientCreateScriptDagNodesArgsTypeDef",
    "ClientCreateScriptDagNodesTypeDef",
    "ClientCreateScriptResponseTypeDef",
    "ClientCreateSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef",
    "ClientCreateSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef",
    "ClientCreateSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef",
    "ClientCreateSecurityConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateSecurityConfigurationResponseTypeDef",
    "ClientCreateTableTableInputPartitionKeysTypeDef",
    "ClientCreateTableTableInputStorageDescriptorColumnsTypeDef",
    "ClientCreateTableTableInputStorageDescriptorSerdeInfoTypeDef",
    "ClientCreateTableTableInputStorageDescriptorSkewedInfoTypeDef",
    "ClientCreateTableTableInputStorageDescriptorSortColumnsTypeDef",
    "ClientCreateTableTableInputStorageDescriptorTypeDef",
    "ClientCreateTableTableInputTypeDef",
    "ClientCreateTriggerActionsNotificationPropertyTypeDef",
    "ClientCreateTriggerActionsTypeDef",
    "ClientCreateTriggerPredicateConditionsTypeDef",
    "ClientCreateTriggerPredicateTypeDef",
    "ClientCreateTriggerResponseTypeDef",
    "ClientCreateUserDefinedFunctionFunctionInputResourceUrisTypeDef",
    "ClientCreateUserDefinedFunctionFunctionInputTypeDef",
    "ClientCreateWorkflowResponseTypeDef",
    "ClientDeleteJobResponseTypeDef",
    "ClientDeleteMlTransformResponseTypeDef",
    "ClientDeleteTriggerResponseTypeDef",
    "ClientDeleteWorkflowResponseTypeDef",
    "ClientGetCatalogImportStatusResponseImportStatusTypeDef",
    "ClientGetCatalogImportStatusResponseTypeDef",
    "ClientGetClassifierResponseClassifierCsvClassifierTypeDef",
    "ClientGetClassifierResponseClassifierGrokClassifierTypeDef",
    "ClientGetClassifierResponseClassifierJsonClassifierTypeDef",
    "ClientGetClassifierResponseClassifierXMLClassifierTypeDef",
    "ClientGetClassifierResponseClassifierTypeDef",
    "ClientGetClassifierResponseTypeDef",
    "ClientGetClassifiersResponseClassifiersCsvClassifierTypeDef",
    "ClientGetClassifiersResponseClassifiersGrokClassifierTypeDef",
    "ClientGetClassifiersResponseClassifiersJsonClassifierTypeDef",
    "ClientGetClassifiersResponseClassifiersXMLClassifierTypeDef",
    "ClientGetClassifiersResponseClassifiersTypeDef",
    "ClientGetClassifiersResponseTypeDef",
    "ClientGetConnectionResponseConnectionPhysicalConnectionRequirementsTypeDef",
    "ClientGetConnectionResponseConnectionTypeDef",
    "ClientGetConnectionResponseTypeDef",
    "ClientGetConnectionsFilterTypeDef",
    "ClientGetConnectionsResponseConnectionListPhysicalConnectionRequirementsTypeDef",
    "ClientGetConnectionsResponseConnectionListTypeDef",
    "ClientGetConnectionsResponseTypeDef",
    "ClientGetCrawlerMetricsResponseCrawlerMetricsListTypeDef",
    "ClientGetCrawlerMetricsResponseTypeDef",
    "ClientGetCrawlerResponseCrawlerLastCrawlTypeDef",
    "ClientGetCrawlerResponseCrawlerScheduleTypeDef",
    "ClientGetCrawlerResponseCrawlerSchemaChangePolicyTypeDef",
    "ClientGetCrawlerResponseCrawlerTargetsCatalogTargetsTypeDef",
    "ClientGetCrawlerResponseCrawlerTargetsDynamoDBTargetsTypeDef",
    "ClientGetCrawlerResponseCrawlerTargetsJdbcTargetsTypeDef",
    "ClientGetCrawlerResponseCrawlerTargetsS3TargetsTypeDef",
    "ClientGetCrawlerResponseCrawlerTargetsTypeDef",
    "ClientGetCrawlerResponseCrawlerTypeDef",
    "ClientGetCrawlerResponseTypeDef",
    "ClientGetCrawlersResponseCrawlersLastCrawlTypeDef",
    "ClientGetCrawlersResponseCrawlersScheduleTypeDef",
    "ClientGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef",
    "ClientGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef",
    "ClientGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef",
    "ClientGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef",
    "ClientGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef",
    "ClientGetCrawlersResponseCrawlersTargetsTypeDef",
    "ClientGetCrawlersResponseCrawlersTypeDef",
    "ClientGetCrawlersResponseTypeDef",
    "ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef",
    "ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsEncryptionAtRestTypeDef",
    "ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsTypeDef",
    "ClientGetDataCatalogEncryptionSettingsResponseTypeDef",
    "ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsPrincipalTypeDef",
    "ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsTypeDef",
    "ClientGetDatabaseResponseDatabaseTypeDef",
    "ClientGetDatabaseResponseTypeDef",
    "ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef",
    "ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsTypeDef",
    "ClientGetDatabasesResponseDatabaseListTypeDef",
    "ClientGetDatabasesResponseTypeDef",
    "ClientGetDataflowGraphResponseDagEdgesTypeDef",
    "ClientGetDataflowGraphResponseDagNodesArgsTypeDef",
    "ClientGetDataflowGraphResponseDagNodesTypeDef",
    "ClientGetDataflowGraphResponseTypeDef",
    "ClientGetDevEndpointResponseDevEndpointTypeDef",
    "ClientGetDevEndpointResponseTypeDef",
    "ClientGetDevEndpointsResponseDevEndpointsTypeDef",
    "ClientGetDevEndpointsResponseTypeDef",
    "ClientGetJobBookmarkResponseJobBookmarkEntryTypeDef",
    "ClientGetJobBookmarkResponseTypeDef",
    "ClientGetJobResponseJobCommandTypeDef",
    "ClientGetJobResponseJobConnectionsTypeDef",
    "ClientGetJobResponseJobExecutionPropertyTypeDef",
    "ClientGetJobResponseJobNotificationPropertyTypeDef",
    "ClientGetJobResponseJobTypeDef",
    "ClientGetJobResponseTypeDef",
    "ClientGetJobRunResponseJobRunNotificationPropertyTypeDef",
    "ClientGetJobRunResponseJobRunPredecessorRunsTypeDef",
    "ClientGetJobRunResponseJobRunTypeDef",
    "ClientGetJobRunResponseTypeDef",
    "ClientGetJobRunsResponseJobRunsNotificationPropertyTypeDef",
    "ClientGetJobRunsResponseJobRunsPredecessorRunsTypeDef",
    "ClientGetJobRunsResponseJobRunsTypeDef",
    "ClientGetJobRunsResponseTypeDef",
    "ClientGetJobsResponseJobsCommandTypeDef",
    "ClientGetJobsResponseJobsConnectionsTypeDef",
    "ClientGetJobsResponseJobsExecutionPropertyTypeDef",
    "ClientGetJobsResponseJobsNotificationPropertyTypeDef",
    "ClientGetJobsResponseJobsTypeDef",
    "ClientGetJobsResponseTypeDef",
    "ClientGetMappingLocationDynamoDBTypeDef",
    "ClientGetMappingLocationJdbcTypeDef",
    "ClientGetMappingLocationS3TypeDef",
    "ClientGetMappingLocationTypeDef",
    "ClientGetMappingResponseMappingTypeDef",
    "ClientGetMappingResponseTypeDef",
    "ClientGetMappingSinksTypeDef",
    "ClientGetMappingSourceTypeDef",
    "ClientGetMlTaskRunResponsePropertiesExportLabelsTaskRunPropertiesTypeDef",
    "ClientGetMlTaskRunResponsePropertiesFindMatchesTaskRunPropertiesTypeDef",
    "ClientGetMlTaskRunResponsePropertiesImportLabelsTaskRunPropertiesTypeDef",
    "ClientGetMlTaskRunResponsePropertiesLabelingSetGenerationTaskRunPropertiesTypeDef",
    "ClientGetMlTaskRunResponsePropertiesTypeDef",
    "ClientGetMlTaskRunResponseTypeDef",
    "ClientGetMlTaskRunsFilterTypeDef",
    "ClientGetMlTaskRunsResponseTaskRunsPropertiesExportLabelsTaskRunPropertiesTypeDef",
    "ClientGetMlTaskRunsResponseTaskRunsPropertiesFindMatchesTaskRunPropertiesTypeDef",
    "ClientGetMlTaskRunsResponseTaskRunsPropertiesImportLabelsTaskRunPropertiesTypeDef",
    "ClientGetMlTaskRunsResponseTaskRunsPropertiesLabelingSetGenerationTaskRunPropertiesTypeDef",
    "ClientGetMlTaskRunsResponseTaskRunsPropertiesTypeDef",
    "ClientGetMlTaskRunsResponseTaskRunsTypeDef",
    "ClientGetMlTaskRunsResponseTypeDef",
    "ClientGetMlTaskRunsSortTypeDef",
    "ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef",
    "ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsTypeDef",
    "ClientGetMlTransformResponseEvaluationMetricsTypeDef",
    "ClientGetMlTransformResponseInputRecordTablesTypeDef",
    "ClientGetMlTransformResponseParametersFindMatchesParametersTypeDef",
    "ClientGetMlTransformResponseParametersTypeDef",
    "ClientGetMlTransformResponseSchemaTypeDef",
    "ClientGetMlTransformResponseTypeDef",
    "ClientGetMlTransformsFilterSchemaTypeDef",
    "ClientGetMlTransformsFilterTypeDef",
    "ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef",
    "ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsTypeDef",
    "ClientGetMlTransformsResponseTransformsEvaluationMetricsTypeDef",
    "ClientGetMlTransformsResponseTransformsInputRecordTablesTypeDef",
    "ClientGetMlTransformsResponseTransformsParametersFindMatchesParametersTypeDef",
    "ClientGetMlTransformsResponseTransformsParametersTypeDef",
    "ClientGetMlTransformsResponseTransformsSchemaTypeDef",
    "ClientGetMlTransformsResponseTransformsTypeDef",
    "ClientGetMlTransformsResponseTypeDef",
    "ClientGetMlTransformsSortTypeDef",
    "ClientGetPartitionResponsePartitionStorageDescriptorColumnsTypeDef",
    "ClientGetPartitionResponsePartitionStorageDescriptorSerdeInfoTypeDef",
    "ClientGetPartitionResponsePartitionStorageDescriptorSkewedInfoTypeDef",
    "ClientGetPartitionResponsePartitionStorageDescriptorSortColumnsTypeDef",
    "ClientGetPartitionResponsePartitionStorageDescriptorTypeDef",
    "ClientGetPartitionResponsePartitionTypeDef",
    "ClientGetPartitionResponseTypeDef",
    "ClientGetPartitionsResponsePartitionsStorageDescriptorColumnsTypeDef",
    "ClientGetPartitionsResponsePartitionsStorageDescriptorSerdeInfoTypeDef",
    "ClientGetPartitionsResponsePartitionsStorageDescriptorSkewedInfoTypeDef",
    "ClientGetPartitionsResponsePartitionsStorageDescriptorSortColumnsTypeDef",
    "ClientGetPartitionsResponsePartitionsStorageDescriptorTypeDef",
    "ClientGetPartitionsResponsePartitionsTypeDef",
    "ClientGetPartitionsResponseTypeDef",
    "ClientGetPartitionsSegmentTypeDef",
    "ClientGetPlanLocationDynamoDBTypeDef",
    "ClientGetPlanLocationJdbcTypeDef",
    "ClientGetPlanLocationS3TypeDef",
    "ClientGetPlanLocationTypeDef",
    "ClientGetPlanMappingTypeDef",
    "ClientGetPlanResponseTypeDef",
    "ClientGetPlanSinksTypeDef",
    "ClientGetPlanSourceTypeDef",
    "ClientGetResourcePolicyResponseTypeDef",
    "ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef",
    "ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef",
    "ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef",
    "ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationTypeDef",
    "ClientGetSecurityConfigurationResponseSecurityConfigurationTypeDef",
    "ClientGetSecurityConfigurationResponseTypeDef",
    "ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef",
    "ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef",
    "ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef",
    "ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationTypeDef",
    "ClientGetSecurityConfigurationsResponseSecurityConfigurationsTypeDef",
    "ClientGetSecurityConfigurationsResponseTypeDef",
    "ClientGetTableResponseTablePartitionKeysTypeDef",
    "ClientGetTableResponseTableStorageDescriptorColumnsTypeDef",
    "ClientGetTableResponseTableStorageDescriptorSerdeInfoTypeDef",
    "ClientGetTableResponseTableStorageDescriptorSkewedInfoTypeDef",
    "ClientGetTableResponseTableStorageDescriptorSortColumnsTypeDef",
    "ClientGetTableResponseTableStorageDescriptorTypeDef",
    "ClientGetTableResponseTableTypeDef",
    "ClientGetTableResponseTypeDef",
    "ClientGetTableVersionResponseTableVersionTablePartitionKeysTypeDef",
    "ClientGetTableVersionResponseTableVersionTableStorageDescriptorColumnsTypeDef",
    "ClientGetTableVersionResponseTableVersionTableStorageDescriptorSerdeInfoTypeDef",
    "ClientGetTableVersionResponseTableVersionTableStorageDescriptorSkewedInfoTypeDef",
    "ClientGetTableVersionResponseTableVersionTableStorageDescriptorSortColumnsTypeDef",
    "ClientGetTableVersionResponseTableVersionTableStorageDescriptorTypeDef",
    "ClientGetTableVersionResponseTableVersionTableTypeDef",
    "ClientGetTableVersionResponseTableVersionTypeDef",
    "ClientGetTableVersionResponseTypeDef",
    "ClientGetTableVersionsResponseTableVersionsTablePartitionKeysTypeDef",
    "ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorColumnsTypeDef",
    "ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef",
    "ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef",
    "ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef",
    "ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorTypeDef",
    "ClientGetTableVersionsResponseTableVersionsTableTypeDef",
    "ClientGetTableVersionsResponseTableVersionsTypeDef",
    "ClientGetTableVersionsResponseTypeDef",
    "ClientGetTablesResponseTableListPartitionKeysTypeDef",
    "ClientGetTablesResponseTableListStorageDescriptorColumnsTypeDef",
    "ClientGetTablesResponseTableListStorageDescriptorSerdeInfoTypeDef",
    "ClientGetTablesResponseTableListStorageDescriptorSkewedInfoTypeDef",
    "ClientGetTablesResponseTableListStorageDescriptorSortColumnsTypeDef",
    "ClientGetTablesResponseTableListStorageDescriptorTypeDef",
    "ClientGetTablesResponseTableListTypeDef",
    "ClientGetTablesResponseTypeDef",
    "ClientGetTagsResponseTypeDef",
    "ClientGetTriggerResponseTriggerActionsNotificationPropertyTypeDef",
    "ClientGetTriggerResponseTriggerActionsTypeDef",
    "ClientGetTriggerResponseTriggerPredicateConditionsTypeDef",
    "ClientGetTriggerResponseTriggerPredicateTypeDef",
    "ClientGetTriggerResponseTriggerTypeDef",
    "ClientGetTriggerResponseTypeDef",
    "ClientGetTriggersResponseTriggersActionsNotificationPropertyTypeDef",
    "ClientGetTriggersResponseTriggersActionsTypeDef",
    "ClientGetTriggersResponseTriggersPredicateConditionsTypeDef",
    "ClientGetTriggersResponseTriggersPredicateTypeDef",
    "ClientGetTriggersResponseTriggersTypeDef",
    "ClientGetTriggersResponseTypeDef",
    "ClientGetUserDefinedFunctionResponseUserDefinedFunctionResourceUrisTypeDef",
    "ClientGetUserDefinedFunctionResponseUserDefinedFunctionTypeDef",
    "ClientGetUserDefinedFunctionResponseTypeDef",
    "ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsResourceUrisTypeDef",
    "ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsTypeDef",
    "ClientGetUserDefinedFunctionsResponseTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphEdgesTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsCrawlsTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphNodesTypeDef",
    "ClientGetWorkflowResponseWorkflowGraphTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphEdgesTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsCrawlsTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunGraphTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunStatisticsTypeDef",
    "ClientGetWorkflowResponseWorkflowLastRunTypeDef",
    "ClientGetWorkflowResponseWorkflowTypeDef",
    "ClientGetWorkflowResponseTypeDef",
    "ClientGetWorkflowRunPropertiesResponseTypeDef",
    "ClientGetWorkflowRunResponseRunGraphEdgesTypeDef",
    "ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsCrawlsTypeDef",
    "ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsTypeDef",
    "ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    "ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    "ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsTypeDef",
    "ClientGetWorkflowRunResponseRunGraphNodesJobDetailsTypeDef",
    "ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    "ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsTypeDef",
    "ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    "ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    "ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerTypeDef",
    "ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTypeDef",
    "ClientGetWorkflowRunResponseRunGraphNodesTypeDef",
    "ClientGetWorkflowRunResponseRunGraphTypeDef",
    "ClientGetWorkflowRunResponseRunStatisticsTypeDef",
    "ClientGetWorkflowRunResponseRunTypeDef",
    "ClientGetWorkflowRunResponseTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphEdgesTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsCrawlsTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphNodesTypeDef",
    "ClientGetWorkflowRunsResponseRunsGraphTypeDef",
    "ClientGetWorkflowRunsResponseRunsStatisticsTypeDef",
    "ClientGetWorkflowRunsResponseRunsTypeDef",
    "ClientGetWorkflowRunsResponseTypeDef",
    "ClientListCrawlersResponseTypeDef",
    "ClientListDevEndpointsResponseTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientListTriggersResponseTypeDef",
    "ClientListWorkflowsResponseTypeDef",
    "ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef",
    "ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef",
    "ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsTypeDef",
    "ClientPutResourcePolicyResponseTypeDef",
    "ClientResetJobBookmarkResponseJobBookmarkEntryTypeDef",
    "ClientResetJobBookmarkResponseTypeDef",
    "ClientSearchTablesFiltersTypeDef",
    "ClientSearchTablesResponseTableListPartitionKeysTypeDef",
    "ClientSearchTablesResponseTableListStorageDescriptorColumnsTypeDef",
    "ClientSearchTablesResponseTableListStorageDescriptorSerdeInfoTypeDef",
    "ClientSearchTablesResponseTableListStorageDescriptorSkewedInfoTypeDef",
    "ClientSearchTablesResponseTableListStorageDescriptorSortColumnsTypeDef",
    "ClientSearchTablesResponseTableListStorageDescriptorTypeDef",
    "ClientSearchTablesResponseTableListTypeDef",
    "ClientSearchTablesResponseTypeDef",
    "ClientSearchTablesSortCriteriaTypeDef",
    "ClientStartExportLabelsTaskRunResponseTypeDef",
    "ClientStartImportLabelsTaskRunResponseTypeDef",
    "ClientStartJobRunNotificationPropertyTypeDef",
    "ClientStartJobRunResponseTypeDef",
    "ClientStartMlEvaluationTaskRunResponseTypeDef",
    "ClientStartMlLabelingSetGenerationTaskRunResponseTypeDef",
    "ClientStartTriggerResponseTypeDef",
    "ClientStartWorkflowRunResponseTypeDef",
    "ClientStopTriggerResponseTypeDef",
    "ClientUpdateClassifierCsvClassifierTypeDef",
    "ClientUpdateClassifierGrokClassifierTypeDef",
    "ClientUpdateClassifierJsonClassifierTypeDef",
    "ClientUpdateClassifierXMLClassifierTypeDef",
    "ClientUpdateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef",
    "ClientUpdateConnectionConnectionInputTypeDef",
    "ClientUpdateCrawlerSchemaChangePolicyTypeDef",
    "ClientUpdateCrawlerTargetsCatalogTargetsTypeDef",
    "ClientUpdateCrawlerTargetsDynamoDBTargetsTypeDef",
    "ClientUpdateCrawlerTargetsJdbcTargetsTypeDef",
    "ClientUpdateCrawlerTargetsS3TargetsTypeDef",
    "ClientUpdateCrawlerTargetsTypeDef",
    "ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef",
    "ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef",
    "ClientUpdateDatabaseDatabaseInputTypeDef",
    "ClientUpdateDevEndpointCustomLibrariesTypeDef",
    "ClientUpdateJobJobUpdateCommandTypeDef",
    "ClientUpdateJobJobUpdateConnectionsTypeDef",
    "ClientUpdateJobJobUpdateExecutionPropertyTypeDef",
    "ClientUpdateJobJobUpdateNotificationPropertyTypeDef",
    "ClientUpdateJobJobUpdateTypeDef",
    "ClientUpdateJobResponseTypeDef",
    "ClientUpdateMlTransformParametersFindMatchesParametersTypeDef",
    "ClientUpdateMlTransformParametersTypeDef",
    "ClientUpdateMlTransformResponseTypeDef",
    "ClientUpdatePartitionPartitionInputStorageDescriptorColumnsTypeDef",
    "ClientUpdatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef",
    "ClientUpdatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef",
    "ClientUpdatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef",
    "ClientUpdatePartitionPartitionInputStorageDescriptorTypeDef",
    "ClientUpdatePartitionPartitionInputTypeDef",
    "ClientUpdateTableTableInputPartitionKeysTypeDef",
    "ClientUpdateTableTableInputStorageDescriptorColumnsTypeDef",
    "ClientUpdateTableTableInputStorageDescriptorSerdeInfoTypeDef",
    "ClientUpdateTableTableInputStorageDescriptorSkewedInfoTypeDef",
    "ClientUpdateTableTableInputStorageDescriptorSortColumnsTypeDef",
    "ClientUpdateTableTableInputStorageDescriptorTypeDef",
    "ClientUpdateTableTableInputTypeDef",
    "ClientUpdateTriggerResponseTriggerActionsNotificationPropertyTypeDef",
    "ClientUpdateTriggerResponseTriggerActionsTypeDef",
    "ClientUpdateTriggerResponseTriggerPredicateConditionsTypeDef",
    "ClientUpdateTriggerResponseTriggerPredicateTypeDef",
    "ClientUpdateTriggerResponseTriggerTypeDef",
    "ClientUpdateTriggerResponseTypeDef",
    "ClientUpdateTriggerTriggerUpdateActionsNotificationPropertyTypeDef",
    "ClientUpdateTriggerTriggerUpdateActionsTypeDef",
    "ClientUpdateTriggerTriggerUpdatePredicateConditionsTypeDef",
    "ClientUpdateTriggerTriggerUpdatePredicateTypeDef",
    "ClientUpdateTriggerTriggerUpdateTypeDef",
    "ClientUpdateUserDefinedFunctionFunctionInputResourceUrisTypeDef",
    "ClientUpdateUserDefinedFunctionFunctionInputTypeDef",
    "ClientUpdateWorkflowResponseTypeDef",
    "GetClassifiersPaginatePaginationConfigTypeDef",
    "GetClassifiersPaginateResponseClassifiersCsvClassifierTypeDef",
    "GetClassifiersPaginateResponseClassifiersGrokClassifierTypeDef",
    "GetClassifiersPaginateResponseClassifiersJsonClassifierTypeDef",
    "GetClassifiersPaginateResponseClassifiersXMLClassifierTypeDef",
    "GetClassifiersPaginateResponseClassifiersTypeDef",
    "GetClassifiersPaginateResponseTypeDef",
    "GetConnectionsPaginateFilterTypeDef",
    "GetConnectionsPaginatePaginationConfigTypeDef",
    "GetConnectionsPaginateResponseConnectionListPhysicalConnectionRequirementsTypeDef",
    "GetConnectionsPaginateResponseConnectionListTypeDef",
    "GetConnectionsPaginateResponseTypeDef",
    "GetCrawlerMetricsPaginatePaginationConfigTypeDef",
    "GetCrawlerMetricsPaginateResponseCrawlerMetricsListTypeDef",
    "GetCrawlerMetricsPaginateResponseTypeDef",
    "GetCrawlersPaginatePaginationConfigTypeDef",
    "GetCrawlersPaginateResponseCrawlersLastCrawlTypeDef",
    "GetCrawlersPaginateResponseCrawlersScheduleTypeDef",
    "GetCrawlersPaginateResponseCrawlersSchemaChangePolicyTypeDef",
    "GetCrawlersPaginateResponseCrawlersTargetsCatalogTargetsTypeDef",
    "GetCrawlersPaginateResponseCrawlersTargetsDynamoDBTargetsTypeDef",
    "GetCrawlersPaginateResponseCrawlersTargetsJdbcTargetsTypeDef",
    "GetCrawlersPaginateResponseCrawlersTargetsS3TargetsTypeDef",
    "GetCrawlersPaginateResponseCrawlersTargetsTypeDef",
    "GetCrawlersPaginateResponseCrawlersTypeDef",
    "GetCrawlersPaginateResponseTypeDef",
    "GetDatabasesPaginatePaginationConfigTypeDef",
    "GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef",
    "GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsTypeDef",
    "GetDatabasesPaginateResponseDatabaseListTypeDef",
    "GetDatabasesPaginateResponseTypeDef",
    "GetDevEndpointsPaginatePaginationConfigTypeDef",
    "GetDevEndpointsPaginateResponseDevEndpointsTypeDef",
    "GetDevEndpointsPaginateResponseTypeDef",
    "GetJobRunsPaginatePaginationConfigTypeDef",
    "GetJobRunsPaginateResponseJobRunsNotificationPropertyTypeDef",
    "GetJobRunsPaginateResponseJobRunsPredecessorRunsTypeDef",
    "GetJobRunsPaginateResponseJobRunsTypeDef",
    "GetJobRunsPaginateResponseTypeDef",
    "GetJobsPaginatePaginationConfigTypeDef",
    "GetJobsPaginateResponseJobsCommandTypeDef",
    "GetJobsPaginateResponseJobsConnectionsTypeDef",
    "GetJobsPaginateResponseJobsExecutionPropertyTypeDef",
    "GetJobsPaginateResponseJobsNotificationPropertyTypeDef",
    "GetJobsPaginateResponseJobsTypeDef",
    "GetJobsPaginateResponseTypeDef",
    "GetPartitionsPaginatePaginationConfigTypeDef",
    "GetPartitionsPaginateResponsePartitionsStorageDescriptorColumnsTypeDef",
    "GetPartitionsPaginateResponsePartitionsStorageDescriptorSerdeInfoTypeDef",
    "GetPartitionsPaginateResponsePartitionsStorageDescriptorSkewedInfoTypeDef",
    "GetPartitionsPaginateResponsePartitionsStorageDescriptorSortColumnsTypeDef",
    "GetPartitionsPaginateResponsePartitionsStorageDescriptorTypeDef",
    "GetPartitionsPaginateResponsePartitionsTypeDef",
    "GetPartitionsPaginateResponseTypeDef",
    "GetPartitionsPaginateSegmentTypeDef",
    "GetSecurityConfigurationsPaginatePaginationConfigTypeDef",
    "GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef",
    "GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef",
    "GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef",
    "GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationTypeDef",
    "GetSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef",
    "GetSecurityConfigurationsPaginateResponseTypeDef",
    "GetTableVersionsPaginatePaginationConfigTypeDef",
    "GetTableVersionsPaginateResponseTableVersionsTablePartitionKeysTypeDef",
    "GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorColumnsTypeDef",
    "GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef",
    "GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef",
    "GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef",
    "GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorTypeDef",
    "GetTableVersionsPaginateResponseTableVersionsTableTypeDef",
    "GetTableVersionsPaginateResponseTableVersionsTypeDef",
    "GetTableVersionsPaginateResponseTypeDef",
    "GetTablesPaginatePaginationConfigTypeDef",
    "GetTablesPaginateResponseTableListPartitionKeysTypeDef",
    "GetTablesPaginateResponseTableListStorageDescriptorColumnsTypeDef",
    "GetTablesPaginateResponseTableListStorageDescriptorSerdeInfoTypeDef",
    "GetTablesPaginateResponseTableListStorageDescriptorSkewedInfoTypeDef",
    "GetTablesPaginateResponseTableListStorageDescriptorSortColumnsTypeDef",
    "GetTablesPaginateResponseTableListStorageDescriptorTypeDef",
    "GetTablesPaginateResponseTableListTypeDef",
    "GetTablesPaginateResponseTypeDef",
    "GetTriggersPaginatePaginationConfigTypeDef",
    "GetTriggersPaginateResponseTriggersActionsNotificationPropertyTypeDef",
    "GetTriggersPaginateResponseTriggersActionsTypeDef",
    "GetTriggersPaginateResponseTriggersPredicateConditionsTypeDef",
    "GetTriggersPaginateResponseTriggersPredicateTypeDef",
    "GetTriggersPaginateResponseTriggersTypeDef",
    "GetTriggersPaginateResponseTypeDef",
    "GetUserDefinedFunctionsPaginatePaginationConfigTypeDef",
    "GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsResourceUrisTypeDef",
    "GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsTypeDef",
    "GetUserDefinedFunctionsPaginateResponseTypeDef",
)


_ClientBatchCreatePartitionPartitionInputListStorageDescriptorColumnsTypeDef = TypedDict(
    "_ClientBatchCreatePartitionPartitionInputListStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientBatchCreatePartitionPartitionInputListStorageDescriptorColumnsTypeDef(
    _ClientBatchCreatePartitionPartitionInputListStorageDescriptorColumnsTypeDef
):
    pass


_ClientBatchCreatePartitionPartitionInputListStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_ClientBatchCreatePartitionPartitionInputListStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientBatchCreatePartitionPartitionInputListStorageDescriptorSerdeInfoTypeDef(
    _ClientBatchCreatePartitionPartitionInputListStorageDescriptorSerdeInfoTypeDef
):
    pass


_ClientBatchCreatePartitionPartitionInputListStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_ClientBatchCreatePartitionPartitionInputListStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class ClientBatchCreatePartitionPartitionInputListStorageDescriptorSkewedInfoTypeDef(
    _ClientBatchCreatePartitionPartitionInputListStorageDescriptorSkewedInfoTypeDef
):
    pass


_ClientBatchCreatePartitionPartitionInputListStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_ClientBatchCreatePartitionPartitionInputListStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class ClientBatchCreatePartitionPartitionInputListStorageDescriptorSortColumnsTypeDef(
    _ClientBatchCreatePartitionPartitionInputListStorageDescriptorSortColumnsTypeDef
):
    pass


_ClientBatchCreatePartitionPartitionInputListStorageDescriptorTypeDef = TypedDict(
    "_ClientBatchCreatePartitionPartitionInputListStorageDescriptorTypeDef",
    {
        "Columns": List[
            ClientBatchCreatePartitionPartitionInputListStorageDescriptorColumnsTypeDef
        ],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientBatchCreatePartitionPartitionInputListStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            ClientBatchCreatePartitionPartitionInputListStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientBatchCreatePartitionPartitionInputListStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class ClientBatchCreatePartitionPartitionInputListStorageDescriptorTypeDef(
    _ClientBatchCreatePartitionPartitionInputListStorageDescriptorTypeDef
):
    pass


_ClientBatchCreatePartitionPartitionInputListTypeDef = TypedDict(
    "_ClientBatchCreatePartitionPartitionInputListTypeDef",
    {
        "Values": List[str],
        "LastAccessTime": datetime,
        "StorageDescriptor": ClientBatchCreatePartitionPartitionInputListStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)


class ClientBatchCreatePartitionPartitionInputListTypeDef(
    _ClientBatchCreatePartitionPartitionInputListTypeDef
):
    """
    - *(dict) --*

      The structure used to create and update a partition.
      - **Values** *(list) --*

        The values of the partition. Although this parameter is not required by the SDK, you must
        specify this parameter for a valid input.
        The values for the keys for the new partition must be passed as an array of String objects
        that must be ordered in the same order as the partition keys appearing in the Amazon S3
        prefix. Otherwise AWS Glue will add the values to the wrong keys.
        - *(string) --*
    """


_ClientBatchCreatePartitionResponseErrorsErrorDetailTypeDef = TypedDict(
    "_ClientBatchCreatePartitionResponseErrorsErrorDetailTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchCreatePartitionResponseErrorsErrorDetailTypeDef(
    _ClientBatchCreatePartitionResponseErrorsErrorDetailTypeDef
):
    pass


_ClientBatchCreatePartitionResponseErrorsTypeDef = TypedDict(
    "_ClientBatchCreatePartitionResponseErrorsTypeDef",
    {
        "PartitionValues": List[str],
        "ErrorDetail": ClientBatchCreatePartitionResponseErrorsErrorDetailTypeDef,
    },
    total=False,
)


class ClientBatchCreatePartitionResponseErrorsTypeDef(
    _ClientBatchCreatePartitionResponseErrorsTypeDef
):
    """
    - *(dict) --*

      Contains information about a partition error.
      - **PartitionValues** *(list) --*

        The values that define the partition.
        - *(string) --*
    """


_ClientBatchCreatePartitionResponseTypeDef = TypedDict(
    "_ClientBatchCreatePartitionResponseTypeDef",
    {"Errors": List[ClientBatchCreatePartitionResponseErrorsTypeDef]},
    total=False,
)


class ClientBatchCreatePartitionResponseTypeDef(_ClientBatchCreatePartitionResponseTypeDef):
    """
    - *(dict) --*

      - **Errors** *(list) --*

        The errors encountered when trying to create the requested partitions.
        - *(dict) --*

          Contains information about a partition error.
          - **PartitionValues** *(list) --*

            The values that define the partition.
            - *(string) --*
    """


_ClientBatchDeleteConnectionResponseErrorsTypeDef = TypedDict(
    "_ClientBatchDeleteConnectionResponseErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDeleteConnectionResponseErrorsTypeDef(
    _ClientBatchDeleteConnectionResponseErrorsTypeDef
):
    pass


_ClientBatchDeleteConnectionResponseTypeDef = TypedDict(
    "_ClientBatchDeleteConnectionResponseTypeDef",
    {"Succeeded": List[str], "Errors": Dict[str, ClientBatchDeleteConnectionResponseErrorsTypeDef]},
    total=False,
)


class ClientBatchDeleteConnectionResponseTypeDef(_ClientBatchDeleteConnectionResponseTypeDef):
    """
    - *(dict) --*

      - **Succeeded** *(list) --*

        A list of names of the connection definitions that were successfully deleted.
        - *(string) --*
    """


_ClientBatchDeletePartitionPartitionsToDeleteTypeDef = TypedDict(
    "_ClientBatchDeletePartitionPartitionsToDeleteTypeDef", {"Values": List[str]}
)


class ClientBatchDeletePartitionPartitionsToDeleteTypeDef(
    _ClientBatchDeletePartitionPartitionsToDeleteTypeDef
):
    """
    - *(dict) --*

      Contains a list of values defining partitions.
      - **Values** *(list) --***[REQUIRED]**

        The list of values.
        - *(string) --*
    """


_ClientBatchDeletePartitionResponseErrorsErrorDetailTypeDef = TypedDict(
    "_ClientBatchDeletePartitionResponseErrorsErrorDetailTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDeletePartitionResponseErrorsErrorDetailTypeDef(
    _ClientBatchDeletePartitionResponseErrorsErrorDetailTypeDef
):
    pass


_ClientBatchDeletePartitionResponseErrorsTypeDef = TypedDict(
    "_ClientBatchDeletePartitionResponseErrorsTypeDef",
    {
        "PartitionValues": List[str],
        "ErrorDetail": ClientBatchDeletePartitionResponseErrorsErrorDetailTypeDef,
    },
    total=False,
)


class ClientBatchDeletePartitionResponseErrorsTypeDef(
    _ClientBatchDeletePartitionResponseErrorsTypeDef
):
    """
    - *(dict) --*

      Contains information about a partition error.
      - **PartitionValues** *(list) --*

        The values that define the partition.
        - *(string) --*
    """


_ClientBatchDeletePartitionResponseTypeDef = TypedDict(
    "_ClientBatchDeletePartitionResponseTypeDef",
    {"Errors": List[ClientBatchDeletePartitionResponseErrorsTypeDef]},
    total=False,
)


class ClientBatchDeletePartitionResponseTypeDef(_ClientBatchDeletePartitionResponseTypeDef):
    """
    - *(dict) --*

      - **Errors** *(list) --*

        The errors encountered when trying to delete the requested partitions.
        - *(dict) --*

          Contains information about a partition error.
          - **PartitionValues** *(list) --*

            The values that define the partition.
            - *(string) --*
    """


_ClientBatchDeleteTableResponseErrorsErrorDetailTypeDef = TypedDict(
    "_ClientBatchDeleteTableResponseErrorsErrorDetailTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDeleteTableResponseErrorsErrorDetailTypeDef(
    _ClientBatchDeleteTableResponseErrorsErrorDetailTypeDef
):
    pass


_ClientBatchDeleteTableResponseErrorsTypeDef = TypedDict(
    "_ClientBatchDeleteTableResponseErrorsTypeDef",
    {"TableName": str, "ErrorDetail": ClientBatchDeleteTableResponseErrorsErrorDetailTypeDef},
    total=False,
)


class ClientBatchDeleteTableResponseErrorsTypeDef(_ClientBatchDeleteTableResponseErrorsTypeDef):
    """
    - *(dict) --*

      An error record for table operations.
      - **TableName** *(string) --*

        The name of the table. For Hive compatibility, this must be entirely lowercase.
    """


_ClientBatchDeleteTableResponseTypeDef = TypedDict(
    "_ClientBatchDeleteTableResponseTypeDef",
    {"Errors": List[ClientBatchDeleteTableResponseErrorsTypeDef]},
    total=False,
)


class ClientBatchDeleteTableResponseTypeDef(_ClientBatchDeleteTableResponseTypeDef):
    """
    - *(dict) --*

      - **Errors** *(list) --*

        A list of errors encountered in attempting to delete the specified tables.
        - *(dict) --*

          An error record for table operations.
          - **TableName** *(string) --*

            The name of the table. For Hive compatibility, this must be entirely lowercase.
    """


_ClientBatchDeleteTableVersionResponseErrorsErrorDetailTypeDef = TypedDict(
    "_ClientBatchDeleteTableVersionResponseErrorsErrorDetailTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDeleteTableVersionResponseErrorsErrorDetailTypeDef(
    _ClientBatchDeleteTableVersionResponseErrorsErrorDetailTypeDef
):
    pass


_ClientBatchDeleteTableVersionResponseErrorsTypeDef = TypedDict(
    "_ClientBatchDeleteTableVersionResponseErrorsTypeDef",
    {
        "TableName": str,
        "VersionId": str,
        "ErrorDetail": ClientBatchDeleteTableVersionResponseErrorsErrorDetailTypeDef,
    },
    total=False,
)


class ClientBatchDeleteTableVersionResponseErrorsTypeDef(
    _ClientBatchDeleteTableVersionResponseErrorsTypeDef
):
    """
    - *(dict) --*

      An error record for table-version operations.
      - **TableName** *(string) --*

        The name of the table in question.
    """


_ClientBatchDeleteTableVersionResponseTypeDef = TypedDict(
    "_ClientBatchDeleteTableVersionResponseTypeDef",
    {"Errors": List[ClientBatchDeleteTableVersionResponseErrorsTypeDef]},
    total=False,
)


class ClientBatchDeleteTableVersionResponseTypeDef(_ClientBatchDeleteTableVersionResponseTypeDef):
    """
    - *(dict) --*

      - **Errors** *(list) --*

        A list of errors encountered while trying to delete the specified table versions.
        - *(dict) --*

          An error record for table-version operations.
          - **TableName** *(string) --*

            The name of the table in question.
    """


_ClientBatchGetCrawlersResponseCrawlersLastCrawlTypeDef = TypedDict(
    "_ClientBatchGetCrawlersResponseCrawlersLastCrawlTypeDef",
    {
        "Status": Literal["SUCCEEDED", "CANCELLED", "FAILED"],
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
        "MessagePrefix": str,
        "StartTime": datetime,
    },
    total=False,
)


class ClientBatchGetCrawlersResponseCrawlersLastCrawlTypeDef(
    _ClientBatchGetCrawlersResponseCrawlersLastCrawlTypeDef
):
    pass


_ClientBatchGetCrawlersResponseCrawlersScheduleTypeDef = TypedDict(
    "_ClientBatchGetCrawlersResponseCrawlersScheduleTypeDef",
    {"ScheduleExpression": str, "State": Literal["SCHEDULED", "NOT_SCHEDULED", "TRANSITIONING"]},
    total=False,
)


class ClientBatchGetCrawlersResponseCrawlersScheduleTypeDef(
    _ClientBatchGetCrawlersResponseCrawlersScheduleTypeDef
):
    pass


_ClientBatchGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef = TypedDict(
    "_ClientBatchGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": Literal["LOG", "UPDATE_IN_DATABASE"],
        "DeleteBehavior": Literal["LOG", "DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE"],
    },
    total=False,
)


class ClientBatchGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef(
    _ClientBatchGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef
):
    pass


_ClientBatchGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef = TypedDict(
    "_ClientBatchGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef",
    {"DatabaseName": str, "Tables": List[str]},
    total=False,
)


class ClientBatchGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef(
    _ClientBatchGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef
):
    pass


_ClientBatchGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef = TypedDict(
    "_ClientBatchGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef",
    {"Path": str},
    total=False,
)


class ClientBatchGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef(
    _ClientBatchGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef
):
    pass


_ClientBatchGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef = TypedDict(
    "_ClientBatchGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef",
    {"ConnectionName": str, "Path": str, "Exclusions": List[str]},
    total=False,
)


class ClientBatchGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef(
    _ClientBatchGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef
):
    pass


_ClientBatchGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef = TypedDict(
    "_ClientBatchGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef",
    {"Path": str, "Exclusions": List[str]},
    total=False,
)


class ClientBatchGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef(
    _ClientBatchGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef
):
    pass


_ClientBatchGetCrawlersResponseCrawlersTargetsTypeDef = TypedDict(
    "_ClientBatchGetCrawlersResponseCrawlersTargetsTypeDef",
    {
        "S3Targets": List[ClientBatchGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef],
        "JdbcTargets": List[ClientBatchGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef],
        "DynamoDBTargets": List[
            ClientBatchGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef
        ],
        "CatalogTargets": List[ClientBatchGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef],
    },
    total=False,
)


class ClientBatchGetCrawlersResponseCrawlersTargetsTypeDef(
    _ClientBatchGetCrawlersResponseCrawlersTargetsTypeDef
):
    pass


_ClientBatchGetCrawlersResponseCrawlersTypeDef = TypedDict(
    "_ClientBatchGetCrawlersResponseCrawlersTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": ClientBatchGetCrawlersResponseCrawlersTargetsTypeDef,
        "DatabaseName": str,
        "Description": str,
        "Classifiers": List[str],
        "SchemaChangePolicy": ClientBatchGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef,
        "State": Literal["READY", "RUNNING", "STOPPING"],
        "TablePrefix": str,
        "Schedule": ClientBatchGetCrawlersResponseCrawlersScheduleTypeDef,
        "CrawlElapsedTime": int,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "LastCrawl": ClientBatchGetCrawlersResponseCrawlersLastCrawlTypeDef,
        "Version": int,
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
    },
    total=False,
)


class ClientBatchGetCrawlersResponseCrawlersTypeDef(_ClientBatchGetCrawlersResponseCrawlersTypeDef):
    """
    - *(dict) --*

      Specifies a crawler program that examines a data source and uses classifiers to try to
      determine its schema. If successful, the crawler records metadata concerning the data source
      in the AWS Glue Data Catalog.
      - **Name** *(string) --*

        The name of the crawler.
    """


_ClientBatchGetCrawlersResponseTypeDef = TypedDict(
    "_ClientBatchGetCrawlersResponseTypeDef",
    {
        "Crawlers": List[ClientBatchGetCrawlersResponseCrawlersTypeDef],
        "CrawlersNotFound": List[str],
    },
    total=False,
)


class ClientBatchGetCrawlersResponseTypeDef(_ClientBatchGetCrawlersResponseTypeDef):
    """
    - *(dict) --*

      - **Crawlers** *(list) --*

        A list of crawler definitions.
        - *(dict) --*

          Specifies a crawler program that examines a data source and uses classifiers to try to
          determine its schema. If successful, the crawler records metadata concerning the data
          source in the AWS Glue Data Catalog.
          - **Name** *(string) --*

            The name of the crawler.
    """


_ClientBatchGetDevEndpointsResponseDevEndpointsTypeDef = TypedDict(
    "_ClientBatchGetDevEndpointsResponseDevEndpointsTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "YarnEndpointAddress": str,
        "PrivateAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "PublicAddress": str,
        "Status": str,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "NumberOfNodes": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "LastUpdateStatus": str,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "PublicKey": str,
        "PublicKeys": List[str],
        "SecurityConfiguration": str,
        "Arguments": Dict[str, str],
    },
    total=False,
)


class ClientBatchGetDevEndpointsResponseDevEndpointsTypeDef(
    _ClientBatchGetDevEndpointsResponseDevEndpointsTypeDef
):
    """
    - *(dict) --*

      A development endpoint where a developer can remotely debug extract, transform, and load (ETL)
      scripts.
      - **EndpointName** *(string) --*

        The name of the ``DevEndpoint`` .
    """


_ClientBatchGetDevEndpointsResponseTypeDef = TypedDict(
    "_ClientBatchGetDevEndpointsResponseTypeDef",
    {
        "DevEndpoints": List[ClientBatchGetDevEndpointsResponseDevEndpointsTypeDef],
        "DevEndpointsNotFound": List[str],
    },
    total=False,
)


class ClientBatchGetDevEndpointsResponseTypeDef(_ClientBatchGetDevEndpointsResponseTypeDef):
    """
    - *(dict) --*

      - **DevEndpoints** *(list) --*

        A list of ``DevEndpoint`` definitions.
        - *(dict) --*

          A development endpoint where a developer can remotely debug extract, transform, and load
          (ETL) scripts.
          - **EndpointName** *(string) --*

            The name of the ``DevEndpoint`` .
    """


_ClientBatchGetJobsResponseJobsCommandTypeDef = TypedDict(
    "_ClientBatchGetJobsResponseJobsCommandTypeDef",
    {"Name": str, "ScriptLocation": str, "PythonVersion": str},
    total=False,
)


class ClientBatchGetJobsResponseJobsCommandTypeDef(_ClientBatchGetJobsResponseJobsCommandTypeDef):
    pass


_ClientBatchGetJobsResponseJobsConnectionsTypeDef = TypedDict(
    "_ClientBatchGetJobsResponseJobsConnectionsTypeDef", {"Connections": List[str]}, total=False
)


class ClientBatchGetJobsResponseJobsConnectionsTypeDef(
    _ClientBatchGetJobsResponseJobsConnectionsTypeDef
):
    pass


_ClientBatchGetJobsResponseJobsExecutionPropertyTypeDef = TypedDict(
    "_ClientBatchGetJobsResponseJobsExecutionPropertyTypeDef",
    {"MaxConcurrentRuns": int},
    total=False,
)


class ClientBatchGetJobsResponseJobsExecutionPropertyTypeDef(
    _ClientBatchGetJobsResponseJobsExecutionPropertyTypeDef
):
    pass


_ClientBatchGetJobsResponseJobsNotificationPropertyTypeDef = TypedDict(
    "_ClientBatchGetJobsResponseJobsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientBatchGetJobsResponseJobsNotificationPropertyTypeDef(
    _ClientBatchGetJobsResponseJobsNotificationPropertyTypeDef
):
    pass


_ClientBatchGetJobsResponseJobsTypeDef = TypedDict(
    "_ClientBatchGetJobsResponseJobsTypeDef",
    {
        "Name": str,
        "Description": str,
        "LogUri": str,
        "Role": str,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "ExecutionProperty": ClientBatchGetJobsResponseJobsExecutionPropertyTypeDef,
        "Command": ClientBatchGetJobsResponseJobsCommandTypeDef,
        "DefaultArguments": Dict[str, str],
        "Connections": ClientBatchGetJobsResponseJobsConnectionsTypeDef,
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientBatchGetJobsResponseJobsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class ClientBatchGetJobsResponseJobsTypeDef(_ClientBatchGetJobsResponseJobsTypeDef):
    """
    - *(dict) --*

      Specifies a job definition.
      - **Name** *(string) --*

        The name you assign to this job definition.
    """


_ClientBatchGetJobsResponseTypeDef = TypedDict(
    "_ClientBatchGetJobsResponseTypeDef",
    {"Jobs": List[ClientBatchGetJobsResponseJobsTypeDef], "JobsNotFound": List[str]},
    total=False,
)


class ClientBatchGetJobsResponseTypeDef(_ClientBatchGetJobsResponseTypeDef):
    """
    - *(dict) --*

      - **Jobs** *(list) --*

        A list of job definitions.
        - *(dict) --*

          Specifies a job definition.
          - **Name** *(string) --*

            The name you assign to this job definition.
    """


_ClientBatchGetPartitionPartitionsToGetTypeDef = TypedDict(
    "_ClientBatchGetPartitionPartitionsToGetTypeDef", {"Values": List[str]}
)


class ClientBatchGetPartitionPartitionsToGetTypeDef(_ClientBatchGetPartitionPartitionsToGetTypeDef):
    """
    - *(dict) --*

      Contains a list of values defining partitions.
      - **Values** *(list) --***[REQUIRED]**

        The list of values.
        - *(string) --*
    """


_ClientBatchGetPartitionResponsePartitionsStorageDescriptorColumnsTypeDef = TypedDict(
    "_ClientBatchGetPartitionResponsePartitionsStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientBatchGetPartitionResponsePartitionsStorageDescriptorColumnsTypeDef(
    _ClientBatchGetPartitionResponsePartitionsStorageDescriptorColumnsTypeDef
):
    pass


_ClientBatchGetPartitionResponsePartitionsStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_ClientBatchGetPartitionResponsePartitionsStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientBatchGetPartitionResponsePartitionsStorageDescriptorSerdeInfoTypeDef(
    _ClientBatchGetPartitionResponsePartitionsStorageDescriptorSerdeInfoTypeDef
):
    pass


_ClientBatchGetPartitionResponsePartitionsStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_ClientBatchGetPartitionResponsePartitionsStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class ClientBatchGetPartitionResponsePartitionsStorageDescriptorSkewedInfoTypeDef(
    _ClientBatchGetPartitionResponsePartitionsStorageDescriptorSkewedInfoTypeDef
):
    pass


_ClientBatchGetPartitionResponsePartitionsStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_ClientBatchGetPartitionResponsePartitionsStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class ClientBatchGetPartitionResponsePartitionsStorageDescriptorSortColumnsTypeDef(
    _ClientBatchGetPartitionResponsePartitionsStorageDescriptorSortColumnsTypeDef
):
    pass


_ClientBatchGetPartitionResponsePartitionsStorageDescriptorTypeDef = TypedDict(
    "_ClientBatchGetPartitionResponsePartitionsStorageDescriptorTypeDef",
    {
        "Columns": List[ClientBatchGetPartitionResponsePartitionsStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientBatchGetPartitionResponsePartitionsStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            ClientBatchGetPartitionResponsePartitionsStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientBatchGetPartitionResponsePartitionsStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class ClientBatchGetPartitionResponsePartitionsStorageDescriptorTypeDef(
    _ClientBatchGetPartitionResponsePartitionsStorageDescriptorTypeDef
):
    pass


_ClientBatchGetPartitionResponsePartitionsTypeDef = TypedDict(
    "_ClientBatchGetPartitionResponsePartitionsTypeDef",
    {
        "Values": List[str],
        "DatabaseName": str,
        "TableName": str,
        "CreationTime": datetime,
        "LastAccessTime": datetime,
        "StorageDescriptor": ClientBatchGetPartitionResponsePartitionsStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)


class ClientBatchGetPartitionResponsePartitionsTypeDef(
    _ClientBatchGetPartitionResponsePartitionsTypeDef
):
    """
    - *(dict) --*

      Represents a slice of table data.
      - **Values** *(list) --*

        The values of the partition.
        - *(string) --*
    """


_ClientBatchGetPartitionResponseUnprocessedKeysTypeDef = TypedDict(
    "_ClientBatchGetPartitionResponseUnprocessedKeysTypeDef", {"Values": List[str]}, total=False
)


class ClientBatchGetPartitionResponseUnprocessedKeysTypeDef(
    _ClientBatchGetPartitionResponseUnprocessedKeysTypeDef
):
    pass


_ClientBatchGetPartitionResponseTypeDef = TypedDict(
    "_ClientBatchGetPartitionResponseTypeDef",
    {
        "Partitions": List[ClientBatchGetPartitionResponsePartitionsTypeDef],
        "UnprocessedKeys": List[ClientBatchGetPartitionResponseUnprocessedKeysTypeDef],
    },
    total=False,
)


class ClientBatchGetPartitionResponseTypeDef(_ClientBatchGetPartitionResponseTypeDef):
    """
    - *(dict) --*

      - **Partitions** *(list) --*

        A list of the requested partitions.
        - *(dict) --*

          Represents a slice of table data.
          - **Values** *(list) --*

            The values of the partition.
            - *(string) --*
    """


_ClientBatchGetTriggersResponseTriggersActionsNotificationPropertyTypeDef = TypedDict(
    "_ClientBatchGetTriggersResponseTriggersActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientBatchGetTriggersResponseTriggersActionsNotificationPropertyTypeDef(
    _ClientBatchGetTriggersResponseTriggersActionsNotificationPropertyTypeDef
):
    pass


_ClientBatchGetTriggersResponseTriggersActionsTypeDef = TypedDict(
    "_ClientBatchGetTriggersResponseTriggersActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientBatchGetTriggersResponseTriggersActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)


class ClientBatchGetTriggersResponseTriggersActionsTypeDef(
    _ClientBatchGetTriggersResponseTriggersActionsTypeDef
):
    pass


_ClientBatchGetTriggersResponseTriggersPredicateConditionsTypeDef = TypedDict(
    "_ClientBatchGetTriggersResponseTriggersPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)


class ClientBatchGetTriggersResponseTriggersPredicateConditionsTypeDef(
    _ClientBatchGetTriggersResponseTriggersPredicateConditionsTypeDef
):
    pass


_ClientBatchGetTriggersResponseTriggersPredicateTypeDef = TypedDict(
    "_ClientBatchGetTriggersResponseTriggersPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[ClientBatchGetTriggersResponseTriggersPredicateConditionsTypeDef],
    },
    total=False,
)


class ClientBatchGetTriggersResponseTriggersPredicateTypeDef(
    _ClientBatchGetTriggersResponseTriggersPredicateTypeDef
):
    pass


_ClientBatchGetTriggersResponseTriggersTypeDef = TypedDict(
    "_ClientBatchGetTriggersResponseTriggersTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[ClientBatchGetTriggersResponseTriggersActionsTypeDef],
        "Predicate": ClientBatchGetTriggersResponseTriggersPredicateTypeDef,
    },
    total=False,
)


class ClientBatchGetTriggersResponseTriggersTypeDef(_ClientBatchGetTriggersResponseTriggersTypeDef):
    """
    - *(dict) --*

      Information about a specific trigger.
      - **Name** *(string) --*

        The name of the trigger.
    """


_ClientBatchGetTriggersResponseTypeDef = TypedDict(
    "_ClientBatchGetTriggersResponseTypeDef",
    {
        "Triggers": List[ClientBatchGetTriggersResponseTriggersTypeDef],
        "TriggersNotFound": List[str],
    },
    total=False,
)


class ClientBatchGetTriggersResponseTypeDef(_ClientBatchGetTriggersResponseTypeDef):
    """
    - *(dict) --*

      - **Triggers** *(list) --*

        A list of trigger definitions.
        - *(dict) --*

          Information about a specific trigger.
          - **Name** *(string) --*

            The name of the trigger.
    """


_ClientBatchGetWorkflowsResponseWorkflowsGraphEdgesTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphEdgesTypeDef",
    {"SourceId": str, "DestinationId": str},
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphEdgesTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphEdgesTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsCrawlsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsCrawlsTypeDef",
    {
        "State": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsCrawlsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsCrawlsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsTypeDef",
    {"Crawls": List[ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsCrawlsTypeDef]},
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[
            ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
        ],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsTypeDef",
    {"JobRuns": List[ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsTypeDef]},
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[
            ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[
            ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsTypeDef
        ],
        "Predicate": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateTypeDef,
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTypeDef",
    {"Trigger": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerTypeDef},
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTypeDef",
    {
        "Type": Literal["CRAWLER", "JOB", "TRIGGER"],
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTypeDef,
        "JobDetails": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsTypeDef,
        "CrawlerDetails": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsTypeDef,
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsGraphTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsGraphTypeDef",
    {
        "Nodes": List[ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTypeDef],
        "Edges": List[ClientBatchGetWorkflowsResponseWorkflowsGraphEdgesTypeDef],
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsGraphTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsGraphTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphEdgesTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphEdgesTypeDef",
    {"SourceId": str, "DestinationId": str},
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphEdgesTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphEdgesTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsCrawlsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsCrawlsTypeDef",
    {
        "State": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsCrawlsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsCrawlsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsTypeDef",
    {
        "Crawls": List[
            ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsCrawlsTypeDef
        ]
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[
            ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
        ],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsTypeDef",
    {
        "JobRuns": List[
            ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsTypeDef
        ]
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[
            ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[
            ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef
        ],
        "Predicate": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef,
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTypeDef",
    {
        "Trigger": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerTypeDef
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTypeDef",
    {
        "Type": Literal["CRAWLER", "JOB", "TRIGGER"],
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTypeDef,
        "JobDetails": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsTypeDef,
        "CrawlerDetails": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsTypeDef,
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphTypeDef",
    {
        "Nodes": List[ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTypeDef],
        "Edges": List[ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphEdgesTypeDef],
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunStatisticsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunStatisticsTypeDef",
    {
        "TotalActions": int,
        "TimeoutActions": int,
        "FailedActions": int,
        "StoppedActions": int,
        "SucceededActions": int,
        "RunningActions": int,
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunStatisticsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunStatisticsTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsLastRunTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsLastRunTypeDef",
    {
        "Name": str,
        "WorkflowRunId": str,
        "WorkflowRunProperties": Dict[str, str],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "Status": Literal["RUNNING", "COMPLETED"],
        "Statistics": ClientBatchGetWorkflowsResponseWorkflowsLastRunStatisticsTypeDef,
        "Graph": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphTypeDef,
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsLastRunTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsLastRunTypeDef
):
    pass


_ClientBatchGetWorkflowsResponseWorkflowsTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseWorkflowsTypeDef",
    {
        "Name": str,
        "Description": str,
        "DefaultRunProperties": Dict[str, str],
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "LastRun": ClientBatchGetWorkflowsResponseWorkflowsLastRunTypeDef,
        "Graph": ClientBatchGetWorkflowsResponseWorkflowsGraphTypeDef,
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseWorkflowsTypeDef(
    _ClientBatchGetWorkflowsResponseWorkflowsTypeDef
):
    """
    - *(dict) --*

      A workflow represents a flow in which AWS Glue components should be executed to complete a
      logical task.
      - **Name** *(string) --*

        The name of the workflow representing the flow.
    """


_ClientBatchGetWorkflowsResponseTypeDef = TypedDict(
    "_ClientBatchGetWorkflowsResponseTypeDef",
    {
        "Workflows": List[ClientBatchGetWorkflowsResponseWorkflowsTypeDef],
        "MissingWorkflows": List[str],
    },
    total=False,
)


class ClientBatchGetWorkflowsResponseTypeDef(_ClientBatchGetWorkflowsResponseTypeDef):
    """
    - *(dict) --*

      - **Workflows** *(list) --*

        A list of workflow resource metadata.
        - *(dict) --*

          A workflow represents a flow in which AWS Glue components should be executed to complete a
          logical task.
          - **Name** *(string) --*

            The name of the workflow representing the flow.
    """


_ClientBatchStopJobRunResponseErrorsErrorDetailTypeDef = TypedDict(
    "_ClientBatchStopJobRunResponseErrorsErrorDetailTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchStopJobRunResponseErrorsErrorDetailTypeDef(
    _ClientBatchStopJobRunResponseErrorsErrorDetailTypeDef
):
    pass


_ClientBatchStopJobRunResponseErrorsTypeDef = TypedDict(
    "_ClientBatchStopJobRunResponseErrorsTypeDef",
    {
        "JobName": str,
        "JobRunId": str,
        "ErrorDetail": ClientBatchStopJobRunResponseErrorsErrorDetailTypeDef,
    },
    total=False,
)


class ClientBatchStopJobRunResponseErrorsTypeDef(_ClientBatchStopJobRunResponseErrorsTypeDef):
    pass


_ClientBatchStopJobRunResponseSuccessfulSubmissionsTypeDef = TypedDict(
    "_ClientBatchStopJobRunResponseSuccessfulSubmissionsTypeDef",
    {"JobName": str, "JobRunId": str},
    total=False,
)


class ClientBatchStopJobRunResponseSuccessfulSubmissionsTypeDef(
    _ClientBatchStopJobRunResponseSuccessfulSubmissionsTypeDef
):
    """
    - *(dict) --*

      Records a successful request to stop a specified ``JobRun`` .
      - **JobName** *(string) --*

        The name of the job definition used in the job run that was stopped.
    """


_ClientBatchStopJobRunResponseTypeDef = TypedDict(
    "_ClientBatchStopJobRunResponseTypeDef",
    {
        "SuccessfulSubmissions": List[ClientBatchStopJobRunResponseSuccessfulSubmissionsTypeDef],
        "Errors": List[ClientBatchStopJobRunResponseErrorsTypeDef],
    },
    total=False,
)


class ClientBatchStopJobRunResponseTypeDef(_ClientBatchStopJobRunResponseTypeDef):
    """
    - *(dict) --*

      - **SuccessfulSubmissions** *(list) --*

        A list of the JobRuns that were successfully submitted for stopping.
        - *(dict) --*

          Records a successful request to stop a specified ``JobRun`` .
          - **JobName** *(string) --*

            The name of the job definition used in the job run that was stopped.
    """


_ClientCancelMlTaskRunResponseTypeDef = TypedDict(
    "_ClientCancelMlTaskRunResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
    },
    total=False,
)


class ClientCancelMlTaskRunResponseTypeDef(_ClientCancelMlTaskRunResponseTypeDef):
    """
    - *(dict) --*

      - **TransformId** *(string) --*

        The unique identifier of the machine learning transform.
    """


_RequiredClientCreateClassifierCsvClassifierTypeDef = TypedDict(
    "_RequiredClientCreateClassifierCsvClassifierTypeDef", {"Name": str}
)
_OptionalClientCreateClassifierCsvClassifierTypeDef = TypedDict(
    "_OptionalClientCreateClassifierCsvClassifierTypeDef",
    {
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": Literal["UNKNOWN", "PRESENT", "ABSENT"],
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)


class ClientCreateClassifierCsvClassifierTypeDef(
    _RequiredClientCreateClassifierCsvClassifierTypeDef,
    _OptionalClientCreateClassifierCsvClassifierTypeDef,
):
    """
    A ``CsvClassifier`` object specifying the classifier to create.
    - **Name** *(string) --***[REQUIRED]**

      The name of the classifier.
    """


_RequiredClientCreateClassifierGrokClassifierTypeDef = TypedDict(
    "_RequiredClientCreateClassifierGrokClassifierTypeDef", {"Classification": str}
)
_OptionalClientCreateClassifierGrokClassifierTypeDef = TypedDict(
    "_OptionalClientCreateClassifierGrokClassifierTypeDef",
    {"Name": str, "GrokPattern": str, "CustomPatterns": str},
    total=False,
)


class ClientCreateClassifierGrokClassifierTypeDef(
    _RequiredClientCreateClassifierGrokClassifierTypeDef,
    _OptionalClientCreateClassifierGrokClassifierTypeDef,
):
    """
    A ``GrokClassifier`` object specifying the classifier to create.
    - **Classification** *(string) --***[REQUIRED]**

      An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture
      logs, Amazon CloudWatch Logs, and so on.
    """


_RequiredClientCreateClassifierJsonClassifierTypeDef = TypedDict(
    "_RequiredClientCreateClassifierJsonClassifierTypeDef", {"Name": str}
)
_OptionalClientCreateClassifierJsonClassifierTypeDef = TypedDict(
    "_OptionalClientCreateClassifierJsonClassifierTypeDef", {"JsonPath": str}, total=False
)


class ClientCreateClassifierJsonClassifierTypeDef(
    _RequiredClientCreateClassifierJsonClassifierTypeDef,
    _OptionalClientCreateClassifierJsonClassifierTypeDef,
):
    """
    A ``JsonClassifier`` object specifying the classifier to create.
    - **Name** *(string) --***[REQUIRED]**

      The name of the classifier.
    """


_RequiredClientCreateClassifierXMLClassifierTypeDef = TypedDict(
    "_RequiredClientCreateClassifierXMLClassifierTypeDef", {"Classification": str}
)
_OptionalClientCreateClassifierXMLClassifierTypeDef = TypedDict(
    "_OptionalClientCreateClassifierXMLClassifierTypeDef", {"Name": str, "RowTag": str}, total=False
)


class ClientCreateClassifierXMLClassifierTypeDef(
    _RequiredClientCreateClassifierXMLClassifierTypeDef,
    _OptionalClientCreateClassifierXMLClassifierTypeDef,
):
    """
    An ``XMLClassifier`` object specifying the classifier to create.
    - **Classification** *(string) --***[REQUIRED]**

      An identifier of the data format that the classifier matches.
    """


_ClientCreateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef = TypedDict(
    "_ClientCreateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef",
    {"SubnetId": str, "SecurityGroupIdList": List[str], "AvailabilityZone": str},
    total=False,
)


class ClientCreateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef(
    _ClientCreateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef
):
    pass


_RequiredClientCreateConnectionConnectionInputTypeDef = TypedDict(
    "_RequiredClientCreateConnectionConnectionInputTypeDef", {"Name": str}
)
_OptionalClientCreateConnectionConnectionInputTypeDef = TypedDict(
    "_OptionalClientCreateConnectionConnectionInputTypeDef",
    {
        "Description": str,
        "ConnectionType": Literal["JDBC", "SFTP"],
        "MatchCriteria": List[str],
        "ConnectionProperties": Dict[str, str],
        "PhysicalConnectionRequirements": ClientCreateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef,
    },
    total=False,
)


class ClientCreateConnectionConnectionInputTypeDef(
    _RequiredClientCreateConnectionConnectionInputTypeDef,
    _OptionalClientCreateConnectionConnectionInputTypeDef,
):
    """
    A ``ConnectionInput`` object defining the connection to create.
    - **Name** *(string) --***[REQUIRED]**

      The name of the connection.
    """


_ClientCreateCrawlerSchemaChangePolicyTypeDef = TypedDict(
    "_ClientCreateCrawlerSchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": Literal["LOG", "UPDATE_IN_DATABASE"],
        "DeleteBehavior": Literal["LOG", "DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE"],
    },
    total=False,
)


class ClientCreateCrawlerSchemaChangePolicyTypeDef(_ClientCreateCrawlerSchemaChangePolicyTypeDef):
    """
    The policy for the crawler's update and deletion behavior.
    - **UpdateBehavior** *(string) --*

      The update behavior when the crawler finds a changed schema.
    """


_ClientCreateCrawlerTargetsCatalogTargetsTypeDef = TypedDict(
    "_ClientCreateCrawlerTargetsCatalogTargetsTypeDef",
    {"DatabaseName": str, "Tables": List[str]},
    total=False,
)


class ClientCreateCrawlerTargetsCatalogTargetsTypeDef(
    _ClientCreateCrawlerTargetsCatalogTargetsTypeDef
):
    pass


_ClientCreateCrawlerTargetsDynamoDBTargetsTypeDef = TypedDict(
    "_ClientCreateCrawlerTargetsDynamoDBTargetsTypeDef", {"Path": str}, total=False
)


class ClientCreateCrawlerTargetsDynamoDBTargetsTypeDef(
    _ClientCreateCrawlerTargetsDynamoDBTargetsTypeDef
):
    pass


_ClientCreateCrawlerTargetsJdbcTargetsTypeDef = TypedDict(
    "_ClientCreateCrawlerTargetsJdbcTargetsTypeDef",
    {"ConnectionName": str, "Path": str, "Exclusions": List[str]},
    total=False,
)


class ClientCreateCrawlerTargetsJdbcTargetsTypeDef(_ClientCreateCrawlerTargetsJdbcTargetsTypeDef):
    pass


_ClientCreateCrawlerTargetsS3TargetsTypeDef = TypedDict(
    "_ClientCreateCrawlerTargetsS3TargetsTypeDef",
    {"Path": str, "Exclusions": List[str]},
    total=False,
)


class ClientCreateCrawlerTargetsS3TargetsTypeDef(_ClientCreateCrawlerTargetsS3TargetsTypeDef):
    """
    - *(dict) --*

      Specifies a data store in Amazon Simple Storage Service (Amazon S3).
      - **Path** *(string) --*

        The path to the Amazon S3 target.
    """


_ClientCreateCrawlerTargetsTypeDef = TypedDict(
    "_ClientCreateCrawlerTargetsTypeDef",
    {
        "S3Targets": List[ClientCreateCrawlerTargetsS3TargetsTypeDef],
        "JdbcTargets": List[ClientCreateCrawlerTargetsJdbcTargetsTypeDef],
        "DynamoDBTargets": List[ClientCreateCrawlerTargetsDynamoDBTargetsTypeDef],
        "CatalogTargets": List[ClientCreateCrawlerTargetsCatalogTargetsTypeDef],
    },
    total=False,
)


class ClientCreateCrawlerTargetsTypeDef(_ClientCreateCrawlerTargetsTypeDef):
    """
    A list of collection of targets to crawl.
    - **S3Targets** *(list) --*

      Specifies Amazon Simple Storage Service (Amazon S3) targets.
      - *(dict) --*

        Specifies a data store in Amazon Simple Storage Service (Amazon S3).
        - **Path** *(string) --*

          The path to the Amazon S3 target.
    """


_ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "_ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef(
    _ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef
):
    pass


_ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef = TypedDict(
    "_ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef(
    _ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef
):
    pass


_RequiredClientCreateDatabaseDatabaseInputTypeDef = TypedDict(
    "_RequiredClientCreateDatabaseDatabaseInputTypeDef", {"Name": str}
)
_OptionalClientCreateDatabaseDatabaseInputTypeDef = TypedDict(
    "_OptionalClientCreateDatabaseDatabaseInputTypeDef",
    {
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTableDefaultPermissions": List[
            ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDatabaseDatabaseInputTypeDef(
    _RequiredClientCreateDatabaseDatabaseInputTypeDef,
    _OptionalClientCreateDatabaseDatabaseInputTypeDef,
):
    """
    The metadata for the database.
    - **Name** *(string) --***[REQUIRED]**

      The name of the database. For Hive compatibility, this is folded to lowercase when it is
      stored.
    """


_ClientCreateDevEndpointResponseTypeDef = TypedDict(
    "_ClientCreateDevEndpointResponseTypeDef",
    {
        "EndpointName": str,
        "Status": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "RoleArn": str,
        "YarnEndpointAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "NumberOfNodes": int,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "SecurityConfiguration": str,
        "CreatedTimestamp": datetime,
        "Arguments": Dict[str, str],
    },
    total=False,
)


class ClientCreateDevEndpointResponseTypeDef(_ClientCreateDevEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointName** *(string) --*

        The name assigned to the new ``DevEndpoint`` .
    """


_ClientCreateJobCommandTypeDef = TypedDict(
    "_ClientCreateJobCommandTypeDef",
    {"Name": str, "ScriptLocation": str, "PythonVersion": str},
    total=False,
)


class ClientCreateJobCommandTypeDef(_ClientCreateJobCommandTypeDef):
    """
    The ``JobCommand`` that executes this job.
    - **Name** *(string) --*

      The name of the job command. For an Apache Spark ETL job, this must be ``glueetl`` . For a
      Python shell job, it must be ``pythonshell`` .
    """


_ClientCreateJobConnectionsTypeDef = TypedDict(
    "_ClientCreateJobConnectionsTypeDef", {"Connections": List[str]}, total=False
)


class ClientCreateJobConnectionsTypeDef(_ClientCreateJobConnectionsTypeDef):
    """
    The connections used for this job.
    - **Connections** *(list) --*

      A list of connections used by the job.
      - *(string) --*
    """


_ClientCreateJobExecutionPropertyTypeDef = TypedDict(
    "_ClientCreateJobExecutionPropertyTypeDef", {"MaxConcurrentRuns": int}, total=False
)


class ClientCreateJobExecutionPropertyTypeDef(_ClientCreateJobExecutionPropertyTypeDef):
    """
    An ``ExecutionProperty`` specifying the maximum number of concurrent runs allowed for this job.
    - **MaxConcurrentRuns** *(integer) --*

      The maximum number of concurrent runs allowed for the job. The default is 1. An error is
      returned when this threshold is reached. The maximum value you can specify is controlled by a
      service limit.
    """


_ClientCreateJobNotificationPropertyTypeDef = TypedDict(
    "_ClientCreateJobNotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)


class ClientCreateJobNotificationPropertyTypeDef(_ClientCreateJobNotificationPropertyTypeDef):
    """
    Specifies configuration properties of a job notification.
    - **NotifyDelayAfter** *(integer) --*

      After a job run starts, the number of minutes to wait before sending a job run delay
      notification.
    """


_ClientCreateJobResponseTypeDef = TypedDict(
    "_ClientCreateJobResponseTypeDef", {"Name": str}, total=False
)


class ClientCreateJobResponseTypeDef(_ClientCreateJobResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The unique name that was provided for this job definition.
    """


_RequiredClientCreateMlTransformInputRecordTablesTypeDef = TypedDict(
    "_RequiredClientCreateMlTransformInputRecordTablesTypeDef", {"DatabaseName": str}
)
_OptionalClientCreateMlTransformInputRecordTablesTypeDef = TypedDict(
    "_OptionalClientCreateMlTransformInputRecordTablesTypeDef",
    {"TableName": str, "CatalogId": str, "ConnectionName": str},
    total=False,
)


class ClientCreateMlTransformInputRecordTablesTypeDef(
    _RequiredClientCreateMlTransformInputRecordTablesTypeDef,
    _OptionalClientCreateMlTransformInputRecordTablesTypeDef,
):
    """
    - *(dict) --*

      The database and table in the AWS Glue Data Catalog that is used for input or output data.
      - **DatabaseName** *(string) --***[REQUIRED]**

        A database name in the AWS Glue Data Catalog.
    """


_ClientCreateMlTransformParametersFindMatchesParametersTypeDef = TypedDict(
    "_ClientCreateMlTransformParametersFindMatchesParametersTypeDef",
    {
        "PrimaryKeyColumnName": str,
        "PrecisionRecallTradeoff": float,
        "AccuracyCostTradeoff": float,
        "EnforceProvidedLabels": bool,
    },
    total=False,
)


class ClientCreateMlTransformParametersFindMatchesParametersTypeDef(
    _ClientCreateMlTransformParametersFindMatchesParametersTypeDef
):
    pass


_RequiredClientCreateMlTransformParametersTypeDef = TypedDict(
    "_RequiredClientCreateMlTransformParametersTypeDef", {"TransformType": str}
)
_OptionalClientCreateMlTransformParametersTypeDef = TypedDict(
    "_OptionalClientCreateMlTransformParametersTypeDef",
    {"FindMatchesParameters": ClientCreateMlTransformParametersFindMatchesParametersTypeDef},
    total=False,
)


class ClientCreateMlTransformParametersTypeDef(
    _RequiredClientCreateMlTransformParametersTypeDef,
    _OptionalClientCreateMlTransformParametersTypeDef,
):
    """
    The algorithmic parameters that are specific to the transform type used. Conditionally dependent
    on the transform type.
    - **TransformType** *(string) --***[REQUIRED]**

      The type of machine learning transform.
      For information about the types of machine learning transforms, see `Creating Machine Learning
      Transforms
      <http://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform.html>`__ .
    """


_ClientCreateMlTransformResponseTypeDef = TypedDict(
    "_ClientCreateMlTransformResponseTypeDef", {"TransformId": str}, total=False
)


class ClientCreateMlTransformResponseTypeDef(_ClientCreateMlTransformResponseTypeDef):
    """
    - *(dict) --*

      - **TransformId** *(string) --*

        A unique identifier that is generated for the transform.
    """


_ClientCreatePartitionPartitionInputStorageDescriptorColumnsTypeDef = TypedDict(
    "_ClientCreatePartitionPartitionInputStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientCreatePartitionPartitionInputStorageDescriptorColumnsTypeDef(
    _ClientCreatePartitionPartitionInputStorageDescriptorColumnsTypeDef
):
    pass


_ClientCreatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_ClientCreatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientCreatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef(
    _ClientCreatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef
):
    pass


_ClientCreatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_ClientCreatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class ClientCreatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef(
    _ClientCreatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef
):
    pass


_ClientCreatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_ClientCreatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class ClientCreatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef(
    _ClientCreatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef
):
    pass


_ClientCreatePartitionPartitionInputStorageDescriptorTypeDef = TypedDict(
    "_ClientCreatePartitionPartitionInputStorageDescriptorTypeDef",
    {
        "Columns": List[ClientCreatePartitionPartitionInputStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientCreatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientCreatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientCreatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class ClientCreatePartitionPartitionInputStorageDescriptorTypeDef(
    _ClientCreatePartitionPartitionInputStorageDescriptorTypeDef
):
    pass


_ClientCreatePartitionPartitionInputTypeDef = TypedDict(
    "_ClientCreatePartitionPartitionInputTypeDef",
    {
        "Values": List[str],
        "LastAccessTime": datetime,
        "StorageDescriptor": ClientCreatePartitionPartitionInputStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)


class ClientCreatePartitionPartitionInputTypeDef(_ClientCreatePartitionPartitionInputTypeDef):
    """
    A ``PartitionInput`` structure defining the partition to be created.
    - **Values** *(list) --*

      The values of the partition. Although this parameter is not required by the SDK, you must
      specify this parameter for a valid input.
      The values for the keys for the new partition must be passed as an array of String objects
      that must be ordered in the same order as the partition keys appearing in the Amazon S3
      prefix. Otherwise AWS Glue will add the values to the wrong keys.
      - *(string) --*
    """


_RequiredClientCreateScriptDagEdgesTypeDef = TypedDict(
    "_RequiredClientCreateScriptDagEdgesTypeDef", {"Source": str}
)
_OptionalClientCreateScriptDagEdgesTypeDef = TypedDict(
    "_OptionalClientCreateScriptDagEdgesTypeDef",
    {"Target": str, "TargetParameter": str},
    total=False,
)


class ClientCreateScriptDagEdgesTypeDef(
    _RequiredClientCreateScriptDagEdgesTypeDef, _OptionalClientCreateScriptDagEdgesTypeDef
):
    """
    - *(dict) --*

      Represents a directional edge in a directed acyclic graph (DAG).
      - **Source** *(string) --***[REQUIRED]**

        The ID of the node at which the edge starts.
    """


_ClientCreateScriptDagNodesArgsTypeDef = TypedDict(
    "_ClientCreateScriptDagNodesArgsTypeDef",
    {"Name": str, "Value": str, "Param": bool},
    total=False,
)


class ClientCreateScriptDagNodesArgsTypeDef(_ClientCreateScriptDagNodesArgsTypeDef):
    pass


_RequiredClientCreateScriptDagNodesTypeDef = TypedDict(
    "_RequiredClientCreateScriptDagNodesTypeDef", {"Id": str}
)
_OptionalClientCreateScriptDagNodesTypeDef = TypedDict(
    "_OptionalClientCreateScriptDagNodesTypeDef",
    {"NodeType": str, "Args": List[ClientCreateScriptDagNodesArgsTypeDef], "LineNumber": int},
    total=False,
)


class ClientCreateScriptDagNodesTypeDef(
    _RequiredClientCreateScriptDagNodesTypeDef, _OptionalClientCreateScriptDagNodesTypeDef
):
    """
    - *(dict) --*

      Represents a node in a directed acyclic graph (DAG)
      - **Id** *(string) --***[REQUIRED]**

        A node identifier that is unique within the node's graph.
    """


_ClientCreateScriptResponseTypeDef = TypedDict(
    "_ClientCreateScriptResponseTypeDef", {"PythonScript": str, "ScalaCode": str}, total=False
)


class ClientCreateScriptResponseTypeDef(_ClientCreateScriptResponseTypeDef):
    """
    - *(dict) --*

      - **PythonScript** *(string) --*

        The Python script generated from the DAG.
    """


_ClientCreateSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef = TypedDict(
    "_ClientCreateSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef",
    {"CloudWatchEncryptionMode": Literal["DISABLED", "SSE-KMS"], "KmsKeyArn": str},
    total=False,
)


class ClientCreateSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef(
    _ClientCreateSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef
):
    pass


_ClientCreateSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef = TypedDict(
    "_ClientCreateSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef",
    {"JobBookmarksEncryptionMode": Literal["DISABLED", "CSE-KMS"], "KmsKeyArn": str},
    total=False,
)


class ClientCreateSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef(
    _ClientCreateSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef
):
    pass


_ClientCreateSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef = TypedDict(
    "_ClientCreateSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef",
    {"S3EncryptionMode": Literal["DISABLED", "SSE-KMS", "SSE-S3"], "KmsKeyArn": str},
    total=False,
)


class ClientCreateSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef(
    _ClientCreateSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef
):
    """
    - *(dict) --*

      Specifies how Amazon Simple Storage Service (Amazon S3) data should be encrypted.
      - **S3EncryptionMode** *(string) --*

        The encryption mode to use for Amazon S3 data.
    """


_ClientCreateSecurityConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientCreateSecurityConfigurationEncryptionConfigurationTypeDef",
    {
        "S3Encryption": List[
            ClientCreateSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef
        ],
        "CloudWatchEncryption": ClientCreateSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef,
        "JobBookmarksEncryption": ClientCreateSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateSecurityConfigurationEncryptionConfigurationTypeDef(
    _ClientCreateSecurityConfigurationEncryptionConfigurationTypeDef
):
    """
    The encryption configuration for the new security configuration.
    - **S3Encryption** *(list) --*

      The encryption configuration for Amazon Simple Storage Service (Amazon S3) data.
      - *(dict) --*

        Specifies how Amazon Simple Storage Service (Amazon S3) data should be encrypted.
        - **S3EncryptionMode** *(string) --*

          The encryption mode to use for Amazon S3 data.
    """


_ClientCreateSecurityConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateSecurityConfigurationResponseTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)


class ClientCreateSecurityConfigurationResponseTypeDef(
    _ClientCreateSecurityConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name assigned to the new security configuration.
    """


_ClientCreateTableTableInputPartitionKeysTypeDef = TypedDict(
    "_ClientCreateTableTableInputPartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientCreateTableTableInputPartitionKeysTypeDef(
    _ClientCreateTableTableInputPartitionKeysTypeDef
):
    pass


_ClientCreateTableTableInputStorageDescriptorColumnsTypeDef = TypedDict(
    "_ClientCreateTableTableInputStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientCreateTableTableInputStorageDescriptorColumnsTypeDef(
    _ClientCreateTableTableInputStorageDescriptorColumnsTypeDef
):
    pass


_ClientCreateTableTableInputStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_ClientCreateTableTableInputStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientCreateTableTableInputStorageDescriptorSerdeInfoTypeDef(
    _ClientCreateTableTableInputStorageDescriptorSerdeInfoTypeDef
):
    pass


_ClientCreateTableTableInputStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_ClientCreateTableTableInputStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class ClientCreateTableTableInputStorageDescriptorSkewedInfoTypeDef(
    _ClientCreateTableTableInputStorageDescriptorSkewedInfoTypeDef
):
    pass


_ClientCreateTableTableInputStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_ClientCreateTableTableInputStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class ClientCreateTableTableInputStorageDescriptorSortColumnsTypeDef(
    _ClientCreateTableTableInputStorageDescriptorSortColumnsTypeDef
):
    pass


_ClientCreateTableTableInputStorageDescriptorTypeDef = TypedDict(
    "_ClientCreateTableTableInputStorageDescriptorTypeDef",
    {
        "Columns": List[ClientCreateTableTableInputStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientCreateTableTableInputStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientCreateTableTableInputStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientCreateTableTableInputStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class ClientCreateTableTableInputStorageDescriptorTypeDef(
    _ClientCreateTableTableInputStorageDescriptorTypeDef
):
    pass


_RequiredClientCreateTableTableInputTypeDef = TypedDict(
    "_RequiredClientCreateTableTableInputTypeDef", {"Name": str}
)
_OptionalClientCreateTableTableInputTypeDef = TypedDict(
    "_OptionalClientCreateTableTableInputTypeDef",
    {
        "Description": str,
        "Owner": str,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientCreateTableTableInputStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientCreateTableTableInputPartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ClientCreateTableTableInputTypeDef(
    _RequiredClientCreateTableTableInputTypeDef, _OptionalClientCreateTableTableInputTypeDef
):
    """
    The ``TableInput`` object that defines the metadata table to create in the catalog.
    - **Name** *(string) --***[REQUIRED]**

      The table name. For Hive compatibility, this is folded to lowercase when it is stored.
    """


_ClientCreateTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "_ClientCreateTriggerActionsNotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)


class ClientCreateTriggerActionsNotificationPropertyTypeDef(
    _ClientCreateTriggerActionsNotificationPropertyTypeDef
):
    pass


_ClientCreateTriggerActionsTypeDef = TypedDict(
    "_ClientCreateTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientCreateTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)


class ClientCreateTriggerActionsTypeDef(_ClientCreateTriggerActionsTypeDef):
    """
    - *(dict) --*

      Defines an action to be initiated by a trigger.
      - **JobName** *(string) --*

        The name of a job to be executed.
    """


_ClientCreateTriggerPredicateConditionsTypeDef = TypedDict(
    "_ClientCreateTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)


class ClientCreateTriggerPredicateConditionsTypeDef(_ClientCreateTriggerPredicateConditionsTypeDef):
    pass


_ClientCreateTriggerPredicateTypeDef = TypedDict(
    "_ClientCreateTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[ClientCreateTriggerPredicateConditionsTypeDef],
    },
    total=False,
)


class ClientCreateTriggerPredicateTypeDef(_ClientCreateTriggerPredicateTypeDef):
    """
    A predicate to specify when the new trigger should fire.
    This field is required when the trigger type is ``CONDITIONAL`` .
    - **Logical** *(string) --*

      An optional field if only one condition is listed. If multiple conditions are listed, then
      this field is required.
    """


_ClientCreateTriggerResponseTypeDef = TypedDict(
    "_ClientCreateTriggerResponseTypeDef", {"Name": str}, total=False
)


class ClientCreateTriggerResponseTypeDef(_ClientCreateTriggerResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the trigger.
    """


_ClientCreateUserDefinedFunctionFunctionInputResourceUrisTypeDef = TypedDict(
    "_ClientCreateUserDefinedFunctionFunctionInputResourceUrisTypeDef",
    {"ResourceType": Literal["JAR", "FILE", "ARCHIVE"], "Uri": str},
    total=False,
)


class ClientCreateUserDefinedFunctionFunctionInputResourceUrisTypeDef(
    _ClientCreateUserDefinedFunctionFunctionInputResourceUrisTypeDef
):
    pass


_ClientCreateUserDefinedFunctionFunctionInputTypeDef = TypedDict(
    "_ClientCreateUserDefinedFunctionFunctionInputTypeDef",
    {
        "FunctionName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": Literal["USER", "ROLE", "GROUP"],
        "ResourceUris": List[ClientCreateUserDefinedFunctionFunctionInputResourceUrisTypeDef],
    },
    total=False,
)


class ClientCreateUserDefinedFunctionFunctionInputTypeDef(
    _ClientCreateUserDefinedFunctionFunctionInputTypeDef
):
    """
    A ``FunctionInput`` object that defines the function to create in the Data Catalog.
    - **FunctionName** *(string) --*

      The name of the function.
    """


_ClientCreateWorkflowResponseTypeDef = TypedDict(
    "_ClientCreateWorkflowResponseTypeDef", {"Name": str}, total=False
)


class ClientCreateWorkflowResponseTypeDef(_ClientCreateWorkflowResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the workflow which was provided as part of the request.
    """


_ClientDeleteJobResponseTypeDef = TypedDict(
    "_ClientDeleteJobResponseTypeDef", {"JobName": str}, total=False
)


class ClientDeleteJobResponseTypeDef(_ClientDeleteJobResponseTypeDef):
    """
    - *(dict) --*

      - **JobName** *(string) --*

        The name of the job definition that was deleted.
    """


_ClientDeleteMlTransformResponseTypeDef = TypedDict(
    "_ClientDeleteMlTransformResponseTypeDef", {"TransformId": str}, total=False
)


class ClientDeleteMlTransformResponseTypeDef(_ClientDeleteMlTransformResponseTypeDef):
    """
    - *(dict) --*

      - **TransformId** *(string) --*

        The unique identifier of the transform that was deleted.
    """


_ClientDeleteTriggerResponseTypeDef = TypedDict(
    "_ClientDeleteTriggerResponseTypeDef", {"Name": str}, total=False
)


class ClientDeleteTriggerResponseTypeDef(_ClientDeleteTriggerResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the trigger that was deleted.
    """


_ClientDeleteWorkflowResponseTypeDef = TypedDict(
    "_ClientDeleteWorkflowResponseTypeDef", {"Name": str}, total=False
)


class ClientDeleteWorkflowResponseTypeDef(_ClientDeleteWorkflowResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        Name of the workflow specified in input.
    """


_ClientGetCatalogImportStatusResponseImportStatusTypeDef = TypedDict(
    "_ClientGetCatalogImportStatusResponseImportStatusTypeDef",
    {"ImportCompleted": bool, "ImportTime": datetime, "ImportedBy": str},
    total=False,
)


class ClientGetCatalogImportStatusResponseImportStatusTypeDef(
    _ClientGetCatalogImportStatusResponseImportStatusTypeDef
):
    """
    - **ImportStatus** *(dict) --*

      The status of the specified catalog migration.
      - **ImportCompleted** *(boolean) --*

        ``True`` if the migration has completed, or ``False`` otherwise.
    """


_ClientGetCatalogImportStatusResponseTypeDef = TypedDict(
    "_ClientGetCatalogImportStatusResponseTypeDef",
    {"ImportStatus": ClientGetCatalogImportStatusResponseImportStatusTypeDef},
    total=False,
)


class ClientGetCatalogImportStatusResponseTypeDef(_ClientGetCatalogImportStatusResponseTypeDef):
    """
    - *(dict) --*

      - **ImportStatus** *(dict) --*

        The status of the specified catalog migration.
        - **ImportCompleted** *(boolean) --*

          ``True`` if the migration has completed, or ``False`` otherwise.
    """


_ClientGetClassifierResponseClassifierCsvClassifierTypeDef = TypedDict(
    "_ClientGetClassifierResponseClassifierCsvClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": Literal["UNKNOWN", "PRESENT", "ABSENT"],
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)


class ClientGetClassifierResponseClassifierCsvClassifierTypeDef(
    _ClientGetClassifierResponseClassifierCsvClassifierTypeDef
):
    pass


_ClientGetClassifierResponseClassifierGrokClassifierTypeDef = TypedDict(
    "_ClientGetClassifierResponseClassifierGrokClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "GrokPattern": str,
        "CustomPatterns": str,
    },
    total=False,
)


class ClientGetClassifierResponseClassifierGrokClassifierTypeDef(
    _ClientGetClassifierResponseClassifierGrokClassifierTypeDef
):
    """
    - **GrokClassifier** *(dict) --*

      A classifier that uses ``grok`` .
      - **Name** *(string) --*

        The name of the classifier.
    """


_ClientGetClassifierResponseClassifierJsonClassifierTypeDef = TypedDict(
    "_ClientGetClassifierResponseClassifierJsonClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "JsonPath": str,
    },
    total=False,
)


class ClientGetClassifierResponseClassifierJsonClassifierTypeDef(
    _ClientGetClassifierResponseClassifierJsonClassifierTypeDef
):
    pass


_ClientGetClassifierResponseClassifierXMLClassifierTypeDef = TypedDict(
    "_ClientGetClassifierResponseClassifierXMLClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "RowTag": str,
    },
    total=False,
)


class ClientGetClassifierResponseClassifierXMLClassifierTypeDef(
    _ClientGetClassifierResponseClassifierXMLClassifierTypeDef
):
    pass


_ClientGetClassifierResponseClassifierTypeDef = TypedDict(
    "_ClientGetClassifierResponseClassifierTypeDef",
    {
        "GrokClassifier": ClientGetClassifierResponseClassifierGrokClassifierTypeDef,
        "XMLClassifier": ClientGetClassifierResponseClassifierXMLClassifierTypeDef,
        "JsonClassifier": ClientGetClassifierResponseClassifierJsonClassifierTypeDef,
        "CsvClassifier": ClientGetClassifierResponseClassifierCsvClassifierTypeDef,
    },
    total=False,
)


class ClientGetClassifierResponseClassifierTypeDef(_ClientGetClassifierResponseClassifierTypeDef):
    """
    - **Classifier** *(dict) --*

      The requested classifier.
      - **GrokClassifier** *(dict) --*

        A classifier that uses ``grok`` .
        - **Name** *(string) --*

          The name of the classifier.
    """


_ClientGetClassifierResponseTypeDef = TypedDict(
    "_ClientGetClassifierResponseTypeDef",
    {"Classifier": ClientGetClassifierResponseClassifierTypeDef},
    total=False,
)


class ClientGetClassifierResponseTypeDef(_ClientGetClassifierResponseTypeDef):
    """
    - *(dict) --*

      - **Classifier** *(dict) --*

        The requested classifier.
        - **GrokClassifier** *(dict) --*

          A classifier that uses ``grok`` .
          - **Name** *(string) --*

            The name of the classifier.
    """


_ClientGetClassifiersResponseClassifiersCsvClassifierTypeDef = TypedDict(
    "_ClientGetClassifiersResponseClassifiersCsvClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": Literal["UNKNOWN", "PRESENT", "ABSENT"],
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)


class ClientGetClassifiersResponseClassifiersCsvClassifierTypeDef(
    _ClientGetClassifiersResponseClassifiersCsvClassifierTypeDef
):
    pass


_ClientGetClassifiersResponseClassifiersGrokClassifierTypeDef = TypedDict(
    "_ClientGetClassifiersResponseClassifiersGrokClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "GrokPattern": str,
        "CustomPatterns": str,
    },
    total=False,
)


class ClientGetClassifiersResponseClassifiersGrokClassifierTypeDef(
    _ClientGetClassifiersResponseClassifiersGrokClassifierTypeDef
):
    """
    - **GrokClassifier** *(dict) --*

      A classifier that uses ``grok`` .
      - **Name** *(string) --*

        The name of the classifier.
    """


_ClientGetClassifiersResponseClassifiersJsonClassifierTypeDef = TypedDict(
    "_ClientGetClassifiersResponseClassifiersJsonClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "JsonPath": str,
    },
    total=False,
)


class ClientGetClassifiersResponseClassifiersJsonClassifierTypeDef(
    _ClientGetClassifiersResponseClassifiersJsonClassifierTypeDef
):
    pass


_ClientGetClassifiersResponseClassifiersXMLClassifierTypeDef = TypedDict(
    "_ClientGetClassifiersResponseClassifiersXMLClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "RowTag": str,
    },
    total=False,
)


class ClientGetClassifiersResponseClassifiersXMLClassifierTypeDef(
    _ClientGetClassifiersResponseClassifiersXMLClassifierTypeDef
):
    pass


_ClientGetClassifiersResponseClassifiersTypeDef = TypedDict(
    "_ClientGetClassifiersResponseClassifiersTypeDef",
    {
        "GrokClassifier": ClientGetClassifiersResponseClassifiersGrokClassifierTypeDef,
        "XMLClassifier": ClientGetClassifiersResponseClassifiersXMLClassifierTypeDef,
        "JsonClassifier": ClientGetClassifiersResponseClassifiersJsonClassifierTypeDef,
        "CsvClassifier": ClientGetClassifiersResponseClassifiersCsvClassifierTypeDef,
    },
    total=False,
)


class ClientGetClassifiersResponseClassifiersTypeDef(
    _ClientGetClassifiersResponseClassifiersTypeDef
):
    """
    - *(dict) --*

      Classifiers are triggered during a crawl task. A classifier checks whether a given file is in
      a format it can handle. If it is, the classifier creates a schema in the form of a
      ``StructType`` object that matches that data format.
      You can use the standard classifiers that AWS Glue provides, or you can write your own
      classifiers to best categorize your data sources and specify the appropriate schemas to use
      for them. A classifier can be a ``grok`` classifier, an ``XML`` classifier, a ``JSON``
      classifier, or a custom ``CSV`` classifier, as specified in one of the fields in the
      ``Classifier`` object.
      - **GrokClassifier** *(dict) --*

        A classifier that uses ``grok`` .
        - **Name** *(string) --*

          The name of the classifier.
    """


_ClientGetClassifiersResponseTypeDef = TypedDict(
    "_ClientGetClassifiersResponseTypeDef",
    {"Classifiers": List[ClientGetClassifiersResponseClassifiersTypeDef], "NextToken": str},
    total=False,
)


class ClientGetClassifiersResponseTypeDef(_ClientGetClassifiersResponseTypeDef):
    """
    - *(dict) --*

      - **Classifiers** *(list) --*

        The requested list of classifier objects.
        - *(dict) --*

          Classifiers are triggered during a crawl task. A classifier checks whether a given file is
          in a format it can handle. If it is, the classifier creates a schema in the form of a
          ``StructType`` object that matches that data format.
          You can use the standard classifiers that AWS Glue provides, or you can write your own
          classifiers to best categorize your data sources and specify the appropriate schemas to
          use for them. A classifier can be a ``grok`` classifier, an ``XML`` classifier, a ``JSON``
          classifier, or a custom ``CSV`` classifier, as specified in one of the fields in the
          ``Classifier`` object.
          - **GrokClassifier** *(dict) --*

            A classifier that uses ``grok`` .
            - **Name** *(string) --*

              The name of the classifier.
    """


_ClientGetConnectionResponseConnectionPhysicalConnectionRequirementsTypeDef = TypedDict(
    "_ClientGetConnectionResponseConnectionPhysicalConnectionRequirementsTypeDef",
    {"SubnetId": str, "SecurityGroupIdList": List[str], "AvailabilityZone": str},
    total=False,
)


class ClientGetConnectionResponseConnectionPhysicalConnectionRequirementsTypeDef(
    _ClientGetConnectionResponseConnectionPhysicalConnectionRequirementsTypeDef
):
    pass


_ClientGetConnectionResponseConnectionTypeDef = TypedDict(
    "_ClientGetConnectionResponseConnectionTypeDef",
    {
        "Name": str,
        "Description": str,
        "ConnectionType": Literal["JDBC", "SFTP"],
        "MatchCriteria": List[str],
        "ConnectionProperties": Dict[str, str],
        "PhysicalConnectionRequirements": ClientGetConnectionResponseConnectionPhysicalConnectionRequirementsTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "LastUpdatedBy": str,
    },
    total=False,
)


class ClientGetConnectionResponseConnectionTypeDef(_ClientGetConnectionResponseConnectionTypeDef):
    """
    - **Connection** *(dict) --*

      The requested connection definition.
      - **Name** *(string) --*

        The name of the connection definition.
    """


_ClientGetConnectionResponseTypeDef = TypedDict(
    "_ClientGetConnectionResponseTypeDef",
    {"Connection": ClientGetConnectionResponseConnectionTypeDef},
    total=False,
)


class ClientGetConnectionResponseTypeDef(_ClientGetConnectionResponseTypeDef):
    """
    - *(dict) --*

      - **Connection** *(dict) --*

        The requested connection definition.
        - **Name** *(string) --*

          The name of the connection definition.
    """


_ClientGetConnectionsFilterTypeDef = TypedDict(
    "_ClientGetConnectionsFilterTypeDef",
    {"MatchCriteria": List[str], "ConnectionType": Literal["JDBC", "SFTP"]},
    total=False,
)


class ClientGetConnectionsFilterTypeDef(_ClientGetConnectionsFilterTypeDef):
    """
    A filter that controls which connections are returned.
    - **MatchCriteria** *(list) --*

      A criteria string that must match the criteria recorded in the connection definition for that
      connection definition to be returned.
      - *(string) --*
    """


_ClientGetConnectionsResponseConnectionListPhysicalConnectionRequirementsTypeDef = TypedDict(
    "_ClientGetConnectionsResponseConnectionListPhysicalConnectionRequirementsTypeDef",
    {"SubnetId": str, "SecurityGroupIdList": List[str], "AvailabilityZone": str},
    total=False,
)


class ClientGetConnectionsResponseConnectionListPhysicalConnectionRequirementsTypeDef(
    _ClientGetConnectionsResponseConnectionListPhysicalConnectionRequirementsTypeDef
):
    pass


_ClientGetConnectionsResponseConnectionListTypeDef = TypedDict(
    "_ClientGetConnectionsResponseConnectionListTypeDef",
    {
        "Name": str,
        "Description": str,
        "ConnectionType": Literal["JDBC", "SFTP"],
        "MatchCriteria": List[str],
        "ConnectionProperties": Dict[str, str],
        "PhysicalConnectionRequirements": ClientGetConnectionsResponseConnectionListPhysicalConnectionRequirementsTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "LastUpdatedBy": str,
    },
    total=False,
)


class ClientGetConnectionsResponseConnectionListTypeDef(
    _ClientGetConnectionsResponseConnectionListTypeDef
):
    """
    - *(dict) --*

      Defines a connection to a data source.
      - **Name** *(string) --*

        The name of the connection definition.
    """


_ClientGetConnectionsResponseTypeDef = TypedDict(
    "_ClientGetConnectionsResponseTypeDef",
    {"ConnectionList": List[ClientGetConnectionsResponseConnectionListTypeDef], "NextToken": str},
    total=False,
)


class ClientGetConnectionsResponseTypeDef(_ClientGetConnectionsResponseTypeDef):
    """
    - *(dict) --*

      - **ConnectionList** *(list) --*

        A list of requested connection definitions.
        - *(dict) --*

          Defines a connection to a data source.
          - **Name** *(string) --*

            The name of the connection definition.
    """


_ClientGetCrawlerMetricsResponseCrawlerMetricsListTypeDef = TypedDict(
    "_ClientGetCrawlerMetricsResponseCrawlerMetricsListTypeDef",
    {
        "CrawlerName": str,
        "TimeLeftSeconds": float,
        "StillEstimating": bool,
        "LastRuntimeSeconds": float,
        "MedianRuntimeSeconds": float,
        "TablesCreated": int,
        "TablesUpdated": int,
        "TablesDeleted": int,
    },
    total=False,
)


class ClientGetCrawlerMetricsResponseCrawlerMetricsListTypeDef(
    _ClientGetCrawlerMetricsResponseCrawlerMetricsListTypeDef
):
    """
    - *(dict) --*

      Metrics for a specified crawler.
      - **CrawlerName** *(string) --*

        The name of the crawler.
    """


_ClientGetCrawlerMetricsResponseTypeDef = TypedDict(
    "_ClientGetCrawlerMetricsResponseTypeDef",
    {
        "CrawlerMetricsList": List[ClientGetCrawlerMetricsResponseCrawlerMetricsListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientGetCrawlerMetricsResponseTypeDef(_ClientGetCrawlerMetricsResponseTypeDef):
    """
    - *(dict) --*

      - **CrawlerMetricsList** *(list) --*

        A list of metrics for the specified crawler.
        - *(dict) --*

          Metrics for a specified crawler.
          - **CrawlerName** *(string) --*

            The name of the crawler.
    """


_ClientGetCrawlerResponseCrawlerLastCrawlTypeDef = TypedDict(
    "_ClientGetCrawlerResponseCrawlerLastCrawlTypeDef",
    {
        "Status": Literal["SUCCEEDED", "CANCELLED", "FAILED"],
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
        "MessagePrefix": str,
        "StartTime": datetime,
    },
    total=False,
)


class ClientGetCrawlerResponseCrawlerLastCrawlTypeDef(
    _ClientGetCrawlerResponseCrawlerLastCrawlTypeDef
):
    pass


_ClientGetCrawlerResponseCrawlerScheduleTypeDef = TypedDict(
    "_ClientGetCrawlerResponseCrawlerScheduleTypeDef",
    {"ScheduleExpression": str, "State": Literal["SCHEDULED", "NOT_SCHEDULED", "TRANSITIONING"]},
    total=False,
)


class ClientGetCrawlerResponseCrawlerScheduleTypeDef(
    _ClientGetCrawlerResponseCrawlerScheduleTypeDef
):
    pass


_ClientGetCrawlerResponseCrawlerSchemaChangePolicyTypeDef = TypedDict(
    "_ClientGetCrawlerResponseCrawlerSchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": Literal["LOG", "UPDATE_IN_DATABASE"],
        "DeleteBehavior": Literal["LOG", "DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE"],
    },
    total=False,
)


class ClientGetCrawlerResponseCrawlerSchemaChangePolicyTypeDef(
    _ClientGetCrawlerResponseCrawlerSchemaChangePolicyTypeDef
):
    pass


_ClientGetCrawlerResponseCrawlerTargetsCatalogTargetsTypeDef = TypedDict(
    "_ClientGetCrawlerResponseCrawlerTargetsCatalogTargetsTypeDef",
    {"DatabaseName": str, "Tables": List[str]},
    total=False,
)


class ClientGetCrawlerResponseCrawlerTargetsCatalogTargetsTypeDef(
    _ClientGetCrawlerResponseCrawlerTargetsCatalogTargetsTypeDef
):
    pass


_ClientGetCrawlerResponseCrawlerTargetsDynamoDBTargetsTypeDef = TypedDict(
    "_ClientGetCrawlerResponseCrawlerTargetsDynamoDBTargetsTypeDef", {"Path": str}, total=False
)


class ClientGetCrawlerResponseCrawlerTargetsDynamoDBTargetsTypeDef(
    _ClientGetCrawlerResponseCrawlerTargetsDynamoDBTargetsTypeDef
):
    pass


_ClientGetCrawlerResponseCrawlerTargetsJdbcTargetsTypeDef = TypedDict(
    "_ClientGetCrawlerResponseCrawlerTargetsJdbcTargetsTypeDef",
    {"ConnectionName": str, "Path": str, "Exclusions": List[str]},
    total=False,
)


class ClientGetCrawlerResponseCrawlerTargetsJdbcTargetsTypeDef(
    _ClientGetCrawlerResponseCrawlerTargetsJdbcTargetsTypeDef
):
    pass


_ClientGetCrawlerResponseCrawlerTargetsS3TargetsTypeDef = TypedDict(
    "_ClientGetCrawlerResponseCrawlerTargetsS3TargetsTypeDef",
    {"Path": str, "Exclusions": List[str]},
    total=False,
)


class ClientGetCrawlerResponseCrawlerTargetsS3TargetsTypeDef(
    _ClientGetCrawlerResponseCrawlerTargetsS3TargetsTypeDef
):
    pass


_ClientGetCrawlerResponseCrawlerTargetsTypeDef = TypedDict(
    "_ClientGetCrawlerResponseCrawlerTargetsTypeDef",
    {
        "S3Targets": List[ClientGetCrawlerResponseCrawlerTargetsS3TargetsTypeDef],
        "JdbcTargets": List[ClientGetCrawlerResponseCrawlerTargetsJdbcTargetsTypeDef],
        "DynamoDBTargets": List[ClientGetCrawlerResponseCrawlerTargetsDynamoDBTargetsTypeDef],
        "CatalogTargets": List[ClientGetCrawlerResponseCrawlerTargetsCatalogTargetsTypeDef],
    },
    total=False,
)


class ClientGetCrawlerResponseCrawlerTargetsTypeDef(_ClientGetCrawlerResponseCrawlerTargetsTypeDef):
    pass


_ClientGetCrawlerResponseCrawlerTypeDef = TypedDict(
    "_ClientGetCrawlerResponseCrawlerTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": ClientGetCrawlerResponseCrawlerTargetsTypeDef,
        "DatabaseName": str,
        "Description": str,
        "Classifiers": List[str],
        "SchemaChangePolicy": ClientGetCrawlerResponseCrawlerSchemaChangePolicyTypeDef,
        "State": Literal["READY", "RUNNING", "STOPPING"],
        "TablePrefix": str,
        "Schedule": ClientGetCrawlerResponseCrawlerScheduleTypeDef,
        "CrawlElapsedTime": int,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "LastCrawl": ClientGetCrawlerResponseCrawlerLastCrawlTypeDef,
        "Version": int,
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
    },
    total=False,
)


class ClientGetCrawlerResponseCrawlerTypeDef(_ClientGetCrawlerResponseCrawlerTypeDef):
    """
    - **Crawler** *(dict) --*

      The metadata for the specified crawler.
      - **Name** *(string) --*

        The name of the crawler.
    """


_ClientGetCrawlerResponseTypeDef = TypedDict(
    "_ClientGetCrawlerResponseTypeDef",
    {"Crawler": ClientGetCrawlerResponseCrawlerTypeDef},
    total=False,
)


class ClientGetCrawlerResponseTypeDef(_ClientGetCrawlerResponseTypeDef):
    """
    - *(dict) --*

      - **Crawler** *(dict) --*

        The metadata for the specified crawler.
        - **Name** *(string) --*

          The name of the crawler.
    """


_ClientGetCrawlersResponseCrawlersLastCrawlTypeDef = TypedDict(
    "_ClientGetCrawlersResponseCrawlersLastCrawlTypeDef",
    {
        "Status": Literal["SUCCEEDED", "CANCELLED", "FAILED"],
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
        "MessagePrefix": str,
        "StartTime": datetime,
    },
    total=False,
)


class ClientGetCrawlersResponseCrawlersLastCrawlTypeDef(
    _ClientGetCrawlersResponseCrawlersLastCrawlTypeDef
):
    pass


_ClientGetCrawlersResponseCrawlersScheduleTypeDef = TypedDict(
    "_ClientGetCrawlersResponseCrawlersScheduleTypeDef",
    {"ScheduleExpression": str, "State": Literal["SCHEDULED", "NOT_SCHEDULED", "TRANSITIONING"]},
    total=False,
)


class ClientGetCrawlersResponseCrawlersScheduleTypeDef(
    _ClientGetCrawlersResponseCrawlersScheduleTypeDef
):
    pass


_ClientGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef = TypedDict(
    "_ClientGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": Literal["LOG", "UPDATE_IN_DATABASE"],
        "DeleteBehavior": Literal["LOG", "DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE"],
    },
    total=False,
)


class ClientGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef(
    _ClientGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef
):
    pass


_ClientGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef = TypedDict(
    "_ClientGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef",
    {"DatabaseName": str, "Tables": List[str]},
    total=False,
)


class ClientGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef(
    _ClientGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef
):
    pass


_ClientGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef = TypedDict(
    "_ClientGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef", {"Path": str}, total=False
)


class ClientGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef(
    _ClientGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef
):
    pass


_ClientGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef = TypedDict(
    "_ClientGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef",
    {"ConnectionName": str, "Path": str, "Exclusions": List[str]},
    total=False,
)


class ClientGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef(
    _ClientGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef
):
    pass


_ClientGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef = TypedDict(
    "_ClientGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef",
    {"Path": str, "Exclusions": List[str]},
    total=False,
)


class ClientGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef(
    _ClientGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef
):
    pass


_ClientGetCrawlersResponseCrawlersTargetsTypeDef = TypedDict(
    "_ClientGetCrawlersResponseCrawlersTargetsTypeDef",
    {
        "S3Targets": List[ClientGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef],
        "JdbcTargets": List[ClientGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef],
        "DynamoDBTargets": List[ClientGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef],
        "CatalogTargets": List[ClientGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef],
    },
    total=False,
)


class ClientGetCrawlersResponseCrawlersTargetsTypeDef(
    _ClientGetCrawlersResponseCrawlersTargetsTypeDef
):
    pass


_ClientGetCrawlersResponseCrawlersTypeDef = TypedDict(
    "_ClientGetCrawlersResponseCrawlersTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": ClientGetCrawlersResponseCrawlersTargetsTypeDef,
        "DatabaseName": str,
        "Description": str,
        "Classifiers": List[str],
        "SchemaChangePolicy": ClientGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef,
        "State": Literal["READY", "RUNNING", "STOPPING"],
        "TablePrefix": str,
        "Schedule": ClientGetCrawlersResponseCrawlersScheduleTypeDef,
        "CrawlElapsedTime": int,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "LastCrawl": ClientGetCrawlersResponseCrawlersLastCrawlTypeDef,
        "Version": int,
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
    },
    total=False,
)


class ClientGetCrawlersResponseCrawlersTypeDef(_ClientGetCrawlersResponseCrawlersTypeDef):
    """
    - *(dict) --*

      Specifies a crawler program that examines a data source and uses classifiers to try to
      determine its schema. If successful, the crawler records metadata concerning the data source
      in the AWS Glue Data Catalog.
      - **Name** *(string) --*

        The name of the crawler.
    """


_ClientGetCrawlersResponseTypeDef = TypedDict(
    "_ClientGetCrawlersResponseTypeDef",
    {"Crawlers": List[ClientGetCrawlersResponseCrawlersTypeDef], "NextToken": str},
    total=False,
)


class ClientGetCrawlersResponseTypeDef(_ClientGetCrawlersResponseTypeDef):
    """
    - *(dict) --*

      - **Crawlers** *(list) --*

        A list of crawler metadata.
        - *(dict) --*

          Specifies a crawler program that examines a data source and uses classifiers to try to
          determine its schema. If successful, the crawler records metadata concerning the data
          source in the AWS Glue Data Catalog.
          - **Name** *(string) --*

            The name of the crawler.
    """


_ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef = TypedDict(
    "_ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef",
    {"ReturnConnectionPasswordEncrypted": bool, "AwsKmsKeyId": str},
    total=False,
)


class ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef(
    _ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef
):
    pass


_ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsEncryptionAtRestTypeDef = TypedDict(
    "_ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsEncryptionAtRestTypeDef",
    {"CatalogEncryptionMode": Literal["DISABLED", "SSE-KMS"], "SseAwsKmsKeyId": str},
    total=False,
)


class ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsEncryptionAtRestTypeDef(
    _ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsEncryptionAtRestTypeDef
):
    """
    - **EncryptionAtRest** *(dict) --*

      Specifies the encryption-at-rest configuration for the Data Catalog.
      - **CatalogEncryptionMode** *(string) --*

        The encryption-at-rest mode for encrypting Data Catalog data.
    """


_ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsTypeDef = TypedDict(
    "_ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsTypeDef",
    {
        "EncryptionAtRest": ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsEncryptionAtRestTypeDef,
        "ConnectionPasswordEncryption": ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef,
    },
    total=False,
)


class ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsTypeDef(
    _ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsTypeDef
):
    """
    - **DataCatalogEncryptionSettings** *(dict) --*

      The requested security configuration.
      - **EncryptionAtRest** *(dict) --*

        Specifies the encryption-at-rest configuration for the Data Catalog.
        - **CatalogEncryptionMode** *(string) --*

          The encryption-at-rest mode for encrypting Data Catalog data.
    """


_ClientGetDataCatalogEncryptionSettingsResponseTypeDef = TypedDict(
    "_ClientGetDataCatalogEncryptionSettingsResponseTypeDef",
    {
        "DataCatalogEncryptionSettings": ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsTypeDef
    },
    total=False,
)


class ClientGetDataCatalogEncryptionSettingsResponseTypeDef(
    _ClientGetDataCatalogEncryptionSettingsResponseTypeDef
):
    """
    - *(dict) --*

      - **DataCatalogEncryptionSettings** *(dict) --*

        The requested security configuration.
        - **EncryptionAtRest** *(dict) --*

          Specifies the encryption-at-rest configuration for the Data Catalog.
          - **CatalogEncryptionMode** *(string) --*

            The encryption-at-rest mode for encrypting Data Catalog data.
    """


_ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "_ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsPrincipalTypeDef(
    _ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsPrincipalTypeDef
):
    pass


_ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsTypeDef = TypedDict(
    "_ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsTypeDef(
    _ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsTypeDef
):
    pass


_ClientGetDatabaseResponseDatabaseTypeDef = TypedDict(
    "_ClientGetDatabaseResponseDatabaseTypeDef",
    {
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTime": datetime,
        "CreateTableDefaultPermissions": List[
            ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientGetDatabaseResponseDatabaseTypeDef(_ClientGetDatabaseResponseDatabaseTypeDef):
    """
    - **Database** *(dict) --*

      The definition of the specified database in the Data Catalog.
      - **Name** *(string) --*

        The name of the database. For Hive compatibility, this is folded to lowercase when it is
        stored.
    """


_ClientGetDatabaseResponseTypeDef = TypedDict(
    "_ClientGetDatabaseResponseTypeDef",
    {"Database": ClientGetDatabaseResponseDatabaseTypeDef},
    total=False,
)


class ClientGetDatabaseResponseTypeDef(_ClientGetDatabaseResponseTypeDef):
    """
    - *(dict) --*

      - **Database** *(dict) --*

        The definition of the specified database in the Data Catalog.
        - **Name** *(string) --*

          The name of the database. For Hive compatibility, this is folded to lowercase when it is
          stored.
    """


_ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "_ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef(
    _ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef
):
    pass


_ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsTypeDef = TypedDict(
    "_ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsTypeDef(
    _ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsTypeDef
):
    pass


_ClientGetDatabasesResponseDatabaseListTypeDef = TypedDict(
    "_ClientGetDatabasesResponseDatabaseListTypeDef",
    {
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTime": datetime,
        "CreateTableDefaultPermissions": List[
            ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientGetDatabasesResponseDatabaseListTypeDef(_ClientGetDatabasesResponseDatabaseListTypeDef):
    """
    - *(dict) --*

      The ``Database`` object represents a logical grouping of tables that might reside in a Hive
      metastore or an RDBMS.
      - **Name** *(string) --*

        The name of the database. For Hive compatibility, this is folded to lowercase when it is
        stored.
    """


_ClientGetDatabasesResponseTypeDef = TypedDict(
    "_ClientGetDatabasesResponseTypeDef",
    {"DatabaseList": List[ClientGetDatabasesResponseDatabaseListTypeDef], "NextToken": str},
    total=False,
)


class ClientGetDatabasesResponseTypeDef(_ClientGetDatabasesResponseTypeDef):
    """
    - *(dict) --*

      - **DatabaseList** *(list) --*

        A list of ``Database`` objects from the specified catalog.
        - *(dict) --*

          The ``Database`` object represents a logical grouping of tables that might reside in a
          Hive metastore or an RDBMS.
          - **Name** *(string) --*

            The name of the database. For Hive compatibility, this is folded to lowercase when it is
            stored.
    """


_ClientGetDataflowGraphResponseDagEdgesTypeDef = TypedDict(
    "_ClientGetDataflowGraphResponseDagEdgesTypeDef",
    {"Source": str, "Target": str, "TargetParameter": str},
    total=False,
)


class ClientGetDataflowGraphResponseDagEdgesTypeDef(_ClientGetDataflowGraphResponseDagEdgesTypeDef):
    pass


_ClientGetDataflowGraphResponseDagNodesArgsTypeDef = TypedDict(
    "_ClientGetDataflowGraphResponseDagNodesArgsTypeDef",
    {"Name": str, "Value": str, "Param": bool},
    total=False,
)


class ClientGetDataflowGraphResponseDagNodesArgsTypeDef(
    _ClientGetDataflowGraphResponseDagNodesArgsTypeDef
):
    pass


_ClientGetDataflowGraphResponseDagNodesTypeDef = TypedDict(
    "_ClientGetDataflowGraphResponseDagNodesTypeDef",
    {
        "Id": str,
        "NodeType": str,
        "Args": List[ClientGetDataflowGraphResponseDagNodesArgsTypeDef],
        "LineNumber": int,
    },
    total=False,
)


class ClientGetDataflowGraphResponseDagNodesTypeDef(_ClientGetDataflowGraphResponseDagNodesTypeDef):
    """
    - *(dict) --*

      Represents a node in a directed acyclic graph (DAG)
      - **Id** *(string) --*

        A node identifier that is unique within the node's graph.
    """


_ClientGetDataflowGraphResponseTypeDef = TypedDict(
    "_ClientGetDataflowGraphResponseTypeDef",
    {
        "DagNodes": List[ClientGetDataflowGraphResponseDagNodesTypeDef],
        "DagEdges": List[ClientGetDataflowGraphResponseDagEdgesTypeDef],
    },
    total=False,
)


class ClientGetDataflowGraphResponseTypeDef(_ClientGetDataflowGraphResponseTypeDef):
    """
    - *(dict) --*

      - **DagNodes** *(list) --*

        A list of the nodes in the resulting DAG.
        - *(dict) --*

          Represents a node in a directed acyclic graph (DAG)
          - **Id** *(string) --*

            A node identifier that is unique within the node's graph.
    """


_ClientGetDevEndpointResponseDevEndpointTypeDef = TypedDict(
    "_ClientGetDevEndpointResponseDevEndpointTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "YarnEndpointAddress": str,
        "PrivateAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "PublicAddress": str,
        "Status": str,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "NumberOfNodes": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "LastUpdateStatus": str,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "PublicKey": str,
        "PublicKeys": List[str],
        "SecurityConfiguration": str,
        "Arguments": Dict[str, str],
    },
    total=False,
)


class ClientGetDevEndpointResponseDevEndpointTypeDef(
    _ClientGetDevEndpointResponseDevEndpointTypeDef
):
    """
    - **DevEndpoint** *(dict) --*

      A ``DevEndpoint`` definition.
      - **EndpointName** *(string) --*

        The name of the ``DevEndpoint`` .
    """


_ClientGetDevEndpointResponseTypeDef = TypedDict(
    "_ClientGetDevEndpointResponseTypeDef",
    {"DevEndpoint": ClientGetDevEndpointResponseDevEndpointTypeDef},
    total=False,
)


class ClientGetDevEndpointResponseTypeDef(_ClientGetDevEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **DevEndpoint** *(dict) --*

        A ``DevEndpoint`` definition.
        - **EndpointName** *(string) --*

          The name of the ``DevEndpoint`` .
    """


_ClientGetDevEndpointsResponseDevEndpointsTypeDef = TypedDict(
    "_ClientGetDevEndpointsResponseDevEndpointsTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "YarnEndpointAddress": str,
        "PrivateAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "PublicAddress": str,
        "Status": str,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "NumberOfNodes": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "LastUpdateStatus": str,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "PublicKey": str,
        "PublicKeys": List[str],
        "SecurityConfiguration": str,
        "Arguments": Dict[str, str],
    },
    total=False,
)


class ClientGetDevEndpointsResponseDevEndpointsTypeDef(
    _ClientGetDevEndpointsResponseDevEndpointsTypeDef
):
    """
    - *(dict) --*

      A development endpoint where a developer can remotely debug extract, transform, and load (ETL)
      scripts.
      - **EndpointName** *(string) --*

        The name of the ``DevEndpoint`` .
    """


_ClientGetDevEndpointsResponseTypeDef = TypedDict(
    "_ClientGetDevEndpointsResponseTypeDef",
    {"DevEndpoints": List[ClientGetDevEndpointsResponseDevEndpointsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetDevEndpointsResponseTypeDef(_ClientGetDevEndpointsResponseTypeDef):
    """
    - *(dict) --*

      - **DevEndpoints** *(list) --*

        A list of ``DevEndpoint`` definitions.
        - *(dict) --*

          A development endpoint where a developer can remotely debug extract, transform, and load
          (ETL) scripts.
          - **EndpointName** *(string) --*

            The name of the ``DevEndpoint`` .
    """


_ClientGetJobBookmarkResponseJobBookmarkEntryTypeDef = TypedDict(
    "_ClientGetJobBookmarkResponseJobBookmarkEntryTypeDef",
    {
        "JobName": str,
        "Version": int,
        "Run": int,
        "Attempt": int,
        "PreviousRunId": str,
        "RunId": str,
        "JobBookmark": str,
    },
    total=False,
)


class ClientGetJobBookmarkResponseJobBookmarkEntryTypeDef(
    _ClientGetJobBookmarkResponseJobBookmarkEntryTypeDef
):
    """
    - **JobBookmarkEntry** *(dict) --*

      A structure that defines a point that a job can resume processing.
      - **JobName** *(string) --*

        The name of the job in question.
    """


_ClientGetJobBookmarkResponseTypeDef = TypedDict(
    "_ClientGetJobBookmarkResponseTypeDef",
    {"JobBookmarkEntry": ClientGetJobBookmarkResponseJobBookmarkEntryTypeDef},
    total=False,
)


class ClientGetJobBookmarkResponseTypeDef(_ClientGetJobBookmarkResponseTypeDef):
    """
    - *(dict) --*

      - **JobBookmarkEntry** *(dict) --*

        A structure that defines a point that a job can resume processing.
        - **JobName** *(string) --*

          The name of the job in question.
    """


_ClientGetJobResponseJobCommandTypeDef = TypedDict(
    "_ClientGetJobResponseJobCommandTypeDef",
    {"Name": str, "ScriptLocation": str, "PythonVersion": str},
    total=False,
)


class ClientGetJobResponseJobCommandTypeDef(_ClientGetJobResponseJobCommandTypeDef):
    pass


_ClientGetJobResponseJobConnectionsTypeDef = TypedDict(
    "_ClientGetJobResponseJobConnectionsTypeDef", {"Connections": List[str]}, total=False
)


class ClientGetJobResponseJobConnectionsTypeDef(_ClientGetJobResponseJobConnectionsTypeDef):
    pass


_ClientGetJobResponseJobExecutionPropertyTypeDef = TypedDict(
    "_ClientGetJobResponseJobExecutionPropertyTypeDef", {"MaxConcurrentRuns": int}, total=False
)


class ClientGetJobResponseJobExecutionPropertyTypeDef(
    _ClientGetJobResponseJobExecutionPropertyTypeDef
):
    pass


_ClientGetJobResponseJobNotificationPropertyTypeDef = TypedDict(
    "_ClientGetJobResponseJobNotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)


class ClientGetJobResponseJobNotificationPropertyTypeDef(
    _ClientGetJobResponseJobNotificationPropertyTypeDef
):
    pass


_ClientGetJobResponseJobTypeDef = TypedDict(
    "_ClientGetJobResponseJobTypeDef",
    {
        "Name": str,
        "Description": str,
        "LogUri": str,
        "Role": str,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "ExecutionProperty": ClientGetJobResponseJobExecutionPropertyTypeDef,
        "Command": ClientGetJobResponseJobCommandTypeDef,
        "DefaultArguments": Dict[str, str],
        "Connections": ClientGetJobResponseJobConnectionsTypeDef,
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetJobResponseJobNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class ClientGetJobResponseJobTypeDef(_ClientGetJobResponseJobTypeDef):
    """
    - **Job** *(dict) --*

      The requested job definition.
      - **Name** *(string) --*

        The name you assign to this job definition.
    """


_ClientGetJobResponseTypeDef = TypedDict(
    "_ClientGetJobResponseTypeDef", {"Job": ClientGetJobResponseJobTypeDef}, total=False
)


class ClientGetJobResponseTypeDef(_ClientGetJobResponseTypeDef):
    """
    - *(dict) --*

      - **Job** *(dict) --*

        The requested job definition.
        - **Name** *(string) --*

          The name you assign to this job definition.
    """


_ClientGetJobRunResponseJobRunNotificationPropertyTypeDef = TypedDict(
    "_ClientGetJobRunResponseJobRunNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientGetJobRunResponseJobRunNotificationPropertyTypeDef(
    _ClientGetJobRunResponseJobRunNotificationPropertyTypeDef
):
    pass


_ClientGetJobRunResponseJobRunPredecessorRunsTypeDef = TypedDict(
    "_ClientGetJobRunResponseJobRunPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)


class ClientGetJobRunResponseJobRunPredecessorRunsTypeDef(
    _ClientGetJobRunResponseJobRunPredecessorRunsTypeDef
):
    pass


_ClientGetJobRunResponseJobRunTypeDef = TypedDict(
    "_ClientGetJobRunResponseJobRunTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[ClientGetJobRunResponseJobRunPredecessorRunsTypeDef],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientGetJobRunResponseJobRunNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class ClientGetJobRunResponseJobRunTypeDef(_ClientGetJobRunResponseJobRunTypeDef):
    """
    - **JobRun** *(dict) --*

      The requested job-run metadata.
      - **Id** *(string) --*

        The ID of this job run.
    """


_ClientGetJobRunResponseTypeDef = TypedDict(
    "_ClientGetJobRunResponseTypeDef", {"JobRun": ClientGetJobRunResponseJobRunTypeDef}, total=False
)


class ClientGetJobRunResponseTypeDef(_ClientGetJobRunResponseTypeDef):
    """
    - *(dict) --*

      - **JobRun** *(dict) --*

        The requested job-run metadata.
        - **Id** *(string) --*

          The ID of this job run.
    """


_ClientGetJobRunsResponseJobRunsNotificationPropertyTypeDef = TypedDict(
    "_ClientGetJobRunsResponseJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientGetJobRunsResponseJobRunsNotificationPropertyTypeDef(
    _ClientGetJobRunsResponseJobRunsNotificationPropertyTypeDef
):
    pass


_ClientGetJobRunsResponseJobRunsPredecessorRunsTypeDef = TypedDict(
    "_ClientGetJobRunsResponseJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)


class ClientGetJobRunsResponseJobRunsPredecessorRunsTypeDef(
    _ClientGetJobRunsResponseJobRunsPredecessorRunsTypeDef
):
    pass


_ClientGetJobRunsResponseJobRunsTypeDef = TypedDict(
    "_ClientGetJobRunsResponseJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[ClientGetJobRunsResponseJobRunsPredecessorRunsTypeDef],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientGetJobRunsResponseJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class ClientGetJobRunsResponseJobRunsTypeDef(_ClientGetJobRunsResponseJobRunsTypeDef):
    """
    - *(dict) --*

      Contains information about a job run.
      - **Id** *(string) --*

        The ID of this job run.
    """


_ClientGetJobRunsResponseTypeDef = TypedDict(
    "_ClientGetJobRunsResponseTypeDef",
    {"JobRuns": List[ClientGetJobRunsResponseJobRunsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetJobRunsResponseTypeDef(_ClientGetJobRunsResponseTypeDef):
    """
    - *(dict) --*

      - **JobRuns** *(list) --*

        A list of job-run metadata objects.
        - *(dict) --*

          Contains information about a job run.
          - **Id** *(string) --*

            The ID of this job run.
    """


_ClientGetJobsResponseJobsCommandTypeDef = TypedDict(
    "_ClientGetJobsResponseJobsCommandTypeDef",
    {"Name": str, "ScriptLocation": str, "PythonVersion": str},
    total=False,
)


class ClientGetJobsResponseJobsCommandTypeDef(_ClientGetJobsResponseJobsCommandTypeDef):
    pass


_ClientGetJobsResponseJobsConnectionsTypeDef = TypedDict(
    "_ClientGetJobsResponseJobsConnectionsTypeDef", {"Connections": List[str]}, total=False
)


class ClientGetJobsResponseJobsConnectionsTypeDef(_ClientGetJobsResponseJobsConnectionsTypeDef):
    pass


_ClientGetJobsResponseJobsExecutionPropertyTypeDef = TypedDict(
    "_ClientGetJobsResponseJobsExecutionPropertyTypeDef", {"MaxConcurrentRuns": int}, total=False
)


class ClientGetJobsResponseJobsExecutionPropertyTypeDef(
    _ClientGetJobsResponseJobsExecutionPropertyTypeDef
):
    pass


_ClientGetJobsResponseJobsNotificationPropertyTypeDef = TypedDict(
    "_ClientGetJobsResponseJobsNotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)


class ClientGetJobsResponseJobsNotificationPropertyTypeDef(
    _ClientGetJobsResponseJobsNotificationPropertyTypeDef
):
    pass


_ClientGetJobsResponseJobsTypeDef = TypedDict(
    "_ClientGetJobsResponseJobsTypeDef",
    {
        "Name": str,
        "Description": str,
        "LogUri": str,
        "Role": str,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "ExecutionProperty": ClientGetJobsResponseJobsExecutionPropertyTypeDef,
        "Command": ClientGetJobsResponseJobsCommandTypeDef,
        "DefaultArguments": Dict[str, str],
        "Connections": ClientGetJobsResponseJobsConnectionsTypeDef,
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetJobsResponseJobsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class ClientGetJobsResponseJobsTypeDef(_ClientGetJobsResponseJobsTypeDef):
    """
    - *(dict) --*

      Specifies a job definition.
      - **Name** *(string) --*

        The name you assign to this job definition.
    """


_ClientGetJobsResponseTypeDef = TypedDict(
    "_ClientGetJobsResponseTypeDef",
    {"Jobs": List[ClientGetJobsResponseJobsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetJobsResponseTypeDef(_ClientGetJobsResponseTypeDef):
    """
    - *(dict) --*

      - **Jobs** *(list) --*

        A list of job definitions.
        - *(dict) --*

          Specifies a job definition.
          - **Name** *(string) --*

            The name you assign to this job definition.
    """


_ClientGetMappingLocationDynamoDBTypeDef = TypedDict(
    "_ClientGetMappingLocationDynamoDBTypeDef",
    {"Name": str, "Value": str, "Param": bool},
    total=False,
)


class ClientGetMappingLocationDynamoDBTypeDef(_ClientGetMappingLocationDynamoDBTypeDef):
    pass


_RequiredClientGetMappingLocationJdbcTypeDef = TypedDict(
    "_RequiredClientGetMappingLocationJdbcTypeDef", {"Name": str}
)
_OptionalClientGetMappingLocationJdbcTypeDef = TypedDict(
    "_OptionalClientGetMappingLocationJdbcTypeDef", {"Value": str, "Param": bool}, total=False
)


class ClientGetMappingLocationJdbcTypeDef(
    _RequiredClientGetMappingLocationJdbcTypeDef, _OptionalClientGetMappingLocationJdbcTypeDef
):
    """
    - *(dict) --*

      An argument or property of a node.
      - **Name** *(string) --***[REQUIRED]**

        The name of the argument or property.
    """


_ClientGetMappingLocationS3TypeDef = TypedDict(
    "_ClientGetMappingLocationS3TypeDef", {"Name": str, "Value": str, "Param": bool}, total=False
)


class ClientGetMappingLocationS3TypeDef(_ClientGetMappingLocationS3TypeDef):
    pass


_ClientGetMappingLocationTypeDef = TypedDict(
    "_ClientGetMappingLocationTypeDef",
    {
        "Jdbc": List[ClientGetMappingLocationJdbcTypeDef],
        "S3": List[ClientGetMappingLocationS3TypeDef],
        "DynamoDB": List[ClientGetMappingLocationDynamoDBTypeDef],
    },
    total=False,
)


class ClientGetMappingLocationTypeDef(_ClientGetMappingLocationTypeDef):
    """
    Parameters for the mapping.
    - **Jdbc** *(list) --*

      A JDBC location.
      - *(dict) --*

        An argument or property of a node.
        - **Name** *(string) --***[REQUIRED]**

          The name of the argument or property.
    """


_ClientGetMappingResponseMappingTypeDef = TypedDict(
    "_ClientGetMappingResponseMappingTypeDef",
    {
        "SourceTable": str,
        "SourcePath": str,
        "SourceType": str,
        "TargetTable": str,
        "TargetPath": str,
        "TargetType": str,
    },
    total=False,
)


class ClientGetMappingResponseMappingTypeDef(_ClientGetMappingResponseMappingTypeDef):
    """
    - *(dict) --*

      Defines a mapping.
      - **SourceTable** *(string) --*

        The name of the source table.
    """


_ClientGetMappingResponseTypeDef = TypedDict(
    "_ClientGetMappingResponseTypeDef",
    {"Mapping": List[ClientGetMappingResponseMappingTypeDef]},
    total=False,
)


class ClientGetMappingResponseTypeDef(_ClientGetMappingResponseTypeDef):
    """
    - *(dict) --*

      - **Mapping** *(list) --*

        A list of mappings to the specified targets.
        - *(dict) --*

          Defines a mapping.
          - **SourceTable** *(string) --*

            The name of the source table.
    """


_RequiredClientGetMappingSinksTypeDef = TypedDict(
    "_RequiredClientGetMappingSinksTypeDef", {"DatabaseName": str}
)
_OptionalClientGetMappingSinksTypeDef = TypedDict(
    "_OptionalClientGetMappingSinksTypeDef", {"TableName": str}, total=False
)


class ClientGetMappingSinksTypeDef(
    _RequiredClientGetMappingSinksTypeDef, _OptionalClientGetMappingSinksTypeDef
):
    """
    - *(dict) --*

      Specifies a table definition in the AWS Glue Data Catalog.
      - **DatabaseName** *(string) --***[REQUIRED]**

        The database in which the table metadata resides.
    """


_RequiredClientGetMappingSourceTypeDef = TypedDict(
    "_RequiredClientGetMappingSourceTypeDef", {"DatabaseName": str}
)
_OptionalClientGetMappingSourceTypeDef = TypedDict(
    "_OptionalClientGetMappingSourceTypeDef", {"TableName": str}, total=False
)


class ClientGetMappingSourceTypeDef(
    _RequiredClientGetMappingSourceTypeDef, _OptionalClientGetMappingSourceTypeDef
):
    """
    Specifies the source table.
    - **DatabaseName** *(string) --***[REQUIRED]**

      The database in which the table metadata resides.
    """


_ClientGetMlTaskRunResponsePropertiesExportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "_ClientGetMlTaskRunResponsePropertiesExportLabelsTaskRunPropertiesTypeDef",
    {"OutputS3Path": str},
    total=False,
)


class ClientGetMlTaskRunResponsePropertiesExportLabelsTaskRunPropertiesTypeDef(
    _ClientGetMlTaskRunResponsePropertiesExportLabelsTaskRunPropertiesTypeDef
):
    pass


_ClientGetMlTaskRunResponsePropertiesFindMatchesTaskRunPropertiesTypeDef = TypedDict(
    "_ClientGetMlTaskRunResponsePropertiesFindMatchesTaskRunPropertiesTypeDef",
    {"JobId": str, "JobName": str, "JobRunId": str},
    total=False,
)


class ClientGetMlTaskRunResponsePropertiesFindMatchesTaskRunPropertiesTypeDef(
    _ClientGetMlTaskRunResponsePropertiesFindMatchesTaskRunPropertiesTypeDef
):
    pass


_ClientGetMlTaskRunResponsePropertiesImportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "_ClientGetMlTaskRunResponsePropertiesImportLabelsTaskRunPropertiesTypeDef",
    {"InputS3Path": str, "Replace": bool},
    total=False,
)


class ClientGetMlTaskRunResponsePropertiesImportLabelsTaskRunPropertiesTypeDef(
    _ClientGetMlTaskRunResponsePropertiesImportLabelsTaskRunPropertiesTypeDef
):
    pass


_ClientGetMlTaskRunResponsePropertiesLabelingSetGenerationTaskRunPropertiesTypeDef = TypedDict(
    "_ClientGetMlTaskRunResponsePropertiesLabelingSetGenerationTaskRunPropertiesTypeDef",
    {"OutputS3Path": str},
    total=False,
)


class ClientGetMlTaskRunResponsePropertiesLabelingSetGenerationTaskRunPropertiesTypeDef(
    _ClientGetMlTaskRunResponsePropertiesLabelingSetGenerationTaskRunPropertiesTypeDef
):
    pass


_ClientGetMlTaskRunResponsePropertiesTypeDef = TypedDict(
    "_ClientGetMlTaskRunResponsePropertiesTypeDef",
    {
        "TaskType": Literal[
            "EVALUATION",
            "LABELING_SET_GENERATION",
            "IMPORT_LABELS",
            "EXPORT_LABELS",
            "FIND_MATCHES",
        ],
        "ImportLabelsTaskRunProperties": ClientGetMlTaskRunResponsePropertiesImportLabelsTaskRunPropertiesTypeDef,
        "ExportLabelsTaskRunProperties": ClientGetMlTaskRunResponsePropertiesExportLabelsTaskRunPropertiesTypeDef,
        "LabelingSetGenerationTaskRunProperties": ClientGetMlTaskRunResponsePropertiesLabelingSetGenerationTaskRunPropertiesTypeDef,
        "FindMatchesTaskRunProperties": ClientGetMlTaskRunResponsePropertiesFindMatchesTaskRunPropertiesTypeDef,
    },
    total=False,
)


class ClientGetMlTaskRunResponsePropertiesTypeDef(_ClientGetMlTaskRunResponsePropertiesTypeDef):
    pass


_ClientGetMlTaskRunResponseTypeDef = TypedDict(
    "_ClientGetMlTaskRunResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "LogGroupName": str,
        "Properties": ClientGetMlTaskRunResponsePropertiesTypeDef,
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
    },
    total=False,
)


class ClientGetMlTaskRunResponseTypeDef(_ClientGetMlTaskRunResponseTypeDef):
    """
    - *(dict) --*

      - **TransformId** *(string) --*

        The unique identifier of the task run.
    """


_ClientGetMlTaskRunsFilterTypeDef = TypedDict(
    "_ClientGetMlTaskRunsFilterTypeDef",
    {
        "TaskRunType": Literal[
            "EVALUATION",
            "LABELING_SET_GENERATION",
            "IMPORT_LABELS",
            "EXPORT_LABELS",
            "FIND_MATCHES",
        ],
        "Status": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "StartedBefore": datetime,
        "StartedAfter": datetime,
    },
    total=False,
)


class ClientGetMlTaskRunsFilterTypeDef(_ClientGetMlTaskRunsFilterTypeDef):
    """
    The filter criteria, in the ``TaskRunFilterCriteria`` structure, for the task run.
    - **TaskRunType** *(string) --*

      The type of task run.
    """


_ClientGetMlTaskRunsResponseTaskRunsPropertiesExportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "_ClientGetMlTaskRunsResponseTaskRunsPropertiesExportLabelsTaskRunPropertiesTypeDef",
    {"OutputS3Path": str},
    total=False,
)


class ClientGetMlTaskRunsResponseTaskRunsPropertiesExportLabelsTaskRunPropertiesTypeDef(
    _ClientGetMlTaskRunsResponseTaskRunsPropertiesExportLabelsTaskRunPropertiesTypeDef
):
    pass


_ClientGetMlTaskRunsResponseTaskRunsPropertiesFindMatchesTaskRunPropertiesTypeDef = TypedDict(
    "_ClientGetMlTaskRunsResponseTaskRunsPropertiesFindMatchesTaskRunPropertiesTypeDef",
    {"JobId": str, "JobName": str, "JobRunId": str},
    total=False,
)


class ClientGetMlTaskRunsResponseTaskRunsPropertiesFindMatchesTaskRunPropertiesTypeDef(
    _ClientGetMlTaskRunsResponseTaskRunsPropertiesFindMatchesTaskRunPropertiesTypeDef
):
    pass


_ClientGetMlTaskRunsResponseTaskRunsPropertiesImportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "_ClientGetMlTaskRunsResponseTaskRunsPropertiesImportLabelsTaskRunPropertiesTypeDef",
    {"InputS3Path": str, "Replace": bool},
    total=False,
)


class ClientGetMlTaskRunsResponseTaskRunsPropertiesImportLabelsTaskRunPropertiesTypeDef(
    _ClientGetMlTaskRunsResponseTaskRunsPropertiesImportLabelsTaskRunPropertiesTypeDef
):
    pass


_ClientGetMlTaskRunsResponseTaskRunsPropertiesLabelingSetGenerationTaskRunPropertiesTypeDef = TypedDict(
    "_ClientGetMlTaskRunsResponseTaskRunsPropertiesLabelingSetGenerationTaskRunPropertiesTypeDef",
    {"OutputS3Path": str},
    total=False,
)


class ClientGetMlTaskRunsResponseTaskRunsPropertiesLabelingSetGenerationTaskRunPropertiesTypeDef(
    _ClientGetMlTaskRunsResponseTaskRunsPropertiesLabelingSetGenerationTaskRunPropertiesTypeDef
):
    pass


_ClientGetMlTaskRunsResponseTaskRunsPropertiesTypeDef = TypedDict(
    "_ClientGetMlTaskRunsResponseTaskRunsPropertiesTypeDef",
    {
        "TaskType": Literal[
            "EVALUATION",
            "LABELING_SET_GENERATION",
            "IMPORT_LABELS",
            "EXPORT_LABELS",
            "FIND_MATCHES",
        ],
        "ImportLabelsTaskRunProperties": ClientGetMlTaskRunsResponseTaskRunsPropertiesImportLabelsTaskRunPropertiesTypeDef,
        "ExportLabelsTaskRunProperties": ClientGetMlTaskRunsResponseTaskRunsPropertiesExportLabelsTaskRunPropertiesTypeDef,
        "LabelingSetGenerationTaskRunProperties": ClientGetMlTaskRunsResponseTaskRunsPropertiesLabelingSetGenerationTaskRunPropertiesTypeDef,
        "FindMatchesTaskRunProperties": ClientGetMlTaskRunsResponseTaskRunsPropertiesFindMatchesTaskRunPropertiesTypeDef,
    },
    total=False,
)


class ClientGetMlTaskRunsResponseTaskRunsPropertiesTypeDef(
    _ClientGetMlTaskRunsResponseTaskRunsPropertiesTypeDef
):
    pass


_ClientGetMlTaskRunsResponseTaskRunsTypeDef = TypedDict(
    "_ClientGetMlTaskRunsResponseTaskRunsTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "LogGroupName": str,
        "Properties": ClientGetMlTaskRunsResponseTaskRunsPropertiesTypeDef,
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
    },
    total=False,
)


class ClientGetMlTaskRunsResponseTaskRunsTypeDef(_ClientGetMlTaskRunsResponseTaskRunsTypeDef):
    """
    - *(dict) --*

      The sampling parameters that are associated with the machine learning transform.
      - **TransformId** *(string) --*

        The unique identifier for the transform.
    """


_ClientGetMlTaskRunsResponseTypeDef = TypedDict(
    "_ClientGetMlTaskRunsResponseTypeDef",
    {"TaskRuns": List[ClientGetMlTaskRunsResponseTaskRunsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetMlTaskRunsResponseTypeDef(_ClientGetMlTaskRunsResponseTypeDef):
    """
    - *(dict) --*

      - **TaskRuns** *(list) --*

        A list of task runs that are associated with the transform.
        - *(dict) --*

          The sampling parameters that are associated with the machine learning transform.
          - **TransformId** *(string) --*

            The unique identifier for the transform.
    """


_RequiredClientGetMlTaskRunsSortTypeDef = TypedDict(
    "_RequiredClientGetMlTaskRunsSortTypeDef",
    {"Column": Literal["TASK_RUN_TYPE", "STATUS", "STARTED"]},
)
_OptionalClientGetMlTaskRunsSortTypeDef = TypedDict(
    "_OptionalClientGetMlTaskRunsSortTypeDef",
    {"SortDirection": Literal["DESCENDING", "ASCENDING"]},
    total=False,
)


class ClientGetMlTaskRunsSortTypeDef(
    _RequiredClientGetMlTaskRunsSortTypeDef, _OptionalClientGetMlTaskRunsSortTypeDef
):
    """
    The sorting criteria, in the ``TaskRunSortCriteria`` structure, for the task run.
    - **Column** *(string) --***[REQUIRED]**

      The column to be used to sort the list of task runs for the machine learning transform.
    """


_ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef = TypedDict(
    "_ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef",
    {
        "NumTruePositives": int,
        "NumFalsePositives": int,
        "NumTrueNegatives": int,
        "NumFalseNegatives": int,
    },
    total=False,
)


class ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef(
    _ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef
):
    pass


_ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsTypeDef = TypedDict(
    "_ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsTypeDef",
    {
        "AreaUnderPRCurve": float,
        "Precision": float,
        "Recall": float,
        "F1": float,
        "ConfusionMatrix": ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef,
    },
    total=False,
)


class ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsTypeDef(
    _ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsTypeDef
):
    pass


_ClientGetMlTransformResponseEvaluationMetricsTypeDef = TypedDict(
    "_ClientGetMlTransformResponseEvaluationMetricsTypeDef",
    {
        "TransformType": str,
        "FindMatchesMetrics": ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsTypeDef,
    },
    total=False,
)


class ClientGetMlTransformResponseEvaluationMetricsTypeDef(
    _ClientGetMlTransformResponseEvaluationMetricsTypeDef
):
    pass


_ClientGetMlTransformResponseInputRecordTablesTypeDef = TypedDict(
    "_ClientGetMlTransformResponseInputRecordTablesTypeDef",
    {"DatabaseName": str, "TableName": str, "CatalogId": str, "ConnectionName": str},
    total=False,
)


class ClientGetMlTransformResponseInputRecordTablesTypeDef(
    _ClientGetMlTransformResponseInputRecordTablesTypeDef
):
    pass


_ClientGetMlTransformResponseParametersFindMatchesParametersTypeDef = TypedDict(
    "_ClientGetMlTransformResponseParametersFindMatchesParametersTypeDef",
    {
        "PrimaryKeyColumnName": str,
        "PrecisionRecallTradeoff": float,
        "AccuracyCostTradeoff": float,
        "EnforceProvidedLabels": bool,
    },
    total=False,
)


class ClientGetMlTransformResponseParametersFindMatchesParametersTypeDef(
    _ClientGetMlTransformResponseParametersFindMatchesParametersTypeDef
):
    pass


_ClientGetMlTransformResponseParametersTypeDef = TypedDict(
    "_ClientGetMlTransformResponseParametersTypeDef",
    {
        "TransformType": str,
        "FindMatchesParameters": ClientGetMlTransformResponseParametersFindMatchesParametersTypeDef,
    },
    total=False,
)


class ClientGetMlTransformResponseParametersTypeDef(_ClientGetMlTransformResponseParametersTypeDef):
    pass


_ClientGetMlTransformResponseSchemaTypeDef = TypedDict(
    "_ClientGetMlTransformResponseSchemaTypeDef", {"Name": str, "DataType": str}, total=False
)


class ClientGetMlTransformResponseSchemaTypeDef(_ClientGetMlTransformResponseSchemaTypeDef):
    pass


_ClientGetMlTransformResponseTypeDef = TypedDict(
    "_ClientGetMlTransformResponseTypeDef",
    {
        "TransformId": str,
        "Name": str,
        "Description": str,
        "Status": Literal["NOT_READY", "READY", "DELETING"],
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "InputRecordTables": List[ClientGetMlTransformResponseInputRecordTablesTypeDef],
        "Parameters": ClientGetMlTransformResponseParametersTypeDef,
        "EvaluationMetrics": ClientGetMlTransformResponseEvaluationMetricsTypeDef,
        "LabelCount": int,
        "Schema": List[ClientGetMlTransformResponseSchemaTypeDef],
        "Role": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
    },
    total=False,
)


class ClientGetMlTransformResponseTypeDef(_ClientGetMlTransformResponseTypeDef):
    """
    - *(dict) --*

      - **TransformId** *(string) --*

        The unique identifier of the transform, generated at the time that the transform was
        created.
    """


_ClientGetMlTransformsFilterSchemaTypeDef = TypedDict(
    "_ClientGetMlTransformsFilterSchemaTypeDef", {"Name": str, "DataType": str}, total=False
)


class ClientGetMlTransformsFilterSchemaTypeDef(_ClientGetMlTransformsFilterSchemaTypeDef):
    pass


_ClientGetMlTransformsFilterTypeDef = TypedDict(
    "_ClientGetMlTransformsFilterTypeDef",
    {
        "Name": str,
        "TransformType": str,
        "Status": Literal["NOT_READY", "READY", "DELETING"],
        "GlueVersion": str,
        "CreatedBefore": datetime,
        "CreatedAfter": datetime,
        "LastModifiedBefore": datetime,
        "LastModifiedAfter": datetime,
        "Schema": List[ClientGetMlTransformsFilterSchemaTypeDef],
    },
    total=False,
)


class ClientGetMlTransformsFilterTypeDef(_ClientGetMlTransformsFilterTypeDef):
    """
    The filter transformation criteria.
    - **Name** *(string) --*

      A unique transform name that is used to filter the machine learning transforms.
    """


_ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef = TypedDict(
    "_ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef",
    {
        "NumTruePositives": int,
        "NumFalsePositives": int,
        "NumTrueNegatives": int,
        "NumFalseNegatives": int,
    },
    total=False,
)


class ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef(
    _ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef
):
    pass


_ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsTypeDef = TypedDict(
    "_ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsTypeDef",
    {
        "AreaUnderPRCurve": float,
        "Precision": float,
        "Recall": float,
        "F1": float,
        "ConfusionMatrix": ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef,
    },
    total=False,
)


class ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsTypeDef(
    _ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsTypeDef
):
    pass


_ClientGetMlTransformsResponseTransformsEvaluationMetricsTypeDef = TypedDict(
    "_ClientGetMlTransformsResponseTransformsEvaluationMetricsTypeDef",
    {
        "TransformType": str,
        "FindMatchesMetrics": ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsTypeDef,
    },
    total=False,
)


class ClientGetMlTransformsResponseTransformsEvaluationMetricsTypeDef(
    _ClientGetMlTransformsResponseTransformsEvaluationMetricsTypeDef
):
    pass


_ClientGetMlTransformsResponseTransformsInputRecordTablesTypeDef = TypedDict(
    "_ClientGetMlTransformsResponseTransformsInputRecordTablesTypeDef",
    {"DatabaseName": str, "TableName": str, "CatalogId": str, "ConnectionName": str},
    total=False,
)


class ClientGetMlTransformsResponseTransformsInputRecordTablesTypeDef(
    _ClientGetMlTransformsResponseTransformsInputRecordTablesTypeDef
):
    pass


_ClientGetMlTransformsResponseTransformsParametersFindMatchesParametersTypeDef = TypedDict(
    "_ClientGetMlTransformsResponseTransformsParametersFindMatchesParametersTypeDef",
    {
        "PrimaryKeyColumnName": str,
        "PrecisionRecallTradeoff": float,
        "AccuracyCostTradeoff": float,
        "EnforceProvidedLabels": bool,
    },
    total=False,
)


class ClientGetMlTransformsResponseTransformsParametersFindMatchesParametersTypeDef(
    _ClientGetMlTransformsResponseTransformsParametersFindMatchesParametersTypeDef
):
    pass


_ClientGetMlTransformsResponseTransformsParametersTypeDef = TypedDict(
    "_ClientGetMlTransformsResponseTransformsParametersTypeDef",
    {
        "TransformType": str,
        "FindMatchesParameters": ClientGetMlTransformsResponseTransformsParametersFindMatchesParametersTypeDef,
    },
    total=False,
)


class ClientGetMlTransformsResponseTransformsParametersTypeDef(
    _ClientGetMlTransformsResponseTransformsParametersTypeDef
):
    pass


_ClientGetMlTransformsResponseTransformsSchemaTypeDef = TypedDict(
    "_ClientGetMlTransformsResponseTransformsSchemaTypeDef",
    {"Name": str, "DataType": str},
    total=False,
)


class ClientGetMlTransformsResponseTransformsSchemaTypeDef(
    _ClientGetMlTransformsResponseTransformsSchemaTypeDef
):
    pass


_ClientGetMlTransformsResponseTransformsTypeDef = TypedDict(
    "_ClientGetMlTransformsResponseTransformsTypeDef",
    {
        "TransformId": str,
        "Name": str,
        "Description": str,
        "Status": Literal["NOT_READY", "READY", "DELETING"],
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "InputRecordTables": List[ClientGetMlTransformsResponseTransformsInputRecordTablesTypeDef],
        "Parameters": ClientGetMlTransformsResponseTransformsParametersTypeDef,
        "EvaluationMetrics": ClientGetMlTransformsResponseTransformsEvaluationMetricsTypeDef,
        "LabelCount": int,
        "Schema": List[ClientGetMlTransformsResponseTransformsSchemaTypeDef],
        "Role": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
    },
    total=False,
)


class ClientGetMlTransformsResponseTransformsTypeDef(
    _ClientGetMlTransformsResponseTransformsTypeDef
):
    """
    - *(dict) --*

      A structure for a machine learning transform.
      - **TransformId** *(string) --*

        The unique transform ID that is generated for the machine learning transform. The ID is
        guaranteed to be unique and does not change.
    """


_ClientGetMlTransformsResponseTypeDef = TypedDict(
    "_ClientGetMlTransformsResponseTypeDef",
    {"Transforms": List[ClientGetMlTransformsResponseTransformsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetMlTransformsResponseTypeDef(_ClientGetMlTransformsResponseTypeDef):
    """
    - *(dict) --*

      - **Transforms** *(list) --*

        A list of machine learning transforms.
        - *(dict) --*

          A structure for a machine learning transform.
          - **TransformId** *(string) --*

            The unique transform ID that is generated for the machine learning transform. The ID is
            guaranteed to be unique and does not change.
    """


_RequiredClientGetMlTransformsSortTypeDef = TypedDict(
    "_RequiredClientGetMlTransformsSortTypeDef",
    {"Column": Literal["NAME", "TRANSFORM_TYPE", "STATUS", "CREATED", "LAST_MODIFIED"]},
)
_OptionalClientGetMlTransformsSortTypeDef = TypedDict(
    "_OptionalClientGetMlTransformsSortTypeDef",
    {"SortDirection": Literal["DESCENDING", "ASCENDING"]},
    total=False,
)


class ClientGetMlTransformsSortTypeDef(
    _RequiredClientGetMlTransformsSortTypeDef, _OptionalClientGetMlTransformsSortTypeDef
):
    """
    The sorting criteria.
    - **Column** *(string) --***[REQUIRED]**

      The column to be used in the sorting criteria that are associated with the machine learning
      transform.
    """


_ClientGetPartitionResponsePartitionStorageDescriptorColumnsTypeDef = TypedDict(
    "_ClientGetPartitionResponsePartitionStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetPartitionResponsePartitionStorageDescriptorColumnsTypeDef(
    _ClientGetPartitionResponsePartitionStorageDescriptorColumnsTypeDef
):
    pass


_ClientGetPartitionResponsePartitionStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_ClientGetPartitionResponsePartitionStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetPartitionResponsePartitionStorageDescriptorSerdeInfoTypeDef(
    _ClientGetPartitionResponsePartitionStorageDescriptorSerdeInfoTypeDef
):
    pass


_ClientGetPartitionResponsePartitionStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_ClientGetPartitionResponsePartitionStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class ClientGetPartitionResponsePartitionStorageDescriptorSkewedInfoTypeDef(
    _ClientGetPartitionResponsePartitionStorageDescriptorSkewedInfoTypeDef
):
    pass


_ClientGetPartitionResponsePartitionStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_ClientGetPartitionResponsePartitionStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class ClientGetPartitionResponsePartitionStorageDescriptorSortColumnsTypeDef(
    _ClientGetPartitionResponsePartitionStorageDescriptorSortColumnsTypeDef
):
    pass


_ClientGetPartitionResponsePartitionStorageDescriptorTypeDef = TypedDict(
    "_ClientGetPartitionResponsePartitionStorageDescriptorTypeDef",
    {
        "Columns": List[ClientGetPartitionResponsePartitionStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientGetPartitionResponsePartitionStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientGetPartitionResponsePartitionStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientGetPartitionResponsePartitionStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class ClientGetPartitionResponsePartitionStorageDescriptorTypeDef(
    _ClientGetPartitionResponsePartitionStorageDescriptorTypeDef
):
    pass


_ClientGetPartitionResponsePartitionTypeDef = TypedDict(
    "_ClientGetPartitionResponsePartitionTypeDef",
    {
        "Values": List[str],
        "DatabaseName": str,
        "TableName": str,
        "CreationTime": datetime,
        "LastAccessTime": datetime,
        "StorageDescriptor": ClientGetPartitionResponsePartitionStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)


class ClientGetPartitionResponsePartitionTypeDef(_ClientGetPartitionResponsePartitionTypeDef):
    """
    - **Partition** *(dict) --*

      The requested information, in the form of a ``Partition`` object.
      - **Values** *(list) --*

        The values of the partition.
        - *(string) --*
    """


_ClientGetPartitionResponseTypeDef = TypedDict(
    "_ClientGetPartitionResponseTypeDef",
    {"Partition": ClientGetPartitionResponsePartitionTypeDef},
    total=False,
)


class ClientGetPartitionResponseTypeDef(_ClientGetPartitionResponseTypeDef):
    """
    - *(dict) --*

      - **Partition** *(dict) --*

        The requested information, in the form of a ``Partition`` object.
        - **Values** *(list) --*

          The values of the partition.
          - *(string) --*
    """


_ClientGetPartitionsResponsePartitionsStorageDescriptorColumnsTypeDef = TypedDict(
    "_ClientGetPartitionsResponsePartitionsStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetPartitionsResponsePartitionsStorageDescriptorColumnsTypeDef(
    _ClientGetPartitionsResponsePartitionsStorageDescriptorColumnsTypeDef
):
    pass


_ClientGetPartitionsResponsePartitionsStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_ClientGetPartitionsResponsePartitionsStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetPartitionsResponsePartitionsStorageDescriptorSerdeInfoTypeDef(
    _ClientGetPartitionsResponsePartitionsStorageDescriptorSerdeInfoTypeDef
):
    pass


_ClientGetPartitionsResponsePartitionsStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_ClientGetPartitionsResponsePartitionsStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class ClientGetPartitionsResponsePartitionsStorageDescriptorSkewedInfoTypeDef(
    _ClientGetPartitionsResponsePartitionsStorageDescriptorSkewedInfoTypeDef
):
    pass


_ClientGetPartitionsResponsePartitionsStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_ClientGetPartitionsResponsePartitionsStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class ClientGetPartitionsResponsePartitionsStorageDescriptorSortColumnsTypeDef(
    _ClientGetPartitionsResponsePartitionsStorageDescriptorSortColumnsTypeDef
):
    pass


_ClientGetPartitionsResponsePartitionsStorageDescriptorTypeDef = TypedDict(
    "_ClientGetPartitionsResponsePartitionsStorageDescriptorTypeDef",
    {
        "Columns": List[ClientGetPartitionsResponsePartitionsStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientGetPartitionsResponsePartitionsStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            ClientGetPartitionsResponsePartitionsStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientGetPartitionsResponsePartitionsStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class ClientGetPartitionsResponsePartitionsStorageDescriptorTypeDef(
    _ClientGetPartitionsResponsePartitionsStorageDescriptorTypeDef
):
    pass


_ClientGetPartitionsResponsePartitionsTypeDef = TypedDict(
    "_ClientGetPartitionsResponsePartitionsTypeDef",
    {
        "Values": List[str],
        "DatabaseName": str,
        "TableName": str,
        "CreationTime": datetime,
        "LastAccessTime": datetime,
        "StorageDescriptor": ClientGetPartitionsResponsePartitionsStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)


class ClientGetPartitionsResponsePartitionsTypeDef(_ClientGetPartitionsResponsePartitionsTypeDef):
    """
    - *(dict) --*

      Represents a slice of table data.
      - **Values** *(list) --*

        The values of the partition.
        - *(string) --*
    """


_ClientGetPartitionsResponseTypeDef = TypedDict(
    "_ClientGetPartitionsResponseTypeDef",
    {"Partitions": List[ClientGetPartitionsResponsePartitionsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetPartitionsResponseTypeDef(_ClientGetPartitionsResponseTypeDef):
    """
    - *(dict) --*

      - **Partitions** *(list) --*

        A list of requested partitions.
        - *(dict) --*

          Represents a slice of table data.
          - **Values** *(list) --*

            The values of the partition.
            - *(string) --*
    """


_RequiredClientGetPartitionsSegmentTypeDef = TypedDict(
    "_RequiredClientGetPartitionsSegmentTypeDef", {"SegmentNumber": int}
)
_OptionalClientGetPartitionsSegmentTypeDef = TypedDict(
    "_OptionalClientGetPartitionsSegmentTypeDef", {"TotalSegments": int}, total=False
)


class ClientGetPartitionsSegmentTypeDef(
    _RequiredClientGetPartitionsSegmentTypeDef, _OptionalClientGetPartitionsSegmentTypeDef
):
    """
    The segment of the table's partitions to scan in this request.
    - **SegmentNumber** *(integer) --***[REQUIRED]**

      The zero-based index number of the segment. For example, if the total number of segments is 4,
      ``SegmentNumber`` values range from 0 through 3.
    """


_ClientGetPlanLocationDynamoDBTypeDef = TypedDict(
    "_ClientGetPlanLocationDynamoDBTypeDef", {"Name": str, "Value": str, "Param": bool}, total=False
)


class ClientGetPlanLocationDynamoDBTypeDef(_ClientGetPlanLocationDynamoDBTypeDef):
    pass


_RequiredClientGetPlanLocationJdbcTypeDef = TypedDict(
    "_RequiredClientGetPlanLocationJdbcTypeDef", {"Name": str}
)
_OptionalClientGetPlanLocationJdbcTypeDef = TypedDict(
    "_OptionalClientGetPlanLocationJdbcTypeDef", {"Value": str, "Param": bool}, total=False
)


class ClientGetPlanLocationJdbcTypeDef(
    _RequiredClientGetPlanLocationJdbcTypeDef, _OptionalClientGetPlanLocationJdbcTypeDef
):
    """
    - *(dict) --*

      An argument or property of a node.
      - **Name** *(string) --***[REQUIRED]**

        The name of the argument or property.
    """


_ClientGetPlanLocationS3TypeDef = TypedDict(
    "_ClientGetPlanLocationS3TypeDef", {"Name": str, "Value": str, "Param": bool}, total=False
)


class ClientGetPlanLocationS3TypeDef(_ClientGetPlanLocationS3TypeDef):
    pass


_ClientGetPlanLocationTypeDef = TypedDict(
    "_ClientGetPlanLocationTypeDef",
    {
        "Jdbc": List[ClientGetPlanLocationJdbcTypeDef],
        "S3": List[ClientGetPlanLocationS3TypeDef],
        "DynamoDB": List[ClientGetPlanLocationDynamoDBTypeDef],
    },
    total=False,
)


class ClientGetPlanLocationTypeDef(_ClientGetPlanLocationTypeDef):
    """
    The parameters for the mapping.
    - **Jdbc** *(list) --*

      A JDBC location.
      - *(dict) --*

        An argument or property of a node.
        - **Name** *(string) --***[REQUIRED]**

          The name of the argument or property.
    """


_ClientGetPlanMappingTypeDef = TypedDict(
    "_ClientGetPlanMappingTypeDef",
    {
        "SourceTable": str,
        "SourcePath": str,
        "SourceType": str,
        "TargetTable": str,
        "TargetPath": str,
        "TargetType": str,
    },
    total=False,
)


class ClientGetPlanMappingTypeDef(_ClientGetPlanMappingTypeDef):
    """
    - *(dict) --*

      Defines a mapping.
      - **SourceTable** *(string) --*

        The name of the source table.
    """


_ClientGetPlanResponseTypeDef = TypedDict(
    "_ClientGetPlanResponseTypeDef", {"PythonScript": str, "ScalaCode": str}, total=False
)


class ClientGetPlanResponseTypeDef(_ClientGetPlanResponseTypeDef):
    """
    - *(dict) --*

      - **PythonScript** *(string) --*

        A Python script to perform the mapping.
    """


_RequiredClientGetPlanSinksTypeDef = TypedDict(
    "_RequiredClientGetPlanSinksTypeDef", {"DatabaseName": str}
)
_OptionalClientGetPlanSinksTypeDef = TypedDict(
    "_OptionalClientGetPlanSinksTypeDef", {"TableName": str}, total=False
)


class ClientGetPlanSinksTypeDef(
    _RequiredClientGetPlanSinksTypeDef, _OptionalClientGetPlanSinksTypeDef
):
    """
    - *(dict) --*

      Specifies a table definition in the AWS Glue Data Catalog.
      - **DatabaseName** *(string) --***[REQUIRED]**

        The database in which the table metadata resides.
    """


_RequiredClientGetPlanSourceTypeDef = TypedDict(
    "_RequiredClientGetPlanSourceTypeDef", {"DatabaseName": str}
)
_OptionalClientGetPlanSourceTypeDef = TypedDict(
    "_OptionalClientGetPlanSourceTypeDef", {"TableName": str}, total=False
)


class ClientGetPlanSourceTypeDef(
    _RequiredClientGetPlanSourceTypeDef, _OptionalClientGetPlanSourceTypeDef
):
    """
    The source table.
    - **DatabaseName** *(string) --***[REQUIRED]**

      The database in which the table metadata resides.
    """


_ClientGetResourcePolicyResponseTypeDef = TypedDict(
    "_ClientGetResourcePolicyResponseTypeDef",
    {"PolicyInJson": str, "PolicyHash": str, "CreateTime": datetime, "UpdateTime": datetime},
    total=False,
)


class ClientGetResourcePolicyResponseTypeDef(_ClientGetResourcePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **PolicyInJson** *(string) --*

        Contains the requested policy document, in JSON format.
    """


_ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef = TypedDict(
    "_ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef",
    {"CloudWatchEncryptionMode": Literal["DISABLED", "SSE-KMS"], "KmsKeyArn": str},
    total=False,
)


class ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef(
    _ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef
):
    pass


_ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef = TypedDict(
    "_ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef",
    {"JobBookmarksEncryptionMode": Literal["DISABLED", "CSE-KMS"], "KmsKeyArn": str},
    total=False,
)


class ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef(
    _ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef
):
    pass


_ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef = TypedDict(
    "_ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef",
    {"S3EncryptionMode": Literal["DISABLED", "SSE-KMS", "SSE-S3"], "KmsKeyArn": str},
    total=False,
)


class ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef(
    _ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef
):
    pass


_ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationTypeDef",
    {
        "S3Encryption": List[
            ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef
        ],
        "CloudWatchEncryption": ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef,
        "JobBookmarksEncryption": ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef,
    },
    total=False,
)


class ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationTypeDef(
    _ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationTypeDef
):
    pass


_ClientGetSecurityConfigurationResponseSecurityConfigurationTypeDef = TypedDict(
    "_ClientGetSecurityConfigurationResponseSecurityConfigurationTypeDef",
    {
        "Name": str,
        "CreatedTimeStamp": datetime,
        "EncryptionConfiguration": ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientGetSecurityConfigurationResponseSecurityConfigurationTypeDef(
    _ClientGetSecurityConfigurationResponseSecurityConfigurationTypeDef
):
    """
    - **SecurityConfiguration** *(dict) --*

      The requested security configuration.
      - **Name** *(string) --*

        The name of the security configuration.
    """


_ClientGetSecurityConfigurationResponseTypeDef = TypedDict(
    "_ClientGetSecurityConfigurationResponseTypeDef",
    {"SecurityConfiguration": ClientGetSecurityConfigurationResponseSecurityConfigurationTypeDef},
    total=False,
)


class ClientGetSecurityConfigurationResponseTypeDef(_ClientGetSecurityConfigurationResponseTypeDef):
    """
    - *(dict) --*

      - **SecurityConfiguration** *(dict) --*

        The requested security configuration.
        - **Name** *(string) --*

          The name of the security configuration.
    """


_ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef = TypedDict(
    "_ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef",
    {"CloudWatchEncryptionMode": Literal["DISABLED", "SSE-KMS"], "KmsKeyArn": str},
    total=False,
)


class ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef(
    _ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef
):
    pass


_ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef = TypedDict(
    "_ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef",
    {"JobBookmarksEncryptionMode": Literal["DISABLED", "CSE-KMS"], "KmsKeyArn": str},
    total=False,
)


class ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef(
    _ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef
):
    pass


_ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef = TypedDict(
    "_ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef",
    {"S3EncryptionMode": Literal["DISABLED", "SSE-KMS", "SSE-S3"], "KmsKeyArn": str},
    total=False,
)


class ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef(
    _ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef
):
    pass


_ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationTypeDef = TypedDict(
    "_ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationTypeDef",
    {
        "S3Encryption": List[
            ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef
        ],
        "CloudWatchEncryption": ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef,
        "JobBookmarksEncryption": ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef,
    },
    total=False,
)


class ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationTypeDef(
    _ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationTypeDef
):
    pass


_ClientGetSecurityConfigurationsResponseSecurityConfigurationsTypeDef = TypedDict(
    "_ClientGetSecurityConfigurationsResponseSecurityConfigurationsTypeDef",
    {
        "Name": str,
        "CreatedTimeStamp": datetime,
        "EncryptionConfiguration": ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientGetSecurityConfigurationsResponseSecurityConfigurationsTypeDef(
    _ClientGetSecurityConfigurationsResponseSecurityConfigurationsTypeDef
):
    """
    - *(dict) --*

      Specifies a security configuration.
      - **Name** *(string) --*

        The name of the security configuration.
    """


_ClientGetSecurityConfigurationsResponseTypeDef = TypedDict(
    "_ClientGetSecurityConfigurationsResponseTypeDef",
    {
        "SecurityConfigurations": List[
            ClientGetSecurityConfigurationsResponseSecurityConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetSecurityConfigurationsResponseTypeDef(
    _ClientGetSecurityConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **SecurityConfigurations** *(list) --*

        A list of security configurations.
        - *(dict) --*

          Specifies a security configuration.
          - **Name** *(string) --*

            The name of the security configuration.
    """


_ClientGetTableResponseTablePartitionKeysTypeDef = TypedDict(
    "_ClientGetTableResponseTablePartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetTableResponseTablePartitionKeysTypeDef(
    _ClientGetTableResponseTablePartitionKeysTypeDef
):
    pass


_ClientGetTableResponseTableStorageDescriptorColumnsTypeDef = TypedDict(
    "_ClientGetTableResponseTableStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetTableResponseTableStorageDescriptorColumnsTypeDef(
    _ClientGetTableResponseTableStorageDescriptorColumnsTypeDef
):
    pass


_ClientGetTableResponseTableStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_ClientGetTableResponseTableStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetTableResponseTableStorageDescriptorSerdeInfoTypeDef(
    _ClientGetTableResponseTableStorageDescriptorSerdeInfoTypeDef
):
    pass


_ClientGetTableResponseTableStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_ClientGetTableResponseTableStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class ClientGetTableResponseTableStorageDescriptorSkewedInfoTypeDef(
    _ClientGetTableResponseTableStorageDescriptorSkewedInfoTypeDef
):
    pass


_ClientGetTableResponseTableStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_ClientGetTableResponseTableStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class ClientGetTableResponseTableStorageDescriptorSortColumnsTypeDef(
    _ClientGetTableResponseTableStorageDescriptorSortColumnsTypeDef
):
    pass


_ClientGetTableResponseTableStorageDescriptorTypeDef = TypedDict(
    "_ClientGetTableResponseTableStorageDescriptorTypeDef",
    {
        "Columns": List[ClientGetTableResponseTableStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientGetTableResponseTableStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientGetTableResponseTableStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientGetTableResponseTableStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class ClientGetTableResponseTableStorageDescriptorTypeDef(
    _ClientGetTableResponseTableStorageDescriptorTypeDef
):
    pass


_ClientGetTableResponseTableTypeDef = TypedDict(
    "_ClientGetTableResponseTableTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientGetTableResponseTableStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientGetTableResponseTablePartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)


class ClientGetTableResponseTableTypeDef(_ClientGetTableResponseTableTypeDef):
    """
    - **Table** *(dict) --*

      The ``Table`` object that defines the specified table.
      - **Name** *(string) --*

        The table name. For Hive compatibility, this must be entirely lowercase.
    """


_ClientGetTableResponseTypeDef = TypedDict(
    "_ClientGetTableResponseTypeDef", {"Table": ClientGetTableResponseTableTypeDef}, total=False
)


class ClientGetTableResponseTypeDef(_ClientGetTableResponseTypeDef):
    """
    - *(dict) --*

      - **Table** *(dict) --*

        The ``Table`` object that defines the specified table.
        - **Name** *(string) --*

          The table name. For Hive compatibility, this must be entirely lowercase.
    """


_ClientGetTableVersionResponseTableVersionTablePartitionKeysTypeDef = TypedDict(
    "_ClientGetTableVersionResponseTableVersionTablePartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetTableVersionResponseTableVersionTablePartitionKeysTypeDef(
    _ClientGetTableVersionResponseTableVersionTablePartitionKeysTypeDef
):
    pass


_ClientGetTableVersionResponseTableVersionTableStorageDescriptorColumnsTypeDef = TypedDict(
    "_ClientGetTableVersionResponseTableVersionTableStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetTableVersionResponseTableVersionTableStorageDescriptorColumnsTypeDef(
    _ClientGetTableVersionResponseTableVersionTableStorageDescriptorColumnsTypeDef
):
    pass


_ClientGetTableVersionResponseTableVersionTableStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_ClientGetTableVersionResponseTableVersionTableStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetTableVersionResponseTableVersionTableStorageDescriptorSerdeInfoTypeDef(
    _ClientGetTableVersionResponseTableVersionTableStorageDescriptorSerdeInfoTypeDef
):
    pass


_ClientGetTableVersionResponseTableVersionTableStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_ClientGetTableVersionResponseTableVersionTableStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class ClientGetTableVersionResponseTableVersionTableStorageDescriptorSkewedInfoTypeDef(
    _ClientGetTableVersionResponseTableVersionTableStorageDescriptorSkewedInfoTypeDef
):
    pass


_ClientGetTableVersionResponseTableVersionTableStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_ClientGetTableVersionResponseTableVersionTableStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class ClientGetTableVersionResponseTableVersionTableStorageDescriptorSortColumnsTypeDef(
    _ClientGetTableVersionResponseTableVersionTableStorageDescriptorSortColumnsTypeDef
):
    pass


_ClientGetTableVersionResponseTableVersionTableStorageDescriptorTypeDef = TypedDict(
    "_ClientGetTableVersionResponseTableVersionTableStorageDescriptorTypeDef",
    {
        "Columns": List[
            ClientGetTableVersionResponseTableVersionTableStorageDescriptorColumnsTypeDef
        ],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientGetTableVersionResponseTableVersionTableStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            ClientGetTableVersionResponseTableVersionTableStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientGetTableVersionResponseTableVersionTableStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class ClientGetTableVersionResponseTableVersionTableStorageDescriptorTypeDef(
    _ClientGetTableVersionResponseTableVersionTableStorageDescriptorTypeDef
):
    pass


_ClientGetTableVersionResponseTableVersionTableTypeDef = TypedDict(
    "_ClientGetTableVersionResponseTableVersionTableTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientGetTableVersionResponseTableVersionTableStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientGetTableVersionResponseTableVersionTablePartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)


class ClientGetTableVersionResponseTableVersionTableTypeDef(
    _ClientGetTableVersionResponseTableVersionTableTypeDef
):
    """
    - **Table** *(dict) --*

      The table in question.
      - **Name** *(string) --*

        The table name. For Hive compatibility, this must be entirely lowercase.
    """


_ClientGetTableVersionResponseTableVersionTypeDef = TypedDict(
    "_ClientGetTableVersionResponseTableVersionTypeDef",
    {"Table": ClientGetTableVersionResponseTableVersionTableTypeDef, "VersionId": str},
    total=False,
)


class ClientGetTableVersionResponseTableVersionTypeDef(
    _ClientGetTableVersionResponseTableVersionTypeDef
):
    """
    - **TableVersion** *(dict) --*

      The requested table version.
      - **Table** *(dict) --*

        The table in question.
        - **Name** *(string) --*

          The table name. For Hive compatibility, this must be entirely lowercase.
    """


_ClientGetTableVersionResponseTypeDef = TypedDict(
    "_ClientGetTableVersionResponseTypeDef",
    {"TableVersion": ClientGetTableVersionResponseTableVersionTypeDef},
    total=False,
)


class ClientGetTableVersionResponseTypeDef(_ClientGetTableVersionResponseTypeDef):
    """
    - *(dict) --*

      - **TableVersion** *(dict) --*

        The requested table version.
        - **Table** *(dict) --*

          The table in question.
          - **Name** *(string) --*

            The table name. For Hive compatibility, this must be entirely lowercase.
    """


_ClientGetTableVersionsResponseTableVersionsTablePartitionKeysTypeDef = TypedDict(
    "_ClientGetTableVersionsResponseTableVersionsTablePartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetTableVersionsResponseTableVersionsTablePartitionKeysTypeDef(
    _ClientGetTableVersionsResponseTableVersionsTablePartitionKeysTypeDef
):
    pass


_ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorColumnsTypeDef = TypedDict(
    "_ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorColumnsTypeDef(
    _ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorColumnsTypeDef
):
    pass


_ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef(
    _ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef
):
    pass


_ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef(
    _ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef
):
    pass


_ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef(
    _ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef
):
    pass


_ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorTypeDef = TypedDict(
    "_ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorTypeDef",
    {
        "Columns": List[
            ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorColumnsTypeDef
        ],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorTypeDef(
    _ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorTypeDef
):
    pass


_ClientGetTableVersionsResponseTableVersionsTableTypeDef = TypedDict(
    "_ClientGetTableVersionsResponseTableVersionsTableTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientGetTableVersionsResponseTableVersionsTablePartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)


class ClientGetTableVersionsResponseTableVersionsTableTypeDef(
    _ClientGetTableVersionsResponseTableVersionsTableTypeDef
):
    """
    - **Table** *(dict) --*

      The table in question.
      - **Name** *(string) --*

        The table name. For Hive compatibility, this must be entirely lowercase.
    """


_ClientGetTableVersionsResponseTableVersionsTypeDef = TypedDict(
    "_ClientGetTableVersionsResponseTableVersionsTypeDef",
    {"Table": ClientGetTableVersionsResponseTableVersionsTableTypeDef, "VersionId": str},
    total=False,
)


class ClientGetTableVersionsResponseTableVersionsTypeDef(
    _ClientGetTableVersionsResponseTableVersionsTypeDef
):
    """
    - *(dict) --*

      Specifies a version of a table.
      - **Table** *(dict) --*

        The table in question.
        - **Name** *(string) --*

          The table name. For Hive compatibility, this must be entirely lowercase.
    """


_ClientGetTableVersionsResponseTypeDef = TypedDict(
    "_ClientGetTableVersionsResponseTypeDef",
    {"TableVersions": List[ClientGetTableVersionsResponseTableVersionsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetTableVersionsResponseTypeDef(_ClientGetTableVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **TableVersions** *(list) --*

        A list of strings identifying available versions of the specified table.
        - *(dict) --*

          Specifies a version of a table.
          - **Table** *(dict) --*

            The table in question.
            - **Name** *(string) --*

              The table name. For Hive compatibility, this must be entirely lowercase.
    """


_ClientGetTablesResponseTableListPartitionKeysTypeDef = TypedDict(
    "_ClientGetTablesResponseTableListPartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetTablesResponseTableListPartitionKeysTypeDef(
    _ClientGetTablesResponseTableListPartitionKeysTypeDef
):
    pass


_ClientGetTablesResponseTableListStorageDescriptorColumnsTypeDef = TypedDict(
    "_ClientGetTablesResponseTableListStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetTablesResponseTableListStorageDescriptorColumnsTypeDef(
    _ClientGetTablesResponseTableListStorageDescriptorColumnsTypeDef
):
    pass


_ClientGetTablesResponseTableListStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_ClientGetTablesResponseTableListStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetTablesResponseTableListStorageDescriptorSerdeInfoTypeDef(
    _ClientGetTablesResponseTableListStorageDescriptorSerdeInfoTypeDef
):
    pass


_ClientGetTablesResponseTableListStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_ClientGetTablesResponseTableListStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class ClientGetTablesResponseTableListStorageDescriptorSkewedInfoTypeDef(
    _ClientGetTablesResponseTableListStorageDescriptorSkewedInfoTypeDef
):
    pass


_ClientGetTablesResponseTableListStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_ClientGetTablesResponseTableListStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class ClientGetTablesResponseTableListStorageDescriptorSortColumnsTypeDef(
    _ClientGetTablesResponseTableListStorageDescriptorSortColumnsTypeDef
):
    pass


_ClientGetTablesResponseTableListStorageDescriptorTypeDef = TypedDict(
    "_ClientGetTablesResponseTableListStorageDescriptorTypeDef",
    {
        "Columns": List[ClientGetTablesResponseTableListStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientGetTablesResponseTableListStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientGetTablesResponseTableListStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientGetTablesResponseTableListStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class ClientGetTablesResponseTableListStorageDescriptorTypeDef(
    _ClientGetTablesResponseTableListStorageDescriptorTypeDef
):
    pass


_ClientGetTablesResponseTableListTypeDef = TypedDict(
    "_ClientGetTablesResponseTableListTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientGetTablesResponseTableListStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientGetTablesResponseTableListPartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)


class ClientGetTablesResponseTableListTypeDef(_ClientGetTablesResponseTableListTypeDef):
    """
    - *(dict) --*

      Represents a collection of related data organized in columns and rows.
      - **Name** *(string) --*

        The table name. For Hive compatibility, this must be entirely lowercase.
    """


_ClientGetTablesResponseTypeDef = TypedDict(
    "_ClientGetTablesResponseTypeDef",
    {"TableList": List[ClientGetTablesResponseTableListTypeDef], "NextToken": str},
    total=False,
)


class ClientGetTablesResponseTypeDef(_ClientGetTablesResponseTypeDef):
    """
    - *(dict) --*

      - **TableList** *(list) --*

        A list of the requested ``Table`` objects.
        - *(dict) --*

          Represents a collection of related data organized in columns and rows.
          - **Name** *(string) --*

            The table name. For Hive compatibility, this must be entirely lowercase.
    """


_ClientGetTagsResponseTypeDef = TypedDict(
    "_ClientGetTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientGetTagsResponseTypeDef(_ClientGetTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        The requested tags.
        - *(string) --*

          - *(string) --*
    """


_ClientGetTriggerResponseTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "_ClientGetTriggerResponseTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientGetTriggerResponseTriggerActionsNotificationPropertyTypeDef(
    _ClientGetTriggerResponseTriggerActionsNotificationPropertyTypeDef
):
    pass


_ClientGetTriggerResponseTriggerActionsTypeDef = TypedDict(
    "_ClientGetTriggerResponseTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetTriggerResponseTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)


class ClientGetTriggerResponseTriggerActionsTypeDef(_ClientGetTriggerResponseTriggerActionsTypeDef):
    pass


_ClientGetTriggerResponseTriggerPredicateConditionsTypeDef = TypedDict(
    "_ClientGetTriggerResponseTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)


class ClientGetTriggerResponseTriggerPredicateConditionsTypeDef(
    _ClientGetTriggerResponseTriggerPredicateConditionsTypeDef
):
    pass


_ClientGetTriggerResponseTriggerPredicateTypeDef = TypedDict(
    "_ClientGetTriggerResponseTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[ClientGetTriggerResponseTriggerPredicateConditionsTypeDef],
    },
    total=False,
)


class ClientGetTriggerResponseTriggerPredicateTypeDef(
    _ClientGetTriggerResponseTriggerPredicateTypeDef
):
    pass


_ClientGetTriggerResponseTriggerTypeDef = TypedDict(
    "_ClientGetTriggerResponseTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[ClientGetTriggerResponseTriggerActionsTypeDef],
        "Predicate": ClientGetTriggerResponseTriggerPredicateTypeDef,
    },
    total=False,
)


class ClientGetTriggerResponseTriggerTypeDef(_ClientGetTriggerResponseTriggerTypeDef):
    """
    - **Trigger** *(dict) --*

      The requested trigger definition.
      - **Name** *(string) --*

        The name of the trigger.
    """


_ClientGetTriggerResponseTypeDef = TypedDict(
    "_ClientGetTriggerResponseTypeDef",
    {"Trigger": ClientGetTriggerResponseTriggerTypeDef},
    total=False,
)


class ClientGetTriggerResponseTypeDef(_ClientGetTriggerResponseTypeDef):
    """
    - *(dict) --*

      - **Trigger** *(dict) --*

        The requested trigger definition.
        - **Name** *(string) --*

          The name of the trigger.
    """


_ClientGetTriggersResponseTriggersActionsNotificationPropertyTypeDef = TypedDict(
    "_ClientGetTriggersResponseTriggersActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientGetTriggersResponseTriggersActionsNotificationPropertyTypeDef(
    _ClientGetTriggersResponseTriggersActionsNotificationPropertyTypeDef
):
    pass


_ClientGetTriggersResponseTriggersActionsTypeDef = TypedDict(
    "_ClientGetTriggersResponseTriggersActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetTriggersResponseTriggersActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)


class ClientGetTriggersResponseTriggersActionsTypeDef(
    _ClientGetTriggersResponseTriggersActionsTypeDef
):
    pass


_ClientGetTriggersResponseTriggersPredicateConditionsTypeDef = TypedDict(
    "_ClientGetTriggersResponseTriggersPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)


class ClientGetTriggersResponseTriggersPredicateConditionsTypeDef(
    _ClientGetTriggersResponseTriggersPredicateConditionsTypeDef
):
    pass


_ClientGetTriggersResponseTriggersPredicateTypeDef = TypedDict(
    "_ClientGetTriggersResponseTriggersPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[ClientGetTriggersResponseTriggersPredicateConditionsTypeDef],
    },
    total=False,
)


class ClientGetTriggersResponseTriggersPredicateTypeDef(
    _ClientGetTriggersResponseTriggersPredicateTypeDef
):
    pass


_ClientGetTriggersResponseTriggersTypeDef = TypedDict(
    "_ClientGetTriggersResponseTriggersTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[ClientGetTriggersResponseTriggersActionsTypeDef],
        "Predicate": ClientGetTriggersResponseTriggersPredicateTypeDef,
    },
    total=False,
)


class ClientGetTriggersResponseTriggersTypeDef(_ClientGetTriggersResponseTriggersTypeDef):
    """
    - *(dict) --*

      Information about a specific trigger.
      - **Name** *(string) --*

        The name of the trigger.
    """


_ClientGetTriggersResponseTypeDef = TypedDict(
    "_ClientGetTriggersResponseTypeDef",
    {"Triggers": List[ClientGetTriggersResponseTriggersTypeDef], "NextToken": str},
    total=False,
)


class ClientGetTriggersResponseTypeDef(_ClientGetTriggersResponseTypeDef):
    """
    - *(dict) --*

      - **Triggers** *(list) --*

        A list of triggers for the specified job.
        - *(dict) --*

          Information about a specific trigger.
          - **Name** *(string) --*

            The name of the trigger.
    """


_ClientGetUserDefinedFunctionResponseUserDefinedFunctionResourceUrisTypeDef = TypedDict(
    "_ClientGetUserDefinedFunctionResponseUserDefinedFunctionResourceUrisTypeDef",
    {"ResourceType": Literal["JAR", "FILE", "ARCHIVE"], "Uri": str},
    total=False,
)


class ClientGetUserDefinedFunctionResponseUserDefinedFunctionResourceUrisTypeDef(
    _ClientGetUserDefinedFunctionResponseUserDefinedFunctionResourceUrisTypeDef
):
    pass


_ClientGetUserDefinedFunctionResponseUserDefinedFunctionTypeDef = TypedDict(
    "_ClientGetUserDefinedFunctionResponseUserDefinedFunctionTypeDef",
    {
        "FunctionName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": Literal["USER", "ROLE", "GROUP"],
        "CreateTime": datetime,
        "ResourceUris": List[
            ClientGetUserDefinedFunctionResponseUserDefinedFunctionResourceUrisTypeDef
        ],
    },
    total=False,
)


class ClientGetUserDefinedFunctionResponseUserDefinedFunctionTypeDef(
    _ClientGetUserDefinedFunctionResponseUserDefinedFunctionTypeDef
):
    """
    - **UserDefinedFunction** *(dict) --*

      The requested function definition.
      - **FunctionName** *(string) --*

        The name of the function.
    """


_ClientGetUserDefinedFunctionResponseTypeDef = TypedDict(
    "_ClientGetUserDefinedFunctionResponseTypeDef",
    {"UserDefinedFunction": ClientGetUserDefinedFunctionResponseUserDefinedFunctionTypeDef},
    total=False,
)


class ClientGetUserDefinedFunctionResponseTypeDef(_ClientGetUserDefinedFunctionResponseTypeDef):
    """
    - *(dict) --*

      - **UserDefinedFunction** *(dict) --*

        The requested function definition.
        - **FunctionName** *(string) --*

          The name of the function.
    """


_ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsResourceUrisTypeDef = TypedDict(
    "_ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsResourceUrisTypeDef",
    {"ResourceType": Literal["JAR", "FILE", "ARCHIVE"], "Uri": str},
    total=False,
)


class ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsResourceUrisTypeDef(
    _ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsResourceUrisTypeDef
):
    pass


_ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsTypeDef = TypedDict(
    "_ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsTypeDef",
    {
        "FunctionName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": Literal["USER", "ROLE", "GROUP"],
        "CreateTime": datetime,
        "ResourceUris": List[
            ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsResourceUrisTypeDef
        ],
    },
    total=False,
)


class ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsTypeDef(
    _ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsTypeDef
):
    """
    - *(dict) --*

      Represents the equivalent of a Hive user-defined function (``UDF`` ) definition.
      - **FunctionName** *(string) --*

        The name of the function.
    """


_ClientGetUserDefinedFunctionsResponseTypeDef = TypedDict(
    "_ClientGetUserDefinedFunctionsResponseTypeDef",
    {
        "UserDefinedFunctions": List[
            ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetUserDefinedFunctionsResponseTypeDef(_ClientGetUserDefinedFunctionsResponseTypeDef):
    """
    - *(dict) --*

      - **UserDefinedFunctions** *(list) --*

        A list of requested function definitions.
        - *(dict) --*

          Represents the equivalent of a Hive user-defined function (``UDF`` ) definition.
          - **FunctionName** *(string) --*

            The name of the function.
    """


_ClientGetWorkflowResponseWorkflowGraphEdgesTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphEdgesTypeDef",
    {"SourceId": str, "DestinationId": str},
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphEdgesTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphEdgesTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsCrawlsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsCrawlsTypeDef",
    {
        "State": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsCrawlsTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsCrawlsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsTypeDef",
    {"Crawls": List[ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsCrawlsTypeDef]},
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[
            ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
        ],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsTypeDef",
    {"JobRuns": List[ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsTypeDef]},
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[
            ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
        ],
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[
            ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsTypeDef
        ],
        "Predicate": ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateTypeDef,
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTypeDef",
    {"Trigger": ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerTypeDef},
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphNodesTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphNodesTypeDef",
    {
        "Type": Literal["CRAWLER", "JOB", "TRIGGER"],
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTypeDef,
        "JobDetails": ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsTypeDef,
        "CrawlerDetails": ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsTypeDef,
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphNodesTypeDef(
    _ClientGetWorkflowResponseWorkflowGraphNodesTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowGraphTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowGraphTypeDef",
    {
        "Nodes": List[ClientGetWorkflowResponseWorkflowGraphNodesTypeDef],
        "Edges": List[ClientGetWorkflowResponseWorkflowGraphEdgesTypeDef],
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowGraphTypeDef(_ClientGetWorkflowResponseWorkflowGraphTypeDef):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphEdgesTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphEdgesTypeDef",
    {"SourceId": str, "DestinationId": str},
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphEdgesTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphEdgesTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsCrawlsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsCrawlsTypeDef",
    {
        "State": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsCrawlsTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsCrawlsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsTypeDef",
    {"Crawls": List[ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsCrawlsTypeDef]},
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[
            ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
        ],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsTypeDef",
    {"JobRuns": List[ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsTypeDef]},
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[
            ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
        ],
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[
            ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef
        ],
        "Predicate": ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef,
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTypeDef",
    {"Trigger": ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerTypeDef},
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphNodesTypeDef",
    {
        "Type": Literal["CRAWLER", "JOB", "TRIGGER"],
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTypeDef,
        "JobDetails": ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsTypeDef,
        "CrawlerDetails": ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsTypeDef,
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphNodesTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphNodesTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunGraphTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunGraphTypeDef",
    {
        "Nodes": List[ClientGetWorkflowResponseWorkflowLastRunGraphNodesTypeDef],
        "Edges": List[ClientGetWorkflowResponseWorkflowLastRunGraphEdgesTypeDef],
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunGraphTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunGraphTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunStatisticsTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunStatisticsTypeDef",
    {
        "TotalActions": int,
        "TimeoutActions": int,
        "FailedActions": int,
        "StoppedActions": int,
        "SucceededActions": int,
        "RunningActions": int,
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunStatisticsTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunStatisticsTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowLastRunTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowLastRunTypeDef",
    {
        "Name": str,
        "WorkflowRunId": str,
        "WorkflowRunProperties": Dict[str, str],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "Status": Literal["RUNNING", "COMPLETED"],
        "Statistics": ClientGetWorkflowResponseWorkflowLastRunStatisticsTypeDef,
        "Graph": ClientGetWorkflowResponseWorkflowLastRunGraphTypeDef,
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowLastRunTypeDef(
    _ClientGetWorkflowResponseWorkflowLastRunTypeDef
):
    pass


_ClientGetWorkflowResponseWorkflowTypeDef = TypedDict(
    "_ClientGetWorkflowResponseWorkflowTypeDef",
    {
        "Name": str,
        "Description": str,
        "DefaultRunProperties": Dict[str, str],
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "LastRun": ClientGetWorkflowResponseWorkflowLastRunTypeDef,
        "Graph": ClientGetWorkflowResponseWorkflowGraphTypeDef,
    },
    total=False,
)


class ClientGetWorkflowResponseWorkflowTypeDef(_ClientGetWorkflowResponseWorkflowTypeDef):
    """
    - **Workflow** *(dict) --*

      The resource metadata for the workflow.
      - **Name** *(string) --*

        The name of the workflow representing the flow.
    """


_ClientGetWorkflowResponseTypeDef = TypedDict(
    "_ClientGetWorkflowResponseTypeDef",
    {"Workflow": ClientGetWorkflowResponseWorkflowTypeDef},
    total=False,
)


class ClientGetWorkflowResponseTypeDef(_ClientGetWorkflowResponseTypeDef):
    """
    - *(dict) --*

      - **Workflow** *(dict) --*

        The resource metadata for the workflow.
        - **Name** *(string) --*

          The name of the workflow representing the flow.
    """


_ClientGetWorkflowRunPropertiesResponseTypeDef = TypedDict(
    "_ClientGetWorkflowRunPropertiesResponseTypeDef", {"RunProperties": Dict[str, str]}, total=False
)


class ClientGetWorkflowRunPropertiesResponseTypeDef(_ClientGetWorkflowRunPropertiesResponseTypeDef):
    """
    - *(dict) --*

      - **RunProperties** *(dict) --*

        The workflow run properties which were set during the specified run.
        - *(string) --*

          - *(string) --*
    """


_ClientGetWorkflowRunResponseRunGraphEdgesTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphEdgesTypeDef",
    {"SourceId": str, "DestinationId": str},
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphEdgesTypeDef(
    _ClientGetWorkflowRunResponseRunGraphEdgesTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsCrawlsTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsCrawlsTypeDef",
    {
        "State": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsCrawlsTypeDef(
    _ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsCrawlsTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsTypeDef",
    {"Crawls": List[ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsCrawlsTypeDef]},
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsTypeDef(
    _ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef(
    _ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef(
    _ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[
            ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
        ],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsTypeDef(
    _ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphNodesJobDetailsTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphNodesJobDetailsTypeDef",
    {"JobRuns": List[ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsTypeDef]},
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphNodesJobDetailsTypeDef(
    _ClientGetWorkflowRunResponseRunGraphNodesJobDetailsTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef(
    _ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsTypeDef(
    _ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef(
    _ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[
            ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
        ],
    },
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateTypeDef(
    _ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[
            ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsTypeDef
        ],
        "Predicate": ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateTypeDef,
    },
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerTypeDef(
    _ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTypeDef",
    {"Trigger": ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerTypeDef},
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTypeDef(
    _ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphNodesTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphNodesTypeDef",
    {
        "Type": Literal["CRAWLER", "JOB", "TRIGGER"],
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTypeDef,
        "JobDetails": ClientGetWorkflowRunResponseRunGraphNodesJobDetailsTypeDef,
        "CrawlerDetails": ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsTypeDef,
    },
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphNodesTypeDef(
    _ClientGetWorkflowRunResponseRunGraphNodesTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunGraphTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunGraphTypeDef",
    {
        "Nodes": List[ClientGetWorkflowRunResponseRunGraphNodesTypeDef],
        "Edges": List[ClientGetWorkflowRunResponseRunGraphEdgesTypeDef],
    },
    total=False,
)


class ClientGetWorkflowRunResponseRunGraphTypeDef(_ClientGetWorkflowRunResponseRunGraphTypeDef):
    pass


_ClientGetWorkflowRunResponseRunStatisticsTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunStatisticsTypeDef",
    {
        "TotalActions": int,
        "TimeoutActions": int,
        "FailedActions": int,
        "StoppedActions": int,
        "SucceededActions": int,
        "RunningActions": int,
    },
    total=False,
)


class ClientGetWorkflowRunResponseRunStatisticsTypeDef(
    _ClientGetWorkflowRunResponseRunStatisticsTypeDef
):
    pass


_ClientGetWorkflowRunResponseRunTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseRunTypeDef",
    {
        "Name": str,
        "WorkflowRunId": str,
        "WorkflowRunProperties": Dict[str, str],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "Status": Literal["RUNNING", "COMPLETED"],
        "Statistics": ClientGetWorkflowRunResponseRunStatisticsTypeDef,
        "Graph": ClientGetWorkflowRunResponseRunGraphTypeDef,
    },
    total=False,
)


class ClientGetWorkflowRunResponseRunTypeDef(_ClientGetWorkflowRunResponseRunTypeDef):
    """
    - **Run** *(dict) --*

      The requested workflow run metadata.
      - **Name** *(string) --*

        Name of the workflow which was executed.
    """


_ClientGetWorkflowRunResponseTypeDef = TypedDict(
    "_ClientGetWorkflowRunResponseTypeDef",
    {"Run": ClientGetWorkflowRunResponseRunTypeDef},
    total=False,
)


class ClientGetWorkflowRunResponseTypeDef(_ClientGetWorkflowRunResponseTypeDef):
    """
    - *(dict) --*

      - **Run** *(dict) --*

        The requested workflow run metadata.
        - **Name** *(string) --*

          Name of the workflow which was executed.
    """


_ClientGetWorkflowRunsResponseRunsGraphEdgesTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphEdgesTypeDef",
    {"SourceId": str, "DestinationId": str},
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphEdgesTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphEdgesTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsCrawlsTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsCrawlsTypeDef",
    {
        "State": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsCrawlsTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsCrawlsTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsTypeDef",
    {"Crawls": List[ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsCrawlsTypeDef]},
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[
            ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
        ],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsTypeDef",
    {"JobRuns": List[ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsTypeDef]},
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[
            ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
        ],
    },
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[
            ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsTypeDef
        ],
        "Predicate": ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateTypeDef,
    },
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTypeDef",
    {"Trigger": ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerTypeDef},
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphNodesTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphNodesTypeDef",
    {
        "Type": Literal["CRAWLER", "JOB", "TRIGGER"],
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTypeDef,
        "JobDetails": ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsTypeDef,
        "CrawlerDetails": ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsTypeDef,
    },
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphNodesTypeDef(
    _ClientGetWorkflowRunsResponseRunsGraphNodesTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsGraphTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsGraphTypeDef",
    {
        "Nodes": List[ClientGetWorkflowRunsResponseRunsGraphNodesTypeDef],
        "Edges": List[ClientGetWorkflowRunsResponseRunsGraphEdgesTypeDef],
    },
    total=False,
)


class ClientGetWorkflowRunsResponseRunsGraphTypeDef(_ClientGetWorkflowRunsResponseRunsGraphTypeDef):
    pass


_ClientGetWorkflowRunsResponseRunsStatisticsTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsStatisticsTypeDef",
    {
        "TotalActions": int,
        "TimeoutActions": int,
        "FailedActions": int,
        "StoppedActions": int,
        "SucceededActions": int,
        "RunningActions": int,
    },
    total=False,
)


class ClientGetWorkflowRunsResponseRunsStatisticsTypeDef(
    _ClientGetWorkflowRunsResponseRunsStatisticsTypeDef
):
    pass


_ClientGetWorkflowRunsResponseRunsTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseRunsTypeDef",
    {
        "Name": str,
        "WorkflowRunId": str,
        "WorkflowRunProperties": Dict[str, str],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "Status": Literal["RUNNING", "COMPLETED"],
        "Statistics": ClientGetWorkflowRunsResponseRunsStatisticsTypeDef,
        "Graph": ClientGetWorkflowRunsResponseRunsGraphTypeDef,
    },
    total=False,
)


class ClientGetWorkflowRunsResponseRunsTypeDef(_ClientGetWorkflowRunsResponseRunsTypeDef):
    """
    - *(dict) --*

      A workflow run is an execution of a workflow providing all the runtime information.
      - **Name** *(string) --*

        Name of the workflow which was executed.
    """


_ClientGetWorkflowRunsResponseTypeDef = TypedDict(
    "_ClientGetWorkflowRunsResponseTypeDef",
    {"Runs": List[ClientGetWorkflowRunsResponseRunsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetWorkflowRunsResponseTypeDef(_ClientGetWorkflowRunsResponseTypeDef):
    """
    - *(dict) --*

      - **Runs** *(list) --*

        A list of workflow run metadata objects.
        - *(dict) --*

          A workflow run is an execution of a workflow providing all the runtime information.
          - **Name** *(string) --*

            Name of the workflow which was executed.
    """


_ClientListCrawlersResponseTypeDef = TypedDict(
    "_ClientListCrawlersResponseTypeDef", {"CrawlerNames": List[str], "NextToken": str}, total=False
)


class ClientListCrawlersResponseTypeDef(_ClientListCrawlersResponseTypeDef):
    """
    - *(dict) --*

      - **CrawlerNames** *(list) --*

        The names of all crawlers in the account, or the crawlers with the specified tags.
        - *(string) --*
    """


_ClientListDevEndpointsResponseTypeDef = TypedDict(
    "_ClientListDevEndpointsResponseTypeDef",
    {"DevEndpointNames": List[str], "NextToken": str},
    total=False,
)


class ClientListDevEndpointsResponseTypeDef(_ClientListDevEndpointsResponseTypeDef):
    """
    - *(dict) --*

      - **DevEndpointNames** *(list) --*

        The names of all the ``DevEndpoint`` s in the account, or the ``DevEndpoint`` s with the
        specified tags.
        - *(string) --*
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef", {"JobNames": List[str], "NextToken": str}, total=False
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    - *(dict) --*

      - **JobNames** *(list) --*

        The names of all jobs in the account, or the jobs with the specified tags.
        - *(string) --*
    """


_ClientListTriggersResponseTypeDef = TypedDict(
    "_ClientListTriggersResponseTypeDef", {"TriggerNames": List[str], "NextToken": str}, total=False
)


class ClientListTriggersResponseTypeDef(_ClientListTriggersResponseTypeDef):
    """
    - *(dict) --*

      - **TriggerNames** *(list) --*

        The names of all triggers in the account, or the triggers with the specified tags.
        - *(string) --*
    """


_ClientListWorkflowsResponseTypeDef = TypedDict(
    "_ClientListWorkflowsResponseTypeDef", {"Workflows": List[str], "NextToken": str}, total=False
)


class ClientListWorkflowsResponseTypeDef(_ClientListWorkflowsResponseTypeDef):
    """
    - *(dict) --*

      - **Workflows** *(list) --*

        List of names of workflows in the account.
        - *(string) --*
    """


_ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef = TypedDict(
    "_ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef",
    {"ReturnConnectionPasswordEncrypted": bool, "AwsKmsKeyId": str},
    total=False,
)


class ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef(
    _ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef
):
    pass


_RequiredClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef = TypedDict(
    "_RequiredClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef",
    {"CatalogEncryptionMode": Literal["DISABLED", "SSE-KMS"]},
)
_OptionalClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef = TypedDict(
    "_OptionalClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef",
    {"SseAwsKmsKeyId": str},
    total=False,
)


class ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef(
    _RequiredClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef,
    _OptionalClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef,
):
    """
    - **EncryptionAtRest** *(dict) --*

      Specifies the encryption-at-rest configuration for the Data Catalog.
      - **CatalogEncryptionMode** *(string) --***[REQUIRED]**

        The encryption-at-rest mode for encrypting Data Catalog data.
    """


_ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsTypeDef = TypedDict(
    "_ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsTypeDef",
    {
        "EncryptionAtRest": ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef,
        "ConnectionPasswordEncryption": ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef,
    },
    total=False,
)


class ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsTypeDef(
    _ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsTypeDef
):
    """
    The security configuration to set.
    - **EncryptionAtRest** *(dict) --*

      Specifies the encryption-at-rest configuration for the Data Catalog.
      - **CatalogEncryptionMode** *(string) --***[REQUIRED]**

        The encryption-at-rest mode for encrypting Data Catalog data.
    """


_ClientPutResourcePolicyResponseTypeDef = TypedDict(
    "_ClientPutResourcePolicyResponseTypeDef", {"PolicyHash": str}, total=False
)


class ClientPutResourcePolicyResponseTypeDef(_ClientPutResourcePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **PolicyHash** *(string) --*

        A hash of the policy that has just been set. This must be included in a subsequent call that
        overwrites or updates this policy.
    """


_ClientResetJobBookmarkResponseJobBookmarkEntryTypeDef = TypedDict(
    "_ClientResetJobBookmarkResponseJobBookmarkEntryTypeDef",
    {
        "JobName": str,
        "Version": int,
        "Run": int,
        "Attempt": int,
        "PreviousRunId": str,
        "RunId": str,
        "JobBookmark": str,
    },
    total=False,
)


class ClientResetJobBookmarkResponseJobBookmarkEntryTypeDef(
    _ClientResetJobBookmarkResponseJobBookmarkEntryTypeDef
):
    """
    - **JobBookmarkEntry** *(dict) --*

      The reset bookmark entry.
      - **JobName** *(string) --*

        The name of the job in question.
    """


_ClientResetJobBookmarkResponseTypeDef = TypedDict(
    "_ClientResetJobBookmarkResponseTypeDef",
    {"JobBookmarkEntry": ClientResetJobBookmarkResponseJobBookmarkEntryTypeDef},
    total=False,
)


class ClientResetJobBookmarkResponseTypeDef(_ClientResetJobBookmarkResponseTypeDef):
    """
    - *(dict) --*

      - **JobBookmarkEntry** *(dict) --*

        The reset bookmark entry.
        - **JobName** *(string) --*

          The name of the job in question.
    """


_ClientSearchTablesFiltersTypeDef = TypedDict(
    "_ClientSearchTablesFiltersTypeDef",
    {
        "Key": str,
        "Value": str,
        "Comparator": Literal[
            "EQUALS", "GREATER_THAN", "LESS_THAN", "GREATER_THAN_EQUALS", "LESS_THAN_EQUALS"
        ],
    },
    total=False,
)


class ClientSearchTablesFiltersTypeDef(_ClientSearchTablesFiltersTypeDef):
    """
    - *(dict) --*

      Defines a property predicate.
      - **Key** *(string) --*

        The key of the property.
    """


_ClientSearchTablesResponseTableListPartitionKeysTypeDef = TypedDict(
    "_ClientSearchTablesResponseTableListPartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientSearchTablesResponseTableListPartitionKeysTypeDef(
    _ClientSearchTablesResponseTableListPartitionKeysTypeDef
):
    pass


_ClientSearchTablesResponseTableListStorageDescriptorColumnsTypeDef = TypedDict(
    "_ClientSearchTablesResponseTableListStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientSearchTablesResponseTableListStorageDescriptorColumnsTypeDef(
    _ClientSearchTablesResponseTableListStorageDescriptorColumnsTypeDef
):
    pass


_ClientSearchTablesResponseTableListStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_ClientSearchTablesResponseTableListStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientSearchTablesResponseTableListStorageDescriptorSerdeInfoTypeDef(
    _ClientSearchTablesResponseTableListStorageDescriptorSerdeInfoTypeDef
):
    pass


_ClientSearchTablesResponseTableListStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_ClientSearchTablesResponseTableListStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class ClientSearchTablesResponseTableListStorageDescriptorSkewedInfoTypeDef(
    _ClientSearchTablesResponseTableListStorageDescriptorSkewedInfoTypeDef
):
    pass


_ClientSearchTablesResponseTableListStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_ClientSearchTablesResponseTableListStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class ClientSearchTablesResponseTableListStorageDescriptorSortColumnsTypeDef(
    _ClientSearchTablesResponseTableListStorageDescriptorSortColumnsTypeDef
):
    pass


_ClientSearchTablesResponseTableListStorageDescriptorTypeDef = TypedDict(
    "_ClientSearchTablesResponseTableListStorageDescriptorTypeDef",
    {
        "Columns": List[ClientSearchTablesResponseTableListStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientSearchTablesResponseTableListStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientSearchTablesResponseTableListStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientSearchTablesResponseTableListStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class ClientSearchTablesResponseTableListStorageDescriptorTypeDef(
    _ClientSearchTablesResponseTableListStorageDescriptorTypeDef
):
    pass


_ClientSearchTablesResponseTableListTypeDef = TypedDict(
    "_ClientSearchTablesResponseTableListTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientSearchTablesResponseTableListStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientSearchTablesResponseTableListPartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)


class ClientSearchTablesResponseTableListTypeDef(_ClientSearchTablesResponseTableListTypeDef):
    pass


_ClientSearchTablesResponseTypeDef = TypedDict(
    "_ClientSearchTablesResponseTypeDef",
    {"NextToken": str, "TableList": List[ClientSearchTablesResponseTableListTypeDef]},
    total=False,
)


class ClientSearchTablesResponseTypeDef(_ClientSearchTablesResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        A continuation token, present if the current list segment is not the last.
    """


_ClientSearchTablesSortCriteriaTypeDef = TypedDict(
    "_ClientSearchTablesSortCriteriaTypeDef",
    {"FieldName": str, "Sort": Literal["ASC", "DESC"]},
    total=False,
)


class ClientSearchTablesSortCriteriaTypeDef(_ClientSearchTablesSortCriteriaTypeDef):
    """
    - *(dict) --*

      Specifies a field to sort by and a sort order.
      - **FieldName** *(string) --*

        The name of the field on which to sort.
    """


_ClientStartExportLabelsTaskRunResponseTypeDef = TypedDict(
    "_ClientStartExportLabelsTaskRunResponseTypeDef", {"TaskRunId": str}, total=False
)


class ClientStartExportLabelsTaskRunResponseTypeDef(_ClientStartExportLabelsTaskRunResponseTypeDef):
    """
    - *(dict) --*

      - **TaskRunId** *(string) --*

        The unique identifier for the task run.
    """


_ClientStartImportLabelsTaskRunResponseTypeDef = TypedDict(
    "_ClientStartImportLabelsTaskRunResponseTypeDef", {"TaskRunId": str}, total=False
)


class ClientStartImportLabelsTaskRunResponseTypeDef(_ClientStartImportLabelsTaskRunResponseTypeDef):
    """
    - *(dict) --*

      - **TaskRunId** *(string) --*

        The unique identifier for the task run.
    """


_ClientStartJobRunNotificationPropertyTypeDef = TypedDict(
    "_ClientStartJobRunNotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)


class ClientStartJobRunNotificationPropertyTypeDef(_ClientStartJobRunNotificationPropertyTypeDef):
    """
    Specifies configuration properties of a job run notification.
    - **NotifyDelayAfter** *(integer) --*

      After a job run starts, the number of minutes to wait before sending a job run delay
      notification.
    """


_ClientStartJobRunResponseTypeDef = TypedDict(
    "_ClientStartJobRunResponseTypeDef", {"JobRunId": str}, total=False
)


class ClientStartJobRunResponseTypeDef(_ClientStartJobRunResponseTypeDef):
    """
    - *(dict) --*

      - **JobRunId** *(string) --*

        The ID assigned to this job run.
    """


_ClientStartMlEvaluationTaskRunResponseTypeDef = TypedDict(
    "_ClientStartMlEvaluationTaskRunResponseTypeDef", {"TaskRunId": str}, total=False
)


class ClientStartMlEvaluationTaskRunResponseTypeDef(_ClientStartMlEvaluationTaskRunResponseTypeDef):
    """
    - *(dict) --*

      - **TaskRunId** *(string) --*

        The unique identifier associated with this run.
    """


_ClientStartMlLabelingSetGenerationTaskRunResponseTypeDef = TypedDict(
    "_ClientStartMlLabelingSetGenerationTaskRunResponseTypeDef", {"TaskRunId": str}, total=False
)


class ClientStartMlLabelingSetGenerationTaskRunResponseTypeDef(
    _ClientStartMlLabelingSetGenerationTaskRunResponseTypeDef
):
    """
    - *(dict) --*

      - **TaskRunId** *(string) --*

        The unique run identifier that is associated with this task run.
    """


_ClientStartTriggerResponseTypeDef = TypedDict(
    "_ClientStartTriggerResponseTypeDef", {"Name": str}, total=False
)


class ClientStartTriggerResponseTypeDef(_ClientStartTriggerResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the trigger that was started.
    """


_ClientStartWorkflowRunResponseTypeDef = TypedDict(
    "_ClientStartWorkflowRunResponseTypeDef", {"RunId": str}, total=False
)


class ClientStartWorkflowRunResponseTypeDef(_ClientStartWorkflowRunResponseTypeDef):
    """
    - *(dict) --*

      - **RunId** *(string) --*

        An Id for the new run.
    """


_ClientStopTriggerResponseTypeDef = TypedDict(
    "_ClientStopTriggerResponseTypeDef", {"Name": str}, total=False
)


class ClientStopTriggerResponseTypeDef(_ClientStopTriggerResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the trigger that was stopped.
    """


_RequiredClientUpdateClassifierCsvClassifierTypeDef = TypedDict(
    "_RequiredClientUpdateClassifierCsvClassifierTypeDef", {"Name": str}
)
_OptionalClientUpdateClassifierCsvClassifierTypeDef = TypedDict(
    "_OptionalClientUpdateClassifierCsvClassifierTypeDef",
    {
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": Literal["UNKNOWN", "PRESENT", "ABSENT"],
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)


class ClientUpdateClassifierCsvClassifierTypeDef(
    _RequiredClientUpdateClassifierCsvClassifierTypeDef,
    _OptionalClientUpdateClassifierCsvClassifierTypeDef,
):
    """
    A ``CsvClassifier`` object with updated fields.
    - **Name** *(string) --***[REQUIRED]**

      The name of the classifier.
    """


_RequiredClientUpdateClassifierGrokClassifierTypeDef = TypedDict(
    "_RequiredClientUpdateClassifierGrokClassifierTypeDef", {"Name": str}
)
_OptionalClientUpdateClassifierGrokClassifierTypeDef = TypedDict(
    "_OptionalClientUpdateClassifierGrokClassifierTypeDef",
    {"Classification": str, "GrokPattern": str, "CustomPatterns": str},
    total=False,
)


class ClientUpdateClassifierGrokClassifierTypeDef(
    _RequiredClientUpdateClassifierGrokClassifierTypeDef,
    _OptionalClientUpdateClassifierGrokClassifierTypeDef,
):
    """
    A ``GrokClassifier`` object with updated fields.
    - **Name** *(string) --***[REQUIRED]**

      The name of the ``GrokClassifier`` .
    """


_RequiredClientUpdateClassifierJsonClassifierTypeDef = TypedDict(
    "_RequiredClientUpdateClassifierJsonClassifierTypeDef", {"Name": str}
)
_OptionalClientUpdateClassifierJsonClassifierTypeDef = TypedDict(
    "_OptionalClientUpdateClassifierJsonClassifierTypeDef", {"JsonPath": str}, total=False
)


class ClientUpdateClassifierJsonClassifierTypeDef(
    _RequiredClientUpdateClassifierJsonClassifierTypeDef,
    _OptionalClientUpdateClassifierJsonClassifierTypeDef,
):
    """
    A ``JsonClassifier`` object with updated fields.
    - **Name** *(string) --***[REQUIRED]**

      The name of the classifier.
    """


_RequiredClientUpdateClassifierXMLClassifierTypeDef = TypedDict(
    "_RequiredClientUpdateClassifierXMLClassifierTypeDef", {"Name": str}
)
_OptionalClientUpdateClassifierXMLClassifierTypeDef = TypedDict(
    "_OptionalClientUpdateClassifierXMLClassifierTypeDef",
    {"Classification": str, "RowTag": str},
    total=False,
)


class ClientUpdateClassifierXMLClassifierTypeDef(
    _RequiredClientUpdateClassifierXMLClassifierTypeDef,
    _OptionalClientUpdateClassifierXMLClassifierTypeDef,
):
    """
    An ``XMLClassifier`` object with updated fields.
    - **Name** *(string) --***[REQUIRED]**

      The name of the classifier.
    """


_ClientUpdateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef = TypedDict(
    "_ClientUpdateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef",
    {"SubnetId": str, "SecurityGroupIdList": List[str], "AvailabilityZone": str},
    total=False,
)


class ClientUpdateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef(
    _ClientUpdateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef
):
    pass


_RequiredClientUpdateConnectionConnectionInputTypeDef = TypedDict(
    "_RequiredClientUpdateConnectionConnectionInputTypeDef", {"Name": str}
)
_OptionalClientUpdateConnectionConnectionInputTypeDef = TypedDict(
    "_OptionalClientUpdateConnectionConnectionInputTypeDef",
    {
        "Description": str,
        "ConnectionType": Literal["JDBC", "SFTP"],
        "MatchCriteria": List[str],
        "ConnectionProperties": Dict[str, str],
        "PhysicalConnectionRequirements": ClientUpdateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef,
    },
    total=False,
)


class ClientUpdateConnectionConnectionInputTypeDef(
    _RequiredClientUpdateConnectionConnectionInputTypeDef,
    _OptionalClientUpdateConnectionConnectionInputTypeDef,
):
    """
    A ``ConnectionInput`` object that redefines the connection in question.
    - **Name** *(string) --***[REQUIRED]**

      The name of the connection.
    """


_ClientUpdateCrawlerSchemaChangePolicyTypeDef = TypedDict(
    "_ClientUpdateCrawlerSchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": Literal["LOG", "UPDATE_IN_DATABASE"],
        "DeleteBehavior": Literal["LOG", "DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE"],
    },
    total=False,
)


class ClientUpdateCrawlerSchemaChangePolicyTypeDef(_ClientUpdateCrawlerSchemaChangePolicyTypeDef):
    """
    The policy for the crawler's update and deletion behavior.
    - **UpdateBehavior** *(string) --*

      The update behavior when the crawler finds a changed schema.
    """


_ClientUpdateCrawlerTargetsCatalogTargetsTypeDef = TypedDict(
    "_ClientUpdateCrawlerTargetsCatalogTargetsTypeDef",
    {"DatabaseName": str, "Tables": List[str]},
    total=False,
)


class ClientUpdateCrawlerTargetsCatalogTargetsTypeDef(
    _ClientUpdateCrawlerTargetsCatalogTargetsTypeDef
):
    pass


_ClientUpdateCrawlerTargetsDynamoDBTargetsTypeDef = TypedDict(
    "_ClientUpdateCrawlerTargetsDynamoDBTargetsTypeDef", {"Path": str}, total=False
)


class ClientUpdateCrawlerTargetsDynamoDBTargetsTypeDef(
    _ClientUpdateCrawlerTargetsDynamoDBTargetsTypeDef
):
    pass


_ClientUpdateCrawlerTargetsJdbcTargetsTypeDef = TypedDict(
    "_ClientUpdateCrawlerTargetsJdbcTargetsTypeDef",
    {"ConnectionName": str, "Path": str, "Exclusions": List[str]},
    total=False,
)


class ClientUpdateCrawlerTargetsJdbcTargetsTypeDef(_ClientUpdateCrawlerTargetsJdbcTargetsTypeDef):
    pass


_ClientUpdateCrawlerTargetsS3TargetsTypeDef = TypedDict(
    "_ClientUpdateCrawlerTargetsS3TargetsTypeDef",
    {"Path": str, "Exclusions": List[str]},
    total=False,
)


class ClientUpdateCrawlerTargetsS3TargetsTypeDef(_ClientUpdateCrawlerTargetsS3TargetsTypeDef):
    """
    - *(dict) --*

      Specifies a data store in Amazon Simple Storage Service (Amazon S3).
      - **Path** *(string) --*

        The path to the Amazon S3 target.
    """


_ClientUpdateCrawlerTargetsTypeDef = TypedDict(
    "_ClientUpdateCrawlerTargetsTypeDef",
    {
        "S3Targets": List[ClientUpdateCrawlerTargetsS3TargetsTypeDef],
        "JdbcTargets": List[ClientUpdateCrawlerTargetsJdbcTargetsTypeDef],
        "DynamoDBTargets": List[ClientUpdateCrawlerTargetsDynamoDBTargetsTypeDef],
        "CatalogTargets": List[ClientUpdateCrawlerTargetsCatalogTargetsTypeDef],
    },
    total=False,
)


class ClientUpdateCrawlerTargetsTypeDef(_ClientUpdateCrawlerTargetsTypeDef):
    """
    A list of targets to crawl.
    - **S3Targets** *(list) --*

      Specifies Amazon Simple Storage Service (Amazon S3) targets.
      - *(dict) --*

        Specifies a data store in Amazon Simple Storage Service (Amazon S3).
        - **Path** *(string) --*

          The path to the Amazon S3 target.
    """


_ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "_ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef(
    _ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef
):
    pass


_ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef = TypedDict(
    "_ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef(
    _ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef
):
    pass


_RequiredClientUpdateDatabaseDatabaseInputTypeDef = TypedDict(
    "_RequiredClientUpdateDatabaseDatabaseInputTypeDef", {"Name": str}
)
_OptionalClientUpdateDatabaseDatabaseInputTypeDef = TypedDict(
    "_OptionalClientUpdateDatabaseDatabaseInputTypeDef",
    {
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTableDefaultPermissions": List[
            ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDatabaseDatabaseInputTypeDef(
    _RequiredClientUpdateDatabaseDatabaseInputTypeDef,
    _OptionalClientUpdateDatabaseDatabaseInputTypeDef,
):
    """
    A ``DatabaseInput`` object specifying the new definition of the metadata database in the
    catalog.
    - **Name** *(string) --***[REQUIRED]**

      The name of the database. For Hive compatibility, this is folded to lowercase when it is
      stored.
    """


_ClientUpdateDevEndpointCustomLibrariesTypeDef = TypedDict(
    "_ClientUpdateDevEndpointCustomLibrariesTypeDef",
    {"ExtraPythonLibsS3Path": str, "ExtraJarsS3Path": str},
    total=False,
)


class ClientUpdateDevEndpointCustomLibrariesTypeDef(_ClientUpdateDevEndpointCustomLibrariesTypeDef):
    """
    Custom Python or Java libraries to be loaded in the ``DevEndpoint`` .
    - **ExtraPythonLibsS3Path** *(string) --*

      The paths to one or more Python libraries in an Amazon Simple Storage Service (Amazon S3)
      bucket that should be loaded in your ``DevEndpoint`` . Multiple values must be complete paths
      separated by a comma.
      .. note::

        You can only use pure Python libraries with a ``DevEndpoint`` . Libraries that rely on C
        extensions, such as the `pandas <http://pandas.pydata.org/>`__ Python data analysis library,
        are not currently supported.
    """


_ClientUpdateJobJobUpdateCommandTypeDef = TypedDict(
    "_ClientUpdateJobJobUpdateCommandTypeDef",
    {"Name": str, "ScriptLocation": str, "PythonVersion": str},
    total=False,
)


class ClientUpdateJobJobUpdateCommandTypeDef(_ClientUpdateJobJobUpdateCommandTypeDef):
    pass


_ClientUpdateJobJobUpdateConnectionsTypeDef = TypedDict(
    "_ClientUpdateJobJobUpdateConnectionsTypeDef", {"Connections": List[str]}, total=False
)


class ClientUpdateJobJobUpdateConnectionsTypeDef(_ClientUpdateJobJobUpdateConnectionsTypeDef):
    pass


_ClientUpdateJobJobUpdateExecutionPropertyTypeDef = TypedDict(
    "_ClientUpdateJobJobUpdateExecutionPropertyTypeDef", {"MaxConcurrentRuns": int}, total=False
)


class ClientUpdateJobJobUpdateExecutionPropertyTypeDef(
    _ClientUpdateJobJobUpdateExecutionPropertyTypeDef
):
    pass


_ClientUpdateJobJobUpdateNotificationPropertyTypeDef = TypedDict(
    "_ClientUpdateJobJobUpdateNotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)


class ClientUpdateJobJobUpdateNotificationPropertyTypeDef(
    _ClientUpdateJobJobUpdateNotificationPropertyTypeDef
):
    pass


_ClientUpdateJobJobUpdateTypeDef = TypedDict(
    "_ClientUpdateJobJobUpdateTypeDef",
    {
        "Description": str,
        "LogUri": str,
        "Role": str,
        "ExecutionProperty": ClientUpdateJobJobUpdateExecutionPropertyTypeDef,
        "Command": ClientUpdateJobJobUpdateCommandTypeDef,
        "DefaultArguments": Dict[str, str],
        "Connections": ClientUpdateJobJobUpdateConnectionsTypeDef,
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientUpdateJobJobUpdateNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class ClientUpdateJobJobUpdateTypeDef(_ClientUpdateJobJobUpdateTypeDef):
    """
    Specifies the values with which to update the job definition.
    - **Description** *(string) --*

      Description of the job being defined.
    """


_ClientUpdateJobResponseTypeDef = TypedDict(
    "_ClientUpdateJobResponseTypeDef", {"JobName": str}, total=False
)


class ClientUpdateJobResponseTypeDef(_ClientUpdateJobResponseTypeDef):
    """
    - *(dict) --*

      - **JobName** *(string) --*

        Returns the name of the updated job definition.
    """


_ClientUpdateMlTransformParametersFindMatchesParametersTypeDef = TypedDict(
    "_ClientUpdateMlTransformParametersFindMatchesParametersTypeDef",
    {
        "PrimaryKeyColumnName": str,
        "PrecisionRecallTradeoff": float,
        "AccuracyCostTradeoff": float,
        "EnforceProvidedLabels": bool,
    },
    total=False,
)


class ClientUpdateMlTransformParametersFindMatchesParametersTypeDef(
    _ClientUpdateMlTransformParametersFindMatchesParametersTypeDef
):
    pass


_RequiredClientUpdateMlTransformParametersTypeDef = TypedDict(
    "_RequiredClientUpdateMlTransformParametersTypeDef", {"TransformType": str}
)
_OptionalClientUpdateMlTransformParametersTypeDef = TypedDict(
    "_OptionalClientUpdateMlTransformParametersTypeDef",
    {"FindMatchesParameters": ClientUpdateMlTransformParametersFindMatchesParametersTypeDef},
    total=False,
)


class ClientUpdateMlTransformParametersTypeDef(
    _RequiredClientUpdateMlTransformParametersTypeDef,
    _OptionalClientUpdateMlTransformParametersTypeDef,
):
    """
    The configuration parameters that are specific to the transform type (algorithm) used.
    Conditionally dependent on the transform type.
    - **TransformType** *(string) --***[REQUIRED]**

      The type of machine learning transform.
      For information about the types of machine learning transforms, see `Creating Machine Learning
      Transforms
      <http://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform.html>`__ .
    """


_ClientUpdateMlTransformResponseTypeDef = TypedDict(
    "_ClientUpdateMlTransformResponseTypeDef", {"TransformId": str}, total=False
)


class ClientUpdateMlTransformResponseTypeDef(_ClientUpdateMlTransformResponseTypeDef):
    """
    - *(dict) --*

      - **TransformId** *(string) --*

        The unique identifier for the transform that was updated.
    """


_ClientUpdatePartitionPartitionInputStorageDescriptorColumnsTypeDef = TypedDict(
    "_ClientUpdatePartitionPartitionInputStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientUpdatePartitionPartitionInputStorageDescriptorColumnsTypeDef(
    _ClientUpdatePartitionPartitionInputStorageDescriptorColumnsTypeDef
):
    pass


_ClientUpdatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_ClientUpdatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientUpdatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef(
    _ClientUpdatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef
):
    pass


_ClientUpdatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_ClientUpdatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class ClientUpdatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef(
    _ClientUpdatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef
):
    pass


_ClientUpdatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_ClientUpdatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class ClientUpdatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef(
    _ClientUpdatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef
):
    pass


_ClientUpdatePartitionPartitionInputStorageDescriptorTypeDef = TypedDict(
    "_ClientUpdatePartitionPartitionInputStorageDescriptorTypeDef",
    {
        "Columns": List[ClientUpdatePartitionPartitionInputStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientUpdatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientUpdatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientUpdatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class ClientUpdatePartitionPartitionInputStorageDescriptorTypeDef(
    _ClientUpdatePartitionPartitionInputStorageDescriptorTypeDef
):
    pass


_ClientUpdatePartitionPartitionInputTypeDef = TypedDict(
    "_ClientUpdatePartitionPartitionInputTypeDef",
    {
        "Values": List[str],
        "LastAccessTime": datetime,
        "StorageDescriptor": ClientUpdatePartitionPartitionInputStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)


class ClientUpdatePartitionPartitionInputTypeDef(_ClientUpdatePartitionPartitionInputTypeDef):
    """
    The new partition object to update the partition to.
    - **Values** *(list) --*

      The values of the partition. Although this parameter is not required by the SDK, you must
      specify this parameter for a valid input.
      The values for the keys for the new partition must be passed as an array of String objects
      that must be ordered in the same order as the partition keys appearing in the Amazon S3
      prefix. Otherwise AWS Glue will add the values to the wrong keys.
      - *(string) --*
    """


_ClientUpdateTableTableInputPartitionKeysTypeDef = TypedDict(
    "_ClientUpdateTableTableInputPartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientUpdateTableTableInputPartitionKeysTypeDef(
    _ClientUpdateTableTableInputPartitionKeysTypeDef
):
    pass


_ClientUpdateTableTableInputStorageDescriptorColumnsTypeDef = TypedDict(
    "_ClientUpdateTableTableInputStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientUpdateTableTableInputStorageDescriptorColumnsTypeDef(
    _ClientUpdateTableTableInputStorageDescriptorColumnsTypeDef
):
    pass


_ClientUpdateTableTableInputStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_ClientUpdateTableTableInputStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientUpdateTableTableInputStorageDescriptorSerdeInfoTypeDef(
    _ClientUpdateTableTableInputStorageDescriptorSerdeInfoTypeDef
):
    pass


_ClientUpdateTableTableInputStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_ClientUpdateTableTableInputStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class ClientUpdateTableTableInputStorageDescriptorSkewedInfoTypeDef(
    _ClientUpdateTableTableInputStorageDescriptorSkewedInfoTypeDef
):
    pass


_ClientUpdateTableTableInputStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_ClientUpdateTableTableInputStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class ClientUpdateTableTableInputStorageDescriptorSortColumnsTypeDef(
    _ClientUpdateTableTableInputStorageDescriptorSortColumnsTypeDef
):
    pass


_ClientUpdateTableTableInputStorageDescriptorTypeDef = TypedDict(
    "_ClientUpdateTableTableInputStorageDescriptorTypeDef",
    {
        "Columns": List[ClientUpdateTableTableInputStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientUpdateTableTableInputStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientUpdateTableTableInputStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientUpdateTableTableInputStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class ClientUpdateTableTableInputStorageDescriptorTypeDef(
    _ClientUpdateTableTableInputStorageDescriptorTypeDef
):
    pass


_RequiredClientUpdateTableTableInputTypeDef = TypedDict(
    "_RequiredClientUpdateTableTableInputTypeDef", {"Name": str}
)
_OptionalClientUpdateTableTableInputTypeDef = TypedDict(
    "_OptionalClientUpdateTableTableInputTypeDef",
    {
        "Description": str,
        "Owner": str,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientUpdateTableTableInputStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientUpdateTableTableInputPartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ClientUpdateTableTableInputTypeDef(
    _RequiredClientUpdateTableTableInputTypeDef, _OptionalClientUpdateTableTableInputTypeDef
):
    """
    An updated ``TableInput`` object to define the metadata table in the catalog.
    - **Name** *(string) --***[REQUIRED]**

      The table name. For Hive compatibility, this is folded to lowercase when it is stored.
    """


_ClientUpdateTriggerResponseTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "_ClientUpdateTriggerResponseTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientUpdateTriggerResponseTriggerActionsNotificationPropertyTypeDef(
    _ClientUpdateTriggerResponseTriggerActionsNotificationPropertyTypeDef
):
    pass


_ClientUpdateTriggerResponseTriggerActionsTypeDef = TypedDict(
    "_ClientUpdateTriggerResponseTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientUpdateTriggerResponseTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)


class ClientUpdateTriggerResponseTriggerActionsTypeDef(
    _ClientUpdateTriggerResponseTriggerActionsTypeDef
):
    pass


_ClientUpdateTriggerResponseTriggerPredicateConditionsTypeDef = TypedDict(
    "_ClientUpdateTriggerResponseTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)


class ClientUpdateTriggerResponseTriggerPredicateConditionsTypeDef(
    _ClientUpdateTriggerResponseTriggerPredicateConditionsTypeDef
):
    pass


_ClientUpdateTriggerResponseTriggerPredicateTypeDef = TypedDict(
    "_ClientUpdateTriggerResponseTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[ClientUpdateTriggerResponseTriggerPredicateConditionsTypeDef],
    },
    total=False,
)


class ClientUpdateTriggerResponseTriggerPredicateTypeDef(
    _ClientUpdateTriggerResponseTriggerPredicateTypeDef
):
    pass


_ClientUpdateTriggerResponseTriggerTypeDef = TypedDict(
    "_ClientUpdateTriggerResponseTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[ClientUpdateTriggerResponseTriggerActionsTypeDef],
        "Predicate": ClientUpdateTriggerResponseTriggerPredicateTypeDef,
    },
    total=False,
)


class ClientUpdateTriggerResponseTriggerTypeDef(_ClientUpdateTriggerResponseTriggerTypeDef):
    """
    - **Trigger** *(dict) --*

      The resulting trigger definition.
      - **Name** *(string) --*

        The name of the trigger.
    """


_ClientUpdateTriggerResponseTypeDef = TypedDict(
    "_ClientUpdateTriggerResponseTypeDef",
    {"Trigger": ClientUpdateTriggerResponseTriggerTypeDef},
    total=False,
)


class ClientUpdateTriggerResponseTypeDef(_ClientUpdateTriggerResponseTypeDef):
    """
    - *(dict) --*

      - **Trigger** *(dict) --*

        The resulting trigger definition.
        - **Name** *(string) --*

          The name of the trigger.
    """


_ClientUpdateTriggerTriggerUpdateActionsNotificationPropertyTypeDef = TypedDict(
    "_ClientUpdateTriggerTriggerUpdateActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class ClientUpdateTriggerTriggerUpdateActionsNotificationPropertyTypeDef(
    _ClientUpdateTriggerTriggerUpdateActionsNotificationPropertyTypeDef
):
    pass


_ClientUpdateTriggerTriggerUpdateActionsTypeDef = TypedDict(
    "_ClientUpdateTriggerTriggerUpdateActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientUpdateTriggerTriggerUpdateActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)


class ClientUpdateTriggerTriggerUpdateActionsTypeDef(
    _ClientUpdateTriggerTriggerUpdateActionsTypeDef
):
    pass


_ClientUpdateTriggerTriggerUpdatePredicateConditionsTypeDef = TypedDict(
    "_ClientUpdateTriggerTriggerUpdatePredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)


class ClientUpdateTriggerTriggerUpdatePredicateConditionsTypeDef(
    _ClientUpdateTriggerTriggerUpdatePredicateConditionsTypeDef
):
    pass


_ClientUpdateTriggerTriggerUpdatePredicateTypeDef = TypedDict(
    "_ClientUpdateTriggerTriggerUpdatePredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[ClientUpdateTriggerTriggerUpdatePredicateConditionsTypeDef],
    },
    total=False,
)


class ClientUpdateTriggerTriggerUpdatePredicateTypeDef(
    _ClientUpdateTriggerTriggerUpdatePredicateTypeDef
):
    pass


_ClientUpdateTriggerTriggerUpdateTypeDef = TypedDict(
    "_ClientUpdateTriggerTriggerUpdateTypeDef",
    {
        "Name": str,
        "Description": str,
        "Schedule": str,
        "Actions": List[ClientUpdateTriggerTriggerUpdateActionsTypeDef],
        "Predicate": ClientUpdateTriggerTriggerUpdatePredicateTypeDef,
    },
    total=False,
)


class ClientUpdateTriggerTriggerUpdateTypeDef(_ClientUpdateTriggerTriggerUpdateTypeDef):
    """
    The new values with which to update the trigger.
    - **Name** *(string) --*

      Reserved for future use.
    """


_ClientUpdateUserDefinedFunctionFunctionInputResourceUrisTypeDef = TypedDict(
    "_ClientUpdateUserDefinedFunctionFunctionInputResourceUrisTypeDef",
    {"ResourceType": Literal["JAR", "FILE", "ARCHIVE"], "Uri": str},
    total=False,
)


class ClientUpdateUserDefinedFunctionFunctionInputResourceUrisTypeDef(
    _ClientUpdateUserDefinedFunctionFunctionInputResourceUrisTypeDef
):
    pass


_ClientUpdateUserDefinedFunctionFunctionInputTypeDef = TypedDict(
    "_ClientUpdateUserDefinedFunctionFunctionInputTypeDef",
    {
        "FunctionName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": Literal["USER", "ROLE", "GROUP"],
        "ResourceUris": List[ClientUpdateUserDefinedFunctionFunctionInputResourceUrisTypeDef],
    },
    total=False,
)


class ClientUpdateUserDefinedFunctionFunctionInputTypeDef(
    _ClientUpdateUserDefinedFunctionFunctionInputTypeDef
):
    """
    A ``FunctionInput`` object that redefines the function in the Data Catalog.
    - **FunctionName** *(string) --*

      The name of the function.
    """


_ClientUpdateWorkflowResponseTypeDef = TypedDict(
    "_ClientUpdateWorkflowResponseTypeDef", {"Name": str}, total=False
)


class ClientUpdateWorkflowResponseTypeDef(_ClientUpdateWorkflowResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the workflow which was specified in input.
    """


_GetClassifiersPaginatePaginationConfigTypeDef = TypedDict(
    "_GetClassifiersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetClassifiersPaginatePaginationConfigTypeDef(_GetClassifiersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetClassifiersPaginateResponseClassifiersCsvClassifierTypeDef = TypedDict(
    "_GetClassifiersPaginateResponseClassifiersCsvClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": Literal["UNKNOWN", "PRESENT", "ABSENT"],
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)


class GetClassifiersPaginateResponseClassifiersCsvClassifierTypeDef(
    _GetClassifiersPaginateResponseClassifiersCsvClassifierTypeDef
):
    pass


_GetClassifiersPaginateResponseClassifiersGrokClassifierTypeDef = TypedDict(
    "_GetClassifiersPaginateResponseClassifiersGrokClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "GrokPattern": str,
        "CustomPatterns": str,
    },
    total=False,
)


class GetClassifiersPaginateResponseClassifiersGrokClassifierTypeDef(
    _GetClassifiersPaginateResponseClassifiersGrokClassifierTypeDef
):
    """
    - **GrokClassifier** *(dict) --*

      A classifier that uses ``grok`` .
      - **Name** *(string) --*

        The name of the classifier.
    """


_GetClassifiersPaginateResponseClassifiersJsonClassifierTypeDef = TypedDict(
    "_GetClassifiersPaginateResponseClassifiersJsonClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "JsonPath": str,
    },
    total=False,
)


class GetClassifiersPaginateResponseClassifiersJsonClassifierTypeDef(
    _GetClassifiersPaginateResponseClassifiersJsonClassifierTypeDef
):
    pass


_GetClassifiersPaginateResponseClassifiersXMLClassifierTypeDef = TypedDict(
    "_GetClassifiersPaginateResponseClassifiersXMLClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "RowTag": str,
    },
    total=False,
)


class GetClassifiersPaginateResponseClassifiersXMLClassifierTypeDef(
    _GetClassifiersPaginateResponseClassifiersXMLClassifierTypeDef
):
    pass


_GetClassifiersPaginateResponseClassifiersTypeDef = TypedDict(
    "_GetClassifiersPaginateResponseClassifiersTypeDef",
    {
        "GrokClassifier": GetClassifiersPaginateResponseClassifiersGrokClassifierTypeDef,
        "XMLClassifier": GetClassifiersPaginateResponseClassifiersXMLClassifierTypeDef,
        "JsonClassifier": GetClassifiersPaginateResponseClassifiersJsonClassifierTypeDef,
        "CsvClassifier": GetClassifiersPaginateResponseClassifiersCsvClassifierTypeDef,
    },
    total=False,
)


class GetClassifiersPaginateResponseClassifiersTypeDef(
    _GetClassifiersPaginateResponseClassifiersTypeDef
):
    """
    - *(dict) --*

      Classifiers are triggered during a crawl task. A classifier checks whether a given file is in
      a format it can handle. If it is, the classifier creates a schema in the form of a
      ``StructType`` object that matches that data format.
      You can use the standard classifiers that AWS Glue provides, or you can write your own
      classifiers to best categorize your data sources and specify the appropriate schemas to use
      for them. A classifier can be a ``grok`` classifier, an ``XML`` classifier, a ``JSON``
      classifier, or a custom ``CSV`` classifier, as specified in one of the fields in the
      ``Classifier`` object.
      - **GrokClassifier** *(dict) --*

        A classifier that uses ``grok`` .
        - **Name** *(string) --*

          The name of the classifier.
    """


_GetClassifiersPaginateResponseTypeDef = TypedDict(
    "_GetClassifiersPaginateResponseTypeDef",
    {"Classifiers": List[GetClassifiersPaginateResponseClassifiersTypeDef]},
    total=False,
)


class GetClassifiersPaginateResponseTypeDef(_GetClassifiersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Classifiers** *(list) --*

        The requested list of classifier objects.
        - *(dict) --*

          Classifiers are triggered during a crawl task. A classifier checks whether a given file is
          in a format it can handle. If it is, the classifier creates a schema in the form of a
          ``StructType`` object that matches that data format.
          You can use the standard classifiers that AWS Glue provides, or you can write your own
          classifiers to best categorize your data sources and specify the appropriate schemas to
          use for them. A classifier can be a ``grok`` classifier, an ``XML`` classifier, a ``JSON``
          classifier, or a custom ``CSV`` classifier, as specified in one of the fields in the
          ``Classifier`` object.
          - **GrokClassifier** *(dict) --*

            A classifier that uses ``grok`` .
            - **Name** *(string) --*

              The name of the classifier.
    """


_GetConnectionsPaginateFilterTypeDef = TypedDict(
    "_GetConnectionsPaginateFilterTypeDef",
    {"MatchCriteria": List[str], "ConnectionType": Literal["JDBC", "SFTP"]},
    total=False,
)


class GetConnectionsPaginateFilterTypeDef(_GetConnectionsPaginateFilterTypeDef):
    """
    A filter that controls which connections are returned.
    - **MatchCriteria** *(list) --*

      A criteria string that must match the criteria recorded in the connection definition for that
      connection definition to be returned.
      - *(string) --*
    """


_GetConnectionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetConnectionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetConnectionsPaginatePaginationConfigTypeDef(_GetConnectionsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetConnectionsPaginateResponseConnectionListPhysicalConnectionRequirementsTypeDef = TypedDict(
    "_GetConnectionsPaginateResponseConnectionListPhysicalConnectionRequirementsTypeDef",
    {"SubnetId": str, "SecurityGroupIdList": List[str], "AvailabilityZone": str},
    total=False,
)


class GetConnectionsPaginateResponseConnectionListPhysicalConnectionRequirementsTypeDef(
    _GetConnectionsPaginateResponseConnectionListPhysicalConnectionRequirementsTypeDef
):
    pass


_GetConnectionsPaginateResponseConnectionListTypeDef = TypedDict(
    "_GetConnectionsPaginateResponseConnectionListTypeDef",
    {
        "Name": str,
        "Description": str,
        "ConnectionType": Literal["JDBC", "SFTP"],
        "MatchCriteria": List[str],
        "ConnectionProperties": Dict[str, str],
        "PhysicalConnectionRequirements": GetConnectionsPaginateResponseConnectionListPhysicalConnectionRequirementsTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "LastUpdatedBy": str,
    },
    total=False,
)


class GetConnectionsPaginateResponseConnectionListTypeDef(
    _GetConnectionsPaginateResponseConnectionListTypeDef
):
    """
    - *(dict) --*

      Defines a connection to a data source.
      - **Name** *(string) --*

        The name of the connection definition.
    """


_GetConnectionsPaginateResponseTypeDef = TypedDict(
    "_GetConnectionsPaginateResponseTypeDef",
    {"ConnectionList": List[GetConnectionsPaginateResponseConnectionListTypeDef]},
    total=False,
)


class GetConnectionsPaginateResponseTypeDef(_GetConnectionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ConnectionList** *(list) --*

        A list of requested connection definitions.
        - *(dict) --*

          Defines a connection to a data source.
          - **Name** *(string) --*

            The name of the connection definition.
    """


_GetCrawlerMetricsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetCrawlerMetricsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetCrawlerMetricsPaginatePaginationConfigTypeDef(
    _GetCrawlerMetricsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetCrawlerMetricsPaginateResponseCrawlerMetricsListTypeDef = TypedDict(
    "_GetCrawlerMetricsPaginateResponseCrawlerMetricsListTypeDef",
    {
        "CrawlerName": str,
        "TimeLeftSeconds": float,
        "StillEstimating": bool,
        "LastRuntimeSeconds": float,
        "MedianRuntimeSeconds": float,
        "TablesCreated": int,
        "TablesUpdated": int,
        "TablesDeleted": int,
    },
    total=False,
)


class GetCrawlerMetricsPaginateResponseCrawlerMetricsListTypeDef(
    _GetCrawlerMetricsPaginateResponseCrawlerMetricsListTypeDef
):
    """
    - *(dict) --*

      Metrics for a specified crawler.
      - **CrawlerName** *(string) --*

        The name of the crawler.
    """


_GetCrawlerMetricsPaginateResponseTypeDef = TypedDict(
    "_GetCrawlerMetricsPaginateResponseTypeDef",
    {"CrawlerMetricsList": List[GetCrawlerMetricsPaginateResponseCrawlerMetricsListTypeDef]},
    total=False,
)


class GetCrawlerMetricsPaginateResponseTypeDef(_GetCrawlerMetricsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **CrawlerMetricsList** *(list) --*

        A list of metrics for the specified crawler.
        - *(dict) --*

          Metrics for a specified crawler.
          - **CrawlerName** *(string) --*

            The name of the crawler.
    """


_GetCrawlersPaginatePaginationConfigTypeDef = TypedDict(
    "_GetCrawlersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetCrawlersPaginatePaginationConfigTypeDef(_GetCrawlersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetCrawlersPaginateResponseCrawlersLastCrawlTypeDef = TypedDict(
    "_GetCrawlersPaginateResponseCrawlersLastCrawlTypeDef",
    {
        "Status": Literal["SUCCEEDED", "CANCELLED", "FAILED"],
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
        "MessagePrefix": str,
        "StartTime": datetime,
    },
    total=False,
)


class GetCrawlersPaginateResponseCrawlersLastCrawlTypeDef(
    _GetCrawlersPaginateResponseCrawlersLastCrawlTypeDef
):
    pass


_GetCrawlersPaginateResponseCrawlersScheduleTypeDef = TypedDict(
    "_GetCrawlersPaginateResponseCrawlersScheduleTypeDef",
    {"ScheduleExpression": str, "State": Literal["SCHEDULED", "NOT_SCHEDULED", "TRANSITIONING"]},
    total=False,
)


class GetCrawlersPaginateResponseCrawlersScheduleTypeDef(
    _GetCrawlersPaginateResponseCrawlersScheduleTypeDef
):
    pass


_GetCrawlersPaginateResponseCrawlersSchemaChangePolicyTypeDef = TypedDict(
    "_GetCrawlersPaginateResponseCrawlersSchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": Literal["LOG", "UPDATE_IN_DATABASE"],
        "DeleteBehavior": Literal["LOG", "DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE"],
    },
    total=False,
)


class GetCrawlersPaginateResponseCrawlersSchemaChangePolicyTypeDef(
    _GetCrawlersPaginateResponseCrawlersSchemaChangePolicyTypeDef
):
    pass


_GetCrawlersPaginateResponseCrawlersTargetsCatalogTargetsTypeDef = TypedDict(
    "_GetCrawlersPaginateResponseCrawlersTargetsCatalogTargetsTypeDef",
    {"DatabaseName": str, "Tables": List[str]},
    total=False,
)


class GetCrawlersPaginateResponseCrawlersTargetsCatalogTargetsTypeDef(
    _GetCrawlersPaginateResponseCrawlersTargetsCatalogTargetsTypeDef
):
    pass


_GetCrawlersPaginateResponseCrawlersTargetsDynamoDBTargetsTypeDef = TypedDict(
    "_GetCrawlersPaginateResponseCrawlersTargetsDynamoDBTargetsTypeDef", {"Path": str}, total=False
)


class GetCrawlersPaginateResponseCrawlersTargetsDynamoDBTargetsTypeDef(
    _GetCrawlersPaginateResponseCrawlersTargetsDynamoDBTargetsTypeDef
):
    pass


_GetCrawlersPaginateResponseCrawlersTargetsJdbcTargetsTypeDef = TypedDict(
    "_GetCrawlersPaginateResponseCrawlersTargetsJdbcTargetsTypeDef",
    {"ConnectionName": str, "Path": str, "Exclusions": List[str]},
    total=False,
)


class GetCrawlersPaginateResponseCrawlersTargetsJdbcTargetsTypeDef(
    _GetCrawlersPaginateResponseCrawlersTargetsJdbcTargetsTypeDef
):
    pass


_GetCrawlersPaginateResponseCrawlersTargetsS3TargetsTypeDef = TypedDict(
    "_GetCrawlersPaginateResponseCrawlersTargetsS3TargetsTypeDef",
    {"Path": str, "Exclusions": List[str]},
    total=False,
)


class GetCrawlersPaginateResponseCrawlersTargetsS3TargetsTypeDef(
    _GetCrawlersPaginateResponseCrawlersTargetsS3TargetsTypeDef
):
    pass


_GetCrawlersPaginateResponseCrawlersTargetsTypeDef = TypedDict(
    "_GetCrawlersPaginateResponseCrawlersTargetsTypeDef",
    {
        "S3Targets": List[GetCrawlersPaginateResponseCrawlersTargetsS3TargetsTypeDef],
        "JdbcTargets": List[GetCrawlersPaginateResponseCrawlersTargetsJdbcTargetsTypeDef],
        "DynamoDBTargets": List[GetCrawlersPaginateResponseCrawlersTargetsDynamoDBTargetsTypeDef],
        "CatalogTargets": List[GetCrawlersPaginateResponseCrawlersTargetsCatalogTargetsTypeDef],
    },
    total=False,
)


class GetCrawlersPaginateResponseCrawlersTargetsTypeDef(
    _GetCrawlersPaginateResponseCrawlersTargetsTypeDef
):
    pass


_GetCrawlersPaginateResponseCrawlersTypeDef = TypedDict(
    "_GetCrawlersPaginateResponseCrawlersTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": GetCrawlersPaginateResponseCrawlersTargetsTypeDef,
        "DatabaseName": str,
        "Description": str,
        "Classifiers": List[str],
        "SchemaChangePolicy": GetCrawlersPaginateResponseCrawlersSchemaChangePolicyTypeDef,
        "State": Literal["READY", "RUNNING", "STOPPING"],
        "TablePrefix": str,
        "Schedule": GetCrawlersPaginateResponseCrawlersScheduleTypeDef,
        "CrawlElapsedTime": int,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "LastCrawl": GetCrawlersPaginateResponseCrawlersLastCrawlTypeDef,
        "Version": int,
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
    },
    total=False,
)


class GetCrawlersPaginateResponseCrawlersTypeDef(_GetCrawlersPaginateResponseCrawlersTypeDef):
    """
    - *(dict) --*

      Specifies a crawler program that examines a data source and uses classifiers to try to
      determine its schema. If successful, the crawler records metadata concerning the data source
      in the AWS Glue Data Catalog.
      - **Name** *(string) --*

        The name of the crawler.
    """


_GetCrawlersPaginateResponseTypeDef = TypedDict(
    "_GetCrawlersPaginateResponseTypeDef",
    {"Crawlers": List[GetCrawlersPaginateResponseCrawlersTypeDef]},
    total=False,
)


class GetCrawlersPaginateResponseTypeDef(_GetCrawlersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Crawlers** *(list) --*

        A list of crawler metadata.
        - *(dict) --*

          Specifies a crawler program that examines a data source and uses classifiers to try to
          determine its schema. If successful, the crawler records metadata concerning the data
          source in the AWS Glue Data Catalog.
          - **Name** *(string) --*

            The name of the crawler.
    """


_GetDatabasesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDatabasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDatabasesPaginatePaginationConfigTypeDef(_GetDatabasesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "_GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef(
    _GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef
):
    pass


_GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsTypeDef = TypedDict(
    "_GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsTypeDef(
    _GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsTypeDef
):
    pass


_GetDatabasesPaginateResponseDatabaseListTypeDef = TypedDict(
    "_GetDatabasesPaginateResponseDatabaseListTypeDef",
    {
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTime": datetime,
        "CreateTableDefaultPermissions": List[
            GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)


class GetDatabasesPaginateResponseDatabaseListTypeDef(
    _GetDatabasesPaginateResponseDatabaseListTypeDef
):
    """
    - *(dict) --*

      The ``Database`` object represents a logical grouping of tables that might reside in a Hive
      metastore or an RDBMS.
      - **Name** *(string) --*

        The name of the database. For Hive compatibility, this is folded to lowercase when it is
        stored.
    """


_GetDatabasesPaginateResponseTypeDef = TypedDict(
    "_GetDatabasesPaginateResponseTypeDef",
    {"DatabaseList": List[GetDatabasesPaginateResponseDatabaseListTypeDef]},
    total=False,
)


class GetDatabasesPaginateResponseTypeDef(_GetDatabasesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **DatabaseList** *(list) --*

        A list of ``Database`` objects from the specified catalog.
        - *(dict) --*

          The ``Database`` object represents a logical grouping of tables that might reside in a
          Hive metastore or an RDBMS.
          - **Name** *(string) --*

            The name of the database. For Hive compatibility, this is folded to lowercase when it is
            stored.
    """


_GetDevEndpointsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDevEndpointsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDevEndpointsPaginatePaginationConfigTypeDef(
    _GetDevEndpointsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetDevEndpointsPaginateResponseDevEndpointsTypeDef = TypedDict(
    "_GetDevEndpointsPaginateResponseDevEndpointsTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "YarnEndpointAddress": str,
        "PrivateAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "PublicAddress": str,
        "Status": str,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "NumberOfNodes": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "LastUpdateStatus": str,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "PublicKey": str,
        "PublicKeys": List[str],
        "SecurityConfiguration": str,
        "Arguments": Dict[str, str],
    },
    total=False,
)


class GetDevEndpointsPaginateResponseDevEndpointsTypeDef(
    _GetDevEndpointsPaginateResponseDevEndpointsTypeDef
):
    """
    - *(dict) --*

      A development endpoint where a developer can remotely debug extract, transform, and load (ETL)
      scripts.
      - **EndpointName** *(string) --*

        The name of the ``DevEndpoint`` .
    """


_GetDevEndpointsPaginateResponseTypeDef = TypedDict(
    "_GetDevEndpointsPaginateResponseTypeDef",
    {"DevEndpoints": List[GetDevEndpointsPaginateResponseDevEndpointsTypeDef]},
    total=False,
)


class GetDevEndpointsPaginateResponseTypeDef(_GetDevEndpointsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **DevEndpoints** *(list) --*

        A list of ``DevEndpoint`` definitions.
        - *(dict) --*

          A development endpoint where a developer can remotely debug extract, transform, and load
          (ETL) scripts.
          - **EndpointName** *(string) --*

            The name of the ``DevEndpoint`` .
    """


_GetJobRunsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetJobRunsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetJobRunsPaginatePaginationConfigTypeDef(_GetJobRunsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetJobRunsPaginateResponseJobRunsNotificationPropertyTypeDef = TypedDict(
    "_GetJobRunsPaginateResponseJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class GetJobRunsPaginateResponseJobRunsNotificationPropertyTypeDef(
    _GetJobRunsPaginateResponseJobRunsNotificationPropertyTypeDef
):
    pass


_GetJobRunsPaginateResponseJobRunsPredecessorRunsTypeDef = TypedDict(
    "_GetJobRunsPaginateResponseJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)


class GetJobRunsPaginateResponseJobRunsPredecessorRunsTypeDef(
    _GetJobRunsPaginateResponseJobRunsPredecessorRunsTypeDef
):
    pass


_GetJobRunsPaginateResponseJobRunsTypeDef = TypedDict(
    "_GetJobRunsPaginateResponseJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[GetJobRunsPaginateResponseJobRunsPredecessorRunsTypeDef],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": GetJobRunsPaginateResponseJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class GetJobRunsPaginateResponseJobRunsTypeDef(_GetJobRunsPaginateResponseJobRunsTypeDef):
    """
    - *(dict) --*

      Contains information about a job run.
      - **Id** *(string) --*

        The ID of this job run.
    """


_GetJobRunsPaginateResponseTypeDef = TypedDict(
    "_GetJobRunsPaginateResponseTypeDef",
    {"JobRuns": List[GetJobRunsPaginateResponseJobRunsTypeDef]},
    total=False,
)


class GetJobRunsPaginateResponseTypeDef(_GetJobRunsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **JobRuns** *(list) --*

        A list of job-run metadata objects.
        - *(dict) --*

          Contains information about a job run.
          - **Id** *(string) --*

            The ID of this job run.
    """


_GetJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetJobsPaginatePaginationConfigTypeDef(_GetJobsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetJobsPaginateResponseJobsCommandTypeDef = TypedDict(
    "_GetJobsPaginateResponseJobsCommandTypeDef",
    {"Name": str, "ScriptLocation": str, "PythonVersion": str},
    total=False,
)


class GetJobsPaginateResponseJobsCommandTypeDef(_GetJobsPaginateResponseJobsCommandTypeDef):
    pass


_GetJobsPaginateResponseJobsConnectionsTypeDef = TypedDict(
    "_GetJobsPaginateResponseJobsConnectionsTypeDef", {"Connections": List[str]}, total=False
)


class GetJobsPaginateResponseJobsConnectionsTypeDef(_GetJobsPaginateResponseJobsConnectionsTypeDef):
    pass


_GetJobsPaginateResponseJobsExecutionPropertyTypeDef = TypedDict(
    "_GetJobsPaginateResponseJobsExecutionPropertyTypeDef", {"MaxConcurrentRuns": int}, total=False
)


class GetJobsPaginateResponseJobsExecutionPropertyTypeDef(
    _GetJobsPaginateResponseJobsExecutionPropertyTypeDef
):
    pass


_GetJobsPaginateResponseJobsNotificationPropertyTypeDef = TypedDict(
    "_GetJobsPaginateResponseJobsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class GetJobsPaginateResponseJobsNotificationPropertyTypeDef(
    _GetJobsPaginateResponseJobsNotificationPropertyTypeDef
):
    pass


_GetJobsPaginateResponseJobsTypeDef = TypedDict(
    "_GetJobsPaginateResponseJobsTypeDef",
    {
        "Name": str,
        "Description": str,
        "LogUri": str,
        "Role": str,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "ExecutionProperty": GetJobsPaginateResponseJobsExecutionPropertyTypeDef,
        "Command": GetJobsPaginateResponseJobsCommandTypeDef,
        "DefaultArguments": Dict[str, str],
        "Connections": GetJobsPaginateResponseJobsConnectionsTypeDef,
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": GetJobsPaginateResponseJobsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)


class GetJobsPaginateResponseJobsTypeDef(_GetJobsPaginateResponseJobsTypeDef):
    """
    - *(dict) --*

      Specifies a job definition.
      - **Name** *(string) --*

        The name you assign to this job definition.
    """


_GetJobsPaginateResponseTypeDef = TypedDict(
    "_GetJobsPaginateResponseTypeDef",
    {"Jobs": List[GetJobsPaginateResponseJobsTypeDef]},
    total=False,
)


class GetJobsPaginateResponseTypeDef(_GetJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Jobs** *(list) --*

        A list of job definitions.
        - *(dict) --*

          Specifies a job definition.
          - **Name** *(string) --*

            The name you assign to this job definition.
    """


_GetPartitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetPartitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetPartitionsPaginatePaginationConfigTypeDef(_GetPartitionsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetPartitionsPaginateResponsePartitionsStorageDescriptorColumnsTypeDef = TypedDict(
    "_GetPartitionsPaginateResponsePartitionsStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class GetPartitionsPaginateResponsePartitionsStorageDescriptorColumnsTypeDef(
    _GetPartitionsPaginateResponsePartitionsStorageDescriptorColumnsTypeDef
):
    pass


_GetPartitionsPaginateResponsePartitionsStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_GetPartitionsPaginateResponsePartitionsStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class GetPartitionsPaginateResponsePartitionsStorageDescriptorSerdeInfoTypeDef(
    _GetPartitionsPaginateResponsePartitionsStorageDescriptorSerdeInfoTypeDef
):
    pass


_GetPartitionsPaginateResponsePartitionsStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_GetPartitionsPaginateResponsePartitionsStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class GetPartitionsPaginateResponsePartitionsStorageDescriptorSkewedInfoTypeDef(
    _GetPartitionsPaginateResponsePartitionsStorageDescriptorSkewedInfoTypeDef
):
    pass


_GetPartitionsPaginateResponsePartitionsStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_GetPartitionsPaginateResponsePartitionsStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class GetPartitionsPaginateResponsePartitionsStorageDescriptorSortColumnsTypeDef(
    _GetPartitionsPaginateResponsePartitionsStorageDescriptorSortColumnsTypeDef
):
    pass


_GetPartitionsPaginateResponsePartitionsStorageDescriptorTypeDef = TypedDict(
    "_GetPartitionsPaginateResponsePartitionsStorageDescriptorTypeDef",
    {
        "Columns": List[GetPartitionsPaginateResponsePartitionsStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": GetPartitionsPaginateResponsePartitionsStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            GetPartitionsPaginateResponsePartitionsStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": GetPartitionsPaginateResponsePartitionsStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class GetPartitionsPaginateResponsePartitionsStorageDescriptorTypeDef(
    _GetPartitionsPaginateResponsePartitionsStorageDescriptorTypeDef
):
    pass


_GetPartitionsPaginateResponsePartitionsTypeDef = TypedDict(
    "_GetPartitionsPaginateResponsePartitionsTypeDef",
    {
        "Values": List[str],
        "DatabaseName": str,
        "TableName": str,
        "CreationTime": datetime,
        "LastAccessTime": datetime,
        "StorageDescriptor": GetPartitionsPaginateResponsePartitionsStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)


class GetPartitionsPaginateResponsePartitionsTypeDef(
    _GetPartitionsPaginateResponsePartitionsTypeDef
):
    """
    - *(dict) --*

      Represents a slice of table data.
      - **Values** *(list) --*

        The values of the partition.
        - *(string) --*
    """


_GetPartitionsPaginateResponseTypeDef = TypedDict(
    "_GetPartitionsPaginateResponseTypeDef",
    {"Partitions": List[GetPartitionsPaginateResponsePartitionsTypeDef]},
    total=False,
)


class GetPartitionsPaginateResponseTypeDef(_GetPartitionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Partitions** *(list) --*

        A list of requested partitions.
        - *(dict) --*

          Represents a slice of table data.
          - **Values** *(list) --*

            The values of the partition.
            - *(string) --*
    """


_RequiredGetPartitionsPaginateSegmentTypeDef = TypedDict(
    "_RequiredGetPartitionsPaginateSegmentTypeDef", {"SegmentNumber": int}
)
_OptionalGetPartitionsPaginateSegmentTypeDef = TypedDict(
    "_OptionalGetPartitionsPaginateSegmentTypeDef", {"TotalSegments": int}, total=False
)


class GetPartitionsPaginateSegmentTypeDef(
    _RequiredGetPartitionsPaginateSegmentTypeDef, _OptionalGetPartitionsPaginateSegmentTypeDef
):
    """
    The segment of the table's partitions to scan in this request.
    - **SegmentNumber** *(integer) --***[REQUIRED]**

      The zero-based index number of the segment. For example, if the total number of segments is 4,
      ``SegmentNumber`` values range from 0 through 3.
    """


_GetSecurityConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetSecurityConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetSecurityConfigurationsPaginatePaginationConfigTypeDef(
    _GetSecurityConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef = TypedDict(
    "_GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef",
    {"CloudWatchEncryptionMode": Literal["DISABLED", "SSE-KMS"], "KmsKeyArn": str},
    total=False,
)


class GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef(
    _GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef
):
    pass


_GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef = TypedDict(
    "_GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef",
    {"JobBookmarksEncryptionMode": Literal["DISABLED", "CSE-KMS"], "KmsKeyArn": str},
    total=False,
)


class GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef(
    _GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef
):
    pass


_GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef = TypedDict(
    "_GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef",
    {"S3EncryptionMode": Literal["DISABLED", "SSE-KMS", "SSE-S3"], "KmsKeyArn": str},
    total=False,
)


class GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef(
    _GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef
):
    pass


_GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationTypeDef = TypedDict(
    "_GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationTypeDef",
    {
        "S3Encryption": List[
            GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef
        ],
        "CloudWatchEncryption": GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef,
        "JobBookmarksEncryption": GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef,
    },
    total=False,
)


class GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationTypeDef(
    _GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationTypeDef
):
    pass


_GetSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef = TypedDict(
    "_GetSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef",
    {
        "Name": str,
        "CreatedTimeStamp": datetime,
        "EncryptionConfiguration": GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationTypeDef,
    },
    total=False,
)


class GetSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef(
    _GetSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef
):
    """
    - *(dict) --*

      Specifies a security configuration.
      - **Name** *(string) --*

        The name of the security configuration.
    """


_GetSecurityConfigurationsPaginateResponseTypeDef = TypedDict(
    "_GetSecurityConfigurationsPaginateResponseTypeDef",
    {
        "SecurityConfigurations": List[
            GetSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef
        ]
    },
    total=False,
)


class GetSecurityConfigurationsPaginateResponseTypeDef(
    _GetSecurityConfigurationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **SecurityConfigurations** *(list) --*

        A list of security configurations.
        - *(dict) --*

          Specifies a security configuration.
          - **Name** *(string) --*

            The name of the security configuration.
    """


_GetTableVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetTableVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetTableVersionsPaginatePaginationConfigTypeDef(
    _GetTableVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetTableVersionsPaginateResponseTableVersionsTablePartitionKeysTypeDef = TypedDict(
    "_GetTableVersionsPaginateResponseTableVersionsTablePartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class GetTableVersionsPaginateResponseTableVersionsTablePartitionKeysTypeDef(
    _GetTableVersionsPaginateResponseTableVersionsTablePartitionKeysTypeDef
):
    pass


_GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorColumnsTypeDef = TypedDict(
    "_GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorColumnsTypeDef(
    _GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorColumnsTypeDef
):
    pass


_GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef(
    _GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef
):
    pass


_GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef(
    _GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef
):
    pass


_GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef(
    _GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef
):
    pass


_GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorTypeDef = TypedDict(
    "_GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorTypeDef",
    {
        "Columns": List[
            GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorColumnsTypeDef
        ],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorTypeDef(
    _GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorTypeDef
):
    pass


_GetTableVersionsPaginateResponseTableVersionsTableTypeDef = TypedDict(
    "_GetTableVersionsPaginateResponseTableVersionsTableTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorTypeDef,
        "PartitionKeys": List[
            GetTableVersionsPaginateResponseTableVersionsTablePartitionKeysTypeDef
        ],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)


class GetTableVersionsPaginateResponseTableVersionsTableTypeDef(
    _GetTableVersionsPaginateResponseTableVersionsTableTypeDef
):
    """
    - **Table** *(dict) --*

      The table in question.
      - **Name** *(string) --*

        The table name. For Hive compatibility, this must be entirely lowercase.
    """


_GetTableVersionsPaginateResponseTableVersionsTypeDef = TypedDict(
    "_GetTableVersionsPaginateResponseTableVersionsTypeDef",
    {"Table": GetTableVersionsPaginateResponseTableVersionsTableTypeDef, "VersionId": str},
    total=False,
)


class GetTableVersionsPaginateResponseTableVersionsTypeDef(
    _GetTableVersionsPaginateResponseTableVersionsTypeDef
):
    """
    - *(dict) --*

      Specifies a version of a table.
      - **Table** *(dict) --*

        The table in question.
        - **Name** *(string) --*

          The table name. For Hive compatibility, this must be entirely lowercase.
    """


_GetTableVersionsPaginateResponseTypeDef = TypedDict(
    "_GetTableVersionsPaginateResponseTypeDef",
    {"TableVersions": List[GetTableVersionsPaginateResponseTableVersionsTypeDef]},
    total=False,
)


class GetTableVersionsPaginateResponseTypeDef(_GetTableVersionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TableVersions** *(list) --*

        A list of strings identifying available versions of the specified table.
        - *(dict) --*

          Specifies a version of a table.
          - **Table** *(dict) --*

            The table in question.
            - **Name** *(string) --*

              The table name. For Hive compatibility, this must be entirely lowercase.
    """


_GetTablesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetTablesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetTablesPaginatePaginationConfigTypeDef(_GetTablesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetTablesPaginateResponseTableListPartitionKeysTypeDef = TypedDict(
    "_GetTablesPaginateResponseTableListPartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class GetTablesPaginateResponseTableListPartitionKeysTypeDef(
    _GetTablesPaginateResponseTableListPartitionKeysTypeDef
):
    pass


_GetTablesPaginateResponseTableListStorageDescriptorColumnsTypeDef = TypedDict(
    "_GetTablesPaginateResponseTableListStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class GetTablesPaginateResponseTableListStorageDescriptorColumnsTypeDef(
    _GetTablesPaginateResponseTableListStorageDescriptorColumnsTypeDef
):
    pass


_GetTablesPaginateResponseTableListStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "_GetTablesPaginateResponseTableListStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)


class GetTablesPaginateResponseTableListStorageDescriptorSerdeInfoTypeDef(
    _GetTablesPaginateResponseTableListStorageDescriptorSerdeInfoTypeDef
):
    pass


_GetTablesPaginateResponseTableListStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "_GetTablesPaginateResponseTableListStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)


class GetTablesPaginateResponseTableListStorageDescriptorSkewedInfoTypeDef(
    _GetTablesPaginateResponseTableListStorageDescriptorSkewedInfoTypeDef
):
    pass


_GetTablesPaginateResponseTableListStorageDescriptorSortColumnsTypeDef = TypedDict(
    "_GetTablesPaginateResponseTableListStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)


class GetTablesPaginateResponseTableListStorageDescriptorSortColumnsTypeDef(
    _GetTablesPaginateResponseTableListStorageDescriptorSortColumnsTypeDef
):
    pass


_GetTablesPaginateResponseTableListStorageDescriptorTypeDef = TypedDict(
    "_GetTablesPaginateResponseTableListStorageDescriptorTypeDef",
    {
        "Columns": List[GetTablesPaginateResponseTableListStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": GetTablesPaginateResponseTableListStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[GetTablesPaginateResponseTableListStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": GetTablesPaginateResponseTableListStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)


class GetTablesPaginateResponseTableListStorageDescriptorTypeDef(
    _GetTablesPaginateResponseTableListStorageDescriptorTypeDef
):
    pass


_GetTablesPaginateResponseTableListTypeDef = TypedDict(
    "_GetTablesPaginateResponseTableListTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": GetTablesPaginateResponseTableListStorageDescriptorTypeDef,
        "PartitionKeys": List[GetTablesPaginateResponseTableListPartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)


class GetTablesPaginateResponseTableListTypeDef(_GetTablesPaginateResponseTableListTypeDef):
    """
    - *(dict) --*

      Represents a collection of related data organized in columns and rows.
      - **Name** *(string) --*

        The table name. For Hive compatibility, this must be entirely lowercase.
    """


_GetTablesPaginateResponseTypeDef = TypedDict(
    "_GetTablesPaginateResponseTypeDef",
    {"TableList": List[GetTablesPaginateResponseTableListTypeDef]},
    total=False,
)


class GetTablesPaginateResponseTypeDef(_GetTablesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TableList** *(list) --*

        A list of the requested ``Table`` objects.
        - *(dict) --*

          Represents a collection of related data organized in columns and rows.
          - **Name** *(string) --*

            The table name. For Hive compatibility, this must be entirely lowercase.
    """


_GetTriggersPaginatePaginationConfigTypeDef = TypedDict(
    "_GetTriggersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetTriggersPaginatePaginationConfigTypeDef(_GetTriggersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetTriggersPaginateResponseTriggersActionsNotificationPropertyTypeDef = TypedDict(
    "_GetTriggersPaginateResponseTriggersActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)


class GetTriggersPaginateResponseTriggersActionsNotificationPropertyTypeDef(
    _GetTriggersPaginateResponseTriggersActionsNotificationPropertyTypeDef
):
    pass


_GetTriggersPaginateResponseTriggersActionsTypeDef = TypedDict(
    "_GetTriggersPaginateResponseTriggersActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": GetTriggersPaginateResponseTriggersActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)


class GetTriggersPaginateResponseTriggersActionsTypeDef(
    _GetTriggersPaginateResponseTriggersActionsTypeDef
):
    pass


_GetTriggersPaginateResponseTriggersPredicateConditionsTypeDef = TypedDict(
    "_GetTriggersPaginateResponseTriggersPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)


class GetTriggersPaginateResponseTriggersPredicateConditionsTypeDef(
    _GetTriggersPaginateResponseTriggersPredicateConditionsTypeDef
):
    pass


_GetTriggersPaginateResponseTriggersPredicateTypeDef = TypedDict(
    "_GetTriggersPaginateResponseTriggersPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[GetTriggersPaginateResponseTriggersPredicateConditionsTypeDef],
    },
    total=False,
)


class GetTriggersPaginateResponseTriggersPredicateTypeDef(
    _GetTriggersPaginateResponseTriggersPredicateTypeDef
):
    pass


_GetTriggersPaginateResponseTriggersTypeDef = TypedDict(
    "_GetTriggersPaginateResponseTriggersTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[GetTriggersPaginateResponseTriggersActionsTypeDef],
        "Predicate": GetTriggersPaginateResponseTriggersPredicateTypeDef,
    },
    total=False,
)


class GetTriggersPaginateResponseTriggersTypeDef(_GetTriggersPaginateResponseTriggersTypeDef):
    """
    - *(dict) --*

      Information about a specific trigger.
      - **Name** *(string) --*

        The name of the trigger.
    """


_GetTriggersPaginateResponseTypeDef = TypedDict(
    "_GetTriggersPaginateResponseTypeDef",
    {"Triggers": List[GetTriggersPaginateResponseTriggersTypeDef]},
    total=False,
)


class GetTriggersPaginateResponseTypeDef(_GetTriggersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Triggers** *(list) --*

        A list of triggers for the specified job.
        - *(dict) --*

          Information about a specific trigger.
          - **Name** *(string) --*

            The name of the trigger.
    """


_GetUserDefinedFunctionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetUserDefinedFunctionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetUserDefinedFunctionsPaginatePaginationConfigTypeDef(
    _GetUserDefinedFunctionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsResourceUrisTypeDef = TypedDict(
    "_GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsResourceUrisTypeDef",
    {"ResourceType": Literal["JAR", "FILE", "ARCHIVE"], "Uri": str},
    total=False,
)


class GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsResourceUrisTypeDef(
    _GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsResourceUrisTypeDef
):
    pass


_GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsTypeDef = TypedDict(
    "_GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsTypeDef",
    {
        "FunctionName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": Literal["USER", "ROLE", "GROUP"],
        "CreateTime": datetime,
        "ResourceUris": List[
            GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsResourceUrisTypeDef
        ],
    },
    total=False,
)


class GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsTypeDef(
    _GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsTypeDef
):
    """
    - *(dict) --*

      Represents the equivalent of a Hive user-defined function (``UDF`` ) definition.
      - **FunctionName** *(string) --*

        The name of the function.
    """


_GetUserDefinedFunctionsPaginateResponseTypeDef = TypedDict(
    "_GetUserDefinedFunctionsPaginateResponseTypeDef",
    {
        "UserDefinedFunctions": List[
            GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsTypeDef
        ]
    },
    total=False,
)


class GetUserDefinedFunctionsPaginateResponseTypeDef(
    _GetUserDefinedFunctionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **UserDefinedFunctions** *(list) --*

        A list of requested function definitions.
        - *(dict) --*

          Represents the equivalent of a Hive user-defined function (``UDF`` ) definition.
          - **FunctionName** *(string) --*

            The name of the function.
    """
