"Main interface for ssm service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientCancelMaintenanceWindowExecutionResponseTypeDef",
    "ClientCreateActivationResponseTypeDef",
    "ClientCreateActivationTagsTypeDef",
    "ClientCreateAssociationBatchEntriesOutputLocationS3LocationTypeDef",
    "ClientCreateAssociationBatchEntriesOutputLocationTypeDef",
    "ClientCreateAssociationBatchEntriesTargetsTypeDef",
    "ClientCreateAssociationBatchEntriesTypeDef",
    "ClientCreateAssociationBatchResponseFailedEntryOutputLocationS3LocationTypeDef",
    "ClientCreateAssociationBatchResponseFailedEntryOutputLocationTypeDef",
    "ClientCreateAssociationBatchResponseFailedEntryTargetsTypeDef",
    "ClientCreateAssociationBatchResponseFailedEntryTypeDef",
    "ClientCreateAssociationBatchResponseFailedTypeDef",
    "ClientCreateAssociationBatchResponseSuccessfulOutputLocationS3LocationTypeDef",
    "ClientCreateAssociationBatchResponseSuccessfulOutputLocationTypeDef",
    "ClientCreateAssociationBatchResponseSuccessfulOverviewTypeDef",
    "ClientCreateAssociationBatchResponseSuccessfulStatusTypeDef",
    "ClientCreateAssociationBatchResponseSuccessfulTargetsTypeDef",
    "ClientCreateAssociationBatchResponseSuccessfulTypeDef",
    "ClientCreateAssociationBatchResponseTypeDef",
    "ClientCreateAssociationOutputLocationS3LocationTypeDef",
    "ClientCreateAssociationOutputLocationTypeDef",
    "ClientCreateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    "ClientCreateAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    "ClientCreateAssociationResponseAssociationDescriptionOverviewTypeDef",
    "ClientCreateAssociationResponseAssociationDescriptionStatusTypeDef",
    "ClientCreateAssociationResponseAssociationDescriptionTargetsTypeDef",
    "ClientCreateAssociationResponseAssociationDescriptionTypeDef",
    "ClientCreateAssociationResponseTypeDef",
    "ClientCreateAssociationTargetsTypeDef",
    "ClientCreateDocumentAttachmentsTypeDef",
    "ClientCreateDocumentRequiresTypeDef",
    "ClientCreateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef",
    "ClientCreateDocumentResponseDocumentDescriptionParametersTypeDef",
    "ClientCreateDocumentResponseDocumentDescriptionRequiresTypeDef",
    "ClientCreateDocumentResponseDocumentDescriptionTagsTypeDef",
    "ClientCreateDocumentResponseDocumentDescriptionTypeDef",
    "ClientCreateDocumentResponseTypeDef",
    "ClientCreateDocumentTagsTypeDef",
    "ClientCreateMaintenanceWindowResponseTypeDef",
    "ClientCreateMaintenanceWindowTagsTypeDef",
    "ClientCreateOpsItemNotificationsTypeDef",
    "ClientCreateOpsItemOperationalDataTypeDef",
    "ClientCreateOpsItemRelatedOpsItemsTypeDef",
    "ClientCreateOpsItemResponseTypeDef",
    "ClientCreateOpsItemTagsTypeDef",
    "ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    "ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    "ClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef",
    "ClientCreatePatchBaselineApprovalRulesTypeDef",
    "ClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    "ClientCreatePatchBaselineGlobalFiltersTypeDef",
    "ClientCreatePatchBaselineResponseTypeDef",
    "ClientCreatePatchBaselineSourcesTypeDef",
    "ClientCreatePatchBaselineTagsTypeDef",
    "ClientCreateResourceDataSyncS3DestinationTypeDef",
    "ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    "ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef",
    "ClientCreateResourceDataSyncSyncSourceTypeDef",
    "ClientDeleteInventoryResponseDeletionSummarySummaryItemsTypeDef",
    "ClientDeleteInventoryResponseDeletionSummaryTypeDef",
    "ClientDeleteInventoryResponseTypeDef",
    "ClientDeleteMaintenanceWindowResponseTypeDef",
    "ClientDeleteParametersResponseTypeDef",
    "ClientDeletePatchBaselineResponseTypeDef",
    "ClientDeregisterPatchBaselineForPatchGroupResponseTypeDef",
    "ClientDeregisterTargetFromMaintenanceWindowResponseTypeDef",
    "ClientDeregisterTaskFromMaintenanceWindowResponseTypeDef",
    "ClientDescribeActivationsFiltersTypeDef",
    "ClientDescribeActivationsResponseActivationListTagsTypeDef",
    "ClientDescribeActivationsResponseActivationListTypeDef",
    "ClientDescribeActivationsResponseTypeDef",
    "ClientDescribeAssociationExecutionTargetsFiltersTypeDef",
    "ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsOutputSourceTypeDef",
    "ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsTypeDef",
    "ClientDescribeAssociationExecutionTargetsResponseTypeDef",
    "ClientDescribeAssociationExecutionsFiltersTypeDef",
    "ClientDescribeAssociationExecutionsResponseAssociationExecutionsTypeDef",
    "ClientDescribeAssociationExecutionsResponseTypeDef",
    "ClientDescribeAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    "ClientDescribeAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    "ClientDescribeAssociationResponseAssociationDescriptionOverviewTypeDef",
    "ClientDescribeAssociationResponseAssociationDescriptionStatusTypeDef",
    "ClientDescribeAssociationResponseAssociationDescriptionTargetsTypeDef",
    "ClientDescribeAssociationResponseAssociationDescriptionTypeDef",
    "ClientDescribeAssociationResponseTypeDef",
    "ClientDescribeAutomationExecutionsFiltersTypeDef",
    "ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListResolvedTargetsTypeDef",
    "ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTargetsTypeDef",
    "ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTypeDef",
    "ClientDescribeAutomationExecutionsResponseTypeDef",
    "ClientDescribeAutomationStepExecutionsFiltersTypeDef",
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsFailureDetailsTypeDef",
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetLocationTypeDef",
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetsTypeDef",
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsTypeDef",
    "ClientDescribeAutomationStepExecutionsResponseTypeDef",
    "ClientDescribeAvailablePatchesFiltersTypeDef",
    "ClientDescribeAvailablePatchesResponsePatchesTypeDef",
    "ClientDescribeAvailablePatchesResponseTypeDef",
    "ClientDescribeDocumentPermissionResponseAccountSharingInfoListTypeDef",
    "ClientDescribeDocumentPermissionResponseTypeDef",
    "ClientDescribeDocumentResponseDocumentAttachmentsInformationTypeDef",
    "ClientDescribeDocumentResponseDocumentParametersTypeDef",
    "ClientDescribeDocumentResponseDocumentRequiresTypeDef",
    "ClientDescribeDocumentResponseDocumentTagsTypeDef",
    "ClientDescribeDocumentResponseDocumentTypeDef",
    "ClientDescribeDocumentResponseTypeDef",
    "ClientDescribeEffectiveInstanceAssociationsResponseAssociationsTypeDef",
    "ClientDescribeEffectiveInstanceAssociationsResponseTypeDef",
    "ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchStatusTypeDef",
    "ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchTypeDef",
    "ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesTypeDef",
    "ClientDescribeEffectivePatchesForPatchBaselineResponseTypeDef",
    "ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef",
    "ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlTypeDef",
    "ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosTypeDef",
    "ClientDescribeInstanceAssociationsStatusResponseTypeDef",
    "ClientDescribeInstanceInformationFiltersTypeDef",
    "ClientDescribeInstanceInformationInstanceInformationFilterListTypeDef",
    "ClientDescribeInstanceInformationResponseInstanceInformationListAssociationOverviewTypeDef",
    "ClientDescribeInstanceInformationResponseInstanceInformationListTypeDef",
    "ClientDescribeInstanceInformationResponseTypeDef",
    "ClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef",
    "ClientDescribeInstancePatchStatesForPatchGroupResponseInstancePatchStatesTypeDef",
    "ClientDescribeInstancePatchStatesForPatchGroupResponseTypeDef",
    "ClientDescribeInstancePatchStatesResponseInstancePatchStatesTypeDef",
    "ClientDescribeInstancePatchStatesResponseTypeDef",
    "ClientDescribeInstancePatchesFiltersTypeDef",
    "ClientDescribeInstancePatchesResponsePatchesTypeDef",
    "ClientDescribeInstancePatchesResponseTypeDef",
    "ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef",
    "ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummaryTypeDef",
    "ClientDescribeInventoryDeletionsResponseInventoryDeletionsTypeDef",
    "ClientDescribeInventoryDeletionsResponseTypeDef",
    "ClientDescribeMaintenanceWindowExecutionTaskInvocationsFiltersTypeDef",
    "ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseWindowExecutionTaskInvocationIdentitiesTypeDef",
    "ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseTypeDef",
    "ClientDescribeMaintenanceWindowExecutionTasksFiltersTypeDef",
    "ClientDescribeMaintenanceWindowExecutionTasksResponseWindowExecutionTaskIdentitiesTypeDef",
    "ClientDescribeMaintenanceWindowExecutionTasksResponseTypeDef",
    "ClientDescribeMaintenanceWindowExecutionsFiltersTypeDef",
    "ClientDescribeMaintenanceWindowExecutionsResponseWindowExecutionsTypeDef",
    "ClientDescribeMaintenanceWindowExecutionsResponseTypeDef",
    "ClientDescribeMaintenanceWindowScheduleFiltersTypeDef",
    "ClientDescribeMaintenanceWindowScheduleResponseScheduledWindowExecutionsTypeDef",
    "ClientDescribeMaintenanceWindowScheduleResponseTypeDef",
    "ClientDescribeMaintenanceWindowScheduleTargetsTypeDef",
    "ClientDescribeMaintenanceWindowTargetsFiltersTypeDef",
    "ClientDescribeMaintenanceWindowTargetsResponseTargetsTargetsTypeDef",
    "ClientDescribeMaintenanceWindowTargetsResponseTargetsTypeDef",
    "ClientDescribeMaintenanceWindowTargetsResponseTypeDef",
    "ClientDescribeMaintenanceWindowTasksFiltersTypeDef",
    "ClientDescribeMaintenanceWindowTasksResponseTasksLoggingInfoTypeDef",
    "ClientDescribeMaintenanceWindowTasksResponseTasksTargetsTypeDef",
    "ClientDescribeMaintenanceWindowTasksResponseTasksTaskParametersTypeDef",
    "ClientDescribeMaintenanceWindowTasksResponseTasksTypeDef",
    "ClientDescribeMaintenanceWindowTasksResponseTypeDef",
    "ClientDescribeMaintenanceWindowsFiltersTypeDef",
    "ClientDescribeMaintenanceWindowsForTargetResponseWindowIdentitiesTypeDef",
    "ClientDescribeMaintenanceWindowsForTargetResponseTypeDef",
    "ClientDescribeMaintenanceWindowsForTargetTargetsTypeDef",
    "ClientDescribeMaintenanceWindowsResponseWindowIdentitiesTypeDef",
    "ClientDescribeMaintenanceWindowsResponseTypeDef",
    "ClientDescribeOpsItemsOpsItemFiltersTypeDef",
    "ClientDescribeOpsItemsResponseOpsItemSummariesOperationalDataTypeDef",
    "ClientDescribeOpsItemsResponseOpsItemSummariesTypeDef",
    "ClientDescribeOpsItemsResponseTypeDef",
    "ClientDescribeParametersFiltersTypeDef",
    "ClientDescribeParametersParameterFiltersTypeDef",
    "ClientDescribeParametersResponseParametersPoliciesTypeDef",
    "ClientDescribeParametersResponseParametersTypeDef",
    "ClientDescribeParametersResponseTypeDef",
    "ClientDescribePatchBaselinesFiltersTypeDef",
    "ClientDescribePatchBaselinesResponseBaselineIdentitiesTypeDef",
    "ClientDescribePatchBaselinesResponseTypeDef",
    "ClientDescribePatchGroupStateResponseTypeDef",
    "ClientDescribePatchGroupsFiltersTypeDef",
    "ClientDescribePatchGroupsResponseMappingsBaselineIdentityTypeDef",
    "ClientDescribePatchGroupsResponseMappingsTypeDef",
    "ClientDescribePatchGroupsResponseTypeDef",
    "ClientDescribePatchPropertiesResponseTypeDef",
    "ClientDescribeSessionsFiltersTypeDef",
    "ClientDescribeSessionsResponseSessionsOutputUrlTypeDef",
    "ClientDescribeSessionsResponseSessionsTypeDef",
    "ClientDescribeSessionsResponseTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionProgressCountersTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionResolvedTargetsTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsFailureDetailsTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetLocationTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetsTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionTargetLocationsTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionTargetsTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionTypeDef",
    "ClientGetAutomationExecutionResponseTypeDef",
    "ClientGetCommandInvocationResponseCloudWatchOutputConfigTypeDef",
    "ClientGetCommandInvocationResponseTypeDef",
    "ClientGetConnectionStatusResponseTypeDef",
    "ClientGetDefaultPatchBaselineResponseTypeDef",
    "ClientGetDeployablePatchSnapshotForInstanceResponseTypeDef",
    "ClientGetDocumentResponseAttachmentsContentTypeDef",
    "ClientGetDocumentResponseRequiresTypeDef",
    "ClientGetDocumentResponseTypeDef",
    "ClientGetInventoryAggregatorsGroupsFiltersTypeDef",
    "ClientGetInventoryAggregatorsGroupsTypeDef",
    "ClientGetInventoryAggregatorsTypeDef",
    "ClientGetInventoryFiltersTypeDef",
    "ClientGetInventoryResponseEntitiesDataTypeDef",
    "ClientGetInventoryResponseEntitiesTypeDef",
    "ClientGetInventoryResponseTypeDef",
    "ClientGetInventoryResultAttributesTypeDef",
    "ClientGetInventorySchemaResponseSchemasAttributesTypeDef",
    "ClientGetInventorySchemaResponseSchemasTypeDef",
    "ClientGetInventorySchemaResponseTypeDef",
    "ClientGetMaintenanceWindowExecutionResponseTypeDef",
    "ClientGetMaintenanceWindowExecutionTaskInvocationResponseTypeDef",
    "ClientGetMaintenanceWindowExecutionTaskResponseTaskParametersTypeDef",
    "ClientGetMaintenanceWindowExecutionTaskResponseTypeDef",
    "ClientGetMaintenanceWindowResponseTypeDef",
    "ClientGetMaintenanceWindowTaskResponseLoggingInfoTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTargetsTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskParametersTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTypeDef",
    "ClientGetOpsItemResponseOpsItemNotificationsTypeDef",
    "ClientGetOpsItemResponseOpsItemOperationalDataTypeDef",
    "ClientGetOpsItemResponseOpsItemRelatedOpsItemsTypeDef",
    "ClientGetOpsItemResponseOpsItemTypeDef",
    "ClientGetOpsItemResponseTypeDef",
    "ClientGetOpsSummaryAggregatorsFiltersTypeDef",
    "ClientGetOpsSummaryAggregatorsTypeDef",
    "ClientGetOpsSummaryFiltersTypeDef",
    "ClientGetOpsSummaryResponseEntitiesDataTypeDef",
    "ClientGetOpsSummaryResponseEntitiesTypeDef",
    "ClientGetOpsSummaryResponseTypeDef",
    "ClientGetOpsSummaryResultAttributesTypeDef",
    "ClientGetParameterHistoryResponseParametersPoliciesTypeDef",
    "ClientGetParameterHistoryResponseParametersTypeDef",
    "ClientGetParameterHistoryResponseTypeDef",
    "ClientGetParameterResponseParameterTypeDef",
    "ClientGetParameterResponseTypeDef",
    "ClientGetParametersByPathParameterFiltersTypeDef",
    "ClientGetParametersByPathResponseParametersTypeDef",
    "ClientGetParametersByPathResponseTypeDef",
    "ClientGetParametersResponseParametersTypeDef",
    "ClientGetParametersResponseTypeDef",
    "ClientGetPatchBaselineForPatchGroupResponseTypeDef",
    "ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    "ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    "ClientGetPatchBaselineResponseApprovalRulesPatchRulesTypeDef",
    "ClientGetPatchBaselineResponseApprovalRulesTypeDef",
    "ClientGetPatchBaselineResponseGlobalFiltersPatchFiltersTypeDef",
    "ClientGetPatchBaselineResponseGlobalFiltersTypeDef",
    "ClientGetPatchBaselineResponseSourcesTypeDef",
    "ClientGetPatchBaselineResponseTypeDef",
    "ClientGetServiceSettingResponseServiceSettingTypeDef",
    "ClientGetServiceSettingResponseTypeDef",
    "ClientLabelParameterVersionResponseTypeDef",
    "ClientListAssociationVersionsResponseAssociationVersionsOutputLocationS3LocationTypeDef",
    "ClientListAssociationVersionsResponseAssociationVersionsOutputLocationTypeDef",
    "ClientListAssociationVersionsResponseAssociationVersionsTargetsTypeDef",
    "ClientListAssociationVersionsResponseAssociationVersionsTypeDef",
    "ClientListAssociationVersionsResponseTypeDef",
    "ClientListAssociationsAssociationFilterListTypeDef",
    "ClientListAssociationsResponseAssociationsOverviewTypeDef",
    "ClientListAssociationsResponseAssociationsTargetsTypeDef",
    "ClientListAssociationsResponseAssociationsTypeDef",
    "ClientListAssociationsResponseTypeDef",
    "ClientListCommandInvocationsFiltersTypeDef",
    "ClientListCommandInvocationsResponseCommandInvocationsCloudWatchOutputConfigTypeDef",
    "ClientListCommandInvocationsResponseCommandInvocationsCommandPluginsTypeDef",
    "ClientListCommandInvocationsResponseCommandInvocationsNotificationConfigTypeDef",
    "ClientListCommandInvocationsResponseCommandInvocationsTypeDef",
    "ClientListCommandInvocationsResponseTypeDef",
    "ClientListCommandsFiltersTypeDef",
    "ClientListCommandsResponseCommandsCloudWatchOutputConfigTypeDef",
    "ClientListCommandsResponseCommandsNotificationConfigTypeDef",
    "ClientListCommandsResponseCommandsTargetsTypeDef",
    "ClientListCommandsResponseCommandsTypeDef",
    "ClientListCommandsResponseTypeDef",
    "ClientListComplianceItemsFiltersTypeDef",
    "ClientListComplianceItemsResponseComplianceItemsExecutionSummaryTypeDef",
    "ClientListComplianceItemsResponseComplianceItemsTypeDef",
    "ClientListComplianceItemsResponseTypeDef",
    "ClientListComplianceSummariesFiltersTypeDef",
    "ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    "ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummaryTypeDef",
    "ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    "ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummaryTypeDef",
    "ClientListComplianceSummariesResponseComplianceSummaryItemsTypeDef",
    "ClientListComplianceSummariesResponseTypeDef",
    "ClientListDocumentVersionsResponseDocumentVersionsTypeDef",
    "ClientListDocumentVersionsResponseTypeDef",
    "ClientListDocumentsDocumentFilterListTypeDef",
    "ClientListDocumentsFiltersTypeDef",
    "ClientListDocumentsResponseDocumentIdentifiersRequiresTypeDef",
    "ClientListDocumentsResponseDocumentIdentifiersTagsTypeDef",
    "ClientListDocumentsResponseDocumentIdentifiersTypeDef",
    "ClientListDocumentsResponseTypeDef",
    "ClientListInventoryEntriesFiltersTypeDef",
    "ClientListInventoryEntriesResponseTypeDef",
    "ClientListResourceComplianceSummariesFiltersTypeDef",
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef",
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef",
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef",
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsTypeDef",
    "ClientListResourceComplianceSummariesResponseTypeDef",
    "ClientListResourceDataSyncResponseResourceDataSyncItemsS3DestinationTypeDef",
    "ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    "ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef",
    "ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceTypeDef",
    "ClientListResourceDataSyncResponseResourceDataSyncItemsTypeDef",
    "ClientListResourceDataSyncResponseTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutComplianceItemsExecutionSummaryTypeDef",
    "ClientPutComplianceItemsItemsTypeDef",
    "ClientPutInventoryItemsTypeDef",
    "ClientPutInventoryResponseTypeDef",
    "ClientPutParameterResponseTypeDef",
    "ClientPutParameterTagsTypeDef",
    "ClientRegisterDefaultPatchBaselineResponseTypeDef",
    "ClientRegisterPatchBaselineForPatchGroupResponseTypeDef",
    "ClientRegisterTargetWithMaintenanceWindowResponseTypeDef",
    "ClientRegisterTargetWithMaintenanceWindowTargetsTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowLoggingInfoTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowResponseTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTargetsTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersAutomationTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersLambdaTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersStepFunctionsTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskParametersTypeDef",
    "ClientResetServiceSettingResponseServiceSettingTypeDef",
    "ClientResetServiceSettingResponseTypeDef",
    "ClientResumeSessionResponseTypeDef",
    "ClientSendCommandCloudWatchOutputConfigTypeDef",
    "ClientSendCommandNotificationConfigTypeDef",
    "ClientSendCommandResponseCommandCloudWatchOutputConfigTypeDef",
    "ClientSendCommandResponseCommandNotificationConfigTypeDef",
    "ClientSendCommandResponseCommandTargetsTypeDef",
    "ClientSendCommandResponseCommandTypeDef",
    "ClientSendCommandResponseTypeDef",
    "ClientSendCommandTargetsTypeDef",
    "ClientStartAutomationExecutionResponseTypeDef",
    "ClientStartAutomationExecutionTargetLocationsTypeDef",
    "ClientStartAutomationExecutionTargetsTypeDef",
    "ClientStartSessionResponseTypeDef",
    "ClientTerminateSessionResponseTypeDef",
    "ClientUpdateAssociationOutputLocationS3LocationTypeDef",
    "ClientUpdateAssociationOutputLocationTypeDef",
    "ClientUpdateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    "ClientUpdateAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    "ClientUpdateAssociationResponseAssociationDescriptionOverviewTypeDef",
    "ClientUpdateAssociationResponseAssociationDescriptionStatusTypeDef",
    "ClientUpdateAssociationResponseAssociationDescriptionTargetsTypeDef",
    "ClientUpdateAssociationResponseAssociationDescriptionTypeDef",
    "ClientUpdateAssociationResponseTypeDef",
    "ClientUpdateAssociationStatusAssociationStatusTypeDef",
    "ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    "ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationTypeDef",
    "ClientUpdateAssociationStatusResponseAssociationDescriptionOverviewTypeDef",
    "ClientUpdateAssociationStatusResponseAssociationDescriptionStatusTypeDef",
    "ClientUpdateAssociationStatusResponseAssociationDescriptionTargetsTypeDef",
    "ClientUpdateAssociationStatusResponseAssociationDescriptionTypeDef",
    "ClientUpdateAssociationStatusResponseTypeDef",
    "ClientUpdateAssociationTargetsTypeDef",
    "ClientUpdateDocumentAttachmentsTypeDef",
    "ClientUpdateDocumentDefaultVersionResponseDescriptionTypeDef",
    "ClientUpdateDocumentDefaultVersionResponseTypeDef",
    "ClientUpdateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef",
    "ClientUpdateDocumentResponseDocumentDescriptionParametersTypeDef",
    "ClientUpdateDocumentResponseDocumentDescriptionRequiresTypeDef",
    "ClientUpdateDocumentResponseDocumentDescriptionTagsTypeDef",
    "ClientUpdateDocumentResponseDocumentDescriptionTypeDef",
    "ClientUpdateDocumentResponseTypeDef",
    "ClientUpdateMaintenanceWindowResponseTypeDef",
    "ClientUpdateMaintenanceWindowTargetResponseTargetsTypeDef",
    "ClientUpdateMaintenanceWindowTargetResponseTypeDef",
    "ClientUpdateMaintenanceWindowTargetTargetsTypeDef",
    "ClientUpdateMaintenanceWindowTaskLoggingInfoTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseLoggingInfoTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTargetsTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskParametersTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTypeDef",
    "ClientUpdateMaintenanceWindowTaskTargetsTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersAutomationTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersLambdaTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersStepFunctionsTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskParametersTypeDef",
    "ClientUpdateOpsItemNotificationsTypeDef",
    "ClientUpdateOpsItemOperationalDataTypeDef",
    "ClientUpdateOpsItemRelatedOpsItemsTypeDef",
    "ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    "ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    "ClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef",
    "ClientUpdatePatchBaselineApprovalRulesTypeDef",
    "ClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    "ClientUpdatePatchBaselineGlobalFiltersTypeDef",
    "ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    "ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    "ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesTypeDef",
    "ClientUpdatePatchBaselineResponseApprovalRulesTypeDef",
    "ClientUpdatePatchBaselineResponseGlobalFiltersPatchFiltersTypeDef",
    "ClientUpdatePatchBaselineResponseGlobalFiltersTypeDef",
    "ClientUpdatePatchBaselineResponseSourcesTypeDef",
    "ClientUpdatePatchBaselineResponseTypeDef",
    "ClientUpdatePatchBaselineSourcesTypeDef",
    "ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    "ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef",
    "ClientUpdateResourceDataSyncSyncSourceTypeDef",
    "DescribeActivationsPaginateFiltersTypeDef",
    "DescribeActivationsPaginatePaginationConfigTypeDef",
    "DescribeActivationsPaginateResponseActivationListTagsTypeDef",
    "DescribeActivationsPaginateResponseActivationListTypeDef",
    "DescribeActivationsPaginateResponseTypeDef",
    "DescribeAssociationExecutionTargetsPaginateFiltersTypeDef",
    "DescribeAssociationExecutionTargetsPaginatePaginationConfigTypeDef",
    "DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsOutputSourceTypeDef",
    "DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsTypeDef",
    "DescribeAssociationExecutionTargetsPaginateResponseTypeDef",
    "DescribeAssociationExecutionsPaginateFiltersTypeDef",
    "DescribeAssociationExecutionsPaginatePaginationConfigTypeDef",
    "DescribeAssociationExecutionsPaginateResponseAssociationExecutionsTypeDef",
    "DescribeAssociationExecutionsPaginateResponseTypeDef",
    "DescribeAutomationExecutionsPaginateFiltersTypeDef",
    "DescribeAutomationExecutionsPaginatePaginationConfigTypeDef",
    "DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListResolvedTargetsTypeDef",
    "DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTargetsTypeDef",
    "DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTypeDef",
    "DescribeAutomationExecutionsPaginateResponseTypeDef",
    "DescribeAutomationStepExecutionsPaginateFiltersTypeDef",
    "DescribeAutomationStepExecutionsPaginatePaginationConfigTypeDef",
    "DescribeAutomationStepExecutionsPaginateResponseStepExecutionsFailureDetailsTypeDef",
    "DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetLocationTypeDef",
    "DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetsTypeDef",
    "DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTypeDef",
    "DescribeAutomationStepExecutionsPaginateResponseTypeDef",
    "DescribeAvailablePatchesPaginateFiltersTypeDef",
    "DescribeAvailablePatchesPaginatePaginationConfigTypeDef",
    "DescribeAvailablePatchesPaginateResponsePatchesTypeDef",
    "DescribeAvailablePatchesPaginateResponseTypeDef",
    "DescribeEffectiveInstanceAssociationsPaginatePaginationConfigTypeDef",
    "DescribeEffectiveInstanceAssociationsPaginateResponseAssociationsTypeDef",
    "DescribeEffectiveInstanceAssociationsPaginateResponseTypeDef",
    "DescribeEffectivePatchesForPatchBaselinePaginatePaginationConfigTypeDef",
    "DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchStatusTypeDef",
    "DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchTypeDef",
    "DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesTypeDef",
    "DescribeEffectivePatchesForPatchBaselinePaginateResponseTypeDef",
    "DescribeInstanceAssociationsStatusPaginatePaginationConfigTypeDef",
    "DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef",
    "DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlTypeDef",
    "DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosTypeDef",
    "DescribeInstanceAssociationsStatusPaginateResponseTypeDef",
    "DescribeInstanceInformationPaginateFiltersTypeDef",
    "DescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef",
    "DescribeInstanceInformationPaginatePaginationConfigTypeDef",
    "DescribeInstanceInformationPaginateResponseInstanceInformationListAssociationOverviewTypeDef",
    "DescribeInstanceInformationPaginateResponseInstanceInformationListTypeDef",
    "DescribeInstanceInformationPaginateResponseTypeDef",
    "DescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef",
    "DescribeInstancePatchStatesForPatchGroupPaginatePaginationConfigTypeDef",
    "DescribeInstancePatchStatesForPatchGroupPaginateResponseInstancePatchStatesTypeDef",
    "DescribeInstancePatchStatesForPatchGroupPaginateResponseTypeDef",
    "DescribeInstancePatchStatesPaginatePaginationConfigTypeDef",
    "DescribeInstancePatchStatesPaginateResponseInstancePatchStatesTypeDef",
    "DescribeInstancePatchStatesPaginateResponseTypeDef",
    "DescribeInstancePatchesPaginateFiltersTypeDef",
    "DescribeInstancePatchesPaginatePaginationConfigTypeDef",
    "DescribeInstancePatchesPaginateResponsePatchesTypeDef",
    "DescribeInstancePatchesPaginateResponseTypeDef",
    "DescribeInventoryDeletionsPaginatePaginationConfigTypeDef",
    "DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef",
    "DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummaryTypeDef",
    "DescribeInventoryDeletionsPaginateResponseInventoryDeletionsTypeDef",
    "DescribeInventoryDeletionsPaginateResponseTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginateFiltersTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginatePaginationConfigTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseWindowExecutionTaskInvocationIdentitiesTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseTypeDef",
    "DescribeMaintenanceWindowExecutionTasksPaginateFiltersTypeDef",
    "DescribeMaintenanceWindowExecutionTasksPaginatePaginationConfigTypeDef",
    "DescribeMaintenanceWindowExecutionTasksPaginateResponseWindowExecutionTaskIdentitiesTypeDef",
    "DescribeMaintenanceWindowExecutionTasksPaginateResponseTypeDef",
    "DescribeMaintenanceWindowExecutionsPaginateFiltersTypeDef",
    "DescribeMaintenanceWindowExecutionsPaginatePaginationConfigTypeDef",
    "DescribeMaintenanceWindowExecutionsPaginateResponseWindowExecutionsTypeDef",
    "DescribeMaintenanceWindowExecutionsPaginateResponseTypeDef",
    "DescribeMaintenanceWindowSchedulePaginateFiltersTypeDef",
    "DescribeMaintenanceWindowSchedulePaginatePaginationConfigTypeDef",
    "DescribeMaintenanceWindowSchedulePaginateResponseScheduledWindowExecutionsTypeDef",
    "DescribeMaintenanceWindowSchedulePaginateResponseTypeDef",
    "DescribeMaintenanceWindowSchedulePaginateTargetsTypeDef",
    "DescribeMaintenanceWindowTargetsPaginateFiltersTypeDef",
    "DescribeMaintenanceWindowTargetsPaginatePaginationConfigTypeDef",
    "DescribeMaintenanceWindowTargetsPaginateResponseTargetsTargetsTypeDef",
    "DescribeMaintenanceWindowTargetsPaginateResponseTargetsTypeDef",
    "DescribeMaintenanceWindowTargetsPaginateResponseTypeDef",
    "DescribeMaintenanceWindowTasksPaginateFiltersTypeDef",
    "DescribeMaintenanceWindowTasksPaginatePaginationConfigTypeDef",
    "DescribeMaintenanceWindowTasksPaginateResponseTasksLoggingInfoTypeDef",
    "DescribeMaintenanceWindowTasksPaginateResponseTasksTargetsTypeDef",
    "DescribeMaintenanceWindowTasksPaginateResponseTasksTaskParametersTypeDef",
    "DescribeMaintenanceWindowTasksPaginateResponseTasksTypeDef",
    "DescribeMaintenanceWindowTasksPaginateResponseTypeDef",
    "DescribeMaintenanceWindowsForTargetPaginatePaginationConfigTypeDef",
    "DescribeMaintenanceWindowsForTargetPaginateResponseWindowIdentitiesTypeDef",
    "DescribeMaintenanceWindowsForTargetPaginateResponseTypeDef",
    "DescribeMaintenanceWindowsForTargetPaginateTargetsTypeDef",
    "DescribeMaintenanceWindowsPaginateFiltersTypeDef",
    "DescribeMaintenanceWindowsPaginatePaginationConfigTypeDef",
    "DescribeMaintenanceWindowsPaginateResponseWindowIdentitiesTypeDef",
    "DescribeMaintenanceWindowsPaginateResponseTypeDef",
    "DescribeParametersPaginateFiltersTypeDef",
    "DescribeParametersPaginatePaginationConfigTypeDef",
    "DescribeParametersPaginateParameterFiltersTypeDef",
    "DescribeParametersPaginateResponseParametersPoliciesTypeDef",
    "DescribeParametersPaginateResponseParametersTypeDef",
    "DescribeParametersPaginateResponseTypeDef",
    "DescribePatchBaselinesPaginateFiltersTypeDef",
    "DescribePatchBaselinesPaginatePaginationConfigTypeDef",
    "DescribePatchBaselinesPaginateResponseBaselineIdentitiesTypeDef",
    "DescribePatchBaselinesPaginateResponseTypeDef",
    "DescribePatchGroupsPaginateFiltersTypeDef",
    "DescribePatchGroupsPaginatePaginationConfigTypeDef",
    "DescribePatchGroupsPaginateResponseMappingsBaselineIdentityTypeDef",
    "DescribePatchGroupsPaginateResponseMappingsTypeDef",
    "DescribePatchGroupsPaginateResponseTypeDef",
    "DescribeSessionsPaginateFiltersTypeDef",
    "DescribeSessionsPaginatePaginationConfigTypeDef",
    "DescribeSessionsPaginateResponseSessionsOutputUrlTypeDef",
    "DescribeSessionsPaginateResponseSessionsTypeDef",
    "DescribeSessionsPaginateResponseTypeDef",
    "GetInventoryPaginateAggregatorsGroupsFiltersTypeDef",
    "GetInventoryPaginateAggregatorsGroupsTypeDef",
    "GetInventoryPaginateAggregatorsTypeDef",
    "GetInventoryPaginateFiltersTypeDef",
    "GetInventoryPaginatePaginationConfigTypeDef",
    "GetInventoryPaginateResponseEntitiesDataTypeDef",
    "GetInventoryPaginateResponseEntitiesTypeDef",
    "GetInventoryPaginateResponseTypeDef",
    "GetInventoryPaginateResultAttributesTypeDef",
    "GetInventorySchemaPaginatePaginationConfigTypeDef",
    "GetInventorySchemaPaginateResponseSchemasAttributesTypeDef",
    "GetInventorySchemaPaginateResponseSchemasTypeDef",
    "GetInventorySchemaPaginateResponseTypeDef",
    "GetParameterHistoryPaginatePaginationConfigTypeDef",
    "GetParameterHistoryPaginateResponseParametersPoliciesTypeDef",
    "GetParameterHistoryPaginateResponseParametersTypeDef",
    "GetParameterHistoryPaginateResponseTypeDef",
    "GetParametersByPathPaginatePaginationConfigTypeDef",
    "GetParametersByPathPaginateParameterFiltersTypeDef",
    "GetParametersByPathPaginateResponseParametersTypeDef",
    "GetParametersByPathPaginateResponseTypeDef",
    "ListAssociationVersionsPaginatePaginationConfigTypeDef",
    "ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationS3LocationTypeDef",
    "ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationTypeDef",
    "ListAssociationVersionsPaginateResponseAssociationVersionsTargetsTypeDef",
    "ListAssociationVersionsPaginateResponseAssociationVersionsTypeDef",
    "ListAssociationVersionsPaginateResponseTypeDef",
    "ListAssociationsPaginateAssociationFilterListTypeDef",
    "ListAssociationsPaginatePaginationConfigTypeDef",
    "ListAssociationsPaginateResponseAssociationsOverviewTypeDef",
    "ListAssociationsPaginateResponseAssociationsTargetsTypeDef",
    "ListAssociationsPaginateResponseAssociationsTypeDef",
    "ListAssociationsPaginateResponseTypeDef",
    "ListCommandInvocationsPaginateFiltersTypeDef",
    "ListCommandInvocationsPaginatePaginationConfigTypeDef",
    "ListCommandInvocationsPaginateResponseCommandInvocationsCloudWatchOutputConfigTypeDef",
    "ListCommandInvocationsPaginateResponseCommandInvocationsCommandPluginsTypeDef",
    "ListCommandInvocationsPaginateResponseCommandInvocationsNotificationConfigTypeDef",
    "ListCommandInvocationsPaginateResponseCommandInvocationsTypeDef",
    "ListCommandInvocationsPaginateResponseTypeDef",
    "ListCommandsPaginateFiltersTypeDef",
    "ListCommandsPaginatePaginationConfigTypeDef",
    "ListCommandsPaginateResponseCommandsCloudWatchOutputConfigTypeDef",
    "ListCommandsPaginateResponseCommandsNotificationConfigTypeDef",
    "ListCommandsPaginateResponseCommandsTargetsTypeDef",
    "ListCommandsPaginateResponseCommandsTypeDef",
    "ListCommandsPaginateResponseTypeDef",
    "ListComplianceItemsPaginateFiltersTypeDef",
    "ListComplianceItemsPaginatePaginationConfigTypeDef",
    "ListComplianceItemsPaginateResponseComplianceItemsExecutionSummaryTypeDef",
    "ListComplianceItemsPaginateResponseComplianceItemsTypeDef",
    "ListComplianceItemsPaginateResponseTypeDef",
    "ListComplianceSummariesPaginateFiltersTypeDef",
    "ListComplianceSummariesPaginatePaginationConfigTypeDef",
    "ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    "ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummaryTypeDef",
    "ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    "ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummaryTypeDef",
    "ListComplianceSummariesPaginateResponseComplianceSummaryItemsTypeDef",
    "ListComplianceSummariesPaginateResponseTypeDef",
    "ListDocumentVersionsPaginatePaginationConfigTypeDef",
    "ListDocumentVersionsPaginateResponseDocumentVersionsTypeDef",
    "ListDocumentVersionsPaginateResponseTypeDef",
    "ListDocumentsPaginateDocumentFilterListTypeDef",
    "ListDocumentsPaginateFiltersTypeDef",
    "ListDocumentsPaginatePaginationConfigTypeDef",
    "ListDocumentsPaginateResponseDocumentIdentifiersRequiresTypeDef",
    "ListDocumentsPaginateResponseDocumentIdentifiersTagsTypeDef",
    "ListDocumentsPaginateResponseDocumentIdentifiersTypeDef",
    "ListDocumentsPaginateResponseTypeDef",
    "ListResourceComplianceSummariesPaginateFiltersTypeDef",
    "ListResourceComplianceSummariesPaginatePaginationConfigTypeDef",
    "ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    "ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef",
    "ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef",
    "ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    "ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef",
    "ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsTypeDef",
    "ListResourceComplianceSummariesPaginateResponseTypeDef",
    "ListResourceDataSyncPaginatePaginationConfigTypeDef",
    "ListResourceDataSyncPaginateResponseResourceDataSyncItemsS3DestinationTypeDef",
    "ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    "ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef",
    "ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceTypeDef",
    "ListResourceDataSyncPaginateResponseResourceDataSyncItemsTypeDef",
    "ListResourceDataSyncPaginateResponseTypeDef",
)


_ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsToResourceTagsTypeDef(_ClientAddTagsToResourceTagsTypeDef):
    pass


_ClientCancelMaintenanceWindowExecutionResponseTypeDef = TypedDict(
    "_ClientCancelMaintenanceWindowExecutionResponseTypeDef",
    {"WindowExecutionId": str},
    total=False,
)


class ClientCancelMaintenanceWindowExecutionResponseTypeDef(
    _ClientCancelMaintenanceWindowExecutionResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowExecutionId** *(string) --*

        The ID of the maintenance window execution that has been stopped.
    """


_ClientCreateActivationResponseTypeDef = TypedDict(
    "_ClientCreateActivationResponseTypeDef",
    {"ActivationId": str, "ActivationCode": str},
    total=False,
)


class ClientCreateActivationResponseTypeDef(_ClientCreateActivationResponseTypeDef):
    """
    - *(dict) --*

      - **ActivationId** *(string) --*

        The ID number generated by the system when it processed the activation. The activation ID
        functions like a user name.
    """


_ClientCreateActivationTagsTypeDef = TypedDict(
    "_ClientCreateActivationTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateActivationTagsTypeDef(_ClientCreateActivationTagsTypeDef):
    pass


_ClientCreateAssociationBatchEntriesOutputLocationS3LocationTypeDef = TypedDict(
    "_ClientCreateAssociationBatchEntriesOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)


class ClientCreateAssociationBatchEntriesOutputLocationS3LocationTypeDef(
    _ClientCreateAssociationBatchEntriesOutputLocationS3LocationTypeDef
):
    pass


_ClientCreateAssociationBatchEntriesOutputLocationTypeDef = TypedDict(
    "_ClientCreateAssociationBatchEntriesOutputLocationTypeDef",
    {"S3Location": ClientCreateAssociationBatchEntriesOutputLocationS3LocationTypeDef},
    total=False,
)


class ClientCreateAssociationBatchEntriesOutputLocationTypeDef(
    _ClientCreateAssociationBatchEntriesOutputLocationTypeDef
):
    pass


_ClientCreateAssociationBatchEntriesTargetsTypeDef = TypedDict(
    "_ClientCreateAssociationBatchEntriesTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateAssociationBatchEntriesTargetsTypeDef(
    _ClientCreateAssociationBatchEntriesTargetsTypeDef
):
    pass


_RequiredClientCreateAssociationBatchEntriesTypeDef = TypedDict(
    "_RequiredClientCreateAssociationBatchEntriesTypeDef", {"Name": str}
)
_OptionalClientCreateAssociationBatchEntriesTypeDef = TypedDict(
    "_OptionalClientCreateAssociationBatchEntriesTypeDef",
    {
        "InstanceId": str,
        "Parameters": Dict[str, List[str]],
        "AutomationTargetParameterName": str,
        "DocumentVersion": str,
        "Targets": List[ClientCreateAssociationBatchEntriesTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientCreateAssociationBatchEntriesOutputLocationTypeDef,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)


class ClientCreateAssociationBatchEntriesTypeDef(
    _RequiredClientCreateAssociationBatchEntriesTypeDef,
    _OptionalClientCreateAssociationBatchEntriesTypeDef,
):
    """
    - *(dict) --*

      Describes the association of a Systems Manager SSM document and an instance.
      - **Name** *(string) --***[REQUIRED]**

        The name of the SSM document that contains the configuration information for the instance.
        You can specify Command or Automation documents.
        You can specify AWS-predefined documents, documents you created, or a document that is
        shared with you from another account.
        For SSM documents that are shared with you from other AWS accounts, you must specify the
        complete SSM document ARN, in the following format:

          ``arn:aws:ssm:*region* :*account-id* :document/*document-name* ``
    """


_ClientCreateAssociationBatchResponseFailedEntryOutputLocationS3LocationTypeDef = TypedDict(
    "_ClientCreateAssociationBatchResponseFailedEntryOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)


class ClientCreateAssociationBatchResponseFailedEntryOutputLocationS3LocationTypeDef(
    _ClientCreateAssociationBatchResponseFailedEntryOutputLocationS3LocationTypeDef
):
    pass


_ClientCreateAssociationBatchResponseFailedEntryOutputLocationTypeDef = TypedDict(
    "_ClientCreateAssociationBatchResponseFailedEntryOutputLocationTypeDef",
    {"S3Location": ClientCreateAssociationBatchResponseFailedEntryOutputLocationS3LocationTypeDef},
    total=False,
)


class ClientCreateAssociationBatchResponseFailedEntryOutputLocationTypeDef(
    _ClientCreateAssociationBatchResponseFailedEntryOutputLocationTypeDef
):
    pass


_ClientCreateAssociationBatchResponseFailedEntryTargetsTypeDef = TypedDict(
    "_ClientCreateAssociationBatchResponseFailedEntryTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateAssociationBatchResponseFailedEntryTargetsTypeDef(
    _ClientCreateAssociationBatchResponseFailedEntryTargetsTypeDef
):
    pass


_ClientCreateAssociationBatchResponseFailedEntryTypeDef = TypedDict(
    "_ClientCreateAssociationBatchResponseFailedEntryTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "Parameters": Dict[str, List[str]],
        "AutomationTargetParameterName": str,
        "DocumentVersion": str,
        "Targets": List[ClientCreateAssociationBatchResponseFailedEntryTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientCreateAssociationBatchResponseFailedEntryOutputLocationTypeDef,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)


class ClientCreateAssociationBatchResponseFailedEntryTypeDef(
    _ClientCreateAssociationBatchResponseFailedEntryTypeDef
):
    pass


_ClientCreateAssociationBatchResponseFailedTypeDef = TypedDict(
    "_ClientCreateAssociationBatchResponseFailedTypeDef",
    {
        "Entry": ClientCreateAssociationBatchResponseFailedEntryTypeDef,
        "Message": str,
        "Fault": Literal["Client", "Server", "Unknown"],
    },
    total=False,
)


class ClientCreateAssociationBatchResponseFailedTypeDef(
    _ClientCreateAssociationBatchResponseFailedTypeDef
):
    pass


_ClientCreateAssociationBatchResponseSuccessfulOutputLocationS3LocationTypeDef = TypedDict(
    "_ClientCreateAssociationBatchResponseSuccessfulOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)


class ClientCreateAssociationBatchResponseSuccessfulOutputLocationS3LocationTypeDef(
    _ClientCreateAssociationBatchResponseSuccessfulOutputLocationS3LocationTypeDef
):
    pass


_ClientCreateAssociationBatchResponseSuccessfulOutputLocationTypeDef = TypedDict(
    "_ClientCreateAssociationBatchResponseSuccessfulOutputLocationTypeDef",
    {"S3Location": ClientCreateAssociationBatchResponseSuccessfulOutputLocationS3LocationTypeDef},
    total=False,
)


class ClientCreateAssociationBatchResponseSuccessfulOutputLocationTypeDef(
    _ClientCreateAssociationBatchResponseSuccessfulOutputLocationTypeDef
):
    pass


_ClientCreateAssociationBatchResponseSuccessfulOverviewTypeDef = TypedDict(
    "_ClientCreateAssociationBatchResponseSuccessfulOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)


class ClientCreateAssociationBatchResponseSuccessfulOverviewTypeDef(
    _ClientCreateAssociationBatchResponseSuccessfulOverviewTypeDef
):
    pass


_ClientCreateAssociationBatchResponseSuccessfulStatusTypeDef = TypedDict(
    "_ClientCreateAssociationBatchResponseSuccessfulStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)


class ClientCreateAssociationBatchResponseSuccessfulStatusTypeDef(
    _ClientCreateAssociationBatchResponseSuccessfulStatusTypeDef
):
    pass


_ClientCreateAssociationBatchResponseSuccessfulTargetsTypeDef = TypedDict(
    "_ClientCreateAssociationBatchResponseSuccessfulTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateAssociationBatchResponseSuccessfulTargetsTypeDef(
    _ClientCreateAssociationBatchResponseSuccessfulTargetsTypeDef
):
    pass


_ClientCreateAssociationBatchResponseSuccessfulTypeDef = TypedDict(
    "_ClientCreateAssociationBatchResponseSuccessfulTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientCreateAssociationBatchResponseSuccessfulStatusTypeDef,
        "Overview": ClientCreateAssociationBatchResponseSuccessfulOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientCreateAssociationBatchResponseSuccessfulTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientCreateAssociationBatchResponseSuccessfulOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)


class ClientCreateAssociationBatchResponseSuccessfulTypeDef(
    _ClientCreateAssociationBatchResponseSuccessfulTypeDef
):
    """
    - *(dict) --*

      Describes the parameters for a document.
      - **Name** *(string) --*

        The name of the Systems Manager document.
    """


_ClientCreateAssociationBatchResponseTypeDef = TypedDict(
    "_ClientCreateAssociationBatchResponseTypeDef",
    {
        "Successful": List[ClientCreateAssociationBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientCreateAssociationBatchResponseFailedTypeDef],
    },
    total=False,
)


class ClientCreateAssociationBatchResponseTypeDef(_ClientCreateAssociationBatchResponseTypeDef):
    """
    - *(dict) --*

      - **Successful** *(list) --*

        Information about the associations that succeeded.
        - *(dict) --*

          Describes the parameters for a document.
          - **Name** *(string) --*

            The name of the Systems Manager document.
    """


_ClientCreateAssociationOutputLocationS3LocationTypeDef = TypedDict(
    "_ClientCreateAssociationOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)


class ClientCreateAssociationOutputLocationS3LocationTypeDef(
    _ClientCreateAssociationOutputLocationS3LocationTypeDef
):
    """
    - **S3Location** *(dict) --*

      An Amazon S3 bucket where you want to store the results of this request.
      - **OutputS3Region** *(string) --*

        (Deprecated) You can no longer specify this parameter. The system ignores it. Instead,
        Systems Manager automatically determines the Amazon S3 bucket region.
    """


_ClientCreateAssociationOutputLocationTypeDef = TypedDict(
    "_ClientCreateAssociationOutputLocationTypeDef",
    {"S3Location": ClientCreateAssociationOutputLocationS3LocationTypeDef},
    total=False,
)


class ClientCreateAssociationOutputLocationTypeDef(_ClientCreateAssociationOutputLocationTypeDef):
    """
    An Amazon S3 bucket where you want to store the output details of the request.
    - **S3Location** *(dict) --*

      An Amazon S3 bucket where you want to store the results of this request.
      - **OutputS3Region** *(string) --*

        (Deprecated) You can no longer specify this parameter. The system ignores it. Instead,
        Systems Manager automatically determines the Amazon S3 bucket region.
    """


_ClientCreateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef = TypedDict(
    "_ClientCreateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)


class ClientCreateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef(
    _ClientCreateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef
):
    pass


_ClientCreateAssociationResponseAssociationDescriptionOutputLocationTypeDef = TypedDict(
    "_ClientCreateAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    {
        "S3Location": ClientCreateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef
    },
    total=False,
)


class ClientCreateAssociationResponseAssociationDescriptionOutputLocationTypeDef(
    _ClientCreateAssociationResponseAssociationDescriptionOutputLocationTypeDef
):
    pass


_ClientCreateAssociationResponseAssociationDescriptionOverviewTypeDef = TypedDict(
    "_ClientCreateAssociationResponseAssociationDescriptionOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)


class ClientCreateAssociationResponseAssociationDescriptionOverviewTypeDef(
    _ClientCreateAssociationResponseAssociationDescriptionOverviewTypeDef
):
    pass


_ClientCreateAssociationResponseAssociationDescriptionStatusTypeDef = TypedDict(
    "_ClientCreateAssociationResponseAssociationDescriptionStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)


class ClientCreateAssociationResponseAssociationDescriptionStatusTypeDef(
    _ClientCreateAssociationResponseAssociationDescriptionStatusTypeDef
):
    pass


_ClientCreateAssociationResponseAssociationDescriptionTargetsTypeDef = TypedDict(
    "_ClientCreateAssociationResponseAssociationDescriptionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateAssociationResponseAssociationDescriptionTargetsTypeDef(
    _ClientCreateAssociationResponseAssociationDescriptionTargetsTypeDef
):
    pass


_ClientCreateAssociationResponseAssociationDescriptionTypeDef = TypedDict(
    "_ClientCreateAssociationResponseAssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientCreateAssociationResponseAssociationDescriptionStatusTypeDef,
        "Overview": ClientCreateAssociationResponseAssociationDescriptionOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientCreateAssociationResponseAssociationDescriptionTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientCreateAssociationResponseAssociationDescriptionOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)


class ClientCreateAssociationResponseAssociationDescriptionTypeDef(
    _ClientCreateAssociationResponseAssociationDescriptionTypeDef
):
    """
    - **AssociationDescription** *(dict) --*

      Information about the association.
      - **Name** *(string) --*

        The name of the Systems Manager document.
    """


_ClientCreateAssociationResponseTypeDef = TypedDict(
    "_ClientCreateAssociationResponseTypeDef",
    {"AssociationDescription": ClientCreateAssociationResponseAssociationDescriptionTypeDef},
    total=False,
)


class ClientCreateAssociationResponseTypeDef(_ClientCreateAssociationResponseTypeDef):
    """
    - *(dict) --*

      - **AssociationDescription** *(dict) --*

        Information about the association.
        - **Name** *(string) --*

          The name of the Systems Manager document.
    """


_ClientCreateAssociationTargetsTypeDef = TypedDict(
    "_ClientCreateAssociationTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientCreateAssociationTargetsTypeDef(_ClientCreateAssociationTargetsTypeDef):
    """
    - *(dict) --*

      An array of search criteria that targets instances using a Key,Value combination that you
      specify.
      Supported formats include the following.
      * ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
      * ``Key=tag:*my-tag-key* ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
      * ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
      * (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
      For example:
      * ``Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE``
      * ``Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3``
      * ``Key=tag-key,Values=Name,Instance-Type,CostCenter``
      * (Maintenance window targets only)
      ``Key=resource-groups:Name,Values=
          ProductionResourceGroup``   This example demonstrates how to
      target all resources in the resource group **ProductionResourceGroup** in your maintenance
      window.
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``
      This example demonstrates how to target only Amazon EC2 instances and VPCs in your maintenance
      window.
      * (State Manager association targets only) ``Key=InstanceIds,Values=*``   This example
      demonstrates how to target all managed instances in the AWS Region where the association was
      created.
      For information about how to send commands that target instances using ``Key,Value``
      parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet
      <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__
      in the *AWS Systems Manager User Guide* .
      - **Key** *(string) --*

        User-defined criteria for sending commands that target instances that meet the criteria.
    """


_ClientCreateDocumentAttachmentsTypeDef = TypedDict(
    "_ClientCreateDocumentAttachmentsTypeDef",
    {"Key": Literal["SourceUrl", "S3FileUrl"], "Values": List[str], "Name": str},
    total=False,
)


class ClientCreateDocumentAttachmentsTypeDef(_ClientCreateDocumentAttachmentsTypeDef):
    """
    - *(dict) --*

      Identifying information about a document attachment, including the file name and a key-value
      pair that identifies the location of an attachment to a document.
      - **Key** *(string) --*

        The key of a key-value pair that identifies the location of an attachment to a document.
    """


_RequiredClientCreateDocumentRequiresTypeDef = TypedDict(
    "_RequiredClientCreateDocumentRequiresTypeDef", {"Name": str}
)
_OptionalClientCreateDocumentRequiresTypeDef = TypedDict(
    "_OptionalClientCreateDocumentRequiresTypeDef", {"Version": str}, total=False
)


class ClientCreateDocumentRequiresTypeDef(
    _RequiredClientCreateDocumentRequiresTypeDef, _OptionalClientCreateDocumentRequiresTypeDef
):
    """
    - *(dict) --*

      An SSM document required by the current document.
      - **Name** *(string) --***[REQUIRED]**

        The name of the required SSM document. The name can be an Amazon Resource Name (ARN).
    """


_ClientCreateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef = TypedDict(
    "_ClientCreateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef(
    _ClientCreateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef
):
    pass


_ClientCreateDocumentResponseDocumentDescriptionParametersTypeDef = TypedDict(
    "_ClientCreateDocumentResponseDocumentDescriptionParametersTypeDef",
    {"Name": str, "Type": Literal["String", "StringList"], "Description": str, "DefaultValue": str},
    total=False,
)


class ClientCreateDocumentResponseDocumentDescriptionParametersTypeDef(
    _ClientCreateDocumentResponseDocumentDescriptionParametersTypeDef
):
    pass


_ClientCreateDocumentResponseDocumentDescriptionRequiresTypeDef = TypedDict(
    "_ClientCreateDocumentResponseDocumentDescriptionRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientCreateDocumentResponseDocumentDescriptionRequiresTypeDef(
    _ClientCreateDocumentResponseDocumentDescriptionRequiresTypeDef
):
    pass


_ClientCreateDocumentResponseDocumentDescriptionTagsTypeDef = TypedDict(
    "_ClientCreateDocumentResponseDocumentDescriptionTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateDocumentResponseDocumentDescriptionTagsTypeDef(
    _ClientCreateDocumentResponseDocumentDescriptionTagsTypeDef
):
    pass


_ClientCreateDocumentResponseDocumentDescriptionTypeDef = TypedDict(
    "_ClientCreateDocumentResponseDocumentDescriptionTypeDef",
    {
        "Sha1": str,
        "Hash": str,
        "HashType": Literal["Sha256", "Sha1"],
        "Name": str,
        "VersionName": str,
        "Owner": str,
        "CreatedDate": datetime,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "DocumentVersion": str,
        "Description": str,
        "Parameters": List[ClientCreateDocumentResponseDocumentDescriptionParametersTypeDef],
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
        ],
        "SchemaVersion": str,
        "LatestVersion": str,
        "DefaultVersion": str,
        "DocumentFormat": Literal["YAML", "JSON"],
        "TargetType": str,
        "Tags": List[ClientCreateDocumentResponseDocumentDescriptionTagsTypeDef],
        "AttachmentsInformation": List[
            ClientCreateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef
        ],
        "Requires": List[ClientCreateDocumentResponseDocumentDescriptionRequiresTypeDef],
    },
    total=False,
)


class ClientCreateDocumentResponseDocumentDescriptionTypeDef(
    _ClientCreateDocumentResponseDocumentDescriptionTypeDef
):
    """
    - **DocumentDescription** *(dict) --*

      Information about the Systems Manager document.
      - **Sha1** *(string) --*

        The SHA1 hash of the document, which you can use for verification.
    """


_ClientCreateDocumentResponseTypeDef = TypedDict(
    "_ClientCreateDocumentResponseTypeDef",
    {"DocumentDescription": ClientCreateDocumentResponseDocumentDescriptionTypeDef},
    total=False,
)


class ClientCreateDocumentResponseTypeDef(_ClientCreateDocumentResponseTypeDef):
    """
    - *(dict) --*

      - **DocumentDescription** *(dict) --*

        Information about the Systems Manager document.
        - **Sha1** *(string) --*

          The SHA1 hash of the document, which you can use for verification.
    """


_ClientCreateDocumentTagsTypeDef = TypedDict(
    "_ClientCreateDocumentTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDocumentTagsTypeDef(_ClientCreateDocumentTagsTypeDef):
    pass


_ClientCreateMaintenanceWindowResponseTypeDef = TypedDict(
    "_ClientCreateMaintenanceWindowResponseTypeDef", {"WindowId": str}, total=False
)


class ClientCreateMaintenanceWindowResponseTypeDef(_ClientCreateMaintenanceWindowResponseTypeDef):
    """
    - *(dict) --*

      - **WindowId** *(string) --*

        The ID of the created maintenance window.
    """


_ClientCreateMaintenanceWindowTagsTypeDef = TypedDict(
    "_ClientCreateMaintenanceWindowTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateMaintenanceWindowTagsTypeDef(_ClientCreateMaintenanceWindowTagsTypeDef):
    pass


_ClientCreateOpsItemNotificationsTypeDef = TypedDict(
    "_ClientCreateOpsItemNotificationsTypeDef", {"Arn": str}, total=False
)


class ClientCreateOpsItemNotificationsTypeDef(_ClientCreateOpsItemNotificationsTypeDef):
    """
    - *(dict) --*

      A notification about the OpsItem.
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this
        OpsItem is edited or changed.
    """


_ClientCreateOpsItemOperationalDataTypeDef = TypedDict(
    "_ClientCreateOpsItemOperationalDataTypeDef",
    {"Value": str, "Type": Literal["SearchableString", "String"]},
    total=False,
)


class ClientCreateOpsItemOperationalDataTypeDef(_ClientCreateOpsItemOperationalDataTypeDef):
    pass


_ClientCreateOpsItemRelatedOpsItemsTypeDef = TypedDict(
    "_ClientCreateOpsItemRelatedOpsItemsTypeDef", {"OpsItemId": str}
)


class ClientCreateOpsItemRelatedOpsItemsTypeDef(_ClientCreateOpsItemRelatedOpsItemsTypeDef):
    """
    - *(dict) --*

      An OpsItems that shares something in common with the current OpsItem. For example, related
      OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for
      the impacted resource.
      - **OpsItemId** *(string) --***[REQUIRED]**

        The ID of an OpsItem related to the current OpsItem.
    """


_ClientCreateOpsItemResponseTypeDef = TypedDict(
    "_ClientCreateOpsItemResponseTypeDef", {"OpsItemId": str}, total=False
)


class ClientCreateOpsItemResponseTypeDef(_ClientCreateOpsItemResponseTypeDef):
    """
    - *(dict) --*

      - **OpsItemId** *(string) --*

        The ID of the OpsItem.
    """


_ClientCreateOpsItemTagsTypeDef = TypedDict(
    "_ClientCreateOpsItemTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateOpsItemTagsTypeDef(_ClientCreateOpsItemTagsTypeDef):
    pass


_RequiredClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_RequiredClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ]
    },
)
_OptionalClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_OptionalClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef(
    _RequiredClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef,
    _OptionalClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef,
):
    """
    - *(dict) --*

      Defines which patches should be included in a patch baseline.
      A patch filter consists of a key and a set of values. The filter key is a patch property. For
      example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY,
      CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the patch
      property indicated by the key. For example, if the filter key is PRODUCT and the filter values
      are ["Office 2013", "Office 2016"], then the filter accepts all patches where product name is
      either "Office 2013" or "Office 2016". The filter values can be exact values for the patch
      property given as a key, or a wildcard (*), which matches all values.
      You can view lists of valid values for the patch properties by running the
      ``DescribePatchProperties`` command. For information about which patch properties can be used
      with each major operating system, see  DescribePatchProperties .
      - **Key** *(string) --***[REQUIRED]**

        The key for the filter.
        Run the  DescribePatchProperties command to view lists of valid keys for each operating
        system type.
    """


_ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef = TypedDict(
    "_ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    {
        "PatchFilters": List[
            ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
        ]
    },
)


class ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef(
    _ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef
):
    """
    - **PatchFilterGroup** *(dict) --***[REQUIRED]**

      The patch filter group that defines the criteria for the rule.
      - **PatchFilters** *(list) --***[REQUIRED]**

        The set of patch filters that make up the group.
        - *(dict) --*

          Defines which patches should be included in a patch baseline.
          A patch filter consists of a key and a set of values. The filter key is a patch property.
          For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY,
          CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the
          patch property indicated by the key. For example, if the filter key is PRODUCT and the
          filter values are ["Office 2013", "Office 2016"], then the filter accepts all patches
          where product name is either "Office 2013" or "Office 2016". The filter values can be
          exact values for the patch property given as a key, or a wildcard (*), which matches all
          values.
          You can view lists of valid values for the patch properties by running the
          ``DescribePatchProperties`` command. For information about which patch properties can be
          used with each major operating system, see  DescribePatchProperties .
          - **Key** *(string) --***[REQUIRED]**

            The key for the filter.
            Run the  DescribePatchProperties command to view lists of valid keys for each operating
            system type.
    """


_RequiredClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef = TypedDict(
    "_RequiredClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef",
    {"PatchFilterGroup": ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef},
)
_OptionalClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef = TypedDict(
    "_OptionalClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef",
    {
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApproveAfterDays": int,
        "EnableNonSecurity": bool,
    },
    total=False,
)


class ClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef(
    _RequiredClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef,
    _OptionalClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef,
):
    """
    - *(dict) --*

      Defines an approval rule for a patch baseline.
      - **PatchFilterGroup** *(dict) --***[REQUIRED]**

        The patch filter group that defines the criteria for the rule.
        - **PatchFilters** *(list) --***[REQUIRED]**

          The set of patch filters that make up the group.
          - *(dict) --*

            Defines which patches should be included in a patch baseline.
            A patch filter consists of a key and a set of values. The filter key is a patch
            property. For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT,
            PRODUCT_FAMILY, CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching
            criterion for the patch property indicated by the key. For example, if the filter key is
            PRODUCT and the filter values are ["Office 2013", "Office 2016"], then the filter
            accepts all patches where product name is either "Office 2013" or "Office 2016". The
            filter values can be exact values for the patch property given as a key, or a wildcard
            (*), which matches all values.
            You can view lists of valid values for the patch properties by running the
            ``DescribePatchProperties`` command. For information about which patch properties can be
            used with each major operating system, see  DescribePatchProperties .
            - **Key** *(string) --***[REQUIRED]**

              The key for the filter.
              Run the  DescribePatchProperties command to view lists of valid keys for each
              operating system type.
    """


_ClientCreatePatchBaselineApprovalRulesTypeDef = TypedDict(
    "_ClientCreatePatchBaselineApprovalRulesTypeDef",
    {"PatchRules": List[ClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef]},
)


class ClientCreatePatchBaselineApprovalRulesTypeDef(_ClientCreatePatchBaselineApprovalRulesTypeDef):
    """
    A set of rules used to include patches in the baseline.
    - **PatchRules** *(list) --***[REQUIRED]**

      The rules that make up the rule group.
      - *(dict) --*

        Defines an approval rule for a patch baseline.
        - **PatchFilterGroup** *(dict) --***[REQUIRED]**

          The patch filter group that defines the criteria for the rule.
          - **PatchFilters** *(list) --***[REQUIRED]**

            The set of patch filters that make up the group.
            - *(dict) --*

              Defines which patches should be included in a patch baseline.
              A patch filter consists of a key and a set of values. The filter key is a patch
              property. For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT,
              PRODUCT_FAMILY, CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching
              criterion for the patch property indicated by the key. For example, if the filter key
              is PRODUCT and the filter values are ["Office 2013", "Office 2016"], then the filter
              accepts all patches where product name is either "Office 2013" or "Office 2016". The
              filter values can be exact values for the patch property given as a key, or a wildcard
              (*), which matches all values.
              You can view lists of valid values for the patch properties by running the
              ``DescribePatchProperties`` command. For information about which patch properties can
              be used with each major operating system, see  DescribePatchProperties .
              - **Key** *(string) --***[REQUIRED]**

                The key for the filter.
                Run the  DescribePatchProperties command to view lists of valid keys for each
                operating system type.
    """


_RequiredClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_RequiredClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ]
    },
)
_OptionalClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_OptionalClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef(
    _RequiredClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef,
    _OptionalClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef,
):
    """
    - *(dict) --*

      Defines which patches should be included in a patch baseline.
      A patch filter consists of a key and a set of values. The filter key is a patch property. For
      example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY,
      CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the patch
      property indicated by the key. For example, if the filter key is PRODUCT and the filter values
      are ["Office 2013", "Office 2016"], then the filter accepts all patches where product name is
      either "Office 2013" or "Office 2016". The filter values can be exact values for the patch
      property given as a key, or a wildcard (*), which matches all values.
      You can view lists of valid values for the patch properties by running the
      ``DescribePatchProperties`` command. For information about which patch properties can be used
      with each major operating system, see  DescribePatchProperties .
      - **Key** *(string) --***[REQUIRED]**

        The key for the filter.
        Run the  DescribePatchProperties command to view lists of valid keys for each operating
        system type.
    """


_ClientCreatePatchBaselineGlobalFiltersTypeDef = TypedDict(
    "_ClientCreatePatchBaselineGlobalFiltersTypeDef",
    {"PatchFilters": List[ClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef]},
)


class ClientCreatePatchBaselineGlobalFiltersTypeDef(_ClientCreatePatchBaselineGlobalFiltersTypeDef):
    """
    A set of global filters used to include patches in the baseline.
    - **PatchFilters** *(list) --***[REQUIRED]**

      The set of patch filters that make up the group.
      - *(dict) --*

        Defines which patches should be included in a patch baseline.
        A patch filter consists of a key and a set of values. The filter key is a patch property.
        For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY,
        CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the
        patch property indicated by the key. For example, if the filter key is PRODUCT and the
        filter values are ["Office 2013", "Office 2016"], then the filter accepts all patches where
        product name is either "Office 2013" or "Office 2016". The filter values can be exact values
        for the patch property given as a key, or a wildcard (*), which matches all values.
        You can view lists of valid values for the patch properties by running the
        ``DescribePatchProperties`` command. For information about which patch properties can be
        used with each major operating system, see  DescribePatchProperties .
        - **Key** *(string) --***[REQUIRED]**

          The key for the filter.
          Run the  DescribePatchProperties command to view lists of valid keys for each operating
          system type.
    """


_ClientCreatePatchBaselineResponseTypeDef = TypedDict(
    "_ClientCreatePatchBaselineResponseTypeDef", {"BaselineId": str}, total=False
)


class ClientCreatePatchBaselineResponseTypeDef(_ClientCreatePatchBaselineResponseTypeDef):
    """
    - *(dict) --*

      - **BaselineId** *(string) --*

        The ID of the created patch baseline.
    """


_RequiredClientCreatePatchBaselineSourcesTypeDef = TypedDict(
    "_RequiredClientCreatePatchBaselineSourcesTypeDef", {"Name": str}
)
_OptionalClientCreatePatchBaselineSourcesTypeDef = TypedDict(
    "_OptionalClientCreatePatchBaselineSourcesTypeDef",
    {"Products": List[str], "Configuration": str},
    total=False,
)


class ClientCreatePatchBaselineSourcesTypeDef(
    _RequiredClientCreatePatchBaselineSourcesTypeDef,
    _OptionalClientCreatePatchBaselineSourcesTypeDef,
):
    """
    - *(dict) --*

      Information about the patches to use to update the instances, including target operating
      systems and source repository. Applies to Linux instances only.
      - **Name** *(string) --***[REQUIRED]**

        The name specified to identify the patch source.
    """


_ClientCreatePatchBaselineTagsTypeDef = TypedDict(
    "_ClientCreatePatchBaselineTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreatePatchBaselineTagsTypeDef(_ClientCreatePatchBaselineTagsTypeDef):
    pass


_RequiredClientCreateResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_RequiredClientCreateResourceDataSyncS3DestinationTypeDef", {"BucketName": str}
)
_OptionalClientCreateResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_OptionalClientCreateResourceDataSyncS3DestinationTypeDef",
    {"Prefix": str, "SyncFormat": str, "Region": str, "AWSKMSKeyARN": str},
    total=False,
)


class ClientCreateResourceDataSyncS3DestinationTypeDef(
    _RequiredClientCreateResourceDataSyncS3DestinationTypeDef,
    _OptionalClientCreateResourceDataSyncS3DestinationTypeDef,
):
    """
    Amazon S3 configuration details for the sync.
    - **BucketName** *(string) --***[REQUIRED]**

      The name of the Amazon S3 bucket where the aggregated data is stored.
    """


_ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef = TypedDict(
    "_ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    {"OrganizationalUnitId": str},
    total=False,
)


class ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef(
    _ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
):
    pass


_ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef = TypedDict(
    "_ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": List[
            ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
        ],
    },
    total=False,
)


class ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef(
    _ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef
):
    pass


_RequiredClientCreateResourceDataSyncSyncSourceTypeDef = TypedDict(
    "_RequiredClientCreateResourceDataSyncSyncSourceTypeDef", {"SourceType": str}
)
_OptionalClientCreateResourceDataSyncSyncSourceTypeDef = TypedDict(
    "_OptionalClientCreateResourceDataSyncSyncSourceTypeDef",
    {
        "AwsOrganizationsSource": ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef,
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
    },
    total=False,
)


class ClientCreateResourceDataSyncSyncSourceTypeDef(
    _RequiredClientCreateResourceDataSyncSyncSourceTypeDef,
    _OptionalClientCreateResourceDataSyncSyncSourceTypeDef,
):
    """
    Specify information about the data sources to synchronize.
    - **SourceType** *(string) --***[REQUIRED]**

      The type of data source for the resource data sync. ``SourceType`` is either
      ``AwsOrganizations`` (if an organization is present in AWS Organizations) or
      ``singleAccountMultiRegions`` .
    """


_ClientDeleteInventoryResponseDeletionSummarySummaryItemsTypeDef = TypedDict(
    "_ClientDeleteInventoryResponseDeletionSummarySummaryItemsTypeDef",
    {"Version": str, "Count": int, "RemainingCount": int},
    total=False,
)


class ClientDeleteInventoryResponseDeletionSummarySummaryItemsTypeDef(
    _ClientDeleteInventoryResponseDeletionSummarySummaryItemsTypeDef
):
    pass


_ClientDeleteInventoryResponseDeletionSummaryTypeDef = TypedDict(
    "_ClientDeleteInventoryResponseDeletionSummaryTypeDef",
    {
        "TotalCount": int,
        "RemainingCount": int,
        "SummaryItems": List[ClientDeleteInventoryResponseDeletionSummarySummaryItemsTypeDef],
    },
    total=False,
)


class ClientDeleteInventoryResponseDeletionSummaryTypeDef(
    _ClientDeleteInventoryResponseDeletionSummaryTypeDef
):
    pass


_ClientDeleteInventoryResponseTypeDef = TypedDict(
    "_ClientDeleteInventoryResponseTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionSummary": ClientDeleteInventoryResponseDeletionSummaryTypeDef,
    },
    total=False,
)


class ClientDeleteInventoryResponseTypeDef(_ClientDeleteInventoryResponseTypeDef):
    """
    - *(dict) --*

      - **DeletionId** *(string) --*

        Every ``DeleteInventory`` action is assigned a unique ID. This option returns a unique ID.
        You can use this ID to query the status of a delete operation. This option is useful for
        ensuring that a delete operation has completed before you begin other actions.
    """


_ClientDeleteMaintenanceWindowResponseTypeDef = TypedDict(
    "_ClientDeleteMaintenanceWindowResponseTypeDef", {"WindowId": str}, total=False
)


class ClientDeleteMaintenanceWindowResponseTypeDef(_ClientDeleteMaintenanceWindowResponseTypeDef):
    """
    - *(dict) --*

      - **WindowId** *(string) --*

        The ID of the deleted maintenance window.
    """


_ClientDeleteParametersResponseTypeDef = TypedDict(
    "_ClientDeleteParametersResponseTypeDef",
    {"DeletedParameters": List[str], "InvalidParameters": List[str]},
    total=False,
)


class ClientDeleteParametersResponseTypeDef(_ClientDeleteParametersResponseTypeDef):
    """
    - *(dict) --*

      - **DeletedParameters** *(list) --*

        The names of the deleted parameters.
        - *(string) --*
    """


_ClientDeletePatchBaselineResponseTypeDef = TypedDict(
    "_ClientDeletePatchBaselineResponseTypeDef", {"BaselineId": str}, total=False
)


class ClientDeletePatchBaselineResponseTypeDef(_ClientDeletePatchBaselineResponseTypeDef):
    """
    - *(dict) --*

      - **BaselineId** *(string) --*

        The ID of the deleted patch baseline.
    """


_ClientDeregisterPatchBaselineForPatchGroupResponseTypeDef = TypedDict(
    "_ClientDeregisterPatchBaselineForPatchGroupResponseTypeDef",
    {"BaselineId": str, "PatchGroup": str},
    total=False,
)


class ClientDeregisterPatchBaselineForPatchGroupResponseTypeDef(
    _ClientDeregisterPatchBaselineForPatchGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **BaselineId** *(string) --*

        The ID of the patch baseline the patch group was deregistered from.
    """


_ClientDeregisterTargetFromMaintenanceWindowResponseTypeDef = TypedDict(
    "_ClientDeregisterTargetFromMaintenanceWindowResponseTypeDef",
    {"WindowId": str, "WindowTargetId": str},
    total=False,
)


class ClientDeregisterTargetFromMaintenanceWindowResponseTypeDef(
    _ClientDeregisterTargetFromMaintenanceWindowResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowId** *(string) --*

        The ID of the maintenance window the target was removed from.
    """


_ClientDeregisterTaskFromMaintenanceWindowResponseTypeDef = TypedDict(
    "_ClientDeregisterTaskFromMaintenanceWindowResponseTypeDef",
    {"WindowId": str, "WindowTaskId": str},
    total=False,
)


class ClientDeregisterTaskFromMaintenanceWindowResponseTypeDef(
    _ClientDeregisterTaskFromMaintenanceWindowResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowId** *(string) --*

        The ID of the maintenance window the task was removed from.
    """


_ClientDescribeActivationsFiltersTypeDef = TypedDict(
    "_ClientDescribeActivationsFiltersTypeDef",
    {
        "FilterKey": Literal["ActivationIds", "DefaultInstanceName", "IamRole"],
        "FilterValues": List[str],
    },
    total=False,
)


class ClientDescribeActivationsFiltersTypeDef(_ClientDescribeActivationsFiltersTypeDef):
    """
    - *(dict) --*

      Filter for the DescribeActivation API.
      - **FilterKey** *(string) --*

        The name of the filter.
    """


_ClientDescribeActivationsResponseActivationListTagsTypeDef = TypedDict(
    "_ClientDescribeActivationsResponseActivationListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeActivationsResponseActivationListTagsTypeDef(
    _ClientDescribeActivationsResponseActivationListTagsTypeDef
):
    pass


_ClientDescribeActivationsResponseActivationListTypeDef = TypedDict(
    "_ClientDescribeActivationsResponseActivationListTypeDef",
    {
        "ActivationId": str,
        "Description": str,
        "DefaultInstanceName": str,
        "IamRole": str,
        "RegistrationLimit": int,
        "RegistrationsCount": int,
        "ExpirationDate": datetime,
        "Expired": bool,
        "CreatedDate": datetime,
        "Tags": List[ClientDescribeActivationsResponseActivationListTagsTypeDef],
    },
    total=False,
)


class ClientDescribeActivationsResponseActivationListTypeDef(
    _ClientDescribeActivationsResponseActivationListTypeDef
):
    """
    - *(dict) --*

      An activation registers one or more on-premises servers or virtual machines (VMs) with AWS so
      that you can configure those servers or VMs using Run Command. A server or VM that has been
      registered with AWS is called a managed instance.
      - **ActivationId** *(string) --*

        The ID created by Systems Manager when you submitted the activation.
    """


_ClientDescribeActivationsResponseTypeDef = TypedDict(
    "_ClientDescribeActivationsResponseTypeDef",
    {
        "ActivationList": List[ClientDescribeActivationsResponseActivationListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeActivationsResponseTypeDef(_ClientDescribeActivationsResponseTypeDef):
    """
    - *(dict) --*

      - **ActivationList** *(list) --*

        A list of activations for your AWS account.
        - *(dict) --*

          An activation registers one or more on-premises servers or virtual machines (VMs) with AWS
          so that you can configure those servers or VMs using Run Command. A server or VM that has
          been registered with AWS is called a managed instance.
          - **ActivationId** *(string) --*

            The ID created by Systems Manager when you submitted the activation.
    """


_RequiredClientDescribeAssociationExecutionTargetsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeAssociationExecutionTargetsFiltersTypeDef",
    {"Key": Literal["Status", "ResourceId", "ResourceType"]},
)
_OptionalClientDescribeAssociationExecutionTargetsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeAssociationExecutionTargetsFiltersTypeDef", {"Value": str}, total=False
)


class ClientDescribeAssociationExecutionTargetsFiltersTypeDef(
    _RequiredClientDescribeAssociationExecutionTargetsFiltersTypeDef,
    _OptionalClientDescribeAssociationExecutionTargetsFiltersTypeDef,
):
    """
    - *(dict) --*

      Filters for the association execution.
      - **Key** *(string) --***[REQUIRED]**

        The key value used in the request.
    """


_ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsOutputSourceTypeDef = TypedDict(
    "_ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsOutputSourceTypeDef",
    {"OutputSourceId": str, "OutputSourceType": str},
    total=False,
)


class ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsOutputSourceTypeDef(
    _ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsOutputSourceTypeDef
):
    pass


_ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsTypeDef = TypedDict(
    "_ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "ResourceId": str,
        "ResourceType": str,
        "Status": str,
        "DetailedStatus": str,
        "LastExecutionDate": datetime,
        "OutputSource": ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsOutputSourceTypeDef,
    },
    total=False,
)


class ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsTypeDef(
    _ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsTypeDef
):
    """
    - *(dict) --*

      Includes information about the specified association execution.
      - **AssociationId** *(string) --*

        The association ID.
    """


_ClientDescribeAssociationExecutionTargetsResponseTypeDef = TypedDict(
    "_ClientDescribeAssociationExecutionTargetsResponseTypeDef",
    {
        "AssociationExecutionTargets": List[
            ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAssociationExecutionTargetsResponseTypeDef(
    _ClientDescribeAssociationExecutionTargetsResponseTypeDef
):
    """
    - *(dict) --*

      - **AssociationExecutionTargets** *(list) --*

        Information about the execution.
        - *(dict) --*

          Includes information about the specified association execution.
          - **AssociationId** *(string) --*

            The association ID.
    """


_RequiredClientDescribeAssociationExecutionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeAssociationExecutionsFiltersTypeDef",
    {"Key": Literal["ExecutionId", "Status", "CreatedTime"]},
)
_OptionalClientDescribeAssociationExecutionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeAssociationExecutionsFiltersTypeDef",
    {"Value": str, "Type": Literal["EQUAL", "LESS_THAN", "GREATER_THAN"]},
    total=False,
)


class ClientDescribeAssociationExecutionsFiltersTypeDef(
    _RequiredClientDescribeAssociationExecutionsFiltersTypeDef,
    _OptionalClientDescribeAssociationExecutionsFiltersTypeDef,
):
    """
    - *(dict) --*

      Filters used in the request.
      - **Key** *(string) --***[REQUIRED]**

        The key value used in the request.
    """


_ClientDescribeAssociationExecutionsResponseAssociationExecutionsTypeDef = TypedDict(
    "_ClientDescribeAssociationExecutionsResponseAssociationExecutionsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "Status": str,
        "DetailedStatus": str,
        "CreatedTime": datetime,
        "LastExecutionDate": datetime,
        "ResourceCountByStatus": str,
    },
    total=False,
)


class ClientDescribeAssociationExecutionsResponseAssociationExecutionsTypeDef(
    _ClientDescribeAssociationExecutionsResponseAssociationExecutionsTypeDef
):
    """
    - *(dict) --*

      Includes information about the specified association.
      - **AssociationId** *(string) --*

        The association ID.
    """


_ClientDescribeAssociationExecutionsResponseTypeDef = TypedDict(
    "_ClientDescribeAssociationExecutionsResponseTypeDef",
    {
        "AssociationExecutions": List[
            ClientDescribeAssociationExecutionsResponseAssociationExecutionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAssociationExecutionsResponseTypeDef(
    _ClientDescribeAssociationExecutionsResponseTypeDef
):
    """
    - *(dict) --*

      - **AssociationExecutions** *(list) --*

        A list of the executions for the specified association ID.
        - *(dict) --*

          Includes information about the specified association.
          - **AssociationId** *(string) --*

            The association ID.
    """


_ClientDescribeAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef = TypedDict(
    "_ClientDescribeAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)


class ClientDescribeAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef(
    _ClientDescribeAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef
):
    pass


_ClientDescribeAssociationResponseAssociationDescriptionOutputLocationTypeDef = TypedDict(
    "_ClientDescribeAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    {
        "S3Location": ClientDescribeAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef
    },
    total=False,
)


class ClientDescribeAssociationResponseAssociationDescriptionOutputLocationTypeDef(
    _ClientDescribeAssociationResponseAssociationDescriptionOutputLocationTypeDef
):
    pass


_ClientDescribeAssociationResponseAssociationDescriptionOverviewTypeDef = TypedDict(
    "_ClientDescribeAssociationResponseAssociationDescriptionOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)


class ClientDescribeAssociationResponseAssociationDescriptionOverviewTypeDef(
    _ClientDescribeAssociationResponseAssociationDescriptionOverviewTypeDef
):
    pass


_ClientDescribeAssociationResponseAssociationDescriptionStatusTypeDef = TypedDict(
    "_ClientDescribeAssociationResponseAssociationDescriptionStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)


class ClientDescribeAssociationResponseAssociationDescriptionStatusTypeDef(
    _ClientDescribeAssociationResponseAssociationDescriptionStatusTypeDef
):
    pass


_ClientDescribeAssociationResponseAssociationDescriptionTargetsTypeDef = TypedDict(
    "_ClientDescribeAssociationResponseAssociationDescriptionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeAssociationResponseAssociationDescriptionTargetsTypeDef(
    _ClientDescribeAssociationResponseAssociationDescriptionTargetsTypeDef
):
    pass


_ClientDescribeAssociationResponseAssociationDescriptionTypeDef = TypedDict(
    "_ClientDescribeAssociationResponseAssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientDescribeAssociationResponseAssociationDescriptionStatusTypeDef,
        "Overview": ClientDescribeAssociationResponseAssociationDescriptionOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientDescribeAssociationResponseAssociationDescriptionTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientDescribeAssociationResponseAssociationDescriptionOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)


class ClientDescribeAssociationResponseAssociationDescriptionTypeDef(
    _ClientDescribeAssociationResponseAssociationDescriptionTypeDef
):
    """
    - **AssociationDescription** *(dict) --*

      Information about the association.
      - **Name** *(string) --*

        The name of the Systems Manager document.
    """


_ClientDescribeAssociationResponseTypeDef = TypedDict(
    "_ClientDescribeAssociationResponseTypeDef",
    {"AssociationDescription": ClientDescribeAssociationResponseAssociationDescriptionTypeDef},
    total=False,
)


class ClientDescribeAssociationResponseTypeDef(_ClientDescribeAssociationResponseTypeDef):
    """
    - *(dict) --*

      - **AssociationDescription** *(dict) --*

        Information about the association.
        - **Name** *(string) --*

          The name of the Systems Manager document.
    """


_RequiredClientDescribeAutomationExecutionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeAutomationExecutionsFiltersTypeDef",
    {
        "Key": Literal[
            "DocumentNamePrefix",
            "ExecutionStatus",
            "ExecutionId",
            "ParentExecutionId",
            "CurrentAction",
            "StartTimeBefore",
            "StartTimeAfter",
            "AutomationType",
        ]
    },
)
_OptionalClientDescribeAutomationExecutionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeAutomationExecutionsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeAutomationExecutionsFiltersTypeDef(
    _RequiredClientDescribeAutomationExecutionsFiltersTypeDef,
    _OptionalClientDescribeAutomationExecutionsFiltersTypeDef,
):
    """
    - *(dict) --*

      A filter used to match specific automation executions. This is used to limit the scope of
      Automation execution information returned.
      - **Key** *(string) --***[REQUIRED]**

        One or more keys to limit the results. Valid filter keys include the following:
        DocumentNamePrefix, ExecutionStatus, ExecutionId, ParentExecutionId, CurrentAction,
        StartTimeBefore, StartTimeAfter.
    """


_ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListResolvedTargetsTypeDef = TypedDict(
    "_ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListResolvedTargetsTypeDef",
    {"ParameterValues": List[str], "Truncated": bool},
    total=False,
)


class ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListResolvedTargetsTypeDef(
    _ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListResolvedTargetsTypeDef
):
    pass


_ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTargetsTypeDef = TypedDict(
    "_ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTargetsTypeDef(
    _ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTargetsTypeDef
):
    pass


_ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTypeDef = TypedDict(
    "_ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "AutomationExecutionStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "ExecutedBy": str,
        "LogFile": str,
        "Outputs": Dict[str, List[str]],
        "Mode": Literal["Auto", "Interactive"],
        "ParentAutomationExecutionId": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "FailureMessage": str,
        "TargetParameterName": str,
        "Targets": List[
            ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTargetsTypeDef
        ],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListResolvedTargetsTypeDef,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "AutomationType": Literal["CrossAccount", "Local"],
    },
    total=False,
)


class ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTypeDef(
    _ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTypeDef
):
    """
    - *(dict) --*

      Details about a specific Automation execution.
      - **AutomationExecutionId** *(string) --*

        The execution ID.
    """


_ClientDescribeAutomationExecutionsResponseTypeDef = TypedDict(
    "_ClientDescribeAutomationExecutionsResponseTypeDef",
    {
        "AutomationExecutionMetadataList": List[
            ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAutomationExecutionsResponseTypeDef(
    _ClientDescribeAutomationExecutionsResponseTypeDef
):
    """
    - *(dict) --*

      - **AutomationExecutionMetadataList** *(list) --*

        The list of details about each automation execution which has occurred which matches the
        filter specification, if any.
        - *(dict) --*

          Details about a specific Automation execution.
          - **AutomationExecutionId** *(string) --*

            The execution ID.
    """


_RequiredClientDescribeAutomationStepExecutionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeAutomationStepExecutionsFiltersTypeDef",
    {
        "Key": Literal[
            "StartTimeBefore",
            "StartTimeAfter",
            "StepExecutionStatus",
            "StepExecutionId",
            "StepName",
            "Action",
        ]
    },
)
_OptionalClientDescribeAutomationStepExecutionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeAutomationStepExecutionsFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeAutomationStepExecutionsFiltersTypeDef(
    _RequiredClientDescribeAutomationStepExecutionsFiltersTypeDef,
    _OptionalClientDescribeAutomationStepExecutionsFiltersTypeDef,
):
    """
    - *(dict) --*

      A filter to limit the amount of step execution information returned by the call.
      - **Key** *(string) --***[REQUIRED]**

        One or more keys to limit the results. Valid filter keys include the following: StepName,
        Action, StepExecutionId, StepExecutionStatus, StartTimeBefore, StartTimeAfter.
    """


_ClientDescribeAutomationStepExecutionsResponseStepExecutionsFailureDetailsTypeDef = TypedDict(
    "_ClientDescribeAutomationStepExecutionsResponseStepExecutionsFailureDetailsTypeDef",
    {"FailureStage": str, "FailureType": str, "Details": Dict[str, List[str]]},
    total=False,
)


class ClientDescribeAutomationStepExecutionsResponseStepExecutionsFailureDetailsTypeDef(
    _ClientDescribeAutomationStepExecutionsResponseStepExecutionsFailureDetailsTypeDef
):
    pass


_ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetLocationTypeDef = TypedDict(
    "_ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetLocationTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)


class ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetLocationTypeDef(
    _ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetLocationTypeDef
):
    pass


_ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetsTypeDef = TypedDict(
    "_ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetsTypeDef(
    _ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetsTypeDef
):
    pass


_ClientDescribeAutomationStepExecutionsResponseStepExecutionsTypeDef = TypedDict(
    "_ClientDescribeAutomationStepExecutionsResponseStepExecutionsTypeDef",
    {
        "StepName": str,
        "Action": str,
        "TimeoutSeconds": int,
        "OnFailure": str,
        "MaxAttempts": int,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "StepStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ResponseCode": str,
        "Inputs": Dict[str, str],
        "Outputs": Dict[str, List[str]],
        "Response": str,
        "FailureMessage": str,
        "FailureDetails": ClientDescribeAutomationStepExecutionsResponseStepExecutionsFailureDetailsTypeDef,
        "StepExecutionId": str,
        "OverriddenParameters": Dict[str, List[str]],
        "IsEnd": bool,
        "NextStep": str,
        "IsCritical": bool,
        "ValidNextSteps": List[str],
        "Targets": List[ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetsTypeDef],
        "TargetLocation": ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetLocationTypeDef,
    },
    total=False,
)


class ClientDescribeAutomationStepExecutionsResponseStepExecutionsTypeDef(
    _ClientDescribeAutomationStepExecutionsResponseStepExecutionsTypeDef
):
    """
    - *(dict) --*

      Detailed information about an the execution state of an Automation step.
      - **StepName** *(string) --*

        The name of this execution step.
    """


_ClientDescribeAutomationStepExecutionsResponseTypeDef = TypedDict(
    "_ClientDescribeAutomationStepExecutionsResponseTypeDef",
    {
        "StepExecutions": List[ClientDescribeAutomationStepExecutionsResponseStepExecutionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAutomationStepExecutionsResponseTypeDef(
    _ClientDescribeAutomationStepExecutionsResponseTypeDef
):
    """
    - *(dict) --*

      - **StepExecutions** *(list) --*

        A list of details about the current state of all steps that make up an execution.
        - *(dict) --*

          Detailed information about an the execution state of an Automation step.
          - **StepName** *(string) --*

            The name of this execution step.
    """


_ClientDescribeAvailablePatchesFiltersTypeDef = TypedDict(
    "_ClientDescribeAvailablePatchesFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientDescribeAvailablePatchesFiltersTypeDef(_ClientDescribeAvailablePatchesFiltersTypeDef):
    """
    - *(dict) --*

      Defines a filter used in Patch Manager APIs.
      - **Key** *(string) --*

        The key for the filter.
    """


_ClientDescribeAvailablePatchesResponsePatchesTypeDef = TypedDict(
    "_ClientDescribeAvailablePatchesResponsePatchesTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
    },
    total=False,
)


class ClientDescribeAvailablePatchesResponsePatchesTypeDef(
    _ClientDescribeAvailablePatchesResponsePatchesTypeDef
):
    """
    - *(dict) --*

      Represents metadata about a patch.
      - **Id** *(string) --*

        The ID of the patch (this is different than the Microsoft Knowledge Base ID).
    """


_ClientDescribeAvailablePatchesResponseTypeDef = TypedDict(
    "_ClientDescribeAvailablePatchesResponseTypeDef",
    {"Patches": List[ClientDescribeAvailablePatchesResponsePatchesTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeAvailablePatchesResponseTypeDef(_ClientDescribeAvailablePatchesResponseTypeDef):
    """
    - *(dict) --*

      - **Patches** *(list) --*

        An array of patches. Each entry in the array is a patch structure.
        - *(dict) --*

          Represents metadata about a patch.
          - **Id** *(string) --*

            The ID of the patch (this is different than the Microsoft Knowledge Base ID).
    """


_ClientDescribeDocumentPermissionResponseAccountSharingInfoListTypeDef = TypedDict(
    "_ClientDescribeDocumentPermissionResponseAccountSharingInfoListTypeDef",
    {"AccountId": str, "SharedDocumentVersion": str},
    total=False,
)


class ClientDescribeDocumentPermissionResponseAccountSharingInfoListTypeDef(
    _ClientDescribeDocumentPermissionResponseAccountSharingInfoListTypeDef
):
    pass


_ClientDescribeDocumentPermissionResponseTypeDef = TypedDict(
    "_ClientDescribeDocumentPermissionResponseTypeDef",
    {
        "AccountIds": List[str],
        "AccountSharingInfoList": List[
            ClientDescribeDocumentPermissionResponseAccountSharingInfoListTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDocumentPermissionResponseTypeDef(
    _ClientDescribeDocumentPermissionResponseTypeDef
):
    """
    - *(dict) --*

      - **AccountIds** *(list) --*

        The account IDs that have permission to use this document. The ID can be either an AWS
        account or *All* .
        - *(string) --*
    """


_ClientDescribeDocumentResponseDocumentAttachmentsInformationTypeDef = TypedDict(
    "_ClientDescribeDocumentResponseDocumentAttachmentsInformationTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeDocumentResponseDocumentAttachmentsInformationTypeDef(
    _ClientDescribeDocumentResponseDocumentAttachmentsInformationTypeDef
):
    pass


_ClientDescribeDocumentResponseDocumentParametersTypeDef = TypedDict(
    "_ClientDescribeDocumentResponseDocumentParametersTypeDef",
    {"Name": str, "Type": Literal["String", "StringList"], "Description": str, "DefaultValue": str},
    total=False,
)


class ClientDescribeDocumentResponseDocumentParametersTypeDef(
    _ClientDescribeDocumentResponseDocumentParametersTypeDef
):
    pass


_ClientDescribeDocumentResponseDocumentRequiresTypeDef = TypedDict(
    "_ClientDescribeDocumentResponseDocumentRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientDescribeDocumentResponseDocumentRequiresTypeDef(
    _ClientDescribeDocumentResponseDocumentRequiresTypeDef
):
    pass


_ClientDescribeDocumentResponseDocumentTagsTypeDef = TypedDict(
    "_ClientDescribeDocumentResponseDocumentTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeDocumentResponseDocumentTagsTypeDef(
    _ClientDescribeDocumentResponseDocumentTagsTypeDef
):
    pass


_ClientDescribeDocumentResponseDocumentTypeDef = TypedDict(
    "_ClientDescribeDocumentResponseDocumentTypeDef",
    {
        "Sha1": str,
        "Hash": str,
        "HashType": Literal["Sha256", "Sha1"],
        "Name": str,
        "VersionName": str,
        "Owner": str,
        "CreatedDate": datetime,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "DocumentVersion": str,
        "Description": str,
        "Parameters": List[ClientDescribeDocumentResponseDocumentParametersTypeDef],
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
        ],
        "SchemaVersion": str,
        "LatestVersion": str,
        "DefaultVersion": str,
        "DocumentFormat": Literal["YAML", "JSON"],
        "TargetType": str,
        "Tags": List[ClientDescribeDocumentResponseDocumentTagsTypeDef],
        "AttachmentsInformation": List[
            ClientDescribeDocumentResponseDocumentAttachmentsInformationTypeDef
        ],
        "Requires": List[ClientDescribeDocumentResponseDocumentRequiresTypeDef],
    },
    total=False,
)


class ClientDescribeDocumentResponseDocumentTypeDef(_ClientDescribeDocumentResponseDocumentTypeDef):
    """
    - **Document** *(dict) --*

      Information about the Systems Manager document.
      - **Sha1** *(string) --*

        The SHA1 hash of the document, which you can use for verification.
    """


_ClientDescribeDocumentResponseTypeDef = TypedDict(
    "_ClientDescribeDocumentResponseTypeDef",
    {"Document": ClientDescribeDocumentResponseDocumentTypeDef},
    total=False,
)


class ClientDescribeDocumentResponseTypeDef(_ClientDescribeDocumentResponseTypeDef):
    """
    - *(dict) --*

      - **Document** *(dict) --*

        Information about the Systems Manager document.
        - **Sha1** *(string) --*

          The SHA1 hash of the document, which you can use for verification.
    """


_ClientDescribeEffectiveInstanceAssociationsResponseAssociationsTypeDef = TypedDict(
    "_ClientDescribeEffectiveInstanceAssociationsResponseAssociationsTypeDef",
    {"AssociationId": str, "InstanceId": str, "Content": str, "AssociationVersion": str},
    total=False,
)


class ClientDescribeEffectiveInstanceAssociationsResponseAssociationsTypeDef(
    _ClientDescribeEffectiveInstanceAssociationsResponseAssociationsTypeDef
):
    """
    - *(dict) --*

      One or more association documents on the instance.
      - **AssociationId** *(string) --*

        The association ID.
    """


_ClientDescribeEffectiveInstanceAssociationsResponseTypeDef = TypedDict(
    "_ClientDescribeEffectiveInstanceAssociationsResponseTypeDef",
    {
        "Associations": List[
            ClientDescribeEffectiveInstanceAssociationsResponseAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeEffectiveInstanceAssociationsResponseTypeDef(
    _ClientDescribeEffectiveInstanceAssociationsResponseTypeDef
):
    """
    - *(dict) --*

      - **Associations** *(list) --*

        The associations for the requested instance.
        - *(dict) --*

          One or more association documents on the instance.
          - **AssociationId** *(string) --*

            The association ID.
    """


_ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchStatusTypeDef = TypedDict(
    "_ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchStatusTypeDef",
    {
        "DeploymentStatus": Literal[
            "APPROVED", "PENDING_APPROVAL", "EXPLICIT_APPROVED", "EXPLICIT_REJECTED"
        ],
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovalDate": datetime,
    },
    total=False,
)


class ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchStatusTypeDef(
    _ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchStatusTypeDef
):
    pass


_ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchTypeDef = TypedDict(
    "_ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
    },
    total=False,
)


class ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchTypeDef(
    _ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchTypeDef
):
    """
    - **Patch** *(dict) --*

      Provides metadata for a patch, including information such as the KB ID, severity,
      classification and a URL for where more information can be obtained about the patch.
      - **Id** *(string) --*

        The ID of the patch (this is different than the Microsoft Knowledge Base ID).
    """


_ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesTypeDef = TypedDict(
    "_ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesTypeDef",
    {
        "Patch": ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchTypeDef,
        "PatchStatus": ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchStatusTypeDef,
    },
    total=False,
)


class ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesTypeDef(
    _ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesTypeDef
):
    """
    - *(dict) --*

      The EffectivePatch structure defines metadata about a patch along with the approval state of
      the patch in a particular patch baseline. The approval state includes information about
      whether the patch is currently approved, due to be approved by a rule, explicitly approved, or
      explicitly rejected and the date the patch was or will be approved.
      - **Patch** *(dict) --*

        Provides metadata for a patch, including information such as the KB ID, severity,
        classification and a URL for where more information can be obtained about the patch.
        - **Id** *(string) --*

          The ID of the patch (this is different than the Microsoft Knowledge Base ID).
    """


_ClientDescribeEffectivePatchesForPatchBaselineResponseTypeDef = TypedDict(
    "_ClientDescribeEffectivePatchesForPatchBaselineResponseTypeDef",
    {
        "EffectivePatches": List[
            ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeEffectivePatchesForPatchBaselineResponseTypeDef(
    _ClientDescribeEffectivePatchesForPatchBaselineResponseTypeDef
):
    """
    - *(dict) --*

      - **EffectivePatches** *(list) --*

        An array of patches and patch status.
        - *(dict) --*

          The EffectivePatch structure defines metadata about a patch along with the approval state
          of the patch in a particular patch baseline. The approval state includes information about
          whether the patch is currently approved, due to be approved by a rule, explicitly
          approved, or explicitly rejected and the date the patch was or will be approved.
          - **Patch** *(dict) --*

            Provides metadata for a patch, including information such as the KB ID, severity,
            classification and a URL for where more information can be obtained about the patch.
            - **Id** *(string) --*

              The ID of the patch (this is different than the Microsoft Knowledge Base ID).
    """


_ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef = TypedDict(
    "_ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef",
    {"OutputUrl": str},
    total=False,
)


class ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef(
    _ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef
):
    pass


_ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlTypeDef = TypedDict(
    "_ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlTypeDef",
    {
        "S3OutputUrl": ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef
    },
    total=False,
)


class ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlTypeDef(
    _ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlTypeDef
):
    pass


_ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosTypeDef = TypedDict(
    "_ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosTypeDef",
    {
        "AssociationId": str,
        "Name": str,
        "DocumentVersion": str,
        "AssociationVersion": str,
        "InstanceId": str,
        "ExecutionDate": datetime,
        "Status": str,
        "DetailedStatus": str,
        "ExecutionSummary": str,
        "ErrorCode": str,
        "OutputUrl": ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlTypeDef,
        "AssociationName": str,
    },
    total=False,
)


class ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosTypeDef(
    _ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosTypeDef
):
    """
    - *(dict) --*

      Status information about the instance association.
      - **AssociationId** *(string) --*

        The association ID.
    """


_ClientDescribeInstanceAssociationsStatusResponseTypeDef = TypedDict(
    "_ClientDescribeInstanceAssociationsStatusResponseTypeDef",
    {
        "InstanceAssociationStatusInfos": List[
            ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeInstanceAssociationsStatusResponseTypeDef(
    _ClientDescribeInstanceAssociationsStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **InstanceAssociationStatusInfos** *(list) --*

        Status information about the association.
        - *(dict) --*

          Status information about the instance association.
          - **AssociationId** *(string) --*

            The association ID.
    """


_RequiredClientDescribeInstanceInformationFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeInstanceInformationFiltersTypeDef", {"Key": str}
)
_OptionalClientDescribeInstanceInformationFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeInstanceInformationFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeInstanceInformationFiltersTypeDef(
    _RequiredClientDescribeInstanceInformationFiltersTypeDef,
    _OptionalClientDescribeInstanceInformationFiltersTypeDef,
):
    """
    - *(dict) --*

      The filters to describe or get information about your managed instances.
      - **Key** *(string) --***[REQUIRED]**

        The filter key name to describe your instances. For example:
        "InstanceIds"|"AgentVersion"|"PingStatus"|"PlatformTypes"|"ActivationIds"|"IamRole"
        |"ResourceType"|"AssociationStatus"|"Tag
        Key"
    """


_RequiredClientDescribeInstanceInformationInstanceInformationFilterListTypeDef = TypedDict(
    "_RequiredClientDescribeInstanceInformationInstanceInformationFilterListTypeDef",
    {
        "key": Literal[
            "InstanceIds",
            "AgentVersion",
            "PingStatus",
            "PlatformTypes",
            "ActivationIds",
            "IamRole",
            "ResourceType",
            "AssociationStatus",
        ]
    },
)
_OptionalClientDescribeInstanceInformationInstanceInformationFilterListTypeDef = TypedDict(
    "_OptionalClientDescribeInstanceInformationInstanceInformationFilterListTypeDef",
    {"valueSet": List[str]},
    total=False,
)


class ClientDescribeInstanceInformationInstanceInformationFilterListTypeDef(
    _RequiredClientDescribeInstanceInformationInstanceInformationFilterListTypeDef,
    _OptionalClientDescribeInstanceInformationInstanceInformationFilterListTypeDef,
):
    """
    - *(dict) --*

      Describes a filter for a specific list of instances. You can filter instances information by
      using tags. You specify tags by using a key-value mapping.
      Use this action instead of the
      DescribeInstanceInformationRequest$InstanceInformationFilterList method. The
      ``InstanceInformationFilterList`` method is a legacy method and does not support tags.
      - **key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeInstanceInformationResponseInstanceInformationListAssociationOverviewTypeDef = TypedDict(
    "_ClientDescribeInstanceInformationResponseInstanceInformationListAssociationOverviewTypeDef",
    {"DetailedStatus": str, "InstanceAssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)


class ClientDescribeInstanceInformationResponseInstanceInformationListAssociationOverviewTypeDef(
    _ClientDescribeInstanceInformationResponseInstanceInformationListAssociationOverviewTypeDef
):
    pass


_ClientDescribeInstanceInformationResponseInstanceInformationListTypeDef = TypedDict(
    "_ClientDescribeInstanceInformationResponseInstanceInformationListTypeDef",
    {
        "InstanceId": str,
        "PingStatus": Literal["Online", "ConnectionLost", "Inactive"],
        "LastPingDateTime": datetime,
        "AgentVersion": str,
        "IsLatestVersion": bool,
        "PlatformType": Literal["Windows", "Linux"],
        "PlatformName": str,
        "PlatformVersion": str,
        "ActivationId": str,
        "IamRole": str,
        "RegistrationDate": datetime,
        "ResourceType": Literal["ManagedInstance", "Document", "EC2Instance"],
        "Name": str,
        "IPAddress": str,
        "ComputerName": str,
        "AssociationStatus": str,
        "LastAssociationExecutionDate": datetime,
        "LastSuccessfulAssociationExecutionDate": datetime,
        "AssociationOverview": ClientDescribeInstanceInformationResponseInstanceInformationListAssociationOverviewTypeDef,
    },
    total=False,
)


class ClientDescribeInstanceInformationResponseInstanceInformationListTypeDef(
    _ClientDescribeInstanceInformationResponseInstanceInformationListTypeDef
):
    """
    - *(dict) --*

      Describes a filter for a specific list of instances.
      - **InstanceId** *(string) --*

        The instance ID.
    """


_ClientDescribeInstanceInformationResponseTypeDef = TypedDict(
    "_ClientDescribeInstanceInformationResponseTypeDef",
    {
        "InstanceInformationList": List[
            ClientDescribeInstanceInformationResponseInstanceInformationListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeInstanceInformationResponseTypeDef(
    _ClientDescribeInstanceInformationResponseTypeDef
):
    """
    - *(dict) --*

      - **InstanceInformationList** *(list) --*

        The instance information list.
        - *(dict) --*

          Describes a filter for a specific list of instances.
          - **InstanceId** *(string) --*

            The instance ID.
    """


_RequiredClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef", {"Key": str}
)
_OptionalClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef",
    {"Values": List[str], "Type": Literal["Equal", "NotEqual", "LessThan", "GreaterThan"]},
    total=False,
)


class ClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef(
    _RequiredClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef,
    _OptionalClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef,
):
    """
    - *(dict) --*

      Defines a filter used in DescribeInstancePatchStatesForPatchGroup used to scope down the
      information returned by the API.
      - **Key** *(string) --***[REQUIRED]**

        The key for the filter. Supported values are FailedCount, InstalledCount,
        InstalledOtherCount, MissingCount and NotApplicableCount.
    """


_ClientDescribeInstancePatchStatesForPatchGroupResponseInstancePatchStatesTypeDef = TypedDict(
    "_ClientDescribeInstancePatchStatesForPatchGroupResponseInstancePatchStatesTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": Literal["Scan", "Install"],
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": Literal["RebootIfNeeded", "NoReboot"],
    },
    total=False,
)


class ClientDescribeInstancePatchStatesForPatchGroupResponseInstancePatchStatesTypeDef(
    _ClientDescribeInstancePatchStatesForPatchGroupResponseInstancePatchStatesTypeDef
):
    """
    - *(dict) --*

      Defines the high-level patch compliance state for a managed instance, providing information
      about the number of installed, missing, not applicable, and failed patches along with metadata
      about the operation when this information was gathered for the instance.
      - **InstanceId** *(string) --*

        The ID of the managed instance the high-level patch compliance information was collected
        for.
    """


_ClientDescribeInstancePatchStatesForPatchGroupResponseTypeDef = TypedDict(
    "_ClientDescribeInstancePatchStatesForPatchGroupResponseTypeDef",
    {
        "InstancePatchStates": List[
            ClientDescribeInstancePatchStatesForPatchGroupResponseInstancePatchStatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeInstancePatchStatesForPatchGroupResponseTypeDef(
    _ClientDescribeInstancePatchStatesForPatchGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **InstancePatchStates** *(list) --*

        The high-level patch state for the requested instances.
        - *(dict) --*

          Defines the high-level patch compliance state for a managed instance, providing
          information about the number of installed, missing, not applicable, and failed patches
          along with metadata about the operation when this information was gathered for the
          instance.
          - **InstanceId** *(string) --*

            The ID of the managed instance the high-level patch compliance information was collected
            for.
    """


_ClientDescribeInstancePatchStatesResponseInstancePatchStatesTypeDef = TypedDict(
    "_ClientDescribeInstancePatchStatesResponseInstancePatchStatesTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": Literal["Scan", "Install"],
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": Literal["RebootIfNeeded", "NoReboot"],
    },
    total=False,
)


class ClientDescribeInstancePatchStatesResponseInstancePatchStatesTypeDef(
    _ClientDescribeInstancePatchStatesResponseInstancePatchStatesTypeDef
):
    """
    - *(dict) --*

      Defines the high-level patch compliance state for a managed instance, providing information
      about the number of installed, missing, not applicable, and failed patches along with metadata
      about the operation when this information was gathered for the instance.
      - **InstanceId** *(string) --*

        The ID of the managed instance the high-level patch compliance information was collected
        for.
    """


_ClientDescribeInstancePatchStatesResponseTypeDef = TypedDict(
    "_ClientDescribeInstancePatchStatesResponseTypeDef",
    {
        "InstancePatchStates": List[
            ClientDescribeInstancePatchStatesResponseInstancePatchStatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeInstancePatchStatesResponseTypeDef(
    _ClientDescribeInstancePatchStatesResponseTypeDef
):
    """
    - *(dict) --*

      - **InstancePatchStates** *(list) --*

        The high-level patch state for the requested instances.
        - *(dict) --*

          Defines the high-level patch compliance state for a managed instance, providing
          information about the number of installed, missing, not applicable, and failed patches
          along with metadata about the operation when this information was gathered for the
          instance.
          - **InstanceId** *(string) --*

            The ID of the managed instance the high-level patch compliance information was collected
            for.
    """


_ClientDescribeInstancePatchesFiltersTypeDef = TypedDict(
    "_ClientDescribeInstancePatchesFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientDescribeInstancePatchesFiltersTypeDef(_ClientDescribeInstancePatchesFiltersTypeDef):
    """
    - *(dict) --*

      Defines a filter used in Patch Manager APIs.
      - **Key** *(string) --*

        The key for the filter.
    """


_ClientDescribeInstancePatchesResponsePatchesTypeDef = TypedDict(
    "_ClientDescribeInstancePatchesResponsePatchesTypeDef",
    {
        "Title": str,
        "KBId": str,
        "Classification": str,
        "Severity": str,
        "State": Literal[
            "INSTALLED",
            "INSTALLED_OTHER",
            "INSTALLED_PENDING_REBOOT",
            "INSTALLED_REJECTED",
            "MISSING",
            "NOT_APPLICABLE",
            "FAILED",
        ],
        "InstalledTime": datetime,
    },
    total=False,
)


class ClientDescribeInstancePatchesResponsePatchesTypeDef(
    _ClientDescribeInstancePatchesResponsePatchesTypeDef
):
    """
    - *(dict) --*

      Information about the state of a patch on a particular instance as it relates to the patch
      baseline used to patch the instance.
      - **Title** *(string) --*

        The title of the patch.
    """


_ClientDescribeInstancePatchesResponseTypeDef = TypedDict(
    "_ClientDescribeInstancePatchesResponseTypeDef",
    {"Patches": List[ClientDescribeInstancePatchesResponsePatchesTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeInstancePatchesResponseTypeDef(_ClientDescribeInstancePatchesResponseTypeDef):
    """
    - *(dict) --*

      - **Patches** *(list) --*

        Each entry in the array is a structure containing:
        Title (string)
        KBId (string)
        Classification (string)
        Severity (string)
        State (string, such as "INSTALLED" or "FAILED")
        InstalledTime (DateTime)
        InstalledBy (string)
        - *(dict) --*

          Information about the state of a patch on a particular instance as it relates to the patch
          baseline used to patch the instance.
          - **Title** *(string) --*

            The title of the patch.
    """


_ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef = TypedDict(
    "_ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef",
    {"Version": str, "Count": int, "RemainingCount": int},
    total=False,
)


class ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef(
    _ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef
):
    pass


_ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummaryTypeDef = TypedDict(
    "_ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummaryTypeDef",
    {
        "TotalCount": int,
        "RemainingCount": int,
        "SummaryItems": List[
            ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummaryTypeDef(
    _ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummaryTypeDef
):
    pass


_ClientDescribeInventoryDeletionsResponseInventoryDeletionsTypeDef = TypedDict(
    "_ClientDescribeInventoryDeletionsResponseInventoryDeletionsTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionStartTime": datetime,
        "LastStatus": Literal["InProgress", "Complete"],
        "LastStatusMessage": str,
        "DeletionSummary": ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummaryTypeDef,
        "LastStatusUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeInventoryDeletionsResponseInventoryDeletionsTypeDef(
    _ClientDescribeInventoryDeletionsResponseInventoryDeletionsTypeDef
):
    """
    - *(dict) --*

      Status information returned by the ``DeleteInventory`` action.
      - **DeletionId** *(string) --*

        The deletion ID returned by the ``DeleteInventory`` action.
    """


_ClientDescribeInventoryDeletionsResponseTypeDef = TypedDict(
    "_ClientDescribeInventoryDeletionsResponseTypeDef",
    {
        "InventoryDeletions": List[
            ClientDescribeInventoryDeletionsResponseInventoryDeletionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeInventoryDeletionsResponseTypeDef(
    _ClientDescribeInventoryDeletionsResponseTypeDef
):
    """
    - *(dict) --*

      - **InventoryDeletions** *(list) --*

        A list of status items for deleted inventory.
        - *(dict) --*

          Status information returned by the ``DeleteInventory`` action.
          - **DeletionId** *(string) --*

            The deletion ID returned by the ``DeleteInventory`` action.
    """


_ClientDescribeMaintenanceWindowExecutionTaskInvocationsFiltersTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowExecutionTaskInvocationsFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeMaintenanceWindowExecutionTaskInvocationsFiltersTypeDef(
    _ClientDescribeMaintenanceWindowExecutionTaskInvocationsFiltersTypeDef
):
    """
    - *(dict) --*

      Filter used in the request. Supported filter keys are Name and Enabled.
      - **Key** *(string) --*

        The name of the filter.
    """


_ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseWindowExecutionTaskInvocationIdentitiesTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseWindowExecutionTaskInvocationIdentitiesTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Parameters": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)


class ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseWindowExecutionTaskInvocationIdentitiesTypeDef(
    _ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseWindowExecutionTaskInvocationIdentitiesTypeDef
):
    """
    - *(dict) --*

      Describes the information about a task invocation for a particular target as part of a task
      execution performed as part of a maintenance window execution.
      - **WindowExecutionId** *(string) --*

        The ID of the maintenance window execution that ran the task.
    """


_ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseTypeDef",
    {
        "WindowExecutionTaskInvocationIdentities": List[
            ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseWindowExecutionTaskInvocationIdentitiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseTypeDef(
    _ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowExecutionTaskInvocationIdentities** *(list) --*

        Information about the task invocation results per invocation.
        - *(dict) --*

          Describes the information about a task invocation for a particular target as part of a
          task execution performed as part of a maintenance window execution.
          - **WindowExecutionId** *(string) --*

            The ID of the maintenance window execution that ran the task.
    """


_ClientDescribeMaintenanceWindowExecutionTasksFiltersTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowExecutionTasksFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeMaintenanceWindowExecutionTasksFiltersTypeDef(
    _ClientDescribeMaintenanceWindowExecutionTasksFiltersTypeDef
):
    """
    - *(dict) --*

      Filter used in the request. Supported filter keys are Name and Enabled.
      - **Key** *(string) --*

        The name of the filter.
    """


_ClientDescribeMaintenanceWindowExecutionTasksResponseWindowExecutionTaskIdentitiesTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowExecutionTasksResponseWindowExecutionTaskIdentitiesTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "TaskArn": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
    },
    total=False,
)


class ClientDescribeMaintenanceWindowExecutionTasksResponseWindowExecutionTaskIdentitiesTypeDef(
    _ClientDescribeMaintenanceWindowExecutionTasksResponseWindowExecutionTaskIdentitiesTypeDef
):
    """
    - *(dict) --*

      Information about a task execution performed as part of a maintenance window execution.
      - **WindowExecutionId** *(string) --*

        The ID of the maintenance window execution that ran the task.
    """


_ClientDescribeMaintenanceWindowExecutionTasksResponseTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowExecutionTasksResponseTypeDef",
    {
        "WindowExecutionTaskIdentities": List[
            ClientDescribeMaintenanceWindowExecutionTasksResponseWindowExecutionTaskIdentitiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeMaintenanceWindowExecutionTasksResponseTypeDef(
    _ClientDescribeMaintenanceWindowExecutionTasksResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowExecutionTaskIdentities** *(list) --*

        Information about the task executions.
        - *(dict) --*

          Information about a task execution performed as part of a maintenance window execution.
          - **WindowExecutionId** *(string) --*

            The ID of the maintenance window execution that ran the task.
    """


_ClientDescribeMaintenanceWindowExecutionsFiltersTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowExecutionsFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeMaintenanceWindowExecutionsFiltersTypeDef(
    _ClientDescribeMaintenanceWindowExecutionsFiltersTypeDef
):
    """
    - *(dict) --*

      Filter used in the request. Supported filter keys are Name and Enabled.
      - **Key** *(string) --*

        The name of the filter.
    """


_ClientDescribeMaintenanceWindowExecutionsResponseWindowExecutionsTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowExecutionsResponseWindowExecutionsTypeDef",
    {
        "WindowId": str,
        "WindowExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)


class ClientDescribeMaintenanceWindowExecutionsResponseWindowExecutionsTypeDef(
    _ClientDescribeMaintenanceWindowExecutionsResponseWindowExecutionsTypeDef
):
    """
    - *(dict) --*

      Describes the information about an execution of a maintenance window.
      - **WindowId** *(string) --*

        The ID of the maintenance window.
    """


_ClientDescribeMaintenanceWindowExecutionsResponseTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowExecutionsResponseTypeDef",
    {
        "WindowExecutions": List[
            ClientDescribeMaintenanceWindowExecutionsResponseWindowExecutionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeMaintenanceWindowExecutionsResponseTypeDef(
    _ClientDescribeMaintenanceWindowExecutionsResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowExecutions** *(list) --*

        Information about the maintenance window executions.
        - *(dict) --*

          Describes the information about an execution of a maintenance window.
          - **WindowId** *(string) --*

            The ID of the maintenance window.
    """


_ClientDescribeMaintenanceWindowScheduleFiltersTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowScheduleFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeMaintenanceWindowScheduleFiltersTypeDef(
    _ClientDescribeMaintenanceWindowScheduleFiltersTypeDef
):
    """
    - *(dict) --*

      Defines a filter used in Patch Manager APIs.
      - **Key** *(string) --*

        The key for the filter.
    """


_ClientDescribeMaintenanceWindowScheduleResponseScheduledWindowExecutionsTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowScheduleResponseScheduledWindowExecutionsTypeDef",
    {"WindowId": str, "Name": str, "ExecutionTime": str},
    total=False,
)


class ClientDescribeMaintenanceWindowScheduleResponseScheduledWindowExecutionsTypeDef(
    _ClientDescribeMaintenanceWindowScheduleResponseScheduledWindowExecutionsTypeDef
):
    """
    - *(dict) --*

      Information about a scheduled execution for a maintenance window.
      - **WindowId** *(string) --*

        The ID of the maintenance window to be run.
    """


_ClientDescribeMaintenanceWindowScheduleResponseTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowScheduleResponseTypeDef",
    {
        "ScheduledWindowExecutions": List[
            ClientDescribeMaintenanceWindowScheduleResponseScheduledWindowExecutionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeMaintenanceWindowScheduleResponseTypeDef(
    _ClientDescribeMaintenanceWindowScheduleResponseTypeDef
):
    """
    - *(dict) --*

      - **ScheduledWindowExecutions** *(list) --*

        Information about maintenance window executions scheduled for the specified time range.
        - *(dict) --*

          Information about a scheduled execution for a maintenance window.
          - **WindowId** *(string) --*

            The ID of the maintenance window to be run.
    """


_ClientDescribeMaintenanceWindowScheduleTargetsTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowScheduleTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeMaintenanceWindowScheduleTargetsTypeDef(
    _ClientDescribeMaintenanceWindowScheduleTargetsTypeDef
):
    """
    - *(dict) --*

      An array of search criteria that targets instances using a Key,Value combination that you
      specify.
      Supported formats include the following.
      * ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
      * ``Key=tag:*my-tag-key* ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
      * ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
      * (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
      For example:
      * ``Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE``
      * ``Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3``
      * ``Key=tag-key,Values=Name,Instance-Type,CostCenter``
      * (Maintenance window targets only)
      ``Key=resource-groups:Name,Values=
          ProductionResourceGroup``   This example demonstrates how to
      target all resources in the resource group **ProductionResourceGroup** in your maintenance
      window.
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``
      This example demonstrates how to target only Amazon EC2 instances and VPCs in your maintenance
      window.
      * (State Manager association targets only) ``Key=InstanceIds,Values=*``   This example
      demonstrates how to target all managed instances in the AWS Region where the association was
      created.
      For information about how to send commands that target instances using ``Key,Value``
      parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet
      <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__
      in the *AWS Systems Manager User Guide* .
      - **Key** *(string) --*

        User-defined criteria for sending commands that target instances that meet the criteria.
    """


_ClientDescribeMaintenanceWindowTargetsFiltersTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowTargetsFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeMaintenanceWindowTargetsFiltersTypeDef(
    _ClientDescribeMaintenanceWindowTargetsFiltersTypeDef
):
    """
    - *(dict) --*

      Filter used in the request. Supported filter keys are Name and Enabled.
      - **Key** *(string) --*

        The name of the filter.
    """


_ClientDescribeMaintenanceWindowTargetsResponseTargetsTargetsTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowTargetsResponseTargetsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeMaintenanceWindowTargetsResponseTargetsTargetsTypeDef(
    _ClientDescribeMaintenanceWindowTargetsResponseTargetsTargetsTypeDef
):
    pass


_ClientDescribeMaintenanceWindowTargetsResponseTargetsTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowTargetsResponseTargetsTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResourceType": Literal["INSTANCE", "RESOURCE_GROUP"],
        "Targets": List[ClientDescribeMaintenanceWindowTargetsResponseTargetsTargetsTypeDef],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)


class ClientDescribeMaintenanceWindowTargetsResponseTargetsTypeDef(
    _ClientDescribeMaintenanceWindowTargetsResponseTargetsTypeDef
):
    """
    - *(dict) --*

      The target registered with the maintenance window.
      - **WindowId** *(string) --*

        The ID of the maintenance window to register the target with.
    """


_ClientDescribeMaintenanceWindowTargetsResponseTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowTargetsResponseTypeDef",
    {
        "Targets": List[ClientDescribeMaintenanceWindowTargetsResponseTargetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeMaintenanceWindowTargetsResponseTypeDef(
    _ClientDescribeMaintenanceWindowTargetsResponseTypeDef
):
    """
    - *(dict) --*

      - **Targets** *(list) --*

        Information about the targets in the maintenance window.
        - *(dict) --*

          The target registered with the maintenance window.
          - **WindowId** *(string) --*

            The ID of the maintenance window to register the target with.
    """


_ClientDescribeMaintenanceWindowTasksFiltersTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowTasksFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeMaintenanceWindowTasksFiltersTypeDef(
    _ClientDescribeMaintenanceWindowTasksFiltersTypeDef
):
    """
    - *(dict) --*

      Filter used in the request. Supported filter keys are Name and Enabled.
      - **Key** *(string) --*

        The name of the filter.
    """


_ClientDescribeMaintenanceWindowTasksResponseTasksLoggingInfoTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowTasksResponseTasksLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)


class ClientDescribeMaintenanceWindowTasksResponseTasksLoggingInfoTypeDef(
    _ClientDescribeMaintenanceWindowTasksResponseTasksLoggingInfoTypeDef
):
    pass


_ClientDescribeMaintenanceWindowTasksResponseTasksTargetsTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowTasksResponseTasksTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeMaintenanceWindowTasksResponseTasksTargetsTypeDef(
    _ClientDescribeMaintenanceWindowTasksResponseTasksTargetsTypeDef
):
    pass


_ClientDescribeMaintenanceWindowTasksResponseTasksTaskParametersTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowTasksResponseTasksTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeMaintenanceWindowTasksResponseTasksTaskParametersTypeDef(
    _ClientDescribeMaintenanceWindowTasksResponseTasksTaskParametersTypeDef
):
    pass


_ClientDescribeMaintenanceWindowTasksResponseTasksTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowTasksResponseTasksTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "TaskArn": str,
        "Type": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Targets": List[ClientDescribeMaintenanceWindowTasksResponseTasksTargetsTypeDef],
        "TaskParameters": Dict[
            str, ClientDescribeMaintenanceWindowTasksResponseTasksTaskParametersTypeDef
        ],
        "Priority": int,
        "LoggingInfo": ClientDescribeMaintenanceWindowTasksResponseTasksLoggingInfoTypeDef,
        "ServiceRoleArn": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)


class ClientDescribeMaintenanceWindowTasksResponseTasksTypeDef(
    _ClientDescribeMaintenanceWindowTasksResponseTasksTypeDef
):
    """
    - *(dict) --*

      Information about a task defined for a maintenance window.
      - **WindowId** *(string) --*

        The ID of the maintenance window where the task is registered.
    """


_ClientDescribeMaintenanceWindowTasksResponseTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowTasksResponseTypeDef",
    {"Tasks": List[ClientDescribeMaintenanceWindowTasksResponseTasksTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeMaintenanceWindowTasksResponseTypeDef(
    _ClientDescribeMaintenanceWindowTasksResponseTypeDef
):
    """
    - *(dict) --*

      - **Tasks** *(list) --*

        Information about the tasks in the maintenance window.
        - *(dict) --*

          Information about a task defined for a maintenance window.
          - **WindowId** *(string) --*

            The ID of the maintenance window where the task is registered.
    """


_ClientDescribeMaintenanceWindowsFiltersTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowsFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeMaintenanceWindowsFiltersTypeDef(
    _ClientDescribeMaintenanceWindowsFiltersTypeDef
):
    """
    - *(dict) --*

      Filter used in the request. Supported filter keys are Name and Enabled.
      - **Key** *(string) --*

        The name of the filter.
    """


_ClientDescribeMaintenanceWindowsForTargetResponseWindowIdentitiesTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowsForTargetResponseWindowIdentitiesTypeDef",
    {"WindowId": str, "Name": str},
    total=False,
)


class ClientDescribeMaintenanceWindowsForTargetResponseWindowIdentitiesTypeDef(
    _ClientDescribeMaintenanceWindowsForTargetResponseWindowIdentitiesTypeDef
):
    """
    - *(dict) --*

      The maintenance window to which the specified target belongs.
      - **WindowId** *(string) --*

        The ID of the maintenance window.
    """


_ClientDescribeMaintenanceWindowsForTargetResponseTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowsForTargetResponseTypeDef",
    {
        "WindowIdentities": List[
            ClientDescribeMaintenanceWindowsForTargetResponseWindowIdentitiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeMaintenanceWindowsForTargetResponseTypeDef(
    _ClientDescribeMaintenanceWindowsForTargetResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowIdentities** *(list) --*

        Information about the maintenance window targets and tasks an instance is associated with.
        - *(dict) --*

          The maintenance window to which the specified target belongs.
          - **WindowId** *(string) --*

            The ID of the maintenance window.
    """


_ClientDescribeMaintenanceWindowsForTargetTargetsTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowsForTargetTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeMaintenanceWindowsForTargetTargetsTypeDef(
    _ClientDescribeMaintenanceWindowsForTargetTargetsTypeDef
):
    """
    - *(dict) --*

      An array of search criteria that targets instances using a Key,Value combination that you
      specify.
      Supported formats include the following.
      * ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
      * ``Key=tag:*my-tag-key* ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
      * ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
      * (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
      For example:
      * ``Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE``
      * ``Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3``
      * ``Key=tag-key,Values=Name,Instance-Type,CostCenter``
      * (Maintenance window targets only)
      ``Key=resource-groups:Name,Values=
          ProductionResourceGroup``   This example demonstrates how to
      target all resources in the resource group **ProductionResourceGroup** in your maintenance
      window.
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``
      This example demonstrates how to target only Amazon EC2 instances and VPCs in your maintenance
      window.
      * (State Manager association targets only) ``Key=InstanceIds,Values=*``   This example
      demonstrates how to target all managed instances in the AWS Region where the association was
      created.
      For information about how to send commands that target instances using ``Key,Value``
      parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet
      <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__
      in the *AWS Systems Manager User Guide* .
      - **Key** *(string) --*

        User-defined criteria for sending commands that target instances that meet the criteria.
    """


_ClientDescribeMaintenanceWindowsResponseWindowIdentitiesTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowsResponseWindowIdentitiesTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "Enabled": bool,
        "Duration": int,
        "Cutoff": int,
        "Schedule": str,
        "ScheduleTimezone": str,
        "EndDate": str,
        "StartDate": str,
        "NextExecutionTime": str,
    },
    total=False,
)


class ClientDescribeMaintenanceWindowsResponseWindowIdentitiesTypeDef(
    _ClientDescribeMaintenanceWindowsResponseWindowIdentitiesTypeDef
):
    """
    - *(dict) --*

      Information about the maintenance window.
      - **WindowId** *(string) --*

        The ID of the maintenance window.
    """


_ClientDescribeMaintenanceWindowsResponseTypeDef = TypedDict(
    "_ClientDescribeMaintenanceWindowsResponseTypeDef",
    {
        "WindowIdentities": List[ClientDescribeMaintenanceWindowsResponseWindowIdentitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeMaintenanceWindowsResponseTypeDef(
    _ClientDescribeMaintenanceWindowsResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowIdentities** *(list) --*

        Information about the maintenance windows.
        - *(dict) --*

          Information about the maintenance window.
          - **WindowId** *(string) --*

            The ID of the maintenance window.
    """


_RequiredClientDescribeOpsItemsOpsItemFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeOpsItemsOpsItemFiltersTypeDef",
    {
        "Key": Literal[
            "Status",
            "CreatedBy",
            "Source",
            "Priority",
            "Title",
            "OpsItemId",
            "CreatedTime",
            "LastModifiedTime",
            "OperationalData",
            "OperationalDataKey",
            "OperationalDataValue",
            "ResourceId",
            "AutomationId",
            "Category",
            "Severity",
        ]
    },
)
_OptionalClientDescribeOpsItemsOpsItemFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeOpsItemsOpsItemFiltersTypeDef",
    {"Values": List[str], "Operator": Literal["Equal", "Contains", "GreaterThan", "LessThan"]},
    total=False,
)


class ClientDescribeOpsItemsOpsItemFiltersTypeDef(
    _RequiredClientDescribeOpsItemsOpsItemFiltersTypeDef,
    _OptionalClientDescribeOpsItemsOpsItemFiltersTypeDef,
):
    """
    - *(dict) --*

      Describes an OpsItem filter.
      - **Key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeOpsItemsResponseOpsItemSummariesOperationalDataTypeDef = TypedDict(
    "_ClientDescribeOpsItemsResponseOpsItemSummariesOperationalDataTypeDef",
    {"Value": str, "Type": Literal["SearchableString", "String"]},
    total=False,
)


class ClientDescribeOpsItemsResponseOpsItemSummariesOperationalDataTypeDef(
    _ClientDescribeOpsItemsResponseOpsItemSummariesOperationalDataTypeDef
):
    pass


_ClientDescribeOpsItemsResponseOpsItemSummariesTypeDef = TypedDict(
    "_ClientDescribeOpsItemsResponseOpsItemSummariesTypeDef",
    {
        "CreatedBy": str,
        "CreatedTime": datetime,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Priority": int,
        "Source": str,
        "Status": Literal["Open", "InProgress", "Resolved"],
        "OpsItemId": str,
        "Title": str,
        "OperationalData": Dict[
            str, ClientDescribeOpsItemsResponseOpsItemSummariesOperationalDataTypeDef
        ],
        "Category": str,
        "Severity": str,
    },
    total=False,
)


class ClientDescribeOpsItemsResponseOpsItemSummariesTypeDef(
    _ClientDescribeOpsItemsResponseOpsItemSummariesTypeDef
):
    pass


_ClientDescribeOpsItemsResponseTypeDef = TypedDict(
    "_ClientDescribeOpsItemsResponseTypeDef",
    {
        "NextToken": str,
        "OpsItemSummaries": List[ClientDescribeOpsItemsResponseOpsItemSummariesTypeDef],
    },
    total=False,
)


class ClientDescribeOpsItemsResponseTypeDef(_ClientDescribeOpsItemsResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        The token for the next set of items to return. Use this token to get the next set of
        results.
    """


_RequiredClientDescribeParametersFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeParametersFiltersTypeDef", {"Key": Literal["Name", "Type", "KeyId"]}
)
_OptionalClientDescribeParametersFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeParametersFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeParametersFiltersTypeDef(
    _RequiredClientDescribeParametersFiltersTypeDef, _OptionalClientDescribeParametersFiltersTypeDef
):
    """
    - *(dict) --*

      This data type is deprecated. Instead, use  ParameterStringFilter .
      - **Key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeParametersParameterFiltersTypeDef = TypedDict(
    "_ClientDescribeParametersParameterFiltersTypeDef",
    {"Key": str, "Option": str, "Values": List[str]},
    total=False,
)


class ClientDescribeParametersParameterFiltersTypeDef(
    _ClientDescribeParametersParameterFiltersTypeDef
):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of results.
      .. warning::

        The ``ParameterStringFilter`` object is used by the  DescribeParameters and
        GetParametersByPath API actions. However, not all of the pattern values listed for ``Key``
        can be used with both actions.
        For ``DescribeActions`` , all of the listed patterns are valid, with the exception of
        ``Label`` .
        For ``GetParametersByPath`` , the following patterns listed for ``Key`` are not valid:
        ``Name`` , ``Path`` , and ``Tier`` .
        For examples of CLI commands demonstrating valid parameter filter constructions, see
        `Searching for Systems Manager Parameters
        <http://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-search.html>`__ in
        the *AWS Systems Manager User Guide* .
    """


_ClientDescribeParametersResponseParametersPoliciesTypeDef = TypedDict(
    "_ClientDescribeParametersResponseParametersPoliciesTypeDef",
    {"PolicyText": str, "PolicyType": str, "PolicyStatus": str},
    total=False,
)


class ClientDescribeParametersResponseParametersPoliciesTypeDef(
    _ClientDescribeParametersResponseParametersPoliciesTypeDef
):
    pass


_ClientDescribeParametersResponseParametersTypeDef = TypedDict(
    "_ClientDescribeParametersResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "AllowedPattern": str,
        "Version": int,
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List[ClientDescribeParametersResponseParametersPoliciesTypeDef],
    },
    total=False,
)


class ClientDescribeParametersResponseParametersTypeDef(
    _ClientDescribeParametersResponseParametersTypeDef
):
    """
    - *(dict) --*

      Metadata includes information like the ARN of the last user and the date/time the parameter
      was last used.
      - **Name** *(string) --*

        The parameter name.
    """


_ClientDescribeParametersResponseTypeDef = TypedDict(
    "_ClientDescribeParametersResponseTypeDef",
    {"Parameters": List[ClientDescribeParametersResponseParametersTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeParametersResponseTypeDef(_ClientDescribeParametersResponseTypeDef):
    """
    - *(dict) --*

      - **Parameters** *(list) --*

        Parameters returned by the request.
        - *(dict) --*

          Metadata includes information like the ARN of the last user and the date/time the
          parameter was last used.
          - **Name** *(string) --*

            The parameter name.
    """


_ClientDescribePatchBaselinesFiltersTypeDef = TypedDict(
    "_ClientDescribePatchBaselinesFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientDescribePatchBaselinesFiltersTypeDef(_ClientDescribePatchBaselinesFiltersTypeDef):
    """
    - *(dict) --*

      Defines a filter used in Patch Manager APIs.
      - **Key** *(string) --*

        The key for the filter.
    """


_ClientDescribePatchBaselinesResponseBaselineIdentitiesTypeDef = TypedDict(
    "_ClientDescribePatchBaselinesResponseBaselineIdentitiesTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)


class ClientDescribePatchBaselinesResponseBaselineIdentitiesTypeDef(
    _ClientDescribePatchBaselinesResponseBaselineIdentitiesTypeDef
):
    """
    - *(dict) --*

      Defines the basic information about a patch baseline.
      - **BaselineId** *(string) --*

        The ID of the patch baseline.
    """


_ClientDescribePatchBaselinesResponseTypeDef = TypedDict(
    "_ClientDescribePatchBaselinesResponseTypeDef",
    {
        "BaselineIdentities": List[ClientDescribePatchBaselinesResponseBaselineIdentitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribePatchBaselinesResponseTypeDef(_ClientDescribePatchBaselinesResponseTypeDef):
    """
    - *(dict) --*

      - **BaselineIdentities** *(list) --*

        An array of PatchBaselineIdentity elements.
        - *(dict) --*

          Defines the basic information about a patch baseline.
          - **BaselineId** *(string) --*

            The ID of the patch baseline.
    """


_ClientDescribePatchGroupStateResponseTypeDef = TypedDict(
    "_ClientDescribePatchGroupStateResponseTypeDef",
    {
        "Instances": int,
        "InstancesWithInstalledPatches": int,
        "InstancesWithInstalledOtherPatches": int,
        "InstancesWithInstalledPendingRebootPatches": int,
        "InstancesWithInstalledRejectedPatches": int,
        "InstancesWithMissingPatches": int,
        "InstancesWithFailedPatches": int,
        "InstancesWithNotApplicablePatches": int,
        "InstancesWithUnreportedNotApplicablePatches": int,
    },
    total=False,
)


class ClientDescribePatchGroupStateResponseTypeDef(_ClientDescribePatchGroupStateResponseTypeDef):
    """
    - *(dict) --*

      - **Instances** *(integer) --*

        The number of instances in the patch group.
    """


_ClientDescribePatchGroupsFiltersTypeDef = TypedDict(
    "_ClientDescribePatchGroupsFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientDescribePatchGroupsFiltersTypeDef(_ClientDescribePatchGroupsFiltersTypeDef):
    """
    - *(dict) --*

      Defines a filter used in Patch Manager APIs.
      - **Key** *(string) --*

        The key for the filter.
    """


_ClientDescribePatchGroupsResponseMappingsBaselineIdentityTypeDef = TypedDict(
    "_ClientDescribePatchGroupsResponseMappingsBaselineIdentityTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)


class ClientDescribePatchGroupsResponseMappingsBaselineIdentityTypeDef(
    _ClientDescribePatchGroupsResponseMappingsBaselineIdentityTypeDef
):
    pass


_ClientDescribePatchGroupsResponseMappingsTypeDef = TypedDict(
    "_ClientDescribePatchGroupsResponseMappingsTypeDef",
    {
        "PatchGroup": str,
        "BaselineIdentity": ClientDescribePatchGroupsResponseMappingsBaselineIdentityTypeDef,
    },
    total=False,
)


class ClientDescribePatchGroupsResponseMappingsTypeDef(
    _ClientDescribePatchGroupsResponseMappingsTypeDef
):
    """
    - *(dict) --*

      The mapping between a patch group and the patch baseline the patch group is registered with.
      - **PatchGroup** *(string) --*

        The name of the patch group registered with the patch baseline.
    """


_ClientDescribePatchGroupsResponseTypeDef = TypedDict(
    "_ClientDescribePatchGroupsResponseTypeDef",
    {"Mappings": List[ClientDescribePatchGroupsResponseMappingsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribePatchGroupsResponseTypeDef(_ClientDescribePatchGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **Mappings** *(list) --*

        Each entry in the array contains:
        PatchGroup: string (between 1 and 256 characters, Regex:
        ^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$)
        PatchBaselineIdentity: A PatchBaselineIdentity element.
        - *(dict) --*

          The mapping between a patch group and the patch baseline the patch group is registered
          with.
          - **PatchGroup** *(string) --*

            The name of the patch group registered with the patch baseline.
    """


_ClientDescribePatchPropertiesResponseTypeDef = TypedDict(
    "_ClientDescribePatchPropertiesResponseTypeDef",
    {"Properties": List[Dict[str, str]], "NextToken": str},
    total=False,
)


class ClientDescribePatchPropertiesResponseTypeDef(_ClientDescribePatchPropertiesResponseTypeDef):
    """
    - *(dict) --*

      - **Properties** *(list) --*

        A list of the properties for patches matching the filter request parameters.
        - *(dict) --*

          - *(string) --*

            - *(string) --*
    """


_RequiredClientDescribeSessionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeSessionsFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Target", "Owner", "Status"]},
)
_OptionalClientDescribeSessionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeSessionsFiltersTypeDef", {"value": str}, total=False
)


class ClientDescribeSessionsFiltersTypeDef(
    _RequiredClientDescribeSessionsFiltersTypeDef, _OptionalClientDescribeSessionsFiltersTypeDef
):
    """
    - *(dict) --*

      Describes a filter for Session Manager information.
      - **key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeSessionsResponseSessionsOutputUrlTypeDef = TypedDict(
    "_ClientDescribeSessionsResponseSessionsOutputUrlTypeDef",
    {"S3OutputUrl": str, "CloudWatchOutputUrl": str},
    total=False,
)


class ClientDescribeSessionsResponseSessionsOutputUrlTypeDef(
    _ClientDescribeSessionsResponseSessionsOutputUrlTypeDef
):
    pass


_ClientDescribeSessionsResponseSessionsTypeDef = TypedDict(
    "_ClientDescribeSessionsResponseSessionsTypeDef",
    {
        "SessionId": str,
        "Target": str,
        "Status": Literal[
            "Connected", "Connecting", "Disconnected", "Terminated", "Terminating", "Failed"
        ],
        "StartDate": datetime,
        "EndDate": datetime,
        "DocumentName": str,
        "Owner": str,
        "Details": str,
        "OutputUrl": ClientDescribeSessionsResponseSessionsOutputUrlTypeDef,
    },
    total=False,
)


class ClientDescribeSessionsResponseSessionsTypeDef(_ClientDescribeSessionsResponseSessionsTypeDef):
    """
    - *(dict) --*

      Information about a Session Manager connection to an instance.
      - **SessionId** *(string) --*

        The ID of the session.
    """


_ClientDescribeSessionsResponseTypeDef = TypedDict(
    "_ClientDescribeSessionsResponseTypeDef",
    {"Sessions": List[ClientDescribeSessionsResponseSessionsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeSessionsResponseTypeDef(_ClientDescribeSessionsResponseTypeDef):
    """
    - *(dict) --*

      - **Sessions** *(list) --*

        A list of sessions meeting the request parameters.
        - *(dict) --*

          Information about a Session Manager connection to an instance.
          - **SessionId** *(string) --*

            The ID of the session.
    """


_ClientGetAutomationExecutionResponseAutomationExecutionProgressCountersTypeDef = TypedDict(
    "_ClientGetAutomationExecutionResponseAutomationExecutionProgressCountersTypeDef",
    {
        "TotalSteps": int,
        "SuccessSteps": int,
        "FailedSteps": int,
        "CancelledSteps": int,
        "TimedOutSteps": int,
    },
    total=False,
)


class ClientGetAutomationExecutionResponseAutomationExecutionProgressCountersTypeDef(
    _ClientGetAutomationExecutionResponseAutomationExecutionProgressCountersTypeDef
):
    pass


_ClientGetAutomationExecutionResponseAutomationExecutionResolvedTargetsTypeDef = TypedDict(
    "_ClientGetAutomationExecutionResponseAutomationExecutionResolvedTargetsTypeDef",
    {"ParameterValues": List[str], "Truncated": bool},
    total=False,
)


class ClientGetAutomationExecutionResponseAutomationExecutionResolvedTargetsTypeDef(
    _ClientGetAutomationExecutionResponseAutomationExecutionResolvedTargetsTypeDef
):
    pass


_ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsFailureDetailsTypeDef = TypedDict(
    "_ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsFailureDetailsTypeDef",
    {"FailureStage": str, "FailureType": str, "Details": Dict[str, List[str]]},
    total=False,
)


class ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsFailureDetailsTypeDef(
    _ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsFailureDetailsTypeDef
):
    pass


_ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetLocationTypeDef = TypedDict(
    "_ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetLocationTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)


class ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetLocationTypeDef(
    _ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetLocationTypeDef
):
    pass


_ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetsTypeDef = TypedDict(
    "_ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetsTypeDef(
    _ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetsTypeDef
):
    pass


_ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTypeDef = TypedDict(
    "_ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTypeDef",
    {
        "StepName": str,
        "Action": str,
        "TimeoutSeconds": int,
        "OnFailure": str,
        "MaxAttempts": int,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "StepStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ResponseCode": str,
        "Inputs": Dict[str, str],
        "Outputs": Dict[str, List[str]],
        "Response": str,
        "FailureMessage": str,
        "FailureDetails": ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsFailureDetailsTypeDef,
        "StepExecutionId": str,
        "OverriddenParameters": Dict[str, List[str]],
        "IsEnd": bool,
        "NextStep": str,
        "IsCritical": bool,
        "ValidNextSteps": List[str],
        "Targets": List[
            ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetsTypeDef
        ],
        "TargetLocation": ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetLocationTypeDef,
    },
    total=False,
)


class ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTypeDef(
    _ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTypeDef
):
    pass


_ClientGetAutomationExecutionResponseAutomationExecutionTargetLocationsTypeDef = TypedDict(
    "_ClientGetAutomationExecutionResponseAutomationExecutionTargetLocationsTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)


class ClientGetAutomationExecutionResponseAutomationExecutionTargetLocationsTypeDef(
    _ClientGetAutomationExecutionResponseAutomationExecutionTargetLocationsTypeDef
):
    pass


_ClientGetAutomationExecutionResponseAutomationExecutionTargetsTypeDef = TypedDict(
    "_ClientGetAutomationExecutionResponseAutomationExecutionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetAutomationExecutionResponseAutomationExecutionTargetsTypeDef(
    _ClientGetAutomationExecutionResponseAutomationExecutionTargetsTypeDef
):
    pass


_ClientGetAutomationExecutionResponseAutomationExecutionTypeDef = TypedDict(
    "_ClientGetAutomationExecutionResponseAutomationExecutionTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "AutomationExecutionStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "StepExecutions": List[
            ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTypeDef
        ],
        "StepExecutionsTruncated": bool,
        "Parameters": Dict[str, List[str]],
        "Outputs": Dict[str, List[str]],
        "FailureMessage": str,
        "Mode": Literal["Auto", "Interactive"],
        "ParentAutomationExecutionId": str,
        "ExecutedBy": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "TargetParameterName": str,
        "Targets": List[ClientGetAutomationExecutionResponseAutomationExecutionTargetsTypeDef],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": ClientGetAutomationExecutionResponseAutomationExecutionResolvedTargetsTypeDef,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "TargetLocations": List[
            ClientGetAutomationExecutionResponseAutomationExecutionTargetLocationsTypeDef
        ],
        "ProgressCounters": ClientGetAutomationExecutionResponseAutomationExecutionProgressCountersTypeDef,
    },
    total=False,
)


class ClientGetAutomationExecutionResponseAutomationExecutionTypeDef(
    _ClientGetAutomationExecutionResponseAutomationExecutionTypeDef
):
    """
    - **AutomationExecution** *(dict) --*

      Detailed information about the current state of an automation execution.
      - **AutomationExecutionId** *(string) --*

        The execution ID.
    """


_ClientGetAutomationExecutionResponseTypeDef = TypedDict(
    "_ClientGetAutomationExecutionResponseTypeDef",
    {"AutomationExecution": ClientGetAutomationExecutionResponseAutomationExecutionTypeDef},
    total=False,
)


class ClientGetAutomationExecutionResponseTypeDef(_ClientGetAutomationExecutionResponseTypeDef):
    """
    - *(dict) --*

      - **AutomationExecution** *(dict) --*

        Detailed information about the current state of an automation execution.
        - **AutomationExecutionId** *(string) --*

          The execution ID.
    """


_ClientGetCommandInvocationResponseCloudWatchOutputConfigTypeDef = TypedDict(
    "_ClientGetCommandInvocationResponseCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)


class ClientGetCommandInvocationResponseCloudWatchOutputConfigTypeDef(
    _ClientGetCommandInvocationResponseCloudWatchOutputConfigTypeDef
):
    pass


_ClientGetCommandInvocationResponseTypeDef = TypedDict(
    "_ClientGetCommandInvocationResponseTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "PluginName": str,
        "ResponseCode": int,
        "ExecutionStartDateTime": str,
        "ExecutionElapsedTime": str,
        "ExecutionEndDateTime": str,
        "Status": Literal[
            "Pending",
            "InProgress",
            "Delayed",
            "Success",
            "Cancelled",
            "TimedOut",
            "Failed",
            "Cancelling",
        ],
        "StatusDetails": str,
        "StandardOutputContent": str,
        "StandardOutputUrl": str,
        "StandardErrorContent": str,
        "StandardErrorUrl": str,
        "CloudWatchOutputConfig": ClientGetCommandInvocationResponseCloudWatchOutputConfigTypeDef,
    },
    total=False,
)


class ClientGetCommandInvocationResponseTypeDef(_ClientGetCommandInvocationResponseTypeDef):
    """
    - *(dict) --*

      - **CommandId** *(string) --*

        The parent command ID of the invocation plugin.
    """


_ClientGetConnectionStatusResponseTypeDef = TypedDict(
    "_ClientGetConnectionStatusResponseTypeDef",
    {"Target": str, "Status": Literal["Connected", "NotConnected"]},
    total=False,
)


class ClientGetConnectionStatusResponseTypeDef(_ClientGetConnectionStatusResponseTypeDef):
    """
    - *(dict) --*

      - **Target** *(string) --*

        The ID of the instance to check connection status.
    """


_ClientGetDefaultPatchBaselineResponseTypeDef = TypedDict(
    "_ClientGetDefaultPatchBaselineResponseTypeDef",
    {
        "BaselineId": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
    },
    total=False,
)


class ClientGetDefaultPatchBaselineResponseTypeDef(_ClientGetDefaultPatchBaselineResponseTypeDef):
    """
    - *(dict) --*

      - **BaselineId** *(string) --*

        The ID of the default patch baseline.
    """


_ClientGetDeployablePatchSnapshotForInstanceResponseTypeDef = TypedDict(
    "_ClientGetDeployablePatchSnapshotForInstanceResponseTypeDef",
    {"InstanceId": str, "SnapshotId": str, "SnapshotDownloadUrl": str, "Product": str},
    total=False,
)


class ClientGetDeployablePatchSnapshotForInstanceResponseTypeDef(
    _ClientGetDeployablePatchSnapshotForInstanceResponseTypeDef
):
    """
    - *(dict) --*

      - **InstanceId** *(string) --*

        The ID of the instance.
    """


_ClientGetDocumentResponseAttachmentsContentTypeDef = TypedDict(
    "_ClientGetDocumentResponseAttachmentsContentTypeDef",
    {"Name": str, "Size": int, "Hash": str, "HashType": str, "Url": str},
    total=False,
)


class ClientGetDocumentResponseAttachmentsContentTypeDef(
    _ClientGetDocumentResponseAttachmentsContentTypeDef
):
    pass


_ClientGetDocumentResponseRequiresTypeDef = TypedDict(
    "_ClientGetDocumentResponseRequiresTypeDef", {"Name": str, "Version": str}, total=False
)


class ClientGetDocumentResponseRequiresTypeDef(_ClientGetDocumentResponseRequiresTypeDef):
    pass


_ClientGetDocumentResponseTypeDef = TypedDict(
    "_ClientGetDocumentResponseTypeDef",
    {
        "Name": str,
        "VersionName": str,
        "DocumentVersion": str,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "Content": str,
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
        ],
        "DocumentFormat": Literal["YAML", "JSON"],
        "Requires": List[ClientGetDocumentResponseRequiresTypeDef],
        "AttachmentsContent": List[ClientGetDocumentResponseAttachmentsContentTypeDef],
    },
    total=False,
)


class ClientGetDocumentResponseTypeDef(_ClientGetDocumentResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the Systems Manager document.
    """


_ClientGetInventoryAggregatorsGroupsFiltersTypeDef = TypedDict(
    "_ClientGetInventoryAggregatorsGroupsFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class ClientGetInventoryAggregatorsGroupsFiltersTypeDef(
    _ClientGetInventoryAggregatorsGroupsFiltersTypeDef
):
    pass


_ClientGetInventoryAggregatorsGroupsTypeDef = TypedDict(
    "_ClientGetInventoryAggregatorsGroupsTypeDef",
    {"Name": str, "Filters": List[ClientGetInventoryAggregatorsGroupsFiltersTypeDef]},
    total=False,
)


class ClientGetInventoryAggregatorsGroupsTypeDef(_ClientGetInventoryAggregatorsGroupsTypeDef):
    pass


_ClientGetInventoryAggregatorsTypeDef = TypedDict(
    "_ClientGetInventoryAggregatorsTypeDef",
    {
        "Expression": str,
        "Aggregators": Any,
        "Groups": List[ClientGetInventoryAggregatorsGroupsTypeDef],
    },
    total=False,
)


class ClientGetInventoryAggregatorsTypeDef(_ClientGetInventoryAggregatorsTypeDef):
    """
    - *(dict) --*

      Specifies the inventory type and attribute for the aggregation execution.
      - **Expression** *(string) --*

        The inventory type and attribute name for aggregation.
    """


_RequiredClientGetInventoryFiltersTypeDef = TypedDict(
    "_RequiredClientGetInventoryFiltersTypeDef", {"Key": str}
)
_OptionalClientGetInventoryFiltersTypeDef = TypedDict(
    "_OptionalClientGetInventoryFiltersTypeDef",
    {
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class ClientGetInventoryFiltersTypeDef(
    _RequiredClientGetInventoryFiltersTypeDef, _OptionalClientGetInventoryFiltersTypeDef
):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of results.
      - **Key** *(string) --***[REQUIRED]**

        The name of the filter key.
    """


_ClientGetInventoryResponseEntitiesDataTypeDef = TypedDict(
    "_ClientGetInventoryResponseEntitiesDataTypeDef",
    {
        "TypeName": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "ContentHash": str,
        "Content": List[Dict[str, str]],
    },
    total=False,
)


class ClientGetInventoryResponseEntitiesDataTypeDef(_ClientGetInventoryResponseEntitiesDataTypeDef):
    pass


_ClientGetInventoryResponseEntitiesTypeDef = TypedDict(
    "_ClientGetInventoryResponseEntitiesTypeDef",
    {"Id": str, "Data": Dict[str, ClientGetInventoryResponseEntitiesDataTypeDef]},
    total=False,
)


class ClientGetInventoryResponseEntitiesTypeDef(_ClientGetInventoryResponseEntitiesTypeDef):
    """
    - *(dict) --*

      Inventory query results.
      - **Id** *(string) --*

        ID of the inventory result entity. For example, for managed instance inventory the result
        will be the managed instance ID. For EC2 instance inventory, the result will be the instance
        ID.
    """


_ClientGetInventoryResponseTypeDef = TypedDict(
    "_ClientGetInventoryResponseTypeDef",
    {"Entities": List[ClientGetInventoryResponseEntitiesTypeDef], "NextToken": str},
    total=False,
)


class ClientGetInventoryResponseTypeDef(_ClientGetInventoryResponseTypeDef):
    """
    - *(dict) --*

      - **Entities** *(list) --*

        Collection of inventory entities such as a collection of instance inventory.
        - *(dict) --*

          Inventory query results.
          - **Id** *(string) --*

            ID of the inventory result entity. For example, for managed instance inventory the
            result will be the managed instance ID. For EC2 instance inventory, the result will be
            the instance ID.
    """


_ClientGetInventoryResultAttributesTypeDef = TypedDict(
    "_ClientGetInventoryResultAttributesTypeDef", {"TypeName": str}
)


class ClientGetInventoryResultAttributesTypeDef(_ClientGetInventoryResultAttributesTypeDef):
    """
    - *(dict) --*

      The inventory item result attribute.
      - **TypeName** *(string) --***[REQUIRED]**

        Name of the inventory item type. Valid value: AWS:InstanceInformation. Default Value:
        AWS:InstanceInformation.
    """


_ClientGetInventorySchemaResponseSchemasAttributesTypeDef = TypedDict(
    "_ClientGetInventorySchemaResponseSchemasAttributesTypeDef",
    {"Name": str, "DataType": Literal["string", "number"]},
    total=False,
)


class ClientGetInventorySchemaResponseSchemasAttributesTypeDef(
    _ClientGetInventorySchemaResponseSchemasAttributesTypeDef
):
    pass


_ClientGetInventorySchemaResponseSchemasTypeDef = TypedDict(
    "_ClientGetInventorySchemaResponseSchemasTypeDef",
    {
        "TypeName": str,
        "Version": str,
        "Attributes": List[ClientGetInventorySchemaResponseSchemasAttributesTypeDef],
        "DisplayName": str,
    },
    total=False,
)


class ClientGetInventorySchemaResponseSchemasTypeDef(
    _ClientGetInventorySchemaResponseSchemasTypeDef
):
    """
    - *(dict) --*

      The inventory item schema definition. Users can use this to compose inventory query filters.
      - **TypeName** *(string) --*

        The name of the inventory type. Default inventory item type names start with AWS. Custom
        inventory type names will start with Custom. Default inventory item types include the
        following: AWS:AWSComponent, AWS:Application, AWS:InstanceInformation, AWS:Network, and
        AWS:WindowsUpdate.
    """


_ClientGetInventorySchemaResponseTypeDef = TypedDict(
    "_ClientGetInventorySchemaResponseTypeDef",
    {"Schemas": List[ClientGetInventorySchemaResponseSchemasTypeDef], "NextToken": str},
    total=False,
)


class ClientGetInventorySchemaResponseTypeDef(_ClientGetInventorySchemaResponseTypeDef):
    """
    - *(dict) --*

      - **Schemas** *(list) --*

        Inventory schemas returned by the request.
        - *(dict) --*

          The inventory item schema definition. Users can use this to compose inventory query
          filters.
          - **TypeName** *(string) --*

            The name of the inventory type. Default inventory item type names start with AWS. Custom
            inventory type names will start with Custom. Default inventory item types include the
            following: AWS:AWSComponent, AWS:Application, AWS:InstanceInformation, AWS:Network, and
            AWS:WindowsUpdate.
    """


_ClientGetMaintenanceWindowExecutionResponseTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowExecutionResponseTypeDef",
    {
        "WindowExecutionId": str,
        "TaskIds": List[str],
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)


class ClientGetMaintenanceWindowExecutionResponseTypeDef(
    _ClientGetMaintenanceWindowExecutionResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowExecutionId** *(string) --*

        The ID of the maintenance window execution.
    """


_ClientGetMaintenanceWindowExecutionTaskInvocationResponseTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowExecutionTaskInvocationResponseTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Parameters": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)


class ClientGetMaintenanceWindowExecutionTaskInvocationResponseTypeDef(
    _ClientGetMaintenanceWindowExecutionTaskInvocationResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowExecutionId** *(string) --*

        The maintenance window execution ID.
    """


_ClientGetMaintenanceWindowExecutionTaskResponseTaskParametersTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowExecutionTaskResponseTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientGetMaintenanceWindowExecutionTaskResponseTaskParametersTypeDef(
    _ClientGetMaintenanceWindowExecutionTaskResponseTaskParametersTypeDef
):
    pass


_ClientGetMaintenanceWindowExecutionTaskResponseTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowExecutionTaskResponseTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "TaskArn": str,
        "ServiceRole": str,
        "Type": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "TaskParameters": List[
            Dict[str, ClientGetMaintenanceWindowExecutionTaskResponseTaskParametersTypeDef]
        ],
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)


class ClientGetMaintenanceWindowExecutionTaskResponseTypeDef(
    _ClientGetMaintenanceWindowExecutionTaskResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowExecutionId** *(string) --*

        The ID of the maintenance window execution that includes the task.
    """


_ClientGetMaintenanceWindowResponseTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowResponseTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "NextExecutionTime": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
    },
    total=False,
)


class ClientGetMaintenanceWindowResponseTypeDef(_ClientGetMaintenanceWindowResponseTypeDef):
    """
    - *(dict) --*

      - **WindowId** *(string) --*

        The ID of the created maintenance window.
    """


_ClientGetMaintenanceWindowTaskResponseLoggingInfoTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowTaskResponseLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)


class ClientGetMaintenanceWindowTaskResponseLoggingInfoTypeDef(
    _ClientGetMaintenanceWindowTaskResponseLoggingInfoTypeDef
):
    pass


_ClientGetMaintenanceWindowTaskResponseTargetsTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowTaskResponseTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetMaintenanceWindowTaskResponseTargetsTypeDef(
    _ClientGetMaintenanceWindowTaskResponseTargetsTypeDef
):
    pass


_ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)


class ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef(
    _ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef
):
    pass


_ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": bytes},
    total=False,
)


class ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef(
    _ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef
):
    pass


_ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)


class ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef(
    _ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef
):
    pass


_ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef",
    {
        "Comment": str,
        "DocumentHash": str,
        "DocumentHashType": Literal["Sha256", "Sha1"],
        "NotificationConfig": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)


class ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef(
    _ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef
):
    pass


_ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef",
    {"Input": str, "Name": str},
    total=False,
)


class ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef(
    _ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef
):
    pass


_ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef",
    {
        "RunCommand": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef,
        "Automation": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef,
        "StepFunctions": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef,
        "Lambda": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef,
    },
    total=False,
)


class ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef(
    _ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef
):
    pass


_ClientGetMaintenanceWindowTaskResponseTaskParametersTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowTaskResponseTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientGetMaintenanceWindowTaskResponseTaskParametersTypeDef(
    _ClientGetMaintenanceWindowTaskResponseTaskParametersTypeDef
):
    pass


_ClientGetMaintenanceWindowTaskResponseTypeDef = TypedDict(
    "_ClientGetMaintenanceWindowTaskResponseTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List[ClientGetMaintenanceWindowTaskResponseTargetsTypeDef],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "TaskParameters": Dict[str, ClientGetMaintenanceWindowTaskResponseTaskParametersTypeDef],
        "TaskInvocationParameters": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef,
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": ClientGetMaintenanceWindowTaskResponseLoggingInfoTypeDef,
        "Name": str,
        "Description": str,
    },
    total=False,
)


class ClientGetMaintenanceWindowTaskResponseTypeDef(_ClientGetMaintenanceWindowTaskResponseTypeDef):
    """
    - *(dict) --*

      - **WindowId** *(string) --*

        The retrieved maintenance window ID.
    """


_ClientGetOpsItemResponseOpsItemNotificationsTypeDef = TypedDict(
    "_ClientGetOpsItemResponseOpsItemNotificationsTypeDef", {"Arn": str}, total=False
)


class ClientGetOpsItemResponseOpsItemNotificationsTypeDef(
    _ClientGetOpsItemResponseOpsItemNotificationsTypeDef
):
    pass


_ClientGetOpsItemResponseOpsItemOperationalDataTypeDef = TypedDict(
    "_ClientGetOpsItemResponseOpsItemOperationalDataTypeDef",
    {"Value": str, "Type": Literal["SearchableString", "String"]},
    total=False,
)


class ClientGetOpsItemResponseOpsItemOperationalDataTypeDef(
    _ClientGetOpsItemResponseOpsItemOperationalDataTypeDef
):
    pass


_ClientGetOpsItemResponseOpsItemRelatedOpsItemsTypeDef = TypedDict(
    "_ClientGetOpsItemResponseOpsItemRelatedOpsItemsTypeDef", {"OpsItemId": str}, total=False
)


class ClientGetOpsItemResponseOpsItemRelatedOpsItemsTypeDef(
    _ClientGetOpsItemResponseOpsItemRelatedOpsItemsTypeDef
):
    pass


_ClientGetOpsItemResponseOpsItemTypeDef = TypedDict(
    "_ClientGetOpsItemResponseOpsItemTypeDef",
    {
        "CreatedBy": str,
        "CreatedTime": datetime,
        "Description": str,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Notifications": List[ClientGetOpsItemResponseOpsItemNotificationsTypeDef],
        "Priority": int,
        "RelatedOpsItems": List[ClientGetOpsItemResponseOpsItemRelatedOpsItemsTypeDef],
        "Status": Literal["Open", "InProgress", "Resolved"],
        "OpsItemId": str,
        "Version": str,
        "Title": str,
        "Source": str,
        "OperationalData": Dict[str, ClientGetOpsItemResponseOpsItemOperationalDataTypeDef],
        "Category": str,
        "Severity": str,
    },
    total=False,
)


class ClientGetOpsItemResponseOpsItemTypeDef(_ClientGetOpsItemResponseOpsItemTypeDef):
    """
    - **OpsItem** *(dict) --*

      The OpsItem.
      - **CreatedBy** *(string) --*

        The ARN of the AWS account that created the OpsItem.
    """


_ClientGetOpsItemResponseTypeDef = TypedDict(
    "_ClientGetOpsItemResponseTypeDef",
    {"OpsItem": ClientGetOpsItemResponseOpsItemTypeDef},
    total=False,
)


class ClientGetOpsItemResponseTypeDef(_ClientGetOpsItemResponseTypeDef):
    """
    - *(dict) --*

      - **OpsItem** *(dict) --*

        The OpsItem.
        - **CreatedBy** *(string) --*

          The ARN of the AWS account that created the OpsItem.
    """


_ClientGetOpsSummaryAggregatorsFiltersTypeDef = TypedDict(
    "_ClientGetOpsSummaryAggregatorsFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class ClientGetOpsSummaryAggregatorsFiltersTypeDef(_ClientGetOpsSummaryAggregatorsFiltersTypeDef):
    pass


_ClientGetOpsSummaryAggregatorsTypeDef = TypedDict(
    "_ClientGetOpsSummaryAggregatorsTypeDef",
    {
        "AggregatorType": str,
        "TypeName": str,
        "AttributeName": str,
        "Values": Dict[str, str],
        "Filters": List[ClientGetOpsSummaryAggregatorsFiltersTypeDef],
        "Aggregators": Any,
    },
    total=False,
)


class ClientGetOpsSummaryAggregatorsTypeDef(_ClientGetOpsSummaryAggregatorsTypeDef):
    """
    - *(dict) --*

      One or more aggregators for viewing counts of OpsItems using different dimensions such as
      ``Source`` , ``CreatedTime`` , or ``Source and CreatedTime`` , to name a few.
      - **AggregatorType** *(string) --*

        Either a Range or Count aggregator for limiting an OpsItem summary.
    """


_RequiredClientGetOpsSummaryFiltersTypeDef = TypedDict(
    "_RequiredClientGetOpsSummaryFiltersTypeDef", {"Key": str}
)
_OptionalClientGetOpsSummaryFiltersTypeDef = TypedDict(
    "_OptionalClientGetOpsSummaryFiltersTypeDef",
    {
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class ClientGetOpsSummaryFiltersTypeDef(
    _RequiredClientGetOpsSummaryFiltersTypeDef, _OptionalClientGetOpsSummaryFiltersTypeDef
):
    """
    - *(dict) --*

      A filter for viewing OpsItem summaries.
      - **Key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientGetOpsSummaryResponseEntitiesDataTypeDef = TypedDict(
    "_ClientGetOpsSummaryResponseEntitiesDataTypeDef",
    {"CaptureTime": str, "Content": List[Dict[str, str]]},
    total=False,
)


class ClientGetOpsSummaryResponseEntitiesDataTypeDef(
    _ClientGetOpsSummaryResponseEntitiesDataTypeDef
):
    pass


_ClientGetOpsSummaryResponseEntitiesTypeDef = TypedDict(
    "_ClientGetOpsSummaryResponseEntitiesTypeDef",
    {"Id": str, "Data": Dict[str, ClientGetOpsSummaryResponseEntitiesDataTypeDef]},
    total=False,
)


class ClientGetOpsSummaryResponseEntitiesTypeDef(_ClientGetOpsSummaryResponseEntitiesTypeDef):
    """
    - *(dict) --*

      The result of the query.
      - **Id** *(string) --*

        The query ID.
    """


_ClientGetOpsSummaryResponseTypeDef = TypedDict(
    "_ClientGetOpsSummaryResponseTypeDef",
    {"Entities": List[ClientGetOpsSummaryResponseEntitiesTypeDef], "NextToken": str},
    total=False,
)


class ClientGetOpsSummaryResponseTypeDef(_ClientGetOpsSummaryResponseTypeDef):
    """
    - *(dict) --*

      - **Entities** *(list) --*

        The list of aggregated and filtered OpsItems.
        - *(dict) --*

          The result of the query.
          - **Id** *(string) --*

            The query ID.
    """


_ClientGetOpsSummaryResultAttributesTypeDef = TypedDict(
    "_ClientGetOpsSummaryResultAttributesTypeDef", {"TypeName": str}
)


class ClientGetOpsSummaryResultAttributesTypeDef(_ClientGetOpsSummaryResultAttributesTypeDef):
    """
    - *(dict) --*

      The OpsItem data type to return.
      - **TypeName** *(string) --***[REQUIRED]**

        Name of the data type. Valid value: AWS:OpsItem, AWS:EC2InstanceInformation,
        AWS:OpsItemTrendline, or AWS:ComplianceSummary.
    """


_ClientGetParameterHistoryResponseParametersPoliciesTypeDef = TypedDict(
    "_ClientGetParameterHistoryResponseParametersPoliciesTypeDef",
    {"PolicyText": str, "PolicyType": str, "PolicyStatus": str},
    total=False,
)


class ClientGetParameterHistoryResponseParametersPoliciesTypeDef(
    _ClientGetParameterHistoryResponseParametersPoliciesTypeDef
):
    pass


_ClientGetParameterHistoryResponseParametersTypeDef = TypedDict(
    "_ClientGetParameterHistoryResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "Value": str,
        "AllowedPattern": str,
        "Version": int,
        "Labels": List[str],
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List[ClientGetParameterHistoryResponseParametersPoliciesTypeDef],
    },
    total=False,
)


class ClientGetParameterHistoryResponseParametersTypeDef(
    _ClientGetParameterHistoryResponseParametersTypeDef
):
    """
    - *(dict) --*

      Information about parameter usage.
      - **Name** *(string) --*

        The name of the parameter.
    """


_ClientGetParameterHistoryResponseTypeDef = TypedDict(
    "_ClientGetParameterHistoryResponseTypeDef",
    {"Parameters": List[ClientGetParameterHistoryResponseParametersTypeDef], "NextToken": str},
    total=False,
)


class ClientGetParameterHistoryResponseTypeDef(_ClientGetParameterHistoryResponseTypeDef):
    """
    - *(dict) --*

      - **Parameters** *(list) --*

        A list of parameters returned by the request.
        - *(dict) --*

          Information about parameter usage.
          - **Name** *(string) --*

            The name of the parameter.
    """


_ClientGetParameterResponseParameterTypeDef = TypedDict(
    "_ClientGetParameterResponseParameterTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
    },
    total=False,
)


class ClientGetParameterResponseParameterTypeDef(_ClientGetParameterResponseParameterTypeDef):
    """
    - **Parameter** *(dict) --*

      Information about a parameter.
      - **Name** *(string) --*

        The name of the parameter.
    """


_ClientGetParameterResponseTypeDef = TypedDict(
    "_ClientGetParameterResponseTypeDef",
    {"Parameter": ClientGetParameterResponseParameterTypeDef},
    total=False,
)


class ClientGetParameterResponseTypeDef(_ClientGetParameterResponseTypeDef):
    """
    - *(dict) --*

      - **Parameter** *(dict) --*

        Information about a parameter.
        - **Name** *(string) --*

          The name of the parameter.
    """


_ClientGetParametersByPathParameterFiltersTypeDef = TypedDict(
    "_ClientGetParametersByPathParameterFiltersTypeDef",
    {"Key": str, "Option": str, "Values": List[str]},
    total=False,
)


class ClientGetParametersByPathParameterFiltersTypeDef(
    _ClientGetParametersByPathParameterFiltersTypeDef
):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of results.
      .. warning::

        The ``ParameterStringFilter`` object is used by the  DescribeParameters and
        GetParametersByPath API actions. However, not all of the pattern values listed for ``Key``
        can be used with both actions.
        For ``DescribeActions`` , all of the listed patterns are valid, with the exception of
        ``Label`` .
        For ``GetParametersByPath`` , the following patterns listed for ``Key`` are not valid:
        ``Name`` , ``Path`` , and ``Tier`` .
        For examples of CLI commands demonstrating valid parameter filter constructions, see
        `Searching for Systems Manager Parameters
        <http://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-search.html>`__ in
        the *AWS Systems Manager User Guide* .
    """


_ClientGetParametersByPathResponseParametersTypeDef = TypedDict(
    "_ClientGetParametersByPathResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
    },
    total=False,
)


class ClientGetParametersByPathResponseParametersTypeDef(
    _ClientGetParametersByPathResponseParametersTypeDef
):
    """
    - *(dict) --*

      An Amazon EC2 Systems Manager parameter in Parameter Store.
      - **Name** *(string) --*

        The name of the parameter.
    """


_ClientGetParametersByPathResponseTypeDef = TypedDict(
    "_ClientGetParametersByPathResponseTypeDef",
    {"Parameters": List[ClientGetParametersByPathResponseParametersTypeDef], "NextToken": str},
    total=False,
)


class ClientGetParametersByPathResponseTypeDef(_ClientGetParametersByPathResponseTypeDef):
    """
    - *(dict) --*

      - **Parameters** *(list) --*

        A list of parameters found in the specified hierarchy.
        - *(dict) --*

          An Amazon EC2 Systems Manager parameter in Parameter Store.
          - **Name** *(string) --*

            The name of the parameter.
    """


_ClientGetParametersResponseParametersTypeDef = TypedDict(
    "_ClientGetParametersResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
    },
    total=False,
)


class ClientGetParametersResponseParametersTypeDef(_ClientGetParametersResponseParametersTypeDef):
    """
    - *(dict) --*

      An Amazon EC2 Systems Manager parameter in Parameter Store.
      - **Name** *(string) --*

        The name of the parameter.
    """


_ClientGetParametersResponseTypeDef = TypedDict(
    "_ClientGetParametersResponseTypeDef",
    {
        "Parameters": List[ClientGetParametersResponseParametersTypeDef],
        "InvalidParameters": List[str],
    },
    total=False,
)


class ClientGetParametersResponseTypeDef(_ClientGetParametersResponseTypeDef):
    """
    - *(dict) --*

      - **Parameters** *(list) --*

        A list of details for a parameter.
        - *(dict) --*

          An Amazon EC2 Systems Manager parameter in Parameter Store.
          - **Name** *(string) --*

            The name of the parameter.
    """


_ClientGetPatchBaselineForPatchGroupResponseTypeDef = TypedDict(
    "_ClientGetPatchBaselineForPatchGroupResponseTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
    },
    total=False,
)


class ClientGetPatchBaselineForPatchGroupResponseTypeDef(
    _ClientGetPatchBaselineForPatchGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **BaselineId** *(string) --*

        The ID of the patch baseline that should be used for the patch group.
    """


_ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef(
    _ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
):
    pass


_ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef = TypedDict(
    "_ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    {
        "PatchFilters": List[
            ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
        ]
    },
    total=False,
)


class ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef(
    _ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef
):
    pass


_ClientGetPatchBaselineResponseApprovalRulesPatchRulesTypeDef = TypedDict(
    "_ClientGetPatchBaselineResponseApprovalRulesPatchRulesTypeDef",
    {
        "PatchFilterGroup": ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef,
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApproveAfterDays": int,
        "EnableNonSecurity": bool,
    },
    total=False,
)


class ClientGetPatchBaselineResponseApprovalRulesPatchRulesTypeDef(
    _ClientGetPatchBaselineResponseApprovalRulesPatchRulesTypeDef
):
    pass


_ClientGetPatchBaselineResponseApprovalRulesTypeDef = TypedDict(
    "_ClientGetPatchBaselineResponseApprovalRulesTypeDef",
    {"PatchRules": List[ClientGetPatchBaselineResponseApprovalRulesPatchRulesTypeDef]},
    total=False,
)


class ClientGetPatchBaselineResponseApprovalRulesTypeDef(
    _ClientGetPatchBaselineResponseApprovalRulesTypeDef
):
    pass


_ClientGetPatchBaselineResponseGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_ClientGetPatchBaselineResponseGlobalFiltersPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientGetPatchBaselineResponseGlobalFiltersPatchFiltersTypeDef(
    _ClientGetPatchBaselineResponseGlobalFiltersPatchFiltersTypeDef
):
    pass


_ClientGetPatchBaselineResponseGlobalFiltersTypeDef = TypedDict(
    "_ClientGetPatchBaselineResponseGlobalFiltersTypeDef",
    {"PatchFilters": List[ClientGetPatchBaselineResponseGlobalFiltersPatchFiltersTypeDef]},
    total=False,
)


class ClientGetPatchBaselineResponseGlobalFiltersTypeDef(
    _ClientGetPatchBaselineResponseGlobalFiltersTypeDef
):
    pass


_ClientGetPatchBaselineResponseSourcesTypeDef = TypedDict(
    "_ClientGetPatchBaselineResponseSourcesTypeDef",
    {"Name": str, "Products": List[str], "Configuration": str},
    total=False,
)


class ClientGetPatchBaselineResponseSourcesTypeDef(_ClientGetPatchBaselineResponseSourcesTypeDef):
    pass


_ClientGetPatchBaselineResponseTypeDef = TypedDict(
    "_ClientGetPatchBaselineResponseTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "GlobalFilters": ClientGetPatchBaselineResponseGlobalFiltersTypeDef,
        "ApprovalRules": ClientGetPatchBaselineResponseApprovalRulesTypeDef,
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": Literal["ALLOW_AS_DEPENDENCY", "BLOCK"],
        "PatchGroups": List[str],
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List[ClientGetPatchBaselineResponseSourcesTypeDef],
    },
    total=False,
)


class ClientGetPatchBaselineResponseTypeDef(_ClientGetPatchBaselineResponseTypeDef):
    """
    - *(dict) --*

      - **BaselineId** *(string) --*

        The ID of the retrieved patch baseline.
    """


_ClientGetServiceSettingResponseServiceSettingTypeDef = TypedDict(
    "_ClientGetServiceSettingResponseServiceSettingTypeDef",
    {
        "SettingId": str,
        "SettingValue": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "ARN": str,
        "Status": str,
    },
    total=False,
)


class ClientGetServiceSettingResponseServiceSettingTypeDef(
    _ClientGetServiceSettingResponseServiceSettingTypeDef
):
    """
    - **ServiceSetting** *(dict) --*

      The query result of the current service setting.
      - **SettingId** *(string) --*

        The ID of the service setting.
    """


_ClientGetServiceSettingResponseTypeDef = TypedDict(
    "_ClientGetServiceSettingResponseTypeDef",
    {"ServiceSetting": ClientGetServiceSettingResponseServiceSettingTypeDef},
    total=False,
)


class ClientGetServiceSettingResponseTypeDef(_ClientGetServiceSettingResponseTypeDef):
    """
    - *(dict) --*

      The query result body of the GetServiceSetting API action.
      - **ServiceSetting** *(dict) --*

        The query result of the current service setting.
        - **SettingId** *(string) --*

          The ID of the service setting.
    """


_ClientLabelParameterVersionResponseTypeDef = TypedDict(
    "_ClientLabelParameterVersionResponseTypeDef",
    {"InvalidLabels": List[str], "ParameterVersion": int},
    total=False,
)


class ClientLabelParameterVersionResponseTypeDef(_ClientLabelParameterVersionResponseTypeDef):
    """
    - *(dict) --*

      - **InvalidLabels** *(list) --*

        The label does not meet the requirements. For information about parameter label
        requirements, see `Labeling Parameters
        <http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html>`__
        in the *AWS Systems Manager User Guide* .
        - *(string) --*
    """


_ClientListAssociationVersionsResponseAssociationVersionsOutputLocationS3LocationTypeDef = TypedDict(
    "_ClientListAssociationVersionsResponseAssociationVersionsOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)


class ClientListAssociationVersionsResponseAssociationVersionsOutputLocationS3LocationTypeDef(
    _ClientListAssociationVersionsResponseAssociationVersionsOutputLocationS3LocationTypeDef
):
    pass


_ClientListAssociationVersionsResponseAssociationVersionsOutputLocationTypeDef = TypedDict(
    "_ClientListAssociationVersionsResponseAssociationVersionsOutputLocationTypeDef",
    {
        "S3Location": ClientListAssociationVersionsResponseAssociationVersionsOutputLocationS3LocationTypeDef
    },
    total=False,
)


class ClientListAssociationVersionsResponseAssociationVersionsOutputLocationTypeDef(
    _ClientListAssociationVersionsResponseAssociationVersionsOutputLocationTypeDef
):
    pass


_ClientListAssociationVersionsResponseAssociationVersionsTargetsTypeDef = TypedDict(
    "_ClientListAssociationVersionsResponseAssociationVersionsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientListAssociationVersionsResponseAssociationVersionsTargetsTypeDef(
    _ClientListAssociationVersionsResponseAssociationVersionsTargetsTypeDef
):
    pass


_ClientListAssociationVersionsResponseAssociationVersionsTypeDef = TypedDict(
    "_ClientListAssociationVersionsResponseAssociationVersionsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "CreatedDate": datetime,
        "Name": str,
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "Targets": List[ClientListAssociationVersionsResponseAssociationVersionsTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientListAssociationVersionsResponseAssociationVersionsOutputLocationTypeDef,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)


class ClientListAssociationVersionsResponseAssociationVersionsTypeDef(
    _ClientListAssociationVersionsResponseAssociationVersionsTypeDef
):
    """
    - *(dict) --*

      Information about the association version.
      - **AssociationId** *(string) --*

        The ID created by the system when the association was created.
    """


_ClientListAssociationVersionsResponseTypeDef = TypedDict(
    "_ClientListAssociationVersionsResponseTypeDef",
    {
        "AssociationVersions": List[
            ClientListAssociationVersionsResponseAssociationVersionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListAssociationVersionsResponseTypeDef(_ClientListAssociationVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **AssociationVersions** *(list) --*

        Information about all versions of the association for the specified association ID.
        - *(dict) --*

          Information about the association version.
          - **AssociationId** *(string) --*

            The ID created by the system when the association was created.
    """


_RequiredClientListAssociationsAssociationFilterListTypeDef = TypedDict(
    "_RequiredClientListAssociationsAssociationFilterListTypeDef",
    {
        "key": Literal[
            "InstanceId",
            "Name",
            "AssociationId",
            "AssociationStatusName",
            "LastExecutedBefore",
            "LastExecutedAfter",
            "AssociationName",
        ]
    },
)
_OptionalClientListAssociationsAssociationFilterListTypeDef = TypedDict(
    "_OptionalClientListAssociationsAssociationFilterListTypeDef", {"value": str}, total=False
)


class ClientListAssociationsAssociationFilterListTypeDef(
    _RequiredClientListAssociationsAssociationFilterListTypeDef,
    _OptionalClientListAssociationsAssociationFilterListTypeDef,
):
    """
    - *(dict) --*

      Describes a filter.
      - **key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientListAssociationsResponseAssociationsOverviewTypeDef = TypedDict(
    "_ClientListAssociationsResponseAssociationsOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)


class ClientListAssociationsResponseAssociationsOverviewTypeDef(
    _ClientListAssociationsResponseAssociationsOverviewTypeDef
):
    pass


_ClientListAssociationsResponseAssociationsTargetsTypeDef = TypedDict(
    "_ClientListAssociationsResponseAssociationsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientListAssociationsResponseAssociationsTargetsTypeDef(
    _ClientListAssociationsResponseAssociationsTargetsTypeDef
):
    pass


_ClientListAssociationsResponseAssociationsTypeDef = TypedDict(
    "_ClientListAssociationsResponseAssociationsTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationId": str,
        "AssociationVersion": str,
        "DocumentVersion": str,
        "Targets": List[ClientListAssociationsResponseAssociationsTargetsTypeDef],
        "LastExecutionDate": datetime,
        "Overview": ClientListAssociationsResponseAssociationsOverviewTypeDef,
        "ScheduleExpression": str,
        "AssociationName": str,
    },
    total=False,
)


class ClientListAssociationsResponseAssociationsTypeDef(
    _ClientListAssociationsResponseAssociationsTypeDef
):
    """
    - *(dict) --*

      Describes an association of a Systems Manager document and an instance.
      - **Name** *(string) --*

        The name of the Systems Manager document.
    """


_ClientListAssociationsResponseTypeDef = TypedDict(
    "_ClientListAssociationsResponseTypeDef",
    {"Associations": List[ClientListAssociationsResponseAssociationsTypeDef], "NextToken": str},
    total=False,
)


class ClientListAssociationsResponseTypeDef(_ClientListAssociationsResponseTypeDef):
    """
    - *(dict) --*

      - **Associations** *(list) --*

        The associations.
        - *(dict) --*

          Describes an association of a Systems Manager document and an instance.
          - **Name** *(string) --*

            The name of the Systems Manager document.
    """


_RequiredClientListCommandInvocationsFiltersTypeDef = TypedDict(
    "_RequiredClientListCommandInvocationsFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Status", "ExecutionStage", "DocumentName"]},
)
_OptionalClientListCommandInvocationsFiltersTypeDef = TypedDict(
    "_OptionalClientListCommandInvocationsFiltersTypeDef", {"value": str}, total=False
)


class ClientListCommandInvocationsFiltersTypeDef(
    _RequiredClientListCommandInvocationsFiltersTypeDef,
    _OptionalClientListCommandInvocationsFiltersTypeDef,
):
    """
    - *(dict) --*

      Describes a command filter.
      - **key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientListCommandInvocationsResponseCommandInvocationsCloudWatchOutputConfigTypeDef = TypedDict(
    "_ClientListCommandInvocationsResponseCommandInvocationsCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)


class ClientListCommandInvocationsResponseCommandInvocationsCloudWatchOutputConfigTypeDef(
    _ClientListCommandInvocationsResponseCommandInvocationsCloudWatchOutputConfigTypeDef
):
    pass


_ClientListCommandInvocationsResponseCommandInvocationsCommandPluginsTypeDef = TypedDict(
    "_ClientListCommandInvocationsResponseCommandInvocationsCommandPluginsTypeDef",
    {
        "Name": str,
        "Status": Literal["Pending", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"],
        "StatusDetails": str,
        "ResponseCode": int,
        "ResponseStartDateTime": datetime,
        "ResponseFinishDateTime": datetime,
        "Output": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
    },
    total=False,
)


class ClientListCommandInvocationsResponseCommandInvocationsCommandPluginsTypeDef(
    _ClientListCommandInvocationsResponseCommandInvocationsCommandPluginsTypeDef
):
    pass


_ClientListCommandInvocationsResponseCommandInvocationsNotificationConfigTypeDef = TypedDict(
    "_ClientListCommandInvocationsResponseCommandInvocationsNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)


class ClientListCommandInvocationsResponseCommandInvocationsNotificationConfigTypeDef(
    _ClientListCommandInvocationsResponseCommandInvocationsNotificationConfigTypeDef
):
    pass


_ClientListCommandInvocationsResponseCommandInvocationsTypeDef = TypedDict(
    "_ClientListCommandInvocationsResponseCommandInvocationsTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "InstanceName": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending",
            "InProgress",
            "Delayed",
            "Success",
            "Cancelled",
            "TimedOut",
            "Failed",
            "Cancelling",
        ],
        "StatusDetails": str,
        "TraceOutput": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "CommandPlugins": List[
            ClientListCommandInvocationsResponseCommandInvocationsCommandPluginsTypeDef
        ],
        "ServiceRole": str,
        "NotificationConfig": ClientListCommandInvocationsResponseCommandInvocationsNotificationConfigTypeDef,
        "CloudWatchOutputConfig": ClientListCommandInvocationsResponseCommandInvocationsCloudWatchOutputConfigTypeDef,
    },
    total=False,
)


class ClientListCommandInvocationsResponseCommandInvocationsTypeDef(
    _ClientListCommandInvocationsResponseCommandInvocationsTypeDef
):
    """
    - *(dict) --*

      An invocation is copy of a command sent to a specific instance. A command can apply to one or
      more instances. A command invocation applies to one instance. For example, if a user runs
      SendCommand against three instances, then a command invocation is created for each requested
      instance ID. A command invocation returns status and detail information about a command you
      ran.
      - **CommandId** *(string) --*

        The command against which this invocation was requested.
    """


_ClientListCommandInvocationsResponseTypeDef = TypedDict(
    "_ClientListCommandInvocationsResponseTypeDef",
    {
        "CommandInvocations": List[ClientListCommandInvocationsResponseCommandInvocationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListCommandInvocationsResponseTypeDef(_ClientListCommandInvocationsResponseTypeDef):
    """
    - *(dict) --*

      - **CommandInvocations** *(list) --*

        (Optional) A list of all invocations.
        - *(dict) --*

          An invocation is copy of a command sent to a specific instance. A command can apply to one
          or more instances. A command invocation applies to one instance. For example, if a user
          runs SendCommand against three instances, then a command invocation is created for each
          requested instance ID. A command invocation returns status and detail information about a
          command you ran.
          - **CommandId** *(string) --*

            The command against which this invocation was requested.
    """


_RequiredClientListCommandsFiltersTypeDef = TypedDict(
    "_RequiredClientListCommandsFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Status", "ExecutionStage", "DocumentName"]},
)
_OptionalClientListCommandsFiltersTypeDef = TypedDict(
    "_OptionalClientListCommandsFiltersTypeDef", {"value": str}, total=False
)


class ClientListCommandsFiltersTypeDef(
    _RequiredClientListCommandsFiltersTypeDef, _OptionalClientListCommandsFiltersTypeDef
):
    """
    - *(dict) --*

      Describes a command filter.
      - **key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientListCommandsResponseCommandsCloudWatchOutputConfigTypeDef = TypedDict(
    "_ClientListCommandsResponseCommandsCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)


class ClientListCommandsResponseCommandsCloudWatchOutputConfigTypeDef(
    _ClientListCommandsResponseCommandsCloudWatchOutputConfigTypeDef
):
    pass


_ClientListCommandsResponseCommandsNotificationConfigTypeDef = TypedDict(
    "_ClientListCommandsResponseCommandsNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)


class ClientListCommandsResponseCommandsNotificationConfigTypeDef(
    _ClientListCommandsResponseCommandsNotificationConfigTypeDef
):
    pass


_ClientListCommandsResponseCommandsTargetsTypeDef = TypedDict(
    "_ClientListCommandsResponseCommandsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientListCommandsResponseCommandsTargetsTypeDef(
    _ClientListCommandsResponseCommandsTargetsTypeDef
):
    pass


_ClientListCommandsResponseCommandsTypeDef = TypedDict(
    "_ClientListCommandsResponseCommandsTypeDef",
    {
        "CommandId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "Comment": str,
        "ExpiresAfter": datetime,
        "Parameters": Dict[str, List[str]],
        "InstanceIds": List[str],
        "Targets": List[ClientListCommandsResponseCommandsTargetsTypeDef],
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending", "InProgress", "Success", "Cancelled", "Failed", "TimedOut", "Cancelling"
        ],
        "StatusDetails": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetCount": int,
        "CompletedCount": int,
        "ErrorCount": int,
        "DeliveryTimedOutCount": int,
        "ServiceRole": str,
        "NotificationConfig": ClientListCommandsResponseCommandsNotificationConfigTypeDef,
        "CloudWatchOutputConfig": ClientListCommandsResponseCommandsCloudWatchOutputConfigTypeDef,
    },
    total=False,
)


class ClientListCommandsResponseCommandsTypeDef(_ClientListCommandsResponseCommandsTypeDef):
    """
    - *(dict) --*

      Describes a command request.
      - **CommandId** *(string) --*

        A unique identifier for this command.
    """


_ClientListCommandsResponseTypeDef = TypedDict(
    "_ClientListCommandsResponseTypeDef",
    {"Commands": List[ClientListCommandsResponseCommandsTypeDef], "NextToken": str},
    total=False,
)


class ClientListCommandsResponseTypeDef(_ClientListCommandsResponseTypeDef):
    """
    - *(dict) --*

      - **Commands** *(list) --*

        (Optional) The list of commands requested by the user.
        - *(dict) --*

          Describes a command request.
          - **CommandId** *(string) --*

            A unique identifier for this command.
    """


_ClientListComplianceItemsFiltersTypeDef = TypedDict(
    "_ClientListComplianceItemsFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)


class ClientListComplianceItemsFiltersTypeDef(_ClientListComplianceItemsFiltersTypeDef):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of results.
      - **Key** *(string) --*

        The name of the filter.
    """


_ClientListComplianceItemsResponseComplianceItemsExecutionSummaryTypeDef = TypedDict(
    "_ClientListComplianceItemsResponseComplianceItemsExecutionSummaryTypeDef",
    {"ExecutionTime": datetime, "ExecutionId": str, "ExecutionType": str},
    total=False,
)


class ClientListComplianceItemsResponseComplianceItemsExecutionSummaryTypeDef(
    _ClientListComplianceItemsResponseComplianceItemsExecutionSummaryTypeDef
):
    pass


_ClientListComplianceItemsResponseComplianceItemsTypeDef = TypedDict(
    "_ClientListComplianceItemsResponseComplianceItemsTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Id": str,
        "Title": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "Severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"],
        "ExecutionSummary": ClientListComplianceItemsResponseComplianceItemsExecutionSummaryTypeDef,
        "Details": Dict[str, str],
    },
    total=False,
)


class ClientListComplianceItemsResponseComplianceItemsTypeDef(
    _ClientListComplianceItemsResponseComplianceItemsTypeDef
):
    """
    - *(dict) --*

      Information about the compliance as defined by the resource type. For example, for a patch
      resource type, ``Items`` includes information about the PatchSeverity, Classification, etc.
      - **ComplianceType** *(string) --*

        The compliance type. For example, Association (for a State Manager association), Patch, or
        Custom:``string`` are all valid compliance types.
    """


_ClientListComplianceItemsResponseTypeDef = TypedDict(
    "_ClientListComplianceItemsResponseTypeDef",
    {
        "ComplianceItems": List[ClientListComplianceItemsResponseComplianceItemsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListComplianceItemsResponseTypeDef(_ClientListComplianceItemsResponseTypeDef):
    """
    - *(dict) --*

      - **ComplianceItems** *(list) --*

        A list of compliance information for the specified resource ID.
        - *(dict) --*

          Information about the compliance as defined by the resource type. For example, for a patch
          resource type, ``Items`` includes information about the PatchSeverity, Classification,
          etc.
          - **ComplianceType** *(string) --*

            The compliance type. For example, Association (for a State Manager association), Patch,
            or Custom:``string`` are all valid compliance types.
    """


_ClientListComplianceSummariesFiltersTypeDef = TypedDict(
    "_ClientListComplianceSummariesFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)


class ClientListComplianceSummariesFiltersTypeDef(_ClientListComplianceSummariesFiltersTypeDef):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of results.
      - **Key** *(string) --*

        The name of the filter.
    """


_ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "_ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)


class ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef(
    _ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef
):
    pass


_ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummaryTypeDef = TypedDict(
    "_ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummaryTypeDef",
    {
        "CompliantCount": int,
        "SeveritySummary": ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)


class ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummaryTypeDef(
    _ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummaryTypeDef
):
    pass


_ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "_ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)


class ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef(
    _ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef
):
    pass


_ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummaryTypeDef = TypedDict(
    "_ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": int,
        "SeveritySummary": ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)


class ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummaryTypeDef(
    _ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummaryTypeDef
):
    pass


_ClientListComplianceSummariesResponseComplianceSummaryItemsTypeDef = TypedDict(
    "_ClientListComplianceSummariesResponseComplianceSummaryItemsTypeDef",
    {
        "ComplianceType": str,
        "CompliantSummary": ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummaryTypeDef,
        "NonCompliantSummary": ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummaryTypeDef,
    },
    total=False,
)


class ClientListComplianceSummariesResponseComplianceSummaryItemsTypeDef(
    _ClientListComplianceSummariesResponseComplianceSummaryItemsTypeDef
):
    """
    - *(dict) --*

      A summary of compliance information by compliance type.
      - **ComplianceType** *(string) --*

        The type of compliance item. For example, the compliance type can be Association, Patch, or
        Custom:string.
    """


_ClientListComplianceSummariesResponseTypeDef = TypedDict(
    "_ClientListComplianceSummariesResponseTypeDef",
    {
        "ComplianceSummaryItems": List[
            ClientListComplianceSummariesResponseComplianceSummaryItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListComplianceSummariesResponseTypeDef(_ClientListComplianceSummariesResponseTypeDef):
    """
    - *(dict) --*

      - **ComplianceSummaryItems** *(list) --*

        A list of compliant and non-compliant summary counts based on compliance types. For example,
        this call returns State Manager associations, patches, or custom compliance types according
        to the filter criteria that you specified.
        - *(dict) --*

          A summary of compliance information by compliance type.
          - **ComplianceType** *(string) --*

            The type of compliance item. For example, the compliance type can be Association, Patch,
            or Custom:string.
    """


_ClientListDocumentVersionsResponseDocumentVersionsTypeDef = TypedDict(
    "_ClientListDocumentVersionsResponseDocumentVersionsTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
        "VersionName": str,
        "CreatedDate": datetime,
        "IsDefaultVersion": bool,
        "DocumentFormat": Literal["YAML", "JSON"],
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
    },
    total=False,
)


class ClientListDocumentVersionsResponseDocumentVersionsTypeDef(
    _ClientListDocumentVersionsResponseDocumentVersionsTypeDef
):
    """
    - *(dict) --*

      Version information about the document.
      - **Name** *(string) --*

        The document name.
    """


_ClientListDocumentVersionsResponseTypeDef = TypedDict(
    "_ClientListDocumentVersionsResponseTypeDef",
    {
        "DocumentVersions": List[ClientListDocumentVersionsResponseDocumentVersionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListDocumentVersionsResponseTypeDef(_ClientListDocumentVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **DocumentVersions** *(list) --*

        The document versions.
        - *(dict) --*

          Version information about the document.
          - **Name** *(string) --*

            The document name.
    """


_RequiredClientListDocumentsDocumentFilterListTypeDef = TypedDict(
    "_RequiredClientListDocumentsDocumentFilterListTypeDef",
    {"key": Literal["Name", "Owner", "PlatformTypes", "DocumentType"]},
)
_OptionalClientListDocumentsDocumentFilterListTypeDef = TypedDict(
    "_OptionalClientListDocumentsDocumentFilterListTypeDef", {"value": str}, total=False
)


class ClientListDocumentsDocumentFilterListTypeDef(
    _RequiredClientListDocumentsDocumentFilterListTypeDef,
    _OptionalClientListDocumentsDocumentFilterListTypeDef,
):
    """
    - *(dict) --*

      Describes a filter.
      - **key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientListDocumentsFiltersTypeDef = TypedDict(
    "_ClientListDocumentsFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientListDocumentsFiltersTypeDef(_ClientListDocumentsFiltersTypeDef):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of documents.
      For keys, you can specify one or more tags that have been applied to a document.
      Other valid values include Owner, Name, PlatformTypes, and DocumentType.
      Note that only one Owner can be specified in a request. For example: ``Key=Owner,Values=
          Self``
      .
      If you use Name as a key, you can use a name prefix to return a list of documents. For
      example, in the AWS CLI, to return a list of all documents that begin with ``Te`` , run the
      following command:

        ``aws ssm list-documents --filters Key=Name,Values=Te``
    """


_ClientListDocumentsResponseDocumentIdentifiersRequiresTypeDef = TypedDict(
    "_ClientListDocumentsResponseDocumentIdentifiersRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientListDocumentsResponseDocumentIdentifiersRequiresTypeDef(
    _ClientListDocumentsResponseDocumentIdentifiersRequiresTypeDef
):
    pass


_ClientListDocumentsResponseDocumentIdentifiersTagsTypeDef = TypedDict(
    "_ClientListDocumentsResponseDocumentIdentifiersTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListDocumentsResponseDocumentIdentifiersTagsTypeDef(
    _ClientListDocumentsResponseDocumentIdentifiersTagsTypeDef
):
    pass


_ClientListDocumentsResponseDocumentIdentifiersTypeDef = TypedDict(
    "_ClientListDocumentsResponseDocumentIdentifiersTypeDef",
    {
        "Name": str,
        "Owner": str,
        "VersionName": str,
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentVersion": str,
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
        ],
        "SchemaVersion": str,
        "DocumentFormat": Literal["YAML", "JSON"],
        "TargetType": str,
        "Tags": List[ClientListDocumentsResponseDocumentIdentifiersTagsTypeDef],
        "Requires": List[ClientListDocumentsResponseDocumentIdentifiersRequiresTypeDef],
    },
    total=False,
)


class ClientListDocumentsResponseDocumentIdentifiersTypeDef(
    _ClientListDocumentsResponseDocumentIdentifiersTypeDef
):
    """
    - *(dict) --*

      Describes the name of a Systems Manager document.
      - **Name** *(string) --*

        The name of the Systems Manager document.
    """


_ClientListDocumentsResponseTypeDef = TypedDict(
    "_ClientListDocumentsResponseTypeDef",
    {
        "DocumentIdentifiers": List[ClientListDocumentsResponseDocumentIdentifiersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListDocumentsResponseTypeDef(_ClientListDocumentsResponseTypeDef):
    """
    - *(dict) --*

      - **DocumentIdentifiers** *(list) --*

        The names of the Systems Manager documents.
        - *(dict) --*

          Describes the name of a Systems Manager document.
          - **Name** *(string) --*

            The name of the Systems Manager document.
    """


_RequiredClientListInventoryEntriesFiltersTypeDef = TypedDict(
    "_RequiredClientListInventoryEntriesFiltersTypeDef", {"Key": str}
)
_OptionalClientListInventoryEntriesFiltersTypeDef = TypedDict(
    "_OptionalClientListInventoryEntriesFiltersTypeDef",
    {
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class ClientListInventoryEntriesFiltersTypeDef(
    _RequiredClientListInventoryEntriesFiltersTypeDef,
    _OptionalClientListInventoryEntriesFiltersTypeDef,
):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of results.
      - **Key** *(string) --***[REQUIRED]**

        The name of the filter key.
    """


_ClientListInventoryEntriesResponseTypeDef = TypedDict(
    "_ClientListInventoryEntriesResponseTypeDef",
    {
        "TypeName": str,
        "InstanceId": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "Entries": List[Dict[str, str]],
        "NextToken": str,
    },
    total=False,
)


class ClientListInventoryEntriesResponseTypeDef(_ClientListInventoryEntriesResponseTypeDef):
    """
    - *(dict) --*

      - **TypeName** *(string) --*

        The type of inventory item returned by the request.
    """


_ClientListResourceComplianceSummariesFiltersTypeDef = TypedDict(
    "_ClientListResourceComplianceSummariesFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)


class ClientListResourceComplianceSummariesFiltersTypeDef(
    _ClientListResourceComplianceSummariesFiltersTypeDef
):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of results.
      - **Key** *(string) --*

        The name of the filter.
    """


_ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "_ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)


class ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef(
    _ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef
):
    pass


_ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef = TypedDict(
    "_ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef",
    {
        "CompliantCount": int,
        "SeveritySummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)


class ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef(
    _ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef
):
    pass


_ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef = TypedDict(
    "_ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef",
    {"ExecutionTime": datetime, "ExecutionId": str, "ExecutionType": str},
    total=False,
)


class ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef(
    _ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef
):
    pass


_ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "_ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)


class ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef(
    _ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef
):
    pass


_ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef = TypedDict(
    "_ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": int,
        "SeveritySummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)


class ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef(
    _ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef
):
    pass


_ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsTypeDef = TypedDict(
    "_ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "OverallSeverity": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ExecutionSummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef,
        "CompliantSummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef,
        "NonCompliantSummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef,
    },
    total=False,
)


class ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsTypeDef(
    _ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsTypeDef
):
    """
    - *(dict) --*

      Compliance summary information for a specific resource.
      - **ComplianceType** *(string) --*

        The compliance type.
    """


_ClientListResourceComplianceSummariesResponseTypeDef = TypedDict(
    "_ClientListResourceComplianceSummariesResponseTypeDef",
    {
        "ResourceComplianceSummaryItems": List[
            ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListResourceComplianceSummariesResponseTypeDef(
    _ClientListResourceComplianceSummariesResponseTypeDef
):
    """
    - *(dict) --*

      - **ResourceComplianceSummaryItems** *(list) --*

        A summary count for specified or targeted managed instances. Summary count includes
        information about compliant and non-compliant State Manager associations, patch status, or
        custom items according to the filter criteria that you specify.
        - *(dict) --*

          Compliance summary information for a specific resource.
          - **ComplianceType** *(string) --*

            The compliance type.
    """


_ClientListResourceDataSyncResponseResourceDataSyncItemsS3DestinationTypeDef = TypedDict(
    "_ClientListResourceDataSyncResponseResourceDataSyncItemsS3DestinationTypeDef",
    {"BucketName": str, "Prefix": str, "SyncFormat": str, "Region": str, "AWSKMSKeyARN": str},
    total=False,
)


class ClientListResourceDataSyncResponseResourceDataSyncItemsS3DestinationTypeDef(
    _ClientListResourceDataSyncResponseResourceDataSyncItemsS3DestinationTypeDef
):
    pass


_ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef = TypedDict(
    "_ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    {"OrganizationalUnitId": str},
    total=False,
)


class ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef(
    _ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
):
    pass


_ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef = TypedDict(
    "_ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": List[
            ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
        ],
    },
    total=False,
)


class ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef(
    _ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef
):
    pass


_ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceTypeDef = TypedDict(
    "_ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceTypeDef",
    {
        "SourceType": str,
        "AwsOrganizationsSource": ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef,
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
        "State": str,
    },
    total=False,
)


class ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceTypeDef(
    _ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceTypeDef
):
    pass


_ClientListResourceDataSyncResponseResourceDataSyncItemsTypeDef = TypedDict(
    "_ClientListResourceDataSyncResponseResourceDataSyncItemsTypeDef",
    {
        "SyncName": str,
        "SyncType": str,
        "SyncSource": ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceTypeDef,
        "S3Destination": ClientListResourceDataSyncResponseResourceDataSyncItemsS3DestinationTypeDef,
        "LastSyncTime": datetime,
        "LastSuccessfulSyncTime": datetime,
        "SyncLastModifiedTime": datetime,
        "LastStatus": Literal["Successful", "Failed", "InProgress"],
        "SyncCreatedTime": datetime,
        "LastSyncStatusMessage": str,
    },
    total=False,
)


class ClientListResourceDataSyncResponseResourceDataSyncItemsTypeDef(
    _ClientListResourceDataSyncResponseResourceDataSyncItemsTypeDef
):
    """
    - *(dict) --*

      Information about a Resource Data Sync configuration, including its current status and last
      successful sync.
      - **SyncName** *(string) --*

        The name of the Resource Data Sync.
    """


_ClientListResourceDataSyncResponseTypeDef = TypedDict(
    "_ClientListResourceDataSyncResponseTypeDef",
    {
        "ResourceDataSyncItems": List[
            ClientListResourceDataSyncResponseResourceDataSyncItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListResourceDataSyncResponseTypeDef(_ClientListResourceDataSyncResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceDataSyncItems** *(list) --*

        A list of your current Resource Data Sync configurations and their statuses.
        - *(dict) --*

          Information about a Resource Data Sync configuration, including its current status and
          last successful sync.
          - **SyncName** *(string) --*

            The name of the Resource Data Sync.
    """


_ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagListTypeDef(
    _ClientListTagsForResourceResponseTagListTypeDef
):
    """
    - *(dict) --*

      Metadata that you assign to your AWS resources. Tags enable you to categorize your resources
      in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can
      apply tags to documents, managed instances, maintenance windows, Parameter Store parameters,
      and patch baselines.
      - **Key** *(string) --*

        The name of the tag.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **TagList** *(list) --*

        A list of tags.
        - *(dict) --*

          Metadata that you assign to your AWS resources. Tags enable you to categorize your
          resources in different ways, for example, by purpose, owner, or environment. In Systems
          Manager, you can apply tags to documents, managed instances, maintenance windows,
          Parameter Store parameters, and patch baselines.
          - **Key** *(string) --*

            The name of the tag.
    """


_RequiredClientPutComplianceItemsExecutionSummaryTypeDef = TypedDict(
    "_RequiredClientPutComplianceItemsExecutionSummaryTypeDef", {"ExecutionTime": datetime}
)
_OptionalClientPutComplianceItemsExecutionSummaryTypeDef = TypedDict(
    "_OptionalClientPutComplianceItemsExecutionSummaryTypeDef",
    {"ExecutionId": str, "ExecutionType": str},
    total=False,
)


class ClientPutComplianceItemsExecutionSummaryTypeDef(
    _RequiredClientPutComplianceItemsExecutionSummaryTypeDef,
    _OptionalClientPutComplianceItemsExecutionSummaryTypeDef,
):
    """
    A summary of the call execution that includes an execution ID, the type of execution (for
    example, ``Command`` ), and the date/time of the execution using a datetime object that is saved
    in the following format: yyyy-MM-dd'T'HH:mm:ss'Z'.
    - **ExecutionTime** *(datetime) --***[REQUIRED]**

      The time the execution ran as a datetime object that is saved in the following format:
      yyyy-MM-dd'T'HH:mm:ss'Z'.
    """


_ClientPutComplianceItemsItemsTypeDef = TypedDict(
    "_ClientPutComplianceItemsItemsTypeDef",
    {
        "Id": str,
        "Title": str,
        "Severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"],
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "Details": Dict[str, str],
    },
    total=False,
)


class ClientPutComplianceItemsItemsTypeDef(_ClientPutComplianceItemsItemsTypeDef):
    """
    - *(dict) --*

      Information about a compliance item.
      - **Id** *(string) --*

        The compliance item ID. For example, if the compliance item is a Windows patch, the ID could
        be the number of the KB article.
    """


_RequiredClientPutInventoryItemsTypeDef = TypedDict(
    "_RequiredClientPutInventoryItemsTypeDef", {"TypeName": str}
)
_OptionalClientPutInventoryItemsTypeDef = TypedDict(
    "_OptionalClientPutInventoryItemsTypeDef",
    {
        "SchemaVersion": str,
        "CaptureTime": str,
        "ContentHash": str,
        "Content": List[Dict[str, str]],
        "Context": Dict[str, str],
    },
    total=False,
)


class ClientPutInventoryItemsTypeDef(
    _RequiredClientPutInventoryItemsTypeDef, _OptionalClientPutInventoryItemsTypeDef
):
    """
    - *(dict) --*

      Information collected from managed instances based on your inventory policy document
      - **TypeName** *(string) --***[REQUIRED]**

        The name of the inventory type. Default inventory item type names start with AWS. Custom
        inventory type names will start with Custom. Default inventory item types include the
        following: AWS:AWSComponent, AWS:Application, AWS:InstanceInformation, AWS:Network, and
        AWS:WindowsUpdate.
    """


_ClientPutInventoryResponseTypeDef = TypedDict(
    "_ClientPutInventoryResponseTypeDef", {"Message": str}, total=False
)


class ClientPutInventoryResponseTypeDef(_ClientPutInventoryResponseTypeDef):
    """
    - *(dict) --*

      - **Message** *(string) --*

        Information about the request.
    """


_ClientPutParameterResponseTypeDef = TypedDict(
    "_ClientPutParameterResponseTypeDef",
    {"Version": int, "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"]},
    total=False,
)


class ClientPutParameterResponseTypeDef(_ClientPutParameterResponseTypeDef):
    """
    - *(dict) --*

      - **Version** *(integer) --*

        The new version number of a parameter. If you edit a parameter value, Parameter Store
        automatically creates a new version and assigns this new version a unique ID. You can
        reference a parameter version ID in API actions or in Systems Manager documents (SSM
        documents). By default, if you don't specify a specific version, the system returns the
        latest parameter value when a parameter is called.
    """


_ClientPutParameterTagsTypeDef = TypedDict(
    "_ClientPutParameterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientPutParameterTagsTypeDef(_ClientPutParameterTagsTypeDef):
    pass


_ClientRegisterDefaultPatchBaselineResponseTypeDef = TypedDict(
    "_ClientRegisterDefaultPatchBaselineResponseTypeDef", {"BaselineId": str}, total=False
)


class ClientRegisterDefaultPatchBaselineResponseTypeDef(
    _ClientRegisterDefaultPatchBaselineResponseTypeDef
):
    """
    - *(dict) --*

      - **BaselineId** *(string) --*

        The ID of the default patch baseline.
    """


_ClientRegisterPatchBaselineForPatchGroupResponseTypeDef = TypedDict(
    "_ClientRegisterPatchBaselineForPatchGroupResponseTypeDef",
    {"BaselineId": str, "PatchGroup": str},
    total=False,
)


class ClientRegisterPatchBaselineForPatchGroupResponseTypeDef(
    _ClientRegisterPatchBaselineForPatchGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **BaselineId** *(string) --*

        The ID of the patch baseline the patch group was registered with.
    """


_ClientRegisterTargetWithMaintenanceWindowResponseTypeDef = TypedDict(
    "_ClientRegisterTargetWithMaintenanceWindowResponseTypeDef",
    {"WindowTargetId": str},
    total=False,
)


class ClientRegisterTargetWithMaintenanceWindowResponseTypeDef(
    _ClientRegisterTargetWithMaintenanceWindowResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowTargetId** *(string) --*

        The ID of the target definition in this maintenance window.
    """


_ClientRegisterTargetWithMaintenanceWindowTargetsTypeDef = TypedDict(
    "_ClientRegisterTargetWithMaintenanceWindowTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientRegisterTargetWithMaintenanceWindowTargetsTypeDef(
    _ClientRegisterTargetWithMaintenanceWindowTargetsTypeDef
):
    pass


_ClientRegisterTaskWithMaintenanceWindowLoggingInfoTypeDef = TypedDict(
    "_ClientRegisterTaskWithMaintenanceWindowLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)


class ClientRegisterTaskWithMaintenanceWindowLoggingInfoTypeDef(
    _ClientRegisterTaskWithMaintenanceWindowLoggingInfoTypeDef
):
    """
    A structure containing information about an Amazon S3 bucket to write instance-level logs to.
    .. note::

      ``LoggingInfo`` has been deprecated. To specify an S3 bucket to contain logs, instead use the
      ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters``
      structure. For information about how Systems Manager handles these options for the supported
      maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .
    """


_ClientRegisterTaskWithMaintenanceWindowResponseTypeDef = TypedDict(
    "_ClientRegisterTaskWithMaintenanceWindowResponseTypeDef", {"WindowTaskId": str}, total=False
)


class ClientRegisterTaskWithMaintenanceWindowResponseTypeDef(
    _ClientRegisterTaskWithMaintenanceWindowResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowTaskId** *(string) --*

        The ID of the task in the maintenance window.
    """


_ClientRegisterTaskWithMaintenanceWindowTargetsTypeDef = TypedDict(
    "_ClientRegisterTaskWithMaintenanceWindowTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientRegisterTaskWithMaintenanceWindowTargetsTypeDef(
    _ClientRegisterTaskWithMaintenanceWindowTargetsTypeDef
):
    pass


_ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersAutomationTypeDef = TypedDict(
    "_ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersAutomationTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)


class ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersAutomationTypeDef(
    _ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersAutomationTypeDef
):
    pass


_ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersLambdaTypeDef = TypedDict(
    "_ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersLambdaTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": bytes},
    total=False,
)


class ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersLambdaTypeDef(
    _ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersLambdaTypeDef
):
    pass


_ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandNotificationConfigTypeDef = TypedDict(
    "_ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)


class ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandNotificationConfigTypeDef(
    _ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandNotificationConfigTypeDef
):
    pass


_ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandTypeDef = TypedDict(
    "_ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandTypeDef",
    {
        "Comment": str,
        "DocumentHash": str,
        "DocumentHashType": Literal["Sha256", "Sha1"],
        "NotificationConfig": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandNotificationConfigTypeDef,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)


class ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandTypeDef(
    _ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandTypeDef
):
    """
    - **RunCommand** *(dict) --*

      The parameters for a RUN_COMMAND task type.
      - **Comment** *(string) --*

        Information about the commands to run.
    """


_ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersStepFunctionsTypeDef = TypedDict(
    "_ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersStepFunctionsTypeDef",
    {"Input": str, "Name": str},
    total=False,
)


class ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersStepFunctionsTypeDef(
    _ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersStepFunctionsTypeDef
):
    pass


_ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersTypeDef = TypedDict(
    "_ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersTypeDef",
    {
        "RunCommand": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandTypeDef,
        "Automation": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersAutomationTypeDef,
        "StepFunctions": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersStepFunctionsTypeDef,
        "Lambda": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersLambdaTypeDef,
    },
    total=False,
)


class ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersTypeDef(
    _ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersTypeDef
):
    """
    The parameters that the task should use during execution. Populate only the fields that match
    the task type. All other fields should be empty.
    - **RunCommand** *(dict) --*

      The parameters for a RUN_COMMAND task type.
      - **Comment** *(string) --*

        Information about the commands to run.
    """


_ClientRegisterTaskWithMaintenanceWindowTaskParametersTypeDef = TypedDict(
    "_ClientRegisterTaskWithMaintenanceWindowTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientRegisterTaskWithMaintenanceWindowTaskParametersTypeDef(
    _ClientRegisterTaskWithMaintenanceWindowTaskParametersTypeDef
):
    pass


_ClientResetServiceSettingResponseServiceSettingTypeDef = TypedDict(
    "_ClientResetServiceSettingResponseServiceSettingTypeDef",
    {
        "SettingId": str,
        "SettingValue": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "ARN": str,
        "Status": str,
    },
    total=False,
)


class ClientResetServiceSettingResponseServiceSettingTypeDef(
    _ClientResetServiceSettingResponseServiceSettingTypeDef
):
    """
    - **ServiceSetting** *(dict) --*

      The current, effective service setting after calling the ResetServiceSetting API action.
      - **SettingId** *(string) --*

        The ID of the service setting.
    """


_ClientResetServiceSettingResponseTypeDef = TypedDict(
    "_ClientResetServiceSettingResponseTypeDef",
    {"ServiceSetting": ClientResetServiceSettingResponseServiceSettingTypeDef},
    total=False,
)


class ClientResetServiceSettingResponseTypeDef(_ClientResetServiceSettingResponseTypeDef):
    """
    - *(dict) --*

      The result body of the ResetServiceSetting API action.
      - **ServiceSetting** *(dict) --*

        The current, effective service setting after calling the ResetServiceSetting API action.
        - **SettingId** *(string) --*

          The ID of the service setting.
    """


_ClientResumeSessionResponseTypeDef = TypedDict(
    "_ClientResumeSessionResponseTypeDef",
    {"SessionId": str, "TokenValue": str, "StreamUrl": str},
    total=False,
)


class ClientResumeSessionResponseTypeDef(_ClientResumeSessionResponseTypeDef):
    """
    - *(dict) --*

      - **SessionId** *(string) --*

        The ID of the session.
    """


_ClientSendCommandCloudWatchOutputConfigTypeDef = TypedDict(
    "_ClientSendCommandCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)


class ClientSendCommandCloudWatchOutputConfigTypeDef(
    _ClientSendCommandCloudWatchOutputConfigTypeDef
):
    """
    Enables Systems Manager to send Run Command output to Amazon CloudWatch Logs.
    - **CloudWatchLogGroupName** *(string) --*

      The name of the CloudWatch log group where you want to send command output. If you don't
      specify a group name, Systems Manager automatically creates a log group for you. The log group
      uses the following naming format: aws/ssm/*SystemsManagerDocumentName* .
    """


_ClientSendCommandNotificationConfigTypeDef = TypedDict(
    "_ClientSendCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)


class ClientSendCommandNotificationConfigTypeDef(_ClientSendCommandNotificationConfigTypeDef):
    """
    Configurations for sending notifications.
    - **NotificationArn** *(string) --*

      An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic.
      Run Command pushes notifications about command status changes to this topic.
    """


_ClientSendCommandResponseCommandCloudWatchOutputConfigTypeDef = TypedDict(
    "_ClientSendCommandResponseCommandCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)


class ClientSendCommandResponseCommandCloudWatchOutputConfigTypeDef(
    _ClientSendCommandResponseCommandCloudWatchOutputConfigTypeDef
):
    pass


_ClientSendCommandResponseCommandNotificationConfigTypeDef = TypedDict(
    "_ClientSendCommandResponseCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)


class ClientSendCommandResponseCommandNotificationConfigTypeDef(
    _ClientSendCommandResponseCommandNotificationConfigTypeDef
):
    pass


_ClientSendCommandResponseCommandTargetsTypeDef = TypedDict(
    "_ClientSendCommandResponseCommandTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientSendCommandResponseCommandTargetsTypeDef(
    _ClientSendCommandResponseCommandTargetsTypeDef
):
    pass


_ClientSendCommandResponseCommandTypeDef = TypedDict(
    "_ClientSendCommandResponseCommandTypeDef",
    {
        "CommandId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "Comment": str,
        "ExpiresAfter": datetime,
        "Parameters": Dict[str, List[str]],
        "InstanceIds": List[str],
        "Targets": List[ClientSendCommandResponseCommandTargetsTypeDef],
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending", "InProgress", "Success", "Cancelled", "Failed", "TimedOut", "Cancelling"
        ],
        "StatusDetails": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetCount": int,
        "CompletedCount": int,
        "ErrorCount": int,
        "DeliveryTimedOutCount": int,
        "ServiceRole": str,
        "NotificationConfig": ClientSendCommandResponseCommandNotificationConfigTypeDef,
        "CloudWatchOutputConfig": ClientSendCommandResponseCommandCloudWatchOutputConfigTypeDef,
    },
    total=False,
)


class ClientSendCommandResponseCommandTypeDef(_ClientSendCommandResponseCommandTypeDef):
    """
    - **Command** *(dict) --*

      The request as it was received by Systems Manager. Also provides the command ID which can be
      used future references to this request.
      - **CommandId** *(string) --*

        A unique identifier for this command.
    """


_ClientSendCommandResponseTypeDef = TypedDict(
    "_ClientSendCommandResponseTypeDef",
    {"Command": ClientSendCommandResponseCommandTypeDef},
    total=False,
)


class ClientSendCommandResponseTypeDef(_ClientSendCommandResponseTypeDef):
    """
    - *(dict) --*

      - **Command** *(dict) --*

        The request as it was received by Systems Manager. Also provides the command ID which can be
        used future references to this request.
        - **CommandId** *(string) --*

          A unique identifier for this command.
    """


_ClientSendCommandTargetsTypeDef = TypedDict(
    "_ClientSendCommandTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientSendCommandTargetsTypeDef(_ClientSendCommandTargetsTypeDef):
    """
    - *(dict) --*

      An array of search criteria that targets instances using a Key,Value combination that you
      specify.
      Supported formats include the following.
      * ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
      * ``Key=tag:*my-tag-key* ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
      * ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
      * (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
      For example:
      * ``Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE``
      * ``Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3``
      * ``Key=tag-key,Values=Name,Instance-Type,CostCenter``
      * (Maintenance window targets only)
      ``Key=resource-groups:Name,Values=
          ProductionResourceGroup``   This example demonstrates how to
      target all resources in the resource group **ProductionResourceGroup** in your maintenance
      window.
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``
      This example demonstrates how to target only Amazon EC2 instances and VPCs in your maintenance
      window.
      * (State Manager association targets only) ``Key=InstanceIds,Values=*``   This example
      demonstrates how to target all managed instances in the AWS Region where the association was
      created.
      For information about how to send commands that target instances using ``Key,Value``
      parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet
      <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__
      in the *AWS Systems Manager User Guide* .
      - **Key** *(string) --*

        User-defined criteria for sending commands that target instances that meet the criteria.
    """


_ClientStartAutomationExecutionResponseTypeDef = TypedDict(
    "_ClientStartAutomationExecutionResponseTypeDef", {"AutomationExecutionId": str}, total=False
)


class ClientStartAutomationExecutionResponseTypeDef(_ClientStartAutomationExecutionResponseTypeDef):
    """
    - *(dict) --*

      - **AutomationExecutionId** *(string) --*

        The unique ID of a newly scheduled automation execution.
    """


_ClientStartAutomationExecutionTargetLocationsTypeDef = TypedDict(
    "_ClientStartAutomationExecutionTargetLocationsTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)


class ClientStartAutomationExecutionTargetLocationsTypeDef(
    _ClientStartAutomationExecutionTargetLocationsTypeDef
):
    """
    - *(dict) --*

      The combination of AWS Regions and accounts targeted by the current Automation execution.
      - **Accounts** *(list) --*

        The AWS accounts targeted by the current Automation execution.
        - *(string) --*
    """


_ClientStartAutomationExecutionTargetsTypeDef = TypedDict(
    "_ClientStartAutomationExecutionTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientStartAutomationExecutionTargetsTypeDef(_ClientStartAutomationExecutionTargetsTypeDef):
    """
    - *(dict) --*

      An array of search criteria that targets instances using a Key,Value combination that you
      specify.
      Supported formats include the following.
      * ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
      * ``Key=tag:*my-tag-key* ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
      * ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
      * (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
      For example:
      * ``Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE``
      * ``Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3``
      * ``Key=tag-key,Values=Name,Instance-Type,CostCenter``
      * (Maintenance window targets only)
      ``Key=resource-groups:Name,Values=
          ProductionResourceGroup``   This example demonstrates how to
      target all resources in the resource group **ProductionResourceGroup** in your maintenance
      window.
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``
      This example demonstrates how to target only Amazon EC2 instances and VPCs in your maintenance
      window.
      * (State Manager association targets only) ``Key=InstanceIds,Values=*``   This example
      demonstrates how to target all managed instances in the AWS Region where the association was
      created.
      For information about how to send commands that target instances using ``Key,Value``
      parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet
      <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__
      in the *AWS Systems Manager User Guide* .
      - **Key** *(string) --*

        User-defined criteria for sending commands that target instances that meet the criteria.
    """


_ClientStartSessionResponseTypeDef = TypedDict(
    "_ClientStartSessionResponseTypeDef",
    {"SessionId": str, "TokenValue": str, "StreamUrl": str},
    total=False,
)


class ClientStartSessionResponseTypeDef(_ClientStartSessionResponseTypeDef):
    """
    - *(dict) --*

      - **SessionId** *(string) --*

        The ID of the session.
    """


_ClientTerminateSessionResponseTypeDef = TypedDict(
    "_ClientTerminateSessionResponseTypeDef", {"SessionId": str}, total=False
)


class ClientTerminateSessionResponseTypeDef(_ClientTerminateSessionResponseTypeDef):
    """
    - *(dict) --*

      - **SessionId** *(string) --*

        The ID of the session that has been terminated.
    """


_ClientUpdateAssociationOutputLocationS3LocationTypeDef = TypedDict(
    "_ClientUpdateAssociationOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)


class ClientUpdateAssociationOutputLocationS3LocationTypeDef(
    _ClientUpdateAssociationOutputLocationS3LocationTypeDef
):
    """
    - **S3Location** *(dict) --*

      An Amazon S3 bucket where you want to store the results of this request.
      - **OutputS3Region** *(string) --*

        (Deprecated) You can no longer specify this parameter. The system ignores it. Instead,
        Systems Manager automatically determines the Amazon S3 bucket region.
    """


_ClientUpdateAssociationOutputLocationTypeDef = TypedDict(
    "_ClientUpdateAssociationOutputLocationTypeDef",
    {"S3Location": ClientUpdateAssociationOutputLocationS3LocationTypeDef},
    total=False,
)


class ClientUpdateAssociationOutputLocationTypeDef(_ClientUpdateAssociationOutputLocationTypeDef):
    """
    An Amazon S3 bucket where you want to store the results of this request.
    - **S3Location** *(dict) --*

      An Amazon S3 bucket where you want to store the results of this request.
      - **OutputS3Region** *(string) --*

        (Deprecated) You can no longer specify this parameter. The system ignores it. Instead,
        Systems Manager automatically determines the Amazon S3 bucket region.
    """


_ClientUpdateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef = TypedDict(
    "_ClientUpdateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)


class ClientUpdateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef(
    _ClientUpdateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef
):
    pass


_ClientUpdateAssociationResponseAssociationDescriptionOutputLocationTypeDef = TypedDict(
    "_ClientUpdateAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    {
        "S3Location": ClientUpdateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef
    },
    total=False,
)


class ClientUpdateAssociationResponseAssociationDescriptionOutputLocationTypeDef(
    _ClientUpdateAssociationResponseAssociationDescriptionOutputLocationTypeDef
):
    pass


_ClientUpdateAssociationResponseAssociationDescriptionOverviewTypeDef = TypedDict(
    "_ClientUpdateAssociationResponseAssociationDescriptionOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)


class ClientUpdateAssociationResponseAssociationDescriptionOverviewTypeDef(
    _ClientUpdateAssociationResponseAssociationDescriptionOverviewTypeDef
):
    pass


_ClientUpdateAssociationResponseAssociationDescriptionStatusTypeDef = TypedDict(
    "_ClientUpdateAssociationResponseAssociationDescriptionStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)


class ClientUpdateAssociationResponseAssociationDescriptionStatusTypeDef(
    _ClientUpdateAssociationResponseAssociationDescriptionStatusTypeDef
):
    pass


_ClientUpdateAssociationResponseAssociationDescriptionTargetsTypeDef = TypedDict(
    "_ClientUpdateAssociationResponseAssociationDescriptionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientUpdateAssociationResponseAssociationDescriptionTargetsTypeDef(
    _ClientUpdateAssociationResponseAssociationDescriptionTargetsTypeDef
):
    pass


_ClientUpdateAssociationResponseAssociationDescriptionTypeDef = TypedDict(
    "_ClientUpdateAssociationResponseAssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientUpdateAssociationResponseAssociationDescriptionStatusTypeDef,
        "Overview": ClientUpdateAssociationResponseAssociationDescriptionOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientUpdateAssociationResponseAssociationDescriptionTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientUpdateAssociationResponseAssociationDescriptionOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)


class ClientUpdateAssociationResponseAssociationDescriptionTypeDef(
    _ClientUpdateAssociationResponseAssociationDescriptionTypeDef
):
    """
    - **AssociationDescription** *(dict) --*

      The description of the association that was updated.
      - **Name** *(string) --*

        The name of the Systems Manager document.
    """


_ClientUpdateAssociationResponseTypeDef = TypedDict(
    "_ClientUpdateAssociationResponseTypeDef",
    {"AssociationDescription": ClientUpdateAssociationResponseAssociationDescriptionTypeDef},
    total=False,
)


class ClientUpdateAssociationResponseTypeDef(_ClientUpdateAssociationResponseTypeDef):
    """
    - *(dict) --*

      - **AssociationDescription** *(dict) --*

        The description of the association that was updated.
        - **Name** *(string) --*

          The name of the Systems Manager document.
    """


_RequiredClientUpdateAssociationStatusAssociationStatusTypeDef = TypedDict(
    "_RequiredClientUpdateAssociationStatusAssociationStatusTypeDef", {"Date": datetime}
)
_OptionalClientUpdateAssociationStatusAssociationStatusTypeDef = TypedDict(
    "_OptionalClientUpdateAssociationStatusAssociationStatusTypeDef",
    {"Name": Literal["Pending", "Success", "Failed"], "Message": str, "AdditionalInfo": str},
    total=False,
)


class ClientUpdateAssociationStatusAssociationStatusTypeDef(
    _RequiredClientUpdateAssociationStatusAssociationStatusTypeDef,
    _OptionalClientUpdateAssociationStatusAssociationStatusTypeDef,
):
    """
    The association status.
    - **Date** *(datetime) --***[REQUIRED]**

      The date when the status changed.
    """


_ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationS3LocationTypeDef = TypedDict(
    "_ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)


class ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationS3LocationTypeDef(
    _ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationS3LocationTypeDef
):
    pass


_ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationTypeDef = TypedDict(
    "_ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationTypeDef",
    {
        "S3Location": ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationS3LocationTypeDef
    },
    total=False,
)


class ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationTypeDef(
    _ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationTypeDef
):
    pass


_ClientUpdateAssociationStatusResponseAssociationDescriptionOverviewTypeDef = TypedDict(
    "_ClientUpdateAssociationStatusResponseAssociationDescriptionOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)


class ClientUpdateAssociationStatusResponseAssociationDescriptionOverviewTypeDef(
    _ClientUpdateAssociationStatusResponseAssociationDescriptionOverviewTypeDef
):
    pass


_ClientUpdateAssociationStatusResponseAssociationDescriptionStatusTypeDef = TypedDict(
    "_ClientUpdateAssociationStatusResponseAssociationDescriptionStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)


class ClientUpdateAssociationStatusResponseAssociationDescriptionStatusTypeDef(
    _ClientUpdateAssociationStatusResponseAssociationDescriptionStatusTypeDef
):
    pass


_ClientUpdateAssociationStatusResponseAssociationDescriptionTargetsTypeDef = TypedDict(
    "_ClientUpdateAssociationStatusResponseAssociationDescriptionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientUpdateAssociationStatusResponseAssociationDescriptionTargetsTypeDef(
    _ClientUpdateAssociationStatusResponseAssociationDescriptionTargetsTypeDef
):
    pass


_ClientUpdateAssociationStatusResponseAssociationDescriptionTypeDef = TypedDict(
    "_ClientUpdateAssociationStatusResponseAssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientUpdateAssociationStatusResponseAssociationDescriptionStatusTypeDef,
        "Overview": ClientUpdateAssociationStatusResponseAssociationDescriptionOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientUpdateAssociationStatusResponseAssociationDescriptionTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)


class ClientUpdateAssociationStatusResponseAssociationDescriptionTypeDef(
    _ClientUpdateAssociationStatusResponseAssociationDescriptionTypeDef
):
    """
    - **AssociationDescription** *(dict) --*

      Information about the association.
      - **Name** *(string) --*

        The name of the Systems Manager document.
    """


_ClientUpdateAssociationStatusResponseTypeDef = TypedDict(
    "_ClientUpdateAssociationStatusResponseTypeDef",
    {"AssociationDescription": ClientUpdateAssociationStatusResponseAssociationDescriptionTypeDef},
    total=False,
)


class ClientUpdateAssociationStatusResponseTypeDef(_ClientUpdateAssociationStatusResponseTypeDef):
    """
    - *(dict) --*

      - **AssociationDescription** *(dict) --*

        Information about the association.
        - **Name** *(string) --*

          The name of the Systems Manager document.
    """


_ClientUpdateAssociationTargetsTypeDef = TypedDict(
    "_ClientUpdateAssociationTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientUpdateAssociationTargetsTypeDef(_ClientUpdateAssociationTargetsTypeDef):
    """
    - *(dict) --*

      An array of search criteria that targets instances using a Key,Value combination that you
      specify.
      Supported formats include the following.
      * ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
      * ``Key=tag:*my-tag-key* ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
      * ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
      * (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
      For example:
      * ``Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE``
      * ``Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3``
      * ``Key=tag-key,Values=Name,Instance-Type,CostCenter``
      * (Maintenance window targets only)
      ``Key=resource-groups:Name,Values=
          ProductionResourceGroup``   This example demonstrates how to
      target all resources in the resource group **ProductionResourceGroup** in your maintenance
      window.
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``
      This example demonstrates how to target only Amazon EC2 instances and VPCs in your maintenance
      window.
      * (State Manager association targets only) ``Key=InstanceIds,Values=*``   This example
      demonstrates how to target all managed instances in the AWS Region where the association was
      created.
      For information about how to send commands that target instances using ``Key,Value``
      parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet
      <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__
      in the *AWS Systems Manager User Guide* .
      - **Key** *(string) --*

        User-defined criteria for sending commands that target instances that meet the criteria.
    """


_ClientUpdateDocumentAttachmentsTypeDef = TypedDict(
    "_ClientUpdateDocumentAttachmentsTypeDef",
    {"Key": Literal["SourceUrl", "S3FileUrl"], "Values": List[str], "Name": str},
    total=False,
)


class ClientUpdateDocumentAttachmentsTypeDef(_ClientUpdateDocumentAttachmentsTypeDef):
    """
    - *(dict) --*

      Identifying information about a document attachment, including the file name and a key-value
      pair that identifies the location of an attachment to a document.
      - **Key** *(string) --*

        The key of a key-value pair that identifies the location of an attachment to a document.
    """


_ClientUpdateDocumentDefaultVersionResponseDescriptionTypeDef = TypedDict(
    "_ClientUpdateDocumentDefaultVersionResponseDescriptionTypeDef",
    {"Name": str, "DefaultVersion": str, "DefaultVersionName": str},
    total=False,
)


class ClientUpdateDocumentDefaultVersionResponseDescriptionTypeDef(
    _ClientUpdateDocumentDefaultVersionResponseDescriptionTypeDef
):
    """
    - **Description** *(dict) --*

      The description of a custom document that you want to set as the default version.
      - **Name** *(string) --*

        The name of the document.
    """


_ClientUpdateDocumentDefaultVersionResponseTypeDef = TypedDict(
    "_ClientUpdateDocumentDefaultVersionResponseTypeDef",
    {"Description": ClientUpdateDocumentDefaultVersionResponseDescriptionTypeDef},
    total=False,
)


class ClientUpdateDocumentDefaultVersionResponseTypeDef(
    _ClientUpdateDocumentDefaultVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **Description** *(dict) --*

        The description of a custom document that you want to set as the default version.
        - **Name** *(string) --*

          The name of the document.
    """


_ClientUpdateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef = TypedDict(
    "_ClientUpdateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef",
    {"Name": str},
    total=False,
)


class ClientUpdateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef(
    _ClientUpdateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef
):
    pass


_ClientUpdateDocumentResponseDocumentDescriptionParametersTypeDef = TypedDict(
    "_ClientUpdateDocumentResponseDocumentDescriptionParametersTypeDef",
    {"Name": str, "Type": Literal["String", "StringList"], "Description": str, "DefaultValue": str},
    total=False,
)


class ClientUpdateDocumentResponseDocumentDescriptionParametersTypeDef(
    _ClientUpdateDocumentResponseDocumentDescriptionParametersTypeDef
):
    pass


_ClientUpdateDocumentResponseDocumentDescriptionRequiresTypeDef = TypedDict(
    "_ClientUpdateDocumentResponseDocumentDescriptionRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientUpdateDocumentResponseDocumentDescriptionRequiresTypeDef(
    _ClientUpdateDocumentResponseDocumentDescriptionRequiresTypeDef
):
    pass


_ClientUpdateDocumentResponseDocumentDescriptionTagsTypeDef = TypedDict(
    "_ClientUpdateDocumentResponseDocumentDescriptionTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateDocumentResponseDocumentDescriptionTagsTypeDef(
    _ClientUpdateDocumentResponseDocumentDescriptionTagsTypeDef
):
    pass


_ClientUpdateDocumentResponseDocumentDescriptionTypeDef = TypedDict(
    "_ClientUpdateDocumentResponseDocumentDescriptionTypeDef",
    {
        "Sha1": str,
        "Hash": str,
        "HashType": Literal["Sha256", "Sha1"],
        "Name": str,
        "VersionName": str,
        "Owner": str,
        "CreatedDate": datetime,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "DocumentVersion": str,
        "Description": str,
        "Parameters": List[ClientUpdateDocumentResponseDocumentDescriptionParametersTypeDef],
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
        ],
        "SchemaVersion": str,
        "LatestVersion": str,
        "DefaultVersion": str,
        "DocumentFormat": Literal["YAML", "JSON"],
        "TargetType": str,
        "Tags": List[ClientUpdateDocumentResponseDocumentDescriptionTagsTypeDef],
        "AttachmentsInformation": List[
            ClientUpdateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef
        ],
        "Requires": List[ClientUpdateDocumentResponseDocumentDescriptionRequiresTypeDef],
    },
    total=False,
)


class ClientUpdateDocumentResponseDocumentDescriptionTypeDef(
    _ClientUpdateDocumentResponseDocumentDescriptionTypeDef
):
    """
    - **DocumentDescription** *(dict) --*

      A description of the document that was updated.
      - **Sha1** *(string) --*

        The SHA1 hash of the document, which you can use for verification.
    """


_ClientUpdateDocumentResponseTypeDef = TypedDict(
    "_ClientUpdateDocumentResponseTypeDef",
    {"DocumentDescription": ClientUpdateDocumentResponseDocumentDescriptionTypeDef},
    total=False,
)


class ClientUpdateDocumentResponseTypeDef(_ClientUpdateDocumentResponseTypeDef):
    """
    - *(dict) --*

      - **DocumentDescription** *(dict) --*

        A description of the document that was updated.
        - **Sha1** *(string) --*

          The SHA1 hash of the document, which you can use for verification.
    """


_ClientUpdateMaintenanceWindowResponseTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowResponseTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
    },
    total=False,
)


class ClientUpdateMaintenanceWindowResponseTypeDef(_ClientUpdateMaintenanceWindowResponseTypeDef):
    """
    - *(dict) --*

      - **WindowId** *(string) --*

        The ID of the created maintenance window.
    """


_ClientUpdateMaintenanceWindowTargetResponseTargetsTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTargetResponseTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientUpdateMaintenanceWindowTargetResponseTargetsTypeDef(
    _ClientUpdateMaintenanceWindowTargetResponseTargetsTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTargetResponseTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTargetResponseTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "Targets": List[ClientUpdateMaintenanceWindowTargetResponseTargetsTypeDef],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)


class ClientUpdateMaintenanceWindowTargetResponseTypeDef(
    _ClientUpdateMaintenanceWindowTargetResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowId** *(string) --*

        The maintenance window ID specified in the update request.
    """


_ClientUpdateMaintenanceWindowTargetTargetsTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTargetTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientUpdateMaintenanceWindowTargetTargetsTypeDef(
    _ClientUpdateMaintenanceWindowTargetTargetsTypeDef
):
    """
    - *(dict) --*

      An array of search criteria that targets instances using a Key,Value combination that you
      specify.
      Supported formats include the following.
      * ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
      * ``Key=tag:*my-tag-key* ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
      * ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
      * (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
      For example:
      * ``Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE``
      * ``Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3``
      * ``Key=tag-key,Values=Name,Instance-Type,CostCenter``
      * (Maintenance window targets only)
      ``Key=resource-groups:Name,Values=
          ProductionResourceGroup``   This example demonstrates how to
      target all resources in the resource group **ProductionResourceGroup** in your maintenance
      window.
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``
      This example demonstrates how to target only Amazon EC2 instances and VPCs in your maintenance
      window.
      * (State Manager association targets only) ``Key=InstanceIds,Values=*``   This example
      demonstrates how to target all managed instances in the AWS Region where the association was
      created.
      For information about how to send commands that target instances using ``Key,Value``
      parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet
      <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__
      in the *AWS Systems Manager User Guide* .
      - **Key** *(string) --*

        User-defined criteria for sending commands that target instances that meet the criteria.
    """


_ClientUpdateMaintenanceWindowTaskLoggingInfoTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)


class ClientUpdateMaintenanceWindowTaskLoggingInfoTypeDef(
    _ClientUpdateMaintenanceWindowTaskLoggingInfoTypeDef
):
    """
    The new logging location in Amazon S3 to specify.
    .. note::

      ``LoggingInfo`` has been deprecated. To specify an S3 bucket to contain logs, instead use the
      ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters``
      structure. For information about how Systems Manager handles these options for the supported
      maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .
    """


_ClientUpdateMaintenanceWindowTaskResponseLoggingInfoTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskResponseLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)


class ClientUpdateMaintenanceWindowTaskResponseLoggingInfoTypeDef(
    _ClientUpdateMaintenanceWindowTaskResponseLoggingInfoTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTaskResponseTargetsTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskResponseTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientUpdateMaintenanceWindowTaskResponseTargetsTypeDef(
    _ClientUpdateMaintenanceWindowTaskResponseTargetsTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)


class ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef(
    _ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": bytes},
    total=False,
)


class ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef(
    _ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)


class ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef(
    _ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef",
    {
        "Comment": str,
        "DocumentHash": str,
        "DocumentHashType": Literal["Sha256", "Sha1"],
        "NotificationConfig": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)


class ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef(
    _ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef",
    {"Input": str, "Name": str},
    total=False,
)


class ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef(
    _ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef",
    {
        "RunCommand": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef,
        "Automation": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef,
        "StepFunctions": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef,
        "Lambda": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef,
    },
    total=False,
)


class ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef(
    _ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTaskResponseTaskParametersTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskResponseTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientUpdateMaintenanceWindowTaskResponseTaskParametersTypeDef(
    _ClientUpdateMaintenanceWindowTaskResponseTaskParametersTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTaskResponseTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskResponseTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List[ClientUpdateMaintenanceWindowTaskResponseTargetsTypeDef],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskParameters": Dict[str, ClientUpdateMaintenanceWindowTaskResponseTaskParametersTypeDef],
        "TaskInvocationParameters": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef,
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": ClientUpdateMaintenanceWindowTaskResponseLoggingInfoTypeDef,
        "Name": str,
        "Description": str,
    },
    total=False,
)


class ClientUpdateMaintenanceWindowTaskResponseTypeDef(
    _ClientUpdateMaintenanceWindowTaskResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowId** *(string) --*

        The ID of the maintenance window that was updated.
    """


_ClientUpdateMaintenanceWindowTaskTargetsTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientUpdateMaintenanceWindowTaskTargetsTypeDef(
    _ClientUpdateMaintenanceWindowTaskTargetsTypeDef
):
    """
    - *(dict) --*

      An array of search criteria that targets instances using a Key,Value combination that you
      specify.
      Supported formats include the following.
      * ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
      * ``Key=tag:*my-tag-key* ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
      * ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
      * (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
      For example:
      * ``Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE``
      * ``Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3``
      * ``Key=tag-key,Values=Name,Instance-Type,CostCenter``
      * (Maintenance window targets only)
      ``Key=resource-groups:Name,Values=
          ProductionResourceGroup``   This example demonstrates how to
      target all resources in the resource group **ProductionResourceGroup** in your maintenance
      window.
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``
      This example demonstrates how to target only Amazon EC2 instances and VPCs in your maintenance
      window.
      * (State Manager association targets only) ``Key=InstanceIds,Values=*``   This example
      demonstrates how to target all managed instances in the AWS Region where the association was
      created.
      For information about how to send commands that target instances using ``Key,Value``
      parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet
      <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__
      in the *AWS Systems Manager User Guide* .
      - **Key** *(string) --*

        User-defined criteria for sending commands that target instances that meet the criteria.
    """


_ClientUpdateMaintenanceWindowTaskTaskInvocationParametersAutomationTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskTaskInvocationParametersAutomationTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)


class ClientUpdateMaintenanceWindowTaskTaskInvocationParametersAutomationTypeDef(
    _ClientUpdateMaintenanceWindowTaskTaskInvocationParametersAutomationTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTaskTaskInvocationParametersLambdaTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskTaskInvocationParametersLambdaTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": bytes},
    total=False,
)


class ClientUpdateMaintenanceWindowTaskTaskInvocationParametersLambdaTypeDef(
    _ClientUpdateMaintenanceWindowTaskTaskInvocationParametersLambdaTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandNotificationConfigTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)


class ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandNotificationConfigTypeDef(
    _ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandNotificationConfigTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandTypeDef",
    {
        "Comment": str,
        "DocumentHash": str,
        "DocumentHashType": Literal["Sha256", "Sha1"],
        "NotificationConfig": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandNotificationConfigTypeDef,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)


class ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandTypeDef(
    _ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandTypeDef
):
    """
    - **RunCommand** *(dict) --*

      The parameters for a RUN_COMMAND task type.
      - **Comment** *(string) --*

        Information about the commands to run.
    """


_ClientUpdateMaintenanceWindowTaskTaskInvocationParametersStepFunctionsTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskTaskInvocationParametersStepFunctionsTypeDef",
    {"Input": str, "Name": str},
    total=False,
)


class ClientUpdateMaintenanceWindowTaskTaskInvocationParametersStepFunctionsTypeDef(
    _ClientUpdateMaintenanceWindowTaskTaskInvocationParametersStepFunctionsTypeDef
):
    pass


_ClientUpdateMaintenanceWindowTaskTaskInvocationParametersTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskTaskInvocationParametersTypeDef",
    {
        "RunCommand": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandTypeDef,
        "Automation": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersAutomationTypeDef,
        "StepFunctions": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersStepFunctionsTypeDef,
        "Lambda": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersLambdaTypeDef,
    },
    total=False,
)


class ClientUpdateMaintenanceWindowTaskTaskInvocationParametersTypeDef(
    _ClientUpdateMaintenanceWindowTaskTaskInvocationParametersTypeDef
):
    """
    The parameters that the task should use during execution. Populate only the fields that match
    the task type. All other fields should be empty.
    - **RunCommand** *(dict) --*

      The parameters for a RUN_COMMAND task type.
      - **Comment** *(string) --*

        Information about the commands to run.
    """


_ClientUpdateMaintenanceWindowTaskTaskParametersTypeDef = TypedDict(
    "_ClientUpdateMaintenanceWindowTaskTaskParametersTypeDef", {"Values": List[str]}, total=False
)


class ClientUpdateMaintenanceWindowTaskTaskParametersTypeDef(
    _ClientUpdateMaintenanceWindowTaskTaskParametersTypeDef
):
    pass


_ClientUpdateOpsItemNotificationsTypeDef = TypedDict(
    "_ClientUpdateOpsItemNotificationsTypeDef", {"Arn": str}, total=False
)


class ClientUpdateOpsItemNotificationsTypeDef(_ClientUpdateOpsItemNotificationsTypeDef):
    """
    - *(dict) --*

      A notification about the OpsItem.
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this
        OpsItem is edited or changed.
    """


_ClientUpdateOpsItemOperationalDataTypeDef = TypedDict(
    "_ClientUpdateOpsItemOperationalDataTypeDef",
    {"Value": str, "Type": Literal["SearchableString", "String"]},
    total=False,
)


class ClientUpdateOpsItemOperationalDataTypeDef(_ClientUpdateOpsItemOperationalDataTypeDef):
    pass


_ClientUpdateOpsItemRelatedOpsItemsTypeDef = TypedDict(
    "_ClientUpdateOpsItemRelatedOpsItemsTypeDef", {"OpsItemId": str}
)


class ClientUpdateOpsItemRelatedOpsItemsTypeDef(_ClientUpdateOpsItemRelatedOpsItemsTypeDef):
    """
    - *(dict) --*

      An OpsItems that shares something in common with the current OpsItem. For example, related
      OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for
      the impacted resource.
      - **OpsItemId** *(string) --***[REQUIRED]**

        The ID of an OpsItem related to the current OpsItem.
    """


_RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ]
    },
)
_OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef(
    _RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef,
    _OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef,
):
    """
    - *(dict) --*

      Defines which patches should be included in a patch baseline.
      A patch filter consists of a key and a set of values. The filter key is a patch property. For
      example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY,
      CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the patch
      property indicated by the key. For example, if the filter key is PRODUCT and the filter values
      are ["Office 2013", "Office 2016"], then the filter accepts all patches where product name is
      either "Office 2013" or "Office 2016". The filter values can be exact values for the patch
      property given as a key, or a wildcard (*), which matches all values.
      You can view lists of valid values for the patch properties by running the
      ``DescribePatchProperties`` command. For information about which patch properties can be used
      with each major operating system, see  DescribePatchProperties .
      - **Key** *(string) --***[REQUIRED]**

        The key for the filter.
        Run the  DescribePatchProperties command to view lists of valid keys for each operating
        system type.
    """


_ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef = TypedDict(
    "_ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    {
        "PatchFilters": List[
            ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
        ]
    },
)


class ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef(
    _ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef
):
    """
    - **PatchFilterGroup** *(dict) --***[REQUIRED]**

      The patch filter group that defines the criteria for the rule.
      - **PatchFilters** *(list) --***[REQUIRED]**

        The set of patch filters that make up the group.
        - *(dict) --*

          Defines which patches should be included in a patch baseline.
          A patch filter consists of a key and a set of values. The filter key is a patch property.
          For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY,
          CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the
          patch property indicated by the key. For example, if the filter key is PRODUCT and the
          filter values are ["Office 2013", "Office 2016"], then the filter accepts all patches
          where product name is either "Office 2013" or "Office 2016". The filter values can be
          exact values for the patch property given as a key, or a wildcard (*), which matches all
          values.
          You can view lists of valid values for the patch properties by running the
          ``DescribePatchProperties`` command. For information about which patch properties can be
          used with each major operating system, see  DescribePatchProperties .
          - **Key** *(string) --***[REQUIRED]**

            The key for the filter.
            Run the  DescribePatchProperties command to view lists of valid keys for each operating
            system type.
    """


_RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef = TypedDict(
    "_RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef",
    {"PatchFilterGroup": ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef},
)
_OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef = TypedDict(
    "_OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef",
    {
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApproveAfterDays": int,
        "EnableNonSecurity": bool,
    },
    total=False,
)


class ClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef(
    _RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef,
    _OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef,
):
    """
    - *(dict) --*

      Defines an approval rule for a patch baseline.
      - **PatchFilterGroup** *(dict) --***[REQUIRED]**

        The patch filter group that defines the criteria for the rule.
        - **PatchFilters** *(list) --***[REQUIRED]**

          The set of patch filters that make up the group.
          - *(dict) --*

            Defines which patches should be included in a patch baseline.
            A patch filter consists of a key and a set of values. The filter key is a patch
            property. For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT,
            PRODUCT_FAMILY, CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching
            criterion for the patch property indicated by the key. For example, if the filter key is
            PRODUCT and the filter values are ["Office 2013", "Office 2016"], then the filter
            accepts all patches where product name is either "Office 2013" or "Office 2016". The
            filter values can be exact values for the patch property given as a key, or a wildcard
            (*), which matches all values.
            You can view lists of valid values for the patch properties by running the
            ``DescribePatchProperties`` command. For information about which patch properties can be
            used with each major operating system, see  DescribePatchProperties .
            - **Key** *(string) --***[REQUIRED]**

              The key for the filter.
              Run the  DescribePatchProperties command to view lists of valid keys for each
              operating system type.
    """


_ClientUpdatePatchBaselineApprovalRulesTypeDef = TypedDict(
    "_ClientUpdatePatchBaselineApprovalRulesTypeDef",
    {"PatchRules": List[ClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef]},
)


class ClientUpdatePatchBaselineApprovalRulesTypeDef(_ClientUpdatePatchBaselineApprovalRulesTypeDef):
    """
    A set of rules used to include patches in the baseline.
    - **PatchRules** *(list) --***[REQUIRED]**

      The rules that make up the rule group.
      - *(dict) --*

        Defines an approval rule for a patch baseline.
        - **PatchFilterGroup** *(dict) --***[REQUIRED]**

          The patch filter group that defines the criteria for the rule.
          - **PatchFilters** *(list) --***[REQUIRED]**

            The set of patch filters that make up the group.
            - *(dict) --*

              Defines which patches should be included in a patch baseline.
              A patch filter consists of a key and a set of values. The filter key is a patch
              property. For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT,
              PRODUCT_FAMILY, CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching
              criterion for the patch property indicated by the key. For example, if the filter key
              is PRODUCT and the filter values are ["Office 2013", "Office 2016"], then the filter
              accepts all patches where product name is either "Office 2013" or "Office 2016". The
              filter values can be exact values for the patch property given as a key, or a wildcard
              (*), which matches all values.
              You can view lists of valid values for the patch properties by running the
              ``DescribePatchProperties`` command. For information about which patch properties can
              be used with each major operating system, see  DescribePatchProperties .
              - **Key** *(string) --***[REQUIRED]**

                The key for the filter.
                Run the  DescribePatchProperties command to view lists of valid keys for each
                operating system type.
    """


_RequiredClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_RequiredClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ]
    },
)
_OptionalClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_OptionalClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef(
    _RequiredClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef,
    _OptionalClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef,
):
    """
    - *(dict) --*

      Defines which patches should be included in a patch baseline.
      A patch filter consists of a key and a set of values. The filter key is a patch property. For
      example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY,
      CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the patch
      property indicated by the key. For example, if the filter key is PRODUCT and the filter values
      are ["Office 2013", "Office 2016"], then the filter accepts all patches where product name is
      either "Office 2013" or "Office 2016". The filter values can be exact values for the patch
      property given as a key, or a wildcard (*), which matches all values.
      You can view lists of valid values for the patch properties by running the
      ``DescribePatchProperties`` command. For information about which patch properties can be used
      with each major operating system, see  DescribePatchProperties .
      - **Key** *(string) --***[REQUIRED]**

        The key for the filter.
        Run the  DescribePatchProperties command to view lists of valid keys for each operating
        system type.
    """


_ClientUpdatePatchBaselineGlobalFiltersTypeDef = TypedDict(
    "_ClientUpdatePatchBaselineGlobalFiltersTypeDef",
    {"PatchFilters": List[ClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef]},
)


class ClientUpdatePatchBaselineGlobalFiltersTypeDef(_ClientUpdatePatchBaselineGlobalFiltersTypeDef):
    """
    A set of global filters used to include patches in the baseline.
    - **PatchFilters** *(list) --***[REQUIRED]**

      The set of patch filters that make up the group.
      - *(dict) --*

        Defines which patches should be included in a patch baseline.
        A patch filter consists of a key and a set of values. The filter key is a patch property.
        For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY,
        CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the
        patch property indicated by the key. For example, if the filter key is PRODUCT and the
        filter values are ["Office 2013", "Office 2016"], then the filter accepts all patches where
        product name is either "Office 2013" or "Office 2016". The filter values can be exact values
        for the patch property given as a key, or a wildcard (*), which matches all values.
        You can view lists of valid values for the patch properties by running the
        ``DescribePatchProperties`` command. For information about which patch properties can be
        used with each major operating system, see  DescribePatchProperties .
        - **Key** *(string) --***[REQUIRED]**

          The key for the filter.
          Run the  DescribePatchProperties command to view lists of valid keys for each operating
          system type.
    """


_ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef(
    _ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
):
    pass


_ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef = TypedDict(
    "_ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    {
        "PatchFilters": List[
            ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
        ]
    },
    total=False,
)


class ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef(
    _ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef
):
    pass


_ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesTypeDef = TypedDict(
    "_ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesTypeDef",
    {
        "PatchFilterGroup": ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef,
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApproveAfterDays": int,
        "EnableNonSecurity": bool,
    },
    total=False,
)


class ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesTypeDef(
    _ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesTypeDef
):
    pass


_ClientUpdatePatchBaselineResponseApprovalRulesTypeDef = TypedDict(
    "_ClientUpdatePatchBaselineResponseApprovalRulesTypeDef",
    {"PatchRules": List[ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesTypeDef]},
    total=False,
)


class ClientUpdatePatchBaselineResponseApprovalRulesTypeDef(
    _ClientUpdatePatchBaselineResponseApprovalRulesTypeDef
):
    pass


_ClientUpdatePatchBaselineResponseGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_ClientUpdatePatchBaselineResponseGlobalFiltersPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientUpdatePatchBaselineResponseGlobalFiltersPatchFiltersTypeDef(
    _ClientUpdatePatchBaselineResponseGlobalFiltersPatchFiltersTypeDef
):
    pass


_ClientUpdatePatchBaselineResponseGlobalFiltersTypeDef = TypedDict(
    "_ClientUpdatePatchBaselineResponseGlobalFiltersTypeDef",
    {"PatchFilters": List[ClientUpdatePatchBaselineResponseGlobalFiltersPatchFiltersTypeDef]},
    total=False,
)


class ClientUpdatePatchBaselineResponseGlobalFiltersTypeDef(
    _ClientUpdatePatchBaselineResponseGlobalFiltersTypeDef
):
    pass


_ClientUpdatePatchBaselineResponseSourcesTypeDef = TypedDict(
    "_ClientUpdatePatchBaselineResponseSourcesTypeDef",
    {"Name": str, "Products": List[str], "Configuration": str},
    total=False,
)


class ClientUpdatePatchBaselineResponseSourcesTypeDef(
    _ClientUpdatePatchBaselineResponseSourcesTypeDef
):
    pass


_ClientUpdatePatchBaselineResponseTypeDef = TypedDict(
    "_ClientUpdatePatchBaselineResponseTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "GlobalFilters": ClientUpdatePatchBaselineResponseGlobalFiltersTypeDef,
        "ApprovalRules": ClientUpdatePatchBaselineResponseApprovalRulesTypeDef,
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": Literal["ALLOW_AS_DEPENDENCY", "BLOCK"],
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List[ClientUpdatePatchBaselineResponseSourcesTypeDef],
    },
    total=False,
)


class ClientUpdatePatchBaselineResponseTypeDef(_ClientUpdatePatchBaselineResponseTypeDef):
    """
    - *(dict) --*

      - **BaselineId** *(string) --*

        The ID of the deleted patch baseline.
    """


_RequiredClientUpdatePatchBaselineSourcesTypeDef = TypedDict(
    "_RequiredClientUpdatePatchBaselineSourcesTypeDef", {"Name": str}
)
_OptionalClientUpdatePatchBaselineSourcesTypeDef = TypedDict(
    "_OptionalClientUpdatePatchBaselineSourcesTypeDef",
    {"Products": List[str], "Configuration": str},
    total=False,
)


class ClientUpdatePatchBaselineSourcesTypeDef(
    _RequiredClientUpdatePatchBaselineSourcesTypeDef,
    _OptionalClientUpdatePatchBaselineSourcesTypeDef,
):
    """
    - *(dict) --*

      Information about the patches to use to update the instances, including target operating
      systems and source repository. Applies to Linux instances only.
      - **Name** *(string) --***[REQUIRED]**

        The name specified to identify the patch source.
    """


_ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef = TypedDict(
    "_ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    {"OrganizationalUnitId": str},
    total=False,
)


class ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef(
    _ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
):
    pass


_ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef = TypedDict(
    "_ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": List[
            ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef(
    _ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef
):
    pass


_RequiredClientUpdateResourceDataSyncSyncSourceTypeDef = TypedDict(
    "_RequiredClientUpdateResourceDataSyncSyncSourceTypeDef", {"SourceType": str}
)
_OptionalClientUpdateResourceDataSyncSyncSourceTypeDef = TypedDict(
    "_OptionalClientUpdateResourceDataSyncSyncSourceTypeDef",
    {
        "AwsOrganizationsSource": ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef,
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
    },
    total=False,
)


class ClientUpdateResourceDataSyncSyncSourceTypeDef(
    _RequiredClientUpdateResourceDataSyncSyncSourceTypeDef,
    _OptionalClientUpdateResourceDataSyncSyncSourceTypeDef,
):
    """
    Specify information about the data sources to synchronize.
    - **SourceType** *(string) --***[REQUIRED]**

      The type of data source for the resource data sync. ``SourceType`` is either
      ``AwsOrganizations`` (if an organization is present in AWS Organizations) or
      ``singleAccountMultiRegions`` .
    """


_DescribeActivationsPaginateFiltersTypeDef = TypedDict(
    "_DescribeActivationsPaginateFiltersTypeDef",
    {
        "FilterKey": Literal["ActivationIds", "DefaultInstanceName", "IamRole"],
        "FilterValues": List[str],
    },
    total=False,
)


class DescribeActivationsPaginateFiltersTypeDef(_DescribeActivationsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      Filter for the DescribeActivation API.
      - **FilterKey** *(string) --*

        The name of the filter.
    """


_DescribeActivationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeActivationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeActivationsPaginatePaginationConfigTypeDef(
    _DescribeActivationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeActivationsPaginateResponseActivationListTagsTypeDef = TypedDict(
    "_DescribeActivationsPaginateResponseActivationListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeActivationsPaginateResponseActivationListTagsTypeDef(
    _DescribeActivationsPaginateResponseActivationListTagsTypeDef
):
    pass


_DescribeActivationsPaginateResponseActivationListTypeDef = TypedDict(
    "_DescribeActivationsPaginateResponseActivationListTypeDef",
    {
        "ActivationId": str,
        "Description": str,
        "DefaultInstanceName": str,
        "IamRole": str,
        "RegistrationLimit": int,
        "RegistrationsCount": int,
        "ExpirationDate": datetime,
        "Expired": bool,
        "CreatedDate": datetime,
        "Tags": List[DescribeActivationsPaginateResponseActivationListTagsTypeDef],
    },
    total=False,
)


class DescribeActivationsPaginateResponseActivationListTypeDef(
    _DescribeActivationsPaginateResponseActivationListTypeDef
):
    """
    - *(dict) --*

      An activation registers one or more on-premises servers or virtual machines (VMs) with AWS so
      that you can configure those servers or VMs using Run Command. A server or VM that has been
      registered with AWS is called a managed instance.
      - **ActivationId** *(string) --*

        The ID created by Systems Manager when you submitted the activation.
    """


_DescribeActivationsPaginateResponseTypeDef = TypedDict(
    "_DescribeActivationsPaginateResponseTypeDef",
    {"ActivationList": List[DescribeActivationsPaginateResponseActivationListTypeDef]},
    total=False,
)


class DescribeActivationsPaginateResponseTypeDef(_DescribeActivationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ActivationList** *(list) --*

        A list of activations for your AWS account.
        - *(dict) --*

          An activation registers one or more on-premises servers or virtual machines (VMs) with AWS
          so that you can configure those servers or VMs using Run Command. A server or VM that has
          been registered with AWS is called a managed instance.
          - **ActivationId** *(string) --*

            The ID created by Systems Manager when you submitted the activation.
    """


_RequiredDescribeAssociationExecutionTargetsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeAssociationExecutionTargetsPaginateFiltersTypeDef",
    {"Key": Literal["Status", "ResourceId", "ResourceType"]},
)
_OptionalDescribeAssociationExecutionTargetsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeAssociationExecutionTargetsPaginateFiltersTypeDef",
    {"Value": str},
    total=False,
)


class DescribeAssociationExecutionTargetsPaginateFiltersTypeDef(
    _RequiredDescribeAssociationExecutionTargetsPaginateFiltersTypeDef,
    _OptionalDescribeAssociationExecutionTargetsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      Filters for the association execution.
      - **Key** *(string) --***[REQUIRED]**

        The key value used in the request.
    """


_DescribeAssociationExecutionTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAssociationExecutionTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAssociationExecutionTargetsPaginatePaginationConfigTypeDef(
    _DescribeAssociationExecutionTargetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsOutputSourceTypeDef = TypedDict(
    "_DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsOutputSourceTypeDef",
    {"OutputSourceId": str, "OutputSourceType": str},
    total=False,
)


class DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsOutputSourceTypeDef(
    _DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsOutputSourceTypeDef
):
    pass


_DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsTypeDef = TypedDict(
    "_DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "ResourceId": str,
        "ResourceType": str,
        "Status": str,
        "DetailedStatus": str,
        "LastExecutionDate": datetime,
        "OutputSource": DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsOutputSourceTypeDef,
    },
    total=False,
)


class DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsTypeDef(
    _DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsTypeDef
):
    """
    - *(dict) --*

      Includes information about the specified association execution.
      - **AssociationId** *(string) --*

        The association ID.
    """


_DescribeAssociationExecutionTargetsPaginateResponseTypeDef = TypedDict(
    "_DescribeAssociationExecutionTargetsPaginateResponseTypeDef",
    {
        "AssociationExecutionTargets": List[
            DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsTypeDef
        ]
    },
    total=False,
)


class DescribeAssociationExecutionTargetsPaginateResponseTypeDef(
    _DescribeAssociationExecutionTargetsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **AssociationExecutionTargets** *(list) --*

        Information about the execution.
        - *(dict) --*

          Includes information about the specified association execution.
          - **AssociationId** *(string) --*

            The association ID.
    """


_RequiredDescribeAssociationExecutionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeAssociationExecutionsPaginateFiltersTypeDef",
    {"Key": Literal["ExecutionId", "Status", "CreatedTime"]},
)
_OptionalDescribeAssociationExecutionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeAssociationExecutionsPaginateFiltersTypeDef",
    {"Value": str, "Type": Literal["EQUAL", "LESS_THAN", "GREATER_THAN"]},
    total=False,
)


class DescribeAssociationExecutionsPaginateFiltersTypeDef(
    _RequiredDescribeAssociationExecutionsPaginateFiltersTypeDef,
    _OptionalDescribeAssociationExecutionsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      Filters used in the request.
      - **Key** *(string) --***[REQUIRED]**

        The key value used in the request.
    """


_DescribeAssociationExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAssociationExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAssociationExecutionsPaginatePaginationConfigTypeDef(
    _DescribeAssociationExecutionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAssociationExecutionsPaginateResponseAssociationExecutionsTypeDef = TypedDict(
    "_DescribeAssociationExecutionsPaginateResponseAssociationExecutionsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "Status": str,
        "DetailedStatus": str,
        "CreatedTime": datetime,
        "LastExecutionDate": datetime,
        "ResourceCountByStatus": str,
    },
    total=False,
)


class DescribeAssociationExecutionsPaginateResponseAssociationExecutionsTypeDef(
    _DescribeAssociationExecutionsPaginateResponseAssociationExecutionsTypeDef
):
    """
    - *(dict) --*

      Includes information about the specified association.
      - **AssociationId** *(string) --*

        The association ID.
    """


_DescribeAssociationExecutionsPaginateResponseTypeDef = TypedDict(
    "_DescribeAssociationExecutionsPaginateResponseTypeDef",
    {
        "AssociationExecutions": List[
            DescribeAssociationExecutionsPaginateResponseAssociationExecutionsTypeDef
        ]
    },
    total=False,
)


class DescribeAssociationExecutionsPaginateResponseTypeDef(
    _DescribeAssociationExecutionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **AssociationExecutions** *(list) --*

        A list of the executions for the specified association ID.
        - *(dict) --*

          Includes information about the specified association.
          - **AssociationId** *(string) --*

            The association ID.
    """


_RequiredDescribeAutomationExecutionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeAutomationExecutionsPaginateFiltersTypeDef",
    {
        "Key": Literal[
            "DocumentNamePrefix",
            "ExecutionStatus",
            "ExecutionId",
            "ParentExecutionId",
            "CurrentAction",
            "StartTimeBefore",
            "StartTimeAfter",
            "AutomationType",
        ]
    },
)
_OptionalDescribeAutomationExecutionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeAutomationExecutionsPaginateFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeAutomationExecutionsPaginateFiltersTypeDef(
    _RequiredDescribeAutomationExecutionsPaginateFiltersTypeDef,
    _OptionalDescribeAutomationExecutionsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      A filter used to match specific automation executions. This is used to limit the scope of
      Automation execution information returned.
      - **Key** *(string) --***[REQUIRED]**

        One or more keys to limit the results. Valid filter keys include the following:
        DocumentNamePrefix, ExecutionStatus, ExecutionId, ParentExecutionId, CurrentAction,
        StartTimeBefore, StartTimeAfter.
    """


_DescribeAutomationExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAutomationExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAutomationExecutionsPaginatePaginationConfigTypeDef(
    _DescribeAutomationExecutionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListResolvedTargetsTypeDef = TypedDict(
    "_DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListResolvedTargetsTypeDef",
    {"ParameterValues": List[str], "Truncated": bool},
    total=False,
)


class DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListResolvedTargetsTypeDef(
    _DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListResolvedTargetsTypeDef
):
    pass


_DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTargetsTypeDef = TypedDict(
    "_DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTargetsTypeDef(
    _DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTargetsTypeDef
):
    pass


_DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTypeDef = TypedDict(
    "_DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "AutomationExecutionStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "ExecutedBy": str,
        "LogFile": str,
        "Outputs": Dict[str, List[str]],
        "Mode": Literal["Auto", "Interactive"],
        "ParentAutomationExecutionId": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "FailureMessage": str,
        "TargetParameterName": str,
        "Targets": List[
            DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTargetsTypeDef
        ],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListResolvedTargetsTypeDef,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "AutomationType": Literal["CrossAccount", "Local"],
    },
    total=False,
)


class DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTypeDef(
    _DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTypeDef
):
    """
    - *(dict) --*

      Details about a specific Automation execution.
      - **AutomationExecutionId** *(string) --*

        The execution ID.
    """


_DescribeAutomationExecutionsPaginateResponseTypeDef = TypedDict(
    "_DescribeAutomationExecutionsPaginateResponseTypeDef",
    {
        "AutomationExecutionMetadataList": List[
            DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTypeDef
        ]
    },
    total=False,
)


class DescribeAutomationExecutionsPaginateResponseTypeDef(
    _DescribeAutomationExecutionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **AutomationExecutionMetadataList** *(list) --*

        The list of details about each automation execution which has occurred which matches the
        filter specification, if any.
        - *(dict) --*

          Details about a specific Automation execution.
          - **AutomationExecutionId** *(string) --*

            The execution ID.
    """


_RequiredDescribeAutomationStepExecutionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeAutomationStepExecutionsPaginateFiltersTypeDef",
    {
        "Key": Literal[
            "StartTimeBefore",
            "StartTimeAfter",
            "StepExecutionStatus",
            "StepExecutionId",
            "StepName",
            "Action",
        ]
    },
)
_OptionalDescribeAutomationStepExecutionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeAutomationStepExecutionsPaginateFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeAutomationStepExecutionsPaginateFiltersTypeDef(
    _RequiredDescribeAutomationStepExecutionsPaginateFiltersTypeDef,
    _OptionalDescribeAutomationStepExecutionsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      A filter to limit the amount of step execution information returned by the call.
      - **Key** *(string) --***[REQUIRED]**

        One or more keys to limit the results. Valid filter keys include the following: StepName,
        Action, StepExecutionId, StepExecutionStatus, StartTimeBefore, StartTimeAfter.
    """


_DescribeAutomationStepExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAutomationStepExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAutomationStepExecutionsPaginatePaginationConfigTypeDef(
    _DescribeAutomationStepExecutionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAutomationStepExecutionsPaginateResponseStepExecutionsFailureDetailsTypeDef = TypedDict(
    "_DescribeAutomationStepExecutionsPaginateResponseStepExecutionsFailureDetailsTypeDef",
    {"FailureStage": str, "FailureType": str, "Details": Dict[str, List[str]]},
    total=False,
)


class DescribeAutomationStepExecutionsPaginateResponseStepExecutionsFailureDetailsTypeDef(
    _DescribeAutomationStepExecutionsPaginateResponseStepExecutionsFailureDetailsTypeDef
):
    pass


_DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetLocationTypeDef = TypedDict(
    "_DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetLocationTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)


class DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetLocationTypeDef(
    _DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetLocationTypeDef
):
    pass


_DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetsTypeDef = TypedDict(
    "_DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetsTypeDef(
    _DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetsTypeDef
):
    pass


_DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTypeDef = TypedDict(
    "_DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTypeDef",
    {
        "StepName": str,
        "Action": str,
        "TimeoutSeconds": int,
        "OnFailure": str,
        "MaxAttempts": int,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "StepStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ResponseCode": str,
        "Inputs": Dict[str, str],
        "Outputs": Dict[str, List[str]],
        "Response": str,
        "FailureMessage": str,
        "FailureDetails": DescribeAutomationStepExecutionsPaginateResponseStepExecutionsFailureDetailsTypeDef,
        "StepExecutionId": str,
        "OverriddenParameters": Dict[str, List[str]],
        "IsEnd": bool,
        "NextStep": str,
        "IsCritical": bool,
        "ValidNextSteps": List[str],
        "Targets": List[
            DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetsTypeDef
        ],
        "TargetLocation": DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetLocationTypeDef,
    },
    total=False,
)


class DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTypeDef(
    _DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTypeDef
):
    """
    - *(dict) --*

      Detailed information about an the execution state of an Automation step.
      - **StepName** *(string) --*

        The name of this execution step.
    """


_DescribeAutomationStepExecutionsPaginateResponseTypeDef = TypedDict(
    "_DescribeAutomationStepExecutionsPaginateResponseTypeDef",
    {"StepExecutions": List[DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTypeDef]},
    total=False,
)


class DescribeAutomationStepExecutionsPaginateResponseTypeDef(
    _DescribeAutomationStepExecutionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **StepExecutions** *(list) --*

        A list of details about the current state of all steps that make up an execution.
        - *(dict) --*

          Detailed information about an the execution state of an Automation step.
          - **StepName** *(string) --*

            The name of this execution step.
    """


_DescribeAvailablePatchesPaginateFiltersTypeDef = TypedDict(
    "_DescribeAvailablePatchesPaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeAvailablePatchesPaginateFiltersTypeDef(
    _DescribeAvailablePatchesPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      Defines a filter used in Patch Manager APIs.
      - **Key** *(string) --*

        The key for the filter.
    """


_DescribeAvailablePatchesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAvailablePatchesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAvailablePatchesPaginatePaginationConfigTypeDef(
    _DescribeAvailablePatchesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAvailablePatchesPaginateResponsePatchesTypeDef = TypedDict(
    "_DescribeAvailablePatchesPaginateResponsePatchesTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
    },
    total=False,
)


class DescribeAvailablePatchesPaginateResponsePatchesTypeDef(
    _DescribeAvailablePatchesPaginateResponsePatchesTypeDef
):
    """
    - *(dict) --*

      Represents metadata about a patch.
      - **Id** *(string) --*

        The ID of the patch (this is different than the Microsoft Knowledge Base ID).
    """


_DescribeAvailablePatchesPaginateResponseTypeDef = TypedDict(
    "_DescribeAvailablePatchesPaginateResponseTypeDef",
    {"Patches": List[DescribeAvailablePatchesPaginateResponsePatchesTypeDef]},
    total=False,
)


class DescribeAvailablePatchesPaginateResponseTypeDef(
    _DescribeAvailablePatchesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Patches** *(list) --*

        An array of patches. Each entry in the array is a patch structure.
        - *(dict) --*

          Represents metadata about a patch.
          - **Id** *(string) --*

            The ID of the patch (this is different than the Microsoft Knowledge Base ID).
    """


_DescribeEffectiveInstanceAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEffectiveInstanceAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEffectiveInstanceAssociationsPaginatePaginationConfigTypeDef(
    _DescribeEffectiveInstanceAssociationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEffectiveInstanceAssociationsPaginateResponseAssociationsTypeDef = TypedDict(
    "_DescribeEffectiveInstanceAssociationsPaginateResponseAssociationsTypeDef",
    {"AssociationId": str, "InstanceId": str, "Content": str, "AssociationVersion": str},
    total=False,
)


class DescribeEffectiveInstanceAssociationsPaginateResponseAssociationsTypeDef(
    _DescribeEffectiveInstanceAssociationsPaginateResponseAssociationsTypeDef
):
    """
    - *(dict) --*

      One or more association documents on the instance.
      - **AssociationId** *(string) --*

        The association ID.
    """


_DescribeEffectiveInstanceAssociationsPaginateResponseTypeDef = TypedDict(
    "_DescribeEffectiveInstanceAssociationsPaginateResponseTypeDef",
    {
        "Associations": List[
            DescribeEffectiveInstanceAssociationsPaginateResponseAssociationsTypeDef
        ]
    },
    total=False,
)


class DescribeEffectiveInstanceAssociationsPaginateResponseTypeDef(
    _DescribeEffectiveInstanceAssociationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Associations** *(list) --*

        The associations for the requested instance.
        - *(dict) --*

          One or more association documents on the instance.
          - **AssociationId** *(string) --*

            The association ID.
    """


_DescribeEffectivePatchesForPatchBaselinePaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEffectivePatchesForPatchBaselinePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEffectivePatchesForPatchBaselinePaginatePaginationConfigTypeDef(
    _DescribeEffectivePatchesForPatchBaselinePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchStatusTypeDef = TypedDict(
    "_DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchStatusTypeDef",
    {
        "DeploymentStatus": Literal[
            "APPROVED", "PENDING_APPROVAL", "EXPLICIT_APPROVED", "EXPLICIT_REJECTED"
        ],
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovalDate": datetime,
    },
    total=False,
)


class DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchStatusTypeDef(
    _DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchStatusTypeDef
):
    pass


_DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchTypeDef = TypedDict(
    "_DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
    },
    total=False,
)


class DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchTypeDef(
    _DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchTypeDef
):
    """
    - **Patch** *(dict) --*

      Provides metadata for a patch, including information such as the KB ID, severity,
      classification and a URL for where more information can be obtained about the patch.
      - **Id** *(string) --*

        The ID of the patch (this is different than the Microsoft Knowledge Base ID).
    """


_DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesTypeDef = TypedDict(
    "_DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesTypeDef",
    {
        "Patch": DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchTypeDef,
        "PatchStatus": DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchStatusTypeDef,
    },
    total=False,
)


class DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesTypeDef(
    _DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesTypeDef
):
    """
    - *(dict) --*

      The EffectivePatch structure defines metadata about a patch along with the approval state of
      the patch in a particular patch baseline. The approval state includes information about
      whether the patch is currently approved, due to be approved by a rule, explicitly approved, or
      explicitly rejected and the date the patch was or will be approved.
      - **Patch** *(dict) --*

        Provides metadata for a patch, including information such as the KB ID, severity,
        classification and a URL for where more information can be obtained about the patch.
        - **Id** *(string) --*

          The ID of the patch (this is different than the Microsoft Knowledge Base ID).
    """


_DescribeEffectivePatchesForPatchBaselinePaginateResponseTypeDef = TypedDict(
    "_DescribeEffectivePatchesForPatchBaselinePaginateResponseTypeDef",
    {
        "EffectivePatches": List[
            DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesTypeDef
        ]
    },
    total=False,
)


class DescribeEffectivePatchesForPatchBaselinePaginateResponseTypeDef(
    _DescribeEffectivePatchesForPatchBaselinePaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **EffectivePatches** *(list) --*

        An array of patches and patch status.
        - *(dict) --*

          The EffectivePatch structure defines metadata about a patch along with the approval state
          of the patch in a particular patch baseline. The approval state includes information about
          whether the patch is currently approved, due to be approved by a rule, explicitly
          approved, or explicitly rejected and the date the patch was or will be approved.
          - **Patch** *(dict) --*

            Provides metadata for a patch, including information such as the KB ID, severity,
            classification and a URL for where more information can be obtained about the patch.
            - **Id** *(string) --*

              The ID of the patch (this is different than the Microsoft Knowledge Base ID).
    """


_DescribeInstanceAssociationsStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeInstanceAssociationsStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeInstanceAssociationsStatusPaginatePaginationConfigTypeDef(
    _DescribeInstanceAssociationsStatusPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef = TypedDict(
    "_DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef",
    {"OutputUrl": str},
    total=False,
)


class DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef(
    _DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef
):
    pass


_DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlTypeDef = TypedDict(
    "_DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlTypeDef",
    {
        "S3OutputUrl": DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef
    },
    total=False,
)


class DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlTypeDef(
    _DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlTypeDef
):
    pass


_DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosTypeDef = TypedDict(
    "_DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosTypeDef",
    {
        "AssociationId": str,
        "Name": str,
        "DocumentVersion": str,
        "AssociationVersion": str,
        "InstanceId": str,
        "ExecutionDate": datetime,
        "Status": str,
        "DetailedStatus": str,
        "ExecutionSummary": str,
        "ErrorCode": str,
        "OutputUrl": DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlTypeDef,
        "AssociationName": str,
    },
    total=False,
)


class DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosTypeDef(
    _DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosTypeDef
):
    """
    - *(dict) --*

      Status information about the instance association.
      - **AssociationId** *(string) --*

        The association ID.
    """


_DescribeInstanceAssociationsStatusPaginateResponseTypeDef = TypedDict(
    "_DescribeInstanceAssociationsStatusPaginateResponseTypeDef",
    {
        "InstanceAssociationStatusInfos": List[
            DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosTypeDef
        ]
    },
    total=False,
)


class DescribeInstanceAssociationsStatusPaginateResponseTypeDef(
    _DescribeInstanceAssociationsStatusPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **InstanceAssociationStatusInfos** *(list) --*

        Status information about the association.
        - *(dict) --*

          Status information about the instance association.
          - **AssociationId** *(string) --*

            The association ID.
    """


_RequiredDescribeInstanceInformationPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeInstanceInformationPaginateFiltersTypeDef", {"Key": str}
)
_OptionalDescribeInstanceInformationPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeInstanceInformationPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeInstanceInformationPaginateFiltersTypeDef(
    _RequiredDescribeInstanceInformationPaginateFiltersTypeDef,
    _OptionalDescribeInstanceInformationPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      The filters to describe or get information about your managed instances.
      - **Key** *(string) --***[REQUIRED]**

        The filter key name to describe your instances. For example:
        "InstanceIds"|"AgentVersion"|"PingStatus"|"PlatformTypes"|"ActivationIds"|"IamRole"
        |"ResourceType"|"AssociationStatus"|"Tag
        Key"
    """


_RequiredDescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef = TypedDict(
    "_RequiredDescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef",
    {
        "key": Literal[
            "InstanceIds",
            "AgentVersion",
            "PingStatus",
            "PlatformTypes",
            "ActivationIds",
            "IamRole",
            "ResourceType",
            "AssociationStatus",
        ]
    },
)
_OptionalDescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef = TypedDict(
    "_OptionalDescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef",
    {"valueSet": List[str]},
    total=False,
)


class DescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef(
    _RequiredDescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef,
    _OptionalDescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef,
):
    """
    - *(dict) --*

      Describes a filter for a specific list of instances. You can filter instances information by
      using tags. You specify tags by using a key-value mapping.
      Use this action instead of the
      DescribeInstanceInformationRequest$InstanceInformationFilterList method. The
      ``InstanceInformationFilterList`` method is a legacy method and does not support tags.
      - **key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_DescribeInstanceInformationPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeInstanceInformationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeInstanceInformationPaginatePaginationConfigTypeDef(
    _DescribeInstanceInformationPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeInstanceInformationPaginateResponseInstanceInformationListAssociationOverviewTypeDef = TypedDict(
    "_DescribeInstanceInformationPaginateResponseInstanceInformationListAssociationOverviewTypeDef",
    {"DetailedStatus": str, "InstanceAssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)


class DescribeInstanceInformationPaginateResponseInstanceInformationListAssociationOverviewTypeDef(
    _DescribeInstanceInformationPaginateResponseInstanceInformationListAssociationOverviewTypeDef
):
    pass


_DescribeInstanceInformationPaginateResponseInstanceInformationListTypeDef = TypedDict(
    "_DescribeInstanceInformationPaginateResponseInstanceInformationListTypeDef",
    {
        "InstanceId": str,
        "PingStatus": Literal["Online", "ConnectionLost", "Inactive"],
        "LastPingDateTime": datetime,
        "AgentVersion": str,
        "IsLatestVersion": bool,
        "PlatformType": Literal["Windows", "Linux"],
        "PlatformName": str,
        "PlatformVersion": str,
        "ActivationId": str,
        "IamRole": str,
        "RegistrationDate": datetime,
        "ResourceType": Literal["ManagedInstance", "Document", "EC2Instance"],
        "Name": str,
        "IPAddress": str,
        "ComputerName": str,
        "AssociationStatus": str,
        "LastAssociationExecutionDate": datetime,
        "LastSuccessfulAssociationExecutionDate": datetime,
        "AssociationOverview": DescribeInstanceInformationPaginateResponseInstanceInformationListAssociationOverviewTypeDef,
    },
    total=False,
)


class DescribeInstanceInformationPaginateResponseInstanceInformationListTypeDef(
    _DescribeInstanceInformationPaginateResponseInstanceInformationListTypeDef
):
    """
    - *(dict) --*

      Describes a filter for a specific list of instances.
      - **InstanceId** *(string) --*

        The instance ID.
    """


_DescribeInstanceInformationPaginateResponseTypeDef = TypedDict(
    "_DescribeInstanceInformationPaginateResponseTypeDef",
    {
        "InstanceInformationList": List[
            DescribeInstanceInformationPaginateResponseInstanceInformationListTypeDef
        ]
    },
    total=False,
)


class DescribeInstanceInformationPaginateResponseTypeDef(
    _DescribeInstanceInformationPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **InstanceInformationList** *(list) --*

        The instance information list.
        - *(dict) --*

          Describes a filter for a specific list of instances.
          - **InstanceId** *(string) --*

            The instance ID.
    """


_RequiredDescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef", {"Key": str}
)
_OptionalDescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef",
    {"Values": List[str], "Type": Literal["Equal", "NotEqual", "LessThan", "GreaterThan"]},
    total=False,
)


class DescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef(
    _RequiredDescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef,
    _OptionalDescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      Defines a filter used in DescribeInstancePatchStatesForPatchGroup used to scope down the
      information returned by the API.
      - **Key** *(string) --***[REQUIRED]**

        The key for the filter. Supported values are FailedCount, InstalledCount,
        InstalledOtherCount, MissingCount and NotApplicableCount.
    """


_DescribeInstancePatchStatesForPatchGroupPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeInstancePatchStatesForPatchGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeInstancePatchStatesForPatchGroupPaginatePaginationConfigTypeDef(
    _DescribeInstancePatchStatesForPatchGroupPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeInstancePatchStatesForPatchGroupPaginateResponseInstancePatchStatesTypeDef = TypedDict(
    "_DescribeInstancePatchStatesForPatchGroupPaginateResponseInstancePatchStatesTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": Literal["Scan", "Install"],
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": Literal["RebootIfNeeded", "NoReboot"],
    },
    total=False,
)


class DescribeInstancePatchStatesForPatchGroupPaginateResponseInstancePatchStatesTypeDef(
    _DescribeInstancePatchStatesForPatchGroupPaginateResponseInstancePatchStatesTypeDef
):
    """
    - *(dict) --*

      Defines the high-level patch compliance state for a managed instance, providing information
      about the number of installed, missing, not applicable, and failed patches along with metadata
      about the operation when this information was gathered for the instance.
      - **InstanceId** *(string) --*

        The ID of the managed instance the high-level patch compliance information was collected
        for.
    """


_DescribeInstancePatchStatesForPatchGroupPaginateResponseTypeDef = TypedDict(
    "_DescribeInstancePatchStatesForPatchGroupPaginateResponseTypeDef",
    {
        "InstancePatchStates": List[
            DescribeInstancePatchStatesForPatchGroupPaginateResponseInstancePatchStatesTypeDef
        ]
    },
    total=False,
)


class DescribeInstancePatchStatesForPatchGroupPaginateResponseTypeDef(
    _DescribeInstancePatchStatesForPatchGroupPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **InstancePatchStates** *(list) --*

        The high-level patch state for the requested instances.
        - *(dict) --*

          Defines the high-level patch compliance state for a managed instance, providing
          information about the number of installed, missing, not applicable, and failed patches
          along with metadata about the operation when this information was gathered for the
          instance.
          - **InstanceId** *(string) --*

            The ID of the managed instance the high-level patch compliance information was collected
            for.
    """


_DescribeInstancePatchStatesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeInstancePatchStatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeInstancePatchStatesPaginatePaginationConfigTypeDef(
    _DescribeInstancePatchStatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeInstancePatchStatesPaginateResponseInstancePatchStatesTypeDef = TypedDict(
    "_DescribeInstancePatchStatesPaginateResponseInstancePatchStatesTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": Literal["Scan", "Install"],
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": Literal["RebootIfNeeded", "NoReboot"],
    },
    total=False,
)


class DescribeInstancePatchStatesPaginateResponseInstancePatchStatesTypeDef(
    _DescribeInstancePatchStatesPaginateResponseInstancePatchStatesTypeDef
):
    """
    - *(dict) --*

      Defines the high-level patch compliance state for a managed instance, providing information
      about the number of installed, missing, not applicable, and failed patches along with metadata
      about the operation when this information was gathered for the instance.
      - **InstanceId** *(string) --*

        The ID of the managed instance the high-level patch compliance information was collected
        for.
    """


_DescribeInstancePatchStatesPaginateResponseTypeDef = TypedDict(
    "_DescribeInstancePatchStatesPaginateResponseTypeDef",
    {
        "InstancePatchStates": List[
            DescribeInstancePatchStatesPaginateResponseInstancePatchStatesTypeDef
        ]
    },
    total=False,
)


class DescribeInstancePatchStatesPaginateResponseTypeDef(
    _DescribeInstancePatchStatesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **InstancePatchStates** *(list) --*

        The high-level patch state for the requested instances.
        - *(dict) --*

          Defines the high-level patch compliance state for a managed instance, providing
          information about the number of installed, missing, not applicable, and failed patches
          along with metadata about the operation when this information was gathered for the
          instance.
          - **InstanceId** *(string) --*

            The ID of the managed instance the high-level patch compliance information was collected
            for.
    """


_DescribeInstancePatchesPaginateFiltersTypeDef = TypedDict(
    "_DescribeInstancePatchesPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class DescribeInstancePatchesPaginateFiltersTypeDef(_DescribeInstancePatchesPaginateFiltersTypeDef):
    """
    - *(dict) --*

      Defines a filter used in Patch Manager APIs.
      - **Key** *(string) --*

        The key for the filter.
    """


_DescribeInstancePatchesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeInstancePatchesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeInstancePatchesPaginatePaginationConfigTypeDef(
    _DescribeInstancePatchesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeInstancePatchesPaginateResponsePatchesTypeDef = TypedDict(
    "_DescribeInstancePatchesPaginateResponsePatchesTypeDef",
    {
        "Title": str,
        "KBId": str,
        "Classification": str,
        "Severity": str,
        "State": Literal[
            "INSTALLED",
            "INSTALLED_OTHER",
            "INSTALLED_PENDING_REBOOT",
            "INSTALLED_REJECTED",
            "MISSING",
            "NOT_APPLICABLE",
            "FAILED",
        ],
        "InstalledTime": datetime,
    },
    total=False,
)


class DescribeInstancePatchesPaginateResponsePatchesTypeDef(
    _DescribeInstancePatchesPaginateResponsePatchesTypeDef
):
    """
    - *(dict) --*

      Information about the state of a patch on a particular instance as it relates to the patch
      baseline used to patch the instance.
      - **Title** *(string) --*

        The title of the patch.
    """


_DescribeInstancePatchesPaginateResponseTypeDef = TypedDict(
    "_DescribeInstancePatchesPaginateResponseTypeDef",
    {"Patches": List[DescribeInstancePatchesPaginateResponsePatchesTypeDef]},
    total=False,
)


class DescribeInstancePatchesPaginateResponseTypeDef(
    _DescribeInstancePatchesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Patches** *(list) --*

        Each entry in the array is a structure containing:
        Title (string)
        KBId (string)
        Classification (string)
        Severity (string)
        State (string, such as "INSTALLED" or "FAILED")
        InstalledTime (DateTime)
        InstalledBy (string)
        - *(dict) --*

          Information about the state of a patch on a particular instance as it relates to the patch
          baseline used to patch the instance.
          - **Title** *(string) --*

            The title of the patch.
    """


_DescribeInventoryDeletionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeInventoryDeletionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeInventoryDeletionsPaginatePaginationConfigTypeDef(
    _DescribeInventoryDeletionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef = TypedDict(
    "_DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef",
    {"Version": str, "Count": int, "RemainingCount": int},
    total=False,
)


class DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef(
    _DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef
):
    pass


_DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummaryTypeDef = TypedDict(
    "_DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummaryTypeDef",
    {
        "TotalCount": int,
        "RemainingCount": int,
        "SummaryItems": List[
            DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef
        ],
    },
    total=False,
)


class DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummaryTypeDef(
    _DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummaryTypeDef
):
    pass


_DescribeInventoryDeletionsPaginateResponseInventoryDeletionsTypeDef = TypedDict(
    "_DescribeInventoryDeletionsPaginateResponseInventoryDeletionsTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionStartTime": datetime,
        "LastStatus": Literal["InProgress", "Complete"],
        "LastStatusMessage": str,
        "DeletionSummary": DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummaryTypeDef,
        "LastStatusUpdateTime": datetime,
    },
    total=False,
)


class DescribeInventoryDeletionsPaginateResponseInventoryDeletionsTypeDef(
    _DescribeInventoryDeletionsPaginateResponseInventoryDeletionsTypeDef
):
    """
    - *(dict) --*

      Status information returned by the ``DeleteInventory`` action.
      - **DeletionId** *(string) --*

        The deletion ID returned by the ``DeleteInventory`` action.
    """


_DescribeInventoryDeletionsPaginateResponseTypeDef = TypedDict(
    "_DescribeInventoryDeletionsPaginateResponseTypeDef",
    {
        "InventoryDeletions": List[
            DescribeInventoryDeletionsPaginateResponseInventoryDeletionsTypeDef
        ]
    },
    total=False,
)


class DescribeInventoryDeletionsPaginateResponseTypeDef(
    _DescribeInventoryDeletionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **InventoryDeletions** *(list) --*

        A list of status items for deleted inventory.
        - *(dict) --*

          Status information returned by the ``DeleteInventory`` action.
          - **DeletionId** *(string) --*

            The deletion ID returned by the ``DeleteInventory`` action.
    """


_DescribeMaintenanceWindowExecutionTaskInvocationsPaginateFiltersTypeDef = TypedDict(
    "_DescribeMaintenanceWindowExecutionTaskInvocationsPaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeMaintenanceWindowExecutionTaskInvocationsPaginateFiltersTypeDef(
    _DescribeMaintenanceWindowExecutionTaskInvocationsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      Filter used in the request. Supported filter keys are Name and Enabled.
      - **Key** *(string) --*

        The name of the filter.
    """


_DescribeMaintenanceWindowExecutionTaskInvocationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMaintenanceWindowExecutionTaskInvocationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMaintenanceWindowExecutionTaskInvocationsPaginatePaginationConfigTypeDef(
    _DescribeMaintenanceWindowExecutionTaskInvocationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseWindowExecutionTaskInvocationIdentitiesTypeDef = TypedDict(
    "_DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseWindowExecutionTaskInvocationIdentitiesTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Parameters": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)


class DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseWindowExecutionTaskInvocationIdentitiesTypeDef(
    _DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseWindowExecutionTaskInvocationIdentitiesTypeDef
):
    """
    - *(dict) --*

      Describes the information about a task invocation for a particular target as part of a task
      execution performed as part of a maintenance window execution.
      - **WindowExecutionId** *(string) --*

        The ID of the maintenance window execution that ran the task.
    """


_DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseTypeDef = TypedDict(
    "_DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseTypeDef",
    {
        "WindowExecutionTaskInvocationIdentities": List[
            DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseWindowExecutionTaskInvocationIdentitiesTypeDef
        ]
    },
    total=False,
)


class DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseTypeDef(
    _DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowExecutionTaskInvocationIdentities** *(list) --*

        Information about the task invocation results per invocation.
        - *(dict) --*

          Describes the information about a task invocation for a particular target as part of a
          task execution performed as part of a maintenance window execution.
          - **WindowExecutionId** *(string) --*

            The ID of the maintenance window execution that ran the task.
    """


_DescribeMaintenanceWindowExecutionTasksPaginateFiltersTypeDef = TypedDict(
    "_DescribeMaintenanceWindowExecutionTasksPaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeMaintenanceWindowExecutionTasksPaginateFiltersTypeDef(
    _DescribeMaintenanceWindowExecutionTasksPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      Filter used in the request. Supported filter keys are Name and Enabled.
      - **Key** *(string) --*

        The name of the filter.
    """


_DescribeMaintenanceWindowExecutionTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMaintenanceWindowExecutionTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMaintenanceWindowExecutionTasksPaginatePaginationConfigTypeDef(
    _DescribeMaintenanceWindowExecutionTasksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeMaintenanceWindowExecutionTasksPaginateResponseWindowExecutionTaskIdentitiesTypeDef = TypedDict(
    "_DescribeMaintenanceWindowExecutionTasksPaginateResponseWindowExecutionTaskIdentitiesTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "TaskArn": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
    },
    total=False,
)


class DescribeMaintenanceWindowExecutionTasksPaginateResponseWindowExecutionTaskIdentitiesTypeDef(
    _DescribeMaintenanceWindowExecutionTasksPaginateResponseWindowExecutionTaskIdentitiesTypeDef
):
    """
    - *(dict) --*

      Information about a task execution performed as part of a maintenance window execution.
      - **WindowExecutionId** *(string) --*

        The ID of the maintenance window execution that ran the task.
    """


_DescribeMaintenanceWindowExecutionTasksPaginateResponseTypeDef = TypedDict(
    "_DescribeMaintenanceWindowExecutionTasksPaginateResponseTypeDef",
    {
        "WindowExecutionTaskIdentities": List[
            DescribeMaintenanceWindowExecutionTasksPaginateResponseWindowExecutionTaskIdentitiesTypeDef
        ]
    },
    total=False,
)


class DescribeMaintenanceWindowExecutionTasksPaginateResponseTypeDef(
    _DescribeMaintenanceWindowExecutionTasksPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowExecutionTaskIdentities** *(list) --*

        Information about the task executions.
        - *(dict) --*

          Information about a task execution performed as part of a maintenance window execution.
          - **WindowExecutionId** *(string) --*

            The ID of the maintenance window execution that ran the task.
    """


_DescribeMaintenanceWindowExecutionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeMaintenanceWindowExecutionsPaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeMaintenanceWindowExecutionsPaginateFiltersTypeDef(
    _DescribeMaintenanceWindowExecutionsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      Filter used in the request. Supported filter keys are Name and Enabled.
      - **Key** *(string) --*

        The name of the filter.
    """


_DescribeMaintenanceWindowExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMaintenanceWindowExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMaintenanceWindowExecutionsPaginatePaginationConfigTypeDef(
    _DescribeMaintenanceWindowExecutionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeMaintenanceWindowExecutionsPaginateResponseWindowExecutionsTypeDef = TypedDict(
    "_DescribeMaintenanceWindowExecutionsPaginateResponseWindowExecutionsTypeDef",
    {
        "WindowId": str,
        "WindowExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)


class DescribeMaintenanceWindowExecutionsPaginateResponseWindowExecutionsTypeDef(
    _DescribeMaintenanceWindowExecutionsPaginateResponseWindowExecutionsTypeDef
):
    """
    - *(dict) --*

      Describes the information about an execution of a maintenance window.
      - **WindowId** *(string) --*

        The ID of the maintenance window.
    """


_DescribeMaintenanceWindowExecutionsPaginateResponseTypeDef = TypedDict(
    "_DescribeMaintenanceWindowExecutionsPaginateResponseTypeDef",
    {
        "WindowExecutions": List[
            DescribeMaintenanceWindowExecutionsPaginateResponseWindowExecutionsTypeDef
        ]
    },
    total=False,
)


class DescribeMaintenanceWindowExecutionsPaginateResponseTypeDef(
    _DescribeMaintenanceWindowExecutionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowExecutions** *(list) --*

        Information about the maintenance window executions.
        - *(dict) --*

          Describes the information about an execution of a maintenance window.
          - **WindowId** *(string) --*

            The ID of the maintenance window.
    """


_DescribeMaintenanceWindowSchedulePaginateFiltersTypeDef = TypedDict(
    "_DescribeMaintenanceWindowSchedulePaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeMaintenanceWindowSchedulePaginateFiltersTypeDef(
    _DescribeMaintenanceWindowSchedulePaginateFiltersTypeDef
):
    """
    - *(dict) --*

      Defines a filter used in Patch Manager APIs.
      - **Key** *(string) --*

        The key for the filter.
    """


_DescribeMaintenanceWindowSchedulePaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMaintenanceWindowSchedulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMaintenanceWindowSchedulePaginatePaginationConfigTypeDef(
    _DescribeMaintenanceWindowSchedulePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeMaintenanceWindowSchedulePaginateResponseScheduledWindowExecutionsTypeDef = TypedDict(
    "_DescribeMaintenanceWindowSchedulePaginateResponseScheduledWindowExecutionsTypeDef",
    {"WindowId": str, "Name": str, "ExecutionTime": str},
    total=False,
)


class DescribeMaintenanceWindowSchedulePaginateResponseScheduledWindowExecutionsTypeDef(
    _DescribeMaintenanceWindowSchedulePaginateResponseScheduledWindowExecutionsTypeDef
):
    """
    - *(dict) --*

      Information about a scheduled execution for a maintenance window.
      - **WindowId** *(string) --*

        The ID of the maintenance window to be run.
    """


_DescribeMaintenanceWindowSchedulePaginateResponseTypeDef = TypedDict(
    "_DescribeMaintenanceWindowSchedulePaginateResponseTypeDef",
    {
        "ScheduledWindowExecutions": List[
            DescribeMaintenanceWindowSchedulePaginateResponseScheduledWindowExecutionsTypeDef
        ]
    },
    total=False,
)


class DescribeMaintenanceWindowSchedulePaginateResponseTypeDef(
    _DescribeMaintenanceWindowSchedulePaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ScheduledWindowExecutions** *(list) --*

        Information about maintenance window executions scheduled for the specified time range.
        - *(dict) --*

          Information about a scheduled execution for a maintenance window.
          - **WindowId** *(string) --*

            The ID of the maintenance window to be run.
    """


_DescribeMaintenanceWindowSchedulePaginateTargetsTypeDef = TypedDict(
    "_DescribeMaintenanceWindowSchedulePaginateTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeMaintenanceWindowSchedulePaginateTargetsTypeDef(
    _DescribeMaintenanceWindowSchedulePaginateTargetsTypeDef
):
    """
    - *(dict) --*

      An array of search criteria that targets instances using a Key,Value combination that you
      specify.
      Supported formats include the following.
      * ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
      * ``Key=tag:*my-tag-key* ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
      * ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
      * (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
      For example:
      * ``Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE``
      * ``Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3``
      * ``Key=tag-key,Values=Name,Instance-Type,CostCenter``
      * (Maintenance window targets only)
      ``Key=resource-groups:Name,Values=
          ProductionResourceGroup``   This example demonstrates how to
      target all resources in the resource group **ProductionResourceGroup** in your maintenance
      window.
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``
      This example demonstrates how to target only Amazon EC2 instances and VPCs in your maintenance
      window.
      * (State Manager association targets only) ``Key=InstanceIds,Values=*``   This example
      demonstrates how to target all managed instances in the AWS Region where the association was
      created.
      For information about how to send commands that target instances using ``Key,Value``
      parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet
      <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__
      in the *AWS Systems Manager User Guide* .
      - **Key** *(string) --*

        User-defined criteria for sending commands that target instances that meet the criteria.
    """


_DescribeMaintenanceWindowTargetsPaginateFiltersTypeDef = TypedDict(
    "_DescribeMaintenanceWindowTargetsPaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeMaintenanceWindowTargetsPaginateFiltersTypeDef(
    _DescribeMaintenanceWindowTargetsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      Filter used in the request. Supported filter keys are Name and Enabled.
      - **Key** *(string) --*

        The name of the filter.
    """


_DescribeMaintenanceWindowTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMaintenanceWindowTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMaintenanceWindowTargetsPaginatePaginationConfigTypeDef(
    _DescribeMaintenanceWindowTargetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeMaintenanceWindowTargetsPaginateResponseTargetsTargetsTypeDef = TypedDict(
    "_DescribeMaintenanceWindowTargetsPaginateResponseTargetsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeMaintenanceWindowTargetsPaginateResponseTargetsTargetsTypeDef(
    _DescribeMaintenanceWindowTargetsPaginateResponseTargetsTargetsTypeDef
):
    pass


_DescribeMaintenanceWindowTargetsPaginateResponseTargetsTypeDef = TypedDict(
    "_DescribeMaintenanceWindowTargetsPaginateResponseTargetsTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResourceType": Literal["INSTANCE", "RESOURCE_GROUP"],
        "Targets": List[DescribeMaintenanceWindowTargetsPaginateResponseTargetsTargetsTypeDef],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)


class DescribeMaintenanceWindowTargetsPaginateResponseTargetsTypeDef(
    _DescribeMaintenanceWindowTargetsPaginateResponseTargetsTypeDef
):
    """
    - *(dict) --*

      The target registered with the maintenance window.
      - **WindowId** *(string) --*

        The ID of the maintenance window to register the target with.
    """


_DescribeMaintenanceWindowTargetsPaginateResponseTypeDef = TypedDict(
    "_DescribeMaintenanceWindowTargetsPaginateResponseTypeDef",
    {"Targets": List[DescribeMaintenanceWindowTargetsPaginateResponseTargetsTypeDef]},
    total=False,
)


class DescribeMaintenanceWindowTargetsPaginateResponseTypeDef(
    _DescribeMaintenanceWindowTargetsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Targets** *(list) --*

        Information about the targets in the maintenance window.
        - *(dict) --*

          The target registered with the maintenance window.
          - **WindowId** *(string) --*

            The ID of the maintenance window to register the target with.
    """


_DescribeMaintenanceWindowTasksPaginateFiltersTypeDef = TypedDict(
    "_DescribeMaintenanceWindowTasksPaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeMaintenanceWindowTasksPaginateFiltersTypeDef(
    _DescribeMaintenanceWindowTasksPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      Filter used in the request. Supported filter keys are Name and Enabled.
      - **Key** *(string) --*

        The name of the filter.
    """


_DescribeMaintenanceWindowTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMaintenanceWindowTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMaintenanceWindowTasksPaginatePaginationConfigTypeDef(
    _DescribeMaintenanceWindowTasksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeMaintenanceWindowTasksPaginateResponseTasksLoggingInfoTypeDef = TypedDict(
    "_DescribeMaintenanceWindowTasksPaginateResponseTasksLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)


class DescribeMaintenanceWindowTasksPaginateResponseTasksLoggingInfoTypeDef(
    _DescribeMaintenanceWindowTasksPaginateResponseTasksLoggingInfoTypeDef
):
    pass


_DescribeMaintenanceWindowTasksPaginateResponseTasksTargetsTypeDef = TypedDict(
    "_DescribeMaintenanceWindowTasksPaginateResponseTasksTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeMaintenanceWindowTasksPaginateResponseTasksTargetsTypeDef(
    _DescribeMaintenanceWindowTasksPaginateResponseTasksTargetsTypeDef
):
    pass


_DescribeMaintenanceWindowTasksPaginateResponseTasksTaskParametersTypeDef = TypedDict(
    "_DescribeMaintenanceWindowTasksPaginateResponseTasksTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeMaintenanceWindowTasksPaginateResponseTasksTaskParametersTypeDef(
    _DescribeMaintenanceWindowTasksPaginateResponseTasksTaskParametersTypeDef
):
    pass


_DescribeMaintenanceWindowTasksPaginateResponseTasksTypeDef = TypedDict(
    "_DescribeMaintenanceWindowTasksPaginateResponseTasksTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "TaskArn": str,
        "Type": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Targets": List[DescribeMaintenanceWindowTasksPaginateResponseTasksTargetsTypeDef],
        "TaskParameters": Dict[
            str, DescribeMaintenanceWindowTasksPaginateResponseTasksTaskParametersTypeDef
        ],
        "Priority": int,
        "LoggingInfo": DescribeMaintenanceWindowTasksPaginateResponseTasksLoggingInfoTypeDef,
        "ServiceRoleArn": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)


class DescribeMaintenanceWindowTasksPaginateResponseTasksTypeDef(
    _DescribeMaintenanceWindowTasksPaginateResponseTasksTypeDef
):
    """
    - *(dict) --*

      Information about a task defined for a maintenance window.
      - **WindowId** *(string) --*

        The ID of the maintenance window where the task is registered.
    """


_DescribeMaintenanceWindowTasksPaginateResponseTypeDef = TypedDict(
    "_DescribeMaintenanceWindowTasksPaginateResponseTypeDef",
    {"Tasks": List[DescribeMaintenanceWindowTasksPaginateResponseTasksTypeDef]},
    total=False,
)


class DescribeMaintenanceWindowTasksPaginateResponseTypeDef(
    _DescribeMaintenanceWindowTasksPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Tasks** *(list) --*

        Information about the tasks in the maintenance window.
        - *(dict) --*

          Information about a task defined for a maintenance window.
          - **WindowId** *(string) --*

            The ID of the maintenance window where the task is registered.
    """


_DescribeMaintenanceWindowsForTargetPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMaintenanceWindowsForTargetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMaintenanceWindowsForTargetPaginatePaginationConfigTypeDef(
    _DescribeMaintenanceWindowsForTargetPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeMaintenanceWindowsForTargetPaginateResponseWindowIdentitiesTypeDef = TypedDict(
    "_DescribeMaintenanceWindowsForTargetPaginateResponseWindowIdentitiesTypeDef",
    {"WindowId": str, "Name": str},
    total=False,
)


class DescribeMaintenanceWindowsForTargetPaginateResponseWindowIdentitiesTypeDef(
    _DescribeMaintenanceWindowsForTargetPaginateResponseWindowIdentitiesTypeDef
):
    """
    - *(dict) --*

      The maintenance window to which the specified target belongs.
      - **WindowId** *(string) --*

        The ID of the maintenance window.
    """


_DescribeMaintenanceWindowsForTargetPaginateResponseTypeDef = TypedDict(
    "_DescribeMaintenanceWindowsForTargetPaginateResponseTypeDef",
    {
        "WindowIdentities": List[
            DescribeMaintenanceWindowsForTargetPaginateResponseWindowIdentitiesTypeDef
        ]
    },
    total=False,
)


class DescribeMaintenanceWindowsForTargetPaginateResponseTypeDef(
    _DescribeMaintenanceWindowsForTargetPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowIdentities** *(list) --*

        Information about the maintenance window targets and tasks an instance is associated with.
        - *(dict) --*

          The maintenance window to which the specified target belongs.
          - **WindowId** *(string) --*

            The ID of the maintenance window.
    """


_DescribeMaintenanceWindowsForTargetPaginateTargetsTypeDef = TypedDict(
    "_DescribeMaintenanceWindowsForTargetPaginateTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeMaintenanceWindowsForTargetPaginateTargetsTypeDef(
    _DescribeMaintenanceWindowsForTargetPaginateTargetsTypeDef
):
    """
    - *(dict) --*

      An array of search criteria that targets instances using a Key,Value combination that you
      specify.
      Supported formats include the following.
      * ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
      * ``Key=tag:*my-tag-key* ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
      * ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
      * (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
      For example:
      * ``Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE``
      * ``Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3``
      * ``Key=tag-key,Values=Name,Instance-Type,CostCenter``
      * (Maintenance window targets only)
      ``Key=resource-groups:Name,Values=
          ProductionResourceGroup``   This example demonstrates how to
      target all resources in the resource group **ProductionResourceGroup** in your maintenance
      window.
      * (Maintenance window targets only)
      ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``
      This example demonstrates how to target only Amazon EC2 instances and VPCs in your maintenance
      window.
      * (State Manager association targets only) ``Key=InstanceIds,Values=*``   This example
      demonstrates how to target all managed instances in the AWS Region where the association was
      created.
      For information about how to send commands that target instances using ``Key,Value``
      parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet
      <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__
      in the *AWS Systems Manager User Guide* .
      - **Key** *(string) --*

        User-defined criteria for sending commands that target instances that meet the criteria.
    """


_DescribeMaintenanceWindowsPaginateFiltersTypeDef = TypedDict(
    "_DescribeMaintenanceWindowsPaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeMaintenanceWindowsPaginateFiltersTypeDef(
    _DescribeMaintenanceWindowsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      Filter used in the request. Supported filter keys are Name and Enabled.
      - **Key** *(string) --*

        The name of the filter.
    """


_DescribeMaintenanceWindowsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMaintenanceWindowsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMaintenanceWindowsPaginatePaginationConfigTypeDef(
    _DescribeMaintenanceWindowsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeMaintenanceWindowsPaginateResponseWindowIdentitiesTypeDef = TypedDict(
    "_DescribeMaintenanceWindowsPaginateResponseWindowIdentitiesTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "Enabled": bool,
        "Duration": int,
        "Cutoff": int,
        "Schedule": str,
        "ScheduleTimezone": str,
        "EndDate": str,
        "StartDate": str,
        "NextExecutionTime": str,
    },
    total=False,
)


class DescribeMaintenanceWindowsPaginateResponseWindowIdentitiesTypeDef(
    _DescribeMaintenanceWindowsPaginateResponseWindowIdentitiesTypeDef
):
    """
    - *(dict) --*

      Information about the maintenance window.
      - **WindowId** *(string) --*

        The ID of the maintenance window.
    """


_DescribeMaintenanceWindowsPaginateResponseTypeDef = TypedDict(
    "_DescribeMaintenanceWindowsPaginateResponseTypeDef",
    {"WindowIdentities": List[DescribeMaintenanceWindowsPaginateResponseWindowIdentitiesTypeDef]},
    total=False,
)


class DescribeMaintenanceWindowsPaginateResponseTypeDef(
    _DescribeMaintenanceWindowsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **WindowIdentities** *(list) --*

        Information about the maintenance windows.
        - *(dict) --*

          Information about the maintenance window.
          - **WindowId** *(string) --*

            The ID of the maintenance window.
    """


_RequiredDescribeParametersPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeParametersPaginateFiltersTypeDef", {"Key": Literal["Name", "Type", "KeyId"]}
)
_OptionalDescribeParametersPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeParametersPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeParametersPaginateFiltersTypeDef(
    _RequiredDescribeParametersPaginateFiltersTypeDef,
    _OptionalDescribeParametersPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      This data type is deprecated. Instead, use  ParameterStringFilter .
      - **Key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_DescribeParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeParametersPaginatePaginationConfigTypeDef(
    _DescribeParametersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeParametersPaginateParameterFiltersTypeDef = TypedDict(
    "_DescribeParametersPaginateParameterFiltersTypeDef",
    {"Key": str, "Option": str, "Values": List[str]},
    total=False,
)


class DescribeParametersPaginateParameterFiltersTypeDef(
    _DescribeParametersPaginateParameterFiltersTypeDef
):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of results.
      .. warning::

        The ``ParameterStringFilter`` object is used by the  DescribeParameters and
        GetParametersByPath API actions. However, not all of the pattern values listed for ``Key``
        can be used with both actions.
        For ``DescribeActions`` , all of the listed patterns are valid, with the exception of
        ``Label`` .
        For ``GetParametersByPath`` , the following patterns listed for ``Key`` are not valid:
        ``Name`` , ``Path`` , and ``Tier`` .
        For examples of CLI commands demonstrating valid parameter filter constructions, see
        `Searching for Systems Manager Parameters
        <http://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-search.html>`__ in
        the *AWS Systems Manager User Guide* .
    """


_DescribeParametersPaginateResponseParametersPoliciesTypeDef = TypedDict(
    "_DescribeParametersPaginateResponseParametersPoliciesTypeDef",
    {"PolicyText": str, "PolicyType": str, "PolicyStatus": str},
    total=False,
)


class DescribeParametersPaginateResponseParametersPoliciesTypeDef(
    _DescribeParametersPaginateResponseParametersPoliciesTypeDef
):
    pass


_DescribeParametersPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeParametersPaginateResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "AllowedPattern": str,
        "Version": int,
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List[DescribeParametersPaginateResponseParametersPoliciesTypeDef],
    },
    total=False,
)


class DescribeParametersPaginateResponseParametersTypeDef(
    _DescribeParametersPaginateResponseParametersTypeDef
):
    """
    - *(dict) --*

      Metadata includes information like the ARN of the last user and the date/time the parameter
      was last used.
      - **Name** *(string) --*

        The parameter name.
    """


_DescribeParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeParametersPaginateResponseTypeDef",
    {"Parameters": List[DescribeParametersPaginateResponseParametersTypeDef]},
    total=False,
)


class DescribeParametersPaginateResponseTypeDef(_DescribeParametersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Parameters** *(list) --*

        Parameters returned by the request.
        - *(dict) --*

          Metadata includes information like the ARN of the last user and the date/time the
          parameter was last used.
          - **Name** *(string) --*

            The parameter name.
    """


_DescribePatchBaselinesPaginateFiltersTypeDef = TypedDict(
    "_DescribePatchBaselinesPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class DescribePatchBaselinesPaginateFiltersTypeDef(_DescribePatchBaselinesPaginateFiltersTypeDef):
    """
    - *(dict) --*

      Defines a filter used in Patch Manager APIs.
      - **Key** *(string) --*

        The key for the filter.
    """


_DescribePatchBaselinesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribePatchBaselinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribePatchBaselinesPaginatePaginationConfigTypeDef(
    _DescribePatchBaselinesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribePatchBaselinesPaginateResponseBaselineIdentitiesTypeDef = TypedDict(
    "_DescribePatchBaselinesPaginateResponseBaselineIdentitiesTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)


class DescribePatchBaselinesPaginateResponseBaselineIdentitiesTypeDef(
    _DescribePatchBaselinesPaginateResponseBaselineIdentitiesTypeDef
):
    """
    - *(dict) --*

      Defines the basic information about a patch baseline.
      - **BaselineId** *(string) --*

        The ID of the patch baseline.
    """


_DescribePatchBaselinesPaginateResponseTypeDef = TypedDict(
    "_DescribePatchBaselinesPaginateResponseTypeDef",
    {"BaselineIdentities": List[DescribePatchBaselinesPaginateResponseBaselineIdentitiesTypeDef]},
    total=False,
)


class DescribePatchBaselinesPaginateResponseTypeDef(_DescribePatchBaselinesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **BaselineIdentities** *(list) --*

        An array of PatchBaselineIdentity elements.
        - *(dict) --*

          Defines the basic information about a patch baseline.
          - **BaselineId** *(string) --*

            The ID of the patch baseline.
    """


_DescribePatchGroupsPaginateFiltersTypeDef = TypedDict(
    "_DescribePatchGroupsPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class DescribePatchGroupsPaginateFiltersTypeDef(_DescribePatchGroupsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      Defines a filter used in Patch Manager APIs.
      - **Key** *(string) --*

        The key for the filter.
    """


_DescribePatchGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribePatchGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribePatchGroupsPaginatePaginationConfigTypeDef(
    _DescribePatchGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribePatchGroupsPaginateResponseMappingsBaselineIdentityTypeDef = TypedDict(
    "_DescribePatchGroupsPaginateResponseMappingsBaselineIdentityTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)


class DescribePatchGroupsPaginateResponseMappingsBaselineIdentityTypeDef(
    _DescribePatchGroupsPaginateResponseMappingsBaselineIdentityTypeDef
):
    pass


_DescribePatchGroupsPaginateResponseMappingsTypeDef = TypedDict(
    "_DescribePatchGroupsPaginateResponseMappingsTypeDef",
    {
        "PatchGroup": str,
        "BaselineIdentity": DescribePatchGroupsPaginateResponseMappingsBaselineIdentityTypeDef,
    },
    total=False,
)


class DescribePatchGroupsPaginateResponseMappingsTypeDef(
    _DescribePatchGroupsPaginateResponseMappingsTypeDef
):
    """
    - *(dict) --*

      The mapping between a patch group and the patch baseline the patch group is registered with.
      - **PatchGroup** *(string) --*

        The name of the patch group registered with the patch baseline.
    """


_DescribePatchGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribePatchGroupsPaginateResponseTypeDef",
    {"Mappings": List[DescribePatchGroupsPaginateResponseMappingsTypeDef]},
    total=False,
)


class DescribePatchGroupsPaginateResponseTypeDef(_DescribePatchGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Mappings** *(list) --*

        Each entry in the array contains:
        PatchGroup: string (between 1 and 256 characters, Regex:
        ^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$)
        PatchBaselineIdentity: A PatchBaselineIdentity element.
        - *(dict) --*

          The mapping between a patch group and the patch baseline the patch group is registered
          with.
          - **PatchGroup** *(string) --*

            The name of the patch group registered with the patch baseline.
    """


_RequiredDescribeSessionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeSessionsPaginateFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Target", "Owner", "Status"]},
)
_OptionalDescribeSessionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeSessionsPaginateFiltersTypeDef", {"value": str}, total=False
)


class DescribeSessionsPaginateFiltersTypeDef(
    _RequiredDescribeSessionsPaginateFiltersTypeDef, _OptionalDescribeSessionsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      Describes a filter for Session Manager information.
      - **key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_DescribeSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSessionsPaginatePaginationConfigTypeDef(
    _DescribeSessionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeSessionsPaginateResponseSessionsOutputUrlTypeDef = TypedDict(
    "_DescribeSessionsPaginateResponseSessionsOutputUrlTypeDef",
    {"S3OutputUrl": str, "CloudWatchOutputUrl": str},
    total=False,
)


class DescribeSessionsPaginateResponseSessionsOutputUrlTypeDef(
    _DescribeSessionsPaginateResponseSessionsOutputUrlTypeDef
):
    pass


_DescribeSessionsPaginateResponseSessionsTypeDef = TypedDict(
    "_DescribeSessionsPaginateResponseSessionsTypeDef",
    {
        "SessionId": str,
        "Target": str,
        "Status": Literal[
            "Connected", "Connecting", "Disconnected", "Terminated", "Terminating", "Failed"
        ],
        "StartDate": datetime,
        "EndDate": datetime,
        "DocumentName": str,
        "Owner": str,
        "Details": str,
        "OutputUrl": DescribeSessionsPaginateResponseSessionsOutputUrlTypeDef,
    },
    total=False,
)


class DescribeSessionsPaginateResponseSessionsTypeDef(
    _DescribeSessionsPaginateResponseSessionsTypeDef
):
    """
    - *(dict) --*

      Information about a Session Manager connection to an instance.
      - **SessionId** *(string) --*

        The ID of the session.
    """


_DescribeSessionsPaginateResponseTypeDef = TypedDict(
    "_DescribeSessionsPaginateResponseTypeDef",
    {"Sessions": List[DescribeSessionsPaginateResponseSessionsTypeDef]},
    total=False,
)


class DescribeSessionsPaginateResponseTypeDef(_DescribeSessionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Sessions** *(list) --*

        A list of sessions meeting the request parameters.
        - *(dict) --*

          Information about a Session Manager connection to an instance.
          - **SessionId** *(string) --*

            The ID of the session.
    """


_GetInventoryPaginateAggregatorsGroupsFiltersTypeDef = TypedDict(
    "_GetInventoryPaginateAggregatorsGroupsFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class GetInventoryPaginateAggregatorsGroupsFiltersTypeDef(
    _GetInventoryPaginateAggregatorsGroupsFiltersTypeDef
):
    pass


_GetInventoryPaginateAggregatorsGroupsTypeDef = TypedDict(
    "_GetInventoryPaginateAggregatorsGroupsTypeDef",
    {"Name": str, "Filters": List[GetInventoryPaginateAggregatorsGroupsFiltersTypeDef]},
    total=False,
)


class GetInventoryPaginateAggregatorsGroupsTypeDef(_GetInventoryPaginateAggregatorsGroupsTypeDef):
    pass


_GetInventoryPaginateAggregatorsTypeDef = TypedDict(
    "_GetInventoryPaginateAggregatorsTypeDef",
    {
        "Expression": str,
        "Aggregators": Any,
        "Groups": List[GetInventoryPaginateAggregatorsGroupsTypeDef],
    },
    total=False,
)


class GetInventoryPaginateAggregatorsTypeDef(_GetInventoryPaginateAggregatorsTypeDef):
    """
    - *(dict) --*

      Specifies the inventory type and attribute for the aggregation execution.
      - **Expression** *(string) --*

        The inventory type and attribute name for aggregation.
    """


_RequiredGetInventoryPaginateFiltersTypeDef = TypedDict(
    "_RequiredGetInventoryPaginateFiltersTypeDef", {"Key": str}
)
_OptionalGetInventoryPaginateFiltersTypeDef = TypedDict(
    "_OptionalGetInventoryPaginateFiltersTypeDef",
    {
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class GetInventoryPaginateFiltersTypeDef(
    _RequiredGetInventoryPaginateFiltersTypeDef, _OptionalGetInventoryPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of results.
      - **Key** *(string) --***[REQUIRED]**

        The name of the filter key.
    """


_GetInventoryPaginatePaginationConfigTypeDef = TypedDict(
    "_GetInventoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetInventoryPaginatePaginationConfigTypeDef(_GetInventoryPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetInventoryPaginateResponseEntitiesDataTypeDef = TypedDict(
    "_GetInventoryPaginateResponseEntitiesDataTypeDef",
    {
        "TypeName": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "ContentHash": str,
        "Content": List[Dict[str, str]],
    },
    total=False,
)


class GetInventoryPaginateResponseEntitiesDataTypeDef(
    _GetInventoryPaginateResponseEntitiesDataTypeDef
):
    pass


_GetInventoryPaginateResponseEntitiesTypeDef = TypedDict(
    "_GetInventoryPaginateResponseEntitiesTypeDef",
    {"Id": str, "Data": Dict[str, GetInventoryPaginateResponseEntitiesDataTypeDef]},
    total=False,
)


class GetInventoryPaginateResponseEntitiesTypeDef(_GetInventoryPaginateResponseEntitiesTypeDef):
    """
    - *(dict) --*

      Inventory query results.
      - **Id** *(string) --*

        ID of the inventory result entity. For example, for managed instance inventory the result
        will be the managed instance ID. For EC2 instance inventory, the result will be the instance
        ID.
    """


_GetInventoryPaginateResponseTypeDef = TypedDict(
    "_GetInventoryPaginateResponseTypeDef",
    {"Entities": List[GetInventoryPaginateResponseEntitiesTypeDef]},
    total=False,
)


class GetInventoryPaginateResponseTypeDef(_GetInventoryPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Entities** *(list) --*

        Collection of inventory entities such as a collection of instance inventory.
        - *(dict) --*

          Inventory query results.
          - **Id** *(string) --*

            ID of the inventory result entity. For example, for managed instance inventory the
            result will be the managed instance ID. For EC2 instance inventory, the result will be
            the instance ID.
    """


_GetInventoryPaginateResultAttributesTypeDef = TypedDict(
    "_GetInventoryPaginateResultAttributesTypeDef", {"TypeName": str}
)


class GetInventoryPaginateResultAttributesTypeDef(_GetInventoryPaginateResultAttributesTypeDef):
    """
    - *(dict) --*

      The inventory item result attribute.
      - **TypeName** *(string) --***[REQUIRED]**

        Name of the inventory item type. Valid value: AWS:InstanceInformation. Default Value:
        AWS:InstanceInformation.
    """


_GetInventorySchemaPaginatePaginationConfigTypeDef = TypedDict(
    "_GetInventorySchemaPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetInventorySchemaPaginatePaginationConfigTypeDef(
    _GetInventorySchemaPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetInventorySchemaPaginateResponseSchemasAttributesTypeDef = TypedDict(
    "_GetInventorySchemaPaginateResponseSchemasAttributesTypeDef",
    {"Name": str, "DataType": Literal["string", "number"]},
    total=False,
)


class GetInventorySchemaPaginateResponseSchemasAttributesTypeDef(
    _GetInventorySchemaPaginateResponseSchemasAttributesTypeDef
):
    pass


_GetInventorySchemaPaginateResponseSchemasTypeDef = TypedDict(
    "_GetInventorySchemaPaginateResponseSchemasTypeDef",
    {
        "TypeName": str,
        "Version": str,
        "Attributes": List[GetInventorySchemaPaginateResponseSchemasAttributesTypeDef],
        "DisplayName": str,
    },
    total=False,
)


class GetInventorySchemaPaginateResponseSchemasTypeDef(
    _GetInventorySchemaPaginateResponseSchemasTypeDef
):
    """
    - *(dict) --*

      The inventory item schema definition. Users can use this to compose inventory query filters.
      - **TypeName** *(string) --*

        The name of the inventory type. Default inventory item type names start with AWS. Custom
        inventory type names will start with Custom. Default inventory item types include the
        following: AWS:AWSComponent, AWS:Application, AWS:InstanceInformation, AWS:Network, and
        AWS:WindowsUpdate.
    """


_GetInventorySchemaPaginateResponseTypeDef = TypedDict(
    "_GetInventorySchemaPaginateResponseTypeDef",
    {"Schemas": List[GetInventorySchemaPaginateResponseSchemasTypeDef]},
    total=False,
)


class GetInventorySchemaPaginateResponseTypeDef(_GetInventorySchemaPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Schemas** *(list) --*

        Inventory schemas returned by the request.
        - *(dict) --*

          The inventory item schema definition. Users can use this to compose inventory query
          filters.
          - **TypeName** *(string) --*

            The name of the inventory type. Default inventory item type names start with AWS. Custom
            inventory type names will start with Custom. Default inventory item types include the
            following: AWS:AWSComponent, AWS:Application, AWS:InstanceInformation, AWS:Network, and
            AWS:WindowsUpdate.
    """


_GetParameterHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_GetParameterHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetParameterHistoryPaginatePaginationConfigTypeDef(
    _GetParameterHistoryPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetParameterHistoryPaginateResponseParametersPoliciesTypeDef = TypedDict(
    "_GetParameterHistoryPaginateResponseParametersPoliciesTypeDef",
    {"PolicyText": str, "PolicyType": str, "PolicyStatus": str},
    total=False,
)


class GetParameterHistoryPaginateResponseParametersPoliciesTypeDef(
    _GetParameterHistoryPaginateResponseParametersPoliciesTypeDef
):
    pass


_GetParameterHistoryPaginateResponseParametersTypeDef = TypedDict(
    "_GetParameterHistoryPaginateResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "Value": str,
        "AllowedPattern": str,
        "Version": int,
        "Labels": List[str],
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List[GetParameterHistoryPaginateResponseParametersPoliciesTypeDef],
    },
    total=False,
)


class GetParameterHistoryPaginateResponseParametersTypeDef(
    _GetParameterHistoryPaginateResponseParametersTypeDef
):
    """
    - *(dict) --*

      Information about parameter usage.
      - **Name** *(string) --*

        The name of the parameter.
    """


_GetParameterHistoryPaginateResponseTypeDef = TypedDict(
    "_GetParameterHistoryPaginateResponseTypeDef",
    {"Parameters": List[GetParameterHistoryPaginateResponseParametersTypeDef]},
    total=False,
)


class GetParameterHistoryPaginateResponseTypeDef(_GetParameterHistoryPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Parameters** *(list) --*

        A list of parameters returned by the request.
        - *(dict) --*

          Information about parameter usage.
          - **Name** *(string) --*

            The name of the parameter.
    """


_GetParametersByPathPaginatePaginationConfigTypeDef = TypedDict(
    "_GetParametersByPathPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetParametersByPathPaginatePaginationConfigTypeDef(
    _GetParametersByPathPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetParametersByPathPaginateParameterFiltersTypeDef = TypedDict(
    "_GetParametersByPathPaginateParameterFiltersTypeDef",
    {"Key": str, "Option": str, "Values": List[str]},
    total=False,
)


class GetParametersByPathPaginateParameterFiltersTypeDef(
    _GetParametersByPathPaginateParameterFiltersTypeDef
):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of results.
      .. warning::

        The ``ParameterStringFilter`` object is used by the  DescribeParameters and
        GetParametersByPath API actions. However, not all of the pattern values listed for ``Key``
        can be used with both actions.
        For ``DescribeActions`` , all of the listed patterns are valid, with the exception of
        ``Label`` .
        For ``GetParametersByPath`` , the following patterns listed for ``Key`` are not valid:
        ``Name`` , ``Path`` , and ``Tier`` .
        For examples of CLI commands demonstrating valid parameter filter constructions, see
        `Searching for Systems Manager Parameters
        <http://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-search.html>`__ in
        the *AWS Systems Manager User Guide* .
    """


_GetParametersByPathPaginateResponseParametersTypeDef = TypedDict(
    "_GetParametersByPathPaginateResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
    },
    total=False,
)


class GetParametersByPathPaginateResponseParametersTypeDef(
    _GetParametersByPathPaginateResponseParametersTypeDef
):
    """
    - *(dict) --*

      An Amazon EC2 Systems Manager parameter in Parameter Store.
      - **Name** *(string) --*

        The name of the parameter.
    """


_GetParametersByPathPaginateResponseTypeDef = TypedDict(
    "_GetParametersByPathPaginateResponseTypeDef",
    {"Parameters": List[GetParametersByPathPaginateResponseParametersTypeDef]},
    total=False,
)


class GetParametersByPathPaginateResponseTypeDef(_GetParametersByPathPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Parameters** *(list) --*

        A list of parameters found in the specified hierarchy.
        - *(dict) --*

          An Amazon EC2 Systems Manager parameter in Parameter Store.
          - **Name** *(string) --*

            The name of the parameter.
    """


_ListAssociationVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssociationVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssociationVersionsPaginatePaginationConfigTypeDef(
    _ListAssociationVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationS3LocationTypeDef = TypedDict(
    "_ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)


class ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationS3LocationTypeDef(
    _ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationS3LocationTypeDef
):
    pass


_ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationTypeDef = TypedDict(
    "_ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationTypeDef",
    {
        "S3Location": ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationS3LocationTypeDef
    },
    total=False,
)


class ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationTypeDef(
    _ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationTypeDef
):
    pass


_ListAssociationVersionsPaginateResponseAssociationVersionsTargetsTypeDef = TypedDict(
    "_ListAssociationVersionsPaginateResponseAssociationVersionsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ListAssociationVersionsPaginateResponseAssociationVersionsTargetsTypeDef(
    _ListAssociationVersionsPaginateResponseAssociationVersionsTargetsTypeDef
):
    pass


_ListAssociationVersionsPaginateResponseAssociationVersionsTypeDef = TypedDict(
    "_ListAssociationVersionsPaginateResponseAssociationVersionsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "CreatedDate": datetime,
        "Name": str,
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "Targets": List[ListAssociationVersionsPaginateResponseAssociationVersionsTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationTypeDef,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)


class ListAssociationVersionsPaginateResponseAssociationVersionsTypeDef(
    _ListAssociationVersionsPaginateResponseAssociationVersionsTypeDef
):
    """
    - *(dict) --*

      Information about the association version.
      - **AssociationId** *(string) --*

        The ID created by the system when the association was created.
    """


_ListAssociationVersionsPaginateResponseTypeDef = TypedDict(
    "_ListAssociationVersionsPaginateResponseTypeDef",
    {
        "AssociationVersions": List[
            ListAssociationVersionsPaginateResponseAssociationVersionsTypeDef
        ]
    },
    total=False,
)


class ListAssociationVersionsPaginateResponseTypeDef(
    _ListAssociationVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **AssociationVersions** *(list) --*

        Information about all versions of the association for the specified association ID.
        - *(dict) --*

          Information about the association version.
          - **AssociationId** *(string) --*

            The ID created by the system when the association was created.
    """


_RequiredListAssociationsPaginateAssociationFilterListTypeDef = TypedDict(
    "_RequiredListAssociationsPaginateAssociationFilterListTypeDef",
    {
        "key": Literal[
            "InstanceId",
            "Name",
            "AssociationId",
            "AssociationStatusName",
            "LastExecutedBefore",
            "LastExecutedAfter",
            "AssociationName",
        ]
    },
)
_OptionalListAssociationsPaginateAssociationFilterListTypeDef = TypedDict(
    "_OptionalListAssociationsPaginateAssociationFilterListTypeDef", {"value": str}, total=False
)


class ListAssociationsPaginateAssociationFilterListTypeDef(
    _RequiredListAssociationsPaginateAssociationFilterListTypeDef,
    _OptionalListAssociationsPaginateAssociationFilterListTypeDef,
):
    """
    - *(dict) --*

      Describes a filter.
      - **key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ListAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssociationsPaginatePaginationConfigTypeDef(
    _ListAssociationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAssociationsPaginateResponseAssociationsOverviewTypeDef = TypedDict(
    "_ListAssociationsPaginateResponseAssociationsOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)


class ListAssociationsPaginateResponseAssociationsOverviewTypeDef(
    _ListAssociationsPaginateResponseAssociationsOverviewTypeDef
):
    pass


_ListAssociationsPaginateResponseAssociationsTargetsTypeDef = TypedDict(
    "_ListAssociationsPaginateResponseAssociationsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ListAssociationsPaginateResponseAssociationsTargetsTypeDef(
    _ListAssociationsPaginateResponseAssociationsTargetsTypeDef
):
    pass


_ListAssociationsPaginateResponseAssociationsTypeDef = TypedDict(
    "_ListAssociationsPaginateResponseAssociationsTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationId": str,
        "AssociationVersion": str,
        "DocumentVersion": str,
        "Targets": List[ListAssociationsPaginateResponseAssociationsTargetsTypeDef],
        "LastExecutionDate": datetime,
        "Overview": ListAssociationsPaginateResponseAssociationsOverviewTypeDef,
        "ScheduleExpression": str,
        "AssociationName": str,
    },
    total=False,
)


class ListAssociationsPaginateResponseAssociationsTypeDef(
    _ListAssociationsPaginateResponseAssociationsTypeDef
):
    """
    - *(dict) --*

      Describes an association of a Systems Manager document and an instance.
      - **Name** *(string) --*

        The name of the Systems Manager document.
    """


_ListAssociationsPaginateResponseTypeDef = TypedDict(
    "_ListAssociationsPaginateResponseTypeDef",
    {"Associations": List[ListAssociationsPaginateResponseAssociationsTypeDef]},
    total=False,
)


class ListAssociationsPaginateResponseTypeDef(_ListAssociationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Associations** *(list) --*

        The associations.
        - *(dict) --*

          Describes an association of a Systems Manager document and an instance.
          - **Name** *(string) --*

            The name of the Systems Manager document.
    """


_RequiredListCommandInvocationsPaginateFiltersTypeDef = TypedDict(
    "_RequiredListCommandInvocationsPaginateFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Status", "ExecutionStage", "DocumentName"]},
)
_OptionalListCommandInvocationsPaginateFiltersTypeDef = TypedDict(
    "_OptionalListCommandInvocationsPaginateFiltersTypeDef", {"value": str}, total=False
)


class ListCommandInvocationsPaginateFiltersTypeDef(
    _RequiredListCommandInvocationsPaginateFiltersTypeDef,
    _OptionalListCommandInvocationsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      Describes a command filter.
      - **key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ListCommandInvocationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCommandInvocationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCommandInvocationsPaginatePaginationConfigTypeDef(
    _ListCommandInvocationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCommandInvocationsPaginateResponseCommandInvocationsCloudWatchOutputConfigTypeDef = TypedDict(
    "_ListCommandInvocationsPaginateResponseCommandInvocationsCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)


class ListCommandInvocationsPaginateResponseCommandInvocationsCloudWatchOutputConfigTypeDef(
    _ListCommandInvocationsPaginateResponseCommandInvocationsCloudWatchOutputConfigTypeDef
):
    pass


_ListCommandInvocationsPaginateResponseCommandInvocationsCommandPluginsTypeDef = TypedDict(
    "_ListCommandInvocationsPaginateResponseCommandInvocationsCommandPluginsTypeDef",
    {
        "Name": str,
        "Status": Literal["Pending", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"],
        "StatusDetails": str,
        "ResponseCode": int,
        "ResponseStartDateTime": datetime,
        "ResponseFinishDateTime": datetime,
        "Output": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
    },
    total=False,
)


class ListCommandInvocationsPaginateResponseCommandInvocationsCommandPluginsTypeDef(
    _ListCommandInvocationsPaginateResponseCommandInvocationsCommandPluginsTypeDef
):
    pass


_ListCommandInvocationsPaginateResponseCommandInvocationsNotificationConfigTypeDef = TypedDict(
    "_ListCommandInvocationsPaginateResponseCommandInvocationsNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)


class ListCommandInvocationsPaginateResponseCommandInvocationsNotificationConfigTypeDef(
    _ListCommandInvocationsPaginateResponseCommandInvocationsNotificationConfigTypeDef
):
    pass


_ListCommandInvocationsPaginateResponseCommandInvocationsTypeDef = TypedDict(
    "_ListCommandInvocationsPaginateResponseCommandInvocationsTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "InstanceName": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending",
            "InProgress",
            "Delayed",
            "Success",
            "Cancelled",
            "TimedOut",
            "Failed",
            "Cancelling",
        ],
        "StatusDetails": str,
        "TraceOutput": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "CommandPlugins": List[
            ListCommandInvocationsPaginateResponseCommandInvocationsCommandPluginsTypeDef
        ],
        "ServiceRole": str,
        "NotificationConfig": ListCommandInvocationsPaginateResponseCommandInvocationsNotificationConfigTypeDef,
        "CloudWatchOutputConfig": ListCommandInvocationsPaginateResponseCommandInvocationsCloudWatchOutputConfigTypeDef,
    },
    total=False,
)


class ListCommandInvocationsPaginateResponseCommandInvocationsTypeDef(
    _ListCommandInvocationsPaginateResponseCommandInvocationsTypeDef
):
    """
    - *(dict) --*

      An invocation is copy of a command sent to a specific instance. A command can apply to one or
      more instances. A command invocation applies to one instance. For example, if a user runs
      SendCommand against three instances, then a command invocation is created for each requested
      instance ID. A command invocation returns status and detail information about a command you
      ran.
      - **CommandId** *(string) --*

        The command against which this invocation was requested.
    """


_ListCommandInvocationsPaginateResponseTypeDef = TypedDict(
    "_ListCommandInvocationsPaginateResponseTypeDef",
    {"CommandInvocations": List[ListCommandInvocationsPaginateResponseCommandInvocationsTypeDef]},
    total=False,
)


class ListCommandInvocationsPaginateResponseTypeDef(_ListCommandInvocationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **CommandInvocations** *(list) --*

        (Optional) A list of all invocations.
        - *(dict) --*

          An invocation is copy of a command sent to a specific instance. A command can apply to one
          or more instances. A command invocation applies to one instance. For example, if a user
          runs SendCommand against three instances, then a command invocation is created for each
          requested instance ID. A command invocation returns status and detail information about a
          command you ran.
          - **CommandId** *(string) --*

            The command against which this invocation was requested.
    """


_RequiredListCommandsPaginateFiltersTypeDef = TypedDict(
    "_RequiredListCommandsPaginateFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Status", "ExecutionStage", "DocumentName"]},
)
_OptionalListCommandsPaginateFiltersTypeDef = TypedDict(
    "_OptionalListCommandsPaginateFiltersTypeDef", {"value": str}, total=False
)


class ListCommandsPaginateFiltersTypeDef(
    _RequiredListCommandsPaginateFiltersTypeDef, _OptionalListCommandsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      Describes a command filter.
      - **key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ListCommandsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCommandsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCommandsPaginatePaginationConfigTypeDef(_ListCommandsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCommandsPaginateResponseCommandsCloudWatchOutputConfigTypeDef = TypedDict(
    "_ListCommandsPaginateResponseCommandsCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)


class ListCommandsPaginateResponseCommandsCloudWatchOutputConfigTypeDef(
    _ListCommandsPaginateResponseCommandsCloudWatchOutputConfigTypeDef
):
    pass


_ListCommandsPaginateResponseCommandsNotificationConfigTypeDef = TypedDict(
    "_ListCommandsPaginateResponseCommandsNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)


class ListCommandsPaginateResponseCommandsNotificationConfigTypeDef(
    _ListCommandsPaginateResponseCommandsNotificationConfigTypeDef
):
    pass


_ListCommandsPaginateResponseCommandsTargetsTypeDef = TypedDict(
    "_ListCommandsPaginateResponseCommandsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ListCommandsPaginateResponseCommandsTargetsTypeDef(
    _ListCommandsPaginateResponseCommandsTargetsTypeDef
):
    pass


_ListCommandsPaginateResponseCommandsTypeDef = TypedDict(
    "_ListCommandsPaginateResponseCommandsTypeDef",
    {
        "CommandId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "Comment": str,
        "ExpiresAfter": datetime,
        "Parameters": Dict[str, List[str]],
        "InstanceIds": List[str],
        "Targets": List[ListCommandsPaginateResponseCommandsTargetsTypeDef],
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending", "InProgress", "Success", "Cancelled", "Failed", "TimedOut", "Cancelling"
        ],
        "StatusDetails": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetCount": int,
        "CompletedCount": int,
        "ErrorCount": int,
        "DeliveryTimedOutCount": int,
        "ServiceRole": str,
        "NotificationConfig": ListCommandsPaginateResponseCommandsNotificationConfigTypeDef,
        "CloudWatchOutputConfig": ListCommandsPaginateResponseCommandsCloudWatchOutputConfigTypeDef,
    },
    total=False,
)


class ListCommandsPaginateResponseCommandsTypeDef(_ListCommandsPaginateResponseCommandsTypeDef):
    """
    - *(dict) --*

      Describes a command request.
      - **CommandId** *(string) --*

        A unique identifier for this command.
    """


_ListCommandsPaginateResponseTypeDef = TypedDict(
    "_ListCommandsPaginateResponseTypeDef",
    {"Commands": List[ListCommandsPaginateResponseCommandsTypeDef]},
    total=False,
)


class ListCommandsPaginateResponseTypeDef(_ListCommandsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Commands** *(list) --*

        (Optional) The list of commands requested by the user.
        - *(dict) --*

          Describes a command request.
          - **CommandId** *(string) --*

            A unique identifier for this command.
    """


_ListComplianceItemsPaginateFiltersTypeDef = TypedDict(
    "_ListComplianceItemsPaginateFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)


class ListComplianceItemsPaginateFiltersTypeDef(_ListComplianceItemsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of results.
      - **Key** *(string) --*

        The name of the filter.
    """


_ListComplianceItemsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListComplianceItemsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListComplianceItemsPaginatePaginationConfigTypeDef(
    _ListComplianceItemsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListComplianceItemsPaginateResponseComplianceItemsExecutionSummaryTypeDef = TypedDict(
    "_ListComplianceItemsPaginateResponseComplianceItemsExecutionSummaryTypeDef",
    {"ExecutionTime": datetime, "ExecutionId": str, "ExecutionType": str},
    total=False,
)


class ListComplianceItemsPaginateResponseComplianceItemsExecutionSummaryTypeDef(
    _ListComplianceItemsPaginateResponseComplianceItemsExecutionSummaryTypeDef
):
    pass


_ListComplianceItemsPaginateResponseComplianceItemsTypeDef = TypedDict(
    "_ListComplianceItemsPaginateResponseComplianceItemsTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Id": str,
        "Title": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "Severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"],
        "ExecutionSummary": ListComplianceItemsPaginateResponseComplianceItemsExecutionSummaryTypeDef,
        "Details": Dict[str, str],
    },
    total=False,
)


class ListComplianceItemsPaginateResponseComplianceItemsTypeDef(
    _ListComplianceItemsPaginateResponseComplianceItemsTypeDef
):
    """
    - *(dict) --*

      Information about the compliance as defined by the resource type. For example, for a patch
      resource type, ``Items`` includes information about the PatchSeverity, Classification, etc.
      - **ComplianceType** *(string) --*

        The compliance type. For example, Association (for a State Manager association), Patch, or
        Custom:``string`` are all valid compliance types.
    """


_ListComplianceItemsPaginateResponseTypeDef = TypedDict(
    "_ListComplianceItemsPaginateResponseTypeDef",
    {"ComplianceItems": List[ListComplianceItemsPaginateResponseComplianceItemsTypeDef]},
    total=False,
)


class ListComplianceItemsPaginateResponseTypeDef(_ListComplianceItemsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ComplianceItems** *(list) --*

        A list of compliance information for the specified resource ID.
        - *(dict) --*

          Information about the compliance as defined by the resource type. For example, for a patch
          resource type, ``Items`` includes information about the PatchSeverity, Classification,
          etc.
          - **ComplianceType** *(string) --*

            The compliance type. For example, Association (for a State Manager association), Patch,
            or Custom:``string`` are all valid compliance types.
    """


_ListComplianceSummariesPaginateFiltersTypeDef = TypedDict(
    "_ListComplianceSummariesPaginateFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)


class ListComplianceSummariesPaginateFiltersTypeDef(_ListComplianceSummariesPaginateFiltersTypeDef):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of results.
      - **Key** *(string) --*

        The name of the filter.
    """


_ListComplianceSummariesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListComplianceSummariesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListComplianceSummariesPaginatePaginationConfigTypeDef(
    _ListComplianceSummariesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "_ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)


class ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef(
    _ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef
):
    pass


_ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummaryTypeDef = TypedDict(
    "_ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummaryTypeDef",
    {
        "CompliantCount": int,
        "SeveritySummary": ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)


class ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummaryTypeDef(
    _ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummaryTypeDef
):
    pass


_ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "_ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)


class ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef(
    _ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef
):
    pass


_ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummaryTypeDef = TypedDict(
    "_ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": int,
        "SeveritySummary": ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)


class ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummaryTypeDef(
    _ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummaryTypeDef
):
    pass


_ListComplianceSummariesPaginateResponseComplianceSummaryItemsTypeDef = TypedDict(
    "_ListComplianceSummariesPaginateResponseComplianceSummaryItemsTypeDef",
    {
        "ComplianceType": str,
        "CompliantSummary": ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummaryTypeDef,
        "NonCompliantSummary": ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummaryTypeDef,
    },
    total=False,
)


class ListComplianceSummariesPaginateResponseComplianceSummaryItemsTypeDef(
    _ListComplianceSummariesPaginateResponseComplianceSummaryItemsTypeDef
):
    """
    - *(dict) --*

      A summary of compliance information by compliance type.
      - **ComplianceType** *(string) --*

        The type of compliance item. For example, the compliance type can be Association, Patch, or
        Custom:string.
    """


_ListComplianceSummariesPaginateResponseTypeDef = TypedDict(
    "_ListComplianceSummariesPaginateResponseTypeDef",
    {
        "ComplianceSummaryItems": List[
            ListComplianceSummariesPaginateResponseComplianceSummaryItemsTypeDef
        ]
    },
    total=False,
)


class ListComplianceSummariesPaginateResponseTypeDef(
    _ListComplianceSummariesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ComplianceSummaryItems** *(list) --*

        A list of compliant and non-compliant summary counts based on compliance types. For example,
        this call returns State Manager associations, patches, or custom compliance types according
        to the filter criteria that you specified.
        - *(dict) --*

          A summary of compliance information by compliance type.
          - **ComplianceType** *(string) --*

            The type of compliance item. For example, the compliance type can be Association, Patch,
            or Custom:string.
    """


_ListDocumentVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDocumentVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDocumentVersionsPaginatePaginationConfigTypeDef(
    _ListDocumentVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDocumentVersionsPaginateResponseDocumentVersionsTypeDef = TypedDict(
    "_ListDocumentVersionsPaginateResponseDocumentVersionsTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
        "VersionName": str,
        "CreatedDate": datetime,
        "IsDefaultVersion": bool,
        "DocumentFormat": Literal["YAML", "JSON"],
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
    },
    total=False,
)


class ListDocumentVersionsPaginateResponseDocumentVersionsTypeDef(
    _ListDocumentVersionsPaginateResponseDocumentVersionsTypeDef
):
    """
    - *(dict) --*

      Version information about the document.
      - **Name** *(string) --*

        The document name.
    """


_ListDocumentVersionsPaginateResponseTypeDef = TypedDict(
    "_ListDocumentVersionsPaginateResponseTypeDef",
    {"DocumentVersions": List[ListDocumentVersionsPaginateResponseDocumentVersionsTypeDef]},
    total=False,
)


class ListDocumentVersionsPaginateResponseTypeDef(_ListDocumentVersionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **DocumentVersions** *(list) --*

        The document versions.
        - *(dict) --*

          Version information about the document.
          - **Name** *(string) --*

            The document name.
    """


_RequiredListDocumentsPaginateDocumentFilterListTypeDef = TypedDict(
    "_RequiredListDocumentsPaginateDocumentFilterListTypeDef",
    {"key": Literal["Name", "Owner", "PlatformTypes", "DocumentType"]},
)
_OptionalListDocumentsPaginateDocumentFilterListTypeDef = TypedDict(
    "_OptionalListDocumentsPaginateDocumentFilterListTypeDef", {"value": str}, total=False
)


class ListDocumentsPaginateDocumentFilterListTypeDef(
    _RequiredListDocumentsPaginateDocumentFilterListTypeDef,
    _OptionalListDocumentsPaginateDocumentFilterListTypeDef,
):
    """
    - *(dict) --*

      Describes a filter.
      - **key** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ListDocumentsPaginateFiltersTypeDef = TypedDict(
    "_ListDocumentsPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ListDocumentsPaginateFiltersTypeDef(_ListDocumentsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of documents.
      For keys, you can specify one or more tags that have been applied to a document.
      Other valid values include Owner, Name, PlatformTypes, and DocumentType.
      Note that only one Owner can be specified in a request. For example: ``Key=Owner,Values=
          Self``
      .
      If you use Name as a key, you can use a name prefix to return a list of documents. For
      example, in the AWS CLI, to return a list of all documents that begin with ``Te`` , run the
      following command:

        ``aws ssm list-documents --filters Key=Name,Values=Te``
    """


_ListDocumentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDocumentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDocumentsPaginatePaginationConfigTypeDef(_ListDocumentsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDocumentsPaginateResponseDocumentIdentifiersRequiresTypeDef = TypedDict(
    "_ListDocumentsPaginateResponseDocumentIdentifiersRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ListDocumentsPaginateResponseDocumentIdentifiersRequiresTypeDef(
    _ListDocumentsPaginateResponseDocumentIdentifiersRequiresTypeDef
):
    pass


_ListDocumentsPaginateResponseDocumentIdentifiersTagsTypeDef = TypedDict(
    "_ListDocumentsPaginateResponseDocumentIdentifiersTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListDocumentsPaginateResponseDocumentIdentifiersTagsTypeDef(
    _ListDocumentsPaginateResponseDocumentIdentifiersTagsTypeDef
):
    pass


_ListDocumentsPaginateResponseDocumentIdentifiersTypeDef = TypedDict(
    "_ListDocumentsPaginateResponseDocumentIdentifiersTypeDef",
    {
        "Name": str,
        "Owner": str,
        "VersionName": str,
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentVersion": str,
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
        ],
        "SchemaVersion": str,
        "DocumentFormat": Literal["YAML", "JSON"],
        "TargetType": str,
        "Tags": List[ListDocumentsPaginateResponseDocumentIdentifiersTagsTypeDef],
        "Requires": List[ListDocumentsPaginateResponseDocumentIdentifiersRequiresTypeDef],
    },
    total=False,
)


class ListDocumentsPaginateResponseDocumentIdentifiersTypeDef(
    _ListDocumentsPaginateResponseDocumentIdentifiersTypeDef
):
    """
    - *(dict) --*

      Describes the name of a Systems Manager document.
      - **Name** *(string) --*

        The name of the Systems Manager document.
    """


_ListDocumentsPaginateResponseTypeDef = TypedDict(
    "_ListDocumentsPaginateResponseTypeDef",
    {"DocumentIdentifiers": List[ListDocumentsPaginateResponseDocumentIdentifiersTypeDef]},
    total=False,
)


class ListDocumentsPaginateResponseTypeDef(_ListDocumentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **DocumentIdentifiers** *(list) --*

        The names of the Systems Manager documents.
        - *(dict) --*

          Describes the name of a Systems Manager document.
          - **Name** *(string) --*

            The name of the Systems Manager document.
    """


_ListResourceComplianceSummariesPaginateFiltersTypeDef = TypedDict(
    "_ListResourceComplianceSummariesPaginateFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)


class ListResourceComplianceSummariesPaginateFiltersTypeDef(
    _ListResourceComplianceSummariesPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      One or more filters. Use a filter to return a more specific list of results.
      - **Key** *(string) --*

        The name of the filter.
    """


_ListResourceComplianceSummariesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceComplianceSummariesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceComplianceSummariesPaginatePaginationConfigTypeDef(
    _ListResourceComplianceSummariesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "_ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)


class ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef(
    _ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef
):
    pass


_ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef = TypedDict(
    "_ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef",
    {
        "CompliantCount": int,
        "SeveritySummary": ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)


class ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef(
    _ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef
):
    pass


_ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef = TypedDict(
    "_ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef",
    {"ExecutionTime": datetime, "ExecutionId": str, "ExecutionType": str},
    total=False,
)


class ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef(
    _ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef
):
    pass


_ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "_ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)


class ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef(
    _ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef
):
    pass


_ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef = TypedDict(
    "_ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": int,
        "SeveritySummary": ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)


class ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef(
    _ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef
):
    pass


_ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsTypeDef = TypedDict(
    "_ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "OverallSeverity": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ExecutionSummary": ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef,
        "CompliantSummary": ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef,
        "NonCompliantSummary": ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef,
    },
    total=False,
)


class ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsTypeDef(
    _ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsTypeDef
):
    """
    - *(dict) --*

      Compliance summary information for a specific resource.
      - **ComplianceType** *(string) --*

        The compliance type.
    """


_ListResourceComplianceSummariesPaginateResponseTypeDef = TypedDict(
    "_ListResourceComplianceSummariesPaginateResponseTypeDef",
    {
        "ResourceComplianceSummaryItems": List[
            ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsTypeDef
        ]
    },
    total=False,
)


class ListResourceComplianceSummariesPaginateResponseTypeDef(
    _ListResourceComplianceSummariesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ResourceComplianceSummaryItems** *(list) --*

        A summary count for specified or targeted managed instances. Summary count includes
        information about compliant and non-compliant State Manager associations, patch status, or
        custom items according to the filter criteria that you specify.
        - *(dict) --*

          Compliance summary information for a specific resource.
          - **ComplianceType** *(string) --*

            The compliance type.
    """


_ListResourceDataSyncPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceDataSyncPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceDataSyncPaginatePaginationConfigTypeDef(
    _ListResourceDataSyncPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListResourceDataSyncPaginateResponseResourceDataSyncItemsS3DestinationTypeDef = TypedDict(
    "_ListResourceDataSyncPaginateResponseResourceDataSyncItemsS3DestinationTypeDef",
    {"BucketName": str, "Prefix": str, "SyncFormat": str, "Region": str, "AWSKMSKeyARN": str},
    total=False,
)


class ListResourceDataSyncPaginateResponseResourceDataSyncItemsS3DestinationTypeDef(
    _ListResourceDataSyncPaginateResponseResourceDataSyncItemsS3DestinationTypeDef
):
    pass


_ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef = TypedDict(
    "_ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    {"OrganizationalUnitId": str},
    total=False,
)


class ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef(
    _ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
):
    pass


_ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef = TypedDict(
    "_ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": List[
            ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
        ],
    },
    total=False,
)


class ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef(
    _ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef
):
    pass


_ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceTypeDef = TypedDict(
    "_ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceTypeDef",
    {
        "SourceType": str,
        "AwsOrganizationsSource": ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef,
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
        "State": str,
    },
    total=False,
)


class ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceTypeDef(
    _ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceTypeDef
):
    pass


_ListResourceDataSyncPaginateResponseResourceDataSyncItemsTypeDef = TypedDict(
    "_ListResourceDataSyncPaginateResponseResourceDataSyncItemsTypeDef",
    {
        "SyncName": str,
        "SyncType": str,
        "SyncSource": ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceTypeDef,
        "S3Destination": ListResourceDataSyncPaginateResponseResourceDataSyncItemsS3DestinationTypeDef,
        "LastSyncTime": datetime,
        "LastSuccessfulSyncTime": datetime,
        "SyncLastModifiedTime": datetime,
        "LastStatus": Literal["Successful", "Failed", "InProgress"],
        "SyncCreatedTime": datetime,
        "LastSyncStatusMessage": str,
    },
    total=False,
)


class ListResourceDataSyncPaginateResponseResourceDataSyncItemsTypeDef(
    _ListResourceDataSyncPaginateResponseResourceDataSyncItemsTypeDef
):
    """
    - *(dict) --*

      Information about a Resource Data Sync configuration, including its current status and last
      successful sync.
      - **SyncName** *(string) --*

        The name of the Resource Data Sync.
    """


_ListResourceDataSyncPaginateResponseTypeDef = TypedDict(
    "_ListResourceDataSyncPaginateResponseTypeDef",
    {
        "ResourceDataSyncItems": List[
            ListResourceDataSyncPaginateResponseResourceDataSyncItemsTypeDef
        ]
    },
    total=False,
)


class ListResourceDataSyncPaginateResponseTypeDef(_ListResourceDataSyncPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceDataSyncItems** *(list) --*

        A list of your current Resource Data Sync configurations and their statuses.
        - *(dict) --*

          Information about a Resource Data Sync configuration, including its current status and
          last successful sync.
          - **SyncName** *(string) --*

            The name of the Resource Data Sync.
    """
