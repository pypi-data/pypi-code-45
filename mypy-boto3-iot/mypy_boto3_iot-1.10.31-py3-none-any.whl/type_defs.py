"Main interface for iot service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAssociateTargetsWithJobResponseTypeDef",
    "ClientCancelJobResponseTypeDef",
    "ClientCreateAuthorizerResponseTypeDef",
    "ClientCreateBillingGroupBillingGroupPropertiesTypeDef",
    "ClientCreateBillingGroupResponseTypeDef",
    "ClientCreateBillingGroupTagsTypeDef",
    "ClientCreateCertificateFromCsrResponseTypeDef",
    "ClientCreateDomainConfigurationAuthorizerConfigTypeDef",
    "ClientCreateDomainConfigurationResponseTypeDef",
    "ClientCreateDynamicThingGroupResponseTypeDef",
    "ClientCreateDynamicThingGroupTagsTypeDef",
    "ClientCreateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef",
    "ClientCreateDynamicThingGroupThingGroupPropertiesTypeDef",
    "ClientCreateJobAbortConfigcriteriaListTypeDef",
    "ClientCreateJobAbortConfigTypeDef",
    "ClientCreateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef",
    "ClientCreateJobJobExecutionsRolloutConfigexponentialRateTypeDef",
    "ClientCreateJobJobExecutionsRolloutConfigTypeDef",
    "ClientCreateJobPresignedUrlConfigTypeDef",
    "ClientCreateJobResponseTypeDef",
    "ClientCreateJobTagsTypeDef",
    "ClientCreateJobTimeoutConfigTypeDef",
    "ClientCreateKeysAndCertificateResponsekeyPairTypeDef",
    "ClientCreateKeysAndCertificateResponseTypeDef",
    "ClientCreateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef",
    "ClientCreateMitigationActionActionParamsenableIoTLoggingParamsTypeDef",
    "ClientCreateMitigationActionActionParamspublishFindingToSnsParamsTypeDef",
    "ClientCreateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    "ClientCreateMitigationActionActionParamsupdateCACertificateParamsTypeDef",
    "ClientCreateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef",
    "ClientCreateMitigationActionActionParamsTypeDef",
    "ClientCreateMitigationActionResponseTypeDef",
    "ClientCreateMitigationActionTagsTypeDef",
    "ClientCreateOtaUpdateAwsJobExecutionsRolloutConfigTypeDef",
    "ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef",
    "ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef",
    "ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningTypeDef",
    "ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef",
    "ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef",
    "ClientCreateOtaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef",
    "ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterTypeDef",
    "ClientCreateOtaUpdateFilescodeSigningTypeDef",
    "ClientCreateOtaUpdateFilesfileLocations3LocationTypeDef",
    "ClientCreateOtaUpdateFilesfileLocationstreamTypeDef",
    "ClientCreateOtaUpdateFilesfileLocationTypeDef",
    "ClientCreateOtaUpdateFilesTypeDef",
    "ClientCreateOtaUpdateResponseTypeDef",
    "ClientCreateOtaUpdateTagsTypeDef",
    "ClientCreatePolicyResponseTypeDef",
    "ClientCreatePolicyVersionResponseTypeDef",
    "ClientCreateProvisioningClaimResponsekeyPairTypeDef",
    "ClientCreateProvisioningClaimResponseTypeDef",
    "ClientCreateProvisioningTemplateResponseTypeDef",
    "ClientCreateProvisioningTemplateTagsTypeDef",
    "ClientCreateProvisioningTemplateVersionResponseTypeDef",
    "ClientCreateRoleAliasResponseTypeDef",
    "ClientCreateScheduledAuditResponseTypeDef",
    "ClientCreateScheduledAuditTagsTypeDef",
    "ClientCreateSecurityProfileAlertTargetsTypeDef",
    "ClientCreateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef",
    "ClientCreateSecurityProfileBehaviorscriteriavalueTypeDef",
    "ClientCreateSecurityProfileBehaviorscriteriaTypeDef",
    "ClientCreateSecurityProfileBehaviorsTypeDef",
    "ClientCreateSecurityProfileResponseTypeDef",
    "ClientCreateSecurityProfileTagsTypeDef",
    "ClientCreateStreamFiless3LocationTypeDef",
    "ClientCreateStreamFilesTypeDef",
    "ClientCreateStreamResponseTypeDef",
    "ClientCreateStreamTagsTypeDef",
    "ClientCreateThingAttributePayloadTypeDef",
    "ClientCreateThingGroupResponseTypeDef",
    "ClientCreateThingGroupTagsTypeDef",
    "ClientCreateThingGroupThingGroupPropertiesattributePayloadTypeDef",
    "ClientCreateThingGroupThingGroupPropertiesTypeDef",
    "ClientCreateThingResponseTypeDef",
    "ClientCreateThingTypeResponseTypeDef",
    "ClientCreateThingTypeTagsTypeDef",
    "ClientCreateThingTypeThingTypePropertiesTypeDef",
    "ClientCreateTopicRuleDestinationDestinationConfigurationhttpUrlConfigurationTypeDef",
    "ClientCreateTopicRuleDestinationDestinationConfigurationTypeDef",
    "ClientCreateTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef",
    "ClientCreateTopicRuleDestinationResponsetopicRuleDestinationTypeDef",
    "ClientCreateTopicRuleDestinationResponseTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionselasticsearchTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsfirehoseTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionshttpauthTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionshttpheadersTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionshttpTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsiotEventsTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionskinesisTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionslambdaTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsrepublishTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionss3TypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionssalesforceTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionssnsTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionssqsTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadactionsTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionhttpTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionkinesisTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionlambdaTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionrepublishTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActions3TypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionsnsTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionsqsTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef",
    "ClientCreateTopicRuleTopicRulePayloaderrorActionTypeDef",
    "ClientCreateTopicRuleTopicRulePayloadTypeDef",
    "ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef",
    "ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef",
    "ClientDescribeAccountAuditConfigurationResponseTypeDef",
    "ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef",
    "ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef",
    "ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef",
    "ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef",
    "ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef",
    "ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef",
    "ClientDescribeAuditFindingResponsefindingTypeDef",
    "ClientDescribeAuditFindingResponseTypeDef",
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef",
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef",
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef",
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef",
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef",
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef",
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef",
    "ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef",
    "ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef",
    "ClientDescribeAuditMitigationActionsTaskResponseTypeDef",
    "ClientDescribeAuditTaskResponseauditDetailsTypeDef",
    "ClientDescribeAuditTaskResponsetaskStatisticsTypeDef",
    "ClientDescribeAuditTaskResponseTypeDef",
    "ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef",
    "ClientDescribeAuthorizerResponseTypeDef",
    "ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef",
    "ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef",
    "ClientDescribeBillingGroupResponseTypeDef",
    "ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef",
    "ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef",
    "ClientDescribeCaCertificateResponseregistrationConfigTypeDef",
    "ClientDescribeCaCertificateResponseTypeDef",
    "ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef",
    "ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef",
    "ClientDescribeCertificateResponsecertificateDescriptionTypeDef",
    "ClientDescribeCertificateResponseTypeDef",
    "ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef",
    "ClientDescribeDefaultAuthorizerResponseTypeDef",
    "ClientDescribeDomainConfigurationResponseauthorizerConfigTypeDef",
    "ClientDescribeDomainConfigurationResponseserverCertificatesTypeDef",
    "ClientDescribeDomainConfigurationResponseTypeDef",
    "ClientDescribeEndpointResponseTypeDef",
    "ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef",
    "ClientDescribeEventConfigurationsResponseTypeDef",
    "ClientDescribeIndexResponseTypeDef",
    "ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef",
    "ClientDescribeJobExecutionResponseexecutionTypeDef",
    "ClientDescribeJobExecutionResponseTypeDef",
    "ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef",
    "ClientDescribeJobResponsejobabortConfigTypeDef",
    "ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef",
    "ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef",
    "ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef",
    "ClientDescribeJobResponsejobjobProcessDetailsTypeDef",
    "ClientDescribeJobResponsejobpresignedUrlConfigTypeDef",
    "ClientDescribeJobResponsejobtimeoutConfigTypeDef",
    "ClientDescribeJobResponsejobTypeDef",
    "ClientDescribeJobResponseTypeDef",
    "ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef",
    "ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef",
    "ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef",
    "ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    "ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef",
    "ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef",
    "ClientDescribeMitigationActionResponseactionParamsTypeDef",
    "ClientDescribeMitigationActionResponseTypeDef",
    "ClientDescribeProvisioningTemplateResponseTypeDef",
    "ClientDescribeProvisioningTemplateVersionResponseTypeDef",
    "ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef",
    "ClientDescribeRoleAliasResponseTypeDef",
    "ClientDescribeScheduledAuditResponseTypeDef",
    "ClientDescribeSecurityProfileResponsealertTargetsTypeDef",
    "ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef",
    "ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef",
    "ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef",
    "ClientDescribeSecurityProfileResponsebehaviorsTypeDef",
    "ClientDescribeSecurityProfileResponseTypeDef",
    "ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef",
    "ClientDescribeStreamResponsestreamInfofilesTypeDef",
    "ClientDescribeStreamResponsestreamInfoTypeDef",
    "ClientDescribeStreamResponseTypeDef",
    "ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef",
    "ClientDescribeThingGroupResponsethingGroupMetadataTypeDef",
    "ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef",
    "ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef",
    "ClientDescribeThingGroupResponseTypeDef",
    "ClientDescribeThingRegistrationTaskResponseTypeDef",
    "ClientDescribeThingResponseTypeDef",
    "ClientDescribeThingTypeResponsethingTypeMetadataTypeDef",
    "ClientDescribeThingTypeResponsethingTypePropertiesTypeDef",
    "ClientDescribeThingTypeResponseTypeDef",
    "ClientGetCardinalityResponseTypeDef",
    "ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef",
    "ClientGetEffectivePoliciesResponseTypeDef",
    "ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef",
    "ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef",
    "ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef",
    "ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef",
    "ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef",
    "ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef",
    "ClientGetIndexingConfigurationResponseTypeDef",
    "ClientGetJobDocumentResponseTypeDef",
    "ClientGetLoggingOptionsResponseTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef",
    "ClientGetOtaUpdateResponseotaUpdateInfoTypeDef",
    "ClientGetOtaUpdateResponseTypeDef",
    "ClientGetPercentilesResponsepercentilesTypeDef",
    "ClientGetPercentilesResponseTypeDef",
    "ClientGetPolicyResponseTypeDef",
    "ClientGetPolicyVersionResponseTypeDef",
    "ClientGetRegistrationCodeResponseTypeDef",
    "ClientGetStatisticsResponsestatisticsTypeDef",
    "ClientGetStatisticsResponseTypeDef",
    "ClientGetTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef",
    "ClientGetTopicRuleDestinationResponsetopicRuleDestinationTypeDef",
    "ClientGetTopicRuleDestinationResponseTypeDef",
    "ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef",
    "ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef",
    "ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef",
    "ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef",
    "ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef",
    "ClientGetTopicRuleResponseruleactionselasticsearchTypeDef",
    "ClientGetTopicRuleResponseruleactionsfirehoseTypeDef",
    "ClientGetTopicRuleResponseruleactionshttpauthsigv4TypeDef",
    "ClientGetTopicRuleResponseruleactionshttpauthTypeDef",
    "ClientGetTopicRuleResponseruleactionshttpheadersTypeDef",
    "ClientGetTopicRuleResponseruleactionshttpTypeDef",
    "ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef",
    "ClientGetTopicRuleResponseruleactionsiotEventsTypeDef",
    "ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    "ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    "ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    "ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef",
    "ClientGetTopicRuleResponseruleactionsiotSiteWiseTypeDef",
    "ClientGetTopicRuleResponseruleactionskinesisTypeDef",
    "ClientGetTopicRuleResponseruleactionslambdaTypeDef",
    "ClientGetTopicRuleResponseruleactionsrepublishTypeDef",
    "ClientGetTopicRuleResponseruleactionss3TypeDef",
    "ClientGetTopicRuleResponseruleactionssalesforceTypeDef",
    "ClientGetTopicRuleResponseruleactionssnsTypeDef",
    "ClientGetTopicRuleResponseruleactionssqsTypeDef",
    "ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef",
    "ClientGetTopicRuleResponseruleactionsTypeDef",
    "ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef",
    "ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef",
    "ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef",
    "ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef",
    "ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef",
    "ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef",
    "ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef",
    "ClientGetTopicRuleResponseruleerrorActionhttpauthsigv4TypeDef",
    "ClientGetTopicRuleResponseruleerrorActionhttpauthTypeDef",
    "ClientGetTopicRuleResponseruleerrorActionhttpheadersTypeDef",
    "ClientGetTopicRuleResponseruleerrorActionhttpTypeDef",
    "ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef",
    "ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef",
    "ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    "ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    "ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    "ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef",
    "ClientGetTopicRuleResponseruleerrorActioniotSiteWiseTypeDef",
    "ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef",
    "ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef",
    "ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef",
    "ClientGetTopicRuleResponseruleerrorActions3TypeDef",
    "ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef",
    "ClientGetTopicRuleResponseruleerrorActionsnsTypeDef",
    "ClientGetTopicRuleResponseruleerrorActionsqsTypeDef",
    "ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef",
    "ClientGetTopicRuleResponseruleerrorActionTypeDef",
    "ClientGetTopicRuleResponseruleTypeDef",
    "ClientGetTopicRuleResponseTypeDef",
    "ClientGetV2LoggingOptionsResponseTypeDef",
    "ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef",
    "ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef",
    "ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef",
    "ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef",
    "ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef",
    "ClientListActiveViolationsResponseactiveViolationsTypeDef",
    "ClientListActiveViolationsResponseTypeDef",
    "ClientListAttachedPoliciesResponsepoliciesTypeDef",
    "ClientListAttachedPoliciesResponseTypeDef",
    "ClientListAuditFindingsResourceIdentifierpolicyVersionIdentifierTypeDef",
    "ClientListAuditFindingsResourceIdentifierTypeDef",
    "ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef",
    "ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef",
    "ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef",
    "ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef",
    "ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef",
    "ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef",
    "ClientListAuditFindingsResponsefindingsTypeDef",
    "ClientListAuditFindingsResponseTypeDef",
    "ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef",
    "ClientListAuditMitigationActionsExecutionsResponseTypeDef",
    "ClientListAuditMitigationActionsTasksResponsetasksTypeDef",
    "ClientListAuditMitigationActionsTasksResponseTypeDef",
    "ClientListAuditTasksResponsetasksTypeDef",
    "ClientListAuditTasksResponseTypeDef",
    "ClientListAuthorizersResponseauthorizersTypeDef",
    "ClientListAuthorizersResponseTypeDef",
    "ClientListBillingGroupsResponsebillingGroupsTypeDef",
    "ClientListBillingGroupsResponseTypeDef",
    "ClientListCaCertificatesResponsecertificatesTypeDef",
    "ClientListCaCertificatesResponseTypeDef",
    "ClientListCertificatesByCaResponsecertificatesTypeDef",
    "ClientListCertificatesByCaResponseTypeDef",
    "ClientListCertificatesResponsecertificatesTypeDef",
    "ClientListCertificatesResponseTypeDef",
    "ClientListDomainConfigurationsResponsedomainConfigurationsTypeDef",
    "ClientListDomainConfigurationsResponseTypeDef",
    "ClientListIndicesResponseTypeDef",
    "ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef",
    "ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef",
    "ClientListJobExecutionsForJobResponseTypeDef",
    "ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef",
    "ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef",
    "ClientListJobExecutionsForThingResponseTypeDef",
    "ClientListJobsResponsejobsTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientListMitigationActionsResponseactionIdentifiersTypeDef",
    "ClientListMitigationActionsResponseTypeDef",
    "ClientListOtaUpdatesResponseotaUpdatesTypeDef",
    "ClientListOtaUpdatesResponseTypeDef",
    "ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef",
    "ClientListOutgoingCertificatesResponseTypeDef",
    "ClientListPoliciesResponsepoliciesTypeDef",
    "ClientListPoliciesResponseTypeDef",
    "ClientListPolicyPrincipalsResponseTypeDef",
    "ClientListPolicyVersionsResponsepolicyVersionsTypeDef",
    "ClientListPolicyVersionsResponseTypeDef",
    "ClientListPrincipalPoliciesResponsepoliciesTypeDef",
    "ClientListPrincipalPoliciesResponseTypeDef",
    "ClientListPrincipalThingsResponseTypeDef",
    "ClientListProvisioningTemplateVersionsResponseversionsTypeDef",
    "ClientListProvisioningTemplateVersionsResponseTypeDef",
    "ClientListProvisioningTemplatesResponsetemplatesTypeDef",
    "ClientListProvisioningTemplatesResponseTypeDef",
    "ClientListRoleAliasesResponseTypeDef",
    "ClientListScheduledAuditsResponsescheduledAuditsTypeDef",
    "ClientListScheduledAuditsResponseTypeDef",
    "ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef",
    "ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef",
    "ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef",
    "ClientListSecurityProfilesForTargetResponseTypeDef",
    "ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef",
    "ClientListSecurityProfilesResponseTypeDef",
    "ClientListStreamsResponsestreamsTypeDef",
    "ClientListStreamsResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTargetsForPolicyResponseTypeDef",
    "ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef",
    "ClientListTargetsForSecurityProfileResponseTypeDef",
    "ClientListThingGroupsForThingResponsethingGroupsTypeDef",
    "ClientListThingGroupsForThingResponseTypeDef",
    "ClientListThingGroupsResponsethingGroupsTypeDef",
    "ClientListThingGroupsResponseTypeDef",
    "ClientListThingPrincipalsResponseTypeDef",
    "ClientListThingRegistrationTaskReportsResponseTypeDef",
    "ClientListThingRegistrationTasksResponseTypeDef",
    "ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef",
    "ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef",
    "ClientListThingTypesResponsethingTypesTypeDef",
    "ClientListThingTypesResponseTypeDef",
    "ClientListThingsInBillingGroupResponseTypeDef",
    "ClientListThingsInThingGroupResponseTypeDef",
    "ClientListThingsResponsethingsTypeDef",
    "ClientListThingsResponseTypeDef",
    "ClientListTopicRuleDestinationsResponsedestinationSummarieshttpUrlSummaryTypeDef",
    "ClientListTopicRuleDestinationsResponsedestinationSummariesTypeDef",
    "ClientListTopicRuleDestinationsResponseTypeDef",
    "ClientListTopicRulesResponserulesTypeDef",
    "ClientListTopicRulesResponseTypeDef",
    "ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef",
    "ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef",
    "ClientListV2LoggingLevelsResponseTypeDef",
    "ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef",
    "ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef",
    "ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef",
    "ClientListViolationEventsResponseviolationEventsbehaviorTypeDef",
    "ClientListViolationEventsResponseviolationEventsmetricValueTypeDef",
    "ClientListViolationEventsResponseviolationEventsTypeDef",
    "ClientListViolationEventsResponseTypeDef",
    "ClientRegisterCaCertificateRegistrationConfigTypeDef",
    "ClientRegisterCaCertificateResponseTypeDef",
    "ClientRegisterCertificateResponseTypeDef",
    "ClientRegisterThingResponseTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionselasticsearchTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsfirehoseTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionshttpauthTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionshttpheadersTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionshttpTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotEventsTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionskinesisTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionslambdaTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsrepublishTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionss3TypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionssalesforceTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionssnsTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionssqsTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadactionsTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionkinesisTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionlambdaTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionrepublishTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActions3TypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionsnsTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionsqsTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionTypeDef",
    "ClientReplaceTopicRuleTopicRulePayloadTypeDef",
    "ClientSearchIndexResponsethingGroupsTypeDef",
    "ClientSearchIndexResponsethingsconnectivityTypeDef",
    "ClientSearchIndexResponsethingsTypeDef",
    "ClientSearchIndexResponseTypeDef",
    "ClientSetDefaultAuthorizerResponseTypeDef",
    "ClientSetLoggingOptionsLoggingOptionsPayloadTypeDef",
    "ClientSetV2LoggingLevelLogTargetTypeDef",
    "ClientStartAuditMitigationActionsTaskResponseTypeDef",
    "ClientStartAuditMitigationActionsTaskTargetTypeDef",
    "ClientStartOnDemandAuditTaskResponseTypeDef",
    "ClientStartThingRegistrationTaskResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientTestAuthorizationAuthInfosTypeDef",
    "ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef",
    "ClientTestAuthorizationResponseauthResultsallowedTypeDef",
    "ClientTestAuthorizationResponseauthResultsauthInfoTypeDef",
    "ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef",
    "ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef",
    "ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef",
    "ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef",
    "ClientTestAuthorizationResponseauthResultsdeniedTypeDef",
    "ClientTestAuthorizationResponseauthResultsTypeDef",
    "ClientTestAuthorizationResponseTypeDef",
    "ClientTestInvokeAuthorizerHttpContextTypeDef",
    "ClientTestInvokeAuthorizerMqttContextTypeDef",
    "ClientTestInvokeAuthorizerResponseTypeDef",
    "ClientTestInvokeAuthorizerTlsContextTypeDef",
    "ClientTransferCertificateResponseTypeDef",
    "ClientUpdateAccountAuditConfigurationAuditCheckConfigurationsTypeDef",
    "ClientUpdateAccountAuditConfigurationAuditNotificationTargetConfigurationsTypeDef",
    "ClientUpdateAuthorizerResponseTypeDef",
    "ClientUpdateBillingGroupBillingGroupPropertiesTypeDef",
    "ClientUpdateBillingGroupResponseTypeDef",
    "ClientUpdateCaCertificateRegistrationConfigTypeDef",
    "ClientUpdateDomainConfigurationAuthorizerConfigTypeDef",
    "ClientUpdateDomainConfigurationResponseTypeDef",
    "ClientUpdateDynamicThingGroupResponseTypeDef",
    "ClientUpdateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef",
    "ClientUpdateDynamicThingGroupThingGroupPropertiesTypeDef",
    "ClientUpdateEventConfigurationsEventConfigurationsTypeDef",
    "ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationcustomFieldsTypeDef",
    "ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationmanagedFieldsTypeDef",
    "ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef",
    "ClientUpdateIndexingConfigurationThingIndexingConfigurationcustomFieldsTypeDef",
    "ClientUpdateIndexingConfigurationThingIndexingConfigurationmanagedFieldsTypeDef",
    "ClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef",
    "ClientUpdateJobAbortConfigcriteriaListTypeDef",
    "ClientUpdateJobAbortConfigTypeDef",
    "ClientUpdateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef",
    "ClientUpdateJobJobExecutionsRolloutConfigexponentialRateTypeDef",
    "ClientUpdateJobJobExecutionsRolloutConfigTypeDef",
    "ClientUpdateJobPresignedUrlConfigTypeDef",
    "ClientUpdateJobTimeoutConfigTypeDef",
    "ClientUpdateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef",
    "ClientUpdateMitigationActionActionParamsenableIoTLoggingParamsTypeDef",
    "ClientUpdateMitigationActionActionParamspublishFindingToSnsParamsTypeDef",
    "ClientUpdateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    "ClientUpdateMitigationActionActionParamsupdateCACertificateParamsTypeDef",
    "ClientUpdateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef",
    "ClientUpdateMitigationActionActionParamsTypeDef",
    "ClientUpdateMitigationActionResponseTypeDef",
    "ClientUpdateRoleAliasResponseTypeDef",
    "ClientUpdateScheduledAuditResponseTypeDef",
    "ClientUpdateSecurityProfileAlertTargetsTypeDef",
    "ClientUpdateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef",
    "ClientUpdateSecurityProfileBehaviorscriteriavalueTypeDef",
    "ClientUpdateSecurityProfileBehaviorscriteriaTypeDef",
    "ClientUpdateSecurityProfileBehaviorsTypeDef",
    "ClientUpdateSecurityProfileResponsealertTargetsTypeDef",
    "ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef",
    "ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef",
    "ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef",
    "ClientUpdateSecurityProfileResponsebehaviorsTypeDef",
    "ClientUpdateSecurityProfileResponseTypeDef",
    "ClientUpdateStreamFiless3LocationTypeDef",
    "ClientUpdateStreamFilesTypeDef",
    "ClientUpdateStreamResponseTypeDef",
    "ClientUpdateThingAttributePayloadTypeDef",
    "ClientUpdateThingGroupResponseTypeDef",
    "ClientUpdateThingGroupThingGroupPropertiesattributePayloadTypeDef",
    "ClientUpdateThingGroupThingGroupPropertiesTypeDef",
    "ClientValidateSecurityProfileBehaviorsBehaviorscriteriastatisticalThresholdTypeDef",
    "ClientValidateSecurityProfileBehaviorsBehaviorscriteriavalueTypeDef",
    "ClientValidateSecurityProfileBehaviorsBehaviorscriteriaTypeDef",
    "ClientValidateSecurityProfileBehaviorsBehaviorsTypeDef",
    "ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef",
    "ClientValidateSecurityProfileBehaviorsResponseTypeDef",
    "ListActiveViolationsPaginatePaginationConfigTypeDef",
    "ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef",
    "ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef",
    "ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef",
    "ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef",
    "ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef",
    "ListActiveViolationsPaginateResponseactiveViolationsTypeDef",
    "ListActiveViolationsPaginateResponseTypeDef",
    "ListAttachedPoliciesPaginatePaginationConfigTypeDef",
    "ListAttachedPoliciesPaginateResponsepoliciesTypeDef",
    "ListAttachedPoliciesPaginateResponseTypeDef",
    "ListAuditFindingsPaginatePaginationConfigTypeDef",
    "ListAuditFindingsPaginateResourceIdentifierpolicyVersionIdentifierTypeDef",
    "ListAuditFindingsPaginateResourceIdentifierTypeDef",
    "ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef",
    "ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef",
    "ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef",
    "ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef",
    "ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef",
    "ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef",
    "ListAuditFindingsPaginateResponsefindingsTypeDef",
    "ListAuditFindingsPaginateResponseTypeDef",
    "ListAuditTasksPaginatePaginationConfigTypeDef",
    "ListAuditTasksPaginateResponsetasksTypeDef",
    "ListAuditTasksPaginateResponseTypeDef",
    "ListAuthorizersPaginatePaginationConfigTypeDef",
    "ListAuthorizersPaginateResponseauthorizersTypeDef",
    "ListAuthorizersPaginateResponseTypeDef",
    "ListBillingGroupsPaginatePaginationConfigTypeDef",
    "ListBillingGroupsPaginateResponsebillingGroupsTypeDef",
    "ListBillingGroupsPaginateResponseTypeDef",
    "ListCACertificatesPaginatePaginationConfigTypeDef",
    "ListCACertificatesPaginateResponsecertificatesTypeDef",
    "ListCACertificatesPaginateResponseTypeDef",
    "ListCertificatesByCAPaginatePaginationConfigTypeDef",
    "ListCertificatesByCAPaginateResponsecertificatesTypeDef",
    "ListCertificatesByCAPaginateResponseTypeDef",
    "ListCertificatesPaginatePaginationConfigTypeDef",
    "ListCertificatesPaginateResponsecertificatesTypeDef",
    "ListCertificatesPaginateResponseTypeDef",
    "ListIndicesPaginatePaginationConfigTypeDef",
    "ListIndicesPaginateResponseTypeDef",
    "ListJobExecutionsForJobPaginatePaginationConfigTypeDef",
    "ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef",
    "ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef",
    "ListJobExecutionsForJobPaginateResponseTypeDef",
    "ListJobExecutionsForThingPaginatePaginationConfigTypeDef",
    "ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef",
    "ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef",
    "ListJobExecutionsForThingPaginateResponseTypeDef",
    "ListJobsPaginatePaginationConfigTypeDef",
    "ListJobsPaginateResponsejobsTypeDef",
    "ListJobsPaginateResponseTypeDef",
    "ListOTAUpdatesPaginatePaginationConfigTypeDef",
    "ListOTAUpdatesPaginateResponseotaUpdatesTypeDef",
    "ListOTAUpdatesPaginateResponseTypeDef",
    "ListOutgoingCertificatesPaginatePaginationConfigTypeDef",
    "ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef",
    "ListOutgoingCertificatesPaginateResponseTypeDef",
    "ListPoliciesPaginatePaginationConfigTypeDef",
    "ListPoliciesPaginateResponsepoliciesTypeDef",
    "ListPoliciesPaginateResponseTypeDef",
    "ListPolicyPrincipalsPaginatePaginationConfigTypeDef",
    "ListPolicyPrincipalsPaginateResponseTypeDef",
    "ListPrincipalPoliciesPaginatePaginationConfigTypeDef",
    "ListPrincipalPoliciesPaginateResponsepoliciesTypeDef",
    "ListPrincipalPoliciesPaginateResponseTypeDef",
    "ListPrincipalThingsPaginatePaginationConfigTypeDef",
    "ListPrincipalThingsPaginateResponseTypeDef",
    "ListRoleAliasesPaginatePaginationConfigTypeDef",
    "ListRoleAliasesPaginateResponseTypeDef",
    "ListScheduledAuditsPaginatePaginationConfigTypeDef",
    "ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef",
    "ListScheduledAuditsPaginateResponseTypeDef",
    "ListSecurityProfilesForTargetPaginatePaginationConfigTypeDef",
    "ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef",
    "ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef",
    "ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef",
    "ListSecurityProfilesForTargetPaginateResponseTypeDef",
    "ListSecurityProfilesPaginatePaginationConfigTypeDef",
    "ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef",
    "ListSecurityProfilesPaginateResponseTypeDef",
    "ListStreamsPaginatePaginationConfigTypeDef",
    "ListStreamsPaginateResponsestreamsTypeDef",
    "ListStreamsPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponsetagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "ListTargetsForPolicyPaginatePaginationConfigTypeDef",
    "ListTargetsForPolicyPaginateResponseTypeDef",
    "ListTargetsForSecurityProfilePaginatePaginationConfigTypeDef",
    "ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef",
    "ListTargetsForSecurityProfilePaginateResponseTypeDef",
    "ListThingGroupsForThingPaginatePaginationConfigTypeDef",
    "ListThingGroupsForThingPaginateResponsethingGroupsTypeDef",
    "ListThingGroupsForThingPaginateResponseTypeDef",
    "ListThingGroupsPaginatePaginationConfigTypeDef",
    "ListThingGroupsPaginateResponsethingGroupsTypeDef",
    "ListThingGroupsPaginateResponseTypeDef",
    "ListThingRegistrationTasksPaginatePaginationConfigTypeDef",
    "ListThingRegistrationTasksPaginateResponseTypeDef",
    "ListThingTypesPaginatePaginationConfigTypeDef",
    "ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef",
    "ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef",
    "ListThingTypesPaginateResponsethingTypesTypeDef",
    "ListThingTypesPaginateResponseTypeDef",
    "ListThingsInBillingGroupPaginatePaginationConfigTypeDef",
    "ListThingsInBillingGroupPaginateResponseTypeDef",
    "ListThingsInThingGroupPaginatePaginationConfigTypeDef",
    "ListThingsInThingGroupPaginateResponseTypeDef",
    "ListThingsPaginatePaginationConfigTypeDef",
    "ListThingsPaginateResponsethingsTypeDef",
    "ListThingsPaginateResponseTypeDef",
    "ListTopicRulesPaginatePaginationConfigTypeDef",
    "ListTopicRulesPaginateResponserulesTypeDef",
    "ListTopicRulesPaginateResponseTypeDef",
    "ListV2LoggingLevelsPaginatePaginationConfigTypeDef",
    "ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef",
    "ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef",
    "ListV2LoggingLevelsPaginateResponseTypeDef",
    "ListViolationEventsPaginatePaginationConfigTypeDef",
    "ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef",
    "ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef",
    "ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef",
    "ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef",
    "ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef",
    "ListViolationEventsPaginateResponseviolationEventsTypeDef",
    "ListViolationEventsPaginateResponseTypeDef",
)


_ClientAssociateTargetsWithJobResponseTypeDef = TypedDict(
    "_ClientAssociateTargetsWithJobResponseTypeDef",
    {"jobArn": str, "jobId": str, "description": str},
    total=False,
)


class ClientAssociateTargetsWithJobResponseTypeDef(_ClientAssociateTargetsWithJobResponseTypeDef):
    """
    - *(dict) --*

      - **jobArn** *(string) --*

        An ARN identifying the job.
    """


_ClientCancelJobResponseTypeDef = TypedDict(
    "_ClientCancelJobResponseTypeDef",
    {"jobArn": str, "jobId": str, "description": str},
    total=False,
)


class ClientCancelJobResponseTypeDef(_ClientCancelJobResponseTypeDef):
    """
    - *(dict) --*

      - **jobArn** *(string) --*

        The job ARN.
    """


_ClientCreateAuthorizerResponseTypeDef = TypedDict(
    "_ClientCreateAuthorizerResponseTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)


class ClientCreateAuthorizerResponseTypeDef(_ClientCreateAuthorizerResponseTypeDef):
    """
    - *(dict) --*

      - **authorizerName** *(string) --*

        The authorizer's name.
    """


_ClientCreateBillingGroupBillingGroupPropertiesTypeDef = TypedDict(
    "_ClientCreateBillingGroupBillingGroupPropertiesTypeDef",
    {"billingGroupDescription": str},
    total=False,
)


class ClientCreateBillingGroupBillingGroupPropertiesTypeDef(
    _ClientCreateBillingGroupBillingGroupPropertiesTypeDef
):
    """
    The properties of the billing group.
    - **billingGroupDescription** *(string) --*

      The description of the billing group.
    """


_ClientCreateBillingGroupResponseTypeDef = TypedDict(
    "_ClientCreateBillingGroupResponseTypeDef",
    {"billingGroupName": str, "billingGroupArn": str, "billingGroupId": str},
    total=False,
)


class ClientCreateBillingGroupResponseTypeDef(_ClientCreateBillingGroupResponseTypeDef):
    """
    - *(dict) --*

      - **billingGroupName** *(string) --*

        The name you gave to the billing group.
    """


_ClientCreateBillingGroupTagsTypeDef = TypedDict(
    "_ClientCreateBillingGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateBillingGroupTagsTypeDef(_ClientCreateBillingGroupTagsTypeDef):
    """
    - *(dict) --*

      A set of key/value pairs that are used to manage the resource.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientCreateCertificateFromCsrResponseTypeDef = TypedDict(
    "_ClientCreateCertificateFromCsrResponseTypeDef",
    {"certificateArn": str, "certificateId": str, "certificatePem": str},
    total=False,
)


class ClientCreateCertificateFromCsrResponseTypeDef(_ClientCreateCertificateFromCsrResponseTypeDef):
    """
    - *(dict) --*

      The output from the CreateCertificateFromCsr operation.
      - **certificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificate. You can use the ARN as a principal for
        policy operations.
    """


_ClientCreateDomainConfigurationAuthorizerConfigTypeDef = TypedDict(
    "_ClientCreateDomainConfigurationAuthorizerConfigTypeDef",
    {"defaultAuthorizerName": str, "allowAuthorizerOverride": bool},
    total=False,
)


class ClientCreateDomainConfigurationAuthorizerConfigTypeDef(
    _ClientCreateDomainConfigurationAuthorizerConfigTypeDef
):
    """
    An object that specifies the authorization service for a domain.
    - **defaultAuthorizerName** *(string) --*

      The name of the authorization service for a domain configuration.
    """


_ClientCreateDomainConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateDomainConfigurationResponseTypeDef",
    {"domainConfigurationName": str, "domainConfigurationArn": str},
    total=False,
)


class ClientCreateDomainConfigurationResponseTypeDef(
    _ClientCreateDomainConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **domainConfigurationName** *(string) --*

        The name of the domain configuration.
    """


_ClientCreateDynamicThingGroupResponseTypeDef = TypedDict(
    "_ClientCreateDynamicThingGroupResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingGroupId": str,
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
    },
    total=False,
)


class ClientCreateDynamicThingGroupResponseTypeDef(_ClientCreateDynamicThingGroupResponseTypeDef):
    """
    - *(dict) --*

      - **thingGroupName** *(string) --*

        The dynamic thing group name.
    """


_ClientCreateDynamicThingGroupTagsTypeDef = TypedDict(
    "_ClientCreateDynamicThingGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDynamicThingGroupTagsTypeDef(_ClientCreateDynamicThingGroupTagsTypeDef):
    """
    - *(dict) --*

      A set of key/value pairs that are used to manage the resource.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientCreateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "_ClientCreateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientCreateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef(
    _ClientCreateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef
):
    pass


_ClientCreateDynamicThingGroupThingGroupPropertiesTypeDef = TypedDict(
    "_ClientCreateDynamicThingGroupThingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientCreateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)


class ClientCreateDynamicThingGroupThingGroupPropertiesTypeDef(
    _ClientCreateDynamicThingGroupThingGroupPropertiesTypeDef
):
    """
    The dynamic thing group properties.
    - **thingGroupDescription** *(string) --*

      The thing group description.
    """


_RequiredClientCreateJobAbortConfigcriteriaListTypeDef = TypedDict(
    "_RequiredClientCreateJobAbortConfigcriteriaListTypeDef",
    {"failureType": Literal["FAILED", "REJECTED", "TIMED_OUT", "ALL"]},
)
_OptionalClientCreateJobAbortConfigcriteriaListTypeDef = TypedDict(
    "_OptionalClientCreateJobAbortConfigcriteriaListTypeDef",
    {"action": str, "thresholdPercentage": float, "minNumberOfExecutedThings": int},
    total=False,
)


class ClientCreateJobAbortConfigcriteriaListTypeDef(
    _RequiredClientCreateJobAbortConfigcriteriaListTypeDef,
    _OptionalClientCreateJobAbortConfigcriteriaListTypeDef,
):
    """
    - *(dict) --*

      Details of abort criteria to define rules to abort the job.
      - **failureType** *(string) --***[REQUIRED]**

        The type of job execution failure to define a rule to initiate a job abort.
    """


_ClientCreateJobAbortConfigTypeDef = TypedDict(
    "_ClientCreateJobAbortConfigTypeDef",
    {"criteriaList": List[ClientCreateJobAbortConfigcriteriaListTypeDef]},
)


class ClientCreateJobAbortConfigTypeDef(_ClientCreateJobAbortConfigTypeDef):
    """
    Allows you to create criteria to abort a job.
    - **criteriaList** *(list) --***[REQUIRED]**

      The list of abort criteria to define rules to abort the job.
      - *(dict) --*

        Details of abort criteria to define rules to abort the job.
        - **failureType** *(string) --***[REQUIRED]**

          The type of job execution failure to define a rule to initiate a job abort.
    """


_ClientCreateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef = TypedDict(
    "_ClientCreateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef",
    {"numberOfNotifiedThings": int, "numberOfSucceededThings": int},
    total=False,
)


class ClientCreateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef(
    _ClientCreateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef
):
    pass


_ClientCreateJobJobExecutionsRolloutConfigexponentialRateTypeDef = TypedDict(
    "_ClientCreateJobJobExecutionsRolloutConfigexponentialRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": ClientCreateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef,
    },
    total=False,
)


class ClientCreateJobJobExecutionsRolloutConfigexponentialRateTypeDef(
    _ClientCreateJobJobExecutionsRolloutConfigexponentialRateTypeDef
):
    pass


_ClientCreateJobJobExecutionsRolloutConfigTypeDef = TypedDict(
    "_ClientCreateJobJobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": ClientCreateJobJobExecutionsRolloutConfigexponentialRateTypeDef,
    },
    total=False,
)


class ClientCreateJobJobExecutionsRolloutConfigTypeDef(
    _ClientCreateJobJobExecutionsRolloutConfigTypeDef
):
    """
    Allows you to create a staged rollout of the job.
    - **maximumPerMinute** *(integer) --*

      The maximum number of things that will be notified of a pending job, per minute. This
      parameter allows you to create a staged rollout.
    """


_ClientCreateJobPresignedUrlConfigTypeDef = TypedDict(
    "_ClientCreateJobPresignedUrlConfigTypeDef", {"roleArn": str, "expiresInSec": int}, total=False
)


class ClientCreateJobPresignedUrlConfigTypeDef(_ClientCreateJobPresignedUrlConfigTypeDef):
    """
    Configuration information for pre-signed S3 URLs.
    - **roleArn** *(string) --*

      The ARN of an IAM role that grants grants permission to download files from the S3 bucket
      where the job data/updates are stored. The role must also grant permission for IoT to download
      the files.
    """


_ClientCreateJobResponseTypeDef = TypedDict(
    "_ClientCreateJobResponseTypeDef",
    {"jobArn": str, "jobId": str, "description": str},
    total=False,
)


class ClientCreateJobResponseTypeDef(_ClientCreateJobResponseTypeDef):
    """
    - *(dict) --*

      - **jobArn** *(string) --*

        The job ARN.
    """


_ClientCreateJobTagsTypeDef = TypedDict(
    "_ClientCreateJobTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateJobTagsTypeDef(_ClientCreateJobTagsTypeDef):
    """
    - *(dict) --*

      A set of key/value pairs that are used to manage the resource.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientCreateJobTimeoutConfigTypeDef = TypedDict(
    "_ClientCreateJobTimeoutConfigTypeDef", {"inProgressTimeoutInMinutes": int}, total=False
)


class ClientCreateJobTimeoutConfigTypeDef(_ClientCreateJobTimeoutConfigTypeDef):
    """
    Specifies the amount of time each device has to finish its execution of the job. The timer is
    started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is
    not set to another terminal state before the time expires, it will be automatically set to
    ``TIMED_OUT`` .
    - **inProgressTimeoutInMinutes** *(integer) --*

      Specifies the amount of time, in minutes, this device has to finish execution of this job. The
      timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in
      progress timer can't be updated and will apply to all job executions for the job. Whenever a
      job execution remains in the IN_PROGRESS status for longer than this interval, the job
      execution will fail and switch to the terminal ``TIMED_OUT`` status.
    """


_ClientCreateKeysAndCertificateResponsekeyPairTypeDef = TypedDict(
    "_ClientCreateKeysAndCertificateResponsekeyPairTypeDef",
    {"PublicKey": str, "PrivateKey": str},
    total=False,
)


class ClientCreateKeysAndCertificateResponsekeyPairTypeDef(
    _ClientCreateKeysAndCertificateResponsekeyPairTypeDef
):
    pass


_ClientCreateKeysAndCertificateResponseTypeDef = TypedDict(
    "_ClientCreateKeysAndCertificateResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "certificatePem": str,
        "keyPair": ClientCreateKeysAndCertificateResponsekeyPairTypeDef,
    },
    total=False,
)


class ClientCreateKeysAndCertificateResponseTypeDef(_ClientCreateKeysAndCertificateResponseTypeDef):
    """
    - *(dict) --*

      The output of the CreateKeysAndCertificate operation.
      - **certificateArn** *(string) --*

        The ARN of the certificate.
    """


_ClientCreateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "_ClientCreateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef",
    {"thingGroupNames": List[str], "overrideDynamicGroups": bool},
    total=False,
)


class ClientCreateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef(
    _ClientCreateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef
):
    pass


_ClientCreateMitigationActionActionParamsenableIoTLoggingParamsTypeDef = TypedDict(
    "_ClientCreateMitigationActionActionParamsenableIoTLoggingParamsTypeDef",
    {"roleArnForLogging": str, "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"]},
    total=False,
)


class ClientCreateMitigationActionActionParamsenableIoTLoggingParamsTypeDef(
    _ClientCreateMitigationActionActionParamsenableIoTLoggingParamsTypeDef
):
    pass


_ClientCreateMitigationActionActionParamspublishFindingToSnsParamsTypeDef = TypedDict(
    "_ClientCreateMitigationActionActionParamspublishFindingToSnsParamsTypeDef",
    {"topicArn": str},
    total=False,
)


class ClientCreateMitigationActionActionParamspublishFindingToSnsParamsTypeDef(
    _ClientCreateMitigationActionActionParamspublishFindingToSnsParamsTypeDef
):
    pass


_ClientCreateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "_ClientCreateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    {"templateName": str},
    total=False,
)


class ClientCreateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef(
    _ClientCreateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef
):
    pass


_ClientCreateMitigationActionActionParamsupdateCACertificateParamsTypeDef = TypedDict(
    "_ClientCreateMitigationActionActionParamsupdateCACertificateParamsTypeDef",
    {"action": str},
    total=False,
)


class ClientCreateMitigationActionActionParamsupdateCACertificateParamsTypeDef(
    _ClientCreateMitigationActionActionParamsupdateCACertificateParamsTypeDef
):
    pass


_ClientCreateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef = TypedDict(
    "_ClientCreateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef", {"action": str}
)


class ClientCreateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef(
    _ClientCreateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef
):
    """
    - **updateDeviceCertificateParams** *(dict) --*

      Parameters to define a mitigation action that changes the state of the device certificate to
      inactive.
      - **action** *(string) --***[REQUIRED]**

        The action that you want to apply to the device cerrtificate. The only supported value is
        ``DEACTIVATE`` .
    """


_ClientCreateMitigationActionActionParamsTypeDef = TypedDict(
    "_ClientCreateMitigationActionActionParamsTypeDef",
    {
        "updateDeviceCertificateParams": ClientCreateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef,
        "updateCACertificateParams": ClientCreateMitigationActionActionParamsupdateCACertificateParamsTypeDef,
        "addThingsToThingGroupParams": ClientCreateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef,
        "replaceDefaultPolicyVersionParams": ClientCreateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef,
        "enableIoTLoggingParams": ClientCreateMitigationActionActionParamsenableIoTLoggingParamsTypeDef,
        "publishFindingToSnsParams": ClientCreateMitigationActionActionParamspublishFindingToSnsParamsTypeDef,
    },
    total=False,
)


class ClientCreateMitigationActionActionParamsTypeDef(
    _ClientCreateMitigationActionActionParamsTypeDef
):
    """
    Defines the type of action and the parameters for that action.
    - **updateDeviceCertificateParams** *(dict) --*

      Parameters to define a mitigation action that changes the state of the device certificate to
      inactive.
      - **action** *(string) --***[REQUIRED]**

        The action that you want to apply to the device cerrtificate. The only supported value is
        ``DEACTIVATE`` .
    """


_ClientCreateMitigationActionResponseTypeDef = TypedDict(
    "_ClientCreateMitigationActionResponseTypeDef", {"actionArn": str, "actionId": str}, total=False
)


class ClientCreateMitigationActionResponseTypeDef(_ClientCreateMitigationActionResponseTypeDef):
    """
    - *(dict) --*

      - **actionArn** *(string) --*

        The ARN for the new mitigation action.
    """


_ClientCreateMitigationActionTagsTypeDef = TypedDict(
    "_ClientCreateMitigationActionTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateMitigationActionTagsTypeDef(_ClientCreateMitigationActionTagsTypeDef):
    """
    - *(dict) --*

      A set of key/value pairs that are used to manage the resource.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientCreateOtaUpdateAwsJobExecutionsRolloutConfigTypeDef = TypedDict(
    "_ClientCreateOtaUpdateAwsJobExecutionsRolloutConfigTypeDef",
    {"maximumPerMinute": int},
    total=False,
)


class ClientCreateOtaUpdateAwsJobExecutionsRolloutConfigTypeDef(
    _ClientCreateOtaUpdateAwsJobExecutionsRolloutConfigTypeDef
):
    """
    Configuration for the rollout of OTA updates.
    - **maximumPerMinute** *(integer) --*

      The maximum number of OTA update job executions started per minute.
    """


_ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef = TypedDict(
    "_ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef",
    {"certificateName": str, "inlineDocument": str},
    total=False,
)


class ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef(
    _ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef
):
    pass


_ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef = TypedDict(
    "_ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef",
    {"inlineDocument": bytes},
    total=False,
)


class ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef(
    _ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef
):
    pass


_ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningTypeDef = TypedDict(
    "_ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningTypeDef",
    {
        "signature": ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef,
        "certificateChain": ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef,
        "hashAlgorithm": str,
        "signatureAlgorithm": str,
    },
    total=False,
)


class ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningTypeDef(
    _ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningTypeDef
):
    pass


_ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef = TypedDict(
    "_ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef",
    {"bucket": str, "prefix": str},
    total=False,
)


class ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef(
    _ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef
):
    pass


_ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef = TypedDict(
    "_ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef",
    {
        "s3Destination": ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef
    },
    total=False,
)


class ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef(
    _ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef
):
    pass


_ClientCreateOtaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef = TypedDict(
    "_ClientCreateOtaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef",
    {"certificateArn": str, "platform": str, "certificatePathOnDevice": str},
    total=False,
)


class ClientCreateOtaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef(
    _ClientCreateOtaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef
):
    pass


_ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterTypeDef = TypedDict(
    "_ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterTypeDef",
    {
        "signingProfileParameter": ClientCreateOtaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef,
        "signingProfileName": str,
        "destination": ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef,
    },
    total=False,
)


class ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterTypeDef(
    _ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterTypeDef
):
    pass


_ClientCreateOtaUpdateFilescodeSigningTypeDef = TypedDict(
    "_ClientCreateOtaUpdateFilescodeSigningTypeDef",
    {
        "awsSignerJobId": str,
        "startSigningJobParameter": ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterTypeDef,
        "customCodeSigning": ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningTypeDef,
    },
    total=False,
)


class ClientCreateOtaUpdateFilescodeSigningTypeDef(_ClientCreateOtaUpdateFilescodeSigningTypeDef):
    pass


_ClientCreateOtaUpdateFilesfileLocations3LocationTypeDef = TypedDict(
    "_ClientCreateOtaUpdateFilesfileLocations3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)


class ClientCreateOtaUpdateFilesfileLocations3LocationTypeDef(
    _ClientCreateOtaUpdateFilesfileLocations3LocationTypeDef
):
    pass


_ClientCreateOtaUpdateFilesfileLocationstreamTypeDef = TypedDict(
    "_ClientCreateOtaUpdateFilesfileLocationstreamTypeDef",
    {"streamId": str, "fileId": int},
    total=False,
)


class ClientCreateOtaUpdateFilesfileLocationstreamTypeDef(
    _ClientCreateOtaUpdateFilesfileLocationstreamTypeDef
):
    pass


_ClientCreateOtaUpdateFilesfileLocationTypeDef = TypedDict(
    "_ClientCreateOtaUpdateFilesfileLocationTypeDef",
    {
        "stream": ClientCreateOtaUpdateFilesfileLocationstreamTypeDef,
        "s3Location": ClientCreateOtaUpdateFilesfileLocations3LocationTypeDef,
    },
    total=False,
)


class ClientCreateOtaUpdateFilesfileLocationTypeDef(_ClientCreateOtaUpdateFilesfileLocationTypeDef):
    pass


_ClientCreateOtaUpdateFilesTypeDef = TypedDict(
    "_ClientCreateOtaUpdateFilesTypeDef",
    {
        "fileName": str,
        "fileVersion": str,
        "fileLocation": ClientCreateOtaUpdateFilesfileLocationTypeDef,
        "codeSigning": ClientCreateOtaUpdateFilescodeSigningTypeDef,
        "attributes": Dict[str, str],
    },
    total=False,
)


class ClientCreateOtaUpdateFilesTypeDef(_ClientCreateOtaUpdateFilesTypeDef):
    """
    - *(dict) --*

      Describes a file to be associated with an OTA update.
      - **fileName** *(string) --*

        The name of the file.
    """


_ClientCreateOtaUpdateResponseTypeDef = TypedDict(
    "_ClientCreateOtaUpdateResponseTypeDef",
    {
        "otaUpdateId": str,
        "awsIotJobId": str,
        "otaUpdateArn": str,
        "awsIotJobArn": str,
        "otaUpdateStatus": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"
        ],
    },
    total=False,
)


class ClientCreateOtaUpdateResponseTypeDef(_ClientCreateOtaUpdateResponseTypeDef):
    """
    - *(dict) --*

      - **otaUpdateId** *(string) --*

        The OTA update ID.
    """


_ClientCreateOtaUpdateTagsTypeDef = TypedDict(
    "_ClientCreateOtaUpdateTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateOtaUpdateTagsTypeDef(_ClientCreateOtaUpdateTagsTypeDef):
    """
    - *(dict) --*

      A set of key/value pairs that are used to manage the resource.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientCreatePolicyResponseTypeDef = TypedDict(
    "_ClientCreatePolicyResponseTypeDef",
    {"policyName": str, "policyArn": str, "policyDocument": str, "policyVersionId": str},
    total=False,
)


class ClientCreatePolicyResponseTypeDef(_ClientCreatePolicyResponseTypeDef):
    """
    - *(dict) --*

      The output from the CreatePolicy operation.
      - **policyName** *(string) --*

        The policy name.
    """


_ClientCreatePolicyVersionResponseTypeDef = TypedDict(
    "_ClientCreatePolicyVersionResponseTypeDef",
    {"policyArn": str, "policyDocument": str, "policyVersionId": str, "isDefaultVersion": bool},
    total=False,
)


class ClientCreatePolicyVersionResponseTypeDef(_ClientCreatePolicyVersionResponseTypeDef):
    """
    - *(dict) --*

      The output of the CreatePolicyVersion operation.
      - **policyArn** *(string) --*

        The policy ARN.
    """


_ClientCreateProvisioningClaimResponsekeyPairTypeDef = TypedDict(
    "_ClientCreateProvisioningClaimResponsekeyPairTypeDef",
    {"PublicKey": str, "PrivateKey": str},
    total=False,
)


class ClientCreateProvisioningClaimResponsekeyPairTypeDef(
    _ClientCreateProvisioningClaimResponsekeyPairTypeDef
):
    pass


_ClientCreateProvisioningClaimResponseTypeDef = TypedDict(
    "_ClientCreateProvisioningClaimResponseTypeDef",
    {
        "certificateId": str,
        "certificatePem": str,
        "keyPair": ClientCreateProvisioningClaimResponsekeyPairTypeDef,
        "expiration": datetime,
    },
    total=False,
)


class ClientCreateProvisioningClaimResponseTypeDef(_ClientCreateProvisioningClaimResponseTypeDef):
    """
    - *(dict) --*

      - **certificateId** *(string) --*

        The ID of the certificate.
    """


_ClientCreateProvisioningTemplateResponseTypeDef = TypedDict(
    "_ClientCreateProvisioningTemplateResponseTypeDef",
    {"templateArn": str, "templateName": str, "defaultVersionId": int},
    total=False,
)


class ClientCreateProvisioningTemplateResponseTypeDef(
    _ClientCreateProvisioningTemplateResponseTypeDef
):
    """
    - *(dict) --*

      - **templateArn** *(string) --*

        The ARN that identifies the provisioning template.
    """


_ClientCreateProvisioningTemplateTagsTypeDef = TypedDict(
    "_ClientCreateProvisioningTemplateTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateProvisioningTemplateTagsTypeDef(_ClientCreateProvisioningTemplateTagsTypeDef):
    pass


_ClientCreateProvisioningTemplateVersionResponseTypeDef = TypedDict(
    "_ClientCreateProvisioningTemplateVersionResponseTypeDef",
    {"templateArn": str, "templateName": str, "versionId": int, "isDefaultVersion": bool},
    total=False,
)


class ClientCreateProvisioningTemplateVersionResponseTypeDef(
    _ClientCreateProvisioningTemplateVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **templateArn** *(string) --*

        The ARN that identifies the provisioning template.
    """


_ClientCreateRoleAliasResponseTypeDef = TypedDict(
    "_ClientCreateRoleAliasResponseTypeDef", {"roleAlias": str, "roleAliasArn": str}, total=False
)


class ClientCreateRoleAliasResponseTypeDef(_ClientCreateRoleAliasResponseTypeDef):
    """
    - *(dict) --*

      - **roleAlias** *(string) --*

        The role alias.
    """


_ClientCreateScheduledAuditResponseTypeDef = TypedDict(
    "_ClientCreateScheduledAuditResponseTypeDef", {"scheduledAuditArn": str}, total=False
)


class ClientCreateScheduledAuditResponseTypeDef(_ClientCreateScheduledAuditResponseTypeDef):
    """
    - *(dict) --*

      - **scheduledAuditArn** *(string) --*

        The ARN of the scheduled audit.
    """


_ClientCreateScheduledAuditTagsTypeDef = TypedDict(
    "_ClientCreateScheduledAuditTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateScheduledAuditTagsTypeDef(_ClientCreateScheduledAuditTagsTypeDef):
    """
    - *(dict) --*

      A set of key/value pairs that are used to manage the resource.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientCreateSecurityProfileAlertTargetsTypeDef = TypedDict(
    "_ClientCreateSecurityProfileAlertTargetsTypeDef",
    {"alertTargetArn": str, "roleArn": str},
    total=False,
)


class ClientCreateSecurityProfileAlertTargetsTypeDef(
    _ClientCreateSecurityProfileAlertTargetsTypeDef
):
    pass


_ClientCreateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientCreateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientCreateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef(
    _ClientCreateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef
):
    pass


_ClientCreateSecurityProfileBehaviorscriteriavalueTypeDef = TypedDict(
    "_ClientCreateSecurityProfileBehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientCreateSecurityProfileBehaviorscriteriavalueTypeDef(
    _ClientCreateSecurityProfileBehaviorscriteriavalueTypeDef
):
    pass


_ClientCreateSecurityProfileBehaviorscriteriaTypeDef = TypedDict(
    "_ClientCreateSecurityProfileBehaviorscriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientCreateSecurityProfileBehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientCreateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientCreateSecurityProfileBehaviorscriteriaTypeDef(
    _ClientCreateSecurityProfileBehaviorscriteriaTypeDef
):
    pass


_RequiredClientCreateSecurityProfileBehaviorsTypeDef = TypedDict(
    "_RequiredClientCreateSecurityProfileBehaviorsTypeDef", {"name": str}
)
_OptionalClientCreateSecurityProfileBehaviorsTypeDef = TypedDict(
    "_OptionalClientCreateSecurityProfileBehaviorsTypeDef",
    {"metric": str, "criteria": ClientCreateSecurityProfileBehaviorscriteriaTypeDef},
    total=False,
)


class ClientCreateSecurityProfileBehaviorsTypeDef(
    _RequiredClientCreateSecurityProfileBehaviorsTypeDef,
    _OptionalClientCreateSecurityProfileBehaviorsTypeDef,
):
    """
    - *(dict) --*

      A Device Defender security profile behavior.
      - **name** *(string) --***[REQUIRED]**

        The name you have given to the behavior.
    """


_ClientCreateSecurityProfileResponseTypeDef = TypedDict(
    "_ClientCreateSecurityProfileResponseTypeDef",
    {"securityProfileName": str, "securityProfileArn": str},
    total=False,
)


class ClientCreateSecurityProfileResponseTypeDef(_ClientCreateSecurityProfileResponseTypeDef):
    """
    - *(dict) --*

      - **securityProfileName** *(string) --*

        The name you gave to the security profile.
    """


_ClientCreateSecurityProfileTagsTypeDef = TypedDict(
    "_ClientCreateSecurityProfileTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateSecurityProfileTagsTypeDef(_ClientCreateSecurityProfileTagsTypeDef):
    """
    - *(dict) --*

      A set of key/value pairs that are used to manage the resource.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientCreateStreamFiless3LocationTypeDef = TypedDict(
    "_ClientCreateStreamFiless3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)


class ClientCreateStreamFiless3LocationTypeDef(_ClientCreateStreamFiless3LocationTypeDef):
    pass


_ClientCreateStreamFilesTypeDef = TypedDict(
    "_ClientCreateStreamFilesTypeDef",
    {"fileId": int, "s3Location": ClientCreateStreamFiless3LocationTypeDef},
    total=False,
)


class ClientCreateStreamFilesTypeDef(_ClientCreateStreamFilesTypeDef):
    """
    - *(dict) --*

      Represents a file to stream.
      - **fileId** *(integer) --*

        The file ID.
    """


_ClientCreateStreamResponseTypeDef = TypedDict(
    "_ClientCreateStreamResponseTypeDef",
    {"streamId": str, "streamArn": str, "description": str, "streamVersion": int},
    total=False,
)


class ClientCreateStreamResponseTypeDef(_ClientCreateStreamResponseTypeDef):
    """
    - *(dict) --*

      - **streamId** *(string) --*

        The stream ID.
    """


_ClientCreateStreamTagsTypeDef = TypedDict(
    "_ClientCreateStreamTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateStreamTagsTypeDef(_ClientCreateStreamTagsTypeDef):
    """
    - *(dict) --*

      A set of key/value pairs that are used to manage the resource.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientCreateThingAttributePayloadTypeDef = TypedDict(
    "_ClientCreateThingAttributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientCreateThingAttributePayloadTypeDef(_ClientCreateThingAttributePayloadTypeDef):
    """
    The attribute payload, which consists of up to three name/value pairs in a JSON document. For
    example:

      ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``
    """


_ClientCreateThingGroupResponseTypeDef = TypedDict(
    "_ClientCreateThingGroupResponseTypeDef",
    {"thingGroupName": str, "thingGroupArn": str, "thingGroupId": str},
    total=False,
)


class ClientCreateThingGroupResponseTypeDef(_ClientCreateThingGroupResponseTypeDef):
    """
    - *(dict) --*

      - **thingGroupName** *(string) --*

        The thing group name.
    """


_ClientCreateThingGroupTagsTypeDef = TypedDict(
    "_ClientCreateThingGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateThingGroupTagsTypeDef(_ClientCreateThingGroupTagsTypeDef):
    """
    - *(dict) --*

      A set of key/value pairs that are used to manage the resource.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientCreateThingGroupThingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "_ClientCreateThingGroupThingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientCreateThingGroupThingGroupPropertiesattributePayloadTypeDef(
    _ClientCreateThingGroupThingGroupPropertiesattributePayloadTypeDef
):
    pass


_ClientCreateThingGroupThingGroupPropertiesTypeDef = TypedDict(
    "_ClientCreateThingGroupThingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientCreateThingGroupThingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)


class ClientCreateThingGroupThingGroupPropertiesTypeDef(
    _ClientCreateThingGroupThingGroupPropertiesTypeDef
):
    """
    The thing group properties.
    - **thingGroupDescription** *(string) --*

      The thing group description.
    """


_ClientCreateThingResponseTypeDef = TypedDict(
    "_ClientCreateThingResponseTypeDef",
    {"thingName": str, "thingArn": str, "thingId": str},
    total=False,
)


class ClientCreateThingResponseTypeDef(_ClientCreateThingResponseTypeDef):
    """
    - *(dict) --*

      The output of the CreateThing operation.
      - **thingName** *(string) --*

        The name of the new thing.
    """


_ClientCreateThingTypeResponseTypeDef = TypedDict(
    "_ClientCreateThingTypeResponseTypeDef",
    {"thingTypeName": str, "thingTypeArn": str, "thingTypeId": str},
    total=False,
)


class ClientCreateThingTypeResponseTypeDef(_ClientCreateThingTypeResponseTypeDef):
    """
    - *(dict) --*

      The output of the CreateThingType operation.
      - **thingTypeName** *(string) --*

        The name of the thing type.
    """


_ClientCreateThingTypeTagsTypeDef = TypedDict(
    "_ClientCreateThingTypeTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateThingTypeTagsTypeDef(_ClientCreateThingTypeTagsTypeDef):
    """
    - *(dict) --*

      A set of key/value pairs that are used to manage the resource.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientCreateThingTypeThingTypePropertiesTypeDef = TypedDict(
    "_ClientCreateThingTypeThingTypePropertiesTypeDef",
    {"thingTypeDescription": str, "searchableAttributes": List[str]},
    total=False,
)


class ClientCreateThingTypeThingTypePropertiesTypeDef(
    _ClientCreateThingTypeThingTypePropertiesTypeDef
):
    """
    The ThingTypeProperties for the thing type to create. It contains information about the new
    thing type including a description, and a list of searchable thing attribute names.
    - **thingTypeDescription** *(string) --*

      The description of the thing type.
    """


_ClientCreateTopicRuleDestinationDestinationConfigurationhttpUrlConfigurationTypeDef = TypedDict(
    "_ClientCreateTopicRuleDestinationDestinationConfigurationhttpUrlConfigurationTypeDef",
    {"confirmationUrl": str},
)


class ClientCreateTopicRuleDestinationDestinationConfigurationhttpUrlConfigurationTypeDef(
    _ClientCreateTopicRuleDestinationDestinationConfigurationhttpUrlConfigurationTypeDef
):
    """
    - **httpUrlConfiguration** *(dict) --*

      Configuration of the HTTP URL.
      - **confirmationUrl** *(string) --***[REQUIRED]**

        The URL AWS IoT uses to confirm ownership of or access to the topic rule destination URL.
    """


_ClientCreateTopicRuleDestinationDestinationConfigurationTypeDef = TypedDict(
    "_ClientCreateTopicRuleDestinationDestinationConfigurationTypeDef",
    {
        "httpUrlConfiguration": ClientCreateTopicRuleDestinationDestinationConfigurationhttpUrlConfigurationTypeDef
    },
    total=False,
)


class ClientCreateTopicRuleDestinationDestinationConfigurationTypeDef(
    _ClientCreateTopicRuleDestinationDestinationConfigurationTypeDef
):
    """
    The topic rule destination configuration.
    - **httpUrlConfiguration** *(dict) --*

      Configuration of the HTTP URL.
      - **confirmationUrl** *(string) --***[REQUIRED]**

        The URL AWS IoT uses to confirm ownership of or access to the topic rule destination URL.
    """


_ClientCreateTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef = TypedDict(
    "_ClientCreateTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef",
    {"confirmationUrl": str},
    total=False,
)


class ClientCreateTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef(
    _ClientCreateTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef
):
    pass


_ClientCreateTopicRuleDestinationResponsetopicRuleDestinationTypeDef = TypedDict(
    "_ClientCreateTopicRuleDestinationResponsetopicRuleDestinationTypeDef",
    {
        "arn": str,
        "status": Literal["ENABLED", "IN_PROGRESS", "DISABLED", "ERROR"],
        "statusReason": str,
        "httpUrlProperties": ClientCreateTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef,
    },
    total=False,
)


class ClientCreateTopicRuleDestinationResponsetopicRuleDestinationTypeDef(
    _ClientCreateTopicRuleDestinationResponsetopicRuleDestinationTypeDef
):
    """
    - **topicRuleDestination** *(dict) --*

      The topic rule destination.
      - **arn** *(string) --*

        The topic rule destination URL.
    """


_ClientCreateTopicRuleDestinationResponseTypeDef = TypedDict(
    "_ClientCreateTopicRuleDestinationResponseTypeDef",
    {"topicRuleDestination": ClientCreateTopicRuleDestinationResponsetopicRuleDestinationTypeDef},
    total=False,
)


class ClientCreateTopicRuleDestinationResponseTypeDef(
    _ClientCreateTopicRuleDestinationResponseTypeDef
):
    """
    - *(dict) --*

      - **topicRuleDestination** *(dict) --*

        The topic rule destination.
        - **arn** *(string) --*

          The topic rule destination URL.
    """


_ClientCreateTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": Literal["STRING", "NUMBER"],
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": Literal["STRING", "NUMBER"],
        "payloadField": str,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef",
    {"tableName": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionselasticsearchTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionselasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionselasticsearchTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionselasticsearchTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsfirehoseTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsfirehoseTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsfirehoseTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef",
    {"signingRegion": str, "serviceName": str, "roleArn": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionshttpauthTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionshttpauthTypeDef",
    {"sigv4": ClientCreateTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionshttpauthTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionshttpauthTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionshttpheadersTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionshttpheadersTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionshttpheadersTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionshttpheadersTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionshttpTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionshttpTypeDef",
    {
        "url": str,
        "confirmationUrl": str,
        "headers": List[ClientCreateTopicRuleTopicRulePayloadactionshttpheadersTypeDef],
        "auth": ClientCreateTopicRuleTopicRulePayloadactionshttpauthTypeDef,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionshttpTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionshttpTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsiotEventsTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsiotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsiotEventsTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsiotEventsTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    {"timeInSeconds": str, "offsetInNanos": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    {"stringValue": str, "integerValue": str, "doubleValue": str, "booleanValue": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    {
        "value": ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef,
        "timestamp": ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef,
        "quality": str,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValues": List[
            ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
        ],
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef",
    {
        "putAssetPropertyValueEntries": List[
            ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef
        ],
        "roleArn": str,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionskinesisTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionskinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionskinesisTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionskinesisTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionslambdaTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionslambdaTypeDef", {"functionArn": str}, total=False
)


class ClientCreateTopicRuleTopicRulePayloadactionslambdaTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionslambdaTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsrepublishTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsrepublishTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsrepublishTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionss3TypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionss3TypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
        "cannedAcl": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "log-delivery-write",
        ],
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionss3TypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionss3TypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionssalesforceTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionssalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionssalesforceTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionssalesforceTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionssnsTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionssnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": Literal["RAW", "JSON"]},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionssnsTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionssnsTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionssqsTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionssqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionssqsTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionssqsTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloadactionsTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloadactionsTypeDef",
    {
        "dynamoDB": ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBTypeDef,
        "dynamoDBv2": ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef,
        "lambda": ClientCreateTopicRuleTopicRulePayloadactionslambdaTypeDef,
        "sns": ClientCreateTopicRuleTopicRulePayloadactionssnsTypeDef,
        "sqs": ClientCreateTopicRuleTopicRulePayloadactionssqsTypeDef,
        "kinesis": ClientCreateTopicRuleTopicRulePayloadactionskinesisTypeDef,
        "republish": ClientCreateTopicRuleTopicRulePayloadactionsrepublishTypeDef,
        "s3": ClientCreateTopicRuleTopicRulePayloadactionss3TypeDef,
        "firehose": ClientCreateTopicRuleTopicRulePayloadactionsfirehoseTypeDef,
        "cloudwatchMetric": ClientCreateTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientCreateTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef,
        "elasticsearch": ClientCreateTopicRuleTopicRulePayloadactionselasticsearchTypeDef,
        "salesforce": ClientCreateTopicRuleTopicRulePayloadactionssalesforceTypeDef,
        "iotAnalytics": ClientCreateTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef,
        "iotEvents": ClientCreateTopicRuleTopicRulePayloadactionsiotEventsTypeDef,
        "iotSiteWise": ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef,
        "stepFunctions": ClientCreateTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef,
        "http": ClientCreateTopicRuleTopicRulePayloadactionshttpTypeDef,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadactionsTypeDef(
    _ClientCreateTopicRuleTopicRulePayloadactionsTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": Literal["STRING", "NUMBER"],
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": Literal["STRING", "NUMBER"],
        "payloadField": str,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef",
    {"tableName": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef",
    {"signingRegion": str, "serviceName": str, "roleArn": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef",
    {"sigv4": ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionhttpTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionhttpTypeDef",
    {
        "url": str,
        "confirmationUrl": str,
        "headers": List[ClientCreateTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef],
        "auth": ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionhttpTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionhttpTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    {"timeInSeconds": str, "offsetInNanos": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    {"stringValue": str, "integerValue": str, "doubleValue": str, "booleanValue": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    {
        "value": ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef,
        "timestamp": ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef,
        "quality": str,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValues": List[
            ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
        ],
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef",
    {
        "putAssetPropertyValueEntries": List[
            ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef
        ],
        "roleArn": str,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionkinesisTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionkinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionkinesisTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionkinesisTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionlambdaTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionlambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionlambdaTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionlambdaTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionrepublishTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionrepublishTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionrepublishTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActions3TypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActions3TypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
        "cannedAcl": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "log-delivery-write",
        ],
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActions3TypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActions3TypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionsnsTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionsnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": Literal["RAW", "JSON"]},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionsnsTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionsnsTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionsqsTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionsqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionsqsTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionsqsTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef
):
    pass


_ClientCreateTopicRuleTopicRulePayloaderrorActionTypeDef = TypedDict(
    "_ClientCreateTopicRuleTopicRulePayloaderrorActionTypeDef",
    {
        "dynamoDB": ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef,
        "dynamoDBv2": ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef,
        "lambda": ClientCreateTopicRuleTopicRulePayloaderrorActionlambdaTypeDef,
        "sns": ClientCreateTopicRuleTopicRulePayloaderrorActionsnsTypeDef,
        "sqs": ClientCreateTopicRuleTopicRulePayloaderrorActionsqsTypeDef,
        "kinesis": ClientCreateTopicRuleTopicRulePayloaderrorActionkinesisTypeDef,
        "republish": ClientCreateTopicRuleTopicRulePayloaderrorActionrepublishTypeDef,
        "s3": ClientCreateTopicRuleTopicRulePayloaderrorActions3TypeDef,
        "firehose": ClientCreateTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef,
        "cloudwatchMetric": ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef,
        "elasticsearch": ClientCreateTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef,
        "salesforce": ClientCreateTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef,
        "iotAnalytics": ClientCreateTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef,
        "iotEvents": ClientCreateTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef,
        "iotSiteWise": ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef,
        "stepFunctions": ClientCreateTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef,
        "http": ClientCreateTopicRuleTopicRulePayloaderrorActionhttpTypeDef,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloaderrorActionTypeDef(
    _ClientCreateTopicRuleTopicRulePayloaderrorActionTypeDef
):
    pass


_RequiredClientCreateTopicRuleTopicRulePayloadTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuleTopicRulePayloadTypeDef", {"sql": str}
)
_OptionalClientCreateTopicRuleTopicRulePayloadTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuleTopicRulePayloadTypeDef",
    {
        "description": str,
        "actions": List[ClientCreateTopicRuleTopicRulePayloadactionsTypeDef],
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": ClientCreateTopicRuleTopicRulePayloaderrorActionTypeDef,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadTypeDef(
    _RequiredClientCreateTopicRuleTopicRulePayloadTypeDef,
    _OptionalClientCreateTopicRuleTopicRulePayloadTypeDef,
):
    """
    The rule payload.
    - **sql** *(string) --***[REQUIRED]**

      The SQL statement used to query the topic. For more information, see `AWS IoT SQL Reference
      <https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference>`__
      in the *AWS IoT Developer Guide* .
    """


_ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef = TypedDict(
    "_ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef",
    {"enabled": bool},
    total=False,
)


class ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef(
    _ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef
):
    pass


_ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef = TypedDict(
    "_ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef",
    {"targetArn": str, "roleArn": str, "enabled": bool},
    total=False,
)


class ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef(
    _ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef
):
    pass


_ClientDescribeAccountAuditConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeAccountAuditConfigurationResponseTypeDef",
    {
        "roleArn": str,
        "auditNotificationTargetConfigurations": Dict[
            str,
            ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef,
        ],
        "auditCheckConfigurations": Dict[
            str, ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAccountAuditConfigurationResponseTypeDef(
    _ClientDescribeAccountAuditConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **roleArn** *(string) --*

        The ARN of the role that grants permission to AWS IoT to access information about your
        devices, policies, certificates, and other items as required when performing an audit.
        On the first call to ``UpdateAccountAuditConfiguration`` , this parameter is required.
    """


_ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef
):
    pass


_ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)


class ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef(
    _ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef
):
    pass


_ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef",
    {
        "resourceType": Literal[
            "DEVICE_CERTIFICATE",
            "CA_CERTIFICATE",
            "IOT_POLICY",
            "COGNITO_IDENTITY_POOL",
            "CLIENT_ID",
            "ACCOUNT_SETTINGS",
            "ROLE_ALIAS",
            "IAM_ROLE",
        ],
        "resourceIdentifier": ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)


class ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef(
    _ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef
):
    pass


_ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef
):
    pass


_ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)


class ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef(
    _ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef
):
    pass


_ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef",
    {
        "resourceType": Literal[
            "DEVICE_CERTIFICATE",
            "CA_CERTIFICATE",
            "IOT_POLICY",
            "COGNITO_IDENTITY_POOL",
            "CLIENT_ID",
            "ACCOUNT_SETTINGS",
            "ROLE_ALIAS",
            "IAM_ROLE",
        ],
        "resourceIdentifier": ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)


class ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef(
    _ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef
):
    pass


_ClientDescribeAuditFindingResponsefindingTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingTypeDef",
    {
        "findingId": str,
        "taskId": str,
        "checkName": str,
        "taskStartTime": datetime,
        "findingTime": datetime,
        "severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"],
        "nonCompliantResource": ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef,
        "relatedResources": List[ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef],
        "reasonForNonCompliance": str,
        "reasonForNonComplianceCode": str,
    },
    total=False,
)


class ClientDescribeAuditFindingResponsefindingTypeDef(
    _ClientDescribeAuditFindingResponsefindingTypeDef
):
    """
    - **finding** *(dict) --*

      The findings (results) of the audit.
      - **findingId** *(string) --*

        A unique identifier for this set of audit findings. This identifier is used to apply
        mitigation tasks to one or more sets of findings.
    """


_ClientDescribeAuditFindingResponseTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponseTypeDef",
    {"finding": ClientDescribeAuditFindingResponsefindingTypeDef},
    total=False,
)


class ClientDescribeAuditFindingResponseTypeDef(_ClientDescribeAuditFindingResponseTypeDef):
    """
    - *(dict) --*

      - **finding** *(dict) --*

        The findings (results) of the audit.
        - **findingId** *(string) --*

          A unique identifier for this set of audit findings. This identifier is used to apply
          mitigation tasks to one or more sets of findings.
    """


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef",
    {"thingGroupNames": List[str], "overrideDynamicGroups": bool},
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef
):
    pass


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef",
    {"roleArnForLogging": str, "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"]},
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef
):
    pass


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef",
    {"topicArn": str},
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef
):
    pass


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    {"templateName": str},
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef
):
    pass


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef",
    {"action": str},
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef
):
    pass


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef",
    {"action": str},
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef
):
    pass


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef",
    {
        "updateDeviceCertificateParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef,
        "updateCACertificateParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef,
        "addThingsToThingGroupParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef,
        "replaceDefaultPolicyVersionParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef,
        "enableIoTLoggingParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef,
        "publishFindingToSnsParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef,
    },
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef
):
    pass


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef",
    {
        "name": str,
        "id": str,
        "roleArn": str,
        "actionParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef,
    },
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef
):
    pass


_ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef",
    {
        "auditTaskId": str,
        "findingIds": List[str],
        "auditCheckToReasonCodeFilter": Dict[str, List[str]],
    },
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef
):
    pass


_ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef",
    {
        "totalFindingsCount": int,
        "failedFindingsCount": int,
        "succeededFindingsCount": int,
        "skippedFindingsCount": int,
        "canceledFindingsCount": int,
    },
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef
):
    pass


_ClientDescribeAuditMitigationActionsTaskResponseTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseTypeDef",
    {
        "taskStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"],
        "startTime": datetime,
        "endTime": datetime,
        "taskStatistics": Dict[
            str, ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef
        ],
        "target": ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef,
        "auditCheckToActionsMapping": Dict[str, List[str]],
        "actionsDefinition": List[
            ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseTypeDef
):
    """
    - *(dict) --*

      - **taskStatus** *(string) --*

        The current status of the task.
    """


_ClientDescribeAuditTaskResponseauditDetailsTypeDef = TypedDict(
    "_ClientDescribeAuditTaskResponseauditDetailsTypeDef",
    {
        "checkRunStatus": Literal[
            "IN_PROGRESS",
            "WAITING_FOR_DATA_COLLECTION",
            "CANCELED",
            "COMPLETED_COMPLIANT",
            "COMPLETED_NON_COMPLIANT",
            "FAILED",
        ],
        "checkCompliant": bool,
        "totalResourcesCount": int,
        "nonCompliantResourcesCount": int,
        "errorCode": str,
        "message": str,
    },
    total=False,
)


class ClientDescribeAuditTaskResponseauditDetailsTypeDef(
    _ClientDescribeAuditTaskResponseauditDetailsTypeDef
):
    pass


_ClientDescribeAuditTaskResponsetaskStatisticsTypeDef = TypedDict(
    "_ClientDescribeAuditTaskResponsetaskStatisticsTypeDef",
    {
        "totalChecks": int,
        "inProgressChecks": int,
        "waitingForDataCollectionChecks": int,
        "compliantChecks": int,
        "nonCompliantChecks": int,
        "failedChecks": int,
        "canceledChecks": int,
    },
    total=False,
)


class ClientDescribeAuditTaskResponsetaskStatisticsTypeDef(
    _ClientDescribeAuditTaskResponsetaskStatisticsTypeDef
):
    pass


_ClientDescribeAuditTaskResponseTypeDef = TypedDict(
    "_ClientDescribeAuditTaskResponseTypeDef",
    {
        "taskStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"],
        "taskType": Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"],
        "taskStartTime": datetime,
        "taskStatistics": ClientDescribeAuditTaskResponsetaskStatisticsTypeDef,
        "scheduledAuditName": str,
        "auditDetails": Dict[str, ClientDescribeAuditTaskResponseauditDetailsTypeDef],
    },
    total=False,
)


class ClientDescribeAuditTaskResponseTypeDef(_ClientDescribeAuditTaskResponseTypeDef):
    """
    - *(dict) --*

      - **taskStatus** *(string) --*

        The status of the audit: one of "IN_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".
    """


_ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef = TypedDict(
    "_ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "authorizerFunctionArn": str,
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Dict[str, str],
        "status": Literal["ACTIVE", "INACTIVE"],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "signingDisabled": bool,
    },
    total=False,
)


class ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef(
    _ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef
):
    """
    - **authorizerDescription** *(dict) --*

      The authorizer description.
      - **authorizerName** *(string) --*

        The authorizer name.
    """


_ClientDescribeAuthorizerResponseTypeDef = TypedDict(
    "_ClientDescribeAuthorizerResponseTypeDef",
    {"authorizerDescription": ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef},
    total=False,
)


class ClientDescribeAuthorizerResponseTypeDef(_ClientDescribeAuthorizerResponseTypeDef):
    """
    - *(dict) --*

      - **authorizerDescription** *(dict) --*

        The authorizer description.
        - **authorizerName** *(string) --*

          The authorizer name.
    """


_ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef = TypedDict(
    "_ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef",
    {"creationDate": datetime},
    total=False,
)


class ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef(
    _ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef
):
    pass


_ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef = TypedDict(
    "_ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef",
    {"billingGroupDescription": str},
    total=False,
)


class ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef(
    _ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef
):
    pass


_ClientDescribeBillingGroupResponseTypeDef = TypedDict(
    "_ClientDescribeBillingGroupResponseTypeDef",
    {
        "billingGroupName": str,
        "billingGroupId": str,
        "billingGroupArn": str,
        "version": int,
        "billingGroupProperties": ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef,
        "billingGroupMetadata": ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef,
    },
    total=False,
)


class ClientDescribeBillingGroupResponseTypeDef(_ClientDescribeBillingGroupResponseTypeDef):
    """
    - *(dict) --*

      - **billingGroupName** *(string) --*

        The name of the billing group.
    """


_ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef = TypedDict(
    "_ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef",
    {"notBefore": datetime, "notAfter": datetime},
    total=False,
)


class ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef(
    _ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef
):
    pass


_ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef = TypedDict(
    "_ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal["ACTIVE", "INACTIVE"],
        "certificatePem": str,
        "ownedBy": str,
        "creationDate": datetime,
        "autoRegistrationStatus": Literal["ENABLE", "DISABLE"],
        "lastModifiedDate": datetime,
        "customerVersion": int,
        "generationId": str,
        "validity": ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef,
    },
    total=False,
)


class ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef(
    _ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef
):
    """
    - **certificateDescription** *(dict) --*

      The CA certificate description.
      - **certificateArn** *(string) --*

        The CA certificate ARN.
    """


_ClientDescribeCaCertificateResponseregistrationConfigTypeDef = TypedDict(
    "_ClientDescribeCaCertificateResponseregistrationConfigTypeDef",
    {"templateBody": str, "roleArn": str},
    total=False,
)


class ClientDescribeCaCertificateResponseregistrationConfigTypeDef(
    _ClientDescribeCaCertificateResponseregistrationConfigTypeDef
):
    pass


_ClientDescribeCaCertificateResponseTypeDef = TypedDict(
    "_ClientDescribeCaCertificateResponseTypeDef",
    {
        "certificateDescription": ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef,
        "registrationConfig": ClientDescribeCaCertificateResponseregistrationConfigTypeDef,
    },
    total=False,
)


class ClientDescribeCaCertificateResponseTypeDef(_ClientDescribeCaCertificateResponseTypeDef):
    """
    - *(dict) --*

      The output from the DescribeCACertificate operation.
      - **certificateDescription** *(dict) --*

        The CA certificate description.
        - **certificateArn** *(string) --*

          The CA certificate ARN.
    """


_ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef = TypedDict(
    "_ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef",
    {
        "transferMessage": str,
        "rejectReason": str,
        "transferDate": datetime,
        "acceptDate": datetime,
        "rejectDate": datetime,
    },
    total=False,
)


class ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef(
    _ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef
):
    pass


_ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef = TypedDict(
    "_ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef",
    {"notBefore": datetime, "notAfter": datetime},
    total=False,
)


class ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef(
    _ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef
):
    pass


_ClientDescribeCertificateResponsecertificateDescriptionTypeDef = TypedDict(
    "_ClientDescribeCertificateResponsecertificateDescriptionTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "caCertificateId": str,
        "status": Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ],
        "certificatePem": str,
        "ownedBy": str,
        "previousOwnedBy": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "customerVersion": int,
        "transferData": ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef,
        "generationId": str,
        "validity": ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef,
    },
    total=False,
)


class ClientDescribeCertificateResponsecertificateDescriptionTypeDef(
    _ClientDescribeCertificateResponsecertificateDescriptionTypeDef
):
    """
    - **certificateDescription** *(dict) --*

      The description of the certificate.
      - **certificateArn** *(string) --*

        The ARN of the certificate.
    """


_ClientDescribeCertificateResponseTypeDef = TypedDict(
    "_ClientDescribeCertificateResponseTypeDef",
    {"certificateDescription": ClientDescribeCertificateResponsecertificateDescriptionTypeDef},
    total=False,
)


class ClientDescribeCertificateResponseTypeDef(_ClientDescribeCertificateResponseTypeDef):
    """
    - *(dict) --*

      The output of the DescribeCertificate operation.
      - **certificateDescription** *(dict) --*

        The description of the certificate.
        - **certificateArn** *(string) --*

          The ARN of the certificate.
    """


_ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef = TypedDict(
    "_ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "authorizerFunctionArn": str,
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Dict[str, str],
        "status": Literal["ACTIVE", "INACTIVE"],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "signingDisabled": bool,
    },
    total=False,
)


class ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef(
    _ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef
):
    """
    - **authorizerDescription** *(dict) --*

      The default authorizer's description.
      - **authorizerName** *(string) --*

        The authorizer name.
    """


_ClientDescribeDefaultAuthorizerResponseTypeDef = TypedDict(
    "_ClientDescribeDefaultAuthorizerResponseTypeDef",
    {"authorizerDescription": ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef},
    total=False,
)


class ClientDescribeDefaultAuthorizerResponseTypeDef(
    _ClientDescribeDefaultAuthorizerResponseTypeDef
):
    """
    - *(dict) --*

      - **authorizerDescription** *(dict) --*

        The default authorizer's description.
        - **authorizerName** *(string) --*

          The authorizer name.
    """


_ClientDescribeDomainConfigurationResponseauthorizerConfigTypeDef = TypedDict(
    "_ClientDescribeDomainConfigurationResponseauthorizerConfigTypeDef",
    {"defaultAuthorizerName": str, "allowAuthorizerOverride": bool},
    total=False,
)


class ClientDescribeDomainConfigurationResponseauthorizerConfigTypeDef(
    _ClientDescribeDomainConfigurationResponseauthorizerConfigTypeDef
):
    pass


_ClientDescribeDomainConfigurationResponseserverCertificatesTypeDef = TypedDict(
    "_ClientDescribeDomainConfigurationResponseserverCertificatesTypeDef",
    {
        "serverCertificateArn": str,
        "serverCertificateStatus": Literal["INVALID", "VALID"],
        "serverCertificateStatusDetail": str,
    },
    total=False,
)


class ClientDescribeDomainConfigurationResponseserverCertificatesTypeDef(
    _ClientDescribeDomainConfigurationResponseserverCertificatesTypeDef
):
    pass


_ClientDescribeDomainConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeDomainConfigurationResponseTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "domainName": str,
        "serverCertificates": List[
            ClientDescribeDomainConfigurationResponseserverCertificatesTypeDef
        ],
        "authorizerConfig": ClientDescribeDomainConfigurationResponseauthorizerConfigTypeDef,
        "domainConfigurationStatus": Literal["ENABLED", "DISABLED"],
        "serviceType": Literal["DATA", "CREDENTIAL_PROVIDER", "JOBS"],
        "domainType": Literal["ENDPOINT", "AWS_MANAGED", "CUSTOMER_MANAGED"],
    },
    total=False,
)


class ClientDescribeDomainConfigurationResponseTypeDef(
    _ClientDescribeDomainConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **domainConfigurationName** *(string) --*

        The name of the domain configuration.
    """


_ClientDescribeEndpointResponseTypeDef = TypedDict(
    "_ClientDescribeEndpointResponseTypeDef", {"endpointAddress": str}, total=False
)


class ClientDescribeEndpointResponseTypeDef(_ClientDescribeEndpointResponseTypeDef):
    """
    - *(dict) --*

      The output from the DescribeEndpoint operation.
      - **endpointAddress** *(string) --*

        The endpoint. The format of the endpoint is as follows: *identifier* .iot.*region*
        .amazonaws.com.
    """


_ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef = TypedDict(
    "_ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef(
    _ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef
):
    pass


_ClientDescribeEventConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeEventConfigurationsResponseTypeDef",
    {
        "eventConfigurations": Dict[
            str, ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef
        ],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeEventConfigurationsResponseTypeDef(
    _ClientDescribeEventConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **eventConfigurations** *(dict) --*

        The event configurations.
        - *(string) --*

          - *(dict) --*

            Configuration.
            - **Enabled** *(boolean) --*

              True to enable the configuration.
    """


_ClientDescribeIndexResponseTypeDef = TypedDict(
    "_ClientDescribeIndexResponseTypeDef",
    {"indexName": str, "indexStatus": Literal["ACTIVE", "BUILDING", "REBUILDING"], "schema": str},
    total=False,
)


class ClientDescribeIndexResponseTypeDef(_ClientDescribeIndexResponseTypeDef):
    """
    - *(dict) --*

      - **indexName** *(string) --*

        The index name.
    """


_ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef = TypedDict(
    "_ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef",
    {"detailsMap": Dict[str, str]},
    total=False,
)


class ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef(
    _ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef
):
    pass


_ClientDescribeJobExecutionResponseexecutionTypeDef = TypedDict(
    "_ClientDescribeJobExecutionResponseexecutionTypeDef",
    {
        "jobId": str,
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "forceCanceled": bool,
        "statusDetails": ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef,
        "thingArn": str,
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
        "versionNumber": int,
        "approximateSecondsBeforeTimedOut": int,
    },
    total=False,
)


class ClientDescribeJobExecutionResponseexecutionTypeDef(
    _ClientDescribeJobExecutionResponseexecutionTypeDef
):
    """
    - **execution** *(dict) --*

      Information about the job execution.
      - **jobId** *(string) --*

        The unique identifier you assigned to the job when it was created.
    """


_ClientDescribeJobExecutionResponseTypeDef = TypedDict(
    "_ClientDescribeJobExecutionResponseTypeDef",
    {"execution": ClientDescribeJobExecutionResponseexecutionTypeDef},
    total=False,
)


class ClientDescribeJobExecutionResponseTypeDef(_ClientDescribeJobExecutionResponseTypeDef):
    """
    - *(dict) --*

      - **execution** *(dict) --*

        Information about the job execution.
        - **jobId** *(string) --*

          The unique identifier you assigned to the job when it was created.
    """


_ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef",
    {
        "failureType": Literal["FAILED", "REJECTED", "TIMED_OUT", "ALL"],
        "action": str,
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
    total=False,
)


class ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef(
    _ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef
):
    pass


_ClientDescribeJobResponsejobabortConfigTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobabortConfigTypeDef",
    {"criteriaList": List[ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef]},
    total=False,
)


class ClientDescribeJobResponsejobabortConfigTypeDef(
    _ClientDescribeJobResponsejobabortConfigTypeDef
):
    pass


_ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef",
    {"numberOfNotifiedThings": int, "numberOfSucceededThings": int},
    total=False,
)


class ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef(
    _ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef
):
    pass


_ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef(
    _ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef
):
    pass


_ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef(
    _ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef
):
    pass


_ClientDescribeJobResponsejobjobProcessDetailsTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobjobProcessDetailsTypeDef",
    {
        "processingTargets": List[str],
        "numberOfCanceledThings": int,
        "numberOfSucceededThings": int,
        "numberOfFailedThings": int,
        "numberOfRejectedThings": int,
        "numberOfQueuedThings": int,
        "numberOfInProgressThings": int,
        "numberOfRemovedThings": int,
        "numberOfTimedOutThings": int,
    },
    total=False,
)


class ClientDescribeJobResponsejobjobProcessDetailsTypeDef(
    _ClientDescribeJobResponsejobjobProcessDetailsTypeDef
):
    pass


_ClientDescribeJobResponsejobpresignedUrlConfigTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobpresignedUrlConfigTypeDef",
    {"roleArn": str, "expiresInSec": int},
    total=False,
)


class ClientDescribeJobResponsejobpresignedUrlConfigTypeDef(
    _ClientDescribeJobResponsejobpresignedUrlConfigTypeDef
):
    pass


_ClientDescribeJobResponsejobtimeoutConfigTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobtimeoutConfigTypeDef",
    {"inProgressTimeoutInMinutes": int},
    total=False,
)


class ClientDescribeJobResponsejobtimeoutConfigTypeDef(
    _ClientDescribeJobResponsejobtimeoutConfigTypeDef
):
    pass


_ClientDescribeJobResponsejobTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "targetSelection": Literal["CONTINUOUS", "SNAPSHOT"],
        "status": Literal["IN_PROGRESS", "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS"],
        "forceCanceled": bool,
        "reasonCode": str,
        "comment": str,
        "targets": List[str],
        "description": str,
        "presignedUrlConfig": ClientDescribeJobResponsejobpresignedUrlConfigTypeDef,
        "jobExecutionsRolloutConfig": ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef,
        "abortConfig": ClientDescribeJobResponsejobabortConfigTypeDef,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
        "jobProcessDetails": ClientDescribeJobResponsejobjobProcessDetailsTypeDef,
        "timeoutConfig": ClientDescribeJobResponsejobtimeoutConfigTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponsejobTypeDef(_ClientDescribeJobResponsejobTypeDef):
    pass


_ClientDescribeJobResponseTypeDef = TypedDict(
    "_ClientDescribeJobResponseTypeDef",
    {"documentSource": str, "job": ClientDescribeJobResponsejobTypeDef},
    total=False,
)


class ClientDescribeJobResponseTypeDef(_ClientDescribeJobResponseTypeDef):
    """
    - *(dict) --*

      - **documentSource** *(string) --*

        An S3 link to the job document.
    """


_ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef",
    {"thingGroupNames": List[str], "overrideDynamicGroups": bool},
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef
):
    pass


_ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef",
    {"roleArnForLogging": str, "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"]},
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef
):
    pass


_ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef",
    {"topicArn": str},
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef
):
    pass


_ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    {"templateName": str},
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef
):
    pass


_ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef",
    {"action": str},
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef
):
    pass


_ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef",
    {"action": str},
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef
):
    pass


_ClientDescribeMitigationActionResponseactionParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamsTypeDef",
    {
        "updateDeviceCertificateParams": ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef,
        "updateCACertificateParams": ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef,
        "addThingsToThingGroupParams": ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef,
        "replaceDefaultPolicyVersionParams": ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef,
        "enableIoTLoggingParams": ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef,
        "publishFindingToSnsParams": ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef,
    },
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamsTypeDef
):
    pass


_ClientDescribeMitigationActionResponseTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseTypeDef",
    {
        "actionName": str,
        "actionType": Literal[
            "UPDATE_DEVICE_CERTIFICATE",
            "UPDATE_CA_CERTIFICATE",
            "ADD_THINGS_TO_THING_GROUP",
            "REPLACE_DEFAULT_POLICY_VERSION",
            "ENABLE_IOT_LOGGING",
            "PUBLISH_FINDING_TO_SNS",
        ],
        "actionArn": str,
        "actionId": str,
        "roleArn": str,
        "actionParams": ClientDescribeMitigationActionResponseactionParamsTypeDef,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeMitigationActionResponseTypeDef(_ClientDescribeMitigationActionResponseTypeDef):
    """
    - *(dict) --*

      - **actionName** *(string) --*

        The friendly name that uniquely identifies the mitigation action.
    """


_ClientDescribeProvisioningTemplateResponseTypeDef = TypedDict(
    "_ClientDescribeProvisioningTemplateResponseTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "description": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "defaultVersionId": int,
        "templateBody": str,
        "enabled": bool,
        "provisioningRoleArn": str,
    },
    total=False,
)


class ClientDescribeProvisioningTemplateResponseTypeDef(
    _ClientDescribeProvisioningTemplateResponseTypeDef
):
    """
    - *(dict) --*

      - **templateArn** *(string) --*

        The ARN of the fleet provisioning template.
    """


_ClientDescribeProvisioningTemplateVersionResponseTypeDef = TypedDict(
    "_ClientDescribeProvisioningTemplateVersionResponseTypeDef",
    {"versionId": int, "creationDate": datetime, "templateBody": str, "isDefaultVersion": bool},
    total=False,
)


class ClientDescribeProvisioningTemplateVersionResponseTypeDef(
    _ClientDescribeProvisioningTemplateVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **versionId** *(integer) --*

        The fleet provisioning template version ID.
    """


_ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef = TypedDict(
    "_ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef",
    {
        "roleAlias": str,
        "roleAliasArn": str,
        "roleArn": str,
        "owner": str,
        "credentialDurationSeconds": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef(
    _ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef
):
    """
    - **roleAliasDescription** *(dict) --*

      The role alias description.
      - **roleAlias** *(string) --*

        The role alias.
    """


_ClientDescribeRoleAliasResponseTypeDef = TypedDict(
    "_ClientDescribeRoleAliasResponseTypeDef",
    {"roleAliasDescription": ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef},
    total=False,
)


class ClientDescribeRoleAliasResponseTypeDef(_ClientDescribeRoleAliasResponseTypeDef):
    """
    - *(dict) --*

      - **roleAliasDescription** *(dict) --*

        The role alias description.
        - **roleAlias** *(string) --*

          The role alias.
    """


_ClientDescribeScheduledAuditResponseTypeDef = TypedDict(
    "_ClientDescribeScheduledAuditResponseTypeDef",
    {
        "frequency": Literal["DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY"],
        "dayOfMonth": str,
        "dayOfWeek": Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"],
        "targetCheckNames": List[str],
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
    },
    total=False,
)


class ClientDescribeScheduledAuditResponseTypeDef(_ClientDescribeScheduledAuditResponseTypeDef):
    """
    - *(dict) --*

      - **frequency** *(string) --*

        How often the scheduled audit takes place. One of "DAILY", "WEEKLY", "BIWEEKLY", or
        "MONTHLY". The start time of each audit is determined by the system.
    """


_ClientDescribeSecurityProfileResponsealertTargetsTypeDef = TypedDict(
    "_ClientDescribeSecurityProfileResponsealertTargetsTypeDef",
    {"alertTargetArn": str, "roleArn": str},
    total=False,
)


class ClientDescribeSecurityProfileResponsealertTargetsTypeDef(
    _ClientDescribeSecurityProfileResponsealertTargetsTypeDef
):
    pass


_ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef(
    _ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef
):
    pass


_ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef = TypedDict(
    "_ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef(
    _ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef
):
    pass


_ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef = TypedDict(
    "_ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef(
    _ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef
):
    pass


_ClientDescribeSecurityProfileResponsebehaviorsTypeDef = TypedDict(
    "_ClientDescribeSecurityProfileResponsebehaviorsTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef,
    },
    total=False,
)


class ClientDescribeSecurityProfileResponsebehaviorsTypeDef(
    _ClientDescribeSecurityProfileResponsebehaviorsTypeDef
):
    pass


_ClientDescribeSecurityProfileResponseTypeDef = TypedDict(
    "_ClientDescribeSecurityProfileResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "securityProfileDescription": str,
        "behaviors": List[ClientDescribeSecurityProfileResponsebehaviorsTypeDef],
        "alertTargets": Dict[str, ClientDescribeSecurityProfileResponsealertTargetsTypeDef],
        "additionalMetricsToRetain": List[str],
        "version": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeSecurityProfileResponseTypeDef(_ClientDescribeSecurityProfileResponseTypeDef):
    """
    - *(dict) --*

      - **securityProfileName** *(string) --*

        The name of the security profile.
    """


_ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef = TypedDict(
    "_ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)


class ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef(
    _ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef
):
    pass


_ClientDescribeStreamResponsestreamInfofilesTypeDef = TypedDict(
    "_ClientDescribeStreamResponsestreamInfofilesTypeDef",
    {"fileId": int, "s3Location": ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef},
    total=False,
)


class ClientDescribeStreamResponsestreamInfofilesTypeDef(
    _ClientDescribeStreamResponsestreamInfofilesTypeDef
):
    pass


_ClientDescribeStreamResponsestreamInfoTypeDef = TypedDict(
    "_ClientDescribeStreamResponsestreamInfoTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "streamVersion": int,
        "description": str,
        "files": List[ClientDescribeStreamResponsestreamInfofilesTypeDef],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "roleArn": str,
    },
    total=False,
)


class ClientDescribeStreamResponsestreamInfoTypeDef(_ClientDescribeStreamResponsestreamInfoTypeDef):
    """
    - **streamInfo** *(dict) --*

      Information about the stream.
      - **streamId** *(string) --*

        The stream ID.
    """


_ClientDescribeStreamResponseTypeDef = TypedDict(
    "_ClientDescribeStreamResponseTypeDef",
    {"streamInfo": ClientDescribeStreamResponsestreamInfoTypeDef},
    total=False,
)


class ClientDescribeStreamResponseTypeDef(_ClientDescribeStreamResponseTypeDef):
    """
    - *(dict) --*

      - **streamInfo** *(dict) --*

        Information about the stream.
        - **streamId** *(string) --*

          The stream ID.
    """


_ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef = TypedDict(
    "_ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef(
    _ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef
):
    pass


_ClientDescribeThingGroupResponsethingGroupMetadataTypeDef = TypedDict(
    "_ClientDescribeThingGroupResponsethingGroupMetadataTypeDef",
    {
        "parentGroupName": str,
        "rootToParentThingGroups": List[
            ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef
        ],
        "creationDate": datetime,
    },
    total=False,
)


class ClientDescribeThingGroupResponsethingGroupMetadataTypeDef(
    _ClientDescribeThingGroupResponsethingGroupMetadataTypeDef
):
    pass


_ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "_ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef(
    _ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef
):
    pass


_ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef = TypedDict(
    "_ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)


class ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef(
    _ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef
):
    pass


_ClientDescribeThingGroupResponseTypeDef = TypedDict(
    "_ClientDescribeThingGroupResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupId": str,
        "thingGroupArn": str,
        "version": int,
        "thingGroupProperties": ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef,
        "thingGroupMetadata": ClientDescribeThingGroupResponsethingGroupMetadataTypeDef,
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
        "status": Literal["ACTIVE", "BUILDING", "REBUILDING"],
    },
    total=False,
)


class ClientDescribeThingGroupResponseTypeDef(_ClientDescribeThingGroupResponseTypeDef):
    """
    - *(dict) --*

      - **thingGroupName** *(string) --*

        The name of the thing group.
    """


_ClientDescribeThingRegistrationTaskResponseTypeDef = TypedDict(
    "_ClientDescribeThingRegistrationTaskResponseTypeDef",
    {
        "taskId": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "templateBody": str,
        "inputFileBucket": str,
        "inputFileKey": str,
        "roleArn": str,
        "status": Literal["InProgress", "Completed", "Failed", "Cancelled", "Cancelling"],
        "message": str,
        "successCount": int,
        "failureCount": int,
        "percentageProgress": int,
    },
    total=False,
)


class ClientDescribeThingRegistrationTaskResponseTypeDef(
    _ClientDescribeThingRegistrationTaskResponseTypeDef
):
    """
    - *(dict) --*

      - **taskId** *(string) --*

        The task ID.
    """


_ClientDescribeThingResponseTypeDef = TypedDict(
    "_ClientDescribeThingResponseTypeDef",
    {
        "defaultClientId": str,
        "thingName": str,
        "thingId": str,
        "thingArn": str,
        "thingTypeName": str,
        "attributes": Dict[str, str],
        "version": int,
        "billingGroupName": str,
    },
    total=False,
)


class ClientDescribeThingResponseTypeDef(_ClientDescribeThingResponseTypeDef):
    """
    - *(dict) --*

      The output from the DescribeThing operation.
      - **defaultClientId** *(string) --*

        The default client ID.
    """


_ClientDescribeThingTypeResponsethingTypeMetadataTypeDef = TypedDict(
    "_ClientDescribeThingTypeResponsethingTypeMetadataTypeDef",
    {"deprecated": bool, "deprecationDate": datetime, "creationDate": datetime},
    total=False,
)


class ClientDescribeThingTypeResponsethingTypeMetadataTypeDef(
    _ClientDescribeThingTypeResponsethingTypeMetadataTypeDef
):
    pass


_ClientDescribeThingTypeResponsethingTypePropertiesTypeDef = TypedDict(
    "_ClientDescribeThingTypeResponsethingTypePropertiesTypeDef",
    {"thingTypeDescription": str, "searchableAttributes": List[str]},
    total=False,
)


class ClientDescribeThingTypeResponsethingTypePropertiesTypeDef(
    _ClientDescribeThingTypeResponsethingTypePropertiesTypeDef
):
    pass


_ClientDescribeThingTypeResponseTypeDef = TypedDict(
    "_ClientDescribeThingTypeResponseTypeDef",
    {
        "thingTypeName": str,
        "thingTypeId": str,
        "thingTypeArn": str,
        "thingTypeProperties": ClientDescribeThingTypeResponsethingTypePropertiesTypeDef,
        "thingTypeMetadata": ClientDescribeThingTypeResponsethingTypeMetadataTypeDef,
    },
    total=False,
)


class ClientDescribeThingTypeResponseTypeDef(_ClientDescribeThingTypeResponseTypeDef):
    """
    - *(dict) --*

      The output for the DescribeThingType operation.
      - **thingTypeName** *(string) --*

        The name of the thing type.
    """


_ClientGetCardinalityResponseTypeDef = TypedDict(
    "_ClientGetCardinalityResponseTypeDef", {"cardinality": int}, total=False
)


class ClientGetCardinalityResponseTypeDef(_ClientGetCardinalityResponseTypeDef):
    """
    - *(dict) --*

      - **cardinality** *(integer) --*

        The approximate count of unique values that match the query.
    """


_ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef = TypedDict(
    "_ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef",
    {"policyName": str, "policyArn": str, "policyDocument": str},
    total=False,
)


class ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef(
    _ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef
):
    """
    - *(dict) --*

      The policy that has the effect on the authorization results.
      - **policyName** *(string) --*

        The policy name.
    """


_ClientGetEffectivePoliciesResponseTypeDef = TypedDict(
    "_ClientGetEffectivePoliciesResponseTypeDef",
    {"effectivePolicies": List[ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef]},
    total=False,
)


class ClientGetEffectivePoliciesResponseTypeDef(_ClientGetEffectivePoliciesResponseTypeDef):
    """
    - *(dict) --*

      - **effectivePolicies** *(list) --*

        The effective policies.
        - *(dict) --*

          The policy that has the effect on the authorization results.
          - **policyName** *(string) --*

            The policy name.
    """


_ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)


class ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef(
    _ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef
):
    pass


_ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)


class ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef(
    _ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef
):
    pass


_ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef",
    {
        "thingGroupIndexingMode": Literal["OFF", "ON"],
        "managedFields": List[
            ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef
        ],
        "customFields": List[
            ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef
        ],
    },
    total=False,
)


class ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef(
    _ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef
):
    pass


_ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)


class ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef(
    _ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef
):
    pass


_ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)


class ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef(
    _ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef
):
    pass


_ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef",
    {
        "thingIndexingMode": Literal["OFF", "REGISTRY", "REGISTRY_AND_SHADOW"],
        "thingConnectivityIndexingMode": Literal["OFF", "STATUS"],
        "managedFields": List[
            ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef
        ],
        "customFields": List[
            ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef
        ],
    },
    total=False,
)


class ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef(
    _ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef
):
    """
    - **thingIndexingConfiguration** *(dict) --*

      Thing indexing configuration.
      - **thingIndexingMode** *(string) --*

        Thing indexing mode. Valid values are:
        * REGISTRY – Your thing index contains registry data only.
        * REGISTRY_AND_SHADOW - Your thing index contains registry and shadow data.
        * OFF - Thing indexing is disabled.
    """


_ClientGetIndexingConfigurationResponseTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponseTypeDef",
    {
        "thingIndexingConfiguration": ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef,
        "thingGroupIndexingConfiguration": ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef,
    },
    total=False,
)


class ClientGetIndexingConfigurationResponseTypeDef(_ClientGetIndexingConfigurationResponseTypeDef):
    """
    - *(dict) --*

      - **thingIndexingConfiguration** *(dict) --*

        Thing indexing configuration.
        - **thingIndexingMode** *(string) --*

          Thing indexing mode. Valid values are:
          * REGISTRY – Your thing index contains registry data only.
          * REGISTRY_AND_SHADOW - Your thing index contains registry and shadow data.
          * OFF - Thing indexing is disabled.
    """


_ClientGetJobDocumentResponseTypeDef = TypedDict(
    "_ClientGetJobDocumentResponseTypeDef", {"document": str}, total=False
)


class ClientGetJobDocumentResponseTypeDef(_ClientGetJobDocumentResponseTypeDef):
    """
    - *(dict) --*

      - **document** *(string) --*

        The job document content.
    """


_ClientGetLoggingOptionsResponseTypeDef = TypedDict(
    "_ClientGetLoggingOptionsResponseTypeDef",
    {"roleArn": str, "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"]},
    total=False,
)


class ClientGetLoggingOptionsResponseTypeDef(_ClientGetLoggingOptionsResponseTypeDef):
    """
    - *(dict) --*

      The output from the GetLoggingOptions operation.
      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access.
    """


_ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef",
    {"maximumPerMinute": int},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef",
    {"code": str, "message": str},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef",
    {"certificateName": str, "inlineDocument": str},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef",
    {"inlineDocument": bytes},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef",
    {
        "signature": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef,
        "certificateChain": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef,
        "hashAlgorithm": str,
        "signatureAlgorithm": str,
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef",
    {"bucket": str, "prefix": str},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef",
    {
        "s3Destination": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef",
    {"certificateArn": str, "platform": str, "certificatePathOnDevice": str},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef",
    {
        "signingProfileParameter": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef,
        "signingProfileName": str,
        "destination": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef,
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef",
    {
        "awsSignerJobId": str,
        "startSigningJobParameter": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef,
        "customCodeSigning": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef,
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef",
    {"streamId": str, "fileId": int},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef",
    {
        "stream": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef,
        "s3Location": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef,
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef",
    {
        "fileName": str,
        "fileVersion": str,
        "fileLocation": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef,
        "codeSigning": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef,
        "attributes": Dict[str, str],
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef
):
    pass


_ClientGetOtaUpdateResponseotaUpdateInfoTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfoTypeDef",
    {
        "otaUpdateId": str,
        "otaUpdateArn": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "description": str,
        "targets": List[str],
        "awsJobExecutionsRolloutConfig": ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef,
        "targetSelection": Literal["CONTINUOUS", "SNAPSHOT"],
        "otaUpdateFiles": List[ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef],
        "otaUpdateStatus": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"
        ],
        "awsIotJobId": str,
        "awsIotJobArn": str,
        "errorInfo": ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef,
        "additionalParameters": Dict[str, str],
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfoTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfoTypeDef
):
    """
    - **otaUpdateInfo** *(dict) --*

      The OTA update info.
      - **otaUpdateId** *(string) --*

        The OTA update ID.
    """


_ClientGetOtaUpdateResponseTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseTypeDef",
    {"otaUpdateInfo": ClientGetOtaUpdateResponseotaUpdateInfoTypeDef},
    total=False,
)


class ClientGetOtaUpdateResponseTypeDef(_ClientGetOtaUpdateResponseTypeDef):
    """
    - *(dict) --*

      - **otaUpdateInfo** *(dict) --*

        The OTA update info.
        - **otaUpdateId** *(string) --*

          The OTA update ID.
    """


_ClientGetPercentilesResponsepercentilesTypeDef = TypedDict(
    "_ClientGetPercentilesResponsepercentilesTypeDef",
    {"percent": float, "value": float},
    total=False,
)


class ClientGetPercentilesResponsepercentilesTypeDef(
    _ClientGetPercentilesResponsepercentilesTypeDef
):
    """
    - *(dict) --*

      Describes the percentile and percentile value.
      - **percent** *(float) --*

        The percentile.
    """


_ClientGetPercentilesResponseTypeDef = TypedDict(
    "_ClientGetPercentilesResponseTypeDef",
    {"percentiles": List[ClientGetPercentilesResponsepercentilesTypeDef]},
    total=False,
)


class ClientGetPercentilesResponseTypeDef(_ClientGetPercentilesResponseTypeDef):
    """
    - *(dict) --*

      - **percentiles** *(list) --*

        The percentile values of the aggregated fields.
        - *(dict) --*

          Describes the percentile and percentile value.
          - **percent** *(float) --*

            The percentile.
    """


_ClientGetPolicyResponseTypeDef = TypedDict(
    "_ClientGetPolicyResponseTypeDef",
    {
        "policyName": str,
        "policyArn": str,
        "policyDocument": str,
        "defaultVersionId": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "generationId": str,
    },
    total=False,
)


class ClientGetPolicyResponseTypeDef(_ClientGetPolicyResponseTypeDef):
    """
    - *(dict) --*

      The output from the GetPolicy operation.
      - **policyName** *(string) --*

        The policy name.
    """


_ClientGetPolicyVersionResponseTypeDef = TypedDict(
    "_ClientGetPolicyVersionResponseTypeDef",
    {
        "policyArn": str,
        "policyName": str,
        "policyDocument": str,
        "policyVersionId": str,
        "isDefaultVersion": bool,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "generationId": str,
    },
    total=False,
)


class ClientGetPolicyVersionResponseTypeDef(_ClientGetPolicyVersionResponseTypeDef):
    """
    - *(dict) --*

      The output from the GetPolicyVersion operation.
      - **policyArn** *(string) --*

        The policy ARN.
    """


_ClientGetRegistrationCodeResponseTypeDef = TypedDict(
    "_ClientGetRegistrationCodeResponseTypeDef", {"registrationCode": str}, total=False
)


class ClientGetRegistrationCodeResponseTypeDef(_ClientGetRegistrationCodeResponseTypeDef):
    """
    - *(dict) --*

      The output from the GetRegistrationCode operation.
      - **registrationCode** *(string) --*

        The CA certificate registration code.
    """


_ClientGetStatisticsResponsestatisticsTypeDef = TypedDict(
    "_ClientGetStatisticsResponsestatisticsTypeDef",
    {
        "count": int,
        "average": float,
        "sum": float,
        "minimum": float,
        "maximum": float,
        "sumOfSquares": float,
        "variance": float,
        "stdDeviation": float,
    },
    total=False,
)


class ClientGetStatisticsResponsestatisticsTypeDef(_ClientGetStatisticsResponsestatisticsTypeDef):
    """
    - **statistics** *(dict) --*

      The statistics returned by the Fleet Indexing service based on the query and aggregation
      field.
      - **count** *(integer) --*

        The count of things that match the query.
    """


_ClientGetStatisticsResponseTypeDef = TypedDict(
    "_ClientGetStatisticsResponseTypeDef",
    {"statistics": ClientGetStatisticsResponsestatisticsTypeDef},
    total=False,
)


class ClientGetStatisticsResponseTypeDef(_ClientGetStatisticsResponseTypeDef):
    """
    - *(dict) --*

      - **statistics** *(dict) --*

        The statistics returned by the Fleet Indexing service based on the query and aggregation
        field.
        - **count** *(integer) --*

          The count of things that match the query.
    """


_ClientGetTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef = TypedDict(
    "_ClientGetTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef",
    {"confirmationUrl": str},
    total=False,
)


class ClientGetTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef(
    _ClientGetTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef
):
    pass


_ClientGetTopicRuleDestinationResponsetopicRuleDestinationTypeDef = TypedDict(
    "_ClientGetTopicRuleDestinationResponsetopicRuleDestinationTypeDef",
    {
        "arn": str,
        "status": Literal["ENABLED", "IN_PROGRESS", "DISABLED", "ERROR"],
        "statusReason": str,
        "httpUrlProperties": ClientGetTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef,
    },
    total=False,
)


class ClientGetTopicRuleDestinationResponsetopicRuleDestinationTypeDef(
    _ClientGetTopicRuleDestinationResponsetopicRuleDestinationTypeDef
):
    """
    - **topicRuleDestination** *(dict) --*

      The topic rule destination.
      - **arn** *(string) --*

        The topic rule destination URL.
    """


_ClientGetTopicRuleDestinationResponseTypeDef = TypedDict(
    "_ClientGetTopicRuleDestinationResponseTypeDef",
    {"topicRuleDestination": ClientGetTopicRuleDestinationResponsetopicRuleDestinationTypeDef},
    total=False,
)


class ClientGetTopicRuleDestinationResponseTypeDef(_ClientGetTopicRuleDestinationResponseTypeDef):
    """
    - *(dict) --*

      - **topicRuleDestination** *(dict) --*

        The topic rule destination.
        - **arn** *(string) --*

          The topic rule destination URL.
    """


_ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef(
    _ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef(
    _ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": Literal["STRING", "NUMBER"],
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": Literal["STRING", "NUMBER"],
        "payloadField": str,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef(
    _ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef",
    {"tableName": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef(
    _ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef",
    {"roleArn": str, "putItem": ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef(
    _ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionselasticsearchTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionselasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionselasticsearchTypeDef(
    _ClientGetTopicRuleResponseruleactionselasticsearchTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsfirehoseTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsfirehoseTypeDef(
    _ClientGetTopicRuleResponseruleactionsfirehoseTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionshttpauthsigv4TypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionshttpauthsigv4TypeDef",
    {"signingRegion": str, "serviceName": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionshttpauthsigv4TypeDef(
    _ClientGetTopicRuleResponseruleactionshttpauthsigv4TypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionshttpauthTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionshttpauthTypeDef",
    {"sigv4": ClientGetTopicRuleResponseruleactionshttpauthsigv4TypeDef},
    total=False,
)


class ClientGetTopicRuleResponseruleactionshttpauthTypeDef(
    _ClientGetTopicRuleResponseruleactionshttpauthTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionshttpheadersTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionshttpheadersTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionshttpheadersTypeDef(
    _ClientGetTopicRuleResponseruleactionshttpheadersTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionshttpTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionshttpTypeDef",
    {
        "url": str,
        "confirmationUrl": str,
        "headers": List[ClientGetTopicRuleResponseruleactionshttpheadersTypeDef],
        "auth": ClientGetTopicRuleResponseruleactionshttpauthTypeDef,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleactionshttpTypeDef(
    _ClientGetTopicRuleResponseruleactionshttpTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef(
    _ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsiotEventsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsiotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsiotEventsTypeDef(
    _ClientGetTopicRuleResponseruleactionsiotEventsTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    {"timeInSeconds": str, "offsetInNanos": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef(
    _ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    {"stringValue": str, "integerValue": str, "doubleValue": str, "booleanValue": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef(
    _ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    {
        "value": ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef,
        "timestamp": ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef,
        "quality": str,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef(
    _ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValues": List[
            ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
        ],
    },
    total=False,
)


class ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef(
    _ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsiotSiteWiseTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsiotSiteWiseTypeDef",
    {
        "putAssetPropertyValueEntries": List[
            ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef
        ],
        "roleArn": str,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleactionsiotSiteWiseTypeDef(
    _ClientGetTopicRuleResponseruleactionsiotSiteWiseTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionskinesisTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionskinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionskinesisTypeDef(
    _ClientGetTopicRuleResponseruleactionskinesisTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionslambdaTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionslambdaTypeDef", {"functionArn": str}, total=False
)


class ClientGetTopicRuleResponseruleactionslambdaTypeDef(
    _ClientGetTopicRuleResponseruleactionslambdaTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsrepublishTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsrepublishTypeDef(
    _ClientGetTopicRuleResponseruleactionsrepublishTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionss3TypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionss3TypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
        "cannedAcl": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "log-delivery-write",
        ],
    },
    total=False,
)


class ClientGetTopicRuleResponseruleactionss3TypeDef(
    _ClientGetTopicRuleResponseruleactionss3TypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionssalesforceTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionssalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionssalesforceTypeDef(
    _ClientGetTopicRuleResponseruleactionssalesforceTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionssnsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionssnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": Literal["RAW", "JSON"]},
    total=False,
)


class ClientGetTopicRuleResponseruleactionssnsTypeDef(
    _ClientGetTopicRuleResponseruleactionssnsTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionssqsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionssqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientGetTopicRuleResponseruleactionssqsTypeDef(
    _ClientGetTopicRuleResponseruleactionssqsTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef(
    _ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef
):
    pass


_ClientGetTopicRuleResponseruleactionsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsTypeDef",
    {
        "dynamoDB": ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef,
        "dynamoDBv2": ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef,
        "lambda": ClientGetTopicRuleResponseruleactionslambdaTypeDef,
        "sns": ClientGetTopicRuleResponseruleactionssnsTypeDef,
        "sqs": ClientGetTopicRuleResponseruleactionssqsTypeDef,
        "kinesis": ClientGetTopicRuleResponseruleactionskinesisTypeDef,
        "republish": ClientGetTopicRuleResponseruleactionsrepublishTypeDef,
        "s3": ClientGetTopicRuleResponseruleactionss3TypeDef,
        "firehose": ClientGetTopicRuleResponseruleactionsfirehoseTypeDef,
        "cloudwatchMetric": ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef,
        "elasticsearch": ClientGetTopicRuleResponseruleactionselasticsearchTypeDef,
        "salesforce": ClientGetTopicRuleResponseruleactionssalesforceTypeDef,
        "iotAnalytics": ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef,
        "iotEvents": ClientGetTopicRuleResponseruleactionsiotEventsTypeDef,
        "iotSiteWise": ClientGetTopicRuleResponseruleactionsiotSiteWiseTypeDef,
        "stepFunctions": ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef,
        "http": ClientGetTopicRuleResponseruleactionshttpTypeDef,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleactionsTypeDef(_ClientGetTopicRuleResponseruleactionsTypeDef):
    pass


_ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef(
    _ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef(
    _ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": Literal["STRING", "NUMBER"],
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": Literal["STRING", "NUMBER"],
        "payloadField": str,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef(
    _ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef",
    {"tableName": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef(
    _ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef",
    {"roleArn": str, "putItem": ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef(
    _ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionhttpauthsigv4TypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionhttpauthsigv4TypeDef",
    {"signingRegion": str, "serviceName": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionhttpauthsigv4TypeDef(
    _ClientGetTopicRuleResponseruleerrorActionhttpauthsigv4TypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionhttpauthTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionhttpauthTypeDef",
    {"sigv4": ClientGetTopicRuleResponseruleerrorActionhttpauthsigv4TypeDef},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionhttpauthTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionhttpauthTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionhttpheadersTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionhttpheadersTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionhttpheadersTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionhttpheadersTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionhttpTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionhttpTypeDef",
    {
        "url": str,
        "confirmationUrl": str,
        "headers": List[ClientGetTopicRuleResponseruleerrorActionhttpheadersTypeDef],
        "auth": ClientGetTopicRuleResponseruleerrorActionhttpauthTypeDef,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionhttpTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionhttpTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef(
    _ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef(
    _ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    {"timeInSeconds": str, "offsetInNanos": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef(
    _ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    {"stringValue": str, "integerValue": str, "doubleValue": str, "booleanValue": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef(
    _ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    {
        "value": ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef,
        "timestamp": ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef,
        "quality": str,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef(
    _ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValues": List[
            ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
        ],
    },
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef(
    _ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActioniotSiteWiseTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActioniotSiteWiseTypeDef",
    {
        "putAssetPropertyValueEntries": List[
            ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef
        ],
        "roleArn": str,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActioniotSiteWiseTypeDef(
    _ClientGetTopicRuleResponseruleerrorActioniotSiteWiseTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef", {"functionArn": str}, total=False
)


class ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActions3TypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActions3TypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
        "cannedAcl": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "log-delivery-write",
        ],
    },
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActions3TypeDef(
    _ClientGetTopicRuleResponseruleerrorActions3TypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionsnsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionsnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": Literal["RAW", "JSON"]},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionsnsTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionsnsTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionsqsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionsqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionsqsTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionsqsTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef
):
    pass


_ClientGetTopicRuleResponseruleerrorActionTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionTypeDef",
    {
        "dynamoDB": ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef,
        "dynamoDBv2": ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef,
        "lambda": ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef,
        "sns": ClientGetTopicRuleResponseruleerrorActionsnsTypeDef,
        "sqs": ClientGetTopicRuleResponseruleerrorActionsqsTypeDef,
        "kinesis": ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef,
        "republish": ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef,
        "s3": ClientGetTopicRuleResponseruleerrorActions3TypeDef,
        "firehose": ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef,
        "cloudwatchMetric": ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef,
        "elasticsearch": ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef,
        "salesforce": ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef,
        "iotAnalytics": ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef,
        "iotEvents": ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef,
        "iotSiteWise": ClientGetTopicRuleResponseruleerrorActioniotSiteWiseTypeDef,
        "stepFunctions": ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef,
        "http": ClientGetTopicRuleResponseruleerrorActionhttpTypeDef,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionTypeDef
):
    pass


_ClientGetTopicRuleResponseruleTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleTypeDef",
    {
        "ruleName": str,
        "sql": str,
        "description": str,
        "createdAt": datetime,
        "actions": List[ClientGetTopicRuleResponseruleactionsTypeDef],
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": ClientGetTopicRuleResponseruleerrorActionTypeDef,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleTypeDef(_ClientGetTopicRuleResponseruleTypeDef):
    pass


_ClientGetTopicRuleResponseTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseTypeDef",
    {"ruleArn": str, "rule": ClientGetTopicRuleResponseruleTypeDef},
    total=False,
)


class ClientGetTopicRuleResponseTypeDef(_ClientGetTopicRuleResponseTypeDef):
    """
    - *(dict) --*

      The output from the GetTopicRule operation.
      - **ruleArn** *(string) --*

        The rule ARN.
    """


_ClientGetV2LoggingOptionsResponseTypeDef = TypedDict(
    "_ClientGetV2LoggingOptionsResponseTypeDef",
    {
        "roleArn": str,
        "defaultLogLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"],
        "disableAllLogs": bool,
    },
    total=False,
)


class ClientGetV2LoggingOptionsResponseTypeDef(_ClientGetV2LoggingOptionsResponseTypeDef):
    """
    - *(dict) --*

      - **roleArn** *(string) --*

        The IAM role ARN AWS IoT uses to write to your CloudWatch logs.
    """


_ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef(
    _ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef
):
    pass


_ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef(
    _ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef
):
    pass


_ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef(
    _ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef
):
    pass


_ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef,
    },
    total=False,
)


class ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef(
    _ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef
):
    pass


_ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef(
    _ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef
):
    pass


_ClientListActiveViolationsResponseactiveViolationsTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseactiveViolationsTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef,
        "lastViolationValue": ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef,
        "lastViolationTime": datetime,
        "violationStartTime": datetime,
    },
    total=False,
)


class ClientListActiveViolationsResponseactiveViolationsTypeDef(
    _ClientListActiveViolationsResponseactiveViolationsTypeDef
):
    """
    - *(dict) --*

      Information about an active Device Defender security profile behavior violation.
      - **violationId** *(string) --*

        The ID of the active violation.
    """


_ClientListActiveViolationsResponseTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseTypeDef",
    {
        "activeViolations": List[ClientListActiveViolationsResponseactiveViolationsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListActiveViolationsResponseTypeDef(_ClientListActiveViolationsResponseTypeDef):
    """
    - *(dict) --*

      - **activeViolations** *(list) --*

        The list of active violations.
        - *(dict) --*

          Information about an active Device Defender security profile behavior violation.
          - **violationId** *(string) --*

            The ID of the active violation.
    """


_ClientListAttachedPoliciesResponsepoliciesTypeDef = TypedDict(
    "_ClientListAttachedPoliciesResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ClientListAttachedPoliciesResponsepoliciesTypeDef(
    _ClientListAttachedPoliciesResponsepoliciesTypeDef
):
    """
    - *(dict) --*

      Describes an AWS IoT policy.
      - **policyName** *(string) --*

        The policy name.
    """


_ClientListAttachedPoliciesResponseTypeDef = TypedDict(
    "_ClientListAttachedPoliciesResponseTypeDef",
    {"policies": List[ClientListAttachedPoliciesResponsepoliciesTypeDef], "nextMarker": str},
    total=False,
)


class ClientListAttachedPoliciesResponseTypeDef(_ClientListAttachedPoliciesResponseTypeDef):
    """
    - *(dict) --*

      - **policies** *(list) --*

        The policies.
        - *(dict) --*

          Describes an AWS IoT policy.
          - **policyName** *(string) --*

            The policy name.
    """


_ClientListAuditFindingsResourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ClientListAuditFindingsResourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ClientListAuditFindingsResourceIdentifierpolicyVersionIdentifierTypeDef(
    _ClientListAuditFindingsResourceIdentifierpolicyVersionIdentifierTypeDef
):
    pass


_ClientListAuditFindingsResourceIdentifierTypeDef = TypedDict(
    "_ClientListAuditFindingsResourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientListAuditFindingsResourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)


class ClientListAuditFindingsResourceIdentifierTypeDef(
    _ClientListAuditFindingsResourceIdentifierTypeDef
):
    """
    Information identifying the noncompliant resource.
    - **deviceCertificateId** *(string) --*

      The ID of the certificate attached to the resource.
    """


_ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef
):
    pass


_ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)


class ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef(
    _ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef
):
    pass


_ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef",
    {
        "resourceType": Literal[
            "DEVICE_CERTIFICATE",
            "CA_CERTIFICATE",
            "IOT_POLICY",
            "COGNITO_IDENTITY_POOL",
            "CLIENT_ID",
            "ACCOUNT_SETTINGS",
            "ROLE_ALIAS",
            "IAM_ROLE",
        ],
        "resourceIdentifier": ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)


class ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef(
    _ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef
):
    pass


_ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef
):
    pass


_ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)


class ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef(
    _ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef
):
    pass


_ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef",
    {
        "resourceType": Literal[
            "DEVICE_CERTIFICATE",
            "CA_CERTIFICATE",
            "IOT_POLICY",
            "COGNITO_IDENTITY_POOL",
            "CLIENT_ID",
            "ACCOUNT_SETTINGS",
            "ROLE_ALIAS",
            "IAM_ROLE",
        ],
        "resourceIdentifier": ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)


class ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef(
    _ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef
):
    pass


_ClientListAuditFindingsResponsefindingsTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsTypeDef",
    {
        "findingId": str,
        "taskId": str,
        "checkName": str,
        "taskStartTime": datetime,
        "findingTime": datetime,
        "severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"],
        "nonCompliantResource": ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef,
        "relatedResources": List[ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef],
        "reasonForNonCompliance": str,
        "reasonForNonComplianceCode": str,
    },
    total=False,
)


class ClientListAuditFindingsResponsefindingsTypeDef(
    _ClientListAuditFindingsResponsefindingsTypeDef
):
    """
    - *(dict) --*

      The findings (results) of the audit.
      - **findingId** *(string) --*

        A unique identifier for this set of audit findings. This identifier is used to apply
        mitigation tasks to one or more sets of findings.
    """


_ClientListAuditFindingsResponseTypeDef = TypedDict(
    "_ClientListAuditFindingsResponseTypeDef",
    {"findings": List[ClientListAuditFindingsResponsefindingsTypeDef], "nextToken": str},
    total=False,
)


class ClientListAuditFindingsResponseTypeDef(_ClientListAuditFindingsResponseTypeDef):
    """
    - *(dict) --*

      - **findings** *(list) --*

        The findings (results) of the audit.
        - *(dict) --*

          The findings (results) of the audit.
          - **findingId** *(string) --*

            A unique identifier for this set of audit findings. This identifier is used to apply
            mitigation tasks to one or more sets of findings.
    """


_ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef = TypedDict(
    "_ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef",
    {
        "taskId": str,
        "findingId": str,
        "actionName": str,
        "actionId": str,
        "status": Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED", "SKIPPED", "PENDING"],
        "startTime": datetime,
        "endTime": datetime,
        "errorCode": str,
        "message": str,
    },
    total=False,
)


class ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef(
    _ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef
):
    """
    - *(dict) --*

      Returned by ListAuditMitigationActionsTask, this object contains information that describes a
      mitigation action that has been started.
      - **taskId** *(string) --*

        The unique identifier for the task that applies the mitigation action.
    """


_ClientListAuditMitigationActionsExecutionsResponseTypeDef = TypedDict(
    "_ClientListAuditMitigationActionsExecutionsResponseTypeDef",
    {
        "actionsExecutions": List[
            ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListAuditMitigationActionsExecutionsResponseTypeDef(
    _ClientListAuditMitigationActionsExecutionsResponseTypeDef
):
    """
    - *(dict) --*

      - **actionsExecutions** *(list) --*

        A set of task execution results based on the input parameters. Details include the
        mitigation action applied, start time, and task status.
        - *(dict) --*

          Returned by ListAuditMitigationActionsTask, this object contains information that
          describes a mitigation action that has been started.
          - **taskId** *(string) --*

            The unique identifier for the task that applies the mitigation action.
    """


_ClientListAuditMitigationActionsTasksResponsetasksTypeDef = TypedDict(
    "_ClientListAuditMitigationActionsTasksResponsetasksTypeDef",
    {
        "taskId": str,
        "startTime": datetime,
        "taskStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"],
    },
    total=False,
)


class ClientListAuditMitigationActionsTasksResponsetasksTypeDef(
    _ClientListAuditMitigationActionsTasksResponsetasksTypeDef
):
    """
    - *(dict) --*

      Information about an audit mitigation actions task that is returned by
      ``ListAuditMitigationActionsTasks`` .
      - **taskId** *(string) --*

        The unique identifier for the task.
    """


_ClientListAuditMitigationActionsTasksResponseTypeDef = TypedDict(
    "_ClientListAuditMitigationActionsTasksResponseTypeDef",
    {"tasks": List[ClientListAuditMitigationActionsTasksResponsetasksTypeDef], "nextToken": str},
    total=False,
)


class ClientListAuditMitigationActionsTasksResponseTypeDef(
    _ClientListAuditMitigationActionsTasksResponseTypeDef
):
    """
    - *(dict) --*

      - **tasks** *(list) --*

        The collection of audit mitigation tasks that matched the filter criteria.
        - *(dict) --*

          Information about an audit mitigation actions task that is returned by
          ``ListAuditMitigationActionsTasks`` .
          - **taskId** *(string) --*

            The unique identifier for the task.
    """


_ClientListAuditTasksResponsetasksTypeDef = TypedDict(
    "_ClientListAuditTasksResponsetasksTypeDef",
    {
        "taskId": str,
        "taskStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"],
        "taskType": Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"],
    },
    total=False,
)


class ClientListAuditTasksResponsetasksTypeDef(_ClientListAuditTasksResponsetasksTypeDef):
    """
    - *(dict) --*

      The audits that were performed.
      - **taskId** *(string) --*

        The ID of this audit.
    """


_ClientListAuditTasksResponseTypeDef = TypedDict(
    "_ClientListAuditTasksResponseTypeDef",
    {"tasks": List[ClientListAuditTasksResponsetasksTypeDef], "nextToken": str},
    total=False,
)


class ClientListAuditTasksResponseTypeDef(_ClientListAuditTasksResponseTypeDef):
    """
    - *(dict) --*

      - **tasks** *(list) --*

        The audits that were performed during the specified time period.
        - *(dict) --*

          The audits that were performed.
          - **taskId** *(string) --*

            The ID of this audit.
    """


_ClientListAuthorizersResponseauthorizersTypeDef = TypedDict(
    "_ClientListAuthorizersResponseauthorizersTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)


class ClientListAuthorizersResponseauthorizersTypeDef(
    _ClientListAuthorizersResponseauthorizersTypeDef
):
    """
    - *(dict) --*

      The authorizer summary.
      - **authorizerName** *(string) --*

        The authorizer name.
    """


_ClientListAuthorizersResponseTypeDef = TypedDict(
    "_ClientListAuthorizersResponseTypeDef",
    {"authorizers": List[ClientListAuthorizersResponseauthorizersTypeDef], "nextMarker": str},
    total=False,
)


class ClientListAuthorizersResponseTypeDef(_ClientListAuthorizersResponseTypeDef):
    """
    - *(dict) --*

      - **authorizers** *(list) --*

        The authorizers.
        - *(dict) --*

          The authorizer summary.
          - **authorizerName** *(string) --*

            The authorizer name.
    """


_ClientListBillingGroupsResponsebillingGroupsTypeDef = TypedDict(
    "_ClientListBillingGroupsResponsebillingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ClientListBillingGroupsResponsebillingGroupsTypeDef(
    _ClientListBillingGroupsResponsebillingGroupsTypeDef
):
    """
    - *(dict) --*

      The name and ARN of a group.
      - **groupName** *(string) --*

        The group name.
    """


_ClientListBillingGroupsResponseTypeDef = TypedDict(
    "_ClientListBillingGroupsResponseTypeDef",
    {"billingGroups": List[ClientListBillingGroupsResponsebillingGroupsTypeDef], "nextToken": str},
    total=False,
)


class ClientListBillingGroupsResponseTypeDef(_ClientListBillingGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **billingGroups** *(list) --*

        The list of billing groups.
        - *(dict) --*

          The name and ARN of a group.
          - **groupName** *(string) --*

            The group name.
    """


_ClientListCaCertificatesResponsecertificatesTypeDef = TypedDict(
    "_ClientListCaCertificatesResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal["ACTIVE", "INACTIVE"],
        "creationDate": datetime,
    },
    total=False,
)


class ClientListCaCertificatesResponsecertificatesTypeDef(
    _ClientListCaCertificatesResponsecertificatesTypeDef
):
    """
    - *(dict) --*

      A CA certificate.
      - **certificateArn** *(string) --*

        The ARN of the CA certificate.
    """


_ClientListCaCertificatesResponseTypeDef = TypedDict(
    "_ClientListCaCertificatesResponseTypeDef",
    {"certificates": List[ClientListCaCertificatesResponsecertificatesTypeDef], "nextMarker": str},
    total=False,
)


class ClientListCaCertificatesResponseTypeDef(_ClientListCaCertificatesResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListCACertificates operation.
      - **certificates** *(list) --*

        The CA certificates registered in your AWS account.
        - *(dict) --*

          A CA certificate.
          - **certificateArn** *(string) --*

            The ARN of the CA certificate.
    """


_ClientListCertificatesByCaResponsecertificatesTypeDef = TypedDict(
    "_ClientListCertificatesByCaResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ],
        "creationDate": datetime,
    },
    total=False,
)


class ClientListCertificatesByCaResponsecertificatesTypeDef(
    _ClientListCertificatesByCaResponsecertificatesTypeDef
):
    """
    - *(dict) --*

      Information about a certificate.
      - **certificateArn** *(string) --*

        The ARN of the certificate.
    """


_ClientListCertificatesByCaResponseTypeDef = TypedDict(
    "_ClientListCertificatesByCaResponseTypeDef",
    {
        "certificates": List[ClientListCertificatesByCaResponsecertificatesTypeDef],
        "nextMarker": str,
    },
    total=False,
)


class ClientListCertificatesByCaResponseTypeDef(_ClientListCertificatesByCaResponseTypeDef):
    """
    - *(dict) --*

      The output of the ListCertificatesByCA operation.
      - **certificates** *(list) --*

        The device certificates signed by the specified CA certificate.
        - *(dict) --*

          Information about a certificate.
          - **certificateArn** *(string) --*

            The ARN of the certificate.
    """


_ClientListCertificatesResponsecertificatesTypeDef = TypedDict(
    "_ClientListCertificatesResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ],
        "creationDate": datetime,
    },
    total=False,
)


class ClientListCertificatesResponsecertificatesTypeDef(
    _ClientListCertificatesResponsecertificatesTypeDef
):
    """
    - *(dict) --*

      Information about a certificate.
      - **certificateArn** *(string) --*

        The ARN of the certificate.
    """


_ClientListCertificatesResponseTypeDef = TypedDict(
    "_ClientListCertificatesResponseTypeDef",
    {"certificates": List[ClientListCertificatesResponsecertificatesTypeDef], "nextMarker": str},
    total=False,
)


class ClientListCertificatesResponseTypeDef(_ClientListCertificatesResponseTypeDef):
    """
    - *(dict) --*

      The output of the ListCertificates operation.
      - **certificates** *(list) --*

        The descriptions of the certificates.
        - *(dict) --*

          Information about a certificate.
          - **certificateArn** *(string) --*

            The ARN of the certificate.
    """


_ClientListDomainConfigurationsResponsedomainConfigurationsTypeDef = TypedDict(
    "_ClientListDomainConfigurationsResponsedomainConfigurationsTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "serviceType": Literal["DATA", "CREDENTIAL_PROVIDER", "JOBS"],
    },
    total=False,
)


class ClientListDomainConfigurationsResponsedomainConfigurationsTypeDef(
    _ClientListDomainConfigurationsResponsedomainConfigurationsTypeDef
):
    """
    - *(dict) --*

      The summary of a domain configuration. A domain configuration specifies custom IoT-specific
      information about a domain. A domain configuration can be associated with an AWS-managed
      domain (for example, dbc123defghijk.iot.us-west-2.amazonaws.com), a customer managed domain,
      or a default endpoint.
      * Data
      * Jobs
      * CredentialProvider
      .. note::

        The domain configuration feature is in public preview and is subject to change.
    """


_ClientListDomainConfigurationsResponseTypeDef = TypedDict(
    "_ClientListDomainConfigurationsResponseTypeDef",
    {
        "domainConfigurations": List[
            ClientListDomainConfigurationsResponsedomainConfigurationsTypeDef
        ],
        "nextMarker": str,
    },
    total=False,
)


class ClientListDomainConfigurationsResponseTypeDef(_ClientListDomainConfigurationsResponseTypeDef):
    """
    - *(dict) --*

      - **domainConfigurations** *(list) --*

        A list of objects that contain summary information about the user's domain configurations.
        - *(dict) --*

          The summary of a domain configuration. A domain configuration specifies custom
          IoT-specific information about a domain. A domain configuration can be associated with an
          AWS-managed domain (for example, dbc123defghijk.iot.us-west-2.amazonaws.com), a customer
          managed domain, or a default endpoint.
          * Data
          * Jobs
          * CredentialProvider
          .. note::

            The domain configuration feature is in public preview and is subject to change.
    """


_ClientListIndicesResponseTypeDef = TypedDict(
    "_ClientListIndicesResponseTypeDef", {"indexNames": List[str], "nextToken": str}, total=False
)


class ClientListIndicesResponseTypeDef(_ClientListIndicesResponseTypeDef):
    """
    - *(dict) --*

      - **indexNames** *(list) --*

        The index names.
        - *(string) --*
    """


_ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef = TypedDict(
    "_ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef",
    {
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)


class ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef(
    _ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef
):
    pass


_ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef = TypedDict(
    "_ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef",
    {
        "thingArn": str,
        "jobExecutionSummary": ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef,
    },
    total=False,
)


class ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef(
    _ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef
):
    """
    - *(dict) --*

      Contains a summary of information about job executions for a specific job.
      - **thingArn** *(string) --*

        The ARN of the thing on which the job execution is running.
    """


_ClientListJobExecutionsForJobResponseTypeDef = TypedDict(
    "_ClientListJobExecutionsForJobResponseTypeDef",
    {
        "executionSummaries": List[ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListJobExecutionsForJobResponseTypeDef(_ClientListJobExecutionsForJobResponseTypeDef):
    """
    - *(dict) --*

      - **executionSummaries** *(list) --*

        A list of job execution summaries.
        - *(dict) --*

          Contains a summary of information about job executions for a specific job.
          - **thingArn** *(string) --*

            The ARN of the thing on which the job execution is running.
    """


_ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef = TypedDict(
    "_ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef",
    {
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)


class ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef(
    _ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef
):
    pass


_ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef = TypedDict(
    "_ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef",
    {
        "jobId": str,
        "jobExecutionSummary": ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef,
    },
    total=False,
)


class ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef(
    _ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef
):
    """
    - *(dict) --*

      The job execution summary for a thing.
      - **jobId** *(string) --*

        The unique identifier you assigned to this job when it was created.
    """


_ClientListJobExecutionsForThingResponseTypeDef = TypedDict(
    "_ClientListJobExecutionsForThingResponseTypeDef",
    {
        "executionSummaries": List[
            ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListJobExecutionsForThingResponseTypeDef(
    _ClientListJobExecutionsForThingResponseTypeDef
):
    """
    - *(dict) --*

      - **executionSummaries** *(list) --*

        A list of job execution summaries.
        - *(dict) --*

          The job execution summary for a thing.
          - **jobId** *(string) --*

            The unique identifier you assigned to this job when it was created.
    """


_ClientListJobsResponsejobsTypeDef = TypedDict(
    "_ClientListJobsResponsejobsTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "thingGroupId": str,
        "targetSelection": Literal["CONTINUOUS", "SNAPSHOT"],
        "status": Literal["IN_PROGRESS", "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
    },
    total=False,
)


class ClientListJobsResponsejobsTypeDef(_ClientListJobsResponsejobsTypeDef):
    """
    - *(dict) --*

      The job summary.
      - **jobArn** *(string) --*

        The job ARN.
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {"jobs": List[ClientListJobsResponsejobsTypeDef], "nextToken": str},
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    - *(dict) --*

      - **jobs** *(list) --*

        A list of jobs.
        - *(dict) --*

          The job summary.
          - **jobArn** *(string) --*

            The job ARN.
    """


_ClientListMitigationActionsResponseactionIdentifiersTypeDef = TypedDict(
    "_ClientListMitigationActionsResponseactionIdentifiersTypeDef",
    {"actionName": str, "actionArn": str, "creationDate": datetime},
    total=False,
)


class ClientListMitigationActionsResponseactionIdentifiersTypeDef(
    _ClientListMitigationActionsResponseactionIdentifiersTypeDef
):
    """
    - *(dict) --*

      Information that identifies a mitigation action. This information is returned by
      ListMitigationActions.
      - **actionName** *(string) --*

        The friendly name of the mitigation action.
    """


_ClientListMitigationActionsResponseTypeDef = TypedDict(
    "_ClientListMitigationActionsResponseTypeDef",
    {
        "actionIdentifiers": List[ClientListMitigationActionsResponseactionIdentifiersTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListMitigationActionsResponseTypeDef(_ClientListMitigationActionsResponseTypeDef):
    """
    - *(dict) --*

      - **actionIdentifiers** *(list) --*

        A set of actions that matched the specified filter criteria.
        - *(dict) --*

          Information that identifies a mitigation action. This information is returned by
          ListMitigationActions.
          - **actionName** *(string) --*

            The friendly name of the mitigation action.
    """


_ClientListOtaUpdatesResponseotaUpdatesTypeDef = TypedDict(
    "_ClientListOtaUpdatesResponseotaUpdatesTypeDef",
    {"otaUpdateId": str, "otaUpdateArn": str, "creationDate": datetime},
    total=False,
)


class ClientListOtaUpdatesResponseotaUpdatesTypeDef(_ClientListOtaUpdatesResponseotaUpdatesTypeDef):
    """
    - *(dict) --*

      An OTA update summary.
      - **otaUpdateId** *(string) --*

        The OTA update ID.
    """


_ClientListOtaUpdatesResponseTypeDef = TypedDict(
    "_ClientListOtaUpdatesResponseTypeDef",
    {"otaUpdates": List[ClientListOtaUpdatesResponseotaUpdatesTypeDef], "nextToken": str},
    total=False,
)


class ClientListOtaUpdatesResponseTypeDef(_ClientListOtaUpdatesResponseTypeDef):
    """
    - *(dict) --*

      - **otaUpdates** *(list) --*

        A list of OTA update jobs.
        - *(dict) --*

          An OTA update summary.
          - **otaUpdateId** *(string) --*

            The OTA update ID.
    """


_ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef = TypedDict(
    "_ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "transferredTo": str,
        "transferDate": datetime,
        "transferMessage": str,
        "creationDate": datetime,
    },
    total=False,
)


class ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef(
    _ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef
):
    """
    - *(dict) --*

      A certificate that has been transferred but not yet accepted.
      - **certificateArn** *(string) --*

        The certificate ARN.
    """


_ClientListOutgoingCertificatesResponseTypeDef = TypedDict(
    "_ClientListOutgoingCertificatesResponseTypeDef",
    {
        "outgoingCertificates": List[
            ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef
        ],
        "nextMarker": str,
    },
    total=False,
)


class ClientListOutgoingCertificatesResponseTypeDef(_ClientListOutgoingCertificatesResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListOutgoingCertificates operation.
      - **outgoingCertificates** *(list) --*

        The certificates that are being transferred but not yet accepted.
        - *(dict) --*

          A certificate that has been transferred but not yet accepted.
          - **certificateArn** *(string) --*

            The certificate ARN.
    """


_ClientListPoliciesResponsepoliciesTypeDef = TypedDict(
    "_ClientListPoliciesResponsepoliciesTypeDef", {"policyName": str, "policyArn": str}, total=False
)


class ClientListPoliciesResponsepoliciesTypeDef(_ClientListPoliciesResponsepoliciesTypeDef):
    """
    - *(dict) --*

      Describes an AWS IoT policy.
      - **policyName** *(string) --*

        The policy name.
    """


_ClientListPoliciesResponseTypeDef = TypedDict(
    "_ClientListPoliciesResponseTypeDef",
    {"policies": List[ClientListPoliciesResponsepoliciesTypeDef], "nextMarker": str},
    total=False,
)


class ClientListPoliciesResponseTypeDef(_ClientListPoliciesResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListPolicies operation.
      - **policies** *(list) --*

        The descriptions of the policies.
        - *(dict) --*

          Describes an AWS IoT policy.
          - **policyName** *(string) --*

            The policy name.
    """


_ClientListPolicyPrincipalsResponseTypeDef = TypedDict(
    "_ClientListPolicyPrincipalsResponseTypeDef",
    {"principals": List[str], "nextMarker": str},
    total=False,
)


class ClientListPolicyPrincipalsResponseTypeDef(_ClientListPolicyPrincipalsResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListPolicyPrincipals operation.
      - **principals** *(list) --*

        The descriptions of the principals.
        - *(string) --*
    """


_ClientListPolicyVersionsResponsepolicyVersionsTypeDef = TypedDict(
    "_ClientListPolicyVersionsResponsepolicyVersionsTypeDef",
    {"versionId": str, "isDefaultVersion": bool, "createDate": datetime},
    total=False,
)


class ClientListPolicyVersionsResponsepolicyVersionsTypeDef(
    _ClientListPolicyVersionsResponsepolicyVersionsTypeDef
):
    """
    - *(dict) --*

      Describes a policy version.
      - **versionId** *(string) --*

        The policy version ID.
    """


_ClientListPolicyVersionsResponseTypeDef = TypedDict(
    "_ClientListPolicyVersionsResponseTypeDef",
    {"policyVersions": List[ClientListPolicyVersionsResponsepolicyVersionsTypeDef]},
    total=False,
)


class ClientListPolicyVersionsResponseTypeDef(_ClientListPolicyVersionsResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListPolicyVersions operation.
      - **policyVersions** *(list) --*

        The policy versions.
        - *(dict) --*

          Describes a policy version.
          - **versionId** *(string) --*

            The policy version ID.
    """


_ClientListPrincipalPoliciesResponsepoliciesTypeDef = TypedDict(
    "_ClientListPrincipalPoliciesResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ClientListPrincipalPoliciesResponsepoliciesTypeDef(
    _ClientListPrincipalPoliciesResponsepoliciesTypeDef
):
    """
    - *(dict) --*

      Describes an AWS IoT policy.
      - **policyName** *(string) --*

        The policy name.
    """


_ClientListPrincipalPoliciesResponseTypeDef = TypedDict(
    "_ClientListPrincipalPoliciesResponseTypeDef",
    {"policies": List[ClientListPrincipalPoliciesResponsepoliciesTypeDef], "nextMarker": str},
    total=False,
)


class ClientListPrincipalPoliciesResponseTypeDef(_ClientListPrincipalPoliciesResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListPrincipalPolicies operation.
      - **policies** *(list) --*

        The policies.
        - *(dict) --*

          Describes an AWS IoT policy.
          - **policyName** *(string) --*

            The policy name.
    """


_ClientListPrincipalThingsResponseTypeDef = TypedDict(
    "_ClientListPrincipalThingsResponseTypeDef",
    {"things": List[str], "nextToken": str},
    total=False,
)


class ClientListPrincipalThingsResponseTypeDef(_ClientListPrincipalThingsResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListPrincipalThings operation.
      - **things** *(list) --*

        The things.
        - *(string) --*
    """


_ClientListProvisioningTemplateVersionsResponseversionsTypeDef = TypedDict(
    "_ClientListProvisioningTemplateVersionsResponseversionsTypeDef",
    {"versionId": int, "creationDate": datetime, "isDefaultVersion": bool},
    total=False,
)


class ClientListProvisioningTemplateVersionsResponseversionsTypeDef(
    _ClientListProvisioningTemplateVersionsResponseversionsTypeDef
):
    """
    - *(dict) --*

      A summary of information about a fleet provision template version.
      - **versionId** *(integer) --*

        The ID of the fleet privisioning template version.
    """


_ClientListProvisioningTemplateVersionsResponseTypeDef = TypedDict(
    "_ClientListProvisioningTemplateVersionsResponseTypeDef",
    {
        "versions": List[ClientListProvisioningTemplateVersionsResponseversionsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListProvisioningTemplateVersionsResponseTypeDef(
    _ClientListProvisioningTemplateVersionsResponseTypeDef
):
    """
    - *(dict) --*

      - **versions** *(list) --*

        The list of fleet provisioning template versions.
        - *(dict) --*

          A summary of information about a fleet provision template version.
          - **versionId** *(integer) --*

            The ID of the fleet privisioning template version.
    """


_ClientListProvisioningTemplatesResponsetemplatesTypeDef = TypedDict(
    "_ClientListProvisioningTemplatesResponsetemplatesTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "description": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "enabled": bool,
    },
    total=False,
)


class ClientListProvisioningTemplatesResponsetemplatesTypeDef(
    _ClientListProvisioningTemplatesResponsetemplatesTypeDef
):
    """
    - *(dict) --*

      A summary of information about a fleet provisioning template.
      - **templateArn** *(string) --*

        The ARN of the fleet provisioning template.
    """


_ClientListProvisioningTemplatesResponseTypeDef = TypedDict(
    "_ClientListProvisioningTemplatesResponseTypeDef",
    {"templates": List[ClientListProvisioningTemplatesResponsetemplatesTypeDef], "nextToken": str},
    total=False,
)


class ClientListProvisioningTemplatesResponseTypeDef(
    _ClientListProvisioningTemplatesResponseTypeDef
):
    """
    - *(dict) --*

      - **templates** *(list) --*

        A list of fleet provisioning templates
        - *(dict) --*

          A summary of information about a fleet provisioning template.
          - **templateArn** *(string) --*

            The ARN of the fleet provisioning template.
    """


_ClientListRoleAliasesResponseTypeDef = TypedDict(
    "_ClientListRoleAliasesResponseTypeDef",
    {"roleAliases": List[str], "nextMarker": str},
    total=False,
)


class ClientListRoleAliasesResponseTypeDef(_ClientListRoleAliasesResponseTypeDef):
    """
    - *(dict) --*

      - **roleAliases** *(list) --*

        The role aliases.
        - *(string) --*
    """


_ClientListScheduledAuditsResponsescheduledAuditsTypeDef = TypedDict(
    "_ClientListScheduledAuditsResponsescheduledAuditsTypeDef",
    {
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
        "frequency": Literal["DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY"],
        "dayOfMonth": str,
        "dayOfWeek": Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"],
    },
    total=False,
)


class ClientListScheduledAuditsResponsescheduledAuditsTypeDef(
    _ClientListScheduledAuditsResponsescheduledAuditsTypeDef
):
    """
    - *(dict) --*

      Information about the scheduled audit.
      - **scheduledAuditName** *(string) --*

        The name of the scheduled audit.
    """


_ClientListScheduledAuditsResponseTypeDef = TypedDict(
    "_ClientListScheduledAuditsResponseTypeDef",
    {
        "scheduledAudits": List[ClientListScheduledAuditsResponsescheduledAuditsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListScheduledAuditsResponseTypeDef(_ClientListScheduledAuditsResponseTypeDef):
    """
    - *(dict) --*

      - **scheduledAudits** *(list) --*

        The list of scheduled audits.
        - *(dict) --*

          Information about the scheduled audit.
          - **scheduledAuditName** *(string) --*

            The name of the scheduled audit.
    """


_ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef = TypedDict(
    "_ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef",
    {"name": str, "arn": str},
    total=False,
)


class ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef(
    _ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef
):
    """
    - **securityProfileIdentifier** *(dict) --*

      Information that identifies the security profile.
      - **name** *(string) --*

        The name you have given to the security profile.
    """


_ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef = TypedDict(
    "_ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef",
    {"arn": str},
    total=False,
)


class ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef(
    _ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef
):
    pass


_ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef = TypedDict(
    "_ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef",
    {
        "securityProfileIdentifier": ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef,
        "target": ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef,
    },
    total=False,
)


class ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef(
    _ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef
):
    """
    - *(dict) --*

      Information about a security profile and the target associated with it.
      - **securityProfileIdentifier** *(dict) --*

        Information that identifies the security profile.
        - **name** *(string) --*

          The name you have given to the security profile.
    """


_ClientListSecurityProfilesForTargetResponseTypeDef = TypedDict(
    "_ClientListSecurityProfilesForTargetResponseTypeDef",
    {
        "securityProfileTargetMappings": List[
            ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListSecurityProfilesForTargetResponseTypeDef(
    _ClientListSecurityProfilesForTargetResponseTypeDef
):
    """
    - *(dict) --*

      - **securityProfileTargetMappings** *(list) --*

        A list of security profiles and their associated targets.
        - *(dict) --*

          Information about a security profile and the target associated with it.
          - **securityProfileIdentifier** *(dict) --*

            Information that identifies the security profile.
            - **name** *(string) --*

              The name you have given to the security profile.
    """


_ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef = TypedDict(
    "_ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef",
    {"name": str, "arn": str},
    total=False,
)


class ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef(
    _ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef
):
    """
    - *(dict) --*

      Identifying information for a Device Defender security profile.
      - **name** *(string) --*

        The name you have given to the security profile.
    """


_ClientListSecurityProfilesResponseTypeDef = TypedDict(
    "_ClientListSecurityProfilesResponseTypeDef",
    {
        "securityProfileIdentifiers": List[
            ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListSecurityProfilesResponseTypeDef(_ClientListSecurityProfilesResponseTypeDef):
    """
    - *(dict) --*

      - **securityProfileIdentifiers** *(list) --*

        A list of security profile identifiers (names and ARNs).
        - *(dict) --*

          Identifying information for a Device Defender security profile.
          - **name** *(string) --*

            The name you have given to the security profile.
    """


_ClientListStreamsResponsestreamsTypeDef = TypedDict(
    "_ClientListStreamsResponsestreamsTypeDef",
    {"streamId": str, "streamArn": str, "streamVersion": int, "description": str},
    total=False,
)


class ClientListStreamsResponsestreamsTypeDef(_ClientListStreamsResponsestreamsTypeDef):
    """
    - *(dict) --*

      A summary of a stream.
      - **streamId** *(string) --*

        The stream ID.
    """


_ClientListStreamsResponseTypeDef = TypedDict(
    "_ClientListStreamsResponseTypeDef",
    {"streams": List[ClientListStreamsResponsestreamsTypeDef], "nextToken": str},
    total=False,
)


class ClientListStreamsResponseTypeDef(_ClientListStreamsResponseTypeDef):
    """
    - *(dict) --*

      - **streams** *(list) --*

        A list of streams.
        - *(dict) --*

          A summary of a stream.
          - **streamId** *(string) --*

            The stream ID.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponsetagsTypeDef(_ClientListTagsForResourceResponsetagsTypeDef):
    """
    - *(dict) --*

      A set of key/value pairs that are used to manage the resource.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef], "nextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        The list of tags assigned to the resource.
        - *(dict) --*

          A set of key/value pairs that are used to manage the resource.
          - **Key** *(string) --*

            The tag's key.
    """


_ClientListTargetsForPolicyResponseTypeDef = TypedDict(
    "_ClientListTargetsForPolicyResponseTypeDef",
    {"targets": List[str], "nextMarker": str},
    total=False,
)


class ClientListTargetsForPolicyResponseTypeDef(_ClientListTargetsForPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **targets** *(list) --*

        The policy targets.
        - *(string) --*
    """


_ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef = TypedDict(
    "_ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef",
    {"arn": str},
    total=False,
)


class ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef(
    _ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef
):
    """
    - *(dict) --*

      A target to which an alert is sent when a security profile behavior is violated.
      - **arn** *(string) --*

        The ARN of the security profile.
    """


_ClientListTargetsForSecurityProfileResponseTypeDef = TypedDict(
    "_ClientListTargetsForSecurityProfileResponseTypeDef",
    {
        "securityProfileTargets": List[
            ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListTargetsForSecurityProfileResponseTypeDef(
    _ClientListTargetsForSecurityProfileResponseTypeDef
):
    """
    - *(dict) --*

      - **securityProfileTargets** *(list) --*

        The thing groups to which the security profile is attached.
        - *(dict) --*

          A target to which an alert is sent when a security profile behavior is violated.
          - **arn** *(string) --*

            The ARN of the security profile.
    """


_ClientListThingGroupsForThingResponsethingGroupsTypeDef = TypedDict(
    "_ClientListThingGroupsForThingResponsethingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ClientListThingGroupsForThingResponsethingGroupsTypeDef(
    _ClientListThingGroupsForThingResponsethingGroupsTypeDef
):
    """
    - *(dict) --*

      The name and ARN of a group.
      - **groupName** *(string) --*

        The group name.
    """


_ClientListThingGroupsForThingResponseTypeDef = TypedDict(
    "_ClientListThingGroupsForThingResponseTypeDef",
    {
        "thingGroups": List[ClientListThingGroupsForThingResponsethingGroupsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListThingGroupsForThingResponseTypeDef(_ClientListThingGroupsForThingResponseTypeDef):
    """
    - *(dict) --*

      - **thingGroups** *(list) --*

        The thing groups.
        - *(dict) --*

          The name and ARN of a group.
          - **groupName** *(string) --*

            The group name.
    """


_ClientListThingGroupsResponsethingGroupsTypeDef = TypedDict(
    "_ClientListThingGroupsResponsethingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ClientListThingGroupsResponsethingGroupsTypeDef(
    _ClientListThingGroupsResponsethingGroupsTypeDef
):
    """
    - *(dict) --*

      The name and ARN of a group.
      - **groupName** *(string) --*

        The group name.
    """


_ClientListThingGroupsResponseTypeDef = TypedDict(
    "_ClientListThingGroupsResponseTypeDef",
    {"thingGroups": List[ClientListThingGroupsResponsethingGroupsTypeDef], "nextToken": str},
    total=False,
)


class ClientListThingGroupsResponseTypeDef(_ClientListThingGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **thingGroups** *(list) --*

        The thing groups.
        - *(dict) --*

          The name and ARN of a group.
          - **groupName** *(string) --*

            The group name.
    """


_ClientListThingPrincipalsResponseTypeDef = TypedDict(
    "_ClientListThingPrincipalsResponseTypeDef", {"principals": List[str]}, total=False
)


class ClientListThingPrincipalsResponseTypeDef(_ClientListThingPrincipalsResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListThingPrincipals operation.
      - **principals** *(list) --*

        The principals associated with the thing.
        - *(string) --*
    """


_ClientListThingRegistrationTaskReportsResponseTypeDef = TypedDict(
    "_ClientListThingRegistrationTaskReportsResponseTypeDef",
    {"resourceLinks": List[str], "reportType": Literal["ERRORS", "RESULTS"], "nextToken": str},
    total=False,
)


class ClientListThingRegistrationTaskReportsResponseTypeDef(
    _ClientListThingRegistrationTaskReportsResponseTypeDef
):
    """
    - *(dict) --*

      - **resourceLinks** *(list) --*

        Links to the task resources.
        - *(string) --*
    """


_ClientListThingRegistrationTasksResponseTypeDef = TypedDict(
    "_ClientListThingRegistrationTasksResponseTypeDef",
    {"taskIds": List[str], "nextToken": str},
    total=False,
)


class ClientListThingRegistrationTasksResponseTypeDef(
    _ClientListThingRegistrationTasksResponseTypeDef
):
    """
    - *(dict) --*

      - **taskIds** *(list) --*

        A list of bulk thing provisioning task IDs.
        - *(string) --*
    """


_ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef = TypedDict(
    "_ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef",
    {"deprecated": bool, "deprecationDate": datetime, "creationDate": datetime},
    total=False,
)


class ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef(
    _ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef
):
    pass


_ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef = TypedDict(
    "_ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef",
    {"thingTypeDescription": str, "searchableAttributes": List[str]},
    total=False,
)


class ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef(
    _ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef
):
    pass


_ClientListThingTypesResponsethingTypesTypeDef = TypedDict(
    "_ClientListThingTypesResponsethingTypesTypeDef",
    {
        "thingTypeName": str,
        "thingTypeArn": str,
        "thingTypeProperties": ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef,
        "thingTypeMetadata": ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef,
    },
    total=False,
)


class ClientListThingTypesResponsethingTypesTypeDef(_ClientListThingTypesResponsethingTypesTypeDef):
    """
    - *(dict) --*

      The definition of the thing type, including thing type name and description.
      - **thingTypeName** *(string) --*

        The name of the thing type.
    """


_ClientListThingTypesResponseTypeDef = TypedDict(
    "_ClientListThingTypesResponseTypeDef",
    {"thingTypes": List[ClientListThingTypesResponsethingTypesTypeDef], "nextToken": str},
    total=False,
)


class ClientListThingTypesResponseTypeDef(_ClientListThingTypesResponseTypeDef):
    """
    - *(dict) --*

      The output for the ListThingTypes operation.
      - **thingTypes** *(list) --*

        The thing types.
        - *(dict) --*

          The definition of the thing type, including thing type name and description.
          - **thingTypeName** *(string) --*

            The name of the thing type.
    """


_ClientListThingsInBillingGroupResponseTypeDef = TypedDict(
    "_ClientListThingsInBillingGroupResponseTypeDef",
    {"things": List[str], "nextToken": str},
    total=False,
)


class ClientListThingsInBillingGroupResponseTypeDef(_ClientListThingsInBillingGroupResponseTypeDef):
    """
    - *(dict) --*

      - **things** *(list) --*

        A list of things in the billing group.
        - *(string) --*
    """


_ClientListThingsInThingGroupResponseTypeDef = TypedDict(
    "_ClientListThingsInThingGroupResponseTypeDef",
    {"things": List[str], "nextToken": str},
    total=False,
)


class ClientListThingsInThingGroupResponseTypeDef(_ClientListThingsInThingGroupResponseTypeDef):
    """
    - *(dict) --*

      - **things** *(list) --*

        The things in the specified thing group.
        - *(string) --*
    """


_ClientListThingsResponsethingsTypeDef = TypedDict(
    "_ClientListThingsResponsethingsTypeDef",
    {
        "thingName": str,
        "thingTypeName": str,
        "thingArn": str,
        "attributes": Dict[str, str],
        "version": int,
    },
    total=False,
)


class ClientListThingsResponsethingsTypeDef(_ClientListThingsResponsethingsTypeDef):
    """
    - *(dict) --*

      The properties of the thing, including thing name, thing type name, and a list of thing
      attributes.
      - **thingName** *(string) --*

        The name of the thing.
    """


_ClientListThingsResponseTypeDef = TypedDict(
    "_ClientListThingsResponseTypeDef",
    {"things": List[ClientListThingsResponsethingsTypeDef], "nextToken": str},
    total=False,
)


class ClientListThingsResponseTypeDef(_ClientListThingsResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListThings operation.
      - **things** *(list) --*

        The things.
        - *(dict) --*

          The properties of the thing, including thing name, thing type name, and a list of thing
          attributes.
          - **thingName** *(string) --*

            The name of the thing.
    """


_ClientListTopicRuleDestinationsResponsedestinationSummarieshttpUrlSummaryTypeDef = TypedDict(
    "_ClientListTopicRuleDestinationsResponsedestinationSummarieshttpUrlSummaryTypeDef",
    {"confirmationUrl": str},
    total=False,
)


class ClientListTopicRuleDestinationsResponsedestinationSummarieshttpUrlSummaryTypeDef(
    _ClientListTopicRuleDestinationsResponsedestinationSummarieshttpUrlSummaryTypeDef
):
    pass


_ClientListTopicRuleDestinationsResponsedestinationSummariesTypeDef = TypedDict(
    "_ClientListTopicRuleDestinationsResponsedestinationSummariesTypeDef",
    {
        "arn": str,
        "status": Literal["ENABLED", "IN_PROGRESS", "DISABLED", "ERROR"],
        "statusReason": str,
        "httpUrlSummary": ClientListTopicRuleDestinationsResponsedestinationSummarieshttpUrlSummaryTypeDef,
    },
    total=False,
)


class ClientListTopicRuleDestinationsResponsedestinationSummariesTypeDef(
    _ClientListTopicRuleDestinationsResponsedestinationSummariesTypeDef
):
    """
    - *(dict) --*

      Information about the topic rule destination.
      - **arn** *(string) --*

        The topic rule destination ARN.
    """


_ClientListTopicRuleDestinationsResponseTypeDef = TypedDict(
    "_ClientListTopicRuleDestinationsResponseTypeDef",
    {
        "destinationSummaries": List[
            ClientListTopicRuleDestinationsResponsedestinationSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListTopicRuleDestinationsResponseTypeDef(
    _ClientListTopicRuleDestinationsResponseTypeDef
):
    """
    - *(dict) --*

      - **destinationSummaries** *(list) --*

        Information about a topic rule destination.
        - *(dict) --*

          Information about the topic rule destination.
          - **arn** *(string) --*

            The topic rule destination ARN.
    """


_ClientListTopicRulesResponserulesTypeDef = TypedDict(
    "_ClientListTopicRulesResponserulesTypeDef",
    {
        "ruleArn": str,
        "ruleName": str,
        "topicPattern": str,
        "createdAt": datetime,
        "ruleDisabled": bool,
    },
    total=False,
)


class ClientListTopicRulesResponserulesTypeDef(_ClientListTopicRulesResponserulesTypeDef):
    """
    - *(dict) --*

      Describes a rule.
      - **ruleArn** *(string) --*

        The rule ARN.
    """


_ClientListTopicRulesResponseTypeDef = TypedDict(
    "_ClientListTopicRulesResponseTypeDef",
    {"rules": List[ClientListTopicRulesResponserulesTypeDef], "nextToken": str},
    total=False,
)


class ClientListTopicRulesResponseTypeDef(_ClientListTopicRulesResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListTopicRules operation.
      - **rules** *(list) --*

        The rules.
        - *(dict) --*

          Describes a rule.
          - **ruleArn** *(string) --*

            The rule ARN.
    """


_ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef = TypedDict(
    "_ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef",
    {"targetType": Literal["DEFAULT", "THING_GROUP"], "targetName": str},
    total=False,
)


class ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef(
    _ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef
):
    """
    - **logTarget** *(dict) --*

      A log target
      - **targetType** *(string) --*

        The target type.
    """


_ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef = TypedDict(
    "_ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef",
    {
        "logTarget": ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef,
        "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"],
    },
    total=False,
)


class ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef(
    _ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef
):
    """
    - *(dict) --*

      The target configuration.
      - **logTarget** *(dict) --*

        A log target
        - **targetType** *(string) --*

          The target type.
    """


_ClientListV2LoggingLevelsResponseTypeDef = TypedDict(
    "_ClientListV2LoggingLevelsResponseTypeDef",
    {
        "logTargetConfigurations": List[
            ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListV2LoggingLevelsResponseTypeDef(_ClientListV2LoggingLevelsResponseTypeDef):
    """
    - *(dict) --*

      - **logTargetConfigurations** *(list) --*

        The logging configuration for a target.
        - *(dict) --*

          The target configuration.
          - **logTarget** *(dict) --*

            A log target
            - **targetType** *(string) --*

              The target type.
    """


_ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef(
    _ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef
):
    pass


_ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef = TypedDict(
    "_ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef(
    _ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef
):
    pass


_ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef = TypedDict(
    "_ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef(
    _ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef
):
    pass


_ClientListViolationEventsResponseviolationEventsbehaviorTypeDef = TypedDict(
    "_ClientListViolationEventsResponseviolationEventsbehaviorTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef,
    },
    total=False,
)


class ClientListViolationEventsResponseviolationEventsbehaviorTypeDef(
    _ClientListViolationEventsResponseviolationEventsbehaviorTypeDef
):
    pass


_ClientListViolationEventsResponseviolationEventsmetricValueTypeDef = TypedDict(
    "_ClientListViolationEventsResponseviolationEventsmetricValueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientListViolationEventsResponseviolationEventsmetricValueTypeDef(
    _ClientListViolationEventsResponseviolationEventsmetricValueTypeDef
):
    pass


_ClientListViolationEventsResponseviolationEventsTypeDef = TypedDict(
    "_ClientListViolationEventsResponseviolationEventsTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": ClientListViolationEventsResponseviolationEventsbehaviorTypeDef,
        "metricValue": ClientListViolationEventsResponseviolationEventsmetricValueTypeDef,
        "violationEventType": Literal["in-alarm", "alarm-cleared", "alarm-invalidated"],
        "violationEventTime": datetime,
    },
    total=False,
)


class ClientListViolationEventsResponseviolationEventsTypeDef(
    _ClientListViolationEventsResponseviolationEventsTypeDef
):
    """
    - *(dict) --*

      Information about a Device Defender security profile behavior violation.
      - **violationId** *(string) --*

        The ID of the violation event.
    """


_ClientListViolationEventsResponseTypeDef = TypedDict(
    "_ClientListViolationEventsResponseTypeDef",
    {
        "violationEvents": List[ClientListViolationEventsResponseviolationEventsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListViolationEventsResponseTypeDef(_ClientListViolationEventsResponseTypeDef):
    """
    - *(dict) --*

      - **violationEvents** *(list) --*

        The security profile violation alerts issued for this account during the given time period,
        potentially filtered by security profile, behavior violated, or thing (device) violating.
        - *(dict) --*

          Information about a Device Defender security profile behavior violation.
          - **violationId** *(string) --*

            The ID of the violation event.
    """


_ClientRegisterCaCertificateRegistrationConfigTypeDef = TypedDict(
    "_ClientRegisterCaCertificateRegistrationConfigTypeDef",
    {"templateBody": str, "roleArn": str},
    total=False,
)


class ClientRegisterCaCertificateRegistrationConfigTypeDef(
    _ClientRegisterCaCertificateRegistrationConfigTypeDef
):
    """
    Information about the registration configuration.
    - **templateBody** *(string) --*

      The template body.
    """


_ClientRegisterCaCertificateResponseTypeDef = TypedDict(
    "_ClientRegisterCaCertificateResponseTypeDef",
    {"certificateArn": str, "certificateId": str},
    total=False,
)


class ClientRegisterCaCertificateResponseTypeDef(_ClientRegisterCaCertificateResponseTypeDef):
    """
    - *(dict) --*

      The output from the RegisterCACertificateResponse operation.
      - **certificateArn** *(string) --*

        The CA certificate ARN.
    """


_ClientRegisterCertificateResponseTypeDef = TypedDict(
    "_ClientRegisterCertificateResponseTypeDef",
    {"certificateArn": str, "certificateId": str},
    total=False,
)


class ClientRegisterCertificateResponseTypeDef(_ClientRegisterCertificateResponseTypeDef):
    """
    - *(dict) --*

      The output from the RegisterCertificate operation.
      - **certificateArn** *(string) --*

        The certificate ARN.
    """


_ClientRegisterThingResponseTypeDef = TypedDict(
    "_ClientRegisterThingResponseTypeDef",
    {"certificatePem": str, "resourceArns": Dict[str, str]},
    total=False,
)


class ClientRegisterThingResponseTypeDef(_ClientRegisterThingResponseTypeDef):
    """
    - *(dict) --*

      - **certificatePem** *(string) --*

        .
    """


_ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": Literal["STRING", "NUMBER"],
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": Literal["STRING", "NUMBER"],
        "payloadField": str,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef",
    {"tableName": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionselasticsearchTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionselasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionselasticsearchTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionselasticsearchTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsfirehoseTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsfirehoseTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsfirehoseTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef",
    {"signingRegion": str, "serviceName": str, "roleArn": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionshttpauthTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionshttpauthTypeDef",
    {"sigv4": ClientReplaceTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionshttpauthTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionshttpauthTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionshttpheadersTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionshttpheadersTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionshttpheadersTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionshttpheadersTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionshttpTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionshttpTypeDef",
    {
        "url": str,
        "confirmationUrl": str,
        "headers": List[ClientReplaceTopicRuleTopicRulePayloadactionshttpheadersTypeDef],
        "auth": ClientReplaceTopicRuleTopicRulePayloadactionshttpauthTypeDef,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionshttpTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionshttpTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsiotEventsTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsiotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsiotEventsTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsiotEventsTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    {"timeInSeconds": str, "offsetInNanos": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    {"stringValue": str, "integerValue": str, "doubleValue": str, "booleanValue": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    {
        "value": ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef,
        "timestamp": ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef,
        "quality": str,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValues": List[
            ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
        ],
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef",
    {
        "putAssetPropertyValueEntries": List[
            ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef
        ],
        "roleArn": str,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionskinesisTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionskinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionskinesisTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionskinesisTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionslambdaTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionslambdaTypeDef", {"functionArn": str}, total=False
)


class ClientReplaceTopicRuleTopicRulePayloadactionslambdaTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionslambdaTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsrepublishTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsrepublishTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsrepublishTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionss3TypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionss3TypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
        "cannedAcl": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "log-delivery-write",
        ],
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionss3TypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionss3TypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionssalesforceTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionssalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionssalesforceTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionssalesforceTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionssnsTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionssnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": Literal["RAW", "JSON"]},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionssnsTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionssnsTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionssqsTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionssqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionssqsTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionssqsTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloadactionsTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloadactionsTypeDef",
    {
        "dynamoDB": ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBTypeDef,
        "dynamoDBv2": ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef,
        "lambda": ClientReplaceTopicRuleTopicRulePayloadactionslambdaTypeDef,
        "sns": ClientReplaceTopicRuleTopicRulePayloadactionssnsTypeDef,
        "sqs": ClientReplaceTopicRuleTopicRulePayloadactionssqsTypeDef,
        "kinesis": ClientReplaceTopicRuleTopicRulePayloadactionskinesisTypeDef,
        "republish": ClientReplaceTopicRuleTopicRulePayloadactionsrepublishTypeDef,
        "s3": ClientReplaceTopicRuleTopicRulePayloadactionss3TypeDef,
        "firehose": ClientReplaceTopicRuleTopicRulePayloadactionsfirehoseTypeDef,
        "cloudwatchMetric": ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef,
        "elasticsearch": ClientReplaceTopicRuleTopicRulePayloadactionselasticsearchTypeDef,
        "salesforce": ClientReplaceTopicRuleTopicRulePayloadactionssalesforceTypeDef,
        "iotAnalytics": ClientReplaceTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef,
        "iotEvents": ClientReplaceTopicRuleTopicRulePayloadactionsiotEventsTypeDef,
        "iotSiteWise": ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef,
        "stepFunctions": ClientReplaceTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef,
        "http": ClientReplaceTopicRuleTopicRulePayloadactionshttpTypeDef,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadactionsTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloadactionsTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": Literal["STRING", "NUMBER"],
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": Literal["STRING", "NUMBER"],
        "payloadField": str,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef",
    {"tableName": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef",
    {"signingRegion": str, "serviceName": str, "roleArn": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef",
    {"sigv4": ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpTypeDef",
    {
        "url": str,
        "confirmationUrl": str,
        "headers": List[ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef],
        "auth": ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    {"timeInSeconds": str, "offsetInNanos": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    {"stringValue": str, "integerValue": str, "doubleValue": str, "booleanValue": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    {
        "value": ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef,
        "timestamp": ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef,
        "quality": str,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValues": List[
            ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
        ],
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef",
    {
        "putAssetPropertyValueEntries": List[
            ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef
        ],
        "roleArn": str,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionkinesisTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionkinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionkinesisTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionkinesisTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionlambdaTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionlambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionlambdaTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionlambdaTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionrepublishTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionrepublishTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionrepublishTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActions3TypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActions3TypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
        "cannedAcl": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "log-delivery-write",
        ],
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActions3TypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActions3TypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionsnsTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionsnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": Literal["RAW", "JSON"]},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionsnsTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionsnsTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionsqsTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionsqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionsqsTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionsqsTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef
):
    pass


_ClientReplaceTopicRuleTopicRulePayloaderrorActionTypeDef = TypedDict(
    "_ClientReplaceTopicRuleTopicRulePayloaderrorActionTypeDef",
    {
        "dynamoDB": ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef,
        "dynamoDBv2": ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef,
        "lambda": ClientReplaceTopicRuleTopicRulePayloaderrorActionlambdaTypeDef,
        "sns": ClientReplaceTopicRuleTopicRulePayloaderrorActionsnsTypeDef,
        "sqs": ClientReplaceTopicRuleTopicRulePayloaderrorActionsqsTypeDef,
        "kinesis": ClientReplaceTopicRuleTopicRulePayloaderrorActionkinesisTypeDef,
        "republish": ClientReplaceTopicRuleTopicRulePayloaderrorActionrepublishTypeDef,
        "s3": ClientReplaceTopicRuleTopicRulePayloaderrorActions3TypeDef,
        "firehose": ClientReplaceTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef,
        "cloudwatchMetric": ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef,
        "elasticsearch": ClientReplaceTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef,
        "salesforce": ClientReplaceTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef,
        "iotAnalytics": ClientReplaceTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef,
        "iotEvents": ClientReplaceTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef,
        "iotSiteWise": ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef,
        "stepFunctions": ClientReplaceTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef,
        "http": ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpTypeDef,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloaderrorActionTypeDef(
    _ClientReplaceTopicRuleTopicRulePayloaderrorActionTypeDef
):
    pass


_RequiredClientReplaceTopicRuleTopicRulePayloadTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuleTopicRulePayloadTypeDef", {"sql": str}
)
_OptionalClientReplaceTopicRuleTopicRulePayloadTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuleTopicRulePayloadTypeDef",
    {
        "description": str,
        "actions": List[ClientReplaceTopicRuleTopicRulePayloadactionsTypeDef],
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": ClientReplaceTopicRuleTopicRulePayloaderrorActionTypeDef,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadTypeDef(
    _RequiredClientReplaceTopicRuleTopicRulePayloadTypeDef,
    _OptionalClientReplaceTopicRuleTopicRulePayloadTypeDef,
):
    """
    The rule payload.
    - **sql** *(string) --***[REQUIRED]**

      The SQL statement used to query the topic. For more information, see `AWS IoT SQL Reference
      <https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference>`__
      in the *AWS IoT Developer Guide* .
    """


_ClientSearchIndexResponsethingGroupsTypeDef = TypedDict(
    "_ClientSearchIndexResponsethingGroupsTypeDef",
    {
        "thingGroupName": str,
        "thingGroupId": str,
        "thingGroupDescription": str,
        "attributes": Dict[str, str],
        "parentGroupNames": List[str],
    },
    total=False,
)


class ClientSearchIndexResponsethingGroupsTypeDef(_ClientSearchIndexResponsethingGroupsTypeDef):
    pass


_ClientSearchIndexResponsethingsconnectivityTypeDef = TypedDict(
    "_ClientSearchIndexResponsethingsconnectivityTypeDef",
    {"connected": bool, "timestamp": int},
    total=False,
)


class ClientSearchIndexResponsethingsconnectivityTypeDef(
    _ClientSearchIndexResponsethingsconnectivityTypeDef
):
    pass


_ClientSearchIndexResponsethingsTypeDef = TypedDict(
    "_ClientSearchIndexResponsethingsTypeDef",
    {
        "thingName": str,
        "thingId": str,
        "thingTypeName": str,
        "thingGroupNames": List[str],
        "attributes": Dict[str, str],
        "shadow": str,
        "connectivity": ClientSearchIndexResponsethingsconnectivityTypeDef,
    },
    total=False,
)


class ClientSearchIndexResponsethingsTypeDef(_ClientSearchIndexResponsethingsTypeDef):
    pass


_ClientSearchIndexResponseTypeDef = TypedDict(
    "_ClientSearchIndexResponseTypeDef",
    {
        "nextToken": str,
        "things": List[ClientSearchIndexResponsethingsTypeDef],
        "thingGroups": List[ClientSearchIndexResponsethingGroupsTypeDef],
    },
    total=False,
)


class ClientSearchIndexResponseTypeDef(_ClientSearchIndexResponseTypeDef):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        The token used to get the next set of results, or ``null`` if there are no additional
        results.
    """


_ClientSetDefaultAuthorizerResponseTypeDef = TypedDict(
    "_ClientSetDefaultAuthorizerResponseTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)


class ClientSetDefaultAuthorizerResponseTypeDef(_ClientSetDefaultAuthorizerResponseTypeDef):
    """
    - *(dict) --*

      - **authorizerName** *(string) --*

        The authorizer name.
    """


_RequiredClientSetLoggingOptionsLoggingOptionsPayloadTypeDef = TypedDict(
    "_RequiredClientSetLoggingOptionsLoggingOptionsPayloadTypeDef", {"roleArn": str}
)
_OptionalClientSetLoggingOptionsLoggingOptionsPayloadTypeDef = TypedDict(
    "_OptionalClientSetLoggingOptionsLoggingOptionsPayloadTypeDef",
    {"logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"]},
    total=False,
)


class ClientSetLoggingOptionsLoggingOptionsPayloadTypeDef(
    _RequiredClientSetLoggingOptionsLoggingOptionsPayloadTypeDef,
    _OptionalClientSetLoggingOptionsLoggingOptionsPayloadTypeDef,
):
    """
    The logging options payload.
    - **roleArn** *(string) --***[REQUIRED]**

      The ARN of the IAM role that grants access.
    """


_RequiredClientSetV2LoggingLevelLogTargetTypeDef = TypedDict(
    "_RequiredClientSetV2LoggingLevelLogTargetTypeDef",
    {"targetType": Literal["DEFAULT", "THING_GROUP"]},
)
_OptionalClientSetV2LoggingLevelLogTargetTypeDef = TypedDict(
    "_OptionalClientSetV2LoggingLevelLogTargetTypeDef", {"targetName": str}, total=False
)


class ClientSetV2LoggingLevelLogTargetTypeDef(
    _RequiredClientSetV2LoggingLevelLogTargetTypeDef,
    _OptionalClientSetV2LoggingLevelLogTargetTypeDef,
):
    """
    The log target.
    - **targetType** *(string) --***[REQUIRED]**

      The target type.
    """


_ClientStartAuditMitigationActionsTaskResponseTypeDef = TypedDict(
    "_ClientStartAuditMitigationActionsTaskResponseTypeDef", {"taskId": str}, total=False
)


class ClientStartAuditMitigationActionsTaskResponseTypeDef(
    _ClientStartAuditMitigationActionsTaskResponseTypeDef
):
    """
    - *(dict) --*

      - **taskId** *(string) --*

        The unique identifier for the audit mitigation task. This matches the ``taskId`` that you
        specified in the request.
    """


_ClientStartAuditMitigationActionsTaskTargetTypeDef = TypedDict(
    "_ClientStartAuditMitigationActionsTaskTargetTypeDef",
    {
        "auditTaskId": str,
        "findingIds": List[str],
        "auditCheckToReasonCodeFilter": Dict[str, List[str]],
    },
    total=False,
)


class ClientStartAuditMitigationActionsTaskTargetTypeDef(
    _ClientStartAuditMitigationActionsTaskTargetTypeDef
):
    """
    Specifies the audit findings to which the mitigation actions are applied. You can apply them to
    a type of audit check, to all findings from an audit, or to a speecific set of findings.
    - **auditTaskId** *(string) --*

      If the task will apply a mitigation action to findings from a specific audit, this value
      uniquely identifies the audit.
    """


_ClientStartOnDemandAuditTaskResponseTypeDef = TypedDict(
    "_ClientStartOnDemandAuditTaskResponseTypeDef", {"taskId": str}, total=False
)


class ClientStartOnDemandAuditTaskResponseTypeDef(_ClientStartOnDemandAuditTaskResponseTypeDef):
    """
    - *(dict) --*

      - **taskId** *(string) --*

        The ID of the on-demand audit you started.
    """


_ClientStartThingRegistrationTaskResponseTypeDef = TypedDict(
    "_ClientStartThingRegistrationTaskResponseTypeDef", {"taskId": str}, total=False
)


class ClientStartThingRegistrationTaskResponseTypeDef(
    _ClientStartThingRegistrationTaskResponseTypeDef
):
    """
    - *(dict) --*

      - **taskId** *(string) --*

        The bulk thing provisioning task ID.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      A set of key/value pairs that are used to manage the resource.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientTestAuthorizationAuthInfosTypeDef = TypedDict(
    "_ClientTestAuthorizationAuthInfosTypeDef",
    {"actionType": Literal["PUBLISH", "SUBSCRIBE", "RECEIVE", "CONNECT"], "resources": List[str]},
    total=False,
)


class ClientTestAuthorizationAuthInfosTypeDef(_ClientTestAuthorizationAuthInfosTypeDef):
    """
    - *(dict) --*

      A collection of authorization information.
      - **actionType** *(string) --*

        The type of action for which the principal is being authorized.
    """


_ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef(
    _ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef
):
    pass


_ClientTestAuthorizationResponseauthResultsallowedTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsallowedTypeDef",
    {"policies": List[ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef]},
    total=False,
)


class ClientTestAuthorizationResponseauthResultsallowedTypeDef(
    _ClientTestAuthorizationResponseauthResultsallowedTypeDef
):
    pass


_ClientTestAuthorizationResponseauthResultsauthInfoTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsauthInfoTypeDef",
    {"actionType": Literal["PUBLISH", "SUBSCRIBE", "RECEIVE", "CONNECT"], "resources": List[str]},
    total=False,
)


class ClientTestAuthorizationResponseauthResultsauthInfoTypeDef(
    _ClientTestAuthorizationResponseauthResultsauthInfoTypeDef
):
    """
    - **authInfo** *(dict) --*

      Authorization information.
      - **actionType** *(string) --*

        The type of action for which the principal is being authorized.
    """


_ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef(
    _ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef
):
    pass


_ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef",
    {"policies": List[ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef]},
    total=False,
)


class ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef(
    _ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef
):
    pass


_ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef(
    _ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef
):
    pass


_ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef",
    {"policies": List[ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef]},
    total=False,
)


class ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef(
    _ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef
):
    pass


_ClientTestAuthorizationResponseauthResultsdeniedTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsdeniedTypeDef",
    {
        "implicitDeny": ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef,
        "explicitDeny": ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef,
    },
    total=False,
)


class ClientTestAuthorizationResponseauthResultsdeniedTypeDef(
    _ClientTestAuthorizationResponseauthResultsdeniedTypeDef
):
    pass


_ClientTestAuthorizationResponseauthResultsTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsTypeDef",
    {
        "authInfo": ClientTestAuthorizationResponseauthResultsauthInfoTypeDef,
        "allowed": ClientTestAuthorizationResponseauthResultsallowedTypeDef,
        "denied": ClientTestAuthorizationResponseauthResultsdeniedTypeDef,
        "authDecision": Literal["ALLOWED", "EXPLICIT_DENY", "IMPLICIT_DENY"],
        "missingContextValues": List[str],
    },
    total=False,
)


class ClientTestAuthorizationResponseauthResultsTypeDef(
    _ClientTestAuthorizationResponseauthResultsTypeDef
):
    """
    - *(dict) --*

      The authorizer result.
      - **authInfo** *(dict) --*

        Authorization information.
        - **actionType** *(string) --*

          The type of action for which the principal is being authorized.
    """


_ClientTestAuthorizationResponseTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseTypeDef",
    {"authResults": List[ClientTestAuthorizationResponseauthResultsTypeDef]},
    total=False,
)


class ClientTestAuthorizationResponseTypeDef(_ClientTestAuthorizationResponseTypeDef):
    """
    - *(dict) --*

      - **authResults** *(list) --*

        The authentication results.
        - *(dict) --*

          The authorizer result.
          - **authInfo** *(dict) --*

            Authorization information.
            - **actionType** *(string) --*

              The type of action for which the principal is being authorized.
    """


_ClientTestInvokeAuthorizerHttpContextTypeDef = TypedDict(
    "_ClientTestInvokeAuthorizerHttpContextTypeDef",
    {"headers": Dict[str, str], "queryString": str},
    total=False,
)


class ClientTestInvokeAuthorizerHttpContextTypeDef(_ClientTestInvokeAuthorizerHttpContextTypeDef):
    """
    Specifies a test HTTP authorization request.
    - **headers** *(dict) --*

      The header keys and values in an HTTP authorization request.
      - *(string) --*

        - *(string) --*
    """


_ClientTestInvokeAuthorizerMqttContextTypeDef = TypedDict(
    "_ClientTestInvokeAuthorizerMqttContextTypeDef",
    {"username": str, "password": bytes, "clientId": str},
    total=False,
)


class ClientTestInvokeAuthorizerMqttContextTypeDef(_ClientTestInvokeAuthorizerMqttContextTypeDef):
    """
    Specifies a test MQTT authorization request.>
    - **username** *(string) --*

      The value of the ``username`` key in an MQTT authorization request.
    """


_ClientTestInvokeAuthorizerResponseTypeDef = TypedDict(
    "_ClientTestInvokeAuthorizerResponseTypeDef",
    {
        "isAuthenticated": bool,
        "principalId": str,
        "policyDocuments": List[str],
        "refreshAfterInSeconds": int,
        "disconnectAfterInSeconds": int,
    },
    total=False,
)


class ClientTestInvokeAuthorizerResponseTypeDef(_ClientTestInvokeAuthorizerResponseTypeDef):
    """
    - *(dict) --*

      - **isAuthenticated** *(boolean) --*

        True if the token is authenticated, otherwise false.
    """


_ClientTestInvokeAuthorizerTlsContextTypeDef = TypedDict(
    "_ClientTestInvokeAuthorizerTlsContextTypeDef", {"serverName": str}, total=False
)


class ClientTestInvokeAuthorizerTlsContextTypeDef(_ClientTestInvokeAuthorizerTlsContextTypeDef):
    """
    Specifies a test TLS authorization request.
    - **serverName** *(string) --*

      The value of the ``serverName`` key in a TLS authorization request.
    """


_ClientTransferCertificateResponseTypeDef = TypedDict(
    "_ClientTransferCertificateResponseTypeDef", {"transferredCertificateArn": str}, total=False
)


class ClientTransferCertificateResponseTypeDef(_ClientTransferCertificateResponseTypeDef):
    """
    - *(dict) --*

      The output from the TransferCertificate operation.
      - **transferredCertificateArn** *(string) --*

        The ARN of the certificate.
    """


_ClientUpdateAccountAuditConfigurationAuditCheckConfigurationsTypeDef = TypedDict(
    "_ClientUpdateAccountAuditConfigurationAuditCheckConfigurationsTypeDef",
    {"enabled": bool},
    total=False,
)


class ClientUpdateAccountAuditConfigurationAuditCheckConfigurationsTypeDef(
    _ClientUpdateAccountAuditConfigurationAuditCheckConfigurationsTypeDef
):
    pass


_ClientUpdateAccountAuditConfigurationAuditNotificationTargetConfigurationsTypeDef = TypedDict(
    "_ClientUpdateAccountAuditConfigurationAuditNotificationTargetConfigurationsTypeDef",
    {"targetArn": str, "roleArn": str, "enabled": bool},
    total=False,
)


class ClientUpdateAccountAuditConfigurationAuditNotificationTargetConfigurationsTypeDef(
    _ClientUpdateAccountAuditConfigurationAuditNotificationTargetConfigurationsTypeDef
):
    pass


_ClientUpdateAuthorizerResponseTypeDef = TypedDict(
    "_ClientUpdateAuthorizerResponseTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)


class ClientUpdateAuthorizerResponseTypeDef(_ClientUpdateAuthorizerResponseTypeDef):
    """
    - *(dict) --*

      - **authorizerName** *(string) --*

        The authorizer name.
    """


_ClientUpdateBillingGroupBillingGroupPropertiesTypeDef = TypedDict(
    "_ClientUpdateBillingGroupBillingGroupPropertiesTypeDef",
    {"billingGroupDescription": str},
    total=False,
)


class ClientUpdateBillingGroupBillingGroupPropertiesTypeDef(
    _ClientUpdateBillingGroupBillingGroupPropertiesTypeDef
):
    """
    The properties of the billing group.
    - **billingGroupDescription** *(string) --*

      The description of the billing group.
    """


_ClientUpdateBillingGroupResponseTypeDef = TypedDict(
    "_ClientUpdateBillingGroupResponseTypeDef", {"version": int}, total=False
)


class ClientUpdateBillingGroupResponseTypeDef(_ClientUpdateBillingGroupResponseTypeDef):
    """
    - *(dict) --*

      - **version** *(integer) --*

        The latest version of the billing group.
    """


_ClientUpdateCaCertificateRegistrationConfigTypeDef = TypedDict(
    "_ClientUpdateCaCertificateRegistrationConfigTypeDef",
    {"templateBody": str, "roleArn": str},
    total=False,
)


class ClientUpdateCaCertificateRegistrationConfigTypeDef(
    _ClientUpdateCaCertificateRegistrationConfigTypeDef
):
    """
    Information about the registration configuration.
    - **templateBody** *(string) --*

      The template body.
    """


_ClientUpdateDomainConfigurationAuthorizerConfigTypeDef = TypedDict(
    "_ClientUpdateDomainConfigurationAuthorizerConfigTypeDef",
    {"defaultAuthorizerName": str, "allowAuthorizerOverride": bool},
    total=False,
)


class ClientUpdateDomainConfigurationAuthorizerConfigTypeDef(
    _ClientUpdateDomainConfigurationAuthorizerConfigTypeDef
):
    """
    An object that specifies the authorization service for a domain.
    - **defaultAuthorizerName** *(string) --*

      The name of the authorization service for a domain configuration.
    """


_ClientUpdateDomainConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateDomainConfigurationResponseTypeDef",
    {"domainConfigurationName": str, "domainConfigurationArn": str},
    total=False,
)


class ClientUpdateDomainConfigurationResponseTypeDef(
    _ClientUpdateDomainConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **domainConfigurationName** *(string) --*

        The name of the domain configuration that was updated.
    """


_ClientUpdateDynamicThingGroupResponseTypeDef = TypedDict(
    "_ClientUpdateDynamicThingGroupResponseTypeDef", {"version": int}, total=False
)


class ClientUpdateDynamicThingGroupResponseTypeDef(_ClientUpdateDynamicThingGroupResponseTypeDef):
    """
    - *(dict) --*

      - **version** *(integer) --*

        The dynamic thing group version.
    """


_ClientUpdateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "_ClientUpdateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientUpdateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef(
    _ClientUpdateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef
):
    pass


_ClientUpdateDynamicThingGroupThingGroupPropertiesTypeDef = TypedDict(
    "_ClientUpdateDynamicThingGroupThingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientUpdateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)


class ClientUpdateDynamicThingGroupThingGroupPropertiesTypeDef(
    _ClientUpdateDynamicThingGroupThingGroupPropertiesTypeDef
):
    """
    The dynamic thing group properties to update.
    - **thingGroupDescription** *(string) --*

      The thing group description.
    """


_ClientUpdateEventConfigurationsEventConfigurationsTypeDef = TypedDict(
    "_ClientUpdateEventConfigurationsEventConfigurationsTypeDef", {"Enabled": bool}, total=False
)


class ClientUpdateEventConfigurationsEventConfigurationsTypeDef(
    _ClientUpdateEventConfigurationsEventConfigurationsTypeDef
):
    pass


_ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationcustomFieldsTypeDef = TypedDict(
    "_ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationcustomFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)


class ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationcustomFieldsTypeDef(
    _ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationcustomFieldsTypeDef
):
    pass


_ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationmanagedFieldsTypeDef = TypedDict(
    "_ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationmanagedFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)


class ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationmanagedFieldsTypeDef(
    _ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationmanagedFieldsTypeDef
):
    pass


_RequiredClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef",
    {"thingGroupIndexingMode": Literal["OFF", "ON"]},
)
_OptionalClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef",
    {
        "managedFields": List[
            ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationmanagedFieldsTypeDef
        ],
        "customFields": List[
            ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationcustomFieldsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef(
    _RequiredClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef,
    _OptionalClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef,
):
    """
    Thing group indexing configuration.
    - **thingGroupIndexingMode** *(string) --***[REQUIRED]**

      Thing group indexing mode.
    """


_ClientUpdateIndexingConfigurationThingIndexingConfigurationcustomFieldsTypeDef = TypedDict(
    "_ClientUpdateIndexingConfigurationThingIndexingConfigurationcustomFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)


class ClientUpdateIndexingConfigurationThingIndexingConfigurationcustomFieldsTypeDef(
    _ClientUpdateIndexingConfigurationThingIndexingConfigurationcustomFieldsTypeDef
):
    pass


_ClientUpdateIndexingConfigurationThingIndexingConfigurationmanagedFieldsTypeDef = TypedDict(
    "_ClientUpdateIndexingConfigurationThingIndexingConfigurationmanagedFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)


class ClientUpdateIndexingConfigurationThingIndexingConfigurationmanagedFieldsTypeDef(
    _ClientUpdateIndexingConfigurationThingIndexingConfigurationmanagedFieldsTypeDef
):
    pass


_RequiredClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef",
    {"thingIndexingMode": Literal["OFF", "REGISTRY", "REGISTRY_AND_SHADOW"]},
)
_OptionalClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef",
    {
        "thingConnectivityIndexingMode": Literal["OFF", "STATUS"],
        "managedFields": List[
            ClientUpdateIndexingConfigurationThingIndexingConfigurationmanagedFieldsTypeDef
        ],
        "customFields": List[
            ClientUpdateIndexingConfigurationThingIndexingConfigurationcustomFieldsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef(
    _RequiredClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef,
    _OptionalClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef,
):
    """
    Thing indexing configuration.
    - **thingIndexingMode** *(string) --***[REQUIRED]**

      Thing indexing mode. Valid values are:
      * REGISTRY – Your thing index contains registry data only.
      * REGISTRY_AND_SHADOW - Your thing index contains registry and shadow data.
      * OFF - Thing indexing is disabled.
    """


_RequiredClientUpdateJobAbortConfigcriteriaListTypeDef = TypedDict(
    "_RequiredClientUpdateJobAbortConfigcriteriaListTypeDef",
    {"failureType": Literal["FAILED", "REJECTED", "TIMED_OUT", "ALL"]},
)
_OptionalClientUpdateJobAbortConfigcriteriaListTypeDef = TypedDict(
    "_OptionalClientUpdateJobAbortConfigcriteriaListTypeDef",
    {"action": str, "thresholdPercentage": float, "minNumberOfExecutedThings": int},
    total=False,
)


class ClientUpdateJobAbortConfigcriteriaListTypeDef(
    _RequiredClientUpdateJobAbortConfigcriteriaListTypeDef,
    _OptionalClientUpdateJobAbortConfigcriteriaListTypeDef,
):
    """
    - *(dict) --*

      Details of abort criteria to define rules to abort the job.
      - **failureType** *(string) --***[REQUIRED]**

        The type of job execution failure to define a rule to initiate a job abort.
    """


_ClientUpdateJobAbortConfigTypeDef = TypedDict(
    "_ClientUpdateJobAbortConfigTypeDef",
    {"criteriaList": List[ClientUpdateJobAbortConfigcriteriaListTypeDef]},
)


class ClientUpdateJobAbortConfigTypeDef(_ClientUpdateJobAbortConfigTypeDef):
    """
    Allows you to create criteria to abort a job.
    - **criteriaList** *(list) --***[REQUIRED]**

      The list of abort criteria to define rules to abort the job.
      - *(dict) --*

        Details of abort criteria to define rules to abort the job.
        - **failureType** *(string) --***[REQUIRED]**

          The type of job execution failure to define a rule to initiate a job abort.
    """


_ClientUpdateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef = TypedDict(
    "_ClientUpdateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef",
    {"numberOfNotifiedThings": int, "numberOfSucceededThings": int},
    total=False,
)


class ClientUpdateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef(
    _ClientUpdateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef
):
    pass


_ClientUpdateJobJobExecutionsRolloutConfigexponentialRateTypeDef = TypedDict(
    "_ClientUpdateJobJobExecutionsRolloutConfigexponentialRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": ClientUpdateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef,
    },
    total=False,
)


class ClientUpdateJobJobExecutionsRolloutConfigexponentialRateTypeDef(
    _ClientUpdateJobJobExecutionsRolloutConfigexponentialRateTypeDef
):
    pass


_ClientUpdateJobJobExecutionsRolloutConfigTypeDef = TypedDict(
    "_ClientUpdateJobJobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": ClientUpdateJobJobExecutionsRolloutConfigexponentialRateTypeDef,
    },
    total=False,
)


class ClientUpdateJobJobExecutionsRolloutConfigTypeDef(
    _ClientUpdateJobJobExecutionsRolloutConfigTypeDef
):
    """
    Allows you to create a staged rollout of the job.
    - **maximumPerMinute** *(integer) --*

      The maximum number of things that will be notified of a pending job, per minute. This
      parameter allows you to create a staged rollout.
    """


_ClientUpdateJobPresignedUrlConfigTypeDef = TypedDict(
    "_ClientUpdateJobPresignedUrlConfigTypeDef", {"roleArn": str, "expiresInSec": int}, total=False
)


class ClientUpdateJobPresignedUrlConfigTypeDef(_ClientUpdateJobPresignedUrlConfigTypeDef):
    """
    Configuration information for pre-signed S3 URLs.
    - **roleArn** *(string) --*

      The ARN of an IAM role that grants grants permission to download files from the S3 bucket
      where the job data/updates are stored. The role must also grant permission for IoT to download
      the files.
    """


_ClientUpdateJobTimeoutConfigTypeDef = TypedDict(
    "_ClientUpdateJobTimeoutConfigTypeDef", {"inProgressTimeoutInMinutes": int}, total=False
)


class ClientUpdateJobTimeoutConfigTypeDef(_ClientUpdateJobTimeoutConfigTypeDef):
    """
    Specifies the amount of time each device has to finish its execution of the job. The timer is
    started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is
    not set to another terminal state before the time expires, it will be automatically set to
    ``TIMED_OUT`` .
    - **inProgressTimeoutInMinutes** *(integer) --*

      Specifies the amount of time, in minutes, this device has to finish execution of this job. The
      timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in
      progress timer can't be updated and will apply to all job executions for the job. Whenever a
      job execution remains in the IN_PROGRESS status for longer than this interval, the job
      execution will fail and switch to the terminal ``TIMED_OUT`` status.
    """


_ClientUpdateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "_ClientUpdateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef",
    {"thingGroupNames": List[str], "overrideDynamicGroups": bool},
    total=False,
)


class ClientUpdateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef(
    _ClientUpdateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef
):
    pass


_ClientUpdateMitigationActionActionParamsenableIoTLoggingParamsTypeDef = TypedDict(
    "_ClientUpdateMitigationActionActionParamsenableIoTLoggingParamsTypeDef",
    {"roleArnForLogging": str, "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"]},
    total=False,
)


class ClientUpdateMitigationActionActionParamsenableIoTLoggingParamsTypeDef(
    _ClientUpdateMitigationActionActionParamsenableIoTLoggingParamsTypeDef
):
    pass


_ClientUpdateMitigationActionActionParamspublishFindingToSnsParamsTypeDef = TypedDict(
    "_ClientUpdateMitigationActionActionParamspublishFindingToSnsParamsTypeDef",
    {"topicArn": str},
    total=False,
)


class ClientUpdateMitigationActionActionParamspublishFindingToSnsParamsTypeDef(
    _ClientUpdateMitigationActionActionParamspublishFindingToSnsParamsTypeDef
):
    pass


_ClientUpdateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "_ClientUpdateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    {"templateName": str},
    total=False,
)


class ClientUpdateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef(
    _ClientUpdateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef
):
    pass


_ClientUpdateMitigationActionActionParamsupdateCACertificateParamsTypeDef = TypedDict(
    "_ClientUpdateMitigationActionActionParamsupdateCACertificateParamsTypeDef",
    {"action": str},
    total=False,
)


class ClientUpdateMitigationActionActionParamsupdateCACertificateParamsTypeDef(
    _ClientUpdateMitigationActionActionParamsupdateCACertificateParamsTypeDef
):
    pass


_ClientUpdateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef = TypedDict(
    "_ClientUpdateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef", {"action": str}
)


class ClientUpdateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef(
    _ClientUpdateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef
):
    """
    - **updateDeviceCertificateParams** *(dict) --*

      Parameters to define a mitigation action that changes the state of the device certificate to
      inactive.
      - **action** *(string) --***[REQUIRED]**

        The action that you want to apply to the device cerrtificate. The only supported value is
        ``DEACTIVATE`` .
    """


_ClientUpdateMitigationActionActionParamsTypeDef = TypedDict(
    "_ClientUpdateMitigationActionActionParamsTypeDef",
    {
        "updateDeviceCertificateParams": ClientUpdateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef,
        "updateCACertificateParams": ClientUpdateMitigationActionActionParamsupdateCACertificateParamsTypeDef,
        "addThingsToThingGroupParams": ClientUpdateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef,
        "replaceDefaultPolicyVersionParams": ClientUpdateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef,
        "enableIoTLoggingParams": ClientUpdateMitigationActionActionParamsenableIoTLoggingParamsTypeDef,
        "publishFindingToSnsParams": ClientUpdateMitigationActionActionParamspublishFindingToSnsParamsTypeDef,
    },
    total=False,
)


class ClientUpdateMitigationActionActionParamsTypeDef(
    _ClientUpdateMitigationActionActionParamsTypeDef
):
    """
    Defines the type of action and the parameters for that action.
    - **updateDeviceCertificateParams** *(dict) --*

      Parameters to define a mitigation action that changes the state of the device certificate to
      inactive.
      - **action** *(string) --***[REQUIRED]**

        The action that you want to apply to the device cerrtificate. The only supported value is
        ``DEACTIVATE`` .
    """


_ClientUpdateMitigationActionResponseTypeDef = TypedDict(
    "_ClientUpdateMitigationActionResponseTypeDef", {"actionArn": str, "actionId": str}, total=False
)


class ClientUpdateMitigationActionResponseTypeDef(_ClientUpdateMitigationActionResponseTypeDef):
    """
    - *(dict) --*

      - **actionArn** *(string) --*

        The ARN for the new mitigation action.
    """


_ClientUpdateRoleAliasResponseTypeDef = TypedDict(
    "_ClientUpdateRoleAliasResponseTypeDef", {"roleAlias": str, "roleAliasArn": str}, total=False
)


class ClientUpdateRoleAliasResponseTypeDef(_ClientUpdateRoleAliasResponseTypeDef):
    """
    - *(dict) --*

      - **roleAlias** *(string) --*

        The role alias.
    """


_ClientUpdateScheduledAuditResponseTypeDef = TypedDict(
    "_ClientUpdateScheduledAuditResponseTypeDef", {"scheduledAuditArn": str}, total=False
)


class ClientUpdateScheduledAuditResponseTypeDef(_ClientUpdateScheduledAuditResponseTypeDef):
    """
    - *(dict) --*

      - **scheduledAuditArn** *(string) --*

        The ARN of the scheduled audit.
    """


_ClientUpdateSecurityProfileAlertTargetsTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileAlertTargetsTypeDef",
    {"alertTargetArn": str, "roleArn": str},
    total=False,
)


class ClientUpdateSecurityProfileAlertTargetsTypeDef(
    _ClientUpdateSecurityProfileAlertTargetsTypeDef
):
    pass


_ClientUpdateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientUpdateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef(
    _ClientUpdateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef
):
    pass


_ClientUpdateSecurityProfileBehaviorscriteriavalueTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileBehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientUpdateSecurityProfileBehaviorscriteriavalueTypeDef(
    _ClientUpdateSecurityProfileBehaviorscriteriavalueTypeDef
):
    pass


_ClientUpdateSecurityProfileBehaviorscriteriaTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileBehaviorscriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientUpdateSecurityProfileBehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientUpdateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientUpdateSecurityProfileBehaviorscriteriaTypeDef(
    _ClientUpdateSecurityProfileBehaviorscriteriaTypeDef
):
    pass


_RequiredClientUpdateSecurityProfileBehaviorsTypeDef = TypedDict(
    "_RequiredClientUpdateSecurityProfileBehaviorsTypeDef", {"name": str}
)
_OptionalClientUpdateSecurityProfileBehaviorsTypeDef = TypedDict(
    "_OptionalClientUpdateSecurityProfileBehaviorsTypeDef",
    {"metric": str, "criteria": ClientUpdateSecurityProfileBehaviorscriteriaTypeDef},
    total=False,
)


class ClientUpdateSecurityProfileBehaviorsTypeDef(
    _RequiredClientUpdateSecurityProfileBehaviorsTypeDef,
    _OptionalClientUpdateSecurityProfileBehaviorsTypeDef,
):
    """
    - *(dict) --*

      A Device Defender security profile behavior.
      - **name** *(string) --***[REQUIRED]**

        The name you have given to the behavior.
    """


_ClientUpdateSecurityProfileResponsealertTargetsTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileResponsealertTargetsTypeDef",
    {"alertTargetArn": str, "roleArn": str},
    total=False,
)


class ClientUpdateSecurityProfileResponsealertTargetsTypeDef(
    _ClientUpdateSecurityProfileResponsealertTargetsTypeDef
):
    pass


_ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef(
    _ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef
):
    pass


_ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef(
    _ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef
):
    pass


_ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef(
    _ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef
):
    pass


_ClientUpdateSecurityProfileResponsebehaviorsTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileResponsebehaviorsTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef,
    },
    total=False,
)


class ClientUpdateSecurityProfileResponsebehaviorsTypeDef(
    _ClientUpdateSecurityProfileResponsebehaviorsTypeDef
):
    pass


_ClientUpdateSecurityProfileResponseTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "securityProfileDescription": str,
        "behaviors": List[ClientUpdateSecurityProfileResponsebehaviorsTypeDef],
        "alertTargets": Dict[str, ClientUpdateSecurityProfileResponsealertTargetsTypeDef],
        "additionalMetricsToRetain": List[str],
        "version": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class ClientUpdateSecurityProfileResponseTypeDef(_ClientUpdateSecurityProfileResponseTypeDef):
    """
    - *(dict) --*

      - **securityProfileName** *(string) --*

        The name of the security profile that was updated.
    """


_ClientUpdateStreamFiless3LocationTypeDef = TypedDict(
    "_ClientUpdateStreamFiless3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)


class ClientUpdateStreamFiless3LocationTypeDef(_ClientUpdateStreamFiless3LocationTypeDef):
    pass


_ClientUpdateStreamFilesTypeDef = TypedDict(
    "_ClientUpdateStreamFilesTypeDef",
    {"fileId": int, "s3Location": ClientUpdateStreamFiless3LocationTypeDef},
    total=False,
)


class ClientUpdateStreamFilesTypeDef(_ClientUpdateStreamFilesTypeDef):
    """
    - *(dict) --*

      Represents a file to stream.
      - **fileId** *(integer) --*

        The file ID.
    """


_ClientUpdateStreamResponseTypeDef = TypedDict(
    "_ClientUpdateStreamResponseTypeDef",
    {"streamId": str, "streamArn": str, "description": str, "streamVersion": int},
    total=False,
)


class ClientUpdateStreamResponseTypeDef(_ClientUpdateStreamResponseTypeDef):
    """
    - *(dict) --*

      - **streamId** *(string) --*

        The stream ID.
    """


_ClientUpdateThingAttributePayloadTypeDef = TypedDict(
    "_ClientUpdateThingAttributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientUpdateThingAttributePayloadTypeDef(_ClientUpdateThingAttributePayloadTypeDef):
    """
    A list of thing attributes, a JSON string containing name-value pairs. For example:

      ``{\\"attributes\\":{\\"name1\\":\\"value2\\"}}``
    """


_ClientUpdateThingGroupResponseTypeDef = TypedDict(
    "_ClientUpdateThingGroupResponseTypeDef", {"version": int}, total=False
)


class ClientUpdateThingGroupResponseTypeDef(_ClientUpdateThingGroupResponseTypeDef):
    """
    - *(dict) --*

      - **version** *(integer) --*

        The version of the updated thing group.
    """


_ClientUpdateThingGroupThingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "_ClientUpdateThingGroupThingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientUpdateThingGroupThingGroupPropertiesattributePayloadTypeDef(
    _ClientUpdateThingGroupThingGroupPropertiesattributePayloadTypeDef
):
    pass


_ClientUpdateThingGroupThingGroupPropertiesTypeDef = TypedDict(
    "_ClientUpdateThingGroupThingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientUpdateThingGroupThingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)


class ClientUpdateThingGroupThingGroupPropertiesTypeDef(
    _ClientUpdateThingGroupThingGroupPropertiesTypeDef
):
    """
    The thing group properties.
    - **thingGroupDescription** *(string) --*

      The thing group description.
    """


_ClientValidateSecurityProfileBehaviorsBehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientValidateSecurityProfileBehaviorsBehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientValidateSecurityProfileBehaviorsBehaviorscriteriastatisticalThresholdTypeDef(
    _ClientValidateSecurityProfileBehaviorsBehaviorscriteriastatisticalThresholdTypeDef
):
    pass


_ClientValidateSecurityProfileBehaviorsBehaviorscriteriavalueTypeDef = TypedDict(
    "_ClientValidateSecurityProfileBehaviorsBehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientValidateSecurityProfileBehaviorsBehaviorscriteriavalueTypeDef(
    _ClientValidateSecurityProfileBehaviorsBehaviorscriteriavalueTypeDef
):
    pass


_ClientValidateSecurityProfileBehaviorsBehaviorscriteriaTypeDef = TypedDict(
    "_ClientValidateSecurityProfileBehaviorsBehaviorscriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientValidateSecurityProfileBehaviorsBehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientValidateSecurityProfileBehaviorsBehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientValidateSecurityProfileBehaviorsBehaviorscriteriaTypeDef(
    _ClientValidateSecurityProfileBehaviorsBehaviorscriteriaTypeDef
):
    pass


_RequiredClientValidateSecurityProfileBehaviorsBehaviorsTypeDef = TypedDict(
    "_RequiredClientValidateSecurityProfileBehaviorsBehaviorsTypeDef", {"name": str}
)
_OptionalClientValidateSecurityProfileBehaviorsBehaviorsTypeDef = TypedDict(
    "_OptionalClientValidateSecurityProfileBehaviorsBehaviorsTypeDef",
    {"metric": str, "criteria": ClientValidateSecurityProfileBehaviorsBehaviorscriteriaTypeDef},
    total=False,
)


class ClientValidateSecurityProfileBehaviorsBehaviorsTypeDef(
    _RequiredClientValidateSecurityProfileBehaviorsBehaviorsTypeDef,
    _OptionalClientValidateSecurityProfileBehaviorsBehaviorsTypeDef,
):
    """
    - *(dict) --*

      A Device Defender security profile behavior.
      - **name** *(string) --***[REQUIRED]**

        The name you have given to the behavior.
    """


_ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef = TypedDict(
    "_ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef",
    {"errorMessage": str},
    total=False,
)


class ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef(
    _ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef
):
    pass


_ClientValidateSecurityProfileBehaviorsResponseTypeDef = TypedDict(
    "_ClientValidateSecurityProfileBehaviorsResponseTypeDef",
    {
        "valid": bool,
        "validationErrors": List[
            ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef
        ],
    },
    total=False,
)


class ClientValidateSecurityProfileBehaviorsResponseTypeDef(
    _ClientValidateSecurityProfileBehaviorsResponseTypeDef
):
    """
    - *(dict) --*

      - **valid** *(boolean) --*

        True if the behaviors were valid.
    """


_ListActiveViolationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListActiveViolationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListActiveViolationsPaginatePaginationConfigTypeDef(
    _ListActiveViolationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef(
    _ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef
):
    pass


_ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef(
    _ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef
):
    pass


_ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef(
    _ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef
):
    pass


_ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef,
    },
    total=False,
)


class ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef(
    _ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef
):
    pass


_ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef(
    _ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef
):
    pass


_ListActiveViolationsPaginateResponseactiveViolationsTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseactiveViolationsTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef,
        "lastViolationValue": ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef,
        "lastViolationTime": datetime,
        "violationStartTime": datetime,
    },
    total=False,
)


class ListActiveViolationsPaginateResponseactiveViolationsTypeDef(
    _ListActiveViolationsPaginateResponseactiveViolationsTypeDef
):
    """
    - *(dict) --*

      Information about an active Device Defender security profile behavior violation.
      - **violationId** *(string) --*

        The ID of the active violation.
    """


_ListActiveViolationsPaginateResponseTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseTypeDef",
    {
        "activeViolations": List[ListActiveViolationsPaginateResponseactiveViolationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListActiveViolationsPaginateResponseTypeDef(_ListActiveViolationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **activeViolations** *(list) --*

        The list of active violations.
        - *(dict) --*

          Information about an active Device Defender security profile behavior violation.
          - **violationId** *(string) --*

            The ID of the active violation.
    """


_ListAttachedPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAttachedPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAttachedPoliciesPaginatePaginationConfigTypeDef(
    _ListAttachedPoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAttachedPoliciesPaginateResponsepoliciesTypeDef = TypedDict(
    "_ListAttachedPoliciesPaginateResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ListAttachedPoliciesPaginateResponsepoliciesTypeDef(
    _ListAttachedPoliciesPaginateResponsepoliciesTypeDef
):
    """
    - *(dict) --*

      Describes an AWS IoT policy.
      - **policyName** *(string) --*

        The policy name.
    """


_ListAttachedPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListAttachedPoliciesPaginateResponseTypeDef",
    {"policies": List[ListAttachedPoliciesPaginateResponsepoliciesTypeDef], "NextToken": str},
    total=False,
)


class ListAttachedPoliciesPaginateResponseTypeDef(_ListAttachedPoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **policies** *(list) --*

        The policies.
        - *(dict) --*

          Describes an AWS IoT policy.
          - **policyName** *(string) --*

            The policy name.
    """


_ListAuditFindingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAuditFindingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAuditFindingsPaginatePaginationConfigTypeDef(
    _ListAuditFindingsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAuditFindingsPaginateResourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ListAuditFindingsPaginateResourceIdentifierpolicyVersionIdentifierTypeDef(
    _ListAuditFindingsPaginateResourceIdentifierpolicyVersionIdentifierTypeDef
):
    pass


_ListAuditFindingsPaginateResourceIdentifierTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ListAuditFindingsPaginateResourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)


class ListAuditFindingsPaginateResourceIdentifierTypeDef(
    _ListAuditFindingsPaginateResourceIdentifierTypeDef
):
    """
    Information identifying the noncompliant resource.
    - **deviceCertificateId** *(string) --*

      The ID of the certificate attached to the resource.
    """


_ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef
):
    pass


_ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef(
    _ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef
):
    pass


_ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef",
    {
        "resourceType": Literal[
            "DEVICE_CERTIFICATE",
            "CA_CERTIFICATE",
            "IOT_POLICY",
            "COGNITO_IDENTITY_POOL",
            "CLIENT_ID",
            "ACCOUNT_SETTINGS",
            "ROLE_ALIAS",
            "IAM_ROLE",
        ],
        "resourceIdentifier": ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef(
    _ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef
):
    pass


_ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef
):
    pass


_ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef(
    _ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef
):
    pass


_ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef",
    {
        "resourceType": Literal[
            "DEVICE_CERTIFICATE",
            "CA_CERTIFICATE",
            "IOT_POLICY",
            "COGNITO_IDENTITY_POOL",
            "CLIENT_ID",
            "ACCOUNT_SETTINGS",
            "ROLE_ALIAS",
            "IAM_ROLE",
        ],
        "resourceIdentifier": ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef(
    _ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef
):
    pass


_ListAuditFindingsPaginateResponsefindingsTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsTypeDef",
    {
        "findingId": str,
        "taskId": str,
        "checkName": str,
        "taskStartTime": datetime,
        "findingTime": datetime,
        "severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"],
        "nonCompliantResource": ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef,
        "relatedResources": List[ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef],
        "reasonForNonCompliance": str,
        "reasonForNonComplianceCode": str,
    },
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsTypeDef(
    _ListAuditFindingsPaginateResponsefindingsTypeDef
):
    """
    - *(dict) --*

      The findings (results) of the audit.
      - **findingId** *(string) --*

        A unique identifier for this set of audit findings. This identifier is used to apply
        mitigation tasks to one or more sets of findings.
    """


_ListAuditFindingsPaginateResponseTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponseTypeDef",
    {"findings": List[ListAuditFindingsPaginateResponsefindingsTypeDef], "NextToken": str},
    total=False,
)


class ListAuditFindingsPaginateResponseTypeDef(_ListAuditFindingsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **findings** *(list) --*

        The findings (results) of the audit.
        - *(dict) --*

          The findings (results) of the audit.
          - **findingId** *(string) --*

            A unique identifier for this set of audit findings. This identifier is used to apply
            mitigation tasks to one or more sets of findings.
    """


_ListAuditTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAuditTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAuditTasksPaginatePaginationConfigTypeDef(_ListAuditTasksPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAuditTasksPaginateResponsetasksTypeDef = TypedDict(
    "_ListAuditTasksPaginateResponsetasksTypeDef",
    {
        "taskId": str,
        "taskStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"],
        "taskType": Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"],
    },
    total=False,
)


class ListAuditTasksPaginateResponsetasksTypeDef(_ListAuditTasksPaginateResponsetasksTypeDef):
    """
    - *(dict) --*

      The audits that were performed.
      - **taskId** *(string) --*

        The ID of this audit.
    """


_ListAuditTasksPaginateResponseTypeDef = TypedDict(
    "_ListAuditTasksPaginateResponseTypeDef",
    {"tasks": List[ListAuditTasksPaginateResponsetasksTypeDef], "NextToken": str},
    total=False,
)


class ListAuditTasksPaginateResponseTypeDef(_ListAuditTasksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **tasks** *(list) --*

        The audits that were performed during the specified time period.
        - *(dict) --*

          The audits that were performed.
          - **taskId** *(string) --*

            The ID of this audit.
    """


_ListAuthorizersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAuthorizersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAuthorizersPaginatePaginationConfigTypeDef(
    _ListAuthorizersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAuthorizersPaginateResponseauthorizersTypeDef = TypedDict(
    "_ListAuthorizersPaginateResponseauthorizersTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)


class ListAuthorizersPaginateResponseauthorizersTypeDef(
    _ListAuthorizersPaginateResponseauthorizersTypeDef
):
    """
    - *(dict) --*

      The authorizer summary.
      - **authorizerName** *(string) --*

        The authorizer name.
    """


_ListAuthorizersPaginateResponseTypeDef = TypedDict(
    "_ListAuthorizersPaginateResponseTypeDef",
    {"authorizers": List[ListAuthorizersPaginateResponseauthorizersTypeDef], "NextToken": str},
    total=False,
)


class ListAuthorizersPaginateResponseTypeDef(_ListAuthorizersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **authorizers** *(list) --*

        The authorizers.
        - *(dict) --*

          The authorizer summary.
          - **authorizerName** *(string) --*

            The authorizer name.
    """


_ListBillingGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBillingGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBillingGroupsPaginatePaginationConfigTypeDef(
    _ListBillingGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBillingGroupsPaginateResponsebillingGroupsTypeDef = TypedDict(
    "_ListBillingGroupsPaginateResponsebillingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ListBillingGroupsPaginateResponsebillingGroupsTypeDef(
    _ListBillingGroupsPaginateResponsebillingGroupsTypeDef
):
    """
    - *(dict) --*

      The name and ARN of a group.
      - **groupName** *(string) --*

        The group name.
    """


_ListBillingGroupsPaginateResponseTypeDef = TypedDict(
    "_ListBillingGroupsPaginateResponseTypeDef",
    {
        "billingGroups": List[ListBillingGroupsPaginateResponsebillingGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListBillingGroupsPaginateResponseTypeDef(_ListBillingGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **billingGroups** *(list) --*

        The list of billing groups.
        - *(dict) --*

          The name and ARN of a group.
          - **groupName** *(string) --*

            The group name.
    """


_ListCACertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCACertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCACertificatesPaginatePaginationConfigTypeDef(
    _ListCACertificatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCACertificatesPaginateResponsecertificatesTypeDef = TypedDict(
    "_ListCACertificatesPaginateResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal["ACTIVE", "INACTIVE"],
        "creationDate": datetime,
    },
    total=False,
)


class ListCACertificatesPaginateResponsecertificatesTypeDef(
    _ListCACertificatesPaginateResponsecertificatesTypeDef
):
    """
    - *(dict) --*

      A CA certificate.
      - **certificateArn** *(string) --*

        The ARN of the CA certificate.
    """


_ListCACertificatesPaginateResponseTypeDef = TypedDict(
    "_ListCACertificatesPaginateResponseTypeDef",
    {"certificates": List[ListCACertificatesPaginateResponsecertificatesTypeDef], "NextToken": str},
    total=False,
)


class ListCACertificatesPaginateResponseTypeDef(_ListCACertificatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListCACertificates operation.
      - **certificates** *(list) --*

        The CA certificates registered in your AWS account.
        - *(dict) --*

          A CA certificate.
          - **certificateArn** *(string) --*

            The ARN of the CA certificate.
    """


_ListCertificatesByCAPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCertificatesByCAPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCertificatesByCAPaginatePaginationConfigTypeDef(
    _ListCertificatesByCAPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCertificatesByCAPaginateResponsecertificatesTypeDef = TypedDict(
    "_ListCertificatesByCAPaginateResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ],
        "creationDate": datetime,
    },
    total=False,
)


class ListCertificatesByCAPaginateResponsecertificatesTypeDef(
    _ListCertificatesByCAPaginateResponsecertificatesTypeDef
):
    """
    - *(dict) --*

      Information about a certificate.
      - **certificateArn** *(string) --*

        The ARN of the certificate.
    """


_ListCertificatesByCAPaginateResponseTypeDef = TypedDict(
    "_ListCertificatesByCAPaginateResponseTypeDef",
    {
        "certificates": List[ListCertificatesByCAPaginateResponsecertificatesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListCertificatesByCAPaginateResponseTypeDef(_ListCertificatesByCAPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output of the ListCertificatesByCA operation.
      - **certificates** *(list) --*

        The device certificates signed by the specified CA certificate.
        - *(dict) --*

          Information about a certificate.
          - **certificateArn** *(string) --*

            The ARN of the certificate.
    """


_ListCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCertificatesPaginatePaginationConfigTypeDef(
    _ListCertificatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCertificatesPaginateResponsecertificatesTypeDef = TypedDict(
    "_ListCertificatesPaginateResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ],
        "creationDate": datetime,
    },
    total=False,
)


class ListCertificatesPaginateResponsecertificatesTypeDef(
    _ListCertificatesPaginateResponsecertificatesTypeDef
):
    """
    - *(dict) --*

      Information about a certificate.
      - **certificateArn** *(string) --*

        The ARN of the certificate.
    """


_ListCertificatesPaginateResponseTypeDef = TypedDict(
    "_ListCertificatesPaginateResponseTypeDef",
    {"certificates": List[ListCertificatesPaginateResponsecertificatesTypeDef], "NextToken": str},
    total=False,
)


class ListCertificatesPaginateResponseTypeDef(_ListCertificatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output of the ListCertificates operation.
      - **certificates** *(list) --*

        The descriptions of the certificates.
        - *(dict) --*

          Information about a certificate.
          - **certificateArn** *(string) --*

            The ARN of the certificate.
    """


_ListIndicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIndicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIndicesPaginatePaginationConfigTypeDef(_ListIndicesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListIndicesPaginateResponseTypeDef = TypedDict(
    "_ListIndicesPaginateResponseTypeDef", {"indexNames": List[str], "NextToken": str}, total=False
)


class ListIndicesPaginateResponseTypeDef(_ListIndicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **indexNames** *(list) --*

        The index names.
        - *(string) --*
    """


_ListJobExecutionsForJobPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobExecutionsForJobPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobExecutionsForJobPaginatePaginationConfigTypeDef(
    _ListJobExecutionsForJobPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef = TypedDict(
    "_ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef",
    {
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)


class ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef(
    _ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef
):
    pass


_ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef = TypedDict(
    "_ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef",
    {
        "thingArn": str,
        "jobExecutionSummary": ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef,
    },
    total=False,
)


class ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef(
    _ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef
):
    """
    - *(dict) --*

      Contains a summary of information about job executions for a specific job.
      - **thingArn** *(string) --*

        The ARN of the thing on which the job execution is running.
    """


_ListJobExecutionsForJobPaginateResponseTypeDef = TypedDict(
    "_ListJobExecutionsForJobPaginateResponseTypeDef",
    {
        "executionSummaries": List[
            ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListJobExecutionsForJobPaginateResponseTypeDef(
    _ListJobExecutionsForJobPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **executionSummaries** *(list) --*

        A list of job execution summaries.
        - *(dict) --*

          Contains a summary of information about job executions for a specific job.
          - **thingArn** *(string) --*

            The ARN of the thing on which the job execution is running.
    """


_ListJobExecutionsForThingPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobExecutionsForThingPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobExecutionsForThingPaginatePaginationConfigTypeDef(
    _ListJobExecutionsForThingPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef = TypedDict(
    "_ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef",
    {
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)


class ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef(
    _ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef
):
    pass


_ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef = TypedDict(
    "_ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef",
    {
        "jobId": str,
        "jobExecutionSummary": ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef,
    },
    total=False,
)


class ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef(
    _ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef
):
    """
    - *(dict) --*

      The job execution summary for a thing.
      - **jobId** *(string) --*

        The unique identifier you assigned to this job when it was created.
    """


_ListJobExecutionsForThingPaginateResponseTypeDef = TypedDict(
    "_ListJobExecutionsForThingPaginateResponseTypeDef",
    {
        "executionSummaries": List[
            ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListJobExecutionsForThingPaginateResponseTypeDef(
    _ListJobExecutionsForThingPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **executionSummaries** *(list) --*

        A list of job execution summaries.
        - *(dict) --*

          The job execution summary for a thing.
          - **jobId** *(string) --*

            The unique identifier you assigned to this job when it was created.
    """


_ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobsPaginatePaginationConfigTypeDef(_ListJobsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListJobsPaginateResponsejobsTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobsTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "thingGroupId": str,
        "targetSelection": Literal["CONTINUOUS", "SNAPSHOT"],
        "status": Literal["IN_PROGRESS", "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
    },
    total=False,
)


class ListJobsPaginateResponsejobsTypeDef(_ListJobsPaginateResponsejobsTypeDef):
    """
    - *(dict) --*

      The job summary.
      - **jobArn** *(string) --*

        The job ARN.
    """


_ListJobsPaginateResponseTypeDef = TypedDict(
    "_ListJobsPaginateResponseTypeDef",
    {"jobs": List[ListJobsPaginateResponsejobsTypeDef], "NextToken": str},
    total=False,
)


class ListJobsPaginateResponseTypeDef(_ListJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **jobs** *(list) --*

        A list of jobs.
        - *(dict) --*

          The job summary.
          - **jobArn** *(string) --*

            The job ARN.
    """


_ListOTAUpdatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOTAUpdatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOTAUpdatesPaginatePaginationConfigTypeDef(_ListOTAUpdatesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListOTAUpdatesPaginateResponseotaUpdatesTypeDef = TypedDict(
    "_ListOTAUpdatesPaginateResponseotaUpdatesTypeDef",
    {"otaUpdateId": str, "otaUpdateArn": str, "creationDate": datetime},
    total=False,
)


class ListOTAUpdatesPaginateResponseotaUpdatesTypeDef(
    _ListOTAUpdatesPaginateResponseotaUpdatesTypeDef
):
    """
    - *(dict) --*

      An OTA update summary.
      - **otaUpdateId** *(string) --*

        The OTA update ID.
    """


_ListOTAUpdatesPaginateResponseTypeDef = TypedDict(
    "_ListOTAUpdatesPaginateResponseTypeDef",
    {"otaUpdates": List[ListOTAUpdatesPaginateResponseotaUpdatesTypeDef], "NextToken": str},
    total=False,
)


class ListOTAUpdatesPaginateResponseTypeDef(_ListOTAUpdatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **otaUpdates** *(list) --*

        A list of OTA update jobs.
        - *(dict) --*

          An OTA update summary.
          - **otaUpdateId** *(string) --*

            The OTA update ID.
    """


_ListOutgoingCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOutgoingCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOutgoingCertificatesPaginatePaginationConfigTypeDef(
    _ListOutgoingCertificatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef = TypedDict(
    "_ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "transferredTo": str,
        "transferDate": datetime,
        "transferMessage": str,
        "creationDate": datetime,
    },
    total=False,
)


class ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef(
    _ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef
):
    """
    - *(dict) --*

      A certificate that has been transferred but not yet accepted.
      - **certificateArn** *(string) --*

        The certificate ARN.
    """


_ListOutgoingCertificatesPaginateResponseTypeDef = TypedDict(
    "_ListOutgoingCertificatesPaginateResponseTypeDef",
    {
        "outgoingCertificates": List[
            ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListOutgoingCertificatesPaginateResponseTypeDef(
    _ListOutgoingCertificatesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      The output from the ListOutgoingCertificates operation.
      - **outgoingCertificates** *(list) --*

        The certificates that are being transferred but not yet accepted.
        - *(dict) --*

          A certificate that has been transferred but not yet accepted.
          - **certificateArn** *(string) --*

            The certificate ARN.
    """


_ListPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPoliciesPaginatePaginationConfigTypeDef(_ListPoliciesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPoliciesPaginateResponsepoliciesTypeDef = TypedDict(
    "_ListPoliciesPaginateResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ListPoliciesPaginateResponsepoliciesTypeDef(_ListPoliciesPaginateResponsepoliciesTypeDef):
    """
    - *(dict) --*

      Describes an AWS IoT policy.
      - **policyName** *(string) --*

        The policy name.
    """


_ListPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListPoliciesPaginateResponseTypeDef",
    {"policies": List[ListPoliciesPaginateResponsepoliciesTypeDef], "NextToken": str},
    total=False,
)


class ListPoliciesPaginateResponseTypeDef(_ListPoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListPolicies operation.
      - **policies** *(list) --*

        The descriptions of the policies.
        - *(dict) --*

          Describes an AWS IoT policy.
          - **policyName** *(string) --*

            The policy name.
    """


_ListPolicyPrincipalsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPolicyPrincipalsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPolicyPrincipalsPaginatePaginationConfigTypeDef(
    _ListPolicyPrincipalsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPolicyPrincipalsPaginateResponseTypeDef = TypedDict(
    "_ListPolicyPrincipalsPaginateResponseTypeDef",
    {"principals": List[str], "NextToken": str},
    total=False,
)


class ListPolicyPrincipalsPaginateResponseTypeDef(_ListPolicyPrincipalsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListPolicyPrincipals operation.
      - **principals** *(list) --*

        The descriptions of the principals.
        - *(string) --*
    """


_ListPrincipalPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPrincipalPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPrincipalPoliciesPaginatePaginationConfigTypeDef(
    _ListPrincipalPoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPrincipalPoliciesPaginateResponsepoliciesTypeDef = TypedDict(
    "_ListPrincipalPoliciesPaginateResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ListPrincipalPoliciesPaginateResponsepoliciesTypeDef(
    _ListPrincipalPoliciesPaginateResponsepoliciesTypeDef
):
    """
    - *(dict) --*

      Describes an AWS IoT policy.
      - **policyName** *(string) --*

        The policy name.
    """


_ListPrincipalPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListPrincipalPoliciesPaginateResponseTypeDef",
    {"policies": List[ListPrincipalPoliciesPaginateResponsepoliciesTypeDef], "NextToken": str},
    total=False,
)


class ListPrincipalPoliciesPaginateResponseTypeDef(_ListPrincipalPoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListPrincipalPolicies operation.
      - **policies** *(list) --*

        The policies.
        - *(dict) --*

          Describes an AWS IoT policy.
          - **policyName** *(string) --*

            The policy name.
    """


_ListPrincipalThingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPrincipalThingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPrincipalThingsPaginatePaginationConfigTypeDef(
    _ListPrincipalThingsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPrincipalThingsPaginateResponseTypeDef = TypedDict(
    "_ListPrincipalThingsPaginateResponseTypeDef",
    {"things": List[str], "NextToken": str},
    total=False,
)


class ListPrincipalThingsPaginateResponseTypeDef(_ListPrincipalThingsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListPrincipalThings operation.
      - **things** *(list) --*

        The things.
        - *(string) --*
    """


_ListRoleAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRoleAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRoleAliasesPaginatePaginationConfigTypeDef(
    _ListRoleAliasesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRoleAliasesPaginateResponseTypeDef = TypedDict(
    "_ListRoleAliasesPaginateResponseTypeDef",
    {"roleAliases": List[str], "NextToken": str},
    total=False,
)


class ListRoleAliasesPaginateResponseTypeDef(_ListRoleAliasesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **roleAliases** *(list) --*

        The role aliases.
        - *(string) --*
    """


_ListScheduledAuditsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListScheduledAuditsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListScheduledAuditsPaginatePaginationConfigTypeDef(
    _ListScheduledAuditsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef = TypedDict(
    "_ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef",
    {
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
        "frequency": Literal["DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY"],
        "dayOfMonth": str,
        "dayOfWeek": Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"],
    },
    total=False,
)


class ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef(
    _ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef
):
    """
    - *(dict) --*

      Information about the scheduled audit.
      - **scheduledAuditName** *(string) --*

        The name of the scheduled audit.
    """


_ListScheduledAuditsPaginateResponseTypeDef = TypedDict(
    "_ListScheduledAuditsPaginateResponseTypeDef",
    {
        "scheduledAudits": List[ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListScheduledAuditsPaginateResponseTypeDef(_ListScheduledAuditsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **scheduledAudits** *(list) --*

        The list of scheduled audits.
        - *(dict) --*

          Information about the scheduled audit.
          - **scheduledAuditName** *(string) --*

            The name of the scheduled audit.
    """


_ListSecurityProfilesForTargetPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSecurityProfilesForTargetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSecurityProfilesForTargetPaginatePaginationConfigTypeDef(
    _ListSecurityProfilesForTargetPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef = TypedDict(
    "_ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef",
    {"name": str, "arn": str},
    total=False,
)


class ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef(
    _ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef
):
    """
    - **securityProfileIdentifier** *(dict) --*

      Information that identifies the security profile.
      - **name** *(string) --*

        The name you have given to the security profile.
    """


_ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef = TypedDict(
    "_ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef",
    {"arn": str},
    total=False,
)


class ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef(
    _ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef
):
    pass


_ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef = TypedDict(
    "_ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef",
    {
        "securityProfileIdentifier": ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef,
        "target": ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef,
    },
    total=False,
)


class ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef(
    _ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef
):
    """
    - *(dict) --*

      Information about a security profile and the target associated with it.
      - **securityProfileIdentifier** *(dict) --*

        Information that identifies the security profile.
        - **name** *(string) --*

          The name you have given to the security profile.
    """


_ListSecurityProfilesForTargetPaginateResponseTypeDef = TypedDict(
    "_ListSecurityProfilesForTargetPaginateResponseTypeDef",
    {
        "securityProfileTargetMappings": List[
            ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListSecurityProfilesForTargetPaginateResponseTypeDef(
    _ListSecurityProfilesForTargetPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **securityProfileTargetMappings** *(list) --*

        A list of security profiles and their associated targets.
        - *(dict) --*

          Information about a security profile and the target associated with it.
          - **securityProfileIdentifier** *(dict) --*

            Information that identifies the security profile.
            - **name** *(string) --*

              The name you have given to the security profile.
    """


_ListSecurityProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSecurityProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSecurityProfilesPaginatePaginationConfigTypeDef(
    _ListSecurityProfilesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef = TypedDict(
    "_ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef",
    {"name": str, "arn": str},
    total=False,
)


class ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef(
    _ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef
):
    """
    - *(dict) --*

      Identifying information for a Device Defender security profile.
      - **name** *(string) --*

        The name you have given to the security profile.
    """


_ListSecurityProfilesPaginateResponseTypeDef = TypedDict(
    "_ListSecurityProfilesPaginateResponseTypeDef",
    {
        "securityProfileIdentifiers": List[
            ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListSecurityProfilesPaginateResponseTypeDef(_ListSecurityProfilesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **securityProfileIdentifiers** *(list) --*

        A list of security profile identifiers (names and ARNs).
        - *(dict) --*

          Identifying information for a Device Defender security profile.
          - **name** *(string) --*

            The name you have given to the security profile.
    """


_ListStreamsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStreamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStreamsPaginatePaginationConfigTypeDef(_ListStreamsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListStreamsPaginateResponsestreamsTypeDef = TypedDict(
    "_ListStreamsPaginateResponsestreamsTypeDef",
    {"streamId": str, "streamArn": str, "streamVersion": int, "description": str},
    total=False,
)


class ListStreamsPaginateResponsestreamsTypeDef(_ListStreamsPaginateResponsestreamsTypeDef):
    """
    - *(dict) --*

      A summary of a stream.
      - **streamId** *(string) --*

        The stream ID.
    """


_ListStreamsPaginateResponseTypeDef = TypedDict(
    "_ListStreamsPaginateResponseTypeDef",
    {"streams": List[ListStreamsPaginateResponsestreamsTypeDef], "NextToken": str},
    total=False,
)


class ListStreamsPaginateResponseTypeDef(_ListStreamsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **streams** *(list) --*

        A list of streams.
        - *(dict) --*

          A summary of a stream.
          - **streamId** *(string) --*

            The stream ID.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsForResourcePaginateResponsetagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponsetagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsForResourcePaginateResponsetagsTypeDef(
    _ListTagsForResourcePaginateResponsetagsTypeDef
):
    """
    - *(dict) --*

      A set of key/value pairs that are used to manage the resource.
      - **Key** *(string) --*

        The tag's key.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"tags": List[ListTagsForResourcePaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(_ListTagsForResourcePaginateResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        The list of tags assigned to the resource.
        - *(dict) --*

          A set of key/value pairs that are used to manage the resource.
          - **Key** *(string) --*

            The tag's key.
    """


_ListTargetsForPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTargetsForPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTargetsForPolicyPaginatePaginationConfigTypeDef(
    _ListTargetsForPolicyPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTargetsForPolicyPaginateResponseTypeDef = TypedDict(
    "_ListTargetsForPolicyPaginateResponseTypeDef",
    {"targets": List[str], "NextToken": str},
    total=False,
)


class ListTargetsForPolicyPaginateResponseTypeDef(_ListTargetsForPolicyPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **targets** *(list) --*

        The policy targets.
        - *(string) --*
    """


_ListTargetsForSecurityProfilePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTargetsForSecurityProfilePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTargetsForSecurityProfilePaginatePaginationConfigTypeDef(
    _ListTargetsForSecurityProfilePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef = TypedDict(
    "_ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef",
    {"arn": str},
    total=False,
)


class ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef(
    _ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef
):
    """
    - *(dict) --*

      A target to which an alert is sent when a security profile behavior is violated.
      - **arn** *(string) --*

        The ARN of the security profile.
    """


_ListTargetsForSecurityProfilePaginateResponseTypeDef = TypedDict(
    "_ListTargetsForSecurityProfilePaginateResponseTypeDef",
    {
        "securityProfileTargets": List[
            ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListTargetsForSecurityProfilePaginateResponseTypeDef(
    _ListTargetsForSecurityProfilePaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **securityProfileTargets** *(list) --*

        The thing groups to which the security profile is attached.
        - *(dict) --*

          A target to which an alert is sent when a security profile behavior is violated.
          - **arn** *(string) --*

            The ARN of the security profile.
    """


_ListThingGroupsForThingPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingGroupsForThingPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingGroupsForThingPaginatePaginationConfigTypeDef(
    _ListThingGroupsForThingPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListThingGroupsForThingPaginateResponsethingGroupsTypeDef = TypedDict(
    "_ListThingGroupsForThingPaginateResponsethingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ListThingGroupsForThingPaginateResponsethingGroupsTypeDef(
    _ListThingGroupsForThingPaginateResponsethingGroupsTypeDef
):
    """
    - *(dict) --*

      The name and ARN of a group.
      - **groupName** *(string) --*

        The group name.
    """


_ListThingGroupsForThingPaginateResponseTypeDef = TypedDict(
    "_ListThingGroupsForThingPaginateResponseTypeDef",
    {
        "thingGroups": List[ListThingGroupsForThingPaginateResponsethingGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListThingGroupsForThingPaginateResponseTypeDef(
    _ListThingGroupsForThingPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **thingGroups** *(list) --*

        The thing groups.
        - *(dict) --*

          The name and ARN of a group.
          - **groupName** *(string) --*

            The group name.
    """


_ListThingGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingGroupsPaginatePaginationConfigTypeDef(
    _ListThingGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListThingGroupsPaginateResponsethingGroupsTypeDef = TypedDict(
    "_ListThingGroupsPaginateResponsethingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ListThingGroupsPaginateResponsethingGroupsTypeDef(
    _ListThingGroupsPaginateResponsethingGroupsTypeDef
):
    """
    - *(dict) --*

      The name and ARN of a group.
      - **groupName** *(string) --*

        The group name.
    """


_ListThingGroupsPaginateResponseTypeDef = TypedDict(
    "_ListThingGroupsPaginateResponseTypeDef",
    {"thingGroups": List[ListThingGroupsPaginateResponsethingGroupsTypeDef], "NextToken": str},
    total=False,
)


class ListThingGroupsPaginateResponseTypeDef(_ListThingGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **thingGroups** *(list) --*

        The thing groups.
        - *(dict) --*

          The name and ARN of a group.
          - **groupName** *(string) --*

            The group name.
    """


_ListThingRegistrationTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingRegistrationTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingRegistrationTasksPaginatePaginationConfigTypeDef(
    _ListThingRegistrationTasksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListThingRegistrationTasksPaginateResponseTypeDef = TypedDict(
    "_ListThingRegistrationTasksPaginateResponseTypeDef",
    {"taskIds": List[str], "NextToken": str},
    total=False,
)


class ListThingRegistrationTasksPaginateResponseTypeDef(
    _ListThingRegistrationTasksPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **taskIds** *(list) --*

        A list of bulk thing provisioning task IDs.
        - *(string) --*
    """


_ListThingTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingTypesPaginatePaginationConfigTypeDef(_ListThingTypesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef = TypedDict(
    "_ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef",
    {"deprecated": bool, "deprecationDate": datetime, "creationDate": datetime},
    total=False,
)


class ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef(
    _ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef
):
    pass


_ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef = TypedDict(
    "_ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef",
    {"thingTypeDescription": str, "searchableAttributes": List[str]},
    total=False,
)


class ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef(
    _ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef
):
    pass


_ListThingTypesPaginateResponsethingTypesTypeDef = TypedDict(
    "_ListThingTypesPaginateResponsethingTypesTypeDef",
    {
        "thingTypeName": str,
        "thingTypeArn": str,
        "thingTypeProperties": ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef,
        "thingTypeMetadata": ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef,
    },
    total=False,
)


class ListThingTypesPaginateResponsethingTypesTypeDef(
    _ListThingTypesPaginateResponsethingTypesTypeDef
):
    """
    - *(dict) --*

      The definition of the thing type, including thing type name and description.
      - **thingTypeName** *(string) --*

        The name of the thing type.
    """


_ListThingTypesPaginateResponseTypeDef = TypedDict(
    "_ListThingTypesPaginateResponseTypeDef",
    {"thingTypes": List[ListThingTypesPaginateResponsethingTypesTypeDef], "NextToken": str},
    total=False,
)


class ListThingTypesPaginateResponseTypeDef(_ListThingTypesPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output for the ListThingTypes operation.
      - **thingTypes** *(list) --*

        The thing types.
        - *(dict) --*

          The definition of the thing type, including thing type name and description.
          - **thingTypeName** *(string) --*

            The name of the thing type.
    """


_ListThingsInBillingGroupPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingsInBillingGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingsInBillingGroupPaginatePaginationConfigTypeDef(
    _ListThingsInBillingGroupPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListThingsInBillingGroupPaginateResponseTypeDef = TypedDict(
    "_ListThingsInBillingGroupPaginateResponseTypeDef",
    {"things": List[str], "NextToken": str},
    total=False,
)


class ListThingsInBillingGroupPaginateResponseTypeDef(
    _ListThingsInBillingGroupPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **things** *(list) --*

        A list of things in the billing group.
        - *(string) --*
    """


_ListThingsInThingGroupPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingsInThingGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingsInThingGroupPaginatePaginationConfigTypeDef(
    _ListThingsInThingGroupPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListThingsInThingGroupPaginateResponseTypeDef = TypedDict(
    "_ListThingsInThingGroupPaginateResponseTypeDef",
    {"things": List[str], "NextToken": str},
    total=False,
)


class ListThingsInThingGroupPaginateResponseTypeDef(_ListThingsInThingGroupPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **things** *(list) --*

        The things in the specified thing group.
        - *(string) --*
    """


_ListThingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingsPaginatePaginationConfigTypeDef(_ListThingsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListThingsPaginateResponsethingsTypeDef = TypedDict(
    "_ListThingsPaginateResponsethingsTypeDef",
    {
        "thingName": str,
        "thingTypeName": str,
        "thingArn": str,
        "attributes": Dict[str, str],
        "version": int,
    },
    total=False,
)


class ListThingsPaginateResponsethingsTypeDef(_ListThingsPaginateResponsethingsTypeDef):
    """
    - *(dict) --*

      The properties of the thing, including thing name, thing type name, and a list of thing
      attributes.
      - **thingName** *(string) --*

        The name of the thing.
    """


_ListThingsPaginateResponseTypeDef = TypedDict(
    "_ListThingsPaginateResponseTypeDef",
    {"things": List[ListThingsPaginateResponsethingsTypeDef], "NextToken": str},
    total=False,
)


class ListThingsPaginateResponseTypeDef(_ListThingsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListThings operation.
      - **things** *(list) --*

        The things.
        - *(dict) --*

          The properties of the thing, including thing name, thing type name, and a list of thing
          attributes.
          - **thingName** *(string) --*

            The name of the thing.
    """


_ListTopicRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTopicRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTopicRulesPaginatePaginationConfigTypeDef(_ListTopicRulesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTopicRulesPaginateResponserulesTypeDef = TypedDict(
    "_ListTopicRulesPaginateResponserulesTypeDef",
    {
        "ruleArn": str,
        "ruleName": str,
        "topicPattern": str,
        "createdAt": datetime,
        "ruleDisabled": bool,
    },
    total=False,
)


class ListTopicRulesPaginateResponserulesTypeDef(_ListTopicRulesPaginateResponserulesTypeDef):
    """
    - *(dict) --*

      Describes a rule.
      - **ruleArn** *(string) --*

        The rule ARN.
    """


_ListTopicRulesPaginateResponseTypeDef = TypedDict(
    "_ListTopicRulesPaginateResponseTypeDef",
    {"rules": List[ListTopicRulesPaginateResponserulesTypeDef], "NextToken": str},
    total=False,
)


class ListTopicRulesPaginateResponseTypeDef(_ListTopicRulesPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output from the ListTopicRules operation.
      - **rules** *(list) --*

        The rules.
        - *(dict) --*

          Describes a rule.
          - **ruleArn** *(string) --*

            The rule ARN.
    """


_ListV2LoggingLevelsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListV2LoggingLevelsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListV2LoggingLevelsPaginatePaginationConfigTypeDef(
    _ListV2LoggingLevelsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef = TypedDict(
    "_ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef",
    {"targetType": Literal["DEFAULT", "THING_GROUP"], "targetName": str},
    total=False,
)


class ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef(
    _ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef
):
    """
    - **logTarget** *(dict) --*

      A log target
      - **targetType** *(string) --*

        The target type.
    """


_ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef = TypedDict(
    "_ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef",
    {
        "logTarget": ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef,
        "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"],
    },
    total=False,
)


class ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef(
    _ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef
):
    """
    - *(dict) --*

      The target configuration.
      - **logTarget** *(dict) --*

        A log target
        - **targetType** *(string) --*

          The target type.
    """


_ListV2LoggingLevelsPaginateResponseTypeDef = TypedDict(
    "_ListV2LoggingLevelsPaginateResponseTypeDef",
    {
        "logTargetConfigurations": List[
            ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListV2LoggingLevelsPaginateResponseTypeDef(_ListV2LoggingLevelsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **logTargetConfigurations** *(list) --*

        The logging configuration for a target.
        - *(dict) --*

          The target configuration.
          - **logTarget** *(dict) --*

            A log target
            - **targetType** *(string) --*

              The target type.
    """


_ListViolationEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListViolationEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListViolationEventsPaginatePaginationConfigTypeDef(
    _ListViolationEventsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef(
    _ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef
):
    pass


_ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef(
    _ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef
):
    pass


_ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef(
    _ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef
):
    pass


_ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef,
    },
    total=False,
)


class ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef(
    _ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef
):
    pass


_ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef(
    _ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef
):
    pass


_ListViolationEventsPaginateResponseviolationEventsTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseviolationEventsTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef,
        "metricValue": ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef,
        "violationEventType": Literal["in-alarm", "alarm-cleared", "alarm-invalidated"],
        "violationEventTime": datetime,
    },
    total=False,
)


class ListViolationEventsPaginateResponseviolationEventsTypeDef(
    _ListViolationEventsPaginateResponseviolationEventsTypeDef
):
    """
    - *(dict) --*

      Information about a Device Defender security profile behavior violation.
      - **violationId** *(string) --*

        The ID of the violation event.
    """


_ListViolationEventsPaginateResponseTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseTypeDef",
    {
        "violationEvents": List[ListViolationEventsPaginateResponseviolationEventsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListViolationEventsPaginateResponseTypeDef(_ListViolationEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **violationEvents** *(list) --*

        The security profile violation alerts issued for this account during the given time period,
        potentially filtered by security profile, behavior violated, or thing (device) violating.
        - *(dict) --*

          Information about a Device Defender security profile behavior violation.
          - **violationId** *(string) --*

            The ID of the violation event.
    """
